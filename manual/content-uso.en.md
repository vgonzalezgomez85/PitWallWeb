# User manual — PitWall (organization / race direction)

A guide for whoever **operates** PitWall: setting up the race, running it live, fixing laps and producing results.

---

## 1. Introduction
![img: 01-home.png]

**PitWall** is the timing and management system for slot racing. It detects each car crossing the finish line through the timing hardware, with two compatible options:

- **DS-300** — via **serial port**. You can combine **up to 6 DS-300 tracks** in a single race: each box times its own lanes and PitWall combines them. Each box uses **its own port** (one box = one port).
- **DS-300 aggregator** — when an **aggregator device** bundles **several DS-300 boxes (2 to 4) over a single COM port**. PitWall separates the boxes by their frame id and numbers lanes consecutively (box 1 → 1–8, box 2 → 9–16, and so on up to **32 lanes** with 4 boxes). A **single start signal** launches all boxes at once.
- **BART (Policar)** — via **Bluetooth**. It supports **up to the maximum number of lanes that BART allows** (currently **32**).

You can use any of these sources; for PitWall the flow of crossings is equivalent.

- From the **home screen** you reach **Races**, **Settings** and the rest of the modules.
- At the bottom right you always see the **link status** (green = connected; "Sin señal" / no signal = check the cable/port or the Bluetooth).

**The race list** shows all your races with their status (pending / active / finished) and the New race (“+ Nueva carrera”) button.

![img: 02-races-list.png]

## 2. Scenarios, categories and catalogs (your library)

To avoid reconfiguring the same thing for every race, PitWall keeps **reusable templates** that you then pick when creating a race.

**Scenarios (saved tracks).** A **scenario** is a saved physical track: number of tracks and lanes (e.g. `8+8+8 = 24`), its **lane sequence** (rotation) and the **default minimum time**. Any race assigned to that scenario inherits everything automatically.

![img: op-escenarios.png]

When editing a scenario you define its name, the lane configuration, you drag the **rotation sequence** (with **DSC rests** if there are spare drivers), the **default minimum time** and, optionally, **minimum laps per category** (a different Pt for GT, Touring, Classics… on that same track).

![img: op-escenario-form.png]

**Categories.** Level/class groups (GT, Touring, Classics…) that serve to **override the minimum time (Pt) per category** in each scenario and to classify cars and drivers.

![img: op-categorias.png]

**Reusable catalogs (drivers, teams, cars).** Keep your **database** of participants and equipment to reuse it across races:
- **Drivers** — name and category; each driver can have their identification **QR**.
- **Teams** — name, color, country (with its flag; besides standard country flags there are hand-drawn flags for Catalunya and Euskadi), category (colored the same way as in the live view), car and members.
- **Cars** — make, model and category.

All of them can be **bulk-imported from CSV** (the CSV template (“Plantilla CSV”) and Import CSV (“Importar CSV”) buttons, with a preview of new entries vs. duplicates) and exported.

![img: op-catalogo-pilotos.png]

![img: op-qr-pilotos.png]

![img: op-catalogo-equipos.png]

> With Export QR (“Exportar QR”) you print the QR cards for all drivers (for the scan-based driver change in endurance — see *Driver shift control*). The team catalog has its own Export QR, handing out those same cards **grouped by team** (with the team name and category as a header), marking empty teams "no drivers" and members with no linked club driver yet "⚠ no profile".

![img: op-qr-equipos.png]

## 3. Creating a race
![img: 03-wizard-step1.png]

Press New race (“+ Nueva carrera”) and follow the wizard:

- **Type**:
  - *Sprint* → a **quick race**, of **drivers or teams**.
  - *Endurance* → an **endurance race** (by teams), which adds the **control of how much each driver of the team has run** (see *Driver shift control*).
- **Lanes and tracks**: total number of lanes and how they are split across boxes (e.g. 8+8+6 = 3 DS-300 boxes).
- **Minimum lap time (Pt)**: below this time, a crossing is considered a **ghost** (bounce/double read) and does not count.
- **Passes**: how many times the **entire lane sequence** is run. 2 passes = the full rotation is run twice (double the heats).
- **Repeat lane**: each lane is run this number of **consecutive heats** (same lane), adding up the laps — to compare each repetition.
- **Pole** (optional) and **driver rules** (championship only: min/max per driver, change lock at the end of a heat).

