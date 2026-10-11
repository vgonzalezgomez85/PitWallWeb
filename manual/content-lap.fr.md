---
lang: fr
title: Manuel de PitWall Lap
descr: Manuel de PitWall Lap, l'app du pilote de slot : entendre les temps au tour, calendrier de courses avec rappels, entraînements, entraînements de compétition et résultats hors ligne.
kicker: Manuel de l'app · Pour le pilote
h1: Ton assistant slot,<br>dans ta <span class="ac">poche</span>.
lede: Guide de <b>PitWall Lap</b>, l'app du pilote : elle se connecte au chronométrage de la piste pour <b>te dire les temps au tour</b> à voix haute, même écran verrouillé, et garde sur ton téléphone ton <b>calendrier de courses</b>, tes <b>entraînements</b> et tes <b>résultats</b>.
---

## intro | Introduction

PitWall Lap est l'app du **pilote**. Elle a six zones, qui apparaissent dans le menu principal quand tu l'ouvres :

- **Lap** : se connecte au chronométrage de la piste et te dit les temps à voix haute.
- **Calendrier** : tes courses, avec des rappels sur ton téléphone.
- **Entraînements** : les séances de roulage que tu as enregistrées.
- **Entraînements de compétition** : ceux enregistrés par le serveur, que tu peux télécharger pour les consulter hors ligne.
- **Résultats** : courses terminées et tes propres fichiers (Excel, PDF ou photos).
- **Réglages** : langue, stratégie pneus et alertes vocales.

![shot: lap-01-menu.png | PitWall Lap · Menu principal | Menu principal de PitWall Lap | Menu principal : Lap en haut, les quatre zones en grille et les Réglages en dessous.]

L'app fonctionne avec **PitWall Manager** (le serveur de la piste), avec l'ancien chronomètre **TicTac** (InfoLap) et avec le **nouveau TicTac**. Elle existe en **8 langues** : espagnol, catalan, basque, anglais, italien, français, portugais et néerlandais ; à l'ouverture, elle prend celle du téléphone.

> tip: C'est une app pour **iPhone** (installée via TestFlight) et pour **Android** (APK, à télécharger sur pitwall.es et **mis à jour depuis l'app elle-même**). Le téléphone doit être sur le **même réseau WiFi** que le serveur ou le chronomètre ; sans ce réseau, Calendrier, Entraînements, Entraînements de compétition téléchargés et Résultats continuent de fonctionner, mais Lap n'a personne à écouter.

## permisos | Autorisations du téléphone

L'app ne demande des autorisations que quand elle en a besoin :

- **Réseau local** (iPhone) : pour trouver le serveur ou le chronomètre de la piste sur le WiFi. Si tu refuses, iOS écarte les recherches en silence et **Lap ne trouvera rien** même si tout va bien ; cela se corrige dans *Réglages de l'iPhone → PitWall Lap → Réseau local*.
- **Notifications** : la première fois que tu enregistres une course avec des rappels. Sans elles, la course est enregistrée mais aucun rappel ne sonnera.
- **Appareil photo** et **Photos** : seulement si tu ajoutes une photo à *Résultats*.

## lap | Lap : entendre les temps

![shot: lap-02-fuentes.png | PitWall Lap · Lap | Choisir entre PitWall et TicTac | Lap : deux cartes, PitWall (rouge) et TicTac, et le bouton Retour.]

Entre dans **Lap** et choisis la source des temps :

- **PitWall** : le serveur de la piste (PitWall Manager).
- **TicTac** : le chronomètre TicTac Slot, sans serveur derrière.

L'app **trouve la source toute seule** sur le réseau en quelques secondes. Si elle ne la trouve pas, elle te laisse saisir l'**IP à la main** une fois et s'en souvient pour la prochaine fois. Entraînements de compétition et Résultats utilisent aussi cette adresse mémorisée pour parler au serveur.

### Choisir l'activité (PitWall)

![shot: lap-03-actividad.png | PitWall Lap · Choisir l'activité | Liste des courses et entraînements actifs | Choisir l'activité : courses actives et en attente, et la séance d'entraînement s'il y en a une.]

Si le serveur a plusieurs courses, ou une course et un entraînement en même temps, il te laisse **choisir**. S'il n'y a qu'une seule chose, il entre directement dedans.

- **Actualiser** : le bouton en haut à droite (ou tirer la liste vers le bas) interroge de nouveau le serveur sans quitter l'écran. Utilise-le si le directeur vient de préparer la course ou l'entraînement. Depuis « Aucune activité » ou une erreur, si une seule activité apparaît après l'actualisation, il entre directement dedans.
- Ensuite tu choisis ta **série** et ton **nom ou équipe**, et tu arrives sur ton écran de course.

### Ton écran de course

