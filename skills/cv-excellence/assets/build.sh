#!/bin/bash
# ==========================================================================
# Produit toutes les variantes d'un CV a partir d'une source unique.
#
# Pourquoi un script plutot que des copies du fichier : des que deux fichiers
# portent le meme parcours, ils divergent. Une correction faite sur l'un est
# oubliee sur l'autre, et le candidat envoie un CV corrige a l'un et fautif a
# l'autre sans le savoir. Une source, des drapeaux, un script.
#
# Pourquoi la verification apres sed : si un motif ne correspond a rien, sed
# ne proteste pas. Le PDF se compile, il est propre, et il porte la mauvaise
# variante. Le candidat postule en CDI avec un CV de stage. Le `grep -qx`
# apres chaque bascule est la seule chose qui attrape cela.
# ==========================================================================
set -e
cd "$(dirname "$0")"

# tectonic telecharge ce dont il a besoin et ne demande aucune distribution
# TeX installee. A defaut, xelatex convient : le preambule utilise fontspec,
# donc ni pdflatex ni latex ne compileront ce document.
TEC=${TEC:-tectonic}
command -v "$TEC" >/dev/null || {
  echo "tectonic est introuvable. Installer avec : brew install tectonic"
  echo "ou poser TEC=/chemin/vers/xelatex"
  exit 1
}

cd src

# gen <source> <sortie> <sed photo> <sed variante> <drapeaux attendus...>
gen () {
  local source="$1" sortie="$2"
  sed -e "$3" -e "$4" "$source" > "_b.tex"
  shift 4
  for drapeau in "$@"; do
    grep -qx -- "$drapeau" _b.tex || {
      echo "ECHEC : $drapeau absent apres bascule. La variante n'a pas pris."
      rm -f _b.tex
      exit 1
    }
  done
  mkdir -p "$(dirname "../$sortie")"
  # La sortie de tectonic n'est montree qu'en cas d'echec : un build qui
  # reussit n'a rien a dire, un build qui echoue doit dire pourquoi.
  if ! journal=$("$TEC" --keep-logs=false --print=false _b.tex 2>&1); then
    echo "ECHEC de compilation pour $sortie :"
    echo "$journal" | tail -20
    rm -f _b.tex
    exit 1
  fi
  mv _b.pdf "../$sortie"
  rm -f _b.tex
  echo "  $sortie"
}

# La photo est facultative. Sans fichier, les variantes avec photo sont
# simplement sautees : une personne qui n'a pas encore sa photo doit pouvoir
# produire son CV tout de suite.
avec_photo=oui
if [ ! -f photo.jpg ]; then
  avec_photo=non
  echo "Note : src/photo.jpg est absent, les variantes avec photo sont sautees."
fi

P_ON='s/^\\photofalse/\\phototrue/'
P_OFF='s/^\\phototrue/\\photofalse/'
V_POSTE='s/^\\stagetrue/\\stagefalse/; s/^\\postefalse/\\postetrue/'
V_STAGE='s/^\\postetrue/\\postefalse/; s/^\\stagefalse/\\stagetrue/'

echo "Production des variantes :"
gen cv.tex "Poste/CV_NOM_poste.pdf"       "$P_OFF" "$V_POSTE" '\\photofalse' '\\postetrue'  '\\stagefalse'
gen cv.tex "Stage/CV_NOM_stage.pdf"       "$P_OFF" "$V_STAGE" '\\photofalse' '\\postefalse' '\\stagetrue'

if [ "$avec_photo" = oui ]; then
  gen cv.tex "Poste/CV_NOM_poste_photo.pdf" "$P_ON" "$V_POSTE" '\\phototrue' '\\postetrue'  '\\stagefalse'
  gen cv.tex "Stage/CV_NOM_stage_photo.pdf" "$P_ON" "$V_STAGE" '\\phototrue' '\\postefalse' '\\stagetrue'
fi

echo "Termine."