> **Passes** and **repeat lane** only change how the heats are generated; totals are summed per participant.

> Do you manage the championship with **PitWall Control**? You don't have to type the teams and rotation again: you can **import the whole event** from Control (see *Importing a batch from PitWall Control*).

## 4. Importing a batch from PitWall Control
![img: op-import-tanda.png]

If you organize the championship with **PitWall Control** (the season manager), you can set up the event there —teams, cups, lanes and rotation— and pass it to PitWall **without typing anything again**. PitWall **auto-creates the race** from what it receives.

Go into **Races → Import batch**. There are **two ways** to bring the event over:

- **JSON file** — in Control you press **Export batch (JSON)** and save the file; in PitWall you **upload** it on the import screen.
- **Over the network (WiFi/LAN)** — in Control you press **Send to PitWall**: Control **discovers** your PitWall on the local network (or you enter the **IP** by hand) and asks for a **pairing PIN**. That PIN is the one shown by PitWall's **Import batch** screen — type it into Control to authorize the send.

**What PitWall creates.** Each **heat** of the Control event becomes a **batch**, with each team placed in its **starting lane**. The **rests** (`D1`, `D2`…) are placed and rotated like in any rotation (see *Batches, participants and rotation*).

**With pole.** If the event has pole (the **This race has pole** switch in Control; when exporting to a file it asks you), Control **does not send the lane order**. On PitWall's import screen tick **This race has pole**: PitWall creates the race with the **pole session** (all teams) and the grid is decided **after running the pole** (see *Pole*).

> Right after importing you can **edit the race** to assign it your club's **scenario** (and inherit its lanes, sequence and minimum time) — see *Editing race, batches and heats*.

> **Requirement:** for the network send, PitWall and PitWall Control must be on the **same** LAN/WiFi network. The pairing PIN is shown in PitWall's **Import batch**. The other half of the bridge —**bringing the results** back to Control— is explained in the *PitWall Control manual*.

> **Ecosystem connection.** The whole network bridge with PitWall Control —sending batches and bringing back results— can be **allowed or blocked** all at once from **System → Ecosystem connection**, on the home screen. It's **enabled** by default; turn it off and any PitWall Control on the network gets rejected (even with the right PIN) until you switch it back on. You can also check the pairing PIN there.

## 5. Batches, participants and rotation
![img: 34-tanda.png]

A **batch** groups the participants and their **lane rotation** per heat. When you add the **teams/drivers**, PitWall automatically generates all the **heats**.

**How rotation works.** Each participant keeps changing lanes from heat to heat following the configured sequence (e.g. `1, 3, 5, 6, 4, 2`). This way everyone goes through every lane and conditions are evened out.

- *Example (6 lanes, 6 drivers):* in heat 1 driver A runs lane 1; in heat 2, lane 3; in heat 3, lane 5… until completing the loop through all lanes.

**Rotation your way.** PitWall proposes a balanced rotation automatically, but **you can manage it however you like**: reorder the **lane sequence** by hand (by dragging) to decide exactly which lane each participant runs in each heat.

**Rests.** If there are **more participants than lanes**, the sequence includes gaps (`0` / `DSC`) that are **rests**: in that heat that participant does not run. PitWall spreads them out evenly, but **you can also place them wherever you want** within the rotation (drag them to the position you prefer).

**Empty lanes (fewer participants than lanes).** You don't have to fill every lane: you can create a heat with **fewer participants than lanes** (**one** is enough). The spare lanes stay empty, with **no ghost car** showing up in laps or standings. When you create the heat you choose what happens to them:
- **Leave the last ones empty** (default): the **highest-numbered** lanes stay empty for the whole race; nobody runs on them.
- **Rotate the gap**: the free lane (or lanes) **rotates heat by heat**, so every participant ends up passing through the same lanes and the track stays just as fair as with a full grid.

**With passes / repeat lane:**
- *2 passes* → the whole sequence repeats: `1,3,5,6,4,2, 1,3,5,6,4,2`.
- *Repeat lane 2* → each lane, two consecutive heats: `1,1,3,3,5,5,6,6,4,4,2,2`.

## 6. Editing race, batches and heats

After creating a race you can tweak it:
- **Edit race** — change the **name** and, **as long as there are no laps recorded**, the **scenario**. You can **assign** a scenario to a race that didn't have one, **change** it for another or **remove** it. When you **assign** a scenario, the race inherits its **lanes**, its rotation **sequence** and its **minimum time** (and the minimum laps per **category**, if it has them), and PitWall **regenerates the pending batches** with that configuration; when you **remove** it, the race switches to **manual mode** keeping the configuration it had. If there are already laps, the scenario is **locked** (so as not to break the data).

