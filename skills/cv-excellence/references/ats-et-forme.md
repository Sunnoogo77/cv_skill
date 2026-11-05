# La forme : lecture automatisée, structure, pays

Cette fiche porte sur tout ce qui n'est pas le contenu : comment un CV est lu
par les logiciels de recrutement, une colonne ou deux, la longueur, et ce qui
change d'un pays à l'autre. Chaque affirmation porte sa source.

Lire la section utile, pas tout le document.

| Section | Contenu |
|---|---|
| 1 | Ce que font réellement les logiciels de recrutement, et ce qui casse |
| 2 | Structure : une colonne ou deux, ordre des rubriques, longueur |
| 3 | Les quatre cadres de description d'une expérience |
| 4 | Conventions par pays : photo, âge, nationalité, longueur |
| 5 | Ce qui fait rejeter un CV |
| 6 | Ce que la recherche n'a pas pu vérifier |
| 7 | Les chiffres qui circulent et qu'il ne faut jamais reprendre |
| 8 | Synthèse en dix règles |

**Deux réflexes avant d'utiliser cette fiche.** Un conseil qui n'est rattaché à
aucune source nommée se présente comme une préférence de lecture, pas comme une
règle. Et aucun chiffre de la section 7 ne se répète, même s'il est partout :
la section existe parce que ces chiffres sont faux ou invérifiables.

Recherche menée le 5 novembre 2026.

---

## 0. Niveaux de preuve utilisés dans cette fiche

| Niveau | Définition | Usage dans le skill |
|---|---|---|
| **A** | Source primaire : documentation officielle d'un éditeur d'ATS, texte de loi, article publié avec méthode consultable | Peut être affirmé comme un fait, avec sa source |
| **B** | Source professionnelle identifiable (organisme public, cabinet, éditeur de parsing) mais méthode partielle ou non reproductible | À présenter comme « selon X » |
| **C** | Blog commercial, chiffre qui circule sans source primaire retrouvable | **Ne jamais répéter comme un fait.** Mentionner seulement pour le démentir |

Règle pour le skill : si un conseil de CV ne peut pas être rattaché à un niveau A ou B,
il doit être formulé comme une convention ou une préférence de lecture, pas comme une règle.

---

## 1. Les ATS : ce qu'ils font réellement

### 1.1 Le pipeline réel (niveau A, par recoupement des docs éditeurs)

Un ATS ne « note » pas un CV. Il exécute une chaîne, et chaque maillon peut casser :

1. **Extraction du texte** du fichier (PDF/DOCX). Si le fichier est une image, il n'y a pas de texte → rien.
2. **Détermination de l'ordre de lecture** (reading order). C'est l'étape qui casse sur les colonnes.
3. **Segmentation en sections** (expérience, formation, compétences…) par repérage des titres.
4. **Extraction de champs** (nom, e-mail, téléphone, employeurs, dates, diplômes) pour préremplir une fiche candidat.
5. **Indexation plein texte** pour la recherche par mots-clés du recruteur.

