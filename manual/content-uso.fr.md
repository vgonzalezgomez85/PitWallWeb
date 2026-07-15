# Manuel d'utilisation — PitWall (organisation / direction de course)

Guide destiné à celui qui **opère** PitWall : monter la course, la diriger en direct, corriger des tours et sortir les résultats.

---

## 1. Introduction
![img: 01-home.png]

**PitWall** est le système de chronométrage et de gestion de courses de slot. Il détecte le passage de chaque voiture sur la ligne d'arrivée grâce au matériel de chronométrage, avec deux options compatibles :

- **DS-300** — par **port série**. Tu peux relier **jusqu'à 6 circuits** DS-300 dans une seule course : chaque boîtier chronomètre ses voies et PitWall les combine. Chaque boîtier utilise **son propre port** (un boîtier = un port).
- **DS-300 agrégateur** — lorsqu'un **appareil agrégateur** regroupe **plusieurs boîtiers DS-300 (de 2 à 4) sur un seul port COM**. PitWall sépare les boîtiers par leur identifiant de trame et numérote les voies à la suite (boîtier 1 → 1–8, boîtier 2 → 9–16, et ainsi de suite jusqu'à **32 voies** avec 4 boîtiers). Un **seul signal de départ** lance tous les boîtiers en même temps.
- **BART (Policar)** — par **Bluetooth**. Il admet **jusqu'au nombre maximal de voies que permet BART** (actuellement **32**).

Tu peux utiliser n'importe laquelle de ces sources ; pour PitWall le flux de passages est équivalent.

- Depuis l'**écran d'accueil**, tu accèdes aux **Courses**, aux **Réglages** et au reste des modules.
- En bas à droite, tu vois toujours l'**état de la liaison** (vert = connecté ; « Sans signal » = vérifie le câble/port ou le Bluetooth).

**La liste des courses** te montre toutes tes courses avec leur état (en attente / active / terminée) et le bouton *Nouvelle course (« + Nueva carrera »)*.

![img: 02-races-list.png]

## 2. Scénarios, catégories et catalogues (ta bibliothèque)

Pour ne pas reconfigurer la même chose à chaque course, PitWall enregistre des **modèles réutilisables** que tu choisis ensuite au moment de créer une course.

**Scénarios (circuits enregistrés).** Un **scénario** est une piste physique enregistrée : nombre de circuits et de voies (par ex. `8+8+8 = 24`), sa **séquence de voies** (rotation) et le **temps minimum par défaut**. Toute course affectée à ce scénario en hérite automatiquement.

![img: op-escenarios.png]

