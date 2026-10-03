# Manuel d'utilisation — PitWall (organisation / direction de course)

Guide destiné à celui qui **opère** PitWall : monter la course, la diriger en direct, corriger des tours et sortir les résultats.

---

## 1. Introduction
![img: 01-home.png]

**PitWall** est le système de chronométrage et de gestion de courses de slot. Il détecte le passage de chaque voiture sur la ligne d'arrivée grâce au matériel de chronométrage, avec deux options compatibles :

- **DS-300** — par **port série**. Tu peux relier **jusqu'à 6 circuits** DS-300 dans une seule course : chaque boîtier chronomètre ses voies et PitWall les combine. Chaque boîtier utilise **son propre port** (un boîtier = un port).
- **DS-300 agrégateur** — lorsqu'un **appareil agrégateur** regroupe **plusieurs boîtiers DS-300 (de 2 à 4) sur un seul port COM**. PitWall sépare les boîtiers par leur identifiant de trame et numérote les voies à la suite (boîtier 1 → 1–8, boîtier 2 → 9–16, et ainsi de suite jusqu'à **32 voies** avec 4 boîtiers). Un **seul signal de départ** lance tous les boîtiers en même temps.
- **BART (Policar)** — par **Bluetooth**. Il admet **jusqu'au nombre maximal de voies que permet BART** (actuellement **32**). Au-delà de 8 voies il faut **plusieurs Master BART indépendants** (p. ex. `BART_TRACK1`, `BART_TRACK2`…), un par bloc de voies : PitWall se connecte à chacun séparément et numérote les voies à la suite, comme avec l'agrégateur DS-300.

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
- **Équipes** — nom, couleur, pays (avec son drapeau ; en plus des drapeaux de pays standards, il y a des drapeaux dessinés à la main pour la Catalogne et le Pays basque), catégorie (colorée comme dans le direct), voiture et membres.
- **Voitures** — marque, modèle et catégorie.

Tous peuvent être **importés en bloc depuis un CSV** (boutons *Modèle CSV (« Plantilla CSV »)* et *Importer CSV (« Importar CSV »)*, avec un aperçu des nouveautés vs. doublons) et exportés.

![img: op-catalogo-pilotos.png]

![img: op-qr-pilotos.png]

![img: op-catalogo-equipos.png]

> Avec *Exporter QR (« Exportar QR »)*, tu imprimes les cartes QR de tous les pilotes (pour le changement de pilote par scan en endurance — voir *Contrôle des relais*). Le catalogue d'équipes a son propre *Exporter QR*, qui distribue ces mêmes cartes **regroupées par équipe** (nom et catégorie en en-tête), en marquant « sans pilotes » les équipes vides et « ⚠ sans profil » les membres pas encore liés à un pilote du club.

![img: op-qr-equipos.png]

