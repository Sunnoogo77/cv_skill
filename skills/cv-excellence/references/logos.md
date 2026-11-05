# Les logos

Un CV avec des logos justes se retient mieux qu'un CV sans. L'œil reconnaît une
marque avant de lire son nom, et la page cesse d'être un mur de texte. Un CV
avec des logos approximatifs produit l'effet exactement inverse : un logo
déformé, pixellisé ou redessiné se voit immédiatement et dit au lecteur que le
reste a été fait avec la même légèreté.

**La personne décide.** Proposer, montrer le rendu, accepter un refus. Certains
secteurs et certains cabinets attendent un document strictement typographique.

## Trois familles, trois sources

### Les technologies et les outils

`scripts/logos.py` les récupère depuis **Simple Icons**, publié sous CC0 — donc
sans condition de réutilisation.

```bash
python3 <compétence>/scripts/logos.py python docker terraform postgresql --dossier src/logos
```

Les identifiants se cherchent sur simpleicons.org : minuscules, sans espace
(`githubactions`, `microsoftazure`, `visualstudiocode`).

Beaucoup d'outils spécialisés n'y figurent pas — c'est le cas d'une grande part
de l'outillage de sécurité, de nombreux logiciels métier et de la plupart des
progiciels sectoriels. **Dans ce cas la technologie s'écrit en toutes lettres.**
Un nom en gras est parfaitement lisible ; un logo fabriqué pour combler le trou
ne l'est pas.

### Les employeurs et les écoles

Pas de source automatique fiable. Le fichier vient du **site officiel de
l'organisation** : page « presse », « kit de marque », « identité visuelle », ou
à défaut le logo du site lui-même en bonne définition.

Ce qu'on ne fait pas : prendre le logo sur un agrégateur d'images, le
reconstituer, le vectoriser à la main, en choisir un qui ressemble. Si le logo
reste introuvable — c'est fréquent pour les PME, les entreprises non cotées et
certaines structures hors d'Europe —, **la ligne se passe de logo**. L'absence
ne se remarque pas ; une approximation, si.

### La photo du candidat

Ni un logo ni un détail. Voir `references/ats-et-forme.md` pour la règle du
pays, et ci-dessous pour le cadrage.

## Ce que dit le droit, en bref

Citer la marque d'un outil pour indiquer qu'on l'a employé est un **usage
descriptif**, et c'est légitime : personne ne peut interdire à un candidat
d'écrire qu'il travaille avec tel logiciel.

Deux limites à connaître :

- **Ne pas suggérer une affiliation ou une approbation.** Le logo d'une
  entreprise à côté d'une expérience qu'on y a réellement menée ne pose pas de
  problème. Le même logo posé en bandeau décoratif, oui.
- **Certaines bibliothèques d'icônes ont une licence restrictive.** Les jeux
  d'icônes d'architecture publiés par les grands éditeurs de cloud, par exemple,
  n'autorisent souvent leur usage que dans des schémas d'architecture, ce qui
  exclut un CV. Lire la licence avant de prendre un fichier dans un tel jeu.

Le script dépose un fichier `LICENCES.md` à côté des images qui rappelle
l'origine et la nature de l'usage. Le garder.

## La mise en page

Deux commandes, pour deux usages différents.

### `\marque{fichier.png}{hauteur}` — logo en ligne

Dans un intitulé de poste ou de projet, à côté du texte.

```latex
\poste{Consultant sécurité \quad\marque{wazuh.png}{0.40cm}}
      {Client, secteur}{juin – juillet 2026}{Ville}
```

**La hauteur se règle logo par logo**, et c'est volontaire : à hauteur égale, un
logo carré paraît deux fois plus présent qu'un logo large. Valeurs de départ :
`0.40cm` pour un logo carré, `0.44cm` à `0.48cm` pour un logo large, `0.60cm`
pour un pictogramme fin. Puis compiler, regarder, ajuster. C'est un réglage à
l'œil, il n'y a pas de formule.

Deux ou trois logos sur une même ligne se séparent par `\,\,` :

```latex
\marque{azure.png}{0.40cm}\,\,\marque{terraform.png}{0.44cm}\,\,\marque{github-mark.png}{0.42cm}
```

Au-delà de trois, la ligne devient une frise et l'intitulé disparaît.

### `\ecusson{fichier.png}` — logo d'établissement

Dans la rubrique formation, via `\form`. La boîte est fixe, 1,6 cm sur 0,72 cm,
rapport d'image conservé. **C'est la boîte fixe qui aligne la colonne** quelles
que soient les proportions des logos — un blason carré et un bandeau horizontal
occupent la même largeur, et la liste reste droite.

```latex
\form{ecole.png}{\textbf{Diplôme d'ingénieur} \textbullet\ {\color{accent}École d'ingénieurs}, Paris, 2023 – 2026}
```

## Qualité des fichiers

- **PNG à fond transparent**, hauteur d'au moins 256 pixels, 512 de préférence.
  Un logo au fond blanc posera un rectangle visible sur la page.
- **Pas de SVG** : `graphicx` ne l'inclut pas directement. Le script convertit.
- **Vérifier à l'écran après compilation.** Un logo peut être correct dans son
  fichier et écrasé dans la page si la hauteur demandée ne convient pas à ses
  proportions. Ouvrir le PDF et regarder, une fois par logo ajouté.
- **Monochrome ou couleur ?** Les logos officiels en couleur fonctionnent bien
  tant qu'ils restent peu nombreux. Au-delà de cinq ou six, le CV devient
  bariolé ; passer alors l'ensemble en une seule teinte, ou n'en garder que
  quelques-uns.

## La photo

Cadrage portrait, visage net, regard vers l'objectif, fond uni ou très simple,
tenue cohérente avec le secteur visé. Le gabarit la recadre en rectangle de
2,15 cm sur 2,3 cm, sans déformation. Le fichier s'appelle `photo.jpg` et se
place à côté du `.tex`.

Une photo de vacances recadrée se voit. Une photo prise contre un mur blanc avec
un téléphone récent, en lumière du jour, suffit parfaitement et coûte cinq
minutes.