Lors de l'édition d'un scénario, tu définis son nom, la configuration des voies, tu fais glisser la **séquence de rotation** (avec des **repos DSC** s'il y a trop de pilotes), le **temps minimum par défaut** et, en option, des **tours minimums par catégorie** (un Pt différent pour GT, Tourisme, Classiques… sur cette même piste).

![img: op-escenario-form.png]

**Catégories.** Groupes de niveau/classe (GT, Tourisme, Classiques…) qui servent à **surcharger le temps minimum (Pt) par catégorie** dans chaque scénario et à classer voitures et pilotes.

![img: op-categorias.png]

**Catalogues réutilisables (pilotes, équipes, voitures).** Tiens à jour ta **base de données** de participants et de matériel pour la réutiliser d'une course à l'autre :
- **Pilotes** — nom et catégorie ; chaque pilote peut avoir son **QR** d'identification.
- **Équipes** — nom, couleur, pays, voiture et membres.
- **Voitures** — marque, modèle et catégorie.

Tous peuvent être **importés en bloc depuis un CSV** (boutons *Modèle CSV (« Plantilla CSV »)* et *Importer CSV (« Importar CSV »)*, avec un aperçu des nouveautés vs. doublons) et exportés.

![img: op-catalogo-pilotos.png]

![img: op-qr-pilotos.png]

> Avec *Exporter QR (« Exportar QR »)*, tu imprimes les cartes QR de tous les pilotes (pour le changement de pilote par scan en endurance — voir *Contrôle des relais*).

## 3. Créer une course
![img: 03-wizard-step1.png]

Appuie sur *Nouvelle course (« + Nueva carrera »)* et suis l'assistant :

- **Type** :
  - *Sprint* → une **course rapide**, de **pilotes ou d'équipes**.
  - *Endurance* → une **course d'endurance** (par équipes), qui ajoute le **contrôle du temps couru par chaque pilote** de l'équipe (voir *Contrôle des relais de pilote*).
- **Voies et circuits** : nombre total de voies et répartition entre les boîtiers (par ex. 8+8+6 = 3 boîtiers DS-300).
- **Temps minimum de tour (Pt)** : en dessous de ce temps, un passage est considéré comme **fantôme** (rebond/double lecture) et ne compte pas.
- **Passages** : combien de fois la **séquence de voies entière** est parcourue. 2 passages = la rotation complète est courue 2 fois (deux fois plus de manches).
- **Répéter la voie** : chaque voie est courue ce nombre de **manches d'affilée** (même voie), en cumulant les tours — pour comparer chaque répétition.
- **Pole** (facultatif) et **règles de pilote** (championnat uniquement : min/max par pilote, blocage de changement en fin de manche).

> Les **passages** et la **répétition de voie** ne changent que la façon dont les manches sont générées ; les totaux se cumulent par participant.

> Tu gères le championnat avec **PitWall Control** ? Pas besoin de ressaisir les équipes et la rotation : tu peux **importer l'épreuve** entière depuis Control (voir *Importer une série de PitWall Control*).

## 4. Importer une série de PitWall Control
![img: op-import-tanda.png]

Si tu organises le championnat avec **PitWall Control** (le gestionnaire de saison), tu peux y monter l'épreuve —équipes, coupes, voies et rotation— et la transmettre à PitWall **sans rien ressaisir**. PitWall **crée automatiquement la course** à partir de ce qu'il reçoit.

Entre dans **Courses → Importer une série (« Importar tanda »)**. Il y a **deux façons** d'apporter l'épreuve :

- **Fichier JSON.** Dans Control, tu appuies sur **Exporter la série (JSON)** et tu enregistres le fichier ; dans PitWall, tu le **téléverses** sur l'écran d'import.
- **Par réseau (Wi-Fi/LAN).** Dans Control, tu appuies sur **Envoyer à PitWall** : Control **détecte** ton PitWall sur le réseau local (ou tu lui indiques l'**IP** à la main) et demande un **PIN d'appairage**. Ce PIN est celui qu'affiche l'écran **Importer une série** de PitWall — saisis-le dans Control pour autoriser l'envoi.

**Ce que crée PitWall.** Chaque **manche** de l'épreuve de Control devient une **série**, avec chaque équipe placée sur sa **voie de départ**. Les **repos** (`D1`, `D2`…) sont placés et tournent comme dans n'importe quelle rotation (voir *Séries, participants et rotation*).

**Avec pole.** Si l'épreuve a une pole (interrupteur **La course a une pole** dans Control ; à l'export vers fichier, il te le demande), Control **n'envoie pas l'ordre des voies**. Sur l'écran d'import de PitWall, coche **Cette course a une pole** : PitWall crée la course avec la **séance de pole** (toutes les équipes) et la grille se décide **après avoir couru la pole** (voir *Pole*).

> Juste après l'import, tu peux **éditer la course** pour lui attribuer le **scénario** de ton club (et hériter de ses voies, sa séquence et son temps minimum) — voir *Éditer la course, les séries et les manches*.

> **Prérequis :** pour l'envoi par réseau, PitWall et PitWall Control doivent être sur le **même réseau** LAN/Wi-Fi. Le PIN d'appairage s'affiche dans **Importer une série** de PitWall. L'autre moitié du pont —**récupérer les résultats** vers Control— est expliquée dans le *Manuel de PitWall Control*.

## 5. Séries, participants et rotation
![img: 34-tanda.png]

Une **série** regroupe les participants et leur **rotation de voies** par manche. Lorsque tu ajoutes les **équipes/pilotes**, PitWall génère automatiquement toutes les **manches**.

**Comment fonctionne la rotation.** Chaque participant change de voie de manche en manche en suivant la séquence configurée (par ex. `1, 3, 5, 6, 4, 2`). Ainsi, tout le monde passe par toutes les voies et les conditions s'égalisent.

- *Exemple (6 voies, 6 pilotes) :* dans la manche 1, le pilote A court sur la voie 1 ; dans la manche 2, la 3 ; dans la 3, la 5… jusqu'à avoir fait le tour de toutes les voies.

**Rotation à ta guise.** PitWall propose automatiquement une rotation équilibrée, mais **tu peux la gérer comme tu veux** : réordonne la **séquence de voies** à la main (en faisant glisser) pour décider exactement par quelle voie passe chaque participant à chaque manche.

**Repos.** S'il y a **plus de participants que de voies**, la séquence inclut des trous (`0` / `DSC`) qui sont des **repos** : dans cette manche, ce participant ne court pas. PitWall les répartit de façon équilibrée, mais **tu peux aussi les placer où tu veux** dans la rotation (fais-les glisser à la position que tu préfères).

**Avec passages / répétition de voie :**
- *2 passages* → la séquence entière se répète : `1,3,5,6,4,2, 1,3,5,6,4,2`.
- *Répéter la voie 2* → chaque voie, deux manches d'affilée : `1,1,3,3,5,5,6,6,4,4,2,2`.

## 6. Éditer la course, les séries et les manches

Après avoir créé une course, tu peux la retoucher :
- **Éditer la course** — changer le **nom** et, **tant qu'il n'y a pas de tours enregistrés**, le **scénario**. Tu peux **attribuer** un scénario à une course qui n'en avait pas, le **changer** pour un autre ou le **retirer**. En **attribuant** un scénario, la course hérite de ses **voies**, de sa **séquence** de rotation et de son **temps minimum** (et des tours minimum par **catégorie**, s'il y en a), et PitWall **régénère les séries en attente** avec cette configuration ; en le **retirant**, la course passe en **mode manuel** en conservant sa configuration. S'il y a déjà des tours, le scénario reste **verrouillé** (pour ne pas casser les données).

