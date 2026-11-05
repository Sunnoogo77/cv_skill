#!/usr/bin/env python3
"""
Controle d'un CV produit en PDF.

Ce script ne juge pas le fond : il attrape les defauts qui passent inapercus
a la relecture parce qu'ils ne se voient pas a l'ecran. Un CV dont le texte
n'est pas extractible est illisible par la moitie des logiciels de
recrutement, et rien dans l'apercu ne le montre. Un gabarit dont une mention
d'exemple est restee compile parfaitement. Un lien mort s'affiche en bleu
comme les autres.

Usage :
    python3 verifier.py CV.pdf
    python3 verifier.py CV.pdf --liens          verifie aussi les adresses web
    python3 verifier.py CV.pdf --pages 1        exige une seule page

Sortie : une ligne par constat. Code de retour 1 s'il reste une ERREUR.
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

# Restes de gabarit : leur presence signifie qu'une zone n'a pas ete remplie.
RESTES = [
    "Prenom NOM", "Prénom NOM", "prenom.nom@exemple",
    "exemple.fr", "exemple.png", "identifiant",
    "TODO", "XXX", "lorem ipsum", "Ville, Region", "Ville, Région",
]

# Formules qui occupent de la place sans rien prouver. La liste est courte a
# dessein : elle vise les tournures qui reviennent partout, pas le style.
CREUX_FR = [
    "passionné par", "passionnée par", "dynamique et motivé", "esprit d'équipe",
    "bonne communication", "rigoureux et autonome", "force de proposition",
    "polyvalent", "à l'écoute", "sens du relationnel", "maîtrise parfaite",
    "excellente maîtrise", "très bon niveau",
]
CREUX_EN = [
    "passionate about", "team player", "hard worker", "detail-oriented",
    "results-driven", "self-starter", "think outside the box",
    "excellent communication skills", "proven track record",
]

# Mentions qui affirment une obtention. Le script ne peut pas savoir si c'est
# vrai ; il les liste pour que la personne les relise une par une.
AFFIRMATIONS = [
    "certifié", "certifiée", "certified", "obtenu", "obtenue", "diplômé",
    "diplômée", "graduated", "lauréat",
]


def extraire(pdf: Path) -> tuple[str, int]:
    """Rend le texte du PDF et son nombre de pages, par le premier outil
    disponible. Rien n'est installe pour l'occasion : si aucun n'est la, le
    script le dit plutot que d'echouer dans le vide."""
    if shutil.which("pdftotext"):
        texte = subprocess.run(
            ["pdftotext", "-layout", str(pdf), "-"],
            capture_output=True, text=True, check=True,
        ).stdout
        info = subprocess.run(
            ["pdfinfo", str(pdf)], capture_output=True, text=True,
        ).stdout
        pages = 0
        for ligne in info.splitlines():
            if ligne.startswith("Pages:"):
                pages = int(ligne.split()[1])
        return texte, pages

    try:
        from pypdf import PdfReader  # type: ignore
    except ImportError:
        try:
            from PyPDF2 import PdfReader  # type: ignore
        except ImportError:
            PdfReader = None  # type: ignore

    if PdfReader is not None:
        lecteur = PdfReader(str(pdf))
        texte = "\n".join((p.extract_text() or "") for p in lecteur.pages)
        return texte, len(lecteur.pages)

    # Dernier recours sur macOS : PDFKit via swift, present des que les outils
    # de ligne de commande Xcode le sont. Cela evite d'imposer une installation
    # a quelqu'un qui veut seulement relire son CV.
    if sys.platform == "darwin" and shutil.which("swift"):
        code = (
            "import PDFKit\nimport Foundation\n"
            "let u = URL(fileURLWithPath: CommandLine.arguments[1])\n"
            "guard let d = PDFDocument(url: u) else { exit(3) }\n"
            'FileHandle.standardError.write("PAGES:\\(d.pageCount)\\n"'
            ".data(using: .utf8)!)\n"
            'print(d.string ?? "")\n'
        )
        import tempfile

        with tempfile.NamedTemporaryFile("w", suffix=".swift", delete=False) as f:
            f.write(code)
            chemin = f.name
        resultat = subprocess.run(
            ["swift", chemin, str(pdf)], capture_output=True, text=True,
        )
        Path(chemin).unlink(missing_ok=True)
        if resultat.returncode == 0:
            pages = 0
            for ligne in resultat.stderr.splitlines():
                if ligne.startswith("PAGES:"):
                    pages = int(ligne.split(":")[1])
            return resultat.stdout, pages

    print(
        "Aucun outil d'extraction trouve. Installer l'un des deux :\n"
        "  brew install poppler        (fournit pdftotext)\n"
        "  pip install pypdf",
        file=sys.stderr,
    )
    sys.exit(2)


