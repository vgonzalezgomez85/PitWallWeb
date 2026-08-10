# Manual for reading the Live / Statistics views

A guide for drivers. No jargon. The idea is simple: **what each number tells you and how to use it to go faster and more consistently.**

In PitWall you race by **lanes** (C1, C2, C3…) and you keep **rotating lanes heat to heat**. That's why there are two ways to look at your race: **what's happening NOW in this heat** and **how you'll end up AT THE END** when you add up all your heats. This manual teaches you to read both.

---

## 1. The live screen

![img: 20-live-timing.png]

It's the screen of the heat in progress. What you see in real time, lap by lap.

**Clocks per track (C1, C2, C3…).** If the race uses several tracks at once, at the top you have one clock for each. Each clock marks the time of that heat on that track. When the clock reaches zero, that heat ends and everyone rotates lanes.

**Lane cards.** One card per car on track. On each card you read, at a glance:

- **TOTAL** — laps accumulated so far in the heat.
- **LAST** — your last complete lap. It's your immediate reference: are you improving or dropping off?
- **AVERAGE** — your average pace in the heat (a simple average of your laps, not counting the **start crossing**; your first complete lap **does** count). It's what really matters for winning in endurance: not the odd fast lap, but sustained pace.
- **BEST** — your best valid lap of the heat.

**Fastest lap banner.** When someone sets the fastest lap of the moment, a highlighted alert pops up. If it's yours, good. If it's a rival's, it's the benchmark to beat.

### The three live views (the "Vista" button)

With the View (“Vista”) button you choose how the cards are shown, depending on how many lanes there are. There are three modes:

**1 · Horizontal rows** — one row per lane. Recommended for **few lanes**: each lane takes a wide row and reads very comfortably.

![img: 31-vista-1.png]

**2 · Compact grid** — all the tracks at once in a grid. Ideal for **many lanes**: you see everything without scrolling.

![img: 31-vista-2.png]

**3 · Cards with details** — like the compact one, but with **LAP** (laps), **EXIT** (exits), **PIT** and **Δ** visible on each card. More information per lane at a glance.

![img: 31-vista-3.png]

---

## 2. Live-stats: the 3 tabs

Live-stats is the statistics view. It has three tabs and each one answers a different question.

**Current heat.**

![img: 21-livestats-manga.png]

The classification of **this** heat, with the detail of each driver: **L** (laps), **BEST**, **AVERAGE**, **Δ** (delta, your margin), **EXITS** and **LOST** (time lost in exits). Look at it to know how you're doing NOW, who you share a lane with and who leads your heat.

**Projected classification.**

![img: 22-livestats-proyectada.png]

The estimated position **at the end of the race**, when everyone has completed all their heats. It's the one that really matters to know if you're winning. Look at it to know your REAL position in the overall, not just in the heat you're running.

**Lane comparison.**

![img: 23-livestats-carril.png]

How each lane performs. Some lanes are faster than others. Here you see the differences between C1, C2, C3… Look at it to know if your current lane helps or penalizes you, and which lanes you have left to run.

**Quick rule:** *Current heat* = the snapshot of now. *Projected* = how you finish. *Lane* = why your pace changes from heat to heat.

---

## 3. Your panel (My panel)

![img: 21b-livestats-mipanel.png]

Choose your driver and you'll have your own panel with cards. One by one:

**POSITION.** Watch out for this one: it's your **PROJECTED race position**, not the heat one. It tells you where you'll finish if the pace holds. If in your heat you're 4th but your panel says P1, it means that adding up all the heats you're first. Trust this one.

**HEAT LAPS.** How many laps you have in the current heat.

