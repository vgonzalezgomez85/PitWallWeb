# Manuale d'uso — PitWall (organizzazione / direzione di gara)

Guida per chi **utilizza** PitWall: allestire la gara, dirigerla in diretta, correggere i giri ed estrarre i risultati.

---

## 1. Introduzione
![img: 01-home.png]

**PitWall** è il sistema di cronometraggio e gestione delle gare di slot. Rileva il passaggio di ciascuna auto sulla linea del traguardo tramite l'hardware di cronometraggio, con due opzioni compatibili:

- **DS-300** — tramite **porta seriale**. Puoi collegare **fino a 6 circuiti** DS-300 in una sola gara: ogni box cronometra le proprie corsie e PitWall le combina. Ogni box usa **la propria porta** (un box = una porta).
- **DS-300 aggregatore** — quando un **dispositivo aggregatore** riunisce **più box DS-300 (da 2 a 4) su un'unica porta COM**. PitWall separa i box in base al loro identificatore di trama e numera le corsie di seguito (box 1 → 1–8, box 2 → 9–16, e così via fino a **32 corsie** con 4 box). Un **unico segnale di partenza** avvia tutti i box insieme.
- **BART (Policar)** — tramite **Bluetooth**. Supporta **fino al massimo di corsie consentito da BART** (attualmente **32**). Oltre le 8 corsie servono **più Master BART indipendenti** (es. `BART_TRACK1`, `BART_TRACK2`…), uno per ogni blocco di corsie: PitWall si collega a ciascuno separatamente e numera le corsie di seguito, come con l'aggregatore DS-300.

Puoi usare una qualsiasi di queste fonti; per PitWall il flusso dei passaggi è equivalente.

