# Produire le document

## Pourquoi LaTeX, et quand s'en passer

LaTeX donne trois choses difficiles à obtenir autrement : une maîtrise fine de
l'espacement, des variantes reproductibles depuis une source unique, et un PDF
dont le texte reste extractible — ce qui compte beaucoup pour les logiciels de
recrutement.

Il a un coût : il faut l'installer, et la personne ne pourra pas retoucher son
CV dans un traitement de texte. **Proposer, expliquer, accepter un refus.** Un
CV excellent en document bureautique vaut mieux qu'un CV LaTeX que la personne
ne peut pas faire évoluer. Tout le travail des étapes d'entretien, de tri et de
rédaction reste valable quel que soit le format de sortie.

## Mise en place

```
mon-cv/
├── build.sh              copié depuis assets/
└── src/
    ├── preambule.tex     copié depuis assets/
    ├── cv.tex            copié depuis assets/, puis rempli
    ├── photo.jpg         si photo
    └── logos/            fichiers PNG
```

Compilation :

```bash
brew install tectonic        # macOS ; sinon voir tectonic-typesetting.github.io
chmod +x build.sh && ./build.sh
```

`tectonic` télécharge ce dont il a besoin et ne demande aucune distribution TeX
installée. À défaut, **xelatex** convient. Ni `pdflatex` ni `latex` ne
compileront ce document : le préambule utilise `fontspec`.

## L'identité

En tête de `preambule.tex`, six commandes et rien d'autre ne portent de donnée
personnelle :

```latex
\newcommand{\nomcandidat}{Prenom NOM}
\newcommand{\villecandidat}{Ville, Region}
\newcommand{\telcandidat}{+33 0 00 00 00 00}
\newcommand{\telcandidaturl}{+33000000000}
\newcommand{\mailcandidat}{prenom.nom@exemple.fr}
\newcommand{\motsclescandidat}{}
```

`\motsclescandidat` alimente les métadonnées du PDF. Ce ne sont pas des mots
cachés dans la page — ce qui serait une fraude détectée — mais les mots-clés
normaux du fichier, que les outils documentaires indexent.

Retirer du bloc `\entete` les lignes GitHub ou LinkedIn si la personne n'en a
pas. Un lien vers un profil vide dessert.

## Les commandes du gabarit

| Commande | Usage |
|---|---|
| `\entete{titre}{sous-titre}{disponibilité}` | bloc d'en-tête complet, avec ou sans photo selon `\ifphoto` |
| `\section{Nom}` | titre de rubrique, filet compris |
| `\poste{intitulé}{employeur}{dates}{lieu}` | ligne de poste ou de projet |
| `\begin{faits} \item ... \end{faits}` | les puces d'une expérience |
| `\comp{intitulé}{contenu}` | une ligne de compétences ou de certifications |
| `\form{logo}{texte}` | une ligne de formation, logo aligné |
| `\marque{fichier}{hauteur}` | logo en ligne |
| `\ecusson{fichier}` | logo d'établissement dans une boîte fixe |

`\poste` et `\section` appellent `\Needspace` : un titre ne restera jamais seul
en bas d'une page, séparé de ce qu'il annonce.

## Les variantes

Une personne cherche souvent plusieurs choses à la fois — un CDI et une
alternance, un poste et un stage, dans deux pays. Chaque cible mérite son CV, et
ces CV partagent quatre-vingt-dix pour cent de leur contenu.

**Ne jamais dupliquer le fichier.** Deux fichiers qui portent le même parcours
divergent : une correction faite sur l'un est oubliée sur l'autre, et la
personne envoie un CV corrigé à l'un et fautif à l'autre sans le savoir.

Un drapeau par variante, déclaré en tête de `cv.tex` :

```latex
\newif\ifposte
\postetrue
\newif\ifstage
\stagefalse
```

Puis, aux endroits qui changent :

```latex
\ifstage
  ... version stage ...
\else
  ... version poste ...
\fi
```

`build.sh` bascule les drapeaux par `sed` et **vérifie après bascule** :

```bash
grep -qx -- '\\stagetrue' _b.tex || { echo "ECHEC"; exit 1; }
```

Cette vérification n'est pas une précaution de confort. Un `sed` dont le motif
ne correspond à rien ne proteste pas : le PDF se compile, il est propre, et il
porte la mauvaise variante. Sans ce `grep`, la personne postule en CDI avec un
CV de stage et personne ne s'en aperçoit. **Ajouter la vérification pour chaque
nouveau drapeau**, dans chaque appel de `gen`.

La photo suit le même mécanisme, ce qui évite d'avoir à trancher
définitivement : chaque variante sort en deux versions.

## Équilibrer les pages

Le défaut le plus fréquent : une deuxième page à moitié vide, ou un bloc coupé
en deux par un saut de page.

**Ce qu'on ne fait pas.** Ajouter du remplissage — une rubrique « centres
d'intérêt » gonflée, une ligne de compétences inventée. Réduire la police
au-dessous de 10 points. Supprimer un fait réel pour tenir.

**Les leviers, dans l'ordre à essayer.**

1. **L'interligne, limité à la variante concernée.** Le levier le plus efficace
   et le moins visible :

   ```latex
   \ifspont
   \linespread{1.12}
   \fi
   ```

   Placé après `\input{preambule.tex}`, il aère tout le document sans toucher à
   la taille du texte. Entre `1.04` et `1.15`, l'effet sur la pagination est
   considérable et l'œil ne le remarque pas.

2. **Les marges.** `top` et `bottom` à `1.05cm` et `1.0cm` sont déjà serrées ;
   `left` et `right` peuvent descendre à `1.2cm` sans que la page paraisse
   étouffée.

3. **Les espacements du préambule.** Les `\vspace` de `\section` et de `\form`
   se règlent de quelques centièmes d'em, ce qui déplace plusieurs lignes sur
   l'ensemble du document.

4. **Resserrer une formulation.** Une puce de quatre lignes qui en fait trois
   est presque toujours une meilleure puce.

Si la deuxième page reste très courte après tout cela, c'est que le CV doit
tenir en une page. Le dire à la personne plutôt que de meubler.

## Contrôler avant de rendre

```bash
python3 scripts/verifier.py Poste/CV_NOM_poste.pdf --liens
```

Puis **ouvrir le PDF et le regarder**. Le script ne voit pas qu'un logo est
écrasé, qu'une ligne orpheline traîne en haut d'une page, que l'en-tête déborde.
Ces trois défauts-là ne se voient qu'à l'œil, et ils se voient tout de suite.

Vérifier aussi, une fois, que le texte se copie correctement depuis le PDF :
sélectionner une puce, la coller dans un éditeur, lire. C'est exactement ce que
fera le logiciel du recruteur.

## Problèmes courants

**`Font ... not found`** — Latin Modern est livré avec toute distribution TeX ;
si la police manque, c'est que l'installation est incomplète. Avec `tectonic`,
relancer : il télécharge à la demande.

**Un logo ne s'affiche pas** — chemin relatif à `src/`, le dossier `logos/` doit
être à côté du `.tex`. `\marque` ajoute déjà `logos/` au chemin : ne pas le
répéter.

**Caractères accentués cassés** — compiler avec `xelatex` ou `tectonic`, pas
avec `pdflatex`.

**Le PDF fait plusieurs mégaoctets** — une photo ou un logo en très haute
définition. Réduire à 512 pixels de haut : l'impression n'y perd rien et le
fichier passe les limites de taille des formulaires de candidature.
