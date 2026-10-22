---
lang: it
title: Manuale di PitWall Lap
descr: Manuale di PitWall Lap, l'app del pilota di slot: ascoltare i tempi sul giro, calendario gare con promemoria, allenamenti, allenamenti di gara e risultati offline.
kicker: Manuale dell'app · Per il pilota
h1: Il tuo assistente slot,<br>in <span class="ac">tasca</span>.
lede: Guida a <b>PitWall Lap</b>, l'app del pilota: si collega al cronometraggio della pista per <b>dirti a voce i tempi sul giro</b>, anche con lo schermo bloccato, e conserva nel telefono il tuo <b>calendario gare</b>, i tuoi <b>allenamenti</b> e i tuoi <b>risultati</b>.
---

## intro | Introduzione

PitWall Lap è l'app del **pilota**. Ha sei aree, che compaiono nel menu principale quando la apri:

- **Lap**: si collega al cronometraggio della pista e ti dice i tempi a voce.
- **Calendario**: le tue gare, con promemoria sul telefono.
- **Allenamenti**: le sessioni di prova che hai registrato.
- **Allenamenti di gara**: quelli salvati dal server, che puoi scaricare per consultarli offline.
- **Risultati**: gare terminate e i tuoi file (Excel, PDF o foto).
- **Impostazioni**: lingua, strategia gomme e avvisi vocali.

![shot: lap-01-menu.png | PitWall Lap · Menu principale | Menu principale di PitWall Lap | Menu principale: Lap in alto, le quattro aree a griglia e le Impostazioni sotto.]

L'app funziona con **PitWall Manager** (il server della pista), con il cronometro **TicTac** precedente (InfoLap) e con il **TicTac nuovo**. È in **8 lingue**: spagnolo, catalano, basco, inglese, italiano, francese, portoghese e olandese; quando la apri prende quella del telefono.

> tip: È un'app per **iPhone** (si installa con TestFlight) e per **Android** (APK, che si scarica da pitwall.es e si **aggiorna dall'app stessa**). Il telefono deve essere nella **stessa rete WiFi** del server o del cronometro; senza quella rete, Calendario, Allenamenti, Allenamenti di gara scaricati e Risultati continuano a funzionare, ma Lap non ha nulla da ascoltare.

## permisos | Permessi del telefono

L'app chiede i permessi solo quando servono:

- **Rete locale** (iPhone): per trovare il server o il cronometro della pista nel WiFi. Se lo neghi, iOS scarta in silenzio le ricerche e **Lap non troverà nulla** anche se tutto è a posto; si risolve in *Impostazioni di iPhone → PitWall Lap → Rete locale*.
- **Notifiche**: la prima volta che salvi una gara con promemoria. Senza, la gara si salva ma nessun promemoria suonerà.
- **Fotocamera** e **Foto**: solo se aggiungi una foto a *Risultati*.

## lap | Lap: ascoltare i tempi

![shot: lap-02-fuentes.png | PitWall Lap · Lap | Scelta tra PitWall e TicTac | Lap: due schede, PitWall (rossa) e TicTac, e il pulsante Indietro.]

Entra in **Lap** e scegli la fonte dei tempi:

- **PitWall**: il server della pista (PitWall Manager).
- **TicTac**: il cronometro TicTac Slot, senza server.

L'app **trova la fonte da sola** nella rete in pochi secondi. Se non la trova, ti lascia scrivere l'**IP a mano** una volta e lo ricorda per la prossima. Quell'indirizzo ricordato lo usano anche Allenamenti di gara e Risultati per parlare con il server.

### Scegliere l'attività (PitWall)