> **Synchroniser le catalogue avec les courses en attente.** Si tu changes les **pilotes** ou le **pays** d'une équipe dans le catalogue *après* avoir créé une course, ces changements n'arrivent pas tout seuls dans la course déjà montée. Avec **Système → Synchroniser le catalogue** (« Sistema → Sincronizar catálogo », écran d'accueil) —ou le raccourci **« Actualizar desde catálogo »** (Mettre à jour depuis le catalogue) du menu **⋯** de la fiche de course, qui n'apparaît que si la course est candidate— tu les déverses dans toutes les courses qui **n'ont encore lancé aucune manche**, sans passer par « Éditer la série ». PitWall apparie les équipes **par leur nom**, rend l'effectif de chaque course **identique au catalogue** (ajoute et retire des pilotes jusqu'à concordance — un « miroir exact ») et met à jour le pays ; avant d'appliquer, il te montre un **résumé des changements**, avec une case par course. Il ne touche pas à la grille et n'ajoute ni ne supprime d'équipes, et n'agit que sur les courses **au format équipes**. La **catégorie** n'est pas synchronisée : elle est toujours lue en direct depuis le catalogue.

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

> **Connexion écosystème.** Tout le pont réseau avec PitWall Control —envoi des séries et récupération des résultats— peut être **autorisé ou bloqué** d'un coup depuis **Système → Connexion écosystème**, sur l'écran d'accueil. Il est **activé** par défaut ; si tu le désactives, tout PitWall Control du réseau est rejeté (même avec le bon PIN) jusqu'à ce que tu le réactives. Le PIN d'appairage y est aussi consultable.

## 5. Séries, participants et rotation
![img: 34-tanda.png]

Une **série** regroupe les participants et leur **rotation de voies** par manche. Lorsque tu ajoutes les **équipes/pilotes**, PitWall génère automatiquement toutes les **manches**.

**Comment fonctionne la rotation.** Chaque participant change de voie de manche en manche en suivant la séquence configurée (par ex. `1, 3, 5, 6, 4, 2`). Ainsi, tout le monde passe par toutes les voies et les conditions s'égalisent.

- *Exemple (6 voies, 6 pilotes) :* dans la manche 1, le pilote A court sur la voie 1 ; dans la manche 2, la 3 ; dans la 3, la 5… jusqu'à avoir fait le tour de toutes les voies.

**Rotation à ta guise.** PitWall propose automatiquement une rotation équilibrée, mais **tu peux la gérer comme tu veux** : réordonne la **séquence de voies** à la main (en faisant glisser) pour décider exactement par quelle voie passe chaque participant à chaque manche.

**Repos.** S'il y a **plus de participants que de voies**, la séquence inclut des trous (`0` / `DSC`) qui sont des **repos** : dans cette manche, ce participant ne court pas. PitWall les répartit de façon équilibrée, mais **tu peux aussi les placer où tu veux** dans la rotation (fais-les glisser à la position que tu préfères).

**Voies vides (moins de participants que de voies).** Pas besoin de remplir toutes les voies : tu peux créer une manche avec **moins de participants que de voies** (**un** suffit). Les voies en trop restent libres, **sans voiture fantôme** qui apparaîtrait dans les tours ou le classement. À la création de la manche, tu choisis quoi en faire :
- **Les dernières restent vides** (par défaut) : les voies au **numéro le plus élevé** restent vides toute la course ; personne n'y roule.
- **Le trou tourne** : la voie (ou les voies) libre **tourne d'une manche à l'autre**, de sorte que tous les participants finissent par passer par les mêmes voies et la piste reste aussi équitable qu'avec une grille complète.

**Avec passages / répétition de voie :**
- *2 passages* → la séquence entière se répète : `1,3,5,6,4,2, 1,3,5,6,4,2`.
- *Répéter la voie 2* → chaque voie, deux manches d'affilée : `1,1,3,3,5,5,6,6,4,4,2,2`.

## 6. Éditer la course, les séries et les manches

Après avoir créé une course, tu peux la retoucher :
- **Éditer la course** — changer le **nom** et, **tant qu'il n'y a pas de tours enregistrés**, le **scénario**. Tu peux **attribuer** un scénario à une course qui n'en avait pas, le **changer** pour un autre ou le **retirer**. En **attribuant** un scénario, la course hérite de ses **voies**, de sa **séquence** de rotation et de son **temps minimum** (et des tours minimum par **catégorie**, s'il y en a), et PitWall **régénère les séries en attente** avec cette configuration ; en le **retirant**, la course passe en **mode manuel** en conservant sa configuration. S'il y a déjà des tours, le scénario reste **verrouillé** (pour ne pas casser les données).

![img: op-edit-carrera.png]

> Cas typique : tu **importes une série de PitWall Control** (qui arrive en mode manuel) puis tu l'**édites pour lui attribuer le scénario** de ton club, afin qu'elle hérite des voies, de la séquence et du temps minimum de ta piste.

- **Règles d'endurance (relais et pneus)** — dans une course d'**endurance**, et **tant qu'aucune manche n'a été courue**, Éditer la course te permet aussi d'ajuster les **règles de relais par pilote** (minimum et maximum par pilote, nombre maximum de relais et le blocage de fin de manche) et les **pneus par équipe** (la dotation avec laquelle démarre le contrôle des pneus) — les mêmes champs que tu as fixés dans l'assistant à la création de la course. Tu peux ainsi corriger un chiffre sans refaire toute la course. Dès que la **première manche** est courue, ces champs se **verrouillent** (atténués, avec un cadenas 🔒) pour ne pas déséquilibrer ce qui a déjà été couru ; le **nom** et le **scénario** gardent leurs règles habituelles. Si tu mets un **maximum par pilote inférieur au minimum**, PitWall te prévient.

- **Éditer la série** — changer les **noms** des participants et, si la série n'a pas encore commencé, sa composition. Si elle a déjà des manches lancées, elle passe en **mode renommer seulement** (on n'ajoute ni ne retire de participants, pour ne pas déséquilibrer la rotation).

![img: op-edit-tanda.png]

> Si tu veux seulement reporter dans une course les changements de **pilotes ou de pays** faits dans le catalogue d'équipes et que la course **n'a pas encore démarré**, pas besoin de toucher à « Éditer la série » : utilise **Système → Synchroniser le catalogue** (voir *Scénarios, catégories et catalogues*). Pour une course qui a déjà couru une manche, « Éditer la série » en **mode renommer seulement** est la seule voie.

- **Éditer la manche** — changer **qui court sur chaque voie** dans une manche précise, sans régénérer toute la série (utile si une équipe ne se présente pas ou en cas de changement de dernière minute).

## 7. Pole (qualification préalable)
![img: 44-pole-setup.png]

La **pole** est un tour qualificatif **avant** la course pour décider l'ordre de départ. Elle est facultative ; elle s'active à la création de la course (**Pole**) et se lance depuis la page de la course → *Configurer la Pole Position (« Configurar Pole Position »)*.

