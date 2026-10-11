---
lang: en
title: PitWall Lap manual
descr: Manual for PitWall Lap, the slot racer's app: hear your lap times, a race calendar with reminders, practice sessions, competition practice and offline results.
kicker: App manual · For the driver
h1: Your slot assistant,<br>in your <span class="ac">pocket</span>.
lede: Guide to <b>PitWall Lap</b>, the driver's app: it connects to the track's timing system to <b>speak your lap times</b>, even with the screen locked, and keeps your <b>race calendar</b>, your <b>practice sessions</b> and your <b>results</b> on your phone.
---

## intro | Introduction

PitWall Lap is the **driver's** app. It has six areas, which appear in the main menu when you open it:

- **Lap**: connects to the track's timing system and speaks your times.
- **Calendar**: your races, with reminders on your phone.
- **Practice**: the practice runs you have recorded.
- **Competition practice**: the ones saved by the server, which you can download to view offline.
- **Results**: finished races and your own files (Excel, PDF or photos).
- **Settings**: language, tire strategy and voice alerts.

![shot: lap-01-menu.png | PitWall Lap · Main menu | PitWall Lap main menu | Main menu: Lap on top, the four areas in a grid and Settings below.]

The app works with **PitWall Manager** (the track server), with the old **TicTac** timer (InfoLap) and with the **new TicTac**. It comes in **8 languages**: Spanish, Catalan, Basque, English, Italian, French, Portuguese and Dutch; when you open it, it picks your phone's language.

> tip: It is an app for **iPhone** (installed through TestFlight) and for **Android** (APK, downloaded from pitwall.es and **updated from inside the app**). Your phone must be on the **same WiFi network** as the server or the timer; without that network, Calendar, Practice, downloaded Competition practice and Results keep working, but Lap has nothing to listen to.

## permisos | Phone permissions

The app only asks for permissions when it needs them:

- **Local network** (iPhone): to find the track's server or timer on the WiFi. If you refuse, iOS silently drops the searches and **Lap will find nothing** even though everything is fine; fix it in *iPhone Settings → PitWall Lap → Local Network*.
- **Notifications**: the first time you save a race with reminders. Without them the race is saved, but no reminder will sound.
- **Camera** and **Photos**: only if you add a photo to *Results*.

## lap | Lap: hearing your times

![shot: lap-02-fuentes.png | PitWall Lap · Lap | Choosing between PitWall and TicTac | Lap: two cards, PitWall (red) and TicTac, and the Back button.]

Open **Lap** and choose the time source:

- **PitWall**: the track server (PitWall Manager).
- **TicTac**: the TicTac Slot timer, with no server behind it.

The app **finds the source by itself** on the network within a few seconds. If it doesn't, it lets you type the **IP by hand** once and remembers it for next time. Competition practice and Results also use that remembered address to talk to the server.

### Choosing an activity (PitWall)

![shot: lap-03-actividad.png | PitWall Lap · Choose an activity | List of active races and practice | Choose an activity: active and pending races, and the practice session if there is one.]

If the server has several races, or a race and practice at the same time, it lets you **choose**. If there is only one thing, it goes straight in.

- **Refresh**: the button at the top right (or pulling the list down) asks the server again without leaving the screen. Use it if the director has just set up the race or the practice. From «No activity» or an error, if a single activity shows up after refreshing, it goes straight into it.
- Then you pick your **heat group** and your **name or team**, and you land on your race screen.

### Your race screen

![shot: lap-04-mi-turno.png | PitWall Lap · My turn | Race screen | My turn: the last lap in large type, colored by how fast it is, your position and the gaps.]

It is designed to be **glanced at**: the last lap in large type, in **purple** if it is your best, in **green** if you are within 2 % of it and in **amber** if you are slower, with the difference below; your position and the gaps to the rival ahead and the one behind. If the director **pauses**, **stops (STOP)** or ends the heat, the app shows it and tells you by voice.

The **voice** speaks every lap, position changes, half-time, the last minute and the last 30 seconds, and, if you switch them on, every few minutes your lane average, your race average, the gaps and the «average to move up». All of that is set in *Settings* (see below) and can be changed on the fly in *Voice & settings*, folded below your screen.

The **tire strategy** (endurance races) recommends when to change and, if the race uses the server's tire control, shows the available sets and the last change. It can be switched off in *Settings*.

### Free practice and competition practice

If **Practice** appears in «Choose an activity», a practice session is running:

- **Free practice**: you pick your **lane** and the app follows that lane.
- **Competition practice**: teams **rotate lanes in every heat**, so you pick your **team or driver** (the list shows the lane each one is on now, or **Resting**) and the app **follows you wherever you go**. When each heat starts the voice tells you *«Your turn, lane N»*; if you rest that heat, the screen shows it and you hear nothing from the others.