![img: op-edit-carrera.png]

> Cas typique : tu **importes une série de PitWall Control** (qui arrive en mode manuel) puis tu l'**édites pour lui attribuer le scénario** de ton club, afin qu'elle hérite des voies, de la séquence et du temps minimum de ta piste.

- **Éditer la série** — changer les **noms** des participants et, si la série n'a pas encore commencé, sa composition. Si elle a déjà des manches lancées, elle passe en **mode renommer seulement** (on n'ajoute ni ne retire de participants, pour ne pas déséquilibrer la rotation).

![img: op-edit-tanda.png]

- **Éditer la manche** — changer **qui court sur chaque voie** dans une manche précise, sans régénérer toute la série (utile si une équipe ne se présente pas ou en cas de changement de dernière minute).

## 7. Pole (qualification préalable)
![img: 44-pole-setup.png]

La **pole** est un tour qualificatif **avant** la course pour décider l'ordre de départ. Elle est facultative ; elle s'active à la création de la course (**Pole**) et se lance depuis la page de la course → *Configurer la Pole Position (« Configurar Pole Position »)*.

- **Participants** : tous les inscrits apparaissent. L'**ordre de la liste** est l'ordre dans lequel ils sortiront faire leur tour ; appuie sur *🎲 Aléatoire (« 🎲 Aleatorio »)* pour le mélanger.
- **Voie de pole** : **tous** font leur tour qualificatif sur la **même voie** (pour que ce soit comparable). Choisis-la avec **−/+** ou avec *🎲 Aléatoire (« 🎲 Aleatorio »)*.
- Appuie sur *Commencer la Pole (« Empezar Pole »)* : chaque participant entre à tour de rôle, fait son tour et PitWall enregistre son meilleur temps. Dans le chronométrage, tu peux activer *Ignorer le 1er passage (out-lap) (« Omitir 1er cruce »)* pour ne pas compter le tour de lancement.