- **Participants** : tous les inscrits apparaissent dans une **grille numérotée** (1, 2, 3…) qui s'ajuste seule à la largeur de l'écran et se remplit par colonnes —en correspondance avec les groupes de circuit C1/C2/C3—. Cet ordre est celui dans lequel ils sortiront faire leur tour ; tu peux **glisser** n'importe quel participant à la main pour le changer, ou appuyer sur *🎲 Aléatoire (« 🎲 Aleatorio »)* pour tout mélanger.
- **Voie de pole** : **tous** font leur tour qualificatif sur la **même voie** (pour que ce soit comparable). Choisis-la avec **−/+** ou avec *🎲 Aléatoire (« 🎲 Aleatorio »)*.
- **Changement automatique de pilote** : interrupteur à côté d'*Ignorer le 1er passage (« Omitir 1er cruce »)*. Case activée, à la fin de la tentative d'un pilote le bouton *Pilote suivant (« Siguiente piloto »)* fait un compte à rebours de 3 secondes et passe seul au suivant, sans attendre le clic manuel. C'est une préférence du poste de contrôle (elle est enregistrée dans le navigateur lui-même), pas de la course.
- Appuie sur *Commencer la Pole (« Empezar Pole »)* : chaque participant entre à tour de rôle, fait son tour et PitWall enregistre son meilleur temps. Dans le chronométrage, tu peux activer *Ignorer le 1er passage (out-lap) (« Omitir 1er cruce »)* pour ne pas compter le tour de lancement.
- *Absent (« No se presenta »)* : si le participant dont c'est le tour ne se présente pas en piste, le bouton *Absent* le passe. La première fois, il l'envoie à la **fin de la file** —il aura une autre chance quand son tour reviendra—; s'il est de nouveau sauté sans avoir couru entre-temps, il est marqué **absent** pour de bon. Les absents ne concourent pas pour la pole avec un 0,00 synthétique comme si c'était le tour le plus rapide : ils apparaissent à part, dans leur propre bloc, aussi bien dans le classement en direct que dans les résultats finaux.