![shot: lap-05-competicion-selector.png | PitWall Lap · Competition practice | Choosing a team or driver | Competition practice: you choose who to follow; each one shows their current lane or Resting.]

> warn: Following by team in competition practice needs **PitWall Manager 1.56.1** or later. With an older server the app doesn't offer competition practice or stays stuck on one lane.

With **Practice GO** (on your screen, in practice mode) the app records your laps as a run of your own; when you stop, it saves it in *Practice*.

## calendario | Race calendar

![shot: lap-06-calendario.png | PitWall Lap · Calendar | Upcoming and past races | Calendar: upcoming races (with a bell if they have reminders) and past ones.]

The calendar keeps **your races on your phone** and **reminds you** with notifications, with no server and no connection needed. It shows the **upcoming** ones (nearest first) and the **past** ones. Tap a race to edit or delete it.

### Adding a race by hand

![shot: lap-07-evento.png | PitWall Lap · New race | Race form | New race: name, date and time, place, notes and reminders.]

Tap **＋ Add race** and fill in **name**, **date** and **time** (required), and optionally **place** and **notes**. Under **Remind me** tick the reminders you want:

- at start time;
- 30 minutes before;
- 1 hour before;
- 1 day before;
- 1 week before.

A new race reminds you **1 day and 1 hour before** by default. Only reminders that haven't passed yet are scheduled. The first time, your phone will ask for notification permission.

### Importing many races from Excel

If you have the season's calendar in a spreadsheet, you don't have to type every race.

1. Tap **Download template**. The app creates an Excel file in your language and opens the share menu: save it to *Files*, email it to yourself or AirDrop it.
2. Open it in Excel, Numbers or another program and fill in **one race per row** on the *Races* sheet. **Delete the two example rows**. The *Instructions* sheet sums up the rules.
3. Save it as **.xlsx** and go back to the app: **Import from Excel** and pick the file.
4. The app shows a **preview** before saving anything: the races that will be imported, the ones already there and the rows with errors. Confirm with **Import**.

![shot: lap-08-importar.png | PitWall Lap · Import from Excel | Import preview | Preview: what will be imported, what was already there and which rows have errors.]

The template's columns are:

- **Name** (required): the race's name.
- **Date** (required): `dd/mm/yyyy`; `yyyy-mm-dd` or an Excel date also work.
- **Time** (required): `hh:mm`. If the Excel date already includes a time, that is used.
- **Place** (optional): the circuit or venue.
- **Notes** (optional): anything you want to remember.
- **Reminders** (optional): separated by commas, from `hora`, `30min`, `1h`, `1d` and `1sem`. Empty = `1d, 1h`.

Good to know:

- The **headers** can be in any of the 8 languages, in a different order or under another common name (*Race*, *Circuit*, *Date*…), and there can be title rows above them.
- A row with an error **doesn't stop** the others from being imported; the preview gives the **row** and the reason (name missing, invalid date, invalid time).
- If a race is already in the calendar (**same name and same moment**), it is **skipped**, so you can import the same file again without duplicating anything.
- A reminder the app doesn't understand is ignored, and it tells you.
- It works with Excel (**.xlsx** or **.xls**). If you export from another program, save as Excel.

> tip: Adding a race by hand is still available, and you can mix both: import the season and add one-off races afterwards.

## entrenamientos | Practice

![shot: lap-09-entrenamientos.png | PitWall Lap · Practice | List of practice runs | Practice: your practice runs, with laps, best and average.]

Here are the **practice runs you recorded** with *Practice GO*. Open one to see its **chart** (laps and moving average) and note the car's details (model, motor, tire, rim, crown and pinion). With **Compare** you pick 2 to 4 runs and see them **overlaid** on one chart, with their consistency. Everything is saved **on your phone**.

## competicion | Competition practice

![shot: lap-10-competicion-lista.png | PitWall Lap · Competition practice | Downloaded and server sessions | Competition practice: the downloaded ones («on this phone») and the ones still only on the server.]

When a competition practice ends, **PitWall Manager saves it**. This area lets you **download it to your phone** to look at whenever you want, also **offline**.

- The list combines the ones you already have (**✓ on this phone**) and the server's (**⬇ Download**). Tap one from the server and it downloads and opens. With several pending, **Download all** appears.
- Each row shows the date, heats, participants, laps and best lap.
- The session that is **running right now** doesn't appear until it is closed.
- With the server off or out of the WiFi you only see the downloaded ones. To list the server's, you need to have gone into *Lap → PitWall* at least once so the app remembers its address.