![shot: lap-03-actividad.png | PitWall Lap · Scegli l'attività | Elenco di gare e allenamento attivi | Scegli l'attività: gare attive e in attesa, e la sessione di allenamento se c'è.]

Se il server ha più gare, o una gara e un allenamento insieme, ti lascia **scegliere**. Se c'è una cosa sola, entra direttamente.

- **Aggiorna**: il pulsante in alto a destra (o trascinare l'elenco verso il basso) interroga di nuovo il server senza uscire dalla schermata. Usalo se il direttore ha appena preparato la gara o l'allenamento. Da «Nessuna attività» o da un errore, se dopo l'aggiornamento compare una sola attività, entra direttamente.
- Poi scegli la tua **batteria** e il tuo **nome o squadra**, e arrivi alla schermata di gara.

### La tua schermata di gara

![shot: lap-04-mi-turno.png | PitWall Lap · Il mio turno | Schermata di gara | Il mio turno: l'ultimo giro in grande, colorato secondo quanto è veloce, la tua posizione e i distacchi.]

È pensata per essere **guardata con la coda dell'occhio**: l'ultimo giro in grande, in **viola** se è il tuo migliore, in **verde** se sei entro il 2 % e in **ambra** se vai più lento, con la differenza sotto; la tua posizione e i distacchi con l'avversario davanti e quello dietro. Se il direttore mette in **pausa**, **ferma (STOP)** o termina la manche, l'app lo mostra e te lo dice a voce.

La **voce** dice ogni giro, i cambi di posizione, metà manche, l'ultimo minuto e gli ultimi 30 secondi e, se li attivi, ogni pochi minuti la media di corsia, la media di gara, i distacchi e la «media per salire». Tutto si configura in *Impostazioni* (vedi sotto) e si può cambiare al volo in *Voce e impostazioni*, ripiegato sotto la tua schermata.

La **strategia gomme** (gare di durata) consiglia quando cambiare e, se la gara usa il controllo gomme del server, mostra i set disponibili e l'ultimo cambio. Si può disattivare in *Impostazioni*.

### Allenamento libero e allenamento di gara

Se in «Scegli l'attività» compare **Allenamenti**, c'è una sessione di prova in corso:

- **Allenamento libero**: scegli la tua **corsia** e l'app segue quella corsia.
- **Allenamento di gara**: le squadre **ruotano di corsia a ogni heat**, quindi scegli la tua **squadra o pilota** (l'elenco mostra la corsia che ciascuno occupa ora, oppure **Riposa**) e l'app **ti segue ovunque vai**. All'inizio di ogni heat la voce ti dice *«Tocca a te, corsia N»*; se in quell'heat riposi, la schermata lo mostra e non senti nulla degli altri.

![shot: lap-05-competicion-selector.png | PitWall Lap · Allenamento di gara | Scegliere squadra o pilota | Allenamento di gara: scegli chi seguire; ognuno mostra la sua corsia attuale o Riposa.]

> warn: Il seguito per squadra nell'allenamento di gara richiede **PitWall Manager 1.56.1** o successivo. Con un server più vecchio l'app non offre l'allenamento di gara o resta fissa su una corsia.

Con **Allenamento GO** (nella tua schermata, in modalità allenamento) l'app registra i tuoi giri come una sessione tua; quando fermi, la salva in *Allenamenti*.

## calendario | Calendario gare

![shot: lap-06-calendario.png | PitWall Lap · Calendario | Gare future e passate | Calendario: gare future (con la campana se hanno promemoria) e passate.]

Il calendario conserva **le tue gare nel telefono** e ti **avvisa** con notifiche, senza server e senza connessione. Mostra le **prossime** (la più vicina per prima) e le **passate**. Tocca una gara per modificarla o eliminarla.

### Aggiungere una gara a mano

![shot: lap-07-evento.png | PitWall Lap · Nuova gara | Modulo della gara | Nuova gara: nome, data e ora, luogo, note e promemoria.]

Premi **＋ Aggiungi gara** e compila **nome**, **data** e **ora** (obbligatori) e, se vuoi, **luogo** e **note**. In **Avvisami** seleziona i promemoria che vuoi:

- all'ora di inizio;
- 30 minuti prima;
- 1 ora prima;
- 1 giorno prima;
- 1 settimana prima.

Per impostazione predefinita una gara nuova avvisa **1 giorno e 1 ora prima**. Si programmano solo i promemoria il cui momento non è ancora passato. La prima volta, il telefono chiederà il permesso per le notifiche.

### Aggiungere gare da pitwall.es

Il pulsante **Gare di pitwall.es** apre il calendario pubblico delle gare di slot di pitwall.es (lo stesso del motore di ricerca gare del sito), con le gare **in arrivo** raggruppate per mese. Serve una connessione a internet. Ogni gara indica se è **Verificata** o **Trovata dall’IA**; per queste ultime, controlla la data sul sito dell'organizzatore con **Sito ↗**.

- **Filtra** come sul sito: scrivi nella ricerca (nome, campionato, club, città o paese) e usa i pulsanti **Paese**, **Tipo** e **Campionato**. Tutto si combina; **Rimuovi filtri** li toglie in un colpo.
- Premi **＋** per aggiungere una sola gara, oppure selezionane diverse e premi **Aggiungi (n)**. **Seleziona tutte** seleziona solo le gare visibili con i filtri attivi.
- Vengono segnate alle **9:00** del primo giorno con avvisi **1 giorno e 1 ora prima**; poi puoi cambiarlo come per qualsiasi altra gara. Quelle già nel tuo calendario appaiono come **Aggiunta**.

### Importare molte gare da Excel

Se hai il calendario della stagione in un foglio di calcolo, non serve scrivere ogni gara.

1. Premi **Scarica il modello**. L'app crea un Excel nella tua lingua e apre il menu di condivisione: salvalo in *File*, mandatelo per email o con AirDrop.
2. Aprilo in Excel, Numbers o un altro programma e compila **una gara per riga** nel foglio *Gare*. **Elimina le due righe di esempio**. Il foglio *Istruzioni* riassume le regole.
3. Salvalo come **.xlsx** e torna all'app: **Importa da Excel** e scegli il file.
4. L'app mostra un'**anteprima** prima di salvare qualsiasi cosa: le gare che verranno importate, quelle già presenti e le righe con errori. Conferma con **Importa**.

![shot: lap-08-importar.png | PitWall Lap · Importa da Excel | Anteprima dell'importazione | Anteprima: cosa verrà importato, cosa c'era già e quali righe hanno errori.]

Le colonne del modello sono:

- **Nome** (obbligatoria): il nome della gara.
- **Data** (obbligatoria): `gg/mm/aaaa`; vale anche `aaaa-mm-gg` o una data di Excel.
- **Ora** (obbligatoria): `hh:mm`. Se la data di Excel include già l'ora, vale quella.
- **Luogo** (facoltativa): il circuito o la sede.
- **Note** (facoltativa): quello che vuoi ricordare.
- **Promemoria** (facoltativa): separati da virgole, tra `hora`, `30min`, `1h`, `1d` e `1sem`. Vuoto = `1d, 1h`.

Da sapere:

- Le **intestazioni** possono essere in una qualsiasi delle 8 lingue, in un altro ordine o con un altro nome abituale (*Gara*, *Circuito*, *Date*…), e possono esserci righe di titolo sopra.
- Una riga con errore **non impedisce** di importare le altre; l'anteprima indica la **riga** e il motivo (manca il nome, data non valida, ora non valida).
- Se una gara è già nel calendario (**stesso nome e stesso momento**), viene **saltata**, quindi puoi importare lo stesso file di nuovo senza duplicare.
- Un promemoria che l'app non capisce viene ignorato e te lo dice.
- Funziona con Excel (**.xlsx** o **.xls**). Se esporti da un altro programma, salva come Excel.

> tip: Aggiungere una gara a mano resta disponibile, e puoi unire le due strade: importare la stagione e aggiungere dopo le gare singole.

## entrenamientos | Allenamenti

![shot: lap-09-entrenamientos.png | PitWall Lap · Allenamenti | Elenco delle sessioni di allenamento | Allenamenti: le tue sessioni di prova, con giri, migliore e media.]

Qui ci sono le **sessioni di prova che hai registrato** con *Allenamento GO*. Aprine una per vedere il suo **grafico** (giri e media mobile) e annotare i dati dell'auto (modello, motore, gomma, cerchio, corona e pignone). Con **Confronta** scegli da 2 a 4 sessioni e le vedi **sovrapposte** in un solo grafico, con la loro regolarità. Tutto è salvato **nel telefono**.

## competicion | Allenamenti di gara

![shot: lap-10-competicion-lista.png | PitWall Lap · Allenamenti di gara | Elenco scaricati e del server | Allenamenti di gara: quelli scaricati («sul telefono») e quelli ancora solo sul server.]

Quando un allenamento di gara finisce, **PitWall Manager lo salva**. Quest'area ti permette di **scaricarlo nel telefono** per consultarlo quando vuoi, anche **offline**.

- L'elenco unisce quelli che hai già (**✓ sul telefono**) e quelli del server (**⬇ Scarica**). Tocca uno del server e si scarica e si apre. Con più in sospeso compare **Scarica tutti**.
- Ogni riga mostra data, heat, partecipanti, giri e giro migliore.
- La sessione **in corso adesso** non compare finché non viene chiusa.
- Con il server spento o fuori dal WiFi si vedono solo quelli scaricati. Per elencare quelli del server serve essere entrati almeno una volta in *Lap → PitWall*, perché l'app ricordi il suo indirizzo.

![shot: lap-11-competicion-detalle.png | PitWall Lap · Allenamento di gara | Classifica e heat | Dettaglio: classifica della sessione e, heat per heat, cosa ha fatto ogni corsia.]

Il **dettaglio** ha la **classifica** della sessione (vince chi somma più giri in tutti i suoi heat; a parità, il giro migliore) e, **heat per heat**, giri, migliore e media di ogni corsia con il suo partecipante. **Rimuovi dal telefono** elimina la copia locale; l'allenamento resta sul server.

> warn: Per scaricare gli allenamenti serve **PitWall Manager 1.56.0** o successivo.

## resultados | Risultati

![shot: lap-12-resultados.png | PitWall Lap · Risultati | Gare e file propri | Risultati: gare di PitWall e i tuoi file, insieme e per data.]

*Risultati* riunisce, per data, due tipi di cose:

- **Gare terminate in PitWall**: l'app salva il dossier dei risultati quando la gara finisce, quindi lo vedi offline. Se il server risponde, compaiono anche quelle che non hai seguito in diretta (segnate **☁ sul server**). In ognuna hai la classifica e l'**Excel di confronto** da aprire o condividere.
- **I tuoi file**: premi **＋ Aggiungi** e scegli **File (Excel o PDF)**, **Foto dalla libreria** o **Scatta una foto**. Serve per conservare la classifica di una gara di un altro club, un foglio tempi su carta o un PDF del regolamento.

![shot: lap-13-archivo.png | PitWall Lap · File dei risultati | Dettaglio di un file proprio | Un tuo file: si rinomina, si apre o condivide, e si elimina. Le foto si vedono sullo schermo.]

Ogni tuo file viene **copiato nell'app**, quindi resta anche se elimini l'originale. Puoi **rinominarlo**, **aprirlo o condividerlo** (Excel e PDF si aprono nell'app che scegli; le foto si vedono direttamente) ed **eliminarlo**.

## ajustes | Impostazioni

![shot: lap-14-ajustes.png | PitWall Lap · Impostazioni | Schermata delle impostazioni | Impostazioni: lingua, strategia gomme e avvisi vocali.]

Dal pulsante **Impostazioni** del menu configuri:

- **Lingua dell'app**: automatica (quella del telefono) o una delle 8. Cambia anche la **voce** che ti dice i tempi e le frasi che pronuncia. Il basco non ha una voce di sistema su iPhone e usa quella spagnola.
- **Strategia gomme**: la attivi o disattivi. Disattivata, non viene calcolata e il suo accesso sparisce da Lap.
- **Voce**: l'interruttore generale e gli **avvisi**: giri, cambi di posizione, metà manche, ultimo minuto e ultimi 30 secondi, e gli **avvisi periodici** (media di corsia, media di gara, distacchi e «media per salire»). Un periodico si ripete ogni **N minuti**: tocca il suo pulsante per passare tra spento, 1, 2, 3 e 5 minuti.
- **App** (solo Android): la versione installata e il pulsante **Cerca aggiornamenti**.

Quello che imposti qui è **con cui parte ogni sessione**. Durante la gara puoi continuare a cambiare gli avvisi da Lap, in *Voce e impostazioni*.

> tip: Con il **TicTac precedente** l'app dice solo i giri; gli altri avvisi richiedono PitWall Manager o il TicTac nuovo.

## actualizar | Aggiornare l'app

- **iPhone**: le versioni arrivano da **TestFlight**. Apri l'app TestFlight e premi *Aggiorna*; se hai attivato gli aggiornamenti automatici, si installano da sole. Ogni versione di TestFlight **scade dopo 90 giorni**, quindi conviene aggiornare prima.
- **Android**: quando apri l'app (e quando ci torni dopo 6 ore), se su **pitwall.es** c'è una versione più recente della tua, il menu mostra una scheda **«È disponibile una nuova versione»** con il pulsante **Aggiorna**. Premendolo, l'app **scarica l'APK** e apre l'installatore di Android. La prima volta, Android ti chiederà di **consentire a PitWall Lap di installare app**; concedilo e premi di nuovo *Aggiorna*. **Più tardi** nasconde l'avviso fino alla prossima apertura dell'app. Puoi anche controllare quando vuoi in *Impostazioni → App → Cerca aggiornamenti*. Il download si può **annullare** e, se passano 30 secondi senza dati, si interrompe da solo.

> tip: L'aggiornamento si installa **sopra** l'app, senza perdere calendario, allenamenti e risultati. Se non c'è rete o il sito non risponde, l'app semplicemente non avvisa. La prima versione con questo avviso va installata a mano una volta; da lì in poi si aggiorna da sola.

## problemas | Se qualcosa non funziona

- **Lap non trova il server.** Controlla che telefono e server siano nello **stesso WiFi** e, su iPhone, che il permesso **Rete locale** sia attivo. Se ancora non compare, inserisci l'IP a mano.
- **«Nessuna attività».** Il server non ha una gara preparata né un allenamento in corso. Quando il direttore la prepara, premi **Aggiorna**.
- **Non compare l'allenamento di gara.** Controlla che PitWall Manager sia **1.56.1** o successivo e che l'allenamento sia allestito (in corso o in attesa tra gli heat).
- **I promemoria del calendario non suonano.** Nelle impostazioni del telefono controlla che *PitWall Lap* abbia il permesso **Notifiche**. I promemoria il cui momento è già passato non vengono programmati.
- **L'importazione dice che non può leggere il file.** Usa un **Excel (.xlsx)**, per esempio il modello, con le colonne **Nome** e **Data**.
- **La voce non suona con lo schermo bloccato.** Controlla che il volume e l'interruttore del silenzio non siano spenti; l'app parla comunque con il telefono in silenzioso.
- **Non si aggiorna su Android.** Controlla di avere connessione a internet e di aver consentito a PitWall Lap di installare app; puoi anche scaricare l'APK a mano dalla pagina di PitWall Lap su pitwall.es.
- **Novità** (in fondo al menu) mostra la cronologia delle versioni dell'app; è solo in spagnolo.