**BEST.** Your best valid lap. "Valid" means that **it does NOT count**:
- the **start crossing** (from the grid to the line, starting from a standstill: it's half the layout, not a lap),
- nor a **partial crossing** (a lap that's really half a lap miscounted),
- nor times **below the minimum** of the race (impossible ghost crossings).

Careful with this one: **your first complete lap DOES count** — it's real pace and it can perfectly well be your best lap. The only thing discarded is that first crossing from a standstill. So your BEST is a truly real lap, never a gifted number nor a good lap that gets lost.

**AVERAGE.** Your average pace. A simple average of your race laps (includes exits and pit-stops; only excludes the **start crossing**). It's exactly the same criterion TicTac uses, to the millisecond. It's the number the projection uses to estimate where you finish. **Lower your average and you climb in the overall.**

**Δ (delta).** It's your **clean average minus your best lap**. That is: how much margin you have left. A small Δ = you almost always run flat out, very little to shave off. A big Δ = you have pace but lose it on many laps: that's where your gold is, in being more consistent. The "clean average" here doesn't count exits or pits, only your normal running.

**EXITS / PIT-STOPS.** How many times you've gone off and how many stops you've made. Each exit costs you time and positions.

**Time lost in exits.** What those exits cost you, in seconds. Put it in context: sometimes a single exit is worth more positions than tenths of pace throughout the whole heat. Here you see it clearly.

---

## 4. PitWall Lap: your race on the phone

![img: 45-lap-access.png]

**PitWall Lap** is the web page you open on the **phone from your box** to follow your race live, without installing anything. It's only for **endurance (team) races**. It's read-only: you consult your timing, you don't control the race.

**How you get in.** The organization gives you the address (something like `http://<server-IP>:3000/lap/<race>`) and a **4-digit PIN** for your team. You open the address, pick your **team** in the list, enter the **PIN** and press Enter (“Entrar”). With Change team (“Cambiar equipo”) you can log out and log in with another.

![img: 48-lap-team-panel.png]

**Your panel.** At the top, your **position** in large: it's the **projected** one (where you'll finish adding up all the heats), the same one you see in the live screen and in the overall — not the standalone heat one. Below, your distance to the leader (*"N laps down"*, *"level"* or *"🏁 Race leader"*). The status line tells you live **which heat and lane you're on and how much is left** (or *"Resting"* / *"Waiting for next heat"* / *"Race finished"*). And the cards:

- **Last lap** — your last lap (blinks when it updates).
- **Best lap** — your best valid lap.
- **Laps** — total accumulated over the whole race.
- **Race average** — your accumulated average pace (the one the projection uses).
- **Pit stops** — stops made.
- **Gap to leader** — how many laps behind the first.

If projection is active, Estimate at the finish appears with your **estimated position** and your **projected laps**.

**The voice (lap caller).** With the 🔊 Voice (“🔊 Voz”) button you enable the announcer (it starts **off**: you have to tap the screen once so the phone allows the audio to play). It calls out the **time of each lap**, and warns of **position change**, **half heat**, **last minute**, **last 30 s** and **end of heat**. In ⚙️ Voice settings (“⚙️ Ajustes de voz”) you enable/disable each alert and, in the advanced block, that it call out every X minutes your **lane average**, the **gaps with rivals** or the **average needed to climb** a position.

**Screen always on.** While the panel is open, the screen **doesn't turn off**; after **30 seconds without touching it, it dims** (to not waste battery or bother you), but **the voice keeps calling out**. Touch the screen to light it up again.

> Tip: log in with the PIN, enable the **Voice**, leave the phone in the box and listen. It's the way to stay informed without taking your eyes off the track.

**Native app (alternative).** If the team would rather install an app than use the web, there's also the **native PitWall Lap app** (iOS/Android): the same timing and voice, but no PIN — it discovers the server on its own on the local network — plus extras like **live tyre strategy**, **Pole**, **History** and **Training**. It's covered in detail in the *Usage manual*, section *PitWall Lap*.

> **You can now log in from the pole itself**, no need to wait for it to finish and for lanes to be handed out: as soon as the race is confirmed, your team already exists (with its PIN) and your panel tells you if it's your turn now, with a live timer for your attempt and the voice calling out every lap. Once the pole ends, the panel switches on its own to showing your result (position and time) — see *Live pole*.

## 5. Live pole

![img: 46-pole-results.png]

If the race has a **pole** (the qualifying lap that decides the starting order), you can follow it live even if you're not the one running it.

- From the **guest home**, while a pole is under way a **card** appears that takes you straight to its board.
- You can also get there from **Live stats**.

It's a **read-only** view: there are no start, stop or next-driver buttons, just what's happening: **who's on track right now**, the **starting order** still to run and the **provisional classification** (fastest to slowest) as times are recorded. It updates on its own, without reloading.

> If your team is competing in the endurance race that follows the pole, as soon as the race is confirmed you already have your **PitWall Lap panel** active — you can follow your own pole attempt right there, voice included (see *PitWall Lap: your race on the phone*).

## 6. Consistency

![img: 26-livestats-cons-con.png]

The most important card for improving. **Consistency measures your lap-to-lap regularity**: whether you always do the same time or whether you jump around.

**What the % is.** It's 100 minus your relative variation (the CV, coefficient of variation). 100% would be a perfect robot, always identical. The higher, the more regular. In real data the normal range is **between 90% and 99%**. It's the same formula TicTac uses, calculated over your pace laps (discarding one-off incidents).

**The ±SD in seconds (more useful than the %).** Next to the % you'll see something like *±0.13 s*. It's your standard deviation: **how many seconds, up or down, you swing from one lap to the next.** Pay more attention to this than to the %: a ±0.13 s tells you directly how tight you run, and it discriminates better between two drivers who at first glance have a similar %. **Goal: reduce your ±SD.**

**Color levels.** The system classifies you by your variation:

- **Excellent** — variation below 1.5%. Clockwork running.
- **Good** — between 1.5% and 2.5%. Solid.
- **Irregular** — between 2.5% and 4%. You jump around, there's time to gain by being finer.
- **Erratic** — above 4%. A lot of instability; focus on finishing clean laps before attacking.

**Toggle: Without exits / With exits.**

- **Without exits** — your **pure pace**. Removes exits, pits and incidents. It answers: *when I run well, am I consistent?* Use it to polish your driving.
- **With exits** — the **real regularity of your stint**. It includes EVERYTHING: exits, pits, traffic. It answers: *for real, as it was, what pace did I deliver?* Use it to see the real impact of your mistakes. It usually comes out worse than "Without exits", and that difference is exactly what the incidents cost you.

**Minimum laps.** You need at least **3 valid laps** (which, removing the start crossing, are about 4 times across the line) for the number to be reliable. With fewer you'll see a dash (—) until you build up mileage.

---

## 7. The charts

Each chart has three modes. They change according to what you want to see.

**Lap time.** The classic: each point is a lap and its time. You read the shape of your race. Do you drop off as you warm up? Do you fade at the end because of the car or because of you? An isolated spike (an exit) or a trend? It serves to see where you gain and where you lose throughout the stint.

**Around the average.**

![img: 24-livestats-chart-media.png]

Here each lap is drawn as a difference from your average: above = slower lap, below = faster. It's the best view for **consistency**: the flatter and closer to zero your line is, the more regular you are. The spikes upward are your bad laps. Visual goal: flatten the line.

**Lap gap.**

![img: 25-livestats-chart-gaplaps.png]

Your distance to the leader over time (X axis = minutes of the heat; Y axis = the gap to the leader you choose). Up = you lose ground; down = you close in. It serves to see AT WHICH MOMENT of the heat you won or lost the race, and whether the gap is stable or slipping away from you.

---

## 8. Projection and gaps

![img: 22-livestats-proyectada.png]

**Projected position vs heat position.** They're different things and both matter:

- **Heat** — where you are in the heat you're running now. Useful for your direct duel on track.
- **Projected** — where you'll finish the race adding up all the heats. It's your REAL position in the overall. The projection estimates your total laps by dividing the total race time by your average. **Lowering your average = better projection.**

Important: the projected position is **the same everywhere** (live card, Overall Classification and Lap panel). If you see P2 in one place, you see P2 everywhere. There aren't two truths.

**The provisional estimate (the asterisk \*).** If you see an **orange asterisk** next to an estimate, it means that figure **hasn't settled yet**: that team is in its **first heat** and hasn't gone past **60 %** of it, so PitWall doesn't have a solid reference for its pace from the start. The number can still move. As soon as the heat crosses that point, the asterisk disappears and the reference is locked in. You'll see it in the **Le Mans classification** and in the **live stats**; hover over it and the explanation appears.

**The distance carries the fraction (and is also given in seconds).** The gap to the leader is **not** rounded to whole laps: it includes the **fraction** of a lap you've already covered. That's why the label no longer reads *"+3 vlts."* but something like **"a 2,8 v (35,5\")"** — 2.8 laps behind, worth 35.5 seconds:

- **2,8 v** is the real distance in laps, decimal included.
- **35,5"** is what it would cost you to make it up **at your own pace** (those 2.8 laps × your average). It's the same number TicTac calls out.

Where the fraction comes from: **with the heat running** it's the **live** fraction —what you've covered since your last time across the line—, so the distance moves with you within the lap; **with the heat finished, or if you're resting**, it's the fraction you had **as the flag fell**. Before this, when the flag fell you lost all trace of who was further ahead on the road, and two cars 2.8 laps apart looked exactly like two cars 3.0 apart.

**Types of gap.**

- **Gap to leader** — how far you are from the first.
- **Gap by laps** — the distance expressed in laps, **with its fraction** ("I'm 2.8 laps down", not "3").
- **Gap in seconds** — that same distance turned into time using **your** average. That's what you have to claw back.
- **Gap by minute** — how the distance evolves with time, to see if you're closing in or dropping off.

When two drivers have the same laps, the **fraction** breaks the tie: the fraction of a lap you'd completed just as the flag fell. Running right to the end can give you that extra fraction that moves you up a position. And if you're level on the fraction too, the accumulated **total time** decides.

## 9. The Results view (after the race)

When the race ends, **Results** is where everything is analyzed calmly. It has several **tabs**; each one answers a different question. At the top you always see the **fastest lap of the race** (who and on which lane).

### Comparison (the grid by lane)

![img: st-comparativa.png]

It's the main table. One row per participant and, for **each lane** they went through, five stacked data points:
- **Fastest** — your best lap on that lane. The blue dot + **BEST** marks the fastest lap *of that lane* among everyone.
- **Average** — your average pace on that lane.
- **Const. w/o** — your **consistency** (without exits) on that lane, in %.
- **Exits** — how many times you went off there (and, below, the time lost).
- **Pit-stops** — stops on that lane (with the lap number, e.g. *L355*).

It serves to see **which lanes you perform better or worse on**, not just your global number. The blue rectangle marks your **starting lane**.

**Passes / repeat-lane races.** If the same lane is run several times, each lane is **split by occurrence** (`1/2`, `2/2`…), to compare your 1st pass with the 2nd on the same spot.

![img: st-ocurrencia.png]

### Progression (lap by lap)

![img: st-progresion.png]

Every lap of the race, in order. You can **choose who to compare** with, filter by **heat** or by **lane**, and show/hide **exits** (red dots) and **pit-stops** (orange). With the Δ Delta vs average (“Δ Delta vs media”) button each lap is drawn as a difference from your average (better view to judge your regularity: the flatter, the better). It answers: *did I drop off as I warmed up? did I fade at the end? was it an isolated spike or a trend?*

### Positions

![img: st-posiciones.png]

One line per participant; the vertical axis is the **position** (P1 at the top). If your line goes up, you lose positions; if it goes down, you gain. It serves to see **at which moment** of the race your result was decided.

### Gap to leader

![img: st-gap.png]

Your distance to the leader **over time** (you can restrict the range of heats). The line going down = you close in; going up = you drop away. It answers: *in which heat did I drop off or recover?*

### Gap (grid)

![img: st-gapgrid.png]

The same idea but in a **table**: rows = teams, columns = heats, and each cell the **laps of disadvantage** at the close of that heat (0 = leader). The **gold border** warns that there was a **pit-stop** in that heat. You can pick 2–4 teams to see the gap **between them** (not just against the leader).

### Advanced statistics

![img: st-avanzadas.png]

The deep analysis of a participant: **total laps** (and clean ones), **best**, **average** (with *with/without exits* toggle), **Δ consistency**, **exits · pit-stops** and **time lost**. Below, the **evolution by lane** (your average track by track, to see where you were faster) and one card per lane. With **Compare with** you pick a rival and a **head-to-head** table is generated with the differences colored (green = better, red = worse).

### Le Mans classification (teams)

![img: st-lemans.png]

In team races there's also the **Le Mans classification**: the overall in large, with **projected laps**, total, **gap** to the leader, average, best and **P/Climb** (the pace you'd need to catch the one ahead). Ideal for long races.