![shot: lap-11-competicion-detalle.png | PitWall Lap · Competition practice | Standings and heats | Detail: the session standings and, heat by heat, what each lane did.]

The **detail** has the session **standings** (whoever adds up the most laps across all their heats wins; ties go to the best lap) and, **heat by heat**, each lane's laps, best and average with its participant. **Remove from phone** deletes the local copy; the session stays on the server.

> warn: To download practice sessions you need **PitWall Manager 1.56.0** or later.

## resultados | Results

![shot: lap-12-resultados.png | PitWall Lap · Results | Races and your own files | Results: PitWall races and your own files, together and by date.]

*Results* puts together, by date, two kinds of things:

- **Races finished in PitWall**: the app saves the results dossier when the race ends, so you can see it offline. If the server responds, the ones you didn't follow live also appear (marked **☁ on server**). Inside each you have the standings and the **comparison Excel** to open or share.
- **Your files**: tap **＋ Add** and choose **File (Excel or PDF)**, **Photo from library** or **Take a photo**. Use it to keep the standings of another club's race, a paper time sheet or a PDF of the rules.

![shot: lap-13-archivo.png | PitWall Lap · Results file | Detail of your own file | One of your files: rename it, open or share it, and delete it. Photos are shown on screen.]

Each file of yours is **copied into the app**, so it stays even if you delete the original. You can **rename** it, **open or share** it (Excel and PDF open in the app you choose; photos are shown directly) and **delete** it.

## ajustes | Settings

![shot: lap-14-ajustes.png | PitWall Lap · Settings | Settings screen | Settings: language, tire strategy and voice alerts.]

From the **Settings** button in the menu you configure:

- **App language**: automatic (your phone's) or one of the 8. It also changes the **voice** that speaks your times and the phrases it says. Basque has no system voice on iPhone and uses the Spanish one.
- **Tire strategy**: switch it on or off. When off, it isn't calculated and its entry disappears from Lap.
- **Voice**: the master switch and the **alerts**: laps, position changes, half-time, last minute and last 30 seconds, and the **periodic alerts** (lane average, race average, gaps and «average to move up»). A periodic alert repeats every **N minutes**: tap its button to cycle through off, 1, 2, 3 and 5 minutes.
- **App** (Android only): the installed version and the **Check for updates** button.

What you set here is **what every session starts with**. During the race you can keep changing the alerts from Lap, in *Voice & settings*.

> tip: With the **old TicTac** the app only speaks laps; the other alerts need PitWall Manager or the new TicTac.

## actualizar | Updating the app

- **iPhone**: versions arrive through **TestFlight**. Open the TestFlight app and tap *Update*; if you turned on automatic updates, they install by themselves. Each TestFlight build **expires after 90 days**, so it is worth updating before then.
- **Android**: when you open the app (and when you return to it after 6 hours), if **pitwall.es** has a newer version than yours, the menu shows a **«A new version is available»** card with an **Update** button. Tapping it, the app **downloads the APK** and opens Android's installer. The first time, Android will ask you to **allow PitWall Lap to install apps**; grant it and tap *Update* again. **Later** hides the notice until the next time you open the app. You can also check any time in *Settings → App → Check for updates*.

> tip: The update installs **on top of** the app, without losing your calendar, practice runs or results. If there is no network or the website doesn't respond, the app simply doesn't notify you. The first version with this notice has to be installed by hand once; from then on it updates itself.

## problemas | If something doesn't work

- **Lap can't find the server.** Check that your phone and the server are on the **same WiFi** and, on iPhone, that the **Local Network** permission is on. If it still doesn't show up, enter the IP by hand.
- **«No activity».** The server has no race set up or practice running. When the director sets it up, tap **Refresh**.
- **Competition practice doesn't show up.** Check that PitWall Manager is **1.56.1** or later and that the practice is set up (running or on standby between heats).
- **Calendar reminders don't sound.** In your phone's settings, check that *PitWall Lap* has **Notifications** permission. Reminders whose moment has already passed are not scheduled.
- **The import says it can't read the file.** Use an **Excel (.xlsx)** file, for example the template, with the **Name** and **Date** columns.
- **The voice doesn't sound with the screen locked.** Check that the volume and the silent switch are not off; the app speaks anyway with the phone on silent.
- **It doesn't update on Android.** Check that you have an internet connection and that you have allowed PitWall Lap to install apps; you can also download the APK by hand from the PitWall Lap page on pitwall.es.
- **What's new** (at the bottom of the menu) shows the app's version history; it is in Spanish only.