![img: op-edit-carrera.png]

> Typical case: you **import a batch from PitWall Control** (which arrives in manual mode) and then **edit it to assign your club's scenario**, so it inherits your track's lanes, sequence and minimum time.

- **Endurance rules (driver shifts and tyres)** — in an **endurance** race, and **as long as no heat has been run yet**, Edit race also lets you adjust the **driver-shift rules** (minimum and maximum per driver, maximum number of stints and the end-of-heat lockout) and the **tyres per team** (the allowance the tyre control starts from) — the same fields you set in the wizard when creating the race. So you can fix a number without rebuilding the whole race. As soon as the **first heat** runs, those fields are **locked** (dimmed, with a padlock 🔒) so as not to unbalance what has already been run; the **name** and the **scenario** keep their usual rules. If you set a **maximum per driver lower than the minimum**, PitWall warns you.

- **Edit batch** — change the **names** of the participants and, if the batch hasn't started yet, its composition. If it already has heats started, it enters **rename-only mode** (no participants added or removed, so as not to unbalance the rotation).

![img: op-edit-tanda.png]

- **Edit heat** — change **who runs in each lane** in a specific heat, without regenerating the whole batch (useful if a team doesn't show up or there's a last-minute change).

## 7. Pole (pre-race qualifying)
![img: 44-pole-setup.png]

The **pole** is a qualifying lap **before** the race to decide the starting order. It's optional; it's enabled when creating the race (**Pole**) and it's launched from the race page → Set up Pole Position (“Configurar Pole Position”).

