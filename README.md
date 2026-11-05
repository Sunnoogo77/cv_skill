# cv — rédiger un CV qui donne envie de recevoir la personne

Une compétence pour [Claude Code](https://claude.com/claude-code). Une fois
installée, l'agent mène l'entretien, trie ce qui est prouvable, écrit le CV et
produit un PDF — au lieu de reformuler poliment ce qu'on lui donne.

## Ce qu'elle fait

**Elle interroge avant d'écrire.** Expérience par expérience, avec les relances
qui font sortir ce qui compte : *pourquoi t'avait-on recruté ? combien ?
comment sais-tu que ça a marché ? qu'est-ce qui n'a pas marché ?* La plupart
des CV sont faibles parce que personne n'a posé ces questions.

**Elle met en valeur sans mentir.** Une certification en préparation se dit en
préparation, un projet non déployé se dit non déployé, et ce qui est obtenu ne
se mélange jamais avec ce qui ne l'est pas. Il y a une marge considérable entre
dire où l'on en est et le faire savoir sous son meilleur jour : tout le travail
se fait dans cette marge.

**Elle s'adapte au métier.** Dix fiches sectorielles — tech, finance, marketing,
BTP et industrie, santé, droit, académique, commerce, RH, artisanat — avec les
unités de mesure crédibles du domaine, les certifications qui font autorité et
le piège propre à chaque secteur. Un CV de chef de chantier et un CV de juriste
n'obéissent pas aux mêmes règles, et un CV académique à aucune des deux.

**Elle sait ce qui ne peut pas être dit.** Secret professionnel, information
privilégiée, détail d'une architecture de sécurité, dossiers clients : la fiche
confidentialité donne six substitutions et quatre tests à passer ligne par
ligne.

**Elle produit un vrai document.** Un gabarit LaTeX à une colonne, avec logos,
photo optionnelle, et autant de variantes qu'il y a de types de candidature —
CDI, alternance, stage — depuis **une source unique**, parce que deux fichiers
qui portent le même parcours finissent toujours par diverger. Un script vérifie
ensuite le PDF produit. Si LaTeX n'est pas souhaité, le travail reste valable :
seul le format de sortie change.

## Installation

### Le plus simple

Dans une session Claude Code, taper :

```
/plugin install cv --marketplace Sunnoogo77/cv_skill
```

Puis vérifier :

```
/plugin
```

La compétence est disponible dans toutes les sessions. Elle se déclenche d'elle-même
dès qu'il est question de CV ; on peut aussi l'appeler directement par
`/cv:cv-excellence`.

### Depuis le terminal

```bash
claude plugin install cv --marketplace Sunnoogo77/cv_skill
claude plugin list
```

Pour désinstaller : `claude plugin uninstall cv@cv-skill`.

### Sans passer par le plugin

Copier le dossier de la compétence dans son espace personnel :

```bash
git clone https://github.com/Sunnoogo77/cv_skill.git /tmp/cv_skill
mkdir -p ~/.claude/skills
cp -r /tmp/cv_skill/skills/cv-excellence ~/.claude/skills/
```

Ne pas cloner le dépôt directement dans `~/.claude/skills/` : le dossier
contient un manifeste de plugin, qui serait alors chargé comme tel.

## Comment s'en servir

Ouvrir Claude Code dans un dossier vide — celui où le CV sera produit — et
dire ce qu'on veut, en langage ordinaire :

> *J'ai besoin de refaire mon CV. Je suis infirmière, je cherche un poste en
> bloc opératoire.*

> *Mon CV ne donne rien, j'ai envoyé quarante candidatures. Tu peux le
> reprendre ? Il est dans Téléchargements.*

> *Je passe de la logistique au développement web. Je ne sais pas quoi mettre.*

L'agent pose ses questions par petits lots. **Répondre en détail, même en
vrac** : un récit désordonné vaut mieux qu'une réponse brève et propre. Il
relance là où c'est flou, propose, et laisse les décisions qui engagent —
photo, logos, mentions sensibles — à la personne.

Compter trente à quarante-cinq minutes pour un premier CV complet, puis
quelques minutes pour chaque variante.

## Ce dont la compétence a besoin

Rien pour la partie entretien et rédaction.

Pour produire le PDF LaTeX :

```bash
brew install tectonic        # macOS ; sinon tectonic-typesetting.github.io
```

Pour le script de contrôle, au choix `brew install poppler`, `pip install
pypdf`, ou rien du tout sur macOS, où il utilise PDFKit.

## Ce qu'il y a dans le dépôt

```
skills/cv-excellence/
├── SKILL.md                    la marche à suivre
├── references/
│   ├── entretien.md            les questions, et comment relancer
│   ├── redaction.md            écrire une ligne, chiffrer sans mentir
│   ├── secteurs.md             dix fiches métier et la confidentialité
│   ├── ats-et-forme.md         lecture automatisée, longueur, pays
│   ├── logos.md                sources légitimes, proportions
│   └── latex.md                le gabarit, les variantes, l'équilibrage
├── assets/
│   ├── preambule.tex           la mise en page
│   ├── cv.tex                  le squelette, rempli d'un exemple
│   └── build.sh                produit toutes les variantes
└── scripts/
    ├── verifier.py             contrôle du PDF produit
    └── logos.py                logos de technologies (Simple Icons, CC0)
```

Les fiches sectorielles distinguent ce qui est **sourcé** d'un texte
réglementaire ou d'un organisme certificateur, ce qui relève d'un **usage de
marché**, et ce que la recherche **n'a pas pu établir**. Cette dernière
catégorie est écrite noir sur blanc plutôt que comblée : une règle inventée
coûte plus cher qu'une règle absente.

## Ce qu'elle ne fera pas

Écrire un chiffre que la personne n'a pas donné. Présenter une certification en
préparation comme obtenue. Suggérer d'ajouter une photo, un âge ou une
nationalité — en France, l'apparence physique est un critère de discrimination
prohibé et un employeur ne peut exiger une photo que par exception justifiée.
Ajouter des mots-clés invisibles pour tromper un logiciel de tri : c'est détecté,
et c'est éliminatoire.

## Origine

Cette compétence condense le travail de construction d'un jeu de CV réel :
quatre familles de candidature, dix PDF depuis une source unique, logos
authentiques, et une règle tenue d'un bout à l'autre — ne jamais écrire sur un
CV ce qui ne tiendra pas en entretien.

## Licence

MIT, voir [LICENSE](LICENSE). Les logos récupérés par `scripts/logos.py`
viennent de [Simple Icons](https://simpleicons.org), publiés sous CC0 ; les
marques représentées appartiennent à leurs titulaires et ne sont citées que
pour indiquer les outils employés.