- La **schermata iniziale** ha in alto un'intestazione con la ricerca **«Vai a…»** («Ir a…», scorciatoia **⌘K** su Mac o **Ctrl K**): scrivi parte del nome di una sezione o di una gara; **Invio** apre il primo risultato ed **Esc** cancella la ricerca. Accanto, delle pillole mostrano lo stato della sorgente dati (simulazione, DS-300 connesso o disconnesso) e l'**indirizzo IP** del server, per collegare telefoni e schermi.
- Se c'è una **gara in corso**, sotto compare la sua fascia: **manche X di Y**, tornata, il **tempo rimanente** della manche, le **manche** (quella in corso conta già) e il **leader stimato**, lo stesso della *Classifica stimata* della diretta, aggiornato in tempo reale. Ha pulsanti per **Diretta della manche**, **Schermo TV**, **Correzione dei giri** (della manche in corso o dell'ultima terminata), **Statistiche live**, **Controllo piloti** (nei campionati), **Gomme** (se la gara ha treni di gomme), **Registro eventi** e **Gestisci gara**. Senza gara in corso, la fascia mostra la pole in corso oppure le scorciatoie **Nuova gara** / **Allenamento libero**. La schermata iniziale si aggiorna da sola quando parte una gara e quando una manche inizia, finisce o va in pausa.
- Sotto, le sezioni sono disposte a **riquadri**: **Competizione** (Gare, Allenamenti, Statistiche live, Risultati, Lap, Controllo piloti, Controllo gomme…), **Catalogo** (Piloti, Squadre, Auto, Categorie e Scenari, con quanti ne hai di ciascuno) e **Sistema** (Impostazioni, Database, Sincronizza catalogo, Connessione ecosistema, Risoluzione dei problemi…). In fondo, la tabella delle **Gare recenti** con stato, manche e azione diretta (Diretta, Risultati o Apri).
- Ogni sezione si apre nella **sua finestra**: se la clicchi di nuovo, PitWall porta in primo piano la finestra già aperta (nell'app desktop, anche se è ridotta a icona o se da lì sei tornato alla schermata iniziale). Così puoi tenere insieme la diretta, la TV e le statistiche. Le finestre aperte compaiono nella **barra in basso** della schermata iniziale, con **Porta avanti** («Traer») per metterle davanti e **✕** per chiuderle. Con l'interruttore **«Apri i link in: Finestra nuova / Questa finestra»** scegli se preferisci aprire tutto nella stessa finestra, e **Maiusc + clic** apre un link qui stesso senza toccare l'interruttore.
- In basso a destra vedi sempre lo **stato del collegamento** (verde = connesso; "Sin señal" = controlla il cavo/porta o il Bluetooth).

**L'elenco delle gare** ti mostra tutte le tue gare con il loro stato (in attesa / attiva / terminata) e il pulsante **Nuova gara (“+ Nueva carrera”)**.

![img: 02-races-list.png]

## 2. Scenari, categorie e cataloghi (la tua libreria)

Per non riconfigurare le stesse cose a ogni gara, PitWall salva **modelli riutilizzabili** che poi scegli al momento di creare una gara.

**Scenari (circuiti salvati).** Uno **scenario** è una pista fisica salvata: n° di circuiti e corsie (p.es. `8+8+8 = 24`), la sua **sequenza di corsie** (rotazione) e il **tempo minimo predefinito**. Qualsiasi gara assegnata a quello scenario eredita tutto automaticamente.

![img: op-escenarios.png]

Modificando uno scenario ne definisci il nome, la configurazione delle corsie, trascini la **sequenza di rotazione** (con **riposi DSC** se avanzano piloti), il **tempo minimo predefinito** e, facoltativamente, i **giri minimi per categoria** (un Pt diverso per GT, Turismo, Classiche… su quella stessa pista).

![img: op-escenario-form.png]

**Categorie.** Gruppi di livello/classe (GT, Turismo, Classiche…) che servono a **sovrascrivere il tempo minimo (Pt) per categoria** in ogni scenario e a classificare auto e piloti.

![img: op-categorias.png]

**Cataloghi riutilizzabili (piloti, squadre, auto).** Mantieni il tuo **database** di partecipanti e materiale per riutilizzarlo tra le gare:
- **Piloti** — nome e categoria; ogni pilota può avere il proprio **QR** di identificazione.
- **Squadre** — nome, colore, nazione (con la sua bandiera; oltre alle bandiere di nazione standard ci sono bandiere disegnate a mano per Catalogna e Paesi Baschi), categoria (colorata come nel live), auto e componenti.
- **Auto** — marca, modello e categoria.

Tutti possono essere **importati in blocco da CSV** (pulsanti **Modello CSV (“Plantilla CSV”)** e **Importa CSV (“Importar CSV”)**, con anteprima delle novità vs. duplicati) ed esportati.

I tre cataloghi hanno una **casella di ricerca** in alto: filtra mentre scrivi (per i piloti, anche per categoria) e ti dice quanti corrispondono sul totale. Il tasto **/** ti porta alla ricerca ed **Esc** la cancella; se apri una scheda per modificarla e torni indietro, il filtro resta applicato.

![img: op-catalogo-pilotos.png]

![img: op-qr-pilotos.png]

![img: op-catalogo-equipos.png]

> Con **Esporta QR (“Exportar QR”)** stampi le tessere QR di tutti i piloti (per il cambio di pilota tramite scansione nelle gare di resistenza — vedi *Controllo dei turni*). Il catalogo squadre ha un proprio **Esporta QR**, che distribuisce le stesse tessere **raggruppate per squadra** (nome e categoria come intestazione), segnando "senza piloti" le squadre vuote e "⚠ senza profilo" i componenti non ancora collegati a un pilota del club.

![img: op-qr-equipos.png]

> **Sincronizzare il catalogo con le gare in attesa.** Se cambi i **piloti** o il **paese** di una squadra nel catalogo *dopo* aver creato una gara, quei cambiamenti non arrivano da soli alla gara già montata. Con **Sistema → Sincronizzare il catalogo** (“Sistema → Sincronizar catálogo”, nella schermata iniziale) —o la scorciatoia **“Actualizar desde catálogo”** (Aggiorna dal catalogo) del menu **⋯** della scheda gara, che compare solo se la gara è candidata— li riversi in tutte le gare che **non hanno ancora avviato nessuna manche**, senza passare per «Modifica tanda». PitWall abbina le squadre **per nome**, rende l'organico di ogni gara **identico al catalogo** (aggiunge e toglie piloti finché non coincidono — uno "specchio esatto") e aggiorna il paese; prima di applicare ti mostra un **riepilogo delle modifiche**, con una casella per gara. Non tocca la griglia né aggiunge o elimina squadre, e agisce solo sulle gare **in formato squadre**. La **categoria** non si sincronizza: si legge sempre in diretta dal catalogo.

## 3. Creare una gara
![img: 03-wizard-step1.png]

Premi **Nuova gara (“+ Nueva carrera”)** e segui la procedura guidata:

- **Tipo**:
  - *Sprint* → una **gara veloce**, di **piloti o squadre**.
  - *Resistenza* → una **gara di resistenza** (a squadre), che aggiunge il **controllo di quanto ha corso ciascun pilota** della squadra (vedi *Controllo dei turni di pilota*).
- **Corsie e circuiti**: n° totale di corsie e come si ripartiscono tra i box (p.es. 8+8+6 = 3 box DS-300).
- **Tempo minimo di giro (Pt)**: al di sotto di questo tempo, un passaggio è considerato **fantasma** (rimbalzo/doppia lettura) e non conta.
- **Passate**: quante volte si percorre l'**intera sequenza di corsie**. 2 passate = la rotazione completa si corre 2 volte (il doppio delle manche).
- **Ripeti corsia**: ogni corsia si corre questo n° di **manche di seguito** (stessa corsia), sommando i giri — per confrontare ogni ripetizione.
- **Pole** (facoltativa) e **regole di pilota** (solo campionato: min/max per pilota, blocco del cambio a fine manche).

Il primo passo è organizzato in **blocchi numerati** —**Dati**, **Pista**, **Formato** e, solo in endurance, **Regole di endurance**— e una **barra fissa in basso** riassume le tue scelte accanto al pulsante **Avanti**. Prima di proseguire, PitWall controlla che la gara abbia un **nome** e un **tipo** e che ogni circuito abbia **tra 2 e 8 corsie**, e ti segnala cosa manca.

> **Passate** e **ripeti corsia** cambiano solo il modo in cui si generano le manche; i totali si sommano per partecipante.

> Gestisci il campionato con **PitWall Control**? Non devi digitare di nuovo squadre e rotazione: puoi **importare l'intera prova** da Control (vedi *Importare una tanda da PitWall Control*).

## 4. Importare una tanda da PitWall Control
![img: op-import-tanda.png]

Se organizzi il campionato con **PitWall Control** (il gestore di stagione), puoi allestire lì la prova —squadre, coppe, corsie e rotazione— e passarla a PitWall **senza ridigitare nulla**. PitWall **crea automaticamente la gara** da ciò che riceve.

Entra in **Gare → Importa tanda**. Ci sono **due modi** per portare la prova:

- **File JSON.** In Control premi **Esporta tanda (JSON)** e salvi il file; in PitWall lo **carichi** nella schermata di importazione.
- **Via rete (WiFi/LAN).** In Control premi **Invia a PitWall**: Control **rileva** il tuo PitWall sulla rete locale (o gli indichi l'**IP** a mano) e chiede un **PIN di abbinamento**. Quel PIN è quello mostrato dalla schermata **Importa tanda** di PitWall — digitalo in Control per autorizzare l'invio.

**Cosa crea PitWall.** Ogni **manche** della prova di Control diventa una **tanda**, con ciascuna squadra collocata nella sua **corsia di partenza**. I **riposi** (`D1`, `D2`…) vengono collocati e ruotati come in qualsiasi rotazione (vedi *Tande, partecipanti e rotazione*).

**Con pole.** Se la prova ha la pole (interruttore **La gara ha pole** in Control; esportando su file te lo chiede), Control **non invia l'ordine delle corsie**. Nella schermata di importazione di PitWall spunta **Questa gara ha pole**: PitWall crea la gara con la **sessione di pole** (tutte le squadre) e la griglia si decide **dopo aver corso la pole** (vedi *Pole*).

> Subito dopo l'importazione puoi **modificare la gara** per assegnarle lo **scenario** del tuo club (ed ereditarne corsie, sequenza e tempo minimo) — vedi *Modificare gara, tande e manche*.

> **Requisito:** per l'invio via rete, PitWall e PitWall Control devono trovarsi sulla **stessa rete** LAN/WiFi. Il PIN di abbinamento è mostrato in **Importa tanda** di PitWall. L'altra metà del ponte —**riportare i risultati** verso Control— è spiegata nel *Manuale di PitWall Control*.

> **Connessione ecosistema.** L'intero ponte di rete con PitWall Control —invio delle tande e recupero dei risultati— si può **permettere o bloccare** in blocco da **Sistema → Connessione ecosistema**, nella schermata iniziale. È **attiva** di default; se la disattivi, qualsiasi PitWall Control della rete viene rifiutato (anche con il PIN corretto) finché non la riattivi. Da lì puoi anche consultare il PIN di abbinamento.

## 5. Tande, partecipanti e rotazione
![img: 34-tanda.png]

Una **tanda** raggruppa i partecipanti e la loro **rotazione di corsie** per manche. Aggiungendo le **squadre/piloti**, PitWall genera automaticamente tutte le **manche**.

**Come funziona la rotazione.** Ogni partecipante cambia corsia manche dopo manche seguendo la sequenza configurata (p.es. `1, 3, 5, 6, 4, 2`). Così tutti passano per tutte le corsie e le condizioni si equiparano.

- *Esempio (6 corsie, 6 piloti):* nella manche 1 il pilota A corre la corsia 1; nella manche 2, la 3; nella 3, la 5… fino a completare il giro di tutte le corsie.

**Rotazione a piacere.** PitWall propone automaticamente una rotazione equilibrata, ma **puoi gestirla come vuoi**: riordina la **sequenza di corsie** a mano (trascinando) per decidere esattamente per quale corsia passa ciascun partecipante in ogni manche.

**Riposi.** Se ci sono **più partecipanti che corsie**, la sequenza include spazi vuoti (`0` / `DSC`) che sono **riposi**: in quella manche quel partecipante non corre. PitWall li distribuisce in modo equilibrato, ma **puoi anche collocarli dove vuoi** all'interno della rotazione (trascinali nella posizione che preferisci).

**Corsie vuote (meno partecipanti che corsie).** Non serve riempire tutte le corsie: puoi creare una manche con **meno partecipanti che corsie** (ne basta **uno**). Le corsie in più restano libere, **senza auto fantasma** che compaia nei giri o nella classifica. Alla creazione della manche scegli cosa farne:
- **Restano vuote le ultime** (predefinito): le corsie con il **numero più alto** restano vuote per tutta la gara; nessuno ci corre.
- **Il vuoto ruota**: la corsia (o le corsie) libera **ruota di manche in manche**, così tutti i partecipanti finiscono per passare dalle stesse corsie e la pista resta equa come con la griglia completa.

**Con passate / ripeti corsia:**
- *2 passate* → l'intera sequenza si ripete: `1,3,5,6,4,2, 1,3,5,6,4,2`.
- *Ripeti corsia 2* → ogni corsia, due manche di seguito: `1,1,3,3,5,5,6,6,4,4,2,2`.

## 6. Modificare gara, tande e manche

Dopo aver creato una gara puoi ritoccarla:
- **Modifica gara (“Editar carrera”)** — cambiare il **nome** e, **finché non ci sono giri registrati**, lo **scenario**. Puoi **assegnare** uno scenario a una gara che non ne aveva, **cambiarlo** con un altro o **toglierlo**. **Assegnando** uno scenario, la gara ne eredita le **corsie**, la **sequenza** di rotazione e il **tempo minimo** (e i giri minimi per **categoria**, se presenti), e PitWall **rigenera le tande in sospeso** con quella configurazione; **togliendolo**, la gara passa in **modalità manuale** conservando la configurazione che aveva. Se ci sono già giri, lo scenario resta **bloccato** (per non rovinare i dati).

![img: op-edit-carrera.png]

> Caso tipico: **importi una tanda da PitWall Control** (che arriva in modalità manuale) e poi la **modifichi per assegnarle lo scenario** del tuo club, così eredita corsie, sequenza e tempo minimo della tua pista.

- **Regole di endurance (turni e gomme) (“Reglas de resistencia”)** — in una gara di **endurance**, e **finché non è stata corsa nessuna manche**, Modifica gara ti lascia regolare anche le **regole dei turni per pilota** (minimo e massimo per pilota, numero massimo di turni e il blocco di fine manche) e le **gomme per squadra** (la dotazione con cui parte il controllo gomme) — gli stessi campi che hai fissato nella procedura guidata al momento di creare la gara. Così puoi correggere un numero senza rifare tutta la gara. Appena viene corsa la **prima manche**, quei campi si **bloccano** (attenuati, con un lucchetto 🔒) per non scompaginare ciò che è già stato corso; il **nome** e lo **scenario** mantengono le loro regole di sempre. Se imposti un **massimo per pilota inferiore al minimo**, PitWall ti avvisa.

- **Modifica tanda (“Editar tanda”)** — cambiare i **nomi** dei partecipanti e, se la tanda non è ancora iniziata, la sua composizione. Se ha già manche avviate, entra in **modalità solo rinomina** (non si aggiungono né si tolgono partecipanti, per non scompaginare la rotazione).

![img: op-edit-tanda.png]

> Se vuoi solo portare in una gara i cambiamenti di **piloti o paese** fatti nel catalogo squadre e la gara **non è ancora partita**, non serve toccare «Modifica tanda»: usa **Sistema → Sincronizzare il catalogo** (vedi *Scenari, categorie e cataloghi*). Per una gara che ha già corso una manche, «Modifica tanda» in **modalità solo rinomina** è l'unica via.

- **Modifica manche (“Editar manga”)** — cambiare **chi corre in ogni corsia** in una manche specifica, senza rigenerare tutta la tanda (utile se una squadra non si presenta o c'è un cambio dell'ultimo minuto).

## 7. Pole (qualifica preliminare)
![img: 44-pole-setup.png]

La **pole** è un giro di qualifica **prima** della gara per decidere l'ordine di partenza. È facoltativa; si attiva al momento di creare la gara (**Pole**) e si lancia dalla pagina della gara → **Configura Pole Position (“Configurar Pole Position”)**.

- **Partecipanti**: compaiono tutti gli iscritti in una **griglia numerata** (1, 2, 3…) che si adatta da sola alla larghezza dello schermo e si riempie per colonne —corrispondenti ai gruppi di circuito C1/C2/C3—. Quest'ordine è l'ordine in cui usciranno a fare il loro giro; puoi **trascinare** qualsiasi partecipante a mano per cambiarlo, oppure premere **🎲 Casuale (“🎲 Aleatorio”)** per mescolarlo tutto.
- **Corsia di pole**: **tutti** fanno il loro giro di qualifica sulla **stessa corsia** (perché sia confrontabile). Scegliela con **−/+** o con **🎲 Casuale (“🎲 Aleatorio”)**.
- **Cambio automatico di pilota**: interruttore accanto a **Salta 1° passaggio (“Omitir 1er cruce”)**. Con la casella attiva, al termine del tentativo di un pilota il pulsante **Pilota successivo (“Siguiente piloto”)** fa un conto alla rovescia di 3 secondi e avanza da solo, senza aspettare il clic manuale. È una preferenza della postazione di controllo (si salva nel browser stesso), non della gara.
- Premi **Inizia Pole (“Empezar Pole”)**: ogni partecipante entra a turno, fa il suo giro e PitWall registra il suo miglior tempo. Nel cronometraggio puoi attivare **Salta 1° passaggio (out-lap) (“Omitir 1er cruce (out-lap)”)** per non contare il giro di lancio.
- **Non si presenta (“No se presenta”)**: se il partecipante di turno non si vede in pista, il pulsante Non si presenta lo salta. La prima volta lo manda in **fondo alla coda** —avrà un'altra occasione quando torna il suo turno—; se viene saltato una seconda volta senza aver corso nel frattempo, viene segnato **Assente** per davvero. Gli assenti non competono per la pole con uno 0.00 sintetico come se fosse il giro più veloce: compaiono a parte, in un proprio blocco, sia nella classifica dal vivo sia nei risultati finali.

**Risultati della pole.** Al termine compare **Risultati Pole (“Resultados Pole”)** con la **classifica finale** (dal più veloce al più lento, con il gap dal leader e il **giro veloce**). Da qui puoi **✏️ Modificare i tempi (“✏️ Editar tiempos”)** se c'è stato un errore, o proseguire con **🚦 Assegna corsie di partenza (“🚦 Asignar carriles de salida”)**.

![img: 46-pole-results.png]

**Assegnare le corsie dopo la pole.** La pole non distribuisce le corsie automaticamente: apre la schermata **Scelta della corsia (“Elección de carril”)**, dove ogni partecipante **sceglie** la propria corsia **in ordine di classifica** — il **poleman** (il più veloce) sceglie per primo, poi il 2°, e così via. È il classico "il più veloce sceglie la corsia".

![img: 47-pole-lanes.png]

- Il banner **Sta scegliendo ora (“Eligiendo ahora”)** indica a chi tocca; a sinistra vedi l'**ordine di scelta** (la classifica) e a destra le **corsie disponibili** (con il loro colore).
- Ciascuno preme la corsia che vuole; quella corsia scompare dalle disponibili e il turno passa al successivo.
- **Se ci sono più partecipanti che corsie**, compaiono spazi di **💤 Riposo (“💤 Descanso”)**: chi sceglie il riposo **non corre la manche 1** ed **entra nella rotazione a partire dalla manche 2**.
- Quando tutti hanno scelto, premi **🏁 Crea Prima Tanda (“🏁 Crear Primera Tanda”)**: PitWall crea la tanda e genera tutte le manche con quella griglia come punto di partenza (l'ordine di scelta definisce la posizione iniziale nella rotazione di corsie). Da lì in poi, la gara ruota le corsie manche dopo manche come sempre (vedi *Tande e rotazione*).

> La pole non attribuisce punti in gara: decide solo **chi sceglie la corsia per primo** e, con ciò, la griglia di partenza della prima manche.

**Gli ospiti possono seguire la pole in diretta.** Il tabellone di cronometraggio della pole —prima visibile solo a chi la gestiva— è accessibile senza restrizioni di IP da **Statistiche in diretta**, e compare una nuova scheda nella home ospiti mentre è in corso una pole. È in **sola lettura**: i controlli (avviare/fermare/pilota successivo) sono nascosti e si vede in tempo reale chi è in pista, l'ordine di partenza e la classifica provvisoria.

## 8. PitWall Lap — per le squadre
![img: 43-lap-pins.png]

Le squadre possono seguire la loro gara dal cellulare in **due modi**, non esclusivi: la **vista web con PIN** (niente da installare, di sola lettura) o l'**app nativa PitWall Lap** (si installa sul cellulare, con voce e strategia gomme in diretta).

**Funziona già durante la pole stessa, non solo dopo la sua conclusione.** Le squadre (con il loro PIN) vengono create alla conferma della procedura guidata della gara, invece di aspettare l'assegnazione delle corsie alla fine della pole. Così, ogni squadra vede nel suo pannello se tocca a lei adesso, un cronometro in diretta del suo tentativo, i suoi giri e il suo miglior tempo, con la voce che annuncia ogni giro come in gara; al termine della pole, il pannello passa automaticamente a mostrare il suo risultato (posizione e tempo).

**Vista web con PIN.**
- Entra in **PitWall Lap · PIN** della gara. Vedrai l'indirizzo che le squadre aprono sul cellulare (p.es. `http://<IP-del-server>:3000/lap/<id>`) e la tabella **SQUADRA → PIN**.
- Dai a ogni squadra **il suo PIN**. Aprendo l'indirizzo e inserendolo, entrano direttamente nel loro pannello: posizione proiettata, distacco dal leader, giri, media e pit-stop, con la voce inclusa — di sola lettura, e solo per gare di **endurance** (il dettaglio completo è nel *Manuale delle statistiche*, sezione *PitWall Lap: la tua gara sul cellulare*).
- **Nuovo (“Nuevo”)** rigenera il PIN di una squadra (nel caso trapelasse o volessero cambiarlo).
- **PIN di accesso — Attivato / Disattivato** (“PIN de acceso — Activado / Desactivado”). Sulla stessa scheda dei PIN, un interruttore permette di **togliere il PIN** a questa gara. Con il PIN **disattivato**, ogni squadra entra nel proprio pannello di cronometraggio **solo scegliendosi nell'elenco**, senza digitare nulla (comodo negli eventi interni dove il PIN è d'intralcio). I PIN vengono **conservati** nel caso lo riattivi. È un'impostazione **per gara** e viaggia anche verso il cronometro slave BART quando si sincronizza la gara (Race Link).
- **Monitoraggio dei rivali.** Nel suo pannello, ogni squadra può seguire **fino a 5 rivali** e confrontare corsia per corsia giri, giro migliore e medie (solo manche terminate). La lista si salva per squadra, quindi la condividono tutti i cellulari del box. Dettagli nel *Manuale delle statistiche*, sezione *PitWall Lap*.

> I cellulari devono essere sulla **stessa rete** del computer che fa da server. Usa l'IP del computer, non `localhost`, quando lo aprono dal telefono. Se vuoi che le squadre seguano la gara **da fuori della sede** (via internet), vedi *Seguito pubblico su internet*.

**App nativa PitWall Lap (iOS/Android).** È la via completa: il pilota installa l'app sul cellulare e, aprendola, sceglie la fonte (**PitWall** o il cronometro **TicTac Slot** da solo, senza server dietro) e l'app **scopre il server da sola** sulla rete locale in pochi secondi — senza URL né PIN da distribuire. Se la scoperta automatica fallisce, si inserisce l'IP a mano una volta e l'app la ricorda la volta successiva. Se il server ha più gare o tande attive, lascia scegliere; poi il pilota sceglie il suo **nome/squadra** dalla lista per entrare nel proprio pannello.

Condivide con la vista web il cronometraggio in diretta e la voce (giri, cambi di posizione, metà manche, avvisi di tempo e, in modalità avanzata, medie/distacchi/"media per risalire" ogni N minuti), e in più offre:

- **Strategia gomme in diretta** (gare di endurance, con un pilota selezionato): raccomanda quando cambiare — per degradazione reale del ritmo, oppure in modo **pianificato** in base ai giri/treni rimanenti quando la gomma non perde ritmo —, con consiglio in base alla posizione e modellazione dell'usura dei rivali davanti e dietro. Se la gara usa il **controllo gomme del server** (vedi *Controllo delle gomme di endurance*) e la squadra corrisponde per nome, la dotazione e i cambi li gestisce **PitWall Manager**: l'app li mostra in diretta (treni disponibili, ultimo cambio) senza pulsanti manuali. Senza controllo del server, il pilota tiene il conto a mano (treni, cambi obbligatori, costo del pit-stop) e conferma da sé con **Cambié gomas** ("ho cambiato le gomme").
- **Pole**: schermata propria per seguire il tuo giro di qualifica, il distacco dalla pole e la classifica finale, se la gara ne ha una.
- **Storico e Allenamento**: gare passate (anche quelle non seguite in diretta) e una modalità di allenamento libero che registra le tue sessioni di guida (giri, migliore, media) sul cellulare stesso, con grafico e confronto tra loro.

> L'app non usa il PIN: chiunque sulla **stessa rete locale** scopra il server può scegliere qualsiasi squadra dalla lista. Per un accesso controllato o da fuori dalla pista, usa la vista web con PIN — l'app ha sempre bisogno della rete locale, che tu pubblichi o meno il tunnel di *Seguito pubblico su internet*.

## 9. Dirigere la gara in diretta
![img: 20-live-timing.png]

Dalla pagina della gara:

1. **Armare la manche** (▶). Resta pronta in attesa del **GO** del box.
2. **GO**: dando la partenza dal box, compare il **semaforo** e parte il cronometro. Ogni circuito ha il proprio orologio (C1/C2/C3).
3. Durante la manche vedi per ogni corsia: **totale giri**, **ultimo**, **media**, **miglior**, e in alto il banner del **giro veloce**.
4. **Pausa / Riprendi / Ferma** la manche quando serve.
5. Al termine (bandiera o fine tempo), la manche si chiude e si prepara la **successiva**.
6. Terminate tutte le manche di una tanda, parte la **tanda successiva**.

**La scheda della gara è accessibile con una manche in corso.** Entrare in una gara che ha una manche in corso non ti porta più dritto alla diretta: vedi la sua **scheda** (stato, classifica proiettata, tande…) con un link **«Manga N»** (Manche N) per saltare alla diretta quando vuoi. Quando **dai il GO** dalla scheda, lo schermo salta comunque da solo alla diretta, e non si può ancora avviare una seconda manche mentre un'altra è in corso.

**Scegliere la vista.** Con il pulsante **Vista** scegli tra due viste: *Righe orizzontali* (una riga per corsia) o *Schede con dettagli* (una scheda per corsia, leggibile da lontano). La vecchia *Griglia compatta* non esiste più: se l'avevi scelta, si aprono le schede.

**Le schede.** L'**ultimo giro** compare in grande con il **totale dei giri** accanto e, sotto, miglior giro, media, Gap V e giri della manche; le cifre si adattano da sole alla dimensione della scheda, che ci siano 6, 24 o 40 squadre. L'ultimo giro diventa **viola con «RÉCORD CARRERA»** (record della gara) se è il giro più veloce della gara e **blu con «BOXES»** (box) se includeva una sosta. Ogni scheda mostra il **pilota al volante** con una **barra del tempo già guidato** rispetto al massimo per pilota (**ambra** dall'85 %, **rossa** se lo supera); se una corsia non ha fatto il check-in, vedrai **«SIN PILOTO»** (senza pilota) mentre la manche è in corso. Segnala anche uscite, **soste ai box** («PIT 2») e **treni di gomme** usati sul totale («4/12»).

**Righe su due colonne.** Quando le squadre non stanno in una colonna, la vista a righe si divide in **due colonne**, ognuna con la sua intestazione, per vederle **tutte insieme** (fino a 40 su uno schermo 1080p). Nelle gare con controllo piloti, ogni riga mostra il **pilota sotto la squadra**.

**Ordine della diretta.** In **Impostazioni → Preferenze → Ordine della diretta** («Orden del directo») scegli come ordinare schede e righe: per **classifica stimata** (consigliato) o per **giri reali** (a parità, minor tempo totale). Con i giri reali il Gap V non viene mostrato. La classifica stimata del pannello laterale non cambia.

**Classifica stimata a lato.** In entrambe le viste, il pulsante con l'icona del **pannello laterale** (accanto a **Vista**) apre o chiude la **classifica stimata agganciata a destra** delle righe, come in TicTac: **#**, partecipante, **G. Proi.** (« V. Proy. », giri stimati), **Totale** (giri reali) e **Media**. PitWall ricorda se l'hai lasciata aperta per ogni gara. Di base il pannello usa la **larghezza automatica** (quella giusta per leggere i nomi interi, al massimo il 40% dello schermo) e regola il carattere perché ci stiano tutti; se non ci stanno, cambia pagina ogni 20 s. **Trascinando il bordo** scegli tu la larghezza (se avanza spazio compaiono anche **Gap V** e la tendenza) e con un **doppio clic sul bordo** torna all'automatica. Le righe adattano il carattere allo spazio rimasto: il nome del pilota ha la priorità e, nelle finestre molto strette, si nascondono prima Gap V, poi VLT e poi ULTIMO. Nella vista a schede, con il pannello aperto le schede tolgono miglior giro, media e Gap V (sono già nella classifica) e mantengono i giri della manche sotto il totale.

![img: 20b-live-panel-estimada.png]

**Schermi fissi di sala o TV.** Aggiungendo parametri all'indirizzo della diretta, quello schermo parte sempre allo stesso modo senza toccare ciò che è salvato: `?side=standings` (pannello aperto) o `?side=none` (chiuso), e `?view=1` o `?view=3` (*Righe orizzontali* o *Schede con dettagli*; un vecchio link con `?view=2` apre anch'esso le schede). Si possono combinare: `?view=1&side=standings`.

**Distanza dal leader e stima provvisoria.** Nelle schermate di classifica (**Le Mans** e **statistiche in diretta**) la distanza dal leader viene data **con la virgola** e il suo equivalente **in secondi** —*"a 2,8 v (35,5\")"*, cioè a 2,8 giri, ovvero 35,5 secondi—, non arrotondata a giri interi. E se una stima porta un **asterisco arancione**, quella squadra è ancora nella sua **prima manche** senza aver superato il **60 %**: il suo riferimento non è fissato e la cifra può ancora muoversi. Tutto questo è spiegato in dettaglio nel *Manuale di statistiche*.

**Cambiare tanda, ripetere una manche e finalizzare.** Dalla diretta stessa hai scorciatoie senza uscire dalla schermata:
- **Tanda successiva (“Siguiente tanda”)** — quando finiscono le manche di una tanda, passa direttamente alla successiva.
- **Ripeti manche (“Repetir manga”)** — se una manche è stata annullata (falsa partenza, incidente), la rilanci con gli stessi partecipanti e corsie.
- **Finalizza gara (“Finalizar carrera”)** — chiude la gara (la "bandiera"): si congela la classifica e si genera il riepilogo per i risultati e per i cellulari (PitWall Lap).

> Avviso **"Sin señal del DS-300"**: finché è presente, i giri **non vengono registrati**. Controlla la connessione prima di dare il GO.

## 10. Eventi di gara

La pagina **🗒️ Eventi** —accessibile dalla scheda della gara e con un pulsante nell'intestazione della diretta— mostra, manche dopo manche, tutto quello che accade durante la sessione in un formato facile da leggere: **GO** (anche quando viene dato su più box separatamente, circuito per circuito), **pausa e ripresa** per circuito, **fine manche**, **cancellazione**, **ripristino dopo un'interruzione**, **giri fantasma/ignorati** e la loro **riassegnazione** alla corsia corretta, **partenze retroattive** e i **check-in di pilota** (QR, cambio a caldo o correzione manuale).

Le manche vengono mostrate **compattate per impostazione predefinita** —solo quella in corso appare aperta— e si espandono con un clic sulla loro intestazione. Una casella di controllo permette di **nascondere i check-in di pilota di routine** precedenti al GO quando interessa solo il resto degli eventi.

> Con la manche in corso, la pagina aggiunge i **nuovi eventi man mano che accadono**, senza ricaricare. È il modo per ricostruire, dopo una gara, cosa è successo e quando, senza doverlo ricordare a memoria.

## 11. Controllo dei turni di pilota (campionati)

Nelle gare di **campionato a squadre** puoi imporre regole di ripartizione del volante tra i piloti di una squadra. Si definiscono al momento di creare la gara:
- **Tempo minimo / massimo per pilota** — ogni pilota deve girare almeno X e al massimo Y.
- **Blocco dopo un cambio** — un tempo minimo senza poter ricambiare pilota.
- **Massimo di turni per pilota**.

I **cambi di pilota** si registrano scansionando il **QR del pilota** (o inserendo il suo codice) all'ingresso in pista. Dalla diretta apri **Controllo dei turni (“Control de turnos”)**, che mostra il **pilota attuale per corsia**, il **tempo accumulato** di ciascuno (segnalando se viola una regola) e lo **storico dei turni**; se un cambio è stato registrato male, puoi **correggere il tempo** del turno.

> **La fotocamera dello scanner su telefoni e tablet (HTTPS locale).** Lo scanner di QR usa la fotocamera, e il browser la consente solo su **localhost** (il computer dell'operatore) o via **HTTPS**. Un telefono o tablet che raggiunge PitWall tramite l'IP della rete (192.168.x.x) troverà la fotocamera bloccata, con il messaggio *«La fotocamera richiede HTTPS o localhost»*. Per scansionare da quei dispositivi, attiva **Impostazioni → HTTPS locale (fotocamera dello scanner QR)**: PitWall apre una porta sicura separata (**3443** per impostazione predefinita) senza cambiare nulla del funzionamento normale, e occorre **riavviare** il server una volta. Poi apri il controllo dei turni tramite il link **`https://IP:3443/control/shifts`** (sono pronti in quella stessa sezione delle Impostazioni).

> **L'avviso di sicurezza e come eliminarlo.** La prima volta che un dispositivo apre il link `https://`, il browser avvisa una volta (**«connessione non privata → continua»**); dopo aver accettato, la fotocamera funziona. Se vuoi eliminare quell'avviso, **installa la CA di PitWall** sul dispositivo: nelle Impostazioni trovi **Scarica CA** e la pagina **`/cert`** con la guida passo passo per **iPhone/iPad, Android e Windows**. Installare la CA una sola volta basta anche se cambia l'IP della rete: PitWall riemette solo il certificato del server e il dispositivo continua a fidarsi.

## 12. Controllo delle gomme di endurance

In una gara di **endurance** puoi tenere il conto dei **treni di gomme** che ogni squadra consuma. La dotazione —i treni con cui **tutti** partono— si fissa quando crei la gara (assistente, passo 1, campo **«Gomme per squadra»**). Con **0** il controllo è spento e tutto funziona come prima.

Si apre in **due modi**:
- Dalla gara, con il pulsante **🛞 Gomme** (appare solo in endurance e con una dotazione maggiore di 0).
- Come **chiosco** su `/control/tires` (dal menu iniziale: **Competizione → Controllo gomme**), che **rileva da solo** la gara di endurance in corso —come il chiosco dei turni—. Ideale da lasciare aperto su un tablet accanto al box.

La schermata è una **griglia con tutte le squadre**. Ogni riquadro mostra il nome della squadra e due numeri: **Disponibili** e **Usati**.

- **Un clic sul riquadro = consegnare un treno**: i disponibili scendono di uno, gli usati salgono di uno, e resta **annotato in quale manche e a quale minuto:secondo di gara** è stato fatto il cambio (marcato con la manche in corso e il suo cronometro; se in quel momento non ce n'è nessuna in corso, si salva senza tempo).
- La **matita** di ogni riquadro apre lo **storico** di quella squadra, dove puoi **eliminare** una voce (il treno torna ai Disponibili), **modificare** la sua manche e il suo tempo (mm:ss) o **aggiungerne una a mano** (manche, tempo e una nota).

I contatori **non sono salvati grezzi**: sono **derivati** dalle voci (dotazione meno consegne), quindi annullare non lascia mai squilibri. Se una squadra supera la sua quota, i suoi **Disponibili** possono andare in **negativo e in rosso** —pensato per quando dai un treno extra fuori dotazione.

Nell'intestazione, accanto alla dotazione, il pulsante **🗒️ Storico dei cambi** apre —in una **nuova scheda**— una **pagina** con il **registro globale di tutta la gara** (non quello di una sola squadra). È presentato come una **tabella a colonne** (fino a **tre colonne**) che sfrutta la larghezza dello schermo per vederlo quasi **senza scorrere**. I cambi sono **raggruppati per manche**: sono elencate **tutte le manche**, e quelle senza alcun cambio restano comunque marcate **«— nessun cambio di gomme —»**. In ogni manche, ogni consegna mostra la **squadra** (con il suo punto colorato e il nome), **quale numero di treno** era per quella squadra (**treno N della dotazione**, contato in ordine cronologico —1, 2, 3…—, in **rosso** se ha superato la quota) e il **minuto:secondo di gara**. I cambi senza manche assegnata vanno in un gruppo **«Senza manche»** alla fine. È in **sola lettura** —per eliminare, modificare o aggiungere a mano si usa sempre la matita di ogni squadra— e si **aggiorna in diretta** mentre si consegnano gomme.

**Nella vista in diretta**, ogni scheda di squadra mostra un indicatore **🛞 con il numero di treni di gomme usati**, accanto agli avvisi di **uscite (⚠️)** e **pit-stop (🔧)**. Si **aggiorna all'istante** —senza ricaricare— non appena registri un cambio nel controllo gomme, e **lampeggia** quando il numero aumenta. Appare solo nelle gare di **endurance con controllo gomme**, e funziona sia con la manche **in corso** sia **in attesa**.

> Tutto si sincronizza all'istante tra le schermate aperte, e l'indicatore **manche:tempo** batte al ritmo della gara.

## 13. Verifiche tecniche di PitWall Control

Se il club fa passare la **verifica tecnica** delle vetture con **PitWall Control**, quel risultato può arrivare anche a PitWall — attraverso lo stesso ponte di rete delle tande, con lo stesso PIN e lo stesso interruttore **Connessione ecosistema** (vedi *Importare una tanda da PitWall Control*).

Manche dopo manche, Control invia lo **snapshot** di ciò che ha verificato per squadra: **pesi** (iniziale, finale e minimo della vettura), **motore** (tipo, rpm, ums), **pignone/corona** (marca, denti, diametro, materiale), **cerchi** anteriore e posteriore, **treccia**, **sospensione**, **basamento**, **telaio**, **gomma**, se è risultato **validato** o no, e **osservazioni** —con foto, se presenti.

**Come si vede in PitWall.** Non appena arriva il primo invio, la pagina della gara mostra il pulsante **🔍 Verifiche**, che apre una schermata con tutte le verifiche **raggruppate per manche**.

> **Sola consultazione.** In PitWall non si modifica né si crea alcuna verifica: tutto avviene da PitWall Control. Ogni nuovo invio **sostituisce completamente** le verifiche di quella gara (gli invii non si sommano tra loro).

> **A quale gara vanno.** Se Control indica esplicitamente la gara, PitWall associa a quella le verifiche. In caso contrario cerca una gara esistente con il **nome esatto** della prova; se non trova corrispondenza nemmeno così, **crea automaticamente** una gara minima perché le verifiche abbiano dove stare — lo stesso comportamento dell'importazione di una tanda.

## 14. Giro per giro e correzioni (aggiungere / togliere giri)
![img: 30-correcciones.png]

Dalla gara (pulsante di **correzione dei giri** nella diretta o nei risultati) entri nel **giro per giro** di ogni manche. Serve a sistemare le letture registrate male.

- **Sinistra**: le corsie della manche; scegli la squadra/pilota da revisionare.
- **Destra**: la sua lista di giri — **VLT** (n°), **TEMPO**, **OROLOGIO** (momento di gara) e **Δ PREC.** (differenza col giro precedente).
- **Azioni per giro**:
  - **Trasferisci** (↔) — passare il giro a **un'altra corsia/squadra** (se il sistema lo ha assegnato male).
  - **Fantasma** — segnare il giro come non valido (non conta) senza cancellarlo; si può **ripristinare**.
  - **Cancella** (🗑) — eliminare un giro.
  - **Aggiungi giro manuale** — se è mancato un passaggio, lo aggiungi a mano.

> Usalo con criterio: le correzioni cambiano totali, medie e classifica di quella manche.

> **Giri fantasma automatici.** Un giro al di sotto del **Pt** (tempo minimo) viene segnato come **fantasma** e la corsia che lo ha generato non lo conta **mai**. PitWall non lo riassegna più a occhio: lo **trattiene** e lo assegna solo alla corsia che **conferma** di aver saltato un passaggio (quando quella corsia passa con un giro di ~il doppio della sua media). Se nessuno lo conferma, resta qui come **fantasma** perché tu lo riveda a mano. Con **più circuiti** (aggregatore DS-300 o più Master BART), l'assegnazione automatica **non passa mai da un circuito all'altro**: un fantasma può essere certificato solo su una corsia del proprio circuito, mai su quella di un altro (sono piste fisicamente separate).

## 15. Risultati ed esportazioni
![img: 10-results-comparativa.png]

Al termine (o in qualsiasi momento) entra in **Risultati (“Resultados”)**:

- **Comparativa** (griglia): per partecipante, ogni corsia con **Veloce / Media / Consistenza / Uscite / Pit-stop**. Nelle gare di **passate/ripeti-corsia**, ogni corsia si scompone nelle sue **occorrenze** (1/2, 2/2) per confrontare.
- **Progressione / Posizioni / Gap dal leader / Gap (griglia) / Statistiche avanzate**: diverse viste di analisi (spiegate in dettaglio nel *Manuale delle statistiche*).
- **Esportazioni**: **Excel**, **Punti (xlsx/csv)**, **Control (csv)**, **Esporta per GitHub**, **PDF**.
- **L'esportazione in Excel** (risultati, punti e rapporto turni) **funziona solo a gara ferma o terminata**: non si può ottenere l'Excel mentre una manche è in corso (quel calcolo è pesante e bloccherebbe il cronometraggio, con il rischio di perdere un passaggio). Se una manche parte durante la generazione, l'esportazione viene annullata e basta rilanciarla dopo.

**Risultati pubblici.** C'è una pagina aperta —**Risultati (“Resultados”)**, nel menu iniziale— dove chiunque può consultare (senza toccare nulla né poter modificare) i risultati delle gare **finalizzate**. È quella che condividi con piloti e pubblico affinché guardino la classifica e le statistiche della gara.

![img: op-resultados-publicos.png]

## 16. Allenamento
![img: 40-training.png]

Oltre alle gare, PitWall ha una modalità **Allenamento (“Entrenamiento”)** (dalla schermata iniziale) per girare senza allestire una competizione completa. Ci sono due modalità:

- **Allenamento libero**: registra **giri per corsia senza struttura di squadre**. Ideale per sessioni aperte dove ciascuno prova auto e pista; non c'è rotazione né classifica, solo tempi per corsia.
- **Da competizione**: squadre o piloti assegnati alle corsie con **rotazione automatica dopo ogni tanda**, come una gara ma pensato per allenare il formato di campionato.

Scegli la modalità, assegna le corsie e premi **Inizia (“Empezar”)**. Il cronometraggio in diretta funziona come in gara (GO del box, giri, miglior/media per corsia).

**La diretta dell'allenamento.** In alto hai gli stessi pulsanti della diretta di gara (**GO**, pausa, **STOP**, voce, **Vista**, azzera, schermo intero e **Indietro**). La scheda di ogni corsia mostra:

- l'**ultimo giro** e il suo distacco dal migliore;
- la riga **Migliore / Media / Record**;
- gli **ultimi 10 giri**, ciascuno preceduto dal suo numero di giro;
- un **grafico del ritmo** con le linee del miglior giro e della media: passando il mouse (o il dito) su un punto vedi il numero del giro, il suo tempo e quanto si discosta dal migliore.

La **vista compatta** (pulsante **Vista**) riassume ogni corsia in poco spazio: l'ultimo giro con il suo distacco, Migliore / Media / Record e il ritmo in miniatura.

**Preparare un allenamento da competizione.** Il modulo procede per **passi numerati**: circuito, partecipanti e sequenza di cambio corsia. Per aggiungere squadre, scrivi nella **ricerca del catalogo** (**Invio** aggiunge la prima che corrisponde). Ogni partecipante si può **spostare su o giù di corsia**; **Sorteggia corsie** («Sortear carriles») li distribuisce a caso e **Svuota tutto** («Vaciar todo») riparte da zero. Se due partecipanti hanno lo stesso nome, PitWall ti avvisa. Nella sequenza, **Ordine naturale** («Orden natural») la riporta all'ordine 1, 2, 3… Una **barra fissa in basso** riassume le corsie, quanti sono in pista e quanti di riserva, accanto al pulsante **Prepara sessione** («Preparar sesión»).

**Gli allenamenti da competizione vengono salvati.** Alla **caduta della bandiera di ogni tanda**, PitWall salva una riga per ogni corsia che ha girato, con il suo **partecipante**, i suoi **giri**, il suo **miglior giro** e la sua **media**. I partecipanti **a riposo** e le corsie **senza passaggi** non lasciano righe. Uno **stop forzato non salva** quella tanda: viene scartata e ripetuta per intero.

Dalla schermata di preparazione dell'allenamento da competizione, il link **Vedi allenamenti salvati (“Ver entrenos guardados”)** apre l'elenco delle sessioni (**data**, **n° di tande**, **partecipanti**, **giri** e **miglior giro**), con la più recente in alto. Premendo una sessione ne vedi il dettaglio in due blocchi:

- **Classifica** della sessione: vince chi **somma più giri** in tutte le sue tande e, a parità, chi ha il **miglior giro**. La **media** è quella di **tutti** i suoi giri, ponderata per tanda (una tanda da 40 giri pesa quanto deve rispetto a una da 3).
- **Tanda per tanda**: il dettaglio di ogni tanda, corsia per corsia.

Ogni sessione si può **eliminare** dal suo dettaglio. Se fermi la sessione con **STOP** e ha salvato almeno una tanda, PitWall ti porta direttamente ai **suoi** risultati.

> L'**allenamento libero** non salva risultati: è una sessione aperta di tempi per corsia.

## 17. Impostazioni
![img: 04-settings.png]

Le **Impostazioni** sono organizzate con un **menu laterale**: **Sorgente dati**, **Preferenze**, **Rete locale**, **Seguito online**, **Integrazioni** e **Diagnostica**. Ogni sezione ha la sua schermata, il menu mostra dei punti di stato (cronometro, tunnel, modalità debug) e, dopo aver salvato, torni alla sezione in cui eri. In basso, una **barra di salvataggio fissa** ti avvisa delle **modifiche non salvate** e di quali **richiedono il riavvio** di PitWall (solo l'interfaccia di rete e HTTPS; il resto si applica al salvataggio).

- **Sorgente dati**: scegli da dove arrivano i passaggi — **Simulazione**, **DS-300** (un box per porta, con il suo n° di corsie), **DS-300 aggregatore** (più box su un'unica porta COM: indica **porta**, **baud** —57600, 8N1— e **n° di box** 2/3/4 → 16/24/32 corsie) o **BART** via Bluetooth (si connette in **BLE diretto** per impostazione predefinita; il **TCP** resta nell'elenco per l'emulatore o un ponte BLE→TCP). Con l'aggregatore le corsie sono numerate di seguito (box 1 → 1–8, box 2 → 9–16…) e un unico segnale di partenza avvia tutti i box. Se usi **più Master BART** (uno per ogni blocco di corsie), aggiungi una riga per Master con il suo **nome BLE** (es. `BART_TRACK1`, `BART_TRACK2`…) e il suo **n° di corsie**: sono numerate di seguito come i box dell'aggregatore DS-300, e ogni Master va abbinato separatamente.
- **Configurazione della porta, senza complicazioni**: per ogni circuito DS-300 (e per l'aggregatore) a colpo d'occhio vedi solo **Porta** e **Baud rate**. La **porta** si sceglie dall'elenco rilevato; se la tua non compare, con **« Scrivi il percorso a mano »** la digiti (es. `COM3` o `/dev/ttys003`). Il **baud rate** è un menu a tendina con le velocità abituali (9600–921600), con **« Scrivi a mano »** per un valore fuori elenco. Le impostazioni fini della seriale (**Data bits, Parità, Stop bits, Controllo di flusso**) sono ripiegate in **« Opzioni avanzate della porta »**: di default **8N1**, quasi mai da toccare.
- **Preferenze**: l'**Ordine della diretta** (per classifica stimata o per giri reali; vedi *Dirigere la gara in diretta*).
- **Rete locale**: interfaccia di rete, limitare l'accesso web e HTTPS locale (per la fotocamera del QR).
- **Seguito pubblico su internet**: pubblica le viste pubbliche su internet per seguire la gara da fuori della sede (vedi la sezione seguente).
- **Integrazioni** (compatibilità Infolap, che si attiva e disattiva all'istante) e **Diagnostica** (modalità debug e strumenti per indagare un problema).
- La **lingua** (ES/EN) si cambia dal piè di pagina.

**Database.** **Sistema → Database** (`/database`) ha un menu con **Riepilogo** (quante gare, squadre, piloti, circuiti e giri ci sono, e la dimensione del file), **Esp. / Imp. gara**, **Copia di sicurezza** e **Ripristina copia**.

**Esportare e importare una gara.** Per portare sul tuo PC una gara corsa in un altro club senza spostare l'intero database. **Esporta gara** scarica un file **`.pwrace`** con tutto: squadre, piloti, tornate, manche, giri, turni dei piloti, gomme, eventi, verifiche con foto, pole e categorie (una 24 h da 150.000 giri occupa circa 3 MB). **Importa gara** la aggiunge come **gara nuova, all'istante e senza riavviare**, senza toccare le altre gare; se il suo circuito non esiste su questo PC, viene creato.
- Non si può importare **due volte la stessa gara**: PitWall ti avvisa e ti collega a quella che hai già.
- Una gara con una **manche non chiusa** non si esporta: chiudila o annullala prima in **Risoluzione dei problemi → Manche bloccate**.
- Una gara che era **in corso** entra come **in attesa**, così non prende mai il GO del DS-300 di questo PC.
- Esportazione e importazione aspettano che **non ci sia una manche in corso**, come l'esportazione in Excel.

![img: op-database-carrera.png]

**Backup del database.** **Copia di sicurezza** e **Ripristina copia** permettono di **scaricare** uno snapshot completo dei tuoi dati (`.db`) e, se un giorno serve recuperare un'installazione o spostare PitWall su un altro PC, di **caricare** una copia per ripristinarla: il caricamento viene validato (deve essere un vero database SQLite) e resta "in attesa" — non sostituisce nulla al momento, si applica solo **chiudendo PitWall del tutto e riaprendolo**, e prima di applicarlo viene salvata automaticamente una copia dei dati attuali. Puoi annullare un'importazione in attesa in qualsiasi momento prima di riavviare.

**Cronologia delle versioni.** Nel **piè di pagina di tutte le pagine** vedi il numero di **versione** di PitWall. Premendolo si apre la **Cronologia delle versioni** (`/changelog`), con ciò che è stato **Aggiunto**, **Migliorato** e **Corretto** in ogni aggiornamento. La versione **sale a ogni aggiornamento**, così sai sempre quale PitWall hai e cosa è cambiato.

## 18. Seguito pubblico su internet
![img: op-seguimiento-publico.png]

Per impostazione predefinita le viste di PitWall (la **diretta**, i **Risultati** e la **vista web di PitWall Lap**) sono visibili solo sulla **rete locale**. Con il **Seguito pubblico su internet** ogni club può **pubblicarle su internet** affinché piloti e pubblico seguano la gara **da fuori della sede**, senza aprire porte né configurare una VPN: PitWall attiva un **tunnel Cloudflare proprio** del club.

> L'**app nativa** di PitWall Lap non passa da questo tunnel: ha sempre bisogno di essere sulla **stessa rete locale** del server, che tu la pubblichi su internet o no.

Si trova in **Impostazioni → Seguito pubblico su internet**. Ci sono **due modalità**:

- **Rapido.** PitWall genera al volo una **URL temporanea** (`*.trycloudflare.com`): **senza account né dominio**. È l'opzione per un pomeriggio isolato; tieni presente che la URL **cambia a ogni avvio**.
- **Cloudflare proprio.** Usi il **token del tunnel** del club e **il tuo dominio**, così la **URL è fissa** e col tuo marchio. La schermata stessa contiene una **guida passo passo**, con collegamenti al pannello **Zero Trust** di Cloudflare e alla documentazione ufficiale, per creare il tunnel e incollarne il token.

**Comandi.** Pulsanti **Avvia** / **Ferma** con lo **stato** e la **URL in tempo reale** (da copiare e condividere). **Avvia** applica ciò che hai sullo schermo in quel momento. Puoi attivare l'**avvio automatico** perché il tunnel si attivi da solo all'apertura di PitWall.

**Installare cloudflared.** Il tunnel è attivato dallo strumento `cloudflared`. Se non è installato, compare il pulsante **Installa cloudflared**, che **scarica la versione ufficiale** nella cartella dati di PitWall — **senza chiedere permessi di amministratore**.

> **Sicurezza.** Da fuori **si vedono solo le viste pubbliche** (diretta, risultati e la vista web di PitWall Lap). Il **controllo dell'app** (creare, dirigere o modificare gare) **resta bloccato**: nessuno da fuori può toccare la gara.

## 19. Glossario (operazione)
- **Gara**: l'evento completo. Si compone di tande.
- **Tanda**: gruppo di partecipanti con la sua rotazione; si compone di manche.
- **Manche**: una tornata cronometrata (tutte le corsie insieme) di una certa durata.
- **Rotazione**: come cambiano corsia i partecipanti da una manche all'altra.
- **Riposo**: manche in cui un partecipante non corre (spazio vuoto `0` nella sequenza).
- **Passata**: percorso completo della sequenza di corsie; N passate = N× manche.
- **Ripeti corsia**: correre ogni corsia N manche di seguito, sommando i giri.
- **GO**: il segnale di partenza (del box DS-300) che avvia la manche.
- **Giro fantasma**: giro segnato come non valido (non conta), ripristinabile.
- **Uscita (⚠️)**: giro che impiega più del giro più veloce di quel pilota in quella corsia durante la manche + 1,5 s (come i «giri lenti» di TicTac); se impiega il doppio della sua media pulita o di più, è una sosta ai box (🔧). In diretta è provvisorio: quando il giro più veloce migliora, giri precedenti possono diventare uscite.
- **Pole**: sessione di qualifica preliminare (facoltativa); tutti girano sulla stessa corsia e il loro miglior giro fissa la griglia di partenza.
- **Eventi**: pagina (🗒️) con il registro manche per manche di tutto ciò che succede nella gara —GO, pause, fine manche, giri fantasma, check-in di pilota…—, in diretta.
- **Allenamento libero**: modalità per registrare giri per corsia senza squadre né rotazione (sessione aperta).
- **PitWall Lap**: seguito per squadra/pilota dal cellulare (giri annunciati a voce, posizione e, nell'app, strategia gomme) — come vista web con PIN o come app nativa installata.
- **PIN**: codice per squadra per entrare nel proprio pannello nella vista web di PitWall Lap (l'app nativa non lo usa: scopre il server da sola sulla rete locale).
- **Pt (tempo minimo)**: soglia al di sotto della quale un giro è considerato passaggio fantasma e non conta.
- **Scenario**: pista salvata (circuiti, corsie, sequenza e tempo minimo) riutilizzabile in più gare.
- **Categoria**: classe di auto/pilota (GT, Turismo, Classiche…); permette un Pt diverso per categoria.
- **Catalogo**: libreria riutilizzabile di piloti, squadre e auto (importabile da CSV).
- **QR di pilota**: codice che identifica il pilota per registrare il suo turno alla scansione.
- **Turno (shift)**: periodo in cui un pilota è al volante all'interno della sua squadra in resistenza.
- **DS-300**: il box di cronometraggio che rileva il passaggio sul traguardo.
- **Importa tanda**: portare una prova allestita in PitWall Control (via JSON o via rete LAN + PIN) affinché PitWall crei automaticamente la gara.
- **PitWall Control**: l'app di gestione dei campionati che allestisce la prova e riceve i risultati da PitWall.
- **Seguito pubblico su internet**: pubblicare le viste pubbliche (diretta, risultati, Lap) su internet con un tunnel Cloudflare proprio del club.
- **Tunnel Cloudflare**: connessione che espone su internet le viste pubbliche di PitWall senza aprire porte (modalità Rapido con URL temporanea, o Cloudflare proprio con dominio fisso).
- **Cronologia delle versioni**: la pagina (`/changelog`) che apre il numero di versione del piè di pagina, con ciò che è stato aggiunto, migliorato e corretto in ogni aggiornamento.