**Résultats de la pole.** À la fin apparaît *Résultats Pole (« Resultados Pole »)* avec le **classement final** (du plus rapide au plus lent, avec l'écart au leader et le **meilleur tour**). D'ici, tu peux *✏️ Éditer les temps (« ✏️ Editar tiempos »)* s'il y a eu une erreur, ou continuer avec *🚦 Attribuer les voies de départ (« 🚦 Asignar carriles de salida »)*.

![img: 46-pole-results.png]

**Attribuer les voies après la pole.** La pole ne répartit pas les voies automatiquement : elle ouvre l'écran *Choix de voie (« Elección de carril »)*, où chaque participant **choisit** sa voie **dans l'ordre du classement** — le **poleman** (le plus rapide) choisit en premier, puis le 2e, et ainsi de suite. C'est le classique « le plus rapide choisit sa voie ».

![img: 47-pole-lanes.png]

- La bannière *Choix en cours (« Eligiendo ahora »)* indique à qui c'est le tour ; à gauche tu vois l'**ordre de choix** (le classement) et à droite les **voies disponibles** (avec leur couleur).
- Chacun appuie sur la voie qu'il veut ; cette voie disparaît des disponibles et le tour passe au suivant.
- **S'il y a plus de participants que de voies**, des trous de *💤 Repos (« 💤 Descanso »)* apparaissent : celui qui choisit le repos **ne court pas la manche 1** et **entre dans la rotation à partir de la manche 2**.
- Quand tout le monde a choisi, appuie sur *🏁 Créer la Première Série (« 🏁 Crear Primera Tanda »)* : PitWall crée la série et génère toutes les manches avec cette grille comme point de départ (l'ordre de choix définit la position initiale dans la rotation des voies). À partir de là, la course fait tourner les voies de manche en manche comme d'habitude (voir *Séries et rotation*).

> La pole ne rapporte pas de points dans la course : elle décide seulement **qui choisit sa voie en premier** et, par là, la grille de départ de la première manche.

**Les invités peuvent suivre la pole en direct.** Le tableau de chronométrage de la pole —auparavant visible uniquement pour celui qui l'opérait— est accessible sans restriction d'IP depuis **Live-stats**, et une nouvelle carte apparaît sur la page d'accueil invité tant qu'une pole est en cours. Elle est en **lecture seule** : les contrôles (démarrer/arrêter/pilote suivant) sont masqués, et on voit en temps réel qui est en piste, l'ordre de départ et le classement provisoire.

## 8. PitWall Lap — pour les équipes
![img: 43-lap-pins.png]

Les équipes peuvent suivre leur course depuis le mobile de **deux façons**, non exclusives : la **vue web avec PIN** (rien à installer, en lecture seule) ou l'**appli native PitWall Lap** (installée sur le mobile, avec la voix et la stratégie pneus en direct).

**Elle fonctionne déjà pendant la pole elle-même, pas seulement une fois terminée.** Les équipes (avec leur PIN) sont créées à la confirmation de l'assistant de la course, au lieu d'attendre l'attribution des voies à la fin de la pole. Ainsi, chaque équipe voit sur son panneau si c'est son tour maintenant, un chronomètre en direct de sa tentative, ses tours et son meilleur temps, avec la voix qui annonce chaque tour comme en course ; à la fin de la pole, le panneau passe automatiquement à l'affichage de son résultat (position et temps).

**Vue web avec PIN.**
- Entre dans **PitWall Lap · PINs** de la course. Tu verras l'adresse que les équipes ouvrent sur le mobile (par ex. `http://<IP-du-serveur>:3000/lap/<id>`) et le tableau **ÉQUIPE → PIN**.
- Donne à chaque équipe **son PIN**. En ouvrant l'adresse et en le saisissant, ils entrent directement sur leur panneau : position projetée, écart au leader, tours, moyenne et arrêts aux stands, avec la voix incluse — en lecture seule, et uniquement pour les courses d'**endurance** (le détail complet est dans le *Manuel des statistiques*, section *PitWall Lap : ta course sur le mobile*).
- *Nouveau (« Nuevo »)* régénère le PIN d'une équipe (au cas où il aurait fuité ou qu'ils veuillent le changer).
- **PIN d'accès — Activé / Désactivé** (« PIN de acceso — Activado / Desactivado »). Sur la même feuille de PIN, un interrupteur permet de **retirer le PIN** de cette course. Avec le PIN **désactivé**, chaque équipe entre sur son panneau de chrono **rien qu'en se choisissant dans la liste**, sans rien taper (pratique pour les événements internes où le PIN gêne). Les PIN sont **conservés** au cas où tu le réactives. C'est un réglage **par course**, et il voyage aussi vers le chronomètre esclave BART lors de la synchronisation de la course (Race Link).
- **Suivi des rivaux.** Dans son panneau, chaque équipe peut suivre **jusqu'à 5 rivaux** et comparer voie par voie les tours, le meilleur tour et les moyennes (manches terminées uniquement). La liste est enregistrée par équipe : tous les mobiles du stand la partagent. Détails dans le *Manuel des statistiques*, section *PitWall Lap*.

> Les mobiles doivent être sur le **même réseau** que l'ordinateur qui fait office de serveur. Utilise l'IP de la machine, pas `localhost`, quand ils l'ouvrent depuis le téléphone. Si tu veux que les équipes suivent la course **depuis l'extérieur du local** (par internet), voir *Suivi public par internet*.

**Appli native PitWall Lap (iOS/Android).** C'est la voie complète : le pilote installe l'appli sur son mobile et, à l'ouverture, choisit la source (**PitWall** ou le chronomètre **TicTac Slot** en solo, sans serveur derrière) et l'appli **découvre le serveur toute seule** sur le réseau local en quelques secondes — sans URL ni PIN à distribuer. Si la découverte automatique échoue, on saisit l'IP à la main une fois et l'appli s'en souvient la fois suivante. Si le serveur a plusieurs courses ou séries actives, elle laisse choisir ; ensuite le pilote choisit son **nom/équipe** dans la liste pour entrer sur son panneau.

Elle partage avec la vue web le chronométrage en direct et la voix (tours, changements de position, mi-manche, alertes de temps et, en mode avancé, moyennes/écarts/« moyenne pour remonter » toutes les N minutes), et offre en plus :

- **Stratégie pneus en direct** (courses d'endurance, avec un pilote sélectionné) : recommande quand changer — par dégradation réelle du rythme, ou de façon **planifiée** selon les tours/trains restants quand le pneu ne perd pas de rythme —, avec un conseil selon la position et une modélisation de l'usure des rivaux devant et derrière. Si la course utilise le **contrôle des pneus du serveur** (voir *Contrôle des pneus d'endurance*) et que l'équipe correspond par son nom, la dotation et les changements sont pilotés par **PitWall Manager** : l'appli les affiche en direct (trains disponibles, dernier changement) sans bouton manuel. Sans contrôle du serveur, le pilote tient le compte à la main (trains, changements obligatoires, coût d'arrêt) et confirme lui-même avec **Cambié gomas** (« j'ai changé les pneus »).
- **Pole** : son propre écran pour suivre ton tour de qualification, l'écart à la pole et le classement final, si la course en a une.
- **Historique et Entraînement** : les courses passées (même celles que tu n'as pas suivies en direct) et un mode d'entraînement libre qui enregistre tes relais de roulage (tours, meilleur, moyenne) directement sur le mobile, avec un graphique et une comparaison entre eux.

> L'appli n'utilise pas de PIN : n'importe qui sur le **même réseau local** qui découvre le serveur peut choisir n'importe quelle équipe dans la liste. Pour un accès contrôlé ou depuis l'extérieur du circuit, utilise la vue web avec PIN — l'appli a toujours besoin du réseau local, que tu publies ou non le tunnel de *Suivi public par internet*.

## 9. Diriger la course en direct
![img: 20-live-timing.png]

Depuis la page de la course :

1. **Armer la manche** (▶). Elle reste prête, en attente du **GO** du boîtier.
2. **GO** : au moment du départ donné sur le boîtier, le **feu tricolore** apparaît et le chronomètre démarre. Chaque circuit a sa propre horloge (C1/C2/C3).
3. Pendant la manche, tu vois par voie : **total de tours**, **dernier**, **moyenne**, **meilleur**, et en haut la bannière du **meilleur tour**.
4. **Pause / Reprendre / Arrêter** la manche au besoin.
5. À la fin (drapeau ou fin de temps), la manche se ferme et la **suivante** se prépare.
6. Quand toutes les manches d'une série sont terminées, la **série suivante** démarre.

**La fiche de la course reste accessible pendant qu'une manche tourne.** Ouvrir une course qui a une manche en cours ne t'emmène plus directement au direct : tu vois sa **fiche** (état, classement projeté, séries…) avec un lien **« Manga N »** (Manche N) pour sauter au direct quand tu veux. Quand tu **donnes le GO** depuis la fiche, l'écran saute bien tout seul au direct, et on ne peut toujours pas lancer une deuxième manche pendant qu'une autre tourne.

**Choisir la vue.** Avec le bouton *Vue (« Vista »)*, tu changes la mise en page selon les voies : *Lignes horizontales* (peu de voies), *Grille compacte* (beaucoup) ou *Cartes détaillées* (avec tours/sorties/pit/pneus/Δ par carte).

**Distance au leader et estimation provisoire.** Sur les écrans de classement (**Le Mans** et **statistiques en direct**), la distance au leader est donnée **avec la virgule** et son équivalent **en secondes** —*« a 2,8 v (35,5\") »*, soit à 2,8 tours, c'est-à-dire 35,5 secondes—, et non arrondie à des tours entiers. Et si une estimation porte un **astérisque orange**, c'est que cette équipe en est encore à sa **première manche** sans avoir dépassé les **60 %** : sa référence n'est pas figée et le chiffre peut encore bouger. Tout cela est expliqué en détail dans le *Manuel de statistiques*.

**Changer de série, répéter une manche et terminer.** Depuis le direct lui-même, tu as des raccourcis sans quitter l'écran :
- **Série suivante** — quand les manches d'une série se terminent, passe directement à la suivante.
- **Répéter la manche** — si une manche a été jugée mauvaise (faux départ, incident), tu la relances avec les mêmes participants et voies.
- **Terminer la course** — clôt la course (le « drapeau ») : le classement se fige et le résumé est généré pour les résultats et pour les mobiles (PitWall Lap).

> Avertissement **« Sans signal du DS-300 »** : tant qu'il est présent, les tours **ne sont pas enregistrés**. Vérifie la connexion avant de donner le GO.

## 10. Événements de course

La page **🗒️ Événements** —accessible depuis la fiche de la course et via un bouton dans l'en-tête du direct— affiche, manche par manche, tout ce qui se passe pendant la session dans un format facile à lire : **GO** (y compris quand il est donné dans plusieurs boîtiers séparément, circuit par circuit), **pause et reprise** par circuit, **fin de manche**, **annulation**, **récupération après une coupure**, **tours fantômes/ignorés** et leur **réattribution** à la bonne voie, **départs rétroactifs** et les **enregistrements de pilote** (QR, changement à chaud ou correction manuelle).

Les manches s'affichent **repliées par défaut** —seule celle en cours apparaît dépliée— et se déploient d'un clic sur leur en-tête. Une case à cocher permet de **masquer les enregistrements de pilote routiniers** précédant le GO quand seuls les autres événements intéressent.

> Manche en cours, la page **ajoute les nouveaux événements au fur et à mesure qu'ils se produisent**, sans recharger. C'est la façon de reconstituer, après une course, ce qui s'est passé et quand, sans devoir s'en souvenir de mémoire.

## 11. Contrôle des relais de pilote (championnats)

Dans les courses de **championnat par équipes**, tu peux imposer des règles de partage du volant entre les pilotes d'une équipe. Elles se définissent à la création de la course :
- **Temps minimum / maximum par pilote** — chaque pilote doit rouler au moins X et au plus Y.
- **Blocage après un changement** — un minimum de temps avant de pouvoir rechanger de pilote.
- **Maximum de relais par pilote**.

Les **changements de pilote** s'enregistrent en scannant le **QR du pilote** (ou en saisissant son code) à l'entrée en piste. Depuis le direct, tu ouvres **Contrôle des relais**, qui affiche le **pilote actuel par voie**, le **temps cumulé** de chacun (en signalant s'il enfreint une règle) et l'**historique des relais** ; si un changement a été mal enregistré, tu peux **corriger le temps** du relais.

> **La caméra du scanner sur téléphones et tablettes (HTTPS local).** Le scanner de QR utilise la caméra, et le navigateur ne l'autorise que sur **localhost** (l'ordinateur de l'opérateur) ou en **HTTPS**. Un téléphone ou une tablette qui rejoint PitWall par l'IP du réseau (192.168.x.x) verra la caméra bloquée, avec le message *« La caméra a besoin de HTTPS ou localhost »*. Pour scanner depuis ces appareils, active **Réglages → HTTPS local (caméra du scanner QR)** : PitWall ouvre un port sécurisé séparé (**3443** par défaut) sans rien changer au fonctionnement normal, et il faut **redémarrer** le serveur une fois. Ouvre ensuite le contrôle des relais via le lien **`https://IP:3443/control/shifts`** (ils sont prêts dans cette même section des Réglages).

> **L'avertissement de sécurité et comment le faire disparaître.** La première fois qu'un appareil ouvre le lien `https://`, le navigateur avertit une fois (**« connexion non privée → continuer »**) ; une fois accepté, la caméra fonctionne. Si tu veux supprimer cet avertissement, **installe la CA de PitWall** sur l'appareil : les Réglages proposent **Télécharger la CA** et la page **`/cert`** avec un guide pas à pas pour **iPhone/iPad, Android et Windows**. Installer la CA une seule fois suffit même si l'IP du réseau change : PitWall ne réémet que le certificat du serveur et l'appareil continue de lui faire confiance.

## 12. Contrôle des pneus d'endurance

Dans une course d'**endurance**, vous pouvez suivre les **trains de pneus** que chaque équipe utilise. La dotation —les trains avec lesquels **tout le monde** démarre— se fixe à la création de la course (assistant, étape 1, champ **« Pneus par équipe »**). Avec **0**, le contrôle est désactivé et tout fonctionne comme avant.

Il s'ouvre de **deux façons** :
- Depuis la course, avec le bouton **🛞 Pneus** (n'apparaît qu'en endurance et avec une dotation supérieure à 0).
- En **kiosque** sur `/control/tires` (avec sa carte sur l'écran d'accueil), qui **détecte tout seul** la course d'endurance en cours —comme le kiosque des relais—. Idéal à laisser ouvert sur une tablette près du stand.

L'écran est une **grille avec toutes les équipes**. Chaque case affiche le nom de l'équipe et deux nombres : **Disponibles** et **Utilisés**.

- **Un clic sur la case = livrer un train** : les disponibles baissent d'un, les utilisés montent d'un, et cela est **enregistré dans quelle manche et à quelle minute:seconde de course** le changement a eu lieu (horodaté avec la manche en cours et son chrono ; s'il n'y en a aucune en cours à ce moment-là, c'est enregistré sans temps).
- Le **crayon** de chaque case ouvre l'**historique** de cette équipe, où vous pouvez **supprimer** une entrée (le train revient aux Disponibles), **modifier** sa manche et son temps (mm:ss) ou **en ajouter un à la main** (manche, temps et une note).

Les compteurs **ne sont pas stockés bruts** : ils sont **dérivés** des entrées (dotation moins livraisons), donc annuler ne laisse jamais de décalage. Si une équipe dépasse son quota, ses **Disponibles** peuvent passer en **négatif et en rouge** —prévu pour quand vous donnez un train supplémentaire hors dotation.

Dans l'en-tête, à côté de la dotation, le bouton **🗒️ Historique des changements** ouvre —dans un **nouvel onglet**— une **page** avec le **journal global de toute la course** (et non celui d'une seule équipe). Il est présenté comme un **tableau en colonnes** (jusqu'à **trois colonnes**) qui exploite la largeur de l'écran pour tout voir presque **sans défilement**. Les changements sont **groupés par manche** : **toutes les manches** sont listées, et celles sans aucun changement sont tout de même marquées **« — aucun changement de pneus — »**. Dans chaque manche, chaque livraison indique l'**équipe** (avec son point de couleur et son nom), **quel numéro de train** c'était pour cette équipe (**train N de la dotation**, compté par ordre chronologique —1, 2, 3…—, en **rouge** s'il a dépassé le quota) et la **minute:seconde de course**. Les changements sans manche assignée vont dans un groupe **« Sans manche »** à la fin. C'est en **lecture seule** —pour supprimer, modifier ou ajouter à la main, on utilise toujours le crayon de chaque équipe— et il se **rafraîchit en direct** pendant qu'on livre des pneus.

**Dans la vue en direct**, chaque carte d'équipe affiche un indicateur **🛞 avec le nombre de trains de pneus utilisés**, à côté des avertissements de **sorties (⚠️)** et de **pit-stops (🔧)**. Il se **met à jour instantanément** —sans recharger— dès que tu enregistres un changement dans le contrôle des pneus, et il **clignote** quand le nombre augmente. Il n'apparaît que dans les courses d'**endurance avec contrôle des pneus**, et il fonctionne que la manche soit **en cours ou en attente**.

> Tout se synchronise à l'instant entre les écrans ouverts, et l'indicateur **manche:temps** bat au rythme de la course.

## 13. Vérifications techniques de PitWall Control

Si le club fait passer la **vérification technique** des voitures avec **PitWall Control**, ce résultat peut aussi arriver jusqu'à PitWall — par le même pont réseau que les séries, avec le même PIN et le même interrupteur **Connexion écosystème** (voir *Importer une série de PitWall Control*).

Manche par manche, Control envoie l'**instantané** de ce qui a été vérifié par équipe : **poids** (initial, final et minimum de la voiture), **moteur** (type, tours/min, ums), **pignon/couronne** (marque, dents, diamètre, matériau), **jantes** avant et arrière, **tresse**, **suspension**, **châssis-base**, **châssis**, **pneu**, si c'est **validé** ou non, et **observations** —avec photos, s'il y en a.

**Comment ça s'affiche dans PitWall.** Dès que le premier envoi arrive, la page de la course affiche le bouton **🔍 Vérifications**, qui ouvre un écran avec toutes les vérifications **regroupées par manche**.

> **Consultation uniquement.** Dans PitWall on n'édite ni ne crée aucune vérification : tout se fait depuis PitWall Control. Chaque nouvel envoi **remplace entièrement** les vérifications de cette course (les envois ne s'additionnent pas).

> **Vers quelle course elles vont.** Si Control indique explicitement la course, PitWall y associe les vérifications. Sinon, il cherche une course existante avec le **nom exact** de l'épreuve ; si aucune correspondance n'est trouvée non plus, il **crée automatiquement** une course minimale pour que les vérifications aient où vivre — le même comportement que pour l'import d'une série.

## 14. Tour par tour et corrections (ajouter / retirer des tours)
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

> **Tours fantômes automatiques.** Un tour en dessous du **Pt** (temps minimum) est marqué comme **fantôme** et la voie qui l'a produit ne le compte **jamais**. PitWall ne le réattribue plus au jugé : il le **retient** et ne l'attribue qu'à la voie qui **confirme** avoir manqué un passage (quand cette voie passe avec un tour d'environ le double de sa moyenne). Si personne ne le confirme, il reste ici en **fantôme** pour que tu le révises à la main. Avec **plusieurs circuits** (agrégateur DS-300 ou plusieurs Master BART), l'attribution automatique **ne passe jamais d'un circuit à l'autre** : un fantôme ne peut être certifié que sur une voie de son propre circuit, jamais sur celle d'un autre (ce sont des pistes physiquement distinctes).

## 15. Résultats et exports
![img: 10-results-comparativa.png]

À la fin (ou à tout moment), entre dans **Résultats** :

- **Comparatif** (grille) : par participant, chaque voie avec **Rapide / Moyenne / Consistance / Sorties / Pit-stops**. Dans les courses à **passages/répétition de voie**, chaque voie se décompose en ses **occurrences** (1/2, 2/2) pour comparer.
- **Progression / Positions / Écart au leader / Écart (grille) / Statistiques avancées** : différentes vues d'analyse (expliquées en détail dans le *Manuel de statistiques*).
- **Exports** : **Excel**, **Points (xlsx/csv)**, **Control (csv)**, **Exporter pour GitHub**, **PDF**.
- **L'export Excel** (résultats, points et rapport de relais) **ne fonctionne que course arrêtée ou terminée** : impossible de sortir l'Excel pendant qu'une manche tourne (ce calcul lourd bloquerait le chronométrage, au risque de perdre un passage). Si une manche démarre pendant la génération, l'export est annulé et il suffit de le relancer ensuite.

**Résultats publics.** Il existe une page ouverte — **Résultats**, dans le menu d'accueil — où n'importe qui peut consulter (sans rien toucher ni pouvoir éditer) les résultats des courses **terminées**. C'est celle que tu partages avec les pilotes et le public pour qu'ils regardent le classement et les statistiques de la course.

![img: op-resultados-publicos.png]

## 16. Entraînement
![img: 40-training.png]

En plus des courses, PitWall dispose d'un mode **Entraînement** (depuis l'écran d'accueil) pour rouler sans monter une compétition complète. Il y a deux modalités :

- **Entraînement libre** : enregistre des **tours par voie sans structure d'équipes**. Idéal pour des séances ouvertes où chacun teste voiture et piste ; il n'y a ni rotation ni classement, seulement des temps par voie.
- **De compétition** : équipes ou pilotes affectés à des voies avec **rotation automatique après chaque série**, comme une course mais pensé pour s'entraîner au format championnat.

Choisis la modalité, attribue les voies et appuie sur *Commencer (« Empezar »)*. Le chronométrage en direct fonctionne comme en course (GO du boîtier, tours, meilleur/moyenne par voie).

**Les entraînements de compétition sont enregistrés.** À la **chute du drapeau de chaque série**, PitWall enregistre une ligne par voie ayant roulé, avec son **participant**, ses **tours**, son **meilleur tour** et sa **moyenne**. Les participants **au repos** et les voies **sans passages** ne laissent aucune ligne. Un **arrêt forcé n'enregistre pas** cette série : elle est écartée et refaite en entier.

Depuis l'écran de préparation de l'entraînement de compétition, le lien *Voir les entraînements enregistrés (« Ver entrenos guardados »)* ouvre la liste des séances (**date**, **nb de séries**, **participants**, **tours** et **meilleur tour**), la plus récente en haut. En appuyant sur une séance, tu vois son détail en deux blocs :

- **Classement** de la séance : gagne celui qui **cumule le plus de tours** sur toutes ses séries et, à égalité, celui qui a le **meilleur tour**. La **moyenne** est celle de **tous** ses tours, pondérée par série (une série de 40 tours pèse ce qu'elle doit face à une de 3).
- **Série par série** : le détail de chaque série, voie par voie.

Chaque séance peut être **supprimée** depuis son détail. Si tu arrêtes la séance avec **STOP** et qu'elle a enregistré au moins une série, PitWall t'amène directement à **ses** résultats.

> L'**entraînement libre** n'enregistre pas de résultats : c'est une séance ouverte de temps par voie.

## 17. Réglages
![img: 04-settings.png]

- **Source de données** : choisis d'où arrivent les passages — **Simulation**, **DS-300** (un boîtier par port, avec son nombre de voies), **DS-300 agrégateur** (plusieurs boîtiers sur un seul port COM : indique le **port**, le **baud** —57600, 8N1— et le **nombre de boîtiers** 2/3/4 → 16/24/32 voies) ou **BART** par Bluetooth (il se connecte en **BLE direct** par défaut ; le **TCP** reste dans la liste pour l'émulateur ou un pont BLE→TCP). Avec l'agrégateur les voies sont numérotées à la suite (boîtier 1 → 1–8, boîtier 2 → 9–16…) et un seul signal de départ lance tous les boîtiers. Si tu utilises **plusieurs Master BART** (un par bloc de voies), ajoute une ligne par Master avec son **nom BLE** (p. ex. `BART_TRACK1`, `BART_TRACK2`…) et son **nombre de voies** : ils sont numérotés à la suite comme les boîtiers de l'agrégateur DS-300, et chaque Master doit être appairé séparément.
- **Configuration du port, sans prise de tête** : pour chaque circuit DS-300 (et l'agrégateur) tu ne vois d'un coup d'œil que le **Port** et le **Baud rate**. Choisis le **port** dans la liste détectée ; s'il n'y figure pas, **« Saisir le chemin à la main »** permet de le taper (p. ex. `COM3` ou `/dev/ttys003`). Le **baud rate** est un menu déroulant avec les vitesses habituelles (9600–921600), avec **« Saisir à la main »** pour une valeur hors liste. Les réglages fins de la liaison série (**Data bits, Parité, Stop bits, Contrôle de flux**) sont repliés sous **« Options avancées du port »** : par défaut **8N1**, on n'y touche presque jamais.
- **Circuits** : définis des pistes enregistrées (séquence de voies, temps minimum).
- **Suivi public par internet** : publie les vues publiques sur internet pour suivre la course depuis l'extérieur du local (voir la section suivante).
- **Licence** et langue (ES/EN).

**Sauvegarde de la base de données.** Depuis l'accueil, la carte **Base de données** (`/database`) permet de **télécharger** un instantané complet de tes données (`.db`) et, s'il faut un jour récupérer une installation ou déplacer PitWall sur un autre PC, d'**importer** une copie pour la restaurer : l'import est validé (ce doit être une vraie base SQLite) et reste « en attente » — rien n'est remplacé sur le moment, ça ne s'applique qu'en **fermant PitWall complètement puis en le rouvrant**, et tes données actuelles sont sauvegardées automatiquement avant application. Tu peux annuler un import en attente à tout moment avant de redémarrer.

**Historique des versions.** Dans le **pied de toutes les pages**, tu vois le numéro de **version** de PitWall. En cliquant dessus, l'**Historique des versions** (`/changelog`) s'ouvre, avec ce qui a été **Ajouté**, **Amélioré** et **Corrigé** à chaque mise à jour. La version **augmente à chaque mise à jour**, ainsi tu sais toujours quel PitWall tu as et ce qui a changé.

## 18. Suivi public par internet
![img: op-seguimiento-publico.png]

Par défaut, les vues de PitWall (le **direct**, les **Résultats** et la **vue web de PitWall Lap**) ne sont visibles que sur le **réseau local**. Avec le **Suivi public par internet**, chaque club peut les **publier sur internet** pour que pilotes et public suivent la course **depuis l'extérieur du local**, sans ouvrir de ports ni monter un VPN : PitWall crée un **tunnel Cloudflare propre** au club.

> L'**appli native** de PitWall Lap ne passe pas par ce tunnel : elle a toujours besoin d'être sur le **même réseau local** que le serveur, que tu la publies sur internet ou non.

C'est dans **Réglages → Suivi public par internet**. Il y a **deux modes** :

- **Rapide.** PitWall génère une **URL temporaire** (`*.trycloudflare.com`) à la volée : **sans compte ni domaine**. C'est l'option pour un après-midi ponctuel ; note que l'URL **change à chaque démarrage**.
- **Cloudflare propre.** Tu utilises le **token du tunnel** du club et **ton propre domaine**, ce qui rend l'**URL fixe** et à ton image. L'écran lui-même propose un **guide pas à pas**, avec des liens vers le panneau **Zero Trust** de Cloudflare et vers la documentation officielle, pour créer le tunnel et coller son token.

**Contrôles.** Boutons **Démarrer** / **Arrêter** avec l'**état** et l'**URL en direct** (pour la copier et la partager). **Démarrer** applique ce que tu as à l'écran à ce moment-là. Tu peux activer le **démarrage automatique** pour que le tunnel se lance seul à l'ouverture de PitWall.

**Installer cloudflared.** Le tunnel est lancé par l'outil `cloudflared`. S'il n'est pas installé, le bouton **Installer cloudflared** apparaît : il **télécharge la version officielle** dans le dossier de données de PitWall — **sans demander de droits d'administrateur**.

> **Sécurité.** Depuis l'extérieur, **seules les vues publiques sont visibles** (direct, résultats et la vue web de PitWall Lap). Le **contrôle de l'app** (créer, diriger ou éditer des courses) **reste bloqué** : personne de l'extérieur ne peut toucher à la course.

## 19. Glossaire (opération)
- **Course** : l'événement complet. Il se compose de séries.
- **Série** : groupe de participants avec sa rotation ; elle se compose de manches.
- **Manche** : une tirée chronométrée (toutes les voies en même temps) d'une durée donnée.
- **Rotation** : comment les participants changent de voie d'une manche à l'autre.
- **Repos** : manche dans laquelle un participant ne court pas (trou `0` dans la séquence).
- **Passage** : parcours complet de la séquence de voies ; N passages = N× manches.
- **Répéter la voie** : courir chaque voie N manches d'affilée, en cumulant les tours.
- **GO** : le signal de départ (du boîtier DS-300) qui lance la manche.
- **Tour fantôme** : tour marqué comme non valide (il ne compte pas), restaurable.
- **Sortie (⚠️)** : tour qui dure plus que le tour le plus rapide de ce pilote sur cette voie pendant la manche + 1,5 s (comme les « tours lents » de TicTac) ; s'il dure le double de sa moyenne propre ou plus, c'est un arrêt aux stands (🔧). En direct, c'est provisoire : quand le meilleur tour s'améliore, des tours précédents peuvent devenir des sorties.
- **Pole** : séance de qualification préalable (facultative) ; tous roulent sur la même voie et leur meilleur tour fixe la grille de départ.
- **Événements** : page (🗒️) avec le journal manche par manche de tout ce qui se passe dans la course —GO, pauses, fin de manche, tours fantômes, enregistrements de pilote…—, en direct.
- **Entraînement libre** : mode pour enregistrer des tours par voie sans équipes ni rotation (séance ouverte).
- **PitWall Lap** : suivi par équipe/pilote depuis le mobile (tours annoncés, position et, sur l'appli, stratégie pneus) — en vue web avec PIN ou en appli native installée.
- **PIN** : code par équipe pour entrer sur son panneau dans la vue web de PitWall Lap (l'appli native n'en utilise pas : elle découvre le serveur toute seule sur le réseau local).
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
