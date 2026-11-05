#!/usr/bin/env python3
"""
Recupere les logos de technologies depuis Simple Icons et les prepare pour
LaTeX.

Simple Icons publie ses fichiers sous CC0, c'est-a-dire sans condition de
reutilisation. Les marques representees restent la propriete de leurs
titulaires : les citer pour dire quels outils on a employes est un usage
descriptif, legitime, et c'est le seul usage prevu ici.

Ce script ne sert QUE pour les technologies. Le logo d'un employeur ou d'une
ecole ne se recupere pas ici : il vient du site de l'organisation, de son kit
de marque, et il n'y a pas de source automatique fiable pour cela. Quand on
ne le trouve pas, on n'en met pas. Un logo approximatif, redessine ou pris
sur un agregateur est pire que pas de logo du tout : il se voit, et il dit au
recruteur que le reste du CV a ete fait avec la meme legerete.

Usage :
    python3 logos.py python docker postgresql        telecharge trois logos
    python3 logos.py --dossier src/logos python      choisit le dossier
    python3 logos.py --liste                         rappelle comment chercher un slug

Les fichiers sont ecrits en PNG a 512 pixels de haut, fond transparent, prets
pour \\marque{nom.png}{0.40cm}.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

CDN = "https://cdn.jsdelivr.net/npm/simple-icons@latest/icons/{slug}.svg"


def telecharger_svg(slug: str) -> bytes | None:
    requete = urllib.request.Request(
        CDN.format(slug=slug),
        headers={"User-Agent": "recuperation-logos-cv/1.0"},
    )
    try:
        with urllib.request.urlopen(requete, timeout=20) as reponse:
            return reponse.read()
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise


def convertir(svg: bytes, sortie: Path, hauteur: int = 512) -> bool:
    """Convertit en PNG par le premier outil disponible. LaTeX avec graphicx
    n'inclut pas de SVG directement, d'ou la conversion."""
    temporaire = sortie.with_suffix(".svg")
    temporaire.write_bytes(svg)

    if shutil.which("rsvg-convert"):
        subprocess.run(
            ["rsvg-convert", "-h", str(hauteur), str(temporaire), "-o", str(sortie)],
            check=True,
        )
        temporaire.unlink()
        return True

    try:
        import cairosvg  # type: ignore

        cairosvg.svg2png(bytestring=svg, write_to=str(sortie),
                         output_height=hauteur)
        temporaire.unlink()
        return True
    except ImportError:
        pass

    if shutil.which("inkscape"):
        subprocess.run(
            ["inkscape", str(temporaire), "-h", str(hauteur),
             "-o", str(sortie)],
            check=True, capture_output=True,
        )
        temporaire.unlink()
        return True

    print(f"  Le SVG est conserve ({temporaire.name}) : aucun convertisseur "
          f"trouve.\n  Installer l'un des deux : brew install librsvg  |  "
          f"pip install cairosvg")
    return False


def main() -> int:
    parseur = argparse.ArgumentParser(description=__doc__)
    parseur.add_argument("slugs", nargs="*",
                         help="identifiants Simple Icons, par exemple python docker")
    parseur.add_argument("--dossier", type=Path, default=Path("src/logos"))
    parseur.add_argument("--hauteur", type=int, default=512)
    parseur.add_argument("--liste", action="store_true",
                         help="rappelle comment trouver un identifiant")
    args = parseur.parse_args()

    if args.liste or not args.slugs:
        print(
            "Les identifiants se cherchent sur https://simpleicons.org .\n"
            "Ce sont les noms en minuscules, sans espace ni point :\n"
            "  python  docker  postgresql  githubactions  microsoftazure\n"
            "  terraform  kubernetes  react  figma  salesforce  autodesk\n"
            "Beaucoup d'outils specialises n'y figurent pas. Dans ce cas,\n"
            "la technologie s'ecrit en toutes lettres : c'est parfaitement\n"
            "lisible, et c'est preferable a un logo fabrique."
        )
        return 0

    args.dossier.mkdir(parents=True, exist_ok=True)
    manquants = []

    for slug in args.slugs:
        slug = slug.lower().strip()
        sortie = args.dossier / f"{slug}.png"
        svg = telecharger_svg(slug)
        if svg is None:
            manquants.append(slug)
            print(f"  absent   {slug}")
            continue
        if convertir(svg, sortie, args.hauteur):
            print(f"  ecrit    {sortie}")

    if manquants:
        print(
            f"\n{len(manquants)} logo(s) introuvable(s) : {', '.join(manquants)}.\n"
            "Ces technologies s'ecrivent en toutes lettres dans le CV. "
            "Ne pas en fabriquer un."
        )

    licence = args.dossier / "LICENCES.md"
    if not licence.exists():
        licence.write_text(
            "# Origine des logos\n\n"
            "Les logos de technologies viennent de Simple Icons "
            "(https://simpleicons.org), publies sous CC0 1.0.\n\n"
            "Les marques representees appartiennent a leurs titulaires. "
            "Elles sont citees ici dans un usage strictement descriptif : "
            "indiquer les outils employes. Aucune affiliation ni "
            "approbation n'est suggeree.\n\n"
            "Les logos d'employeurs et d'etablissements ne proviennent pas "
            "de cette source. Chacun doit venir du site officiel de "
            "l'organisation concernee.\n",
            encoding="utf-8",
        )
        print(f"  ecrit    {licence}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