The **gap** in this table reads **"a 2,8 v (35,5\")"**: the distance in laps **with its fraction** and, in brackets, what it would cost to make it up at your pace. And if an estimate carries an **orange asterisk**, that figure is still **provisional** (first heat, not yet past 60 %).

> **Icons and colors you'll see:** blue dot + **BEST** = fastest lap of that lane · blue rectangle = starting lane · **gold border** = there was a pit-stop in that heat · trend **▲/▼** = you went up/down compared to the previous heat.

## 10. Glossary

- **Consistency** — your lap-to-lap regularity. 100 minus your relative variation. Higher = more consistent.
- **±SD (standard deviation) / CV** — the ±SD is the seconds you swing from lap to lap (look at this number). The CV is that swing as a percentage relative to your pace; the consistency % is 100 − CV.
- **Average** — a simple average of your lap times, without the start crossing (your first complete lap **does** go in). Includes exits and pits. It's the one the projection uses, and it matches TicTac to the millisecond.
- **Clean average** — your average counting only normal laps (without exits). Used for the Δ and to detect incidents, not to project.
- **Start crossing (warmup / partial crossing)** — the first time you cross the line in the heat: from the grid to the line, starting from a standstill. It's half the layout, not a lap, so it doesn't count for average, best or consistency. **Only that one**: the first complete lap that comes after counts for everything.
- **Sub-minimum** — a time below the race's minimum lap. An impossible ghost crossing; always discarded.
- **Exit** — you've gone off the track. Counts for the average (it's real time lost) but not for your best lap.
- **Pit-stop** — a stop in the pits. Counts as time, not as best lap.
- **Fraction** — the fraction of a lap you've covered: while running, what you've done since your last time across the line; at the end, the one you had as the flag fell. It counts in the distance to the leader and breaks the tie when two of you have the same laps.
- **Projection** — an estimate of your final result by adding up all the heats: total race time divided by your average, plus the fraction you've already covered.
- **Provisional estimate (\*)** — the orange asterisk next to an estimate: the team is in its first heat and hasn't gone past 60 % of it, so its reference isn't locked in and the number can still move.
- **Gap** — your distance to another car (or to the leader), in laps **with the fraction**, in seconds (those laps × your average) or per minute. It reads *"a 2,8 v (35,5\")"*.
- **PitWall Lap** — your team's mobile web page (PIN access): your projected position, your pace cards and the voice that calls out the laps. Only in team races.
- **Live pole** — a read-only board for following the pole's qualifying lap: who's on track, the starting order and the provisional classification. Reachable from the guest home (while a pole is under way) or from Live stats.
- **Occurrence** — each time you run the same lane in passes/repeat-lane races (`1/2`, `2/2`…); it lets you compare one pass with another.
- **P/Climb** — in the Le Mans classification, the pace (average per lap) you'd need to catch the team ahead.
- **Starting lane** — the lane you started from; in the results grid it's marked with a blue box.

---

**In one sentence:** look at your **projected position** to know where you finish, lower your **average** to climb, and flatten your **consistency** (reduce the ±SD) to stop gifting time lap after lap.