![shot: lap-04-mi-turno.png | PitWall Lap · Mon tour | Écran de course | Mon tour : le dernier tour en grand, coloré selon sa rapidité, ta position et les écarts.]

Il est pensé pour être **regardé du coin de l'œil** : le dernier tour en grand, en **violet** si c'est ton meilleur, en **vert** si tu es à moins de 2 % et en **ambre** si tu es plus lent, avec la différence dessous ; ta position et les écarts avec le rival devant et celui derrière. Si le directeur met en **pause**, **arrête (STOP)** ou termine la manche, l'app l'affiche et te le dit à voix haute.

La **voix** dit chaque tour, les changements de position, la mi-manche, la dernière minute et les 30 dernières secondes et, si tu les actives, toutes les quelques minutes la moyenne de voie, la moyenne de course, les écarts et la « moyenne pour monter ». Tout se règle dans *Réglages* (voir plus bas) et peut se changer à la volée dans *Voix et réglages*, replié sous ton écran.

La **stratégie pneus** (courses d'endurance) recommande quand changer et, si la course utilise le contrôle des pneus du serveur, affiche les jeux disponibles et le dernier changement. On peut la désactiver dans *Réglages*.

### Entraînement libre et entraînement de compétition

Si **Entraînements** apparaît dans « Choisir l'activité », une séance de roulage est en cours :

- **Entraînement libre** : tu choisis ta **voie** et l'app suit cette voie.
- **Entraînement de compétition** : les équipes **changent de voie à chaque heat**, donc tu choisis ton **équipe ou pilote** (la liste montre la voie que chacun occupe en ce moment, ou **Au repos**) et l'app **te suit où que tu ailles**. Au début de chaque heat, la voix te dit *« À toi, voie N »* ; si tu te reposes ce heat, l'écran l'affiche et tu n'entends rien des autres.

![shot: lap-05-competicion-selector.png | PitWall Lap · Entraînement de compétition | Choisir équipe ou pilote | Entraînement de compétition : tu choisis qui suivre ; chacun affiche sa voie actuelle ou Au repos.]

> warn: Le suivi par équipe en entraînement de compétition demande **PitWall Manager 1.56.1** ou ultérieur. Avec un serveur plus ancien, l'app ne propose pas l'entraînement de compétition ou reste figée sur une voie.

Avec **Entraînement GO** (sur ton écran, en mode entraînement) l'app enregistre tes tours comme une séance à toi ; quand tu arrêtes, elle la sauvegarde dans *Entraînements*.

## calendario | Calendrier de courses

![shot: lap-06-calendario.png | PitWall Lap · Calendrier | Courses à venir et passées | Calendrier : courses à venir (avec une cloche si elles ont des rappels) et passées.]

Le calendrier garde **tes courses sur ton téléphone** et **te prévient** par notifications, sans serveur ni connexion. Il montre les **prochaines** (la plus proche d'abord) et les **passées**. Touche une course pour la modifier ou la supprimer.

### Ajouter une course à la main

![shot: lap-07-evento.png | PitWall Lap · Nouvelle course | Formulaire de course | Nouvelle course : nom, date et heure, lieu, notes et rappels.]

Appuie sur **＋ Ajouter une course** et remplis **nom**, **date** et **heure** (obligatoires), et en option **lieu** et **notes**. Sous **Me prévenir**, coche les rappels que tu veux :

- à l'heure de début ;
- 30 minutes avant ;
- 1 heure avant ;
- 1 jour avant ;
- 1 semaine avant.

Par défaut, une nouvelle course prévient **1 jour et 1 heure avant**. Seuls les rappels dont le moment n'est pas encore passé sont programmés. La première fois, le téléphone te demandera l'autorisation des notifications.

### Importer plusieurs courses depuis Excel

Si tu as le calendrier de la saison dans un tableur, inutile de saisir chaque course.

1. Appuie sur **Télécharger le modèle**. L'app crée un Excel dans ta langue et ouvre le menu de partage : enregistre-le dans *Fichiers*, envoie-le-toi par e-mail ou par AirDrop.
2. Ouvre-le dans Excel, Numbers ou un autre programme et remplis **une course par ligne** dans la feuille *Courses*. **Supprime les deux lignes d'exemple**. La feuille *Instructions* résume les règles.
3. Enregistre-le en **.xlsx** et reviens dans l'app : **Importer depuis Excel** et choisis le fichier.
4. L'app affiche un **aperçu** avant de rien enregistrer : les courses qui seront importées, celles qui y étaient déjà et les lignes en erreur. Confirme avec **Importer**.

![shot: lap-08-importar.png | PitWall Lap · Importer depuis Excel | Aperçu de l'importation | Aperçu : ce qui sera importé, ce qui y était déjà et quelles lignes ont une erreur.]

Les colonnes du modèle sont :

- **Nom** (obligatoire) : le nom de la course.
- **Date** (obligatoire) : `jj/mm/aaaa` ; `aaaa-mm-jj` ou une date Excel conviennent aussi.
- **Heure** (obligatoire) : `hh:mm`. Si la date Excel contient déjà une heure, c'est celle-ci qui compte.
- **Lieu** (facultatif) : le circuit ou le site.
- **Notes** (facultatif) : ce que tu veux retenir.
- **Rappels** (facultatif) : séparés par des virgules, parmi `hora`, `30min`, `1h`, `1d` et `1sem`. Vide = `1d, 1h`.

À savoir :

- Les **en-têtes** peuvent être dans n'importe laquelle des 8 langues, dans un autre ordre ou sous un autre nom courant (*Course*, *Circuit*, *Date*…), et il peut y avoir des lignes de titre au-dessus.
- Une ligne en erreur **n'empêche pas** d'importer les autres ; l'aperçu indique la **ligne** et le motif (nom manquant, date non valide, heure non valide).
- Si une course est déjà dans le calendrier (**même nom et même moment**), elle est **ignorée** : tu peux donc réimporter le même fichier sans créer de doublons.
- Un rappel que l'app ne comprend pas est ignoré, et elle te le dit.
- Cela fonctionne avec Excel (**.xlsx** ou **.xls**). Si tu exportes depuis un autre programme, enregistre en Excel.

> tip: Ajouter une course à la main reste disponible, et tu peux combiner les deux : importer la saison et ajouter ensuite les courses isolées.

## entrenamientos | Entraînements

![shot: lap-09-entrenamientos.png | PitWall Lap · Entraînements | Liste des séances d'entraînement | Entraînements : tes séances de roulage, avec tours, meilleur et moyenne.]

Ici se trouvent les **séances de roulage que tu as enregistrées** avec *Entraînement GO*. Ouvre-en une pour voir son **graphique** (tours et moyenne mobile) et noter les données de la voiture (modèle, moteur, pneu, jante, couronne et pignon). Avec **Comparer** tu choisis de 2 à 4 séances et tu les vois **superposées** sur un seul graphique, avec leur régularité. Tout est enregistré **sur ton téléphone**.

## competicion | Entraînements de compétition

![shot: lap-10-competicion-lista.png | PitWall Lap · Entraînements de compétition | Liste des téléchargés et du serveur | Entraînements de compétition : les téléchargés (« sur le téléphone ») et ceux qui ne sont encore que sur le serveur.]

Quand un entraînement de compétition se termine, **PitWall Manager l'enregistre**. Cette zone te permet de **le télécharger sur ton téléphone** pour le consulter quand tu veux, aussi **hors ligne**.

- La liste réunit ceux que tu as déjà (**✓ sur le téléphone**) et ceux du serveur (**⬇ Télécharger**). Touche-en un du serveur et il se télécharge et s'ouvre. Avec plusieurs en attente, **Tout télécharger** apparaît.
- Chaque ligne montre la date, les heats, les participants, les tours et le meilleur tour.
- La séance **en cours en ce moment** n'apparaît pas tant qu'elle n'est pas fermée.
- Avec le serveur éteint ou hors du WiFi, on ne voit que ceux téléchargés. Pour lister ceux du serveur, il faut être entré au moins une fois dans *Lap → PitWall*, pour que l'app mémorise son adresse.

![shot: lap-11-competicion-detalle.png | PitWall Lap · Entraînement de compétition | Classement et heats | Détail : classement de la séance et, heat par heat, ce qu'a fait chaque voie.]

Le **détail** contient le **classement** de la séance (gagne celui qui cumule le plus de tours sur tous ses heats ; à égalité, le meilleur tour) et, **heat par heat**, les tours, le meilleur et la moyenne de chaque voie avec son participant. **Retirer du téléphone** supprime la copie locale ; l'entraînement reste sur le serveur.

> warn: Pour télécharger des entraînements, il faut **PitWall Manager 1.56.0** ou ultérieur.

## resultados | Résultats

![shot: lap-12-resultados.png | PitWall Lap · Résultats | Courses et fichiers personnels | Résultats : courses PitWall et tes propres fichiers, ensemble et par date.]

*Résultats* réunit, par date, deux sortes de choses :

- **Courses terminées dans PitWall** : l'app enregistre le dossier de résultats à la fin de la course, donc tu le vois hors ligne. Si le serveur répond, apparaissent aussi celles que tu n'as pas suivies en direct (marquées **☁ sur le serveur**). Dans chacune tu as le classement et l'**Excel comparatif** à ouvrir ou partager.
- **Tes fichiers** : appuie sur **＋ Ajouter** et choisis **Fichier (Excel ou PDF)**, **Photo de la photothèque** ou **Prendre une photo**. Utile pour garder le classement d'une course d'un autre club, une feuille de temps papier ou un PDF du règlement.

![shot: lap-13-archivo.png | PitWall Lap · Fichier de résultats | Détail d'un fichier personnel | Un de tes fichiers : on le renomme, on l'ouvre ou le partage, et on le supprime. Les photos s'affichent à l'écran.]

Chacun de tes fichiers est **copié dans l'app**, donc il reste même si tu supprimes l'original. Tu peux le **renommer**, l'**ouvrir ou le partager** (Excel et PDF s'ouvrent dans l'app que tu choisis ; les photos s'affichent directement) et le **supprimer**.

## ajustes | Réglages

![shot: lap-14-ajustes.png | PitWall Lap · Réglages | Écran des réglages | Réglages : langue, stratégie pneus et alertes vocales.]

Depuis le bouton **Réglages** du menu, tu configures :

- **Langue de l'app** : automatique (celle du téléphone) ou l'une des 8. Elle change aussi la **voix** qui te dit les temps et les phrases qu'elle prononce. Le basque n'a pas de voix système sur iPhone et utilise celle de l'espagnol.
- **Stratégie pneus** : tu l'actives ou la désactives. Désactivée, elle n'est pas calculée et son accès disparaît de Lap.
- **Voix** : l'interrupteur général et les **alertes** : tours, changements de position, mi-manche, dernière minute et 30 dernières secondes, et les **alertes périodiques** (moyenne de voie, moyenne de course, écarts et « moyenne pour monter »). Une alerte périodique se répète toutes les **N minutes** : touche son bouton pour passer par désactivé, 1, 2, 3 et 5 minutes.

Ce que tu règles ici est **ce avec quoi démarre chaque séance**. Pendant la course tu peux continuer à changer les alertes depuis Lap, dans *Voix et réglages*.

> tip: Avec l'**ancien TicTac**, l'app ne dit que les tours ; les autres alertes demandent PitWall Manager ou le nouveau TicTac.

## actualizar | Mettre à jour l'app

- **iPhone** : les versions arrivent par **TestFlight**. Ouvre l'app TestFlight et appuie sur *Mettre à jour* ; si tu as activé les mises à jour automatiques, elles s'installent seules. Chaque version TestFlight **expire au bout de 90 jours**, il vaut donc mieux mettre à jour avant.
- **Android** : à l'ouverture de l'app, si **pitwall.es** a une version plus récente que la tienne, le menu affiche une carte **« Une nouvelle version est disponible »** avec un bouton **Mettre à jour**. En l'appuyant, l'app **télécharge l'APK** et ouvre l'installateur d'Android. La première fois, Android te demandera d'**autoriser PitWall Lap à installer des applications** ; accorde-le et appuie de nouveau sur *Mettre à jour*. **Plus tard** masque l'avis jusqu'à la prochaine ouverture de l'app.

> tip: La mise à jour s'installe **par-dessus** l'app, sans perdre ton calendrier, tes entraînements ni tes résultats. S'il n'y a pas de réseau ou que le site ne répond pas, l'app ne prévient simplement pas. La première version avec cet avis doit être installée à la main une fois ; ensuite elle se met à jour toute seule.

## problemas | Si quelque chose ne fonctionne pas

- **Lap ne trouve pas le serveur.** Vérifie que le téléphone et le serveur sont sur le **même WiFi** et, sur iPhone, que l'autorisation **Réseau local** est activée. Si rien n'apparaît encore, saisis l'IP à la main.
- **« Aucune activité ».** Le serveur n'a ni course préparée ni entraînement en cours. Quand le directeur la prépare, appuie sur **Actualiser**.
- **L'entraînement de compétition n'apparaît pas.** Vérifie que PitWall Manager est en **1.56.1** ou ultérieur et que l'entraînement est monté (en cours ou en attente entre les heats).
- **Les rappels du calendrier ne sonnent pas.** Dans les réglages du téléphone, vérifie que *PitWall Lap* a l'autorisation **Notifications**. Les rappels dont le moment est déjà passé ne sont pas programmés.
- **L'importation dit qu'elle ne peut pas lire le fichier.** Utilise un **Excel (.xlsx)**, par exemple le modèle, avec les colonnes **Nom** et **Date**.
- **La voix ne sonne pas écran verrouillé.** Vérifie que le volume et l'interrupteur de sourdine ne sont pas coupés ; l'app parle quand même avec le téléphone en silencieux.
- **Pas de mise à jour sur Android.** Vérifie que tu as une connexion internet et que tu as autorisé PitWall Lap à installer des applications ; tu peux aussi télécharger l'APK à la main depuis la page de PitWall Lap sur pitwall.es.
- **Nouveautés** (en bas du menu) affiche l'historique des versions de l'app ; il n'est qu'en espagnol.