Point décisif, documenté par trois éditeurs sur cinq : **l'échec du parsing ne détruit pas la candidature, il la dégrade.**
Greenhouse indique qu'en cas d'échec « *you'll see a message that the resume has only been attached to the candidate* » et
« *If a resume fails to parse, you'll need to manually input the candidate's details into the fields* »
([Greenhouse, *Unsuccessful resume parse*](https://support.greenhouse.io/hc/en-us/articles/200989175-Unsuccessful-resume-parse)).
Le fichier reste donc lisible par un humain. Le risque réel est triple : perte de préremplissage, **invisibilité dans la recherche par mots-clés du recruteur**, et friction (saisie manuelle) qui joue contre le candidat.
Exception à connaître : chez Greenhouse, pour l'import par e-mail (Maildrop) et l'import en masse, un échec de parsing peut empêcher la création de la fiche candidat ([Greenhouse, Maildrop](https://support.greenhouse.io/hc/en-us/articles/201990630-Maildrop)).

### 1.2 Greenhouse — la source primaire la plus explicite (niveau A)

Greenhouse publie la liste des causes d'échec. Citations **verbatim** de
[support.greenhouse.io/.../Unsuccessful-resume-parse](https://support.greenhouse.io/hc/en-us/articles/200989175-Unsuccessful-resume-parse) :

Trois familles de causes : « *The resume file is too large* », « *Fake resumes* », « *Resume formatting issues* ».

Problèmes de mise en forme listés, mot pour mot :
- « *A resume with spaces between the letters.* »
- « *Resumes that include graphics, photos, or word art* »
- « *Resumes that are uploaded as an image, rather than a document (such as a .docx or .pdf)* »
- « *Complex resumes with tables, headers, and footers* »
- « *Resumes with the name and contact information in the header, footer, or text box* »
- « *Resumes that have a columned layout* »
- « *Resumes without clear sections and differing formats throughout each section* »
- « *Company names that don't include identifying words such as Inc., Co., LTD, or LLC.* »
- « *Resumes with incomplete job titles. For example, Sr. Account Exec instead of Senior Account Executive* »

Limite de taille : « *Greenhouse Recruiting can't parse resumes larger than 2.5MB.* »
Formats : documents type .docx ou .pdf ; l'upload d'image est une cause d'échec.
Ces défauts peuvent produire un parsing **partiel** « *which will need to be manually corrected and verified* ».

À retenir, et c'est contre-intuitif : **Greenhouse — un ATS moderne, pas un système legacy — met explicitement « columned layout », « tables, headers, and footers » et « name and contact information in the header, footer, or text box » sur sa propre liste de causes d'échec.** C'est la citation la plus solide disponible contre les CV deux colonnes et contre les coordonnées en en-tête de page.

Deux éléments rarement repris et utiles :
- Les **noms/villes factices sont ignorés par le parser** (« placeholder names or town names are automatically skipped »). Conséquence pour un template : ne jamais livrer un CV avec des placeholders résiduels type « Lorem », « Entreprise X », « Ville ».
- Les **intitulés de poste abrégés** (« Sr. Account Exec ») et les **noms d'entreprise sans suffixe juridique** dégradent l'extraction. Écrire « Senior Account Executive » et « Martin Industries SAS » plutôt que « Sr. Acct Exec » et « Martin ».

### 1.3 Workday (niveau A, mais documentation avare)

[doc.workday.com — *Concept: Resume Parsing*](https://doc.workday.com/admin-guide/en-us/human-capital-management/recruiting/candidates/set-up-prospects-and-candidates/hdc1552497830785.html) :
- Champs parsés pour une candidature externe : informations personnelles et de contact, expérience professionnelle, formation, langues.
- Champs **non** préremplis : les champs masqués par configuration, plus « Languages » et « Skills » (la doc est ambiguë : « languages » apparaît côté candidature externe et en exclusion côté auto-remplissage — à ne pas affirmer de façon catégorique).
- Recommandation de format, verbatim : « *For best results, use resumes that don't have images or image-based styles.* »
- Avertissement, verbatim : « *Resume parsing results can vary based on resume format and order of words.* »
- Le recruteur peut relire les données extraites avant validation.
- Workday **ne publie pas** de liste de causes d'échec ni de formats de fichiers acceptés sur cette page.

Noter aussi que Workday est l'ATS où le candidat ressaisit le plus souvent à la main dans un formulaire après upload : l'enjeu « parsing » y est moins un filtre qu'un confort de préremplissage. (Observation de lecture de la doc, pas une affirmation sourcée.)

### 1.4 Lever (niveau A, via sa doc API)

[Lever API documentation](https://hire.lever.co/developer/documentation) :
- Formats parsés : docx, doc, pdf, txt. **Les images sont stockées mais pas parsées** : « *Image files are not supported and will not be successfully parsed for information.* »
- Champs extraits possibles : name, headline, emails, phones, location, company, links — l'extraction n'est pas garantie.
- La saisie manuelle prime sur le parsing : « *If candidate information is provided in the POST request and resume parsing is requested, the manually provided information will always take precedence.* »
- Statut de parsing exposé par l'API : `processing`, `processed`, `unsupported`, `error`, ou `null`. Il existe donc bien un état d'échec explicite côté produit.
- Import en masse CSV : « *Resumes must be in either a Word or PDF file format.* »
- Recherche : le filtre « Resume » restreint la recherche au texte **parsé depuis le CV** (« *will restrict the search to only content that was parsed from the resume* »). C'est la preuve mécanique que **ce qui n'est pas extrait est invisible dans la recherche recruteur.**
- Lever **ne publie pas** de position officielle sur les colonnes. L'affirmation « Lever tolère les colonnes » est non vérifiée.

### 1.5 SAP SuccessFactors (niveau A/B)

- **Moteur** : SAP documente l'usage d'un tiers, **Textkernel**, pour le parsing ([SAP Help, *Working with Resume Parsing*](https://help.sap.com/docs/successfactors-recruiting/setting-up-and-maintaining-sap-successfactors-recruiting/working-with-resume-parsing) — page JS, non récupérable en texte brut ; contenu confirmé via la note SAP ci-dessous).
- **Pas d'OCR** : note SAP [2081576](https://userapps.support.sap.com/sap/support/knowledge/en/2081576) — « *At this time, SAP does not subscribe to the image parsing technology that is offered* » et « *PDF documents that were scanned in or were previously images will not parse as expected* ». Décisif : **un PDF scanné ou aplati en image ne passe pas**, même chez un ATS tier-1.
- Langues de parsing supportées : néerlandais, anglais, allemand, français, espagnol et d'autres (même note). Le français est couvert.
- Formats de pièces jointes acceptés (note [2363852](https://userapps.support.sap.com/sap/support/knowledge/en/2363852)) : .doc, .docx, .gif, .jpeg, .jpg, .pdf, .txt. PDF sécurisés/protégés **non** acceptables. PPT/PPTX non supporté (notes [2251329](https://userapps.support.sap.com/sap/support/knowledge/en/2251329), [2271789](https://userapps.support.sap.com/sap/support/knowledge/en/2271789)) — ce qui contredit la page d'aide générale qui liste PPT ; la note SAP est la source la plus fiable.
- Les champs déjà renseignés ne sont pas écrasés par le parsing.

**Conséquence actionnable** : un PDF exporté en « aplatir / flatten » ou protégé par mot de passe est à proscrire. Et le PDF doit contenir une couche texte sélectionnable.

### 1.6 Oracle Taleo (niveau A, mais documentation datée)

[Oracle Taleo Enterprise 21B, *Using Legacy Recruiting*](https://docs.oracle.com/en/cloud/saas/taleo-enterprise/21b/otrec/candidate-management.html) :
- **Taille maximale : 100 kilo-octets.** « *The file must not exceed 100 kilobytes* ». C'est un ordre de grandeur radicalement différent des 2,5 Mo de Greenhouse, et cela disqualifie de fait un CV contenant une photo haute résolution ou des icônes bitmap.
- Formats acceptés : Word, WordPerfect, texte brut, RTF, HTML, PDF, Excel, OpenOffice Writer.
- Limite linguistique explicite : « *the processing of resumes written in other languages than the submission language might not be supported.* »
- Images non parsées : Taleo Business Edition accepte l'upload PNG/JPEG mais « *the resume will not be parsed when it is in an image format* » ([Oracle 24A readiness note](https://docs.oracle.com/en/cloud/saas/readiness/hcm/24a/tale-24a/24A-tbe-wn-f32282.htm)) — et ces candidats échappent alors à la recherche par mots-clés.
- Oracle reconnaît sous-traiter : le parsing est « *delivered using a third party partner service* », livré « *as-is* ».
- La doc 21B est ancienne ; je n'ai pas trouvé de liste de formats à jour pour Oracle Recruiting Cloud (le successeur). **À vérifier avant d'affirmer les 100 Ko pour un déploiement 2026.**

### 1.7 Synthèse éditeurs

| ATS | Moteur | Taille max documentée | Images parsées | Colonnes : position officielle | Source |
|---|---|---|---|---|---|
| Greenhouse | non documenté | 2,5 Mo | Non | **Cause d'échec documentée** | A |
| Workday | non documenté | non documentée | « avoid images » | Non documentée ; « varie selon le format » | A |
| Lever | non documenté | non documentée | Non (`unsupported`) | **Aucune position publiée** | A |
| SuccessFactors | Textkernel | non documentée | Non (pas d'OCR) | Non documentée ; Textkernel traite les colonnes (voir 1.8) | A |
| Taleo | tiers non nommé | **100 Ko** (doc 21B) | Non | Non documentée | A (daté) |

### 1.8 Pourquoi les colonnes cassent — le mécanisme, chiffré (niveau A)

C'est la source la plus utile de toute cette recherche, parce qu'elle vient de l'éditeur du moteur de parsing utilisé par SuccessFactors et qu'elle est quantifiée.
[Textkernel, *Improving extraction from column resumes*](https://www.textkernel.com/learn-support/blog/improving-extraction-from-column-resumes/) :

- Le problème : en rendu naïf haut→bas / gauche→droite, « *the information from different sections of the CV is mixed together* ».
- Le piège symétrique : si l'on coupe à chaque blanc vertical, « *a key-value structured layout would break the key from the value* ». Autrement dit **les tableaux clé-valeur cassent l'extraction de champ**, ce qui est précisément la structure d'un bloc « Compétences | niveau » en tableau.
- Textkernel a remplacé des règles par un modèle de gradient boosting qui classe chaque blanc vertical (séparateur de colonne ou non). Résultats annoncés :
  - décision correcte sur un blanc : **91 % contre 82 %** pour l'ancien système à règles ;
  - sur le sous-ensemble décisif (les vrais séparateurs de colonne) : **de 60 % à 82 %** ;
  - CV « bien rendus » selon annotateurs humains : **de 62 % à 90 %** ;
  - taux de remplissage des coordonnées : **+4 à +10 points absolus**.
- Échantillons cités : plus de 600 blancs, ~700 CV, plus de 12 000 CV, plus de 1 000 divergences de parser.
- La page n'est pas datée (seulement « © 2026 »).

**Lecture correcte de ces chiffres, et c'est le point central de la section 2 :** même après passage au machine learning, le meilleur moteur de la place rate encore **18 % des séparateurs de colonne** et rend mal **10 % des CV**. Une mise en deux colonnes n'est donc pas « cassée », elle est **un risque résiduel à deux chiffres, gratuit à éliminer**. Et ce chiffre est le meilleur cas : il décrit Textkernel, pas le parser moyen.

Côté recommandation éditeur, Textkernel ajoute une consigne qui vaut pour tout candidat
([Tx Platform v10 API docs](https://developer.textkernel.com/tx-platform/v10/resume-parser/api/)) : envoyer « *the original file, not the result of copy/paste, not a conversion by some other software, not a scanned image* ».
Donc : exporter le PDF depuis le traitement de texte d'origine, jamais re-imprimer/ré-encoder.

**Non vérifié** : un moteur de recherche m'a attribué un chiffre de « ~20 % des CV en mise en page multi-colonnes » à l'article arXiv [2510.09722](https://arxiv.org/abs/2510.09722) (*Layout-Aware Parsing Meets Efficient LLMs*, Zhu et al., 10 oct. 2025). **Ce chiffre n'est pas dans le résumé de l'article** que j'ai lu. Ne pas le citer.

### 1.9 Mythes à démonter explicitement

**« 75 % des CV sont rejetés par l'ATS. »** → Faux, ou plus exactement : **sans source primaire**.
Le chiffre est systématiquement attribué à un argumentaire commercial de 2012 de **Preptel**, société d'optimisation de CV disparue en 2013, qui n'a jamais publié de méthode ni d'échantillon
([SupaCV, *Where the « 75% of Resumes Are Rejected by ATS » Stat Came From*](https://supacv.com/blog/ats-rejection-myth) ; [ResumeVera](https://resumevera.com/guides/ats-rejection-myth-origin)).
Honnêteté nécessaire : **ces sources sont elles-mêmes de niveau C** (des blogs d'outils de CV), et je n'ai trouvé **aucune source primaire ni dans un sens ni dans l'autre**. Le chiffre varie d'ailleurs entre 70 %, 75 % et 88 % selon les sites qui le recopient. Formulation correcte pour le skill : *« ce chiffre circule sans étude identifiable derrière lui ; il ne faut ni le citer, ni raisonner à partir de lui »*.

**« Tout PDF est rejeté. »** → Faux. Greenhouse recommande des documents « *such as .docx or .pdf* » et sa FAQ candidat dit d'uploader un PDF pour de meilleurs résultats ([Greenhouse, MyGreenhouse FAQ](https://support.greenhouse.io/hc/en-us/articles/43418495049499-MyGreenhouse-FAQ-for-Candidates)). Lever, Taleo et SuccessFactors acceptent tous le PDF (§1.4-1.6).
La vraie distinction n'est pas PDF vs DOCX, c'est **PDF avec couche texte vs PDF-image / PDF scanné / PDF protégé**, ces derniers étant explicitement cassés chez SAP (§1.5) et Oracle (§1.6).
Nuance résiduelle : DOCX reste le format le plus sûr par défaut car il porte sa structure logique, alors que le PDF n'encode qu'un placement de glyphes et exige de reconstruire l'ordre de lecture. (Raisonnement de mécanisme, pas une citation.)

**« Il faut bourrer des mots-clés en texte blanc. »** → À la fois **inefficace et déloyal**. À énoncer sans ambiguïté :
- Le parser extrait le texte sans tenir compte de la couleur : le texte blanc est extrait comme le reste, et réapparaît en clair dès qu'un recruteur sélectionne, copie ou exporte le document. Ce mécanisme est cohérent avec toutes les docs éditeurs lues ; **je n'ai pas trouvé de source primaire d'éditeur l'affirmant noir sur blanc** (niveau B).
- La **détection automatisée** du texte blanc par Greenhouse ou Lever est **revendiquée par des blogs sans preuve** : je n'ai pas pu la confirmer. Ne pas l'affirmer.
- En revanche, Greenhouse documente que les **faux contenus** sont une cause d'échec de parsing à part entière (« *Fake resumes* », §1.2).
- Position du skill : c'est une **tromperie sur document de candidature**, découverte au premier copier-coller, et elle relève de la même catégorie que le mensonge sur un diplôme (§5.3). Le skill doit refuser de le faire et expliquer pourquoi, sans s'appuyer sur un détecteur hypothétique.

**« Il existe des templates "ATS-friendly" certifiés. »** → Aucun éditeur d'ATS ne certifie de template. Greenhouse, Workday, Lever, SAP et Oracle publient des contraintes, pas des labels. Tout badge « ATS-proof » est un argument commercial.

**« L'ATS rejette automatiquement sur le contenu du CV. »** → Le mécanisme de rejet automatique documenté est celui des **questions éliminatoires** du formulaire (autorisation de travail, licence requise, mobilité), pas l'analyse du CV. Je n'ai pas de source primaire chiffrant la part d'employeurs activant un auto-rejet sur contenu ; un chiffre de « 8 % » circule, attribué à une enquête Enhancv sur 25 recruteurs américains — **échantillon trop petit et source commerciale, à ne pas citer**.

---

## 2. Structure

### 2.1 Une colonne contre deux colonnes

**Ce qui est établi (niveau A)**
- Greenhouse liste « *Resumes that have a columned layout* » parmi ses causes d'échec de parsing (§1.2).
- Textkernel, le meilleur cas documenté, échoue encore sur ~18 % des séparateurs de colonne et rend mal ~10 % des CV (§1.8).
- Les tableaux clé-valeur cassent l'appariement clé↔valeur (§1.8).

**L'argument adverse, et pourquoi il ne tient pas en l'état**
Enhancv (éditeur de templates deux colonnes) soutient que « virtually all modern ATS » lisent les deux colonnes correctement
([Enhancv, *The State of Resume Parsing*](https://enhancv.com/blog/ats-resume-parsing/), publié 06/07/2026, mis à jour 30/09/2026, par Volen Vulkov, cofondateur d'Enhancv).
Après lecture de la page : les tests revendiqués portent sur **un job board non nommé**, sans méthode, sans taille d'échantillon, sans critère de réussite. Le tableau « plateforme par plateforme » (Taleo, SuccessFactors, iCIMS, Greenhouse, Lever, Ashby) est **asserté sans données**. Les « 44 sur 60 success stories en deux colonnes (73 %) » sont auto-déclarées, sans groupe de comparaison une colonne — le chiffre ne mesure donc rien. L'auteur le concède (« not a controlled experiment »). **Conflit d'intérêts direct : la société vend les templates deux colonnes.**
Ce qui est néanmoins juste et à retenir de cette page : les parsers récents utilisent des modèles d'ordre de lecture (XY-Cut, LayoutReader de Microsoft Research 2021), donc le niveau général progresse. Cela déplace le risque, il ne l'annule pas.

De même, la page de Jobscan sur les tableaux et colonnes
([Jobscan, *Can an ATS Read Tables and Columns in 2026?*](https://www.jobscan.co/blog/resume-tables-columns-ats/), publiée 24/09/2026) ne contient **qu'un seul exemple**, sur Lever, sans méthode ni date de test, où le parser aurait manqué les compétences, la section « About », les coordonnées et les liens. Anecdote, pas donnée. La revendication d'un « test de 8 systèmes » attribuée à un autre blog (cvcraft) n'est pas vérifiable.

**Suivi oculaire : il n'y a pas d'étude de suivi oculaire qui compare une colonne et deux colonnes.**
C'est important à dire au lieu de laisser croire le contraire. La seule étude relue par les pairs que j'ai identifiée sur le regard des recruteurs pendant le tri de CV est
[*Using Machine Learning with Eye-Tracking Data to Predict if a Recruiter Will Approve a Resume*](https://www.mdpi.com/2504-4990/5/3/38), **Machine Learning and Knowledge Extraction** (MDPI, 2023) : cabines individuelles, oculomètre **Tobii Spectrum**, 115 variables décrivant le regard pour prédire l'approbation. **Le site a refusé ma requête (HTTP 403) : je n'ai pas pu lire les effectifs ni les résultats.** À consulter avant d'en tirer quoi que ce soit. Une étude danoise (Aalborg, 2022) est mentionnée par un blog, je n'ai pas trouvé l'article original.

**Position recommandée pour le skill** : **une colonne par défaut**, non pas parce que les deux colonnes seraient « rejetées », mais parce que (a) l'éditeur Greenhouse les désigne lui-même comme cause d'échec, (b) le meilleur parser du marché garde un taux d'erreur à deux chiffres, (c) le gain allégué des deux colonnes n'est appuyé par **aucune donnée exploitable**. Le rapport bénéfice/risque est défavorable. Si l'utilisateur tient aux deux colonnes (secteur créatif, candidature par e-mail direct, réseau), produire **deux versions** : une mise en page libre pour l'humain, une version une colonne pour tout dépôt sur portail.

**Règles dérivées, chacune rattachée à une source primaire :**
- Jamais le nom ni les coordonnées dans un en-tête/pied de page ou une zone de texte (Greenhouse, verbatim §1.2).
- Pas de tableaux, y compris pour les compétences (Greenhouse ; mécanisme clé-valeur Textkernel §1.8).
- Pas de texte dans une image, pas de CV scanné, pas de PDF aplati (SAP note 2081576, Oracle 24A, Workday).
- Pas d'icônes à la place des libellés : une icône enveloppe n'est pas le mot « E-mail ». Le parser cherche des motifs textuels et des intitulés de section ; Greenhouse exige « *clear sections* » avec des titres. Écrire les libellés en texte. (Dérivation de mécanisme, niveau B.)
- Titres de section standards. L'Apec le dit aussi pour la France : « *Assurez-vous que les informations essentielles sont disposées dans des sections clairement définies, facilement repérables grâce à des titres standards* » et « *Évitez également les mises en page trop créatives* » ([Apec, *Comment faire un CV efficace pour les ATS ?*](https://www.apec.fr/candidat/optimiser-votre-candidature/candidature/fiches-avis/optimisez-votre-cv-pour-passer-le-filtre-des-ats-.html) — page en 403 à ma tentative de lecture directe ; citations issues de l'index du moteur, **à revérifier**).
- Polices : aucune doc éditeur lue ne mentionne la police. Le risque réel documenté est l'**espacement anormal des lettres** (« *A resume with spaces between the letters* », Greenhouse) — typique d'un letter-spacing agressif ou d'une police mal sous-ensemblée dans le PDF. Donc : polices système courantes et pas de crénage exotique, non pas par superstition mais pour garantir une extraction propre des mots.
- Intitulés de poste complets et noms d'entreprise avec forme juridique (Greenhouse, verbatim).
- Poids du fichier : viser **< 500 Ko** pour rester compatible même avec les 100 Ko documentés par Taleo 21B quand c'est possible, et de toute façon très loin des 2,5 Mo de Greenhouse. Une photo est le premier contributeur au poids.

### 2.2 Le temps de première lecture : les « 6 secondes » et les « 7,4 secondes »

**Verdict : chiffre fragile, origine commerciale, méthode non publiée. À ne pas citer comme un fait.**

- Origine : **TheLadders**, un site d'emploi commercial — donc partie intéressée — avec une première étude d'eye-tracking en **2012** donnant **6 secondes**, puis une reprise en **2018** donnant **7,4 secondes**.
- **Je n'ai pas pu lire la source primaire.** Les trois URL de TheLadders (le PDF de l'étude et les deux articles) renvoient **HTTP 403** : `theladders.com/static/images/basicSite/pdfs/TheLadders-EyeTracking-StudyC2.pdf`, `/career-advice/you-only-get-6-seconds-of-fame-make-it-count`, `/career-advice/why-do-recruiters-spend-only-7-4-seconds-on-resumes`. web.archive.org est inaccessible depuis cet environnement. **Les effectifs, la durée, le matériel et la définition exacte de la mesure restent donc inconnus.**
- Critique la plus substantielle trouvée : Susan Gygax, professionnelle du recrutement (Spectacle Talent Partners),
[*Is the 6-Second Resume Scan a Myth?*](https://spectacletalentpartners.com/is-the-6-second-resume-scan-a-myth/) — page non datée. Elle relève que le rapport 2018 « *doesn't state how many recruiters were in the study, their experience, or how many times they repeated the two-stage study* » et « *does not specify the types of positions or lengths of resumes* ». Elle qualifie le rapport de guide pratique « *used as clickbait* » et le chiffre de « vacuum metric ». Sa propre contre-enquête (un sondage dans un groupe Facebook de recruteurs) est, de son propre aveu, « inconclusive ».
- Un chiffre attribué parfois à « 30 recruteurs en 2012 » n'a pas pu être confirmé.
- **Donnée contradictoire utile** : l'étude ResumeGo 2018 (§2.4) rapporte des temps de lecture de **2 min 24 s** sur un CV d'une page et **4 min 05 s** sur un CV de deux pages — pour des CV de finalistes, pas pour le premier tri. Les deux chiffres ne mesurent donc pas la même chose : **un tri de pile** (quelques secondes) et une **lecture d'évaluation** (quelques minutes) sont deux moments distincts.

**Formulation recommandée pour le skill** : ne jamais écrire « vous avez 6 secondes ». Écrire : *le premier passage est un tri, pas une lecture ; le CV doit donc permettre de répondre en haut de première page à « quel poste, quel niveau, quelle preuve » — l'ordre de grandeur de quelques secondes est plausible et conforme à la pratique rapportée, mais le chiffre précis de 6 ou 7,4 secondes vient d'une étude commerciale dont la méthode n'a jamais été publiée.*

### 2.3 Ordre des sections

**Aucune source primaire ne prescrit un ordre.** Ce qui est documenté, c'est l'exigence de sections **clairement délimitées et à titres standards** (Greenhouse §1.2 ; Apec §2.1). L'ordre ci-dessous est donc une **convention de métier**, à présenter comme telle.

Ordre par défaut, antichronologique :
1. **Identité et coordonnées** — dans le corps du document, pas en en-tête de page (contrainte A). Nom, ville/région, téléphone, e-mail, URL LinkedIn ou portfolio en texte visible et non derrière un lien masqué.
2. **Titre / accroche** — intitulé du poste visé + 1 à 3 lignes de substance. Pas un « profil » de 6 lignes de qualités.
3. **Expérience professionnelle** — par défaut.
4. **Formation** — remonte **avant** l'expérience dans trois cas : étudiant ou jeune diplômé sans expérience significative ; métier où le diplôme est une condition d'exercice (droit, santé, expertise comptable) ; reconversion par un diplôme récent.
5. **Compétences** — en liste de texte, jamais en tableau ni en barres de progression (contrainte A §1.8). Les barres de niveau n'ont aucune valeur informative extractible.
6. **Projets / réalisations** — section à part entière quand l'expérience salariée est courte : c'est là que se logent l'entrepreneuriat, l'open source, l'associatif.
7. **Langues, certifications**.
8. **Divers** — à ne garder que si les éléments servent la candidature.

Principe de hiérarchie, indépendant de toute étude : **le haut de la première page est la seule zone dont la lecture est quasi certaine**. Tout ce qui plaide la candidature y va.

### 2.4 Longueur

**Seule donnée quantifiée trouvée, et elle contredit la règle de la page unique :**
Étude **ResumeGo** (2018). 482 recruteurs, responsables du recrutement, professionnels RH et dirigeants ; exercice de tri simulé ; terrain du 15 octobre au 2 novembre 2018.
Résultats rapportés : sur 7 712 CV préférés par les participants, **5 375 faisaient deux pages**, soit une préférence d'environ **2,3 fois** pour deux pages. Par niveau : **×1,4 pour les postes débutants, ×2,6 pour les postes intermédiaires, ×2,9 pour les postes d'encadrement**.
Sources : [ERE, *New Survey Declares Winner in One-page vs. Two-page Resume Debate*](https://www.ere.net/articles/one-or-two-page-resumes-best) ; [Fast Company](https://www.fastcompany.com/90271521/are-one-page-or-two-page-resumes-better) ; [TheLadders](https://www.theladders.com/career-advice/new-research-says-2-page-resumes-are-actually-preferred-by-recruiters).
**Réserves à énoncer** : ResumeGo **vend des services de rédaction de CV** ; l'étude a 8 ans ; c'était un exercice simulé et non un recrutement réel ; **je n'ai pas trouvé de réplication indépendante**. Niveau B, pas A.

Repères pratiques, présentés comme conventions :

| Profil | Longueur | Remarque |
|---|---|---|
| Étudiant, stage, premier emploi | 1 page | Il n'y a pas matière à deux pages sans remplissage |
| 0–3 ans d'expérience | 1 page | |
| 3–10 ans | 1 à 2 pages | La donnée ResumeGo plaide pour 2 dès le niveau intermédiaire |
| > 10 ans, encadrement | 2 pages | Idem, préférence la plus marquée |
| Recherche académique, médecine | sans limite | Publications et enseignements exhaustifs ; registre différent |
| Allemagne, Suisse | 2 pages max | §4 |

Règle de décision à retenir : **la longueur n'est pas un objectif, c'est une conséquence.** Deux pages denses battent une page compressée en corps 9 ; une page nette bat deux pages diluées. La question à poser à l'utilisateur n'est pas « une ou deux pages » mais « chaque ligne apporte-t-elle une preuve que la ligne précédente n'apporte pas ».

---

## 3. Décrire une expérience : les quatre cadres

### 3.1 Origines, vérifiées

- **STAR** (Situation, Task, Action, Result) : issu du monde de l'**entretien structuré**, pas du CV. Attribué à **DDI (Development Dimensions International)** dans le cadre de son système **Targeted Selection**. DDI revendique sur son propre site avoir créé le premier système d'entretien comportemental et décrit STAR comme un modèle à quatre points ([DDI, *Targeted Selection / Behavioral Interviewing*](https://www.ddiworld.com/products/targeted-selection) ; [DDI, ressources *Behavioral Interviewing*](https://www.ddiworld.com/resources/behavioral-interviewing)). Les dates circulant (1974, « années 1970 ») viennent de sources secondaires et des pages marketing de DDI ; **l'année exacte n'est pas établie par une source indépendante**. Les bénéfices annoncés (moins de biais, décisions plus fiables) sont des **affirmations de DDI**, sans évaluation indépendante trouvée.
- **CAR** (Challenge/Context, Action, Result) et **PAR** (Problem, Action, Result) : **aucune origine identifiable**. Ce sont des variantes abrégées de STAR popularisées par des coachs. L'acronyme PAR est lui-même instable (parfois « Situation, Problem, Action, Result »). À présenter comme des conventions pédagogiques, **pas** comme des méthodes attribuables.
- **XYZ** — « *Accomplished [X] as measured by [Y] by doing [Z]* » : origine **certaine et unique**. Billet LinkedIn de **Laszlo Bock**, alors SVP People Operations chez Google, **septembre 2014**, « My Personal Formula for a Winning Resume » ([copie republiée](https://beyondrisk.wordpress.com/2014/10/05/laszlo-bock-svp-people-operations-at-google-my-personal-formula-for-a-winning-resume/) ; [original LinkedIn](https://www.linkedin.com/pulse/20140929001534-24454816-my-personal-formula-for-a-better-resume), inaccessible en lecture automatisée).
  **Point à corriger dans tous les contenus qui circulent : ce n'est PAS une méthode officielle de Google.** C'est la formule personnelle d'un dirigeant, publiée à titre personnel. Je n'ai trouvé **aucun document Google** la recommandant. L'étiquette « formule XYZ de Google » est une extrapolation.
  Exemple donné par Bock lui-même, verbatim :
  - avant : « *Studied financial performance of companies and made investment recommendations* »
  - après : « *Improved portfolio performance by 12% ($1.2M) over one year by refining cost of capital calculations* »
  Et son argument méthodologique, souvent perdu : il insiste sur le **dénominateur**. 12 % sur un portefeuille de 10 M$ (soit 1,2 M$) n'a pas le même poids que 12 % sur 100 $. Le Y doit porter sa base de comparaison, sinon le pourcentage ne veut rien dire. Bock ne donne dans ce billet **aucune** recommandation de longueur de CV.

### 3.2 Comparatif opérationnel

| Cadre | Structure | À quoi il sert | Limite | Verdict pour un CV |
|---|---|---|---|---|
| **STAR** | Situation, Tâche, Action, Résultat | Oral : raconter une situation en entretien | 4 temps = trop long pour une puce ; Situation et Tâche se recouvrent et consomment des mots sans rien prouver | **Pour préparer l'entretien, pas pour écrire la puce.** C'est le réservoir de matière |
| **CAR** | Contexte/Défi, Action, Résultat | Compresse Situation+Tâche en un seul temps | Le « contexte » dérive vite en description de poste | Convenable quand le contexte est réellement nécessaire à la compréhension |
| **PAR** | Problème, Action, Résultat | Même compression, mais ancrée sur un problème | L'acronyme n'est pas standardisé | Bon réflexe mental : « quel problème ? » force à sortir du descriptif de fonction |
| **XYZ** | Résultat, Mesure, Moyen | **Met le résultat en premier mot de la puce** | Exige un chiffre ; sans chiffre, la formule tourne à vide | **Le meilleur pour la puce écrite**, parce qu'il est antéposé : le premier mot lu est l'accomplissement |

**Recommandation pour le skill** : utiliser STAR/CAR comme **grille d'entretien pour extraire la matière de l'utilisateur**, puis **écrire en XYZ**. L'intérêt structurel de XYZ est l'antéposition du résultat : sur un document parcouru de haut en bas, le début de ligne est la position la plus lue.

### 3.3 Exemples avant/après

**Avant/après 1 — descriptif de poste → XYZ**
- Avant : « Responsable du community management des réseaux sociaux de l'entreprise. »
- Après : « Porté l'audience Instagram de 1 200 à 8 500 abonnés en 9 mois en passant d'une publication hebdomadaire à un format vidéo court trois fois par semaine. »

**Avant/après 2 — CAR, quand le contexte compte**
- Avant : « Participation à la refonte du processus de facturation. »
- Après : « Dans une équipe de 4 sans outil de facturation dédié, automatisé l'émission des factures sous Google Apps Script, ramenant la clôture mensuelle de 3 jours à 4 heures. »

**Avant/après 3 — STAR oral → XYZ écrit**
- STAR (matière brute pour l'entretien) : *Situation* : le support client répondait en 48 h et les clients se plaignaient. *Tâche* : on m'a demandé de réduire le délai. *Action* : j'ai trié les demandes par motif, rédigé 12 réponses types et mis en place un routage. *Résultat* : délai moyen à 6 h, réclamations divisées par deux.
- XYZ (la puce) : « Réduit le délai de première réponse du support de 48 h à 6 h en catégorisant les demandes et en industrialisant 12 réponses types. »

**Avant/après 4 — verbe faible → verbe d'action**
- Avant : « Était en charge de la coordination de l'équipe projet. »
- Après : « Coordonné 5 contributeurs sur 3 mois pour livrer la refonte du site dans le budget initial. »

### 3.4 Quantifier honnêtement sans divulguer de chiffre d'entreprise

Problème réel et fréquent : le chiffre d'affaires, la marge, le nombre de clients peuvent être confidentiels — et un candidat qui les publie démontre surtout qu'il ne sait pas tenir une information. Huit substituts légitimes, du plus au moins fort :

1. **Variation relative sans base absolue.** « Augmenté le taux de conversion de 18 % » sans dire le volume. Attention : Bock avertit qu'un pourcentage sans base est faible (§3.1). À utiliser quand la base est confidentielle, en sachant que la puce perd en force.
2. **Avant → après sur une grandeur non sensible.** Délais, durées, nombre d'étapes, taux d'erreur, fréquence : « clôture mensuelle de 3 jours à 4 heures ». Souvent plus parlant qu'un montant, et rarement confidentiel.
3. **Ordre de grandeur arrondi et annoncé comme tel.** « portefeuille de l'ordre de 50 clients », « budget à six chiffres ». Honnête si l'arrondi est visible.
4. **Volume de travail et périmètre.** Nombre de dossiers traités, de personnes encadrées, de pays couverts, de systèmes maintenus, taille de la base de code, nombre d'utilisateurs actifs.
5. **Temps et rythme.** « en 9 mois », « 3 fois par semaine », « sur 2 exercices ». Le rythme est une mesure, et il est rarement sensible.
6. **Rang et sélectivité.** « 1er sur 40 projets présentés », « retenu parmi 300 candidatures », « finaliste sur 12 équipes ».
7. **Preuve externe vérifiable.** Lien vers un dépôt, un produit en ligne, une publication, un prix, un nombre d'étoiles, un article de presse. Une preuve consultable vaut mieux qu'un chiffre non vérifiable.
8. **Décision ou adoption.** « méthode reprise par les 3 autres équipes », « process toujours en place 2 ans après ». Mesure l'effet sans révéler de montant.

Règles de probité à inscrire dans le skill :
- **Ne jamais fabriquer un chiffre, même « plausible ».** Un chiffre inventé est une affirmation vérifiable en entretien : « comment l'avez-vous mesuré ? » suffit à l'effondrer.
- **Ne jamais s'attribuer un résultat collectif au singulier.** « Contribué à » / « dans une équipe de 4 » est plus solide que « généré », parce que cela survit à la question de contrôle.
- Si l'utilisateur ne sait pas, le skill doit **le dire et proposer un substitut de la liste**, pas combler.
- Préférer « environ / de l'ordre de » à une fausse précision. « ~45 clients » est crédible ; « 47,3 clients » ne l'est pas.

---

## 4. Conventions par pays

### 4.1 Tableau de synthèse

| | Photo | Date de naissance / âge | Nationalité | Situation familiale | Longueur usuelle | Signature |
|---|---|---|---|---|---|---|
| **France** | Usage courant, **non obligatoire** | Fréquente, non obligatoire | Parfois | En recul | 1–2 p. | — |
| **Allemagne** | **Usage fort**, non obligatoire | Fréquente | Parfois | Historiquement oui, en recul | 1–2 p. | CV daté et signé = tradition résiduelle |
| **Suisse** | **Usage fort, quasi attendu** | Attendue en pratique | Attendue en pratique | Parfois | max 2 p. | Dossier complet avec certificats de travail |
| **Royaume-Uni** | **À éviter** | **À omettre** | Non ; mentionner le droit de travailler | Non | 2 p. | — |
| **États-Unis** | **À éviter** | **À omettre** | Non ; « authorized to work » | Non | 1–2 p. | — |
| **Canada** | **À éviter** | **À omettre** | Non ; droit de travailler | Non | 1–2 p. | — |
| **Afrique de l'Ouest franco.** | Facultative | Usage courant | Usage courant | Usage courant | 1–2 p. | Sources faibles, voir §4.7 |

### 4.2 France

- **La photo n'est pas obligatoire et rien ne l'impose.** L'Apec indique pour son profil candidat : « *La photo n'est pas obligatoire.* » ([Apec, guide Profil Apec 2024](https://www.apec.fr/files/live/sites/www/files/documents_reference/candidat/ProfilApecguide%20candidats_2024.pdf)). Elle reste un usage très répandu sur le CV français. **Attention** : la citation de l'Apec porte sur son profil en ligne, pas sur le CV papier ; je n'ai pas trouvé de position Apec explicite sur la photo du CV lui-même.
- **Cadre légal des informations demandables** : article **L. 1221-6 du Code du travail** — les informations demandées à un candidat doivent présenter **un lien direct et nécessaire** avec l'emploi proposé ou l'évaluation des aptitudes professionnelles ([Légifrance, section Recrutement](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006072050/LEGISCTA000006189415)). C'est la base juridique qui rend illégitimes les questions sur la vie privée, et qui plaide pour retirer du CV situation familiale et nombre d'enfants.
- **CV anonyme : obligation abandonnée.** L'article **L. 1221-7** avait été créé par la loi de 2006 pour imposer aux employeurs de plus de 50 salariés d'examiner les candidatures de façon anonyme. **Le décret d'application n'a jamais été publié**, l'obligation n'est donc jamais entrée en vigueur ; le **Conseil d'État** a enjoint au Premier ministre de prendre ce décret par une décision du **9 juillet 2014** ([Conseil d'État, *CV anonyme*](https://www.conseil-etat.fr/actualites/cv-anonyme)). La **loi n° 2015-994 du 17 août 2015 (loi Rebsamen), art. 48**, a rendu le dispositif **facultatif** : le texte en vigueur dispose désormais que ces informations « **peuvent** être examinées » dans des conditions préservant l'anonymat ([Légifrance, art. L1221-7](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000031087398)). Le Conseil d'État a dès lors refusé de prononcer une astreinte, l'obligation ayant disparu.
  Attention : des sites juridiques affichent encore l'ancienne rédaction impérative (« ne peuvent être examinées que… ») — par exemple [Lexbase](https://www.lexbase.fr/texte-de-loi/art-l1221-7-code-du-travail/L6284ISK.html). **Se référer à Légifrance.**
- **La discrimination à l'embauche sur le nom est mesurée par l'État et elle est massive.** Testing commandé par la **DARES**, réalisé avec l'**IPP** et **ISM Corum**, campagne 2020, publication novembre 2021 : environ **9 600 candidatures fictives** sur **11 métiers**, le nom étant le seul élément variant. Taux de rappel d'environ **22,8 %** pour un nom à consonance maghrébine contre **33,3 %** pour un nom à consonance française, soit un écart relatif d'environ **−31,5 %** ([Note IPP n° 76, nov. 2021](https://www.ipp.eu/wp-content/uploads/2021/11/Note_IPP_n76_Discrimination-a-l_embauche-selon-l_origine.pdf) ; [DARES Analyses, testing discrimination à l'embauche](https://dares.travail-emploi.gouv.fr/sites/default/files/fc5a96e5fc19ccdcf46fd9d55339591b/Dares%20Analyses_testing_discrimination_embauche.pdf)). L'écart est nettement plus faible sur les métiers en tension. Un testing DARES distinct **n'a pas trouvé de discrimination à l'embauche selon le sexe** ([DARES Analyses, testing femmes-hommes](https://dares.travail-emploi.gouv.fr/sites/default/files/dfdbd457a11afc7f64a168d701e3f77b/Dares%20Analyses_testing_femmes-hommes.pdf)). Valat (2023, DARES Analyses n° 268) suggère que c'est moins l'origine maghrébine que la connotation arabo-musulmane du nom qui joue.
  **Réserve de méthode à signaler : je n'ai pas pu lire le texte du PDF de la note IPP** (PDF compressé non extractible dans cet environnement, pas d'outil d'extraction disponible). Les chiffres ci-dessus proviennent de l'indexation du PDF primaire et de synthèses. **À revérifier dans le PDF avant publication.**
  Usage pour le skill : ce fait justifie de proposer, **sans l'imposer**, une version du CV sans photo, parce que la photo ajoute un signal d'origine. C'est le choix du candidat, et le skill n'a pas à décider pour lui.
- Longueur : je n'ai **pas** trouvé de recommandation chiffrée de l'Apec. La page « Quelle longueur doit faire un CV ? » existe sur cadres.apec.fr mais son contenu ne m'a pas été renvoyé.

### 4.3 Allemagne

- **La photo est un usage fort mais sans aucune obligation.** Le fondement est l'**AGG** (*Allgemeines Gleichbehandlungsgesetz*, en vigueur depuis 2006) : la loi n'interdit pas la photo, elle interdit la discrimination. Un employeur ne peut donc pas exiger de photo, et un refus motivé par l'absence de photo peut ouvrir une demande de dommages-intérêts au titre du **§ 15 AGG**.
  **Niveau de preuve : B, et c'est une faiblesse à assumer.** Je n'ai trouvé **que des sites commerciaux allemands** (services de CV, photographes, job boards) pour ces points, aucune source juridique officielle ni décision de justice. Les chiffres de pratique qu'ils avancent (« 65–70 % des employeurs attendent une photo » attribué à StepStone/IQB ; « ~53 % des RH » attribué à Indeed) sont **non vérifiés et à ne pas citer**. Sources consultées : [bewerbomat.ch](https://www.bewerbomat.ch/de/wissen/lebenslauf-vorlage-schweiz), [lebenslauf-easy.de](https://lebenslauf-easy.de/bewerbungsfoto/), [business-on.de](https://www.business-on.de/lebenslauf-ohne-foto.html). **À faire vérifier sur le texte de l'AGG (§§ 1, 7, 15, 22) avant d'en faire une affirmation juridique.**
- **L'Allemagne a testé officiellement la candidature anonyme.** Projet pilote « *Anonymisierte Bewerbungsverfahren* » de l'**Antidiskriminierungsstelle des Bundes** (agence fédérale antidiscrimination), évalué par la **KOWA (Europa-Universität Viadrina)** et l'**IZA**, rapport final **avril 2012** ([rapport final PDF](https://www.antidiskriminierungsstelle.gov.de/SharedDocs/downloads/DE/publikationen/AnonymBewerbung/abschlussbericht_anonymisierte_bewerbungsverfahren_20120417.pdf) ; [rapport intermédiaire 2011](https://www.antidiskriminierungsstelle.gov.de/SharedDocs/downloads/DE/publikationen/AnonymBewerbung/zwischenbericht_anonym_20110616.html)).
  Résultats à présenter avec nuance : plus de **4 000 candidatures anonymisées** et **111 postes ou places pourvus** au bout de six mois ; bilan officiel positif ; indices d'un bénéfice **pour les femmes** (hausse de la probabilité d'une offre d'emploi) ; **en revanche l'effet sur les candidats d'origine immigrée n'a pas été établi** pour l'offre d'emploi selon un document IZA, alors qu'une amélioration des chances d'invitation est rapportée côté presse. Côté candidats interrogés, **45,3 %** préféraient la procédure anonymisée contre **35,8 %** la procédure classique. Étude vieille de plus de 13 ans.

### 4.4 Royaume-Uni

- **Pas d'interdiction légale de la photo** : c'est une convention, et il faut le dire ainsi. Ce qui est juridique, c'est l'interdiction de discriminer sur les **neuf caractéristiques protégées** de l'**Equality Act 2010** (dont l'âge, le handicap, la race, la religion, le sexe, l'orientation sexuelle).
- **Acas** (organisme public britannique de conseil en relations de travail) : les questions sur une caractéristique protégée ne sont admises que dans des cas limités — suivi statistique de l'égalité, aménagements raisonnables, action positive, exigence professionnelle réelle ([Acas, *Following discrimination law — Recruitment*](https://www.acas.org.uk/recruitment/follow-discrimination-law)).
- **Santé et handicap** : Acas indique qu'on **ne doit pas** poser de question sur la santé ou le handicap avant la sélection ou l'offre, sauf exception ; on peut toujours demander si des aménagements du processus sont nécessaires (même page).
- **Âge et date de naissance** : Acas déconseille de demander l'âge ou la date de naissance sur le formulaire ; demander n'est pas discriminatoire en soi, mais un candidat écarté pourra invoquer la question comme élément de preuve ([Acas, *Age discrimination: key points for the workplace*](https://www.acas.org.uk/sites/default/files/2024-04/age-discrimination-key-points-for-the-workplace.pdf) ; [Acas, *Preventing age discrimination*](https://www.acas.org.uk/age-discrimination/preventing-age-discrimination)). **GOV.UK** précise que la date de naissance ne peut figurer sur le formulaire que si un âge minimum est légalement requis, et relève sinon d'un formulaire de suivi séparé ([GOV.UK, *Discrimination in recruitment*](https://www.gov.uk/employer-preventing-discrimination/recruitment)).
- **Situation familiale et enfants** : GOV.UK indique que l'employeur ne doit pas interroger un candidat sur sa situation matrimoniale ni sur ses projets d'enfants (même page).
- **La raison juridique, à énoncer correctement** : une photo, une date de naissance ou une nationalité sur le CV livrent à l'employeur des caractéristiques protégées qu'il n'a pas le droit d'utiliser. Elles **exposent l'employeur** à un contentieux et le mettent dans la position inconfortable de devoir prouver qu'il ne s'en est pas servi. C'est pourquoi beaucoup d'employeurs britanniques écartent ou anonymisent ces CV : **le CV avec photo crée un risque pour le recruteur, pas seulement pour le candidat.** C'est l'argument à donner, plutôt que « c'est illégal » — ce qui est faux.
- Voir aussi [EHRC, *Your Rights to Equality at Work: When You Apply for a Job*](https://www.equalityhumanrights.com/sites/default/files/your_rights_to_equality_at_work_-_applying_for_a_job.pdf).

### 4.5 États-Unis

- **L'EEOC déconseille explicitement à l'employeur de demander une photo**, et indique qu'une photo peut être obtenue à des fins d'identification **après** qu'une offre a été faite et acceptée ([EEOC, *Prohibited Employment Policies/Practices*](https://www.eeoc.gov/prohibited-employment-policiespractices)).
- **EEOC, race** : l'employeur doit éviter de demander des informations qui révèlent ou tendent à révéler la race d'un candidat en l'absence de nécessité professionnelle légitime ; quand une donnée raciale est nécessaire (action positive, suivi des flux de candidatures), l'EEOC suggère des **feuillets détachables** (« tear-off sheets ») séparés du dossier d'évaluation. Ces questions « *may be used as evidence of an employer's intent to discriminate unless the questions asked can be justified by some business purpose* » ([EEOC, *Pre-Employment Inquiries and Race*](https://www.eeoc.gov/pre-employment-inquiries-and-race)).
- **Petites entreprises** : l'EEOC recommande d'éviter les questions sur les caractéristiques protégées — race, couleur, religion, sexe, origine nationale, âge ([EEOC, *What shouldn't I ask when hiring?*](https://www.eeoc.gov/employers/small-business/what-shouldnt-i-ask-when-hiring)).
- **Formulation juridiquement exacte, à ne pas déformer** : il n'est **pas illégal** qu'un candidat mette sa photo sur son CV. Ce qui est illégal, c'est de discriminer. La guidance de l'EEOC s'adresse à l'**employeur**, et c'est ce qui produit l'effet pratique : de nombreux employeurs américains ont pour consigne interne d'écarter ou d'anonymiser les CV avec photo, précisément pour pouvoir prouver qu'ils n'ont pas vu l'information. Un CV américain avec photo peut donc être écarté **par prudence juridique de l'employeur**, ce qui est le pire des scénarios pour le candidat : écarté sans examen et sans motif communiqué.
- **Réserve** : la page EEOC sur la photo est ancienne. À revérifier dans sa version courante avant toute affirmation catégorique.
- Conséquence : **pas de photo, pas de date de naissance, pas de nationalité, pas de situation familiale, pas de genre, pas de numéro de sécurité sociale.** Pour le droit de travailler, la formule usuelle est « authorized to work in the US » ou la mention du visa quand c'est pertinent. Le CV américain porte « Resume », pas « CV » — « CV » y désigne le document académique long.

### 4.6 Canada

Le Canada offre les sources publiques les plus explicites de tout ce panorama, parce que les commissions provinciales publient des listes question par question.

- **Commission des droits de la personne de la Saskatchewan** ([ressources employeurs](https://saskhrc.ca/for-employers/resources/)), verbatim :
  - Photo : avant l'embauche, « *don't ask for photo* » ; après l'embauche, « *may ask for photos if needed* ».
  - Âge : ne pas demander de document révélant l'âge — « *don't ask for any record (like birth certificate)* ». On peut demander si le candidat a moins que l'âge minimum légal.
  - Acte de naissance : à ne pas demander avant l'embauche ; possible après.
  - Situation familiale : ne pas demander « *single, married, remarried, engaged, divorced* » ; ne pas demander son nom de naissance à une femme. Si le poste exige des déplacements, on peut demander si le candidat y est disposé.
  - Nationalité et lieu de naissance : « *Don't ask about birthplace or national origin* », « *Don't ask about an applicant's citizenship status* » ; on peut demander si le candidat est **légalement autorisé à travailler au Canada**.
- **Commission ontarienne des droits de la personne**, guide d'embauche : les questions liées à l'âge sont prohibées, y compris « *Are you 18 years of age or older and less than 65 years of age?* », sauf exceptions étroites ([*Hiring? A Human Rights Guide*, OHRC](https://www.toronto.anglican.ca/wp-content/uploads/2020/11/human_rights_hiring_guide.pdf)).
- **Loi canadienne sur les droits de la personne** : **13 motifs de distinction illicite**, dont la race, l'origine nationale ou ethnique, la couleur, la religion, l'âge, le sexe, l'orientation sexuelle, l'identité ou l'expression de genre, l'état matrimonial, la situation de famille, les caractéristiques génétiques, la déficience et l'état de personne graciée ([Loi, texte intégral, Justice Canada](https://laws-lois.justice.gc.ca/eng/acts/h-6/fulltext.html)). Attention au partage de compétences : si l'employeur est de compétence provinciale, c'est le code provincial qui s'applique.
- Conséquence CV : pas de photo, pas d'âge, pas d'état matrimonial, **jamais de NAS**. Un CV sans photo est la norme.
- **Non vérifié** : plusieurs sites affirment que « le gouvernement du Canada déconseille la photo ». Je n'ai **pas** trouvé la page officielle correspondante. Ne pas attribuer cette recommandation au gouvernement fédéral sans l'avoir trouvée.

### 4.7 Suisse

- **La photo est l'usage le plus fort des pays examinés, et pourtant juridiquement facultative.** Un portail d'emploi suisse va jusqu'à écrire qu'il n'est pas obligatoire d'en joindre une **même lorsqu'elle est expressément demandée** ([jobagent.ch](https://www.jobagent.ch/ratgeber-tools/checklisten-tipps-tricks/obligatorisches-bewerbungsfoto)). En pratique, l'absence de photo peut être lue comme une négligence ([livingease.ch](https://livingease.ch/blog/de/schweizer-lebenslauf-guide-2026)), particulièrement dans les métiers en contact client et les postes d'encadrement ([nexaria.ch](https://www.nexaria.ch/faq/lebenslauf-bewerbung/foto-im-lebenslauf/)).
- Date de naissance et nationalité : attendues en pratique, formellement facultatives ([fotoklar.com](https://fotoklar.com/de/ratgeber/lebenslauf-schweiz-foto)).
- Longueur : **2 pages maximum** ; le dossier complet comprend lettre, CV et annexes (certificats de travail, diplômes) ([bewerbungsmeister.ch](https://bewerbungsmeister.ch/blogs/bewerbungstipps/lebenslauf-schweiz-2025-muster-und-beispiele)).
- Photo en haut à droite, portrait professionnel, pas de selfie.
- **Niveau de preuve : B/C.** Toutes ces sources sont des prestataires (plateformes d'emploi, photographes, services de CV). **Aucune source officielle suisse trouvée.** À traiter comme des usages rapportés, pas comme des règles.

### 4.8 Afrique de l'Ouest francophone

**Section faible, et je préfère le dire que meubler.** Je n'ai trouvé **aucune** source officielle ni étude, pays par pays, sur les conventions de CV au Sénégal, en Côte d'Ivoire, au Burkina Faso ou ailleurs dans la zone.

Le seul élément exploitable : [Jeune Afrique, *Comment rédiger un CV pour l'Afrique francophone ?*](https://www.jeuneafrique.com/emploi-formation/520101/comment-rediger-un-cv-pour-lafrique-francophone/) qui indique qu'**il n'existe pas de particularismes nationaux** dans la zone, que la **photo d'identité est facultative** (en évitant les photos fantaisistes), que les recruteurs reçoivent un volume élevé de candidatures par poste, et recommande la sobriété : une seule police, peu de couleurs, rubriques bien distinctes.

Une piste non explorée : un **modèle de CV de la CEDEAO** existerait en anglais, français et portugais ([mention sur un blog](https://phgarin.wordpress.com/2016/07/27/le-cv-africain-de-la-cedeao/)). **Je n'ai pas vérifié son contenu** ni s'il requiert photo ou situation matrimoniale.

Ce que le skill doit faire ici : **demander à l'utilisateur** plutôt que présumer. Mentionner que l'usage régional rapporté tolère des mentions personnelles (nationalité, situation matrimoniale) que les conventions anglo-saxonnes proscrivent, et que ces mentions deviennent un handicap dès que la candidature cible un employeur britannique, américain ou canadien, y compris implanté localement (ONG, institutions internationales, filiales). **La règle à retenir est celle du pays de l'employeur et de son siège, pas celle du pays de résidence du candidat.**

---

## 5. Ce qui fait rejeter un CV

### 5.1 Formulations creuses — liste de remplacement

Base sourcée : LinkedIn publiait une liste annuelle des mots les plus surutilisés dans les profils. Relevés par la presse :
- édition rapportée en 2013 (4ᵉ annuelle) : *Responsible, Strategic, Creative* en tête ([Forbes, Susan Adams, 11 déc. 2013](https://www.forbes.com/sites/susanadams/2013/12/11/ten-buzzwords-to-cut-from-your-linkedin-profile-3/)).
- édition rapportée vers 2014-2015 : *Motivated, Passionate, Creative* en tête ([Nylon](https://www.nylon.com/articles/linkedin-overused-profile-words)).
- édition rapportée vers 2017 (6ᵉ annuelle) : *Specialized, Leadership, Passionate, Strategic, Experienced, Focused, Expert, Certified, Creative, Excellent* ([CNBC, 25 janv. 2017](https://www.cnbc.com/2017/01/25/the-10-most-overused-buzzwords-that-you-should-delete-from-your-resume.html) ; [CIO](https://www.cio.com/article/251231/the-10-most-overused-linkedin-buzzwords.html)).
**Réserves** : les sources divergent sur la numérotation des éditions ; un blog affirme que LinkedIn a arrêté cette liste en 2018 et **je n'ai pas pu le confirmer**. Je n'ai pas trouvé d'édition récente. À citer comme un relevé daté, pas comme un classement courant.

Le tableau ci-dessous est une **synthèse éditoriale** : le diagnostic (« non vérifiable », « non différenciant ») est un raisonnement, pas une donnée d'étude. Le test unique est : *un candidat médiocre pourrait-il écrire exactement la même phrase ?* Si oui, la phrase ne dit rien.

**Français**

| Formulation creuse | Pourquoi elle échoue | Remplacement |
|---|---|---|
| Passionné par… | Non vérifiable, tout le monde l'écrit | Une preuve d'activité : projet personnel, contribution, certification obtenue hors cadre scolaire |
| Dynamique, motivé, sérieux | Autoévaluation sans preuve | Supprimer. Un résultat chiffré porte l'information |
| Esprit d'équipe | Non différenciant | « Coordonné 5 contributeurs sur 3 mois » |
| Bon relationnel | Non mesurable | « Formé 12 nouveaux arrivants », « animé le comité client mensuel » |
| Rigoureux | Autoévaluation | « Ramené le taux d'erreur de saisie de 4 % à 0,5 % » |
| Autonome | Autoévaluation | « Pilote seul le budget de 40 k€ de l'activité » |
| Force de proposition | Jargon vide | « Proposé et mis en œuvre X, adopté par les 3 autres équipes » |
| Polyvalent | Signale souvent l'absence de spécialité | Nommer les deux ou trois domaines réellement maîtrisés |
| Maîtrise du Pack Office | Attendu par défaut, occupe une ligne pour rien | Supprimer, sauf niveau réel distinctif (Excel : VBA, Power Query) |
| Participation à / Intervention sur | Verbe faible, dilue la responsabilité | Verbe d'action précis : conçu, automatisé, négocié, déployé |
| Était en charge de / Responsable de | Décrit la fiche de poste, pas l'action | Le verbe de l'action réellement menée |
| Bonne connaissance de… | Gradation floue | Un fait : « 3 ans d'usage quotidien », « certification X obtenue en 2025 » |
| À l'écoute du client | Slogan | « Taux de satisfaction maintenu à 92 % sur 400 tickets » |
| Souhaite relever de nouveaux défis | Dit du candidat, pas du poste | L'intitulé du poste visé et la compétence qui le justifie |
| Capacité d'adaptation | Autoévaluation | Un fait d'adaptation : changement de secteur, de pays, d'outil, avec le résultat |

**Anglais**

| Formulation creuse | Pourquoi elle échoue | Remplacement |
|---|---|---|
| Passionate about… | Figurait en tête des listes LinkedIn ; non vérifiable | Une preuve d'activité |
| Team player | Non différenciant | « Led a 5-person cross-functional team for 3 months » |
| Hard-working, motivated, dynamic | Autoévaluation | Supprimer |
| Results-driven / results-oriented | Dit « résultats » sans en donner un | Donner le résultat |
| Detail-oriented | Autoévaluation, ironique s'il reste une coquille | « Cut data-entry error rate from 4% to 0.5% » |
| Excellent communication skills | Non mesurable | « Presented quarterly results to a 40-person leadership forum » |
| Strategic / Leadership / Specialized / Experienced / Expert | Relevés par LinkedIn comme les plus surutilisés | Le fait concret que le mot prétend résumer |
| Think outside the box / synergy / go-getter | Jargon | Supprimer |
| Responsible for… | Fiche de poste, pas action | Verbe d'action + résultat |
| Helped with / Assisted in / Involved in | Verbe faible, efface la contribution | Dire ce qui a été fait, et avec qui, honnêtement |
| Familiar with / Working knowledge of | Gradation floue | « 3 years' daily use », la certification, le lien vers le code |
| References available upon request | Occupe une ligne sans informer ; attendu par défaut | Supprimer |
| Proficient in Microsoft Office | Attendu par défaut | Supprimer, sauf compétence réellement distinctive |
| Self-starter / Go-to person | Autoévaluation | Un fait d'initiative avec son effet |
| Seeking a challenging position where I can grow | Centré sur le candidat | L'intitulé du poste visé et la preuve d'aptitude |

Verbes faibles → verbes d'action : *participé à, aidé à, contribué à (seul), était chargé de, a été impliqué dans, suivi, géré (générique)* → **conçu, construit, automatisé, migré, négocié, réduit, accéléré, lancé, recruté, formé, chiffré, arbitré, livré**. Nuance importante : **« contribué à » reste le mot juste quand la contribution était partielle** — l'éliminer systématiquement pousse au mensonge. Il faut l'éliminer comme cache-misère, pas comme aveu d'honnêteté.

### 5.2 Trous inexpliqués

**Donnée solide, publiée, relue par les pairs — la meilleure de cette fiche sur ce point :**
Kroft, Lange & Notowidigdo, *Duration Dependence and Labor Market Conditions: Evidence from a Field Experiment*, **Quarterly Journal of Economics**, 2013, vol. 128, n° 3, p. 1123-1167
([QJE](https://academic.oup.com/qje/article-abstract/128/3/1123/1852133) ; [NBER WP 18387](https://www.nber.org/system/files/working_papers/w18387/w18387.pdf) ; [PDF auteur](https://faculty.wcas.northwestern.edu/noto/research/Kroft_Lange_Noto_Resume_Study.pdf) ; [résumé J-PAL](https://www.povertyactionlab.org/evaluation/dependence-duration-and-labor-market-conditions-evidence-united-states)).

Méthode : environ **12 000 CV fictifs** envoyés à de vraies offres dans **100 villes américaines**, avec randomisation du statut d'emploi et de la **durée du chômage en cours, de 1 à 36 mois**.
Résultats : le taux de rappel **décroît avec la durée**, et cette décroissance est **concentrée sur les huit premiers mois** — à 8 mois, le rappel est inférieur d'environ **45 %** à celui observé à 1 mois (d'environ **7 % à 4 %**). **Au-delà de huit mois, le temps supplémentaire ne réduit plus le taux de rappel.** L'effet est plus marqué quand le marché local du travail est tendu. La mesure porte sur le **rappel par l'employeur**, pas sur l'offre d'emploi.

Deux conséquences contre-intuitives, et importantes pour un skill :
1. **La pénalité est précoce, pas cumulative.** Un trou de 2 ans ne coûte pas beaucoup plus qu'un trou de 10 mois. Il est donc inutile de maquiller un trou long ; il est en revanche utile d'agir vite sur un trou court.
2. **Le trou récent est celui qui coûte** — ce qui plaide pour mentionner l'activité en cours, même non salariée (formation, projet, entrepreneuriat, soin d'un proche), plutôt que de laisser une absence de ligne.

Traitement recommandé, à présenter comme convention et non comme donnée :
- Dates en **mois + année** partout, de façon homogène. Une granularité annuelle seule peut masquer involontairement un trou et créer un doute.
- Nommer le trou sobrement, sur une ligne, avec ce qui a été fait : « 2024-2025 — Reprise d'études / Formation X », « 2023 — Congé parental », « 2022-2023 — Projet entrepreneurial ».
- **Ne jamais étirer une date pour couvrir un trou** : les dates d'emploi figurent au premier rang des écarts détectés en vérification d'antécédents (§5.3).

### 5.3 Mensonges vérifiables

**Donnée la plus récente et la plus large disponible :** *HireRight 2025 Global Benchmark Report*, plus de **1 000 professionnels RH, risque et acquisition de talents** dans le monde, terrain du **11 février au 9 mars 2025**
([communiqué HireRight](https://www.hireright.com/company/newsroom/hireright-releases-2025-global-benchmark-report) ; [rapport PDF](https://assets.ctfassets.net/tmcb0v2sc9iu/7FkVYtVhoGh5hb5N7ojhJr/8db02423e2a116b415812b37255b9495/2025_-Benchmark-_Report.pdf) ; [People Management](https://www.peoplemanagement.co.uk/article/1923118/nine-10-businesses-report-candidate-discrepancies-during-screening-process-report-finds)).

- **Plus des trois quarts** des entreprises ont trouvé au moins un écart entre les déclarations d'un candidat et la vérification, sur les 12 derniers mois.
- Les types les plus fréquents : **condamnations non déclarées**, puis **écarts sur la formation et l'emploi**.
- Zone **EMEA** (donc France incluse) : **90 %** des entreprises ont rencontré des écarts. Les plus fréquents : **historique d'emploi 64 %**, **diplômes 47 %** ; **22 %** ont découvert une condamnation non déclarée.
- **Réserves** : HireRight **vend des vérifications d'antécédents** — intérêt direct à ce que le chiffre soit élevé ; c'est une **enquête déclarative auprès d'employeurs**, pas une mesure du taux de mensonge des candidats. « 90 % des entreprises ont vu au moins un écart » ne veut **pas** dire « 90 % des candidats mentent ». Un « écart » inclut l'erreur de date de bonne foi.
- **À ne pas citer** : les chiffres de 84 %, 85 % et 88 % de « misrepresentation » qui circulent proviennent d'enquêtes HireRight plus anciennes (88 % = benchmark 2016) ou de blogs sans source. Les chiffres « 41 % d'offres retirées » et « 18 % de licenciements » viennent d'un blog de faible qualité et **ne doivent pas être utilisés**.

Ce qui est **mécaniquement vérifiable**, et donc à ne jamais falsifier : diplôme et année d'obtention (registres, écoles, services de vérification) ; dates d'emploi et intitulé de poste (anciens employeurs, URSSAF/attestations, LinkedIn) ; certifications à numéro (AWS, PMP, CPA, ordres professionnels) ; permis et habilitations ; niveau de langue certifié (TOEIC, IELTS, DELF) ; droit de travailler. Les mensonges les plus fréquents et les plus faciles à prendre : **promotion antidatée, intitulé gonflé (« Directeur » pour un poste de chargé de mission), diplôme « en cours » présenté comme obtenu, et étirement de dates pour masquer un trou** — exactement les deux catégories en tête du rapport HireRight.

Position du skill : **refuser d'écrire une affirmation fausse, y compris par euphémisme.** Il existe presque toujours une formulation vraie et forte : « Master 2 X — en cours, obtention prévue 2027 » ; « cofondateur, équipe de 2 » ; « gestion opérationnelle d'un portefeuille de 40 k€ » au lieu de « directeur financier ».

### 5.4 Fautes et incohérences

Aucune des docs éditeurs lues ne parle d'orthographe, et je n'ai **pas** trouvé d'étude quantifiant l'effet d'une faute sur le taux de rappel. Les chiffres qui circulent (« X % des recruteurs rejettent au premier typo ») sont de niveau C. Le skill doit donc traiter la relecture comme une **exigence professionnelle évidente**, sans l'appuyer sur une statistique inventée.

Checklist de cohérence, à valeur opérationnelle :
- Dates qui se chevauchent ou laissent un trou non expliqué.
- Total d'expérience annoncé dans l'accroche ≠ somme des dates.
- Intitulé de poste du CV ≠ intitulé sur LinkedIn (écart le plus facilement repéré par un recruteur).
- Niveau de langue incompatible avec le CV lui-même (« anglais courant » sur un CV anglais fautif).
- Compétence listée mais absente de toute expérience.
- Un même employeur orthographié de deux façons.
- Mélange de temps et de personnes (« je gère » / « gestion de » / « a géré » sur la même page).
- Placeholders résiduels : un nom ou une ville factices sont **ignorés par le parser de Greenhouse** (§1.2).

---

## 6. Ce que je n'ai pas pu vérifier — à ne pas affirmer

1. **La méthode des études TheLadders (6 s / 7,4 s)** : les trois URL TheLadders renvoient HTTP 403, web.archive.org est inaccessible. Effectifs, durée, matériel, définition de la mesure : **inconnus**. Niveau C tant que la source primaire n'a pas été lue.
2. **L'étude MDPI 2023 sur l'eye-tracking des recruteurs** : HTTP 403. Effectifs et résultats non lus. C'est la seule étude relue par les pairs identifiée sur le sujet.
3. **Le texte du PDF de la note IPP n° 76** : non extractible dans cet environnement (aucun outil d'extraction PDF disponible). Les chiffres 22,8 % / 33,3 % / 9 600 / 11 métiers viennent de l'indexation du PDF primaire et de synthèses, pas de ma lecture du texte.
4. **Le droit allemand sur la photo (AGG)** : aucune source officielle ni jurisprudence trouvée, seulement des sites commerciaux allemands. À faire confirmer sur le texte de l'AGG.
5. **Les conventions suisses** : aucune source officielle. Uniquement des prestataires de services de candidature.
6. **L'Afrique de l'Ouest francophone** : aucune source officielle, aucune étude. Une seule source de presse (Jeune Afrique). Le modèle CEDEAO n'a pas été vérifié.
7. **Les positions de Lever et Workday sur les colonnes** : non publiées. Toute affirmation sur leur tolérance est une extrapolation.
8. **La détection automatisée du texte blanc** par Greenhouse ou Lever : revendiquée par des blogs, non confirmée.
9. **La part d'employeurs activant un auto-rejet sur contenu** : aucune source fiable. Le « 8 % » circulant repose sur 25 recruteurs interrogés par un éditeur de CV.
10. **La page Apec sur les ATS** : HTTP 403 à la lecture directe ; les citations viennent de l'index du moteur de recherche. À revérifier.
11. **La limite de 100 Ko de Taleo** : documentée pour Taleo Enterprise 21B, document ancien. Non vérifiée pour Oracle Recruiting Cloud.
12. **La recommandation de longueur de l'Apec** : page identifiée, contenu non obtenu.
13. **L'année exacte de création de STAR par DDI** (1974 ?) : pas de source indépendante.
14. **« Le gouvernement du Canada déconseille la photo »** : page officielle non trouvée.
15. **L'arrêt de la liste annuelle des buzzwords LinkedIn en 2018** : non confirmé.
16. **Le « ~20 % de CV multi-colonnes »** attribué par un moteur de recherche à arXiv 2510.09722 : **absent du résumé de l'article**. Ne pas citer.

## 7. Chiffres à ne jamais utiliser

- **« 75 % des CV rejetés par les ATS »** et ses variantes 70 % / 88 % — origine : argumentaire commercial Preptel 2012, société disparue, aucune méthode publiée.
- **« 6 secondes »** ou **« 7,4 secondes »** présentés comme un fait établi — étude commerciale à méthode non publiée, inaccessible.
- **« 84 % / 85 % / 88 % des candidats mentent »** — enquêtes anciennes ou blogs sans source.
- **« 41 % d'offres retirées, 18 % de licenciements »** après découverte d'un mensonge — blog de faible qualité.
- **« Une étude de Harvard montre que l'usage naturel des mots-clés surpasse le bourrage de 57 % »** — rencontré dans les résultats de recherche, **aucune source primaire trouvée**. Probablement fabriqué.
- **« Seulement 8 % des recruteurs activent l'auto-rejet »** — 25 répondants, éditeur de CV.
- **« 65-70 % des employeurs allemands attendent une photo »** — attribué à StepStone/IQB sans référence vérifiable.

---

## 8. Synthèse en dix règles, chacune avec son fondement

1. **Une colonne, texte réel, PDF exporté depuis l'original.** Greenhouse liste « columned layout » parmi ses causes d'échec ; Textkernel rate encore ~18 % des séparateurs de colonne ; Textkernel demande le fichier d'origine. *(A)*
2. **Nom et coordonnées dans le corps du document, jamais en en-tête, pied de page ou zone de texte.** Greenhouse, verbatim. *(A)*
3. **Aucun tableau, aucune barre de niveau, aucune icône en remplacement d'un libellé.** Greenhouse pour les tableaux ; Textkernel pour la casse des paires clé-valeur. *(A)*
4. **Jamais de PDF scanné, aplati ou protégé par mot de passe.** SAP ne fait pas d'OCR ; Taleo ne parse pas les images ; Workday déconseille les images. *(A)*
5. **Fichier léger (< 500 Ko), intitulés de poste complets, noms d'entreprise avec leur forme juridique.** Greenhouse 2,5 Mo, Taleo 100 Ko, exigences verbatim de Greenhouse. *(A)*
6. **Titres de rubriques standards et sections nettement séparées.** Greenhouse exige « clear sections » ; l'Apec dit la même chose pour la France. *(A/B)*
7. **Écrire les puces en XYZ** — résultat, mesure, moyen — en se servant de STAR/CAR comme grille d'extraction orale. Et donner la base du pourcentage, comme Bock y insiste. *(A pour l'origine, convention pour l'usage)*
8. **Quantifier sans inventer** : huit substituts licites quand le chiffre est confidentiel (§3.4) ; refuser le chiffre fabriqué, qui ne survit pas à « comment l'avez-vous mesuré ? ». *(règle de probité)*
9. **Adapter aux conventions du pays de l'employeur**, pas du candidat : photo et date de naissance d'usage en France, Allemagne et Suisse ; à retirer pour le Royaume-Uni, les États-Unis et le Canada — non pas parce que c'est illégal pour le candidat, mais parce que cela expose l'employeur à un contentieux sur une caractéristique protégée et le pousse à écarter le dossier par prudence. *(A : EEOC, Acas, GOV.UK, commissions canadiennes)*
10. **Rien de vérifiable qui soit faux.** Historique d'emploi (64 %) et diplômes (47 %) sont les deux premiers postes d'écarts détectés en EMEA selon HireRight 2025. Et un trou coûte surtout dans ses huit premiers mois (Kroft et al., QJE 2013) : il vaut mieux l'expliquer que le maquiller. *(A/B)*