def verifier_liens(texte: str) -> list[str]:
    """Verifie que chaque adresse citee repond. Un lien mort sur un CV coute
    plus cher que l'absence de lien : il donne au recruteur la preuve que
    personne n'a relu."""
    import urllib.error
    import urllib.request

    constats = []
    urls = sorted(set(re.findall(r"https?://[^\s,;)\]}<>\"']+", texte)))
    for url in urls:
        url = url.rstrip(".")
        requete = urllib.request.Request(
            url, method="HEAD",
            headers={"User-Agent": "verification-cv/1.0"},
        )
        try:
            with urllib.request.urlopen(requete, timeout=12) as reponse:
                code = reponse.status
            constats.append(
                f"  ok     {url}" if code < 400 else f"  ERREUR {url} repond {code}"
            )
        except urllib.error.HTTPError as e:
            # 403 et 405 viennent souvent du refus de HEAD, pas d'un lien mort.
            if e.code in (403, 405):
                constats.append(f"  a voir {url} repond {e.code}, a ouvrir a la main")
            else:
                constats.append(f"  ERREUR {url} repond {e.code}")
        except Exception as e:  # reseau, DNS, delai
            constats.append(f"  ERREUR {url} injoignable ({type(e).__name__})")
    return constats


def main() -> int:
    parseur = argparse.ArgumentParser(description=__doc__)
    parseur.add_argument("pdf", type=Path)
    parseur.add_argument("--liens", action="store_true",
                         help="verifier que les adresses web repondent")
    parseur.add_argument("--pages", type=int, default=2,
                         help="nombre de pages attendu au maximum (defaut 2)")
    args = parseur.parse_args()

    if not args.pdf.exists():
        print(f"ERREUR  fichier introuvable : {args.pdf}")
        return 1

    texte, pages = extraire(args.pdf)
    bas = texte.lower()
    erreurs = 0

    print(f"Controle de {args.pdf.name}")
    print(f"  {pages} page(s), {len(texte)} caracteres extraits, "
          f"{args.pdf.stat().st_size // 1024} ko")

    # Un CV dont on extrait trois cents caracteres est une image. Il sera
    # illisible par tout logiciel qui lit le texte, et par un lecteur d'ecran.
    if len(texte) < 800:
        print("  ERREUR  le texte n'est quasiment pas extractible. Le CV est "
              "probablement une image : il ne sera lu ni par les logiciels de "
              "recrutement ni par un lecteur d'ecran.")
        erreurs += 1

    if pages > args.pages:
        print(f"  ERREUR  {pages} pages pour {args.pages} attendues.")
        erreurs += 1

    trouves = [r for r in RESTES if r.lower() in bas]
    if trouves:
        print(f"  ERREUR  restes de gabarit : {', '.join(trouves)}")
        erreurs += 1

    creux = [c for c in CREUX_FR + CREUX_EN if c in bas]
    if creux:
        print(f"  a voir  formules sans preuve : {', '.join(creux)}")
        print("          chacune peut etre remplacee par un fait verifiable.")

    # Un CV sans chiffre n'est pas fautif, mais c'est presque toujours le
    # signe que les realisations sont restees a l'etat de missions.
    chiffres = re.findall(r"\b\d[\d  ,. ]*\b", texte)
    if len(chiffres) < 5:
        print("  a voir  tres peu de chiffres. Les resultats sont-ils tous "
              "qualitatifs, ou manquent-ils ?")

    if "@" not in texte:
        print("  ERREUR  aucune adresse de courriel trouvee.")
        erreurs += 1

    affirme = [a for a in AFFIRMATIONS if a in bas]
    if affirme:
        print(f"  a relire mentions d'obtention a verifier une par une : "
              f"{', '.join(affirme)}")

    if args.liens:
        print("  Adresses :")
        for ligne in verifier_liens(texte):
            print(ligne)
            if "ERREUR" in ligne:
                erreurs += 1

    print("  Aucun defaut bloquant." if erreurs == 0
          else f"  {erreurs} defaut(s) a corriger.")
    return 1 if erreurs else 0


if __name__ == "__main__":
    sys.exit(main())