**Résultats de la pole.** À la fin apparaît *Résultats Pole (« Resultados Pole »)* avec le **classement final** (du plus rapide au plus lent, avec l'écart au leader et le **meilleur tour**). D'ici, tu peux *✏️ Éditer les temps (« ✏️ Editar tiempos »)* s'il y a eu une erreur, ou continuer avec *🚦 Attribuer les voies de départ (« 🚦 Asignar carriles de salida »)*.

![img: 46-pole-results.png]

**Attribuer les voies après la pole.** La pole ne répartit pas les voies automatiquement : elle ouvre l'écran *Choix de voie (« Elección de carril »)*, où chaque participant **choisit** sa voie **dans l'ordre du classement** — le **poleman** (le plus rapide) choisit en premier, puis le 2e, et ainsi de suite. C'est le classique « le plus rapide choisit sa voie ».

![img: 47-pole-lanes.png]

- La bannière *Choix en cours (« Eligiendo ahora »)* indique à qui c'est le tour ; à gauche tu vois l'**ordre de choix** (le classement) et à droite les **voies disponibles** (avec leur couleur).
- Chacun appuie sur la voie qu'il veut ; cette voie disparaît des disponibles et le tour passe au suivant.
- **S'il y a plus de participants que de voies**, des trous de *💤 Repos (« 💤 Descanso »)* apparaissent : celui qui choisit le repos **ne court pas la manche 1** et **entre dans la rotation à partir de la manche 2**.
- Quand tout le monde a choisi, appuie sur *🏁 Créer la Première Série (« 🏁 Crear Primera Tanda »)* : PitWall crée la série et génère toutes les manches avec cette grille comme point de départ (l'ordre de choix définit la position initiale dans la rotation des voies). À partir de là, la course fait tourner les voies de manche en manche comme d'habitude (voir *Séries et rotation*).

> La pole ne rapporte pas de points dans la course : elle décide seulement **qui choisit sa voie en premier** et, par là, la grille de départ de la première manche.

## 8. PitWall Lap — PIN pour les équipes
![img: 43-lap-pins.png]

**PitWall Lap** est la vue mobile qui permet à chaque **équipe/pilote** de suivre son propre chronométrage depuis le téléphone (ses tours, annoncés par la voix, et sa position). Pour qu'ils accèdent uniquement à *leur* panneau, un **PIN** est distribué par équipe.

- Entre dans **PitWall Lap · PINs** de la course. Tu verras l'adresse que les équipes ouvrent sur le mobile (par ex. `http://<IP-du-serveur>:3000/lap/<id>`) et le tableau **ÉQUIPE → PIN**.
- Donne à chaque équipe **son PIN**. En ouvrant l'adresse et en le saisissant, ils entrent directement sur leur panneau.
- *Nouveau (« Nuevo »)* régénère le PIN d'une équipe (au cas où il aurait fuité ou qu'ils veuillent le changer).

> Les mobiles doivent être sur le **même réseau** que l'ordinateur qui fait office de serveur. Utilise l'IP de la machine, pas `localhost`, quand ils l'ouvrent depuis le téléphone. Si tu veux que les équipes suivent la course **depuis l'extérieur du local** (par internet), voir *Suivi public par internet*.

## 9. Diriger la course en direct
![img: 20-live-timing.png]

Depuis la page de la course :

1. **Armer la manche** (▶). Elle reste prête, en attente du **GO** du boîtier.
2. **GO** : au moment du départ donné sur le boîtier, le **feu tricolore** apparaît et le chronomètre démarre. Chaque circuit a sa propre horloge (C1/C2/C3).
3. Pendant la manche, tu vois par voie : **total de tours**, **dernier**, **moyenne**, **meilleur**, et en haut la bannière du **meilleur tour**.
4. **Pause / Reprendre / Arrêter** la manche au besoin.
5. À la fin (drapeau ou fin de temps), la manche se ferme et la **suivante** se prépare.
6. Quand toutes les manches d'une série sont terminées, la **série suivante** démarre.

**Choisir la vue.** Avec le bouton *Vue (« Vista »)*, tu changes la mise en page selon les voies : *Lignes horizontales* (peu de voies), *Grille compacte* (beaucoup) ou *Cartes détaillées* (avec tours/sorties/pit/Δ par carte).

**Changer de série, répéter une manche et terminer.** Depuis le direct lui-même, tu as des raccourcis sans quitter l'écran :
- **Série suivante** — quand les manches d'une série se terminent, passe directement à la suivante.
- **Répéter la manche** — si une manche a été jugée mauvaise (faux départ, incident), tu la relances avec les mêmes participants et voies.
- **Terminer la course** — clôt la course (le « drapeau ») : le classement se fige et le résumé est généré pour les résultats et pour les mobiles (PitWall Lap).

> Avertissement **« Sans signal du DS-300 »** : tant qu'il est présent, les tours **ne sont pas enregistrés**. Vérifie la connexion avant de donner le GO.

## 10. Contrôle des relais de pilote (championnats)

Dans les courses de **championnat par équipes**, tu peux imposer des règles de partage du volant entre les pilotes d'une équipe. Elles se définissent à la création de la course :
- **Temps minimum / maximum par pilote** — chaque pilote doit rouler au moins X et au plus Y.
- **Blocage après un changement** — un minimum de temps avant de pouvoir rechanger de pilote.
- **Maximum de relais par pilote**.

Les **changements de pilote** s'enregistrent en scannant le **QR du pilote** (ou en saisissant son code) à l'entrée en piste. Depuis le direct, tu ouvres **Contrôle des relais**, qui affiche le **pilote actuel par voie**, le **temps cumulé** de chacun (en signalant s'il enfreint une règle) et l'**historique des relais** ; si un changement a été mal enregistré, tu peux **corriger le temps** du relais.

## 11. Tour par tour et corrections (ajouter / retirer des tours)
![img: 30-correcciones.png]

Depuis la course (bouton de **correction des tours** dans le direct ou dans les résultats), tu accèdes au **tour par tour** de chaque manche. Il sert à corriger les lectures mal enregistrées.

- **Gauche** : les voies de la manche ; choisis l'équipe/le pilote à revoir.
- **Droite** : sa liste de tours — **TR** (n°), **TEMPS**, **HORLOGE** (moment de course) et **Δ PRÉC.** (différence avec le tour précédent).
- **Actions par tour** :
  - **Transférer** (↔) — passer le tour à **une autre voie/équipe** (si le système l'a mal attribué).
  - **Fantôme** — marquer le tour comme non valide (il ne compte pas) sans le supprimer ; on peut le **restaurer**.
  - **Supprimer** (🗑) — éliminer un tour.
  - **Ajouter un tour manuel** — s'il a manqué un passage, tu l'ajoutes à la main.

> Utilise-le avec discernement : les corrections modifient les totaux, les moyennes et le classement de cette manche.

## 12. Résultats et exports
![img: 10-results-comparativa.png]

À la fin (ou à tout moment), entre dans **Résultats** :

- **Comparatif** (grille) : par participant, chaque voie avec **Rapide / Moyenne / Consistance / Sorties / Pit-stops**. Dans les courses à **passages/répétition de voie**, chaque voie se décompose en ses **occurrences** (1/2, 2/2) pour comparer.
- **Progression / Positions / Écart au leader / Écart (grille) / Statistiques avancées** : différentes vues d'analyse (expliquées en détail dans le *Manuel de statistiques*).
- **Exports** : **Excel**, **Points (xlsx/csv)**, **Control (csv)**, **Exporter pour GitHub**, **PDF**.

**Résultats publics.** Il existe une page ouverte — **Résultats**, dans le menu d'accueil — où n'importe qui peut consulter (sans rien toucher ni pouvoir éditer) les résultats des courses **terminées**. C'est celle que tu partages avec les pilotes et le public pour qu'ils regardent le classement et les statistiques de la course.

![img: op-resultados-publicos.png]

## 13. Entraînement
![img: 40-training.png]

En plus des courses, PitWall dispose d'un mode **Entraînement** (depuis l'écran d'accueil) pour rouler sans monter une compétition complète. Il y a deux modalités :

- **Entraînement libre** : enregistre des **tours par voie sans structure d'équipes**. Idéal pour des séances ouvertes où chacun teste voiture et piste ; il n'y a ni rotation ni classement, seulement des temps par voie.
- **De compétition** : équipes ou pilotes affectés à des voies avec **rotation automatique après chaque série**, comme une course mais pensé pour s'entraîner au format championnat.

Choisis la modalité, attribue les voies et appuie sur *Commencer (« Empezar »)*. Le chronométrage en direct fonctionne comme en course (GO du boîtier, tours, meilleur/moyenne par voie).

## 14. Réglages
![img: 04-settings.png]

- **Source de données** : choisis d'où arrivent les passages — **Simulation**, **DS-300** (un boîtier par port, avec son nombre de voies), **DS-300 agrégateur** (plusieurs boîtiers sur un seul port COM : indique le **port**, le **baud** —57600, 8N1— et le **nombre de boîtiers** 2/3/4 → 16/24/32 voies) ou **BART** par Bluetooth. Avec l'agrégateur les voies sont numérotées à la suite (boîtier 1 → 1–8, boîtier 2 → 9–16…) et un seul signal de départ lance tous les boîtiers.
- **Circuits** : définis des pistes enregistrées (séquence de voies, temps minimum).
- **Suivi public par internet** : publie les vues publiques sur internet pour suivre la course depuis l'extérieur du local (voir la section suivante).
- **Licence** et langue (ES/EN).

**Historique des versions.** Dans le **pied de toutes les pages**, tu vois le numéro de **version** de PitWall. En cliquant dessus, l'**Historique des versions** (`/changelog`) s'ouvre, avec ce qui a été **Ajouté**, **Amélioré** et **Corrigé** à chaque mise à jour. La version **augmente à chaque mise à jour**, ainsi tu sais toujours quel PitWall tu as et ce qui a changé.

## 15. Suivi public par internet
![img: op-seguimiento-publico.png]

Par défaut, les vues de PitWall (le **direct**, les **Résultats** et **PitWall Lap**) ne sont visibles que sur le **réseau local**. Avec le **Suivi public par internet**, chaque club peut les **publier sur internet** pour que pilotes et public suivent la course **depuis l'extérieur du local**, sans ouvrir de ports ni monter un VPN : PitWall crée un **tunnel Cloudflare propre** au club.

C'est dans **Réglages → Suivi public par internet**. Il y a **deux modes** :

- **Rapide.** PitWall génère une **URL temporaire** (`*.trycloudflare.com`) à la volée : **sans compte ni domaine**. C'est l'option pour un après-midi ponctuel ; note que l'URL **change à chaque démarrage**.
- **Cloudflare propre.** Tu utilises le **token du tunnel** du club et **ton propre domaine**, ce qui rend l'**URL fixe** et à ton image. L'écran lui-même propose un **guide pas à pas**, avec des liens vers le panneau **Zero Trust** de Cloudflare et vers la documentation officielle, pour créer le tunnel et coller son token.

**Contrôles.** Boutons **Démarrer** / **Arrêter** avec l'**état** et l'**URL en direct** (pour la copier et la partager). **Démarrer** applique ce que tu as à l'écran à ce moment-là. Tu peux activer le **démarrage automatique** pour que le tunnel se lance seul à l'ouverture de PitWall.

**Installer cloudflared.** Le tunnel est lancé par l'outil `cloudflared`. S'il n'est pas installé, le bouton **Installer cloudflared** apparaît : il **télécharge la version officielle** dans le dossier de données de PitWall — **sans demander de droits d'administrateur**.

> **Sécurité.** Depuis l'extérieur, **seules les vues publiques sont visibles** (direct, résultats et PitWall Lap). Le **contrôle de l'app** (créer, diriger ou éditer des courses) **reste bloqué** : personne de l'extérieur ne peut toucher à la course.

## 16. Glossaire (opération)
- **Course** : l'événement complet. Il se compose de séries.
- **Série** : groupe de participants avec sa rotation ; elle se compose de manches.
- **Manche** : une tirée chronométrée (toutes les voies en même temps) d'une durée donnée.
- **Rotation** : comment les participants changent de voie d'une manche à l'autre.
- **Repos** : manche dans laquelle un participant ne court pas (trou `0` dans la séquence).
- **Passage** : parcours complet de la séquence de voies ; N passages = N× manches.
- **Répéter la voie** : courir chaque voie N manches d'affilée, en cumulant les tours.
- **GO** : le signal de départ (du boîtier DS-300) qui lance la manche.
- **Tour fantôme** : tour marqué comme non valide (il ne compte pas), restaurable.
- **Pole** : séance de qualification préalable (facultative) ; tous roulent sur la même voie et leur meilleur tour fixe la grille de départ.
- **Entraînement libre** : mode pour enregistrer des tours par voie sans équipes ni rotation (séance ouverte).
- **PitWall Lap** : vue mobile par équipe/pilote (ses tours annoncés et sa position).
- **PIN** : code par équipe pour entrer sur son panneau dans PitWall Lap.
- **Pt (temps minimum)** : seuil en dessous duquel un tour est considéré comme un passage fantôme et ne compte pas.
- **Scénario** : piste enregistrée (circuits, voies, séquence et temps minimum) réutilisable dans plusieurs courses.
- **Catégorie** : classe de voiture/pilote (GT, Tourisme, Classiques…) ; permet un Pt différent par catégorie.
- **Catalogue** : bibliothèque réutilisable de pilotes, équipes et voitures (importable par CSV).
- **QR de pilote** : code qui identifie le pilote pour enregistrer son relais lors du scan.
- **Relais (shift)** : période pendant laquelle un pilote est au volant au sein de son équipe en endurance.
- **DS-300** : le boîtier de chronométrage qui détecte le passage sur la ligne d'arrivée.
- **Importer une série** : apporter une épreuve montée dans PitWall Control (par JSON ou par réseau LAN + PIN) pour que PitWall crée automatiquement la course.
- **PitWall Control** : l'app de gestion de championnats qui monte l'épreuve et reçoit les résultats de PitWall.
- **Suivi public par internet** : publier les vues publiques (direct, résultats, Lap) sur internet avec un tunnel Cloudflare propre au club.
- **Tunnel Cloudflare** : connexion qui expose sur internet les vues publiques de PitWall sans ouvrir de ports (mode Rapide avec URL temporaire, ou Cloudflare propre avec domaine fixe).
- **Historique des versions** : la page (`/changelog`) qu'ouvre le numéro de version du pied, avec ce qui a été ajouté, amélioré et corrigé à chaque mise à jour.