- **Participants**: everyone entered appears in a **numbered grid** (1, 2, 3…) that resizes itself to the screen width and fills by columns —matching the track groups C1/C2/C3—. That order is the order in which they'll go out to do their lap; you can **drag** any participant by hand to change it, or hit 🎲 Random (“🎲 Aleatorio”) to shuffle the whole thing.
- **Pole lane**: **everyone** does their qualifying lap on the **same lane** (so it's comparable). Pick it with **−/+** or with 🎲 Random (“🎲 Aleatorio”).
- **Automatic driver advance**: a toggle next to Skip 1st crossing (“Omitir 1er cruce”). With it on, when a driver's attempt ends the Next driver (“Siguiente piloto”) button counts down 3 seconds and advances on its own, without waiting for a manual click. It's a preference of the control desk (saved in the browser itself), not of the race.
- Press Start Pole (“Empezar Pole”): each participant enters in turn, does their lap and PitWall records their best time. In timing you can enable Skip 1st crossing (“Omitir 1er cruce”) (out-lap) so the launch lap isn't counted.
- No-show (“No se presenta”): if the participant whose turn it is doesn't show up on track, the No-show button skips them. The first time it sends them to the **end of the queue** —they'll get another chance when their turn comes round again—; if they get skipped a second time without having run in between, they're marked **absent** for good. No-shows don't compete for pole with a synthetic 0.00 as if it were the fastest lap: they appear separately, in their own block, both in the live standings and in the final results.

**Pole results.** When it finishes, Pole Results (“Resultados Pole”) appears with the **final classification** (from fastest to slowest, with the gap to the leader and the **fastest lap**). From here you can ✏️ Edit times (“✏️ Editar tiempos”) if there was an error, or continue with 🚦 Assign starting lanes (“🚦 Asignar carriles de salida”).

![img: 46-pole-results.png]

**Assigning lanes after the pole.** The pole doesn't distribute lanes automatically: it opens the Lane choice (“Elección de carril”) screen, where each participant **chooses** their lane **in classification order** — the **poleman** (the fastest) chooses first, then the 2nd, and so on. It's the classic "the fastest one picks lane".

![img: 47-pole-lanes.png]

- The Choosing now (“Eligiendo ahora”) banner indicates whose turn it is; on the left you see the **choosing order** (the classification) and on the right the **available lanes** (with their color).
- Each one presses the lane they want; that lane disappears from the available ones and the turn passes to the next.
- **If there are more participants than lanes**, 💤 Rest (“💤 Descanso”) gaps appear: whoever picks a rest **doesn't run heat 1** and **enters the rotation from heat 2**.
- When everyone has chosen, press 🏁 Create First Batch (“🏁 Crear Primera Tanda”): PitWall creates the batch and generates all the heats with that grid as the starting point (the choosing order defines the initial position in the lane rotation). From there, the race rotates the lanes heat to heat as always (see *Batches and rotation*).

> The pole doesn't score in the race: it only decides **who picks lane first** and, with that, the starting grid of the first heat.

**Guests can now follow the pole live.** The pole's timing board —previously only visible to whoever was running it— is now reachable with no IP restriction from **Live stats**, and a new card appears on the guest home while a pole is under way. It's **read-only**: the controls (start/stop/next driver) are hidden, and you see in real time who's on track, the starting order and the provisional classification.

## 8. PitWall Lap — for the teams
![img: 43-lap-pins.png]

Teams can follow their race from the phone **two ways**, not mutually exclusive: the **web view with PIN** (nothing to install, read-only) or the **native PitWall Lap app** (installed on the phone, with voice and live tyre strategy).

**It already works during the pole itself, not just after it's over.** Teams (with their PIN) are created as soon as the race wizard is confirmed, instead of waiting for lanes to be assigned at the end of the pole. So each team's panel tells them if it's their turn now, with a live timer for their attempt, their laps and their best time, with the voice calling out every lap just like in the race; once the pole ends, the panel switches on its own to showing their result (position and time).

**Web view with PIN.**
- Go into **PitWall Lap · PINs** (“PitWall Lap · PINs”) of the race. You'll see the address teams open on the mobile (e.g. `http://<server-IP>:3000/lap/<id>`) and the **TEAM → PIN** table.
- Give each team **their PIN**. When they open the address and enter it, they go straight into their panel: projected position, gap to the leader, laps, average and pit-stops, voice included — read-only, and only for **endurance** races (the full detail is in the *Statistics manual*, section *PitWall Lap: your race on the phone*).
- New (“Nuevo”) regenerates a team's PIN (in case it was leaked or they want to change it).

> The phones must be on the **same network** as the computer acting as server. Use the computer's IP, not `localhost`, when they open it from the phone. If you want teams to follow the race **from outside the venue** (over the internet), see *Public tracking over the internet*.

**Native PitWall Lap app (iOS/Android).** This is the full route: the driver installs the app on their phone and, on opening it, picks the source (**PitWall** or the **TicTac Slot** timer standalone, with no server behind it) and the app **discovers the server on its own** on the local network within a few seconds — no URL or PIN to hand out. If auto-discovery fails, the IP is entered by hand once and the app remembers it for next time. If the server has several active races or batches, it lets you choose; then the driver picks their **name/team** from the list to enter their panel.

It shares live timing and voice with the web view (laps, position changes, half-heat, time warnings and, in advanced mode, averages/gaps/"average to catch up" every N minutes), and on top of that offers:

- **Live tyre strategy** (endurance races, with a driver selected): recommends when to change — by real pace degradation, or on a **scheduled** basis by remaining laps/sets when the tyre isn't losing pace — with position-based advice and modelling of the tyre wear of the rivals ahead and behind. If the race is running the **server tyre control** (see *Endurance tyre control*) and the team matches by name, the allotment and the changes are driven by **PitWall Manager**: the app shows them live (sets available, last change) with no manual buttons. Without server control, the driver keeps count by hand (sets, mandatory changes, pit-stop cost) and confirms it themselves with **Cambié gomas** ("I changed tyres").
- **Pole**: its own screen to follow your qualifying lap, the gap to pole and the final classification, if the race has one.
- **History and Training**: past races (even ones you didn't follow live) and a free-training mode that records your practice runs (laps, best, average) on the phone itself, with a chart and comparison between them.

> The app doesn't use a PIN: anyone on the **same local network** who discovers the server can pick any team from the list. For controlled access or from outside the venue, use the web view with PIN — the app always needs the local network, whether or not you publish the *Public tracking over the internet* tunnel.

## 9. Running the race live
![img: 20-live-timing.png]

From the race page:

1. **Arm the heat** (▶). It stays ready waiting for the **GO** from the box.
2. **GO**: when the start is given at the box, the **lights** appear and the timer starts. Each track has its own clock (C1/C2/C3).
3. During the heat you see per lane: **total laps**, **last**, **average**, **best**, and at the top the **fastest lap** banner.
4. **Pause / Resume / Stop** the heat when needed.
5. When it ends (flag or time out), the heat closes and the **next one** is prepared.
6. When all the heats of a batch are done, the **next batch** starts.

**Choosing the view.** With the View (“Vista”) button you change the layout depending on the lanes: *Horizontal rows* (few lanes), *Compact grid* (many) or *Cards with details* (with laps/exits/pit/tyres/Δ per card).

**Distance to the leader and provisional estimate.** On the classification screens (**Le Mans** and **live stats**) the distance to the leader is given **with the fraction** and its equivalent **in seconds** —*"a 2,8 v (35,5\")"*, i.e. 2.8 laps behind, worth 35.5 seconds—, not rounded to whole laps. And if an estimate carries an **orange asterisk**, that team is still in its **first heat** without having gone past **60 %** of it: its reference isn't locked in yet and the figure can still move. It's all explained in detail in the *Statistics manual*.

**Switching batch, repeating a heat and finishing.** From the live screen itself you have shortcuts without leaving the screen:
- **Next batch** — when a batch's heats are done, it moves straight to the next.
- **Repeat heat** — if a heat was called bad (false start, incident), you launch it again with the same participants and lanes.
- **Finish race** — closes the race (the "flag"): the classification is frozen and the summary is generated for results and for the mobiles (PitWall Lap).

> "Sin señal del DS-300" (no DS-300 signal) warning: while it's showing, laps are **not recorded**. Check the connection before giving the GO.

## 10. Race events

The **🗒️ Race events** (“🗒️ Sucesos”) page —reachable from the race page and with a button in the live screen's header— shows, heat by heat, everything that happens during the session in an easy-to-read format: **GO** (including when it's given on several boxes separately, track by track), **pause and resume** per track, **end of heat**, **cancellation**, **recovery after a cut**, **ghost/ignored laps** and their **reassignment** to the right lane, **retroactive exits** and **driver check-ins** (QR, on-the-fly change or manual correction).

Heats are shown **collapsed by default** —only the one under way appears open— and expand with a click on their header. A checkbox lets you **hide routine driver check-ins** before the GO when only the rest of the events matter.

> While the heat is running, the page keeps **adding new events as they happen**, without reloading. It's the way to reconstruct, after a race, what happened and when, without relying on memory.

## 11. Driver shift control (championships)

In **team championship** races you can enforce rules for sharing the wheel among a team's drivers. They are defined when creating the race:
- **Minimum / maximum time per driver** — each driver must run at least X and at most Y.
- **Lock after a change** — a minimum time before changing driver again.
- **Maximum number of shifts per driver**.

**Driver changes** are recorded by scanning the **driver's QR** (or entering their code) when they come onto the track. From the live screen you open **Shift control**, which shows the **current driver per lane**, the **accumulated time** of each one (warning if they break a rule) and the **shift history**; if a change was recorded wrong, you can **correct the time** of the shift.

> **The scanner camera on phones and tablets (local HTTPS).** The QR scanner uses the camera, and the browser only allows it on **localhost** (the operator's computer) or over **HTTPS**. A phone or tablet reaching PitWall through the network IP (192.168.x.x) will find the camera blocked, with the message *"Camera needs HTTPS or localhost"*. To scan from those devices, enable **Settings → Local HTTPS (QR scanner camera)**: PitWall opens a separate secure port (**3443** by default) without changing anything about normal operation, and the server must be **restarted** once. Then open driver control through the link **`https://IP:3443/control/shifts`** (they are ready for you in that same Settings section).

> **The security warning and how to remove it.** The first time a device opens the `https://` link, the browser warns once (**"connection not private → continue"**); once you accept, the camera works. If you want that warning gone, **install the PitWall CA** on the device: Settings has **Download CA** and the **`/cert`** page with a step-by-step guide for **iPhone/iPad, Android and Windows**. Installing the CA once is enough even if the network IP changes: PitWall only re-issues the server certificate and the device keeps trusting it.

## 12. Endurance tyre control

In an **endurance** race you can keep track of the **tyre sets** each team uses. The allotment —the sets **everyone** starts with— is set when you create the race (wizard, step 1, **"Tyres per team"** field). With **0**, control is off and everything works as before.

It opens **two ways**:
- From the race, with the **🛞 Tyres** button (only shows in endurance races and with an allotment greater than 0).
- As a **kiosk** at `/control/tires` (with its card on the home screen), which **auto-detects** the endurance race currently running —just like the shifts kiosk—. Ideal to leave open on a tablet next to the pit.

The screen is a **grid with every team**. Each box shows the team name and two numbers: **Available** and **Used**.

- **One click on the box = hand out a set**: available goes down by one, used goes up by one, and it is **recorded in which heat and at which minute:second of the race** the change was made (stamped with the running heat and its clock; if none is running at that moment, it is saved without a time).
- The **pencil** on each box opens that team's **history**, where you can **delete** an entry (the set returns to Available), **edit** its heat and time (mm:ss) or **add one by hand** (heat, time and a note).

The counters are **not stored raw**: they are **derived** from the entries (allotment minus hand-outs), so undoing never leaves a mismatch. If a team goes over its quota, its **Available** can go **negative and red** —meant for when you give an extra set beyond the allotment.

In the header, next to the allotment, the **🗒️ Change history** button opens —in a **new tab**— a **page** with the **global log for the whole race** (not just one team's). It is laid out as a **table in columns** (up to **three columns**) that uses the screen width so you can see it almost **without scrolling**. Changes are **grouped by heat**: **every heat** is listed, and those with no changes are still marked **“— no tyre changes —”**. Within each heat, every hand-out shows the **team** (with its colour dot and name), **which set number** it was for that team (**set N of the allotment**, counted in chronological order —1, 2, 3…—, in **red** if it went over quota) and the **minute:second of the race**. Changes with no heat assigned go to a **“No heat”** group at the end. It is **read-only** —to delete, edit or add by hand you still use each team's pencil— and it **refreshes live** while tyres are being handed out.

**In the live view**, each team card shows a **🛞 indicator with the number of tyre sets used**, alongside the existing **starts (⚠️)** and **pit-stops (🔧)** warnings. It **updates instantly** —no reload— the moment you record a change in the tyre control, and it **flashes** when the number goes up. It only appears in **endurance races with tyre control**, and it works whether the heat is **running or waiting**.

> Everything syncs instantly across open screens, and the **heat:time** indicator ticks along with the race.

## 13. Technical inspection from PitWall Control

If your club runs **technical inspection** of the cars through **PitWall Control**, those results can also reach PitWall — over the same network bridge as batches, with the same PIN and the same **Ecosystem connection** switch (see *Importing a batch from PitWall Control*).

Heat by heat, Control sends the **snapshot** of what it has inspected per team: **weights** (starting, final and minimum car weight), **motor** (type, rpm, ums), **pinion/crown gear** (make, teeth, diameter, material), front and rear **wheels**, **braid**, **suspension**, **chassis bed**, **chassis**, **tyre**, whether it was **passed** or not, and **notes** —with photos, if any.

**How it looks in PitWall.** As soon as the first submission arrives, the race page shows a **🔍 Inspections** button, which opens a screen with every inspection **grouped by heat**.

> **Read-only.** PitWall never edits or creates an inspection: everything is done from PitWall Control. Every new submission **fully replaces** that race's inspections (there's no accumulating separate hand-outs).

> **Which race it lands on.** If Control specifies the race explicitly, PitWall attaches the inspections to that one. Otherwise it looks for an existing race with the **exact same name**; if there's still no match, it **automatically creates** a minimal race for the inspections to live in — the same behaviour as importing a batch.

## 14. Lap by lap and corrections (add / remove laps)
![img: 30-correcciones.png]

From the race (the **lap correction** button in the live screen or in results) you enter the **lap by lap** of each heat. It serves to fix wrongly recorded readings.

- **Left**: the lanes of the heat; pick the team/driver to review.
- **Right**: their lap list — **LAP** (no.), **TIME**, **CLOCK** (race moment) and **Δ PREV.** (difference from the previous lap).
- **Actions per lap**:
  - **Transfer** (↔) — pass the lap to **another lane/team** (if the system assigned it wrong).
  - **Ghost** — mark the lap as invalid (doesn't count) without deleting it; it can be **restored**.
  - **Delete** (🗑) — remove a lap.
  - **Add manual lap** — if a crossing was missed, you add it by hand.

> Use it with judgment: corrections change totals, averages and classification of that heat.

> **Automatic ghost laps.** A lap below the **Pt** (minimum time) is marked as a **ghost** and the lane that produced it **never** counts it. PitWall no longer reassigns it by guessing: it **holds** it and only assigns it to the lane that **confirms** it missed a crossing (when that lane crosses with a lap of ~double its average). If nobody confirms it, it stays here as a **ghost** for you to review by hand.

## 15. Results and exports
![img: 10-results-comparativa.png]

When it finishes (or at any time) go into **Results**:

- **Comparison** (grid): per participant, each lane with **Fastest / Average / Consistency / Exits / Pit-stops**. In **passes/repeat-lane** races, each lane is broken down into its **occurrences** (1/2, 2/2) to compare.
- **Progression / Positions / Gap to leader / Gap (grid) / Advanced statistics**: different analysis views (explained in detail in the *Statistics manual*).
- **Exports**: **Excel**, **Points (xlsx/csv)**, **Control (csv)**, **Export for GitHub**, **PDF**.

**Public results.** There's an open page —**Results**, in the home menu— where anyone can consult (without touching anything or being able to edit) the results of the **finished** races. It's the one you share with drivers and public so they can look at the classification and statistics of the race.

![img: op-resultados-publicos.png]

## 16. Training
![img: 40-training.png]

Besides races, PitWall has a **Training** mode (from the home screen) to run without setting up a full competition. There are two modes:

- **Free training**: records **laps per lane without a team structure**. Ideal for open sessions where each person tries the car and track; there's no rotation or classification, just times per lane.
- **Competition**: teams or drivers assigned to lanes with **automatic rotation after each batch**, like a race but designed to practice the championship format.

Choose the mode, assign the lanes and press **Start**. Live timing works the same as in a race (box GO, laps, best/average per lane).

**Competition training sessions are saved.** When **each heat's flag drops**, PitWall saves one row per lane that ran, with its **participant**, its **laps**, its **best lap** and its **average**. Participants who are **resting** and lanes **with no crossings** leave no row. A **forced stop does not save** that heat: it's discarded and repeated in full.

From the competition training setup, the **See saved sessions** link opens the list of sessions (**date**, **no. of heats**, **participants**, **laps** and **best lap**), most recent first. Pressing a session shows its detail with two blocks:

- **Classification** for the session: the winner is whoever **adds up the most laps** across all their heats and, on a tie, whoever has the **best lap**. The **average** is that of **all** their laps, weighted per heat (a 40-lap heat carries the weight it should against a 3-lap one).
- **Heat by heat**: the breakdown of each heat, lane by lane.

Each session can be **deleted** from its detail. If you stop the session with **STOP** and it saved at least one heat, PitWall takes you straight to **its** results.

> **Free training** does not save results: it's an open session of times per lane.

## 17. Settings
![img: 04-settings.png]

- **Data source**: choose where crossings come from — **Simulation**, **DS-300** (one box per port, with its lane count), **DS-300 aggregator** (several boxes over a single COM port: set the **port**, **baud** —57600, 8N1— and **number of boxes** 2/3/4 → 16/24/32 lanes) or **BART** over Bluetooth (it connects over **direct BLE** by default; **TCP** stays in the list for the emulator or a BLE→TCP bridge). With the aggregator, lanes are numbered consecutively (box 1 → 1–8, box 2 → 9–16…) and a single start signal launches all boxes.
- **Port setup, kept simple**: for each DS-300 circuit (and the aggregator) you only see **Port** and **Baud rate** at a glance. Pick the **port** from the detected list; if yours isn't there, tap **"Type the path manually"** to enter it (e.g. `COM3` or `/dev/ttys003`). The **baud rate** is a dropdown with the usual speeds (9600–921600), with **"Type manually"** for an out-of-list value. The fine serial settings (**Data bits, Parity, Stop bits, Flow control**) are folded under **"Advanced port options"**: they default to **8N1** and rarely need touching.
- **Tracks**: define saved tracks (lane sequence, minimum time).
- **Public tracking over the internet**: publish the public views on the internet to follow the race from outside the venue (see the next section).
- **License** and language (ES/EN).

**Database backup.** From the home screen, the **Database** card (`/database`) lets you **download** a full snapshot of your data (`.db`) and, if you ever need to recover an install or move PitWall to another PC, **upload** a backup to restore it: the upload is validated (it must be a real SQLite database) and stays "pending" — nothing is replaced right away, it only applies once you **fully close PitWall and reopen it**, and your current data is backed up automatically before applying it. You can cancel a pending import at any time before restarting.

**Version history.** In the **footer of every page** you see PitWall's **version** number. Pressing it opens the **Version history** (`/changelog`), with what was **Added**, **Improved** and **Fixed** in each update. The version **goes up with every update**, so you always know which PitWall you have and what has changed.

## 18. Public tracking over the internet
![img: op-seguimiento-publico.png]

By default PitWall's views (the **live timing**, the **Results** and the **PitWall Lap web view**) are only visible on the **local network**. With **Public tracking over the internet** each club can **publish them on the internet** so drivers and public can follow the race **from outside the venue**, without opening ports or setting up a VPN: PitWall brings up the club's **own Cloudflare tunnel**.

> The **native app** of PitWall Lap doesn't go through this tunnel: it always needs to be on the **same local network** as the server, whether you publish it on the internet or not.

It's in **Settings → Public tracking over the internet**. There are **two modes**:

- **Quick.** PitWall generates a **temporary URL** (`*.trycloudflare.com`) on the fly: **no account or domain**. It's the option for a one-off afternoon; keep in mind the URL **changes on every start**.
- **Own Cloudflare.** You use the club's **tunnel token** and **your own domain**, so the **URL is fixed** and branded. The screen itself carries a **step-by-step guide**, with links to Cloudflare's **Zero Trust** dashboard and to the official documentation, to create the tunnel and paste its token.

**Controls.** **Start** / **Stop** buttons with the **status** and the **live URL** (to copy and share it). **Start** applies whatever you have on screen at that moment. You can enable **auto-start** so the tunnel comes up by itself when PitWall opens.

**Install cloudflared.** The tunnel is brought up by the `cloudflared` tool. If it isn't installed, the **Install cloudflared** button appears, which **downloads the official version** to PitWall's data folder — **without asking for administrator permissions**.

> **Security.** From outside, **only the public views are visible** (live timing, results and the PitWall Lap web view). The **app control** (creating, running or editing races) is **blocked**: no one from outside can touch the race.

## 19. Glossary (operation)
- **Race**: the complete event. Made up of batches.
- **Batch**: group of participants with their rotation; made up of heats.
- **Heat**: one timed run (all lanes at once) of a set duration.
- **Rotation**: how participants change lanes from one heat to another.
- **Rest**: a heat in which a participant doesn't run (a `0` gap in the sequence).
- **Pass**: a complete run through the lane sequence; N passes = N× heats.
- **Repeat lane**: run each lane N consecutive heats, adding up laps.
- **GO**: the start signal (from the DS-300 box) that launches the heat.
- **Ghost lap**: a lap marked as invalid (doesn't count), restorable.
- **Pole**: a pre-race qualifying session (optional); everyone runs on the same lane and their best lap sets the starting grid.
- **Race events**: the (🗒️) page with the heat-by-heat log of everything happening in the race —GO, pauses, end of heat, ghost laps, driver check-ins…—, live.
- **Free training**: mode to record laps per lane without teams or rotation (open session).
- **PitWall Lap**: per-team/driver tracking from the phone (called-out laps, position and, in the app, tyre strategy) — as a web view with PIN or as an installed native app.
- **PIN**: per-team code to enter their panel in the PitWall Lap web view (the native app doesn't use one: it discovers the server on its own on the local network).
- **Pt (minimum time)**: threshold below which a lap is considered a ghost crossing and doesn't count.
- **Scenario**: a saved track (tracks, lanes, sequence and minimum time) reusable across several races.
- **Category**: a car/driver class (GT, Touring, Classics…); allows a different Pt per category.
- **Catalog**: reusable library of drivers, teams and cars (importable via CSV).
- **Driver QR**: a code that identifies the driver to record their shift when scanned.
- **Shift**: the period a driver is at the wheel within their team in endurance.
- **DS-300**: the timing box that detects the crossing at the line.
- **Import batch**: bring in an event set up in PitWall Control (by JSON or over LAN + PIN) so PitWall auto-creates the race.
- **PitWall Control**: the championship-management app that sets up the event and receives the results from PitWall.
- **Public tracking over the internet**: publish the public views (live timing, results, Lap) on the internet with the club's own Cloudflare tunnel.
- **Cloudflare tunnel**: a connection that exposes PitWall's public views on the internet without opening ports (Quick mode with a temporary URL, or Own Cloudflare with a fixed domain).
- **Version history**: the page (`/changelog`) opened by the version number in the footer, with what was added, improved and fixed in each update.
