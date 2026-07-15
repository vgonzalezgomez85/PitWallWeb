# Manual de uso — PitWall (organización / dirección de carrera)

Guía para quien **opera** PitWall: montar la carrera, dirigirla en vivo, corregir vueltas y sacar resultados.

---

## 1. Introducción
![img: 01-home.png]

**PitWall** es el sistema de cronometraje y gestión de carreras de slot. Detecta el paso de cada coche por la línea de meta a través del hardware de cronometraje, con dos opciones compatibles:

- **DS-300** — por **puerto serie**. Puedes unir **hasta 6 circuitos** DS-300 en una sola carrera: cada caja cronometra sus carriles y PitWall los combina. Cada caja va por **su propio puerto** (una caja = un puerto).
- **DS-300 agrupador** — cuando un **aparato agrupador** junta **varias cajas DS-300 (de 2 a 4) en un solo puerto COM**. PitWall separa las cajas por su identificador de trama y numera los carriles de corrido (caja 1 → 1–8, caja 2 → 9–16, y así hasta **32 carriles** con 4 cajas). Una **única señal de salida** arranca todas las cajas a la vez.
- **BART (Policar)** — por **Bluetooth**. Admite **hasta el máximo de carriles que permita BART** (actualmente **32**).

Puedes usar cualquiera de estas fuentes; para PitWall el flujo de cruces es equivalente.

- Desde la **pantalla de inicio** accedes a **Carreras**, **Ajustes** y el resto de módulos.
- Abajo a la derecha siempre ves el **estado del enlace** (verde = conectado; "Sin señal" = revisa el cable/puerto o el Bluetooth).

**El listado de carreras** te muestra todas tus carreras con su estado (pendiente / activa / terminada) y el botón **+ Nueva carrera**.

![img: 02-races-list.png]

## 2. Escenarios, categorías y catálogos (tu biblioteca)

Para no reconfigurar lo mismo en cada carrera, PitWall guarda **plantillas reutilizables** que después eliges al crear una carrera.

**Escenarios (circuitos guardados).** Un **escenario** es una pista física guardada: nº de circuitos y carriles (p.ej. `8+8+8 = 24`), su **secuencia de carriles** (rotación) y el **tiempo mínimo por defecto**. Cualquier carrera asignada a ese escenario hereda todo automáticamente.

![img: op-escenarios.png]

Al editar un escenario defines su nombre, la configuración de carriles, arrastras la **secuencia de rotación** (con **descansos DSC** si sobran pilotos), el **tiempo mínimo por defecto** y, opcionalmente, **vueltas mínimas por categoría** (un Pt distinto para GT, Turismo, Clásicos… en esa misma pista).

![img: op-escenario-form.png]

**Categorías.** Grupos de nivel/clase (GT, Turismo, Clásicos…) que sirven para **sobrescribir el tiempo mínimo (Pt) por categoría** en cada escenario y para clasificar coches y pilotos.

![img: op-categorias.png]

**Catálogos reutilizables (pilotos, equipos, coches).** Mantén tu **base de datos** de participantes y material para reutilizarla entre carreras:
- **Pilotos** — nombre y categoría; cada piloto puede tener su **QR** de identificación.
- **Equipos** — nombre, color, país, coche y miembros.
- **Coches** — marca, modelo y categoría.

Todos se pueden **importar en bloque desde CSV** (botones **Plantilla CSV** e **Importar CSV**, con vista previa de novedades vs. duplicados) y exportar.

![img: op-catalogo-pilotos.png]

![img: op-qr-pilotos.png]

> Con **Exportar QR** imprimes las tarjetas QR de todos los pilotos (para el cambio de piloto por escaneo en resistencia — ver *Control de turnos*).

## 3. Crear una carrera
![img: 03-wizard-step1.png]

Pulsa **+ Nueva carrera** y sigue el asistente:

- **Tipo**:
  - *Sprint* → una **carrera rápida**, de **pilotos o equipos**.
  - *Resistencia* → una **carrera de resistencia** (por equipos), que añade el **control de cuánto ha corrido cada piloto** del equipo (ver *Control de turnos de piloto*).
- **Carriles y circuitos**: nº total de carriles y cómo se reparten entre cajas (p.ej. 8+8+6 = 3 cajas DS-300).
- **Tiempo mínimo de vuelta (Pt)**: por debajo de este tiempo, un cruce se considera **fantasma** (rebote/doble lectura) y no cuenta.
- **Pasadas**: cuántas veces se recorre la **secuencia de carriles entera**. 2 pasadas = la rotación completa se corre 2 veces (el doble de mangas).
- **Repetir carril**: cada carril se corre este nº de **mangas seguidas** (mismo carril), sumando las vueltas — para comparar cada repetición.
- **Pole** (opcional) y **reglas de piloto** (solo campeonato: min/max por piloto, bloqueo de cambio al final de manga).

> **Pasadas** y **repetir carril** solo cambian cómo se generan las mangas; los totales se suman por participante.

> ¿Gestionas el campeonato con **PitWall Control**? No hace falta que teclees los equipos y la rotación otra vez: puedes **importar la prueba** entera desde Control (ver *Importar una tanda de PitWall Control*).

## 4. Importar una tanda de PitWall Control
![img: op-import-tanda.png]

Si organizas el campeonato con **PitWall Control** (el gestor de temporada), puedes montar allí la prueba —equipos, copas, carriles y rotación— y pasársela a PitWall **sin volver a teclear nada**. PitWall **autocrea la carrera** a partir de lo que recibe.

Entra en **Carreras → Importar tanda**. Hay **dos formas** de traer la prueba:

- **Fichero JSON.** En Control pulsas **Exportar tanda (JSON)** y guardas el archivo; en PitWall lo **subes** en la pantalla de import.
- **Por red (WiFi/LAN).** En Control pulsas **Enviar a PitWall**: Control **descubre** tu PitWall en la red local (o le indicas la **IP** a mano) y pide un **PIN de emparejamiento**. Ese PIN es el que muestra la pantalla **Importar tanda** de PitWall — tecléalo en Control para autorizar el envío.

**Qué crea PitWall.** Cada **manga** de la prueba de Control se convierte en una **tanda**, con cada equipo colocado en su **carril de salida**. Los **descansos** (`D1`, `D2`…) se colocan y rotan como en cualquier rotación (ver *Tandas, participantes y rotación*).

**Con pole.** Si la prueba tiene pole (interruptor **La carrera tiene pole** en Control; al exportar a fichero te lo pregunta), Control **no envía el orden de carril**. En la pantalla de import de PitWall marca **Esta carrera tiene pole**: PitWall crea la carrera con la **sesión de pole** (todos los equipos) y la parrilla se decide **después de correr la pole** (ver *Pole*).

> Justo después de importar puedes **editar la carrera** para asignarle el **escenario** de tu club (y heredar sus carriles, secuencia y tiempo mínimo) — ver *Editar carrera, tandas y mangas*.

> **Requisito:** para el envío por red, PitWall y PitWall Control deben estar en la **misma red** LAN/WiFi. El PIN de emparejamiento se ve en **Importar tanda** de PitWall. La otra mitad del puente —**traer los resultados** de vuelta a Control— se explica en el *Manual de PitWall Control*.

## 5. Tandas, participantes y rotación
![img: 34-tanda.png]

Una **tanda** agrupa a los participantes y su **rotación de carriles** por manga. Al añadir los **equipos/pilotos**, PitWall genera automáticamente todas las **mangas**.

**Cómo funciona la rotación.** Cada participante va cambiando de carril manga a manga siguiendo la secuencia configurada (p.ej. `1, 3, 5, 6, 4, 2`). Así todos pasan por todos los carriles y las condiciones se igualan.

- *Ejemplo (6 carriles, 6 pilotos):* en la manga 1 el piloto A corre el carril 1; en la manga 2, el 3; en la 3, el 5… hasta completar la vuelta a todos los carriles.

**Rotación a tu gusto.** PitWall propone una rotación equilibrada automáticamente, pero **puedes gestionarla como quieras**: reordena la **secuencia de carriles** a mano (arrastrando) para decidir exactamente por qué carril pasa cada participante en cada manga.

**Descansos.** Si hay **más participantes que carriles**, la secuencia incluye huecos (`0` / `DSC`) que son **descansos**: en esa manga ese participante no corre. PitWall los reparte de forma equilibrada, pero **también puedes colocarlos donde quieras** dentro de la rotación (arrástralos a la posición que prefieras).

**Con pasadas / repetir carril:**
- *2 pasadas* → la secuencia entera se repite: `1,3,5,6,4,2, 1,3,5,6,4,2`.
- *Repetir carril 2* → cada carril, dos mangas seguidas: `1,1,3,3,5,5,6,6,4,4,2,2`.

## 6. Editar carrera, tandas y mangas

Después de crear una carrera puedes retocarla:
- **Editar carrera** — cambiar el **nombre** y, **mientras no haya vueltas registradas**, el **escenario**. Puedes **asignar** un escenario a una carrera que no lo tenía, **cambiarlo** por otro o **quitarlo**. Al **asignar** un escenario, la carrera hereda sus **carriles**, su **secuencia** de rotación y su **tiempo mínimo** (y las vueltas mínimas por **categoría**, si las tiene), y PitWall **regenera las tandas pendientes** con esa configuración; al **quitarlo**, la carrera pasa a **modo manual** conservando la configuración que tenía. Si ya hay vueltas, el escenario queda **bloqueado** (para no romper los datos).

![img: op-edit-carrera.png]

> Caso típico: **importas una tanda de PitWall Control** (que llega en modo manual) y luego la **editas para asignarle el escenario** de tu club, de modo que herede carriles, secuencia y tiempo mínimo de tu pista.

- **Editar tanda** — cambiar los **nombres** de los participantes y, si la tanda aún no ha empezado, su composición. Si ya tiene mangas iniciadas, entra en **modo solo renombrar** (no se añaden ni quitan participantes, para no descuadrar la rotación).

![img: op-edit-tanda.png]

- **Editar manga** — cambiar **quién corre en cada carril** en una manga concreta, sin regenerar toda la tanda (útil si un equipo no se presenta o hay un cambio de última hora).

## 7. Pole (clasificación previa)
![img: 44-pole-setup.png]

La **pole** es una vuelta clasificatoria **antes** de la carrera para decidir el orden de salida. Es opcional; se activa al crear la carrera (**Pole**) y se lanza desde la página de la carrera → **Configurar Pole Position**.

- **Participantes**: aparecen todos los inscritos. El **orden de la lista** es el orden en que saldrán a hacer su vuelta; púlsalo con **🎲 Aleatorio** para barajarlo.
- **Carril de pole**: **todos** hacen su vuelta clasificatoria por el **mismo carril** (para que sea comparable). Elígelo con **−/+** o con **🎲 Aleatorio**.
- Pulsa **Empezar Pole**: cada participante entra por turnos, da su vuelta y PitWall registra su mejor tiempo. En el cronometraje puedes activar **Omitir 1er cruce (out-lap)** para no contar la vuelta de lanzamiento.

**Resultados de la pole.** Al terminar aparece **Resultados Pole** con la **clasificación final** (del más rápido al más lento, con el gap al líder y la **vuelta rápida**). Desde aquí puedes **✏️ Editar tiempos** si hubo un error, o seguir con **🚦 Asignar carriles de salida**.

![img: 46-pole-results.png]

**Asignar carriles después de la pole.** La pole no reparte carriles automáticamente: abre la pantalla **Elección de carril**, donde cada participante **elige** su carril **en orden de clasificación** — el **poleman** (el más rápido) elige primero, luego el 2º, y así sucesivamente. Es el clásico "el más rápido elige carril".

![img: 47-pole-lanes.png]

- El banner **Eligiendo ahora** indica a quién le toca; a la izquierda ves el **orden de elección** (la clasificación) y a la derecha los **carriles disponibles** (con su color).
- Cada uno pulsa el carril que quiere; ese carril desaparece de los disponibles y el turno pasa al siguiente.
- **Si hay más participantes que carriles**, aparecen huecos de **💤 Descanso**: quien elija descanso **no corre la manga 1** y **entra en la rotación desde la manga 2**.
- Cuando todos han elegido, pulsa **🏁 Crear Primera Tanda**: PitWall crea la tanda y genera todas las mangas con esa parrilla como punto de partida (el orden de elección define la posición inicial en la rotación de carriles). A partir de ahí, la carrera rota los carriles manga a manga como siempre (ver *Tandas y rotación*).

> La pole no puntúa en la carrera: solo decide **quién elige carril primero** y, con ello, la parrilla de salida de la primera manga.

## 8. PitWall Lap — PIN para los equipos
![img: 43-lap-pins.png]

**PitWall Lap** es la vista móvil para que cada **equipo/piloto** siga su propio cronometraje desde el teléfono (sus vueltas, cantadas por voz, y su posición). Para que entren solo a *su* panel se reparte un **PIN** por equipo.

- Entra en **PitWall Lap · PINs** de la carrera. Verás la dirección que los equipos abren en el móvil (p.ej. `http://<IP-del-servidor>:3000/lap/<id>`) y la tabla **EQUIPO → PIN**.
- Da a cada equipo **su PIN**. Al abrir la dirección e introducirlo, entran directamente a su panel.
- **Nuevo** regenera el PIN de un equipo (por si se filtró o quieren cambiarlo).

> Los móviles deben estar en la **misma red** que el ordenador que hace de servidor. Usa la IP del equipo, no `localhost`, cuando lo abran desde el teléfono. Si quieres que los equipos sigan la carrera **desde fuera del local** (por internet), mira *Seguimiento público por internet*.

## 9. Dirigir la carrera en vivo
![img: 20-live-timing.png]

Desde la página de la carrera:

1. **Armar la manga** (▶). Queda preparada esperando el **GO** de la caja.
2. **GO**: al dar la salida en la caja, aparece el **semáforo** y arranca el cronómetro. Cada circuito lleva su propio reloj (C1/C2/C3).
3. Durante la manga ves por carril: **total de vueltas**, **última**, **media**, **mejor**, y arriba el banner de **vuelta rápida**.
4. **Pausa / Reanudar / Parar** la manga cuando haga falta.
5. Al terminar (bandera o fin de tiempo), la manga se cierra y se prepara la **siguiente**.
6. Al acabar todas las mangas de una tanda, arranca la **siguiente tanda**.

**Elegir la vista.** Con el botón **Vista** cambias el layout según los carriles: *Filas horizontales* (pocos carriles), *Cuadrícula compacta* (muchos) o *Tarjetas con detalles* (con vueltas/salidas/pit/Δ por tarjeta).

**Cambiar de tanda, repetir una manga y finalizar.** Desde el propio directo tienes atajos sin salir de la pantalla:
- **Siguiente tanda** — cuando acaban las mangas de una tanda, pasa directamente a la siguiente.
- **Repetir manga** — si una manga se dio por mala (falsa salida, incidencia), la vuelves a lanzar con los mismos participantes y carriles.
- **Finalizar carrera** — cierra la carrera (la "bandera"): se congela la clasificación y se genera el resumen para resultados y para los móviles (PitWall Lap).

> Aviso **"Sin señal del DS-300"**: mientras esté, las vueltas **no se registran**. Revisa la conexión antes de dar el GO.

## 10. Control de turnos de piloto (campeonatos)

En carreras de **campeonato por equipos** puedes obligar reglas de reparto de volante entre los pilotos de un equipo. Se definen al crear la carrera:
- **Tiempo mínimo / máximo por piloto** — cada piloto debe rodar al menos X y como mucho Y.
- **Bloqueo tras un cambio** — un mínimo de tiempo sin volver a cambiar de piloto.
- **Máximo de turnos por piloto**.

Los **cambios de piloto** se registran escaneando el **QR del piloto** (o metiendo su código) al entrar a pista. Desde el directo abres **Control de turnos**, que muestra el **piloto actual por carril**, el **tiempo acumulado** de cada uno (avisando si incumple una regla) y el **histórico de turnos**; si un cambio se registró mal, puedes **corregir el tiempo** del turno.

## 11. Vuelta a vuelta y correcciones (añadir / quitar vueltas)
![img: 30-correcciones.png]

Desde la carrera (botón de **corrección de vueltas** en el directo o en resultados) entras al **vuelta a vuelta** de cada manga. Sirve para arreglar lecturas mal registradas.

- **Izquierda**: los carriles de la manga; elige el equipo/piloto a revisar.
- **Derecha**: su lista de vueltas — **VLT** (nº), **TIEMPO**, **RELOJ** (momento de carrera) y **Δ ANT.** (diferencia con la vuelta anterior).
- **Acciones por vuelta**:
  - **Transferir** (↔) — pasar la vuelta a **otro carril/equipo** (si el sistema la asignó mal).
  - **Fantasma** — marcar la vuelta como no válida (no cuenta) sin borrarla; se puede **restaurar**.
  - **Borrar** (🗑) — eliminar una vuelta.
  - **Añadir vuelta manual** — si faltó un cruce, la añades a mano.

> Úsalo con criterio: las correcciones cambian totales, medias y clasificación de esa manga.

## 12. Resultados y exports
![img: 10-results-comparativa.png]

Al terminar (o en cualquier momento) entra en **Resultados**:

- **Comparativa** (parrilla): por participante, cada carril con **Rápida / Media / Consistencia / Salidas / Pit-stops**. En carreras de **pasadas/repetir-carril**, cada carril se desglosa en sus **ocurrencias** (1/2, 2/2) para comparar.
- **Progresión / Posiciones / Gap al líder / Gap (rejilla) / Estadísticas avanzadas**: distintas vistas de análisis (se explican en detalle en el *Manual de estadísticas*).
- **Exports**: **Excel**, **Puntos (xlsx/csv)**, **Control (csv)**, **Exportar para GitHub**, **PDF**.

**Resultados públicos.** Hay una página abierta —**Resultados**, en el menú de inicio— donde cualquiera puede consultar (sin tocar nada ni poder editar) los resultados de las carreras **finalizadas**. Es la que compartes con pilotos y público para que miren la clasificación y las estadísticas de la carrera.

![img: op-resultados-publicos.png]

## 13. Entrenamiento
![img: 40-training.png]

Además de las carreras, PitWall tiene un modo **Entrenamiento** (desde la pantalla de inicio) para rodar sin montar una competición completa. Hay dos modalidades:

- **Entrenamiento libre**: registra **vueltas por carril sin estructura de equipos**. Ideal para sesiones abiertas donde cada uno prueba coche y pista; no hay rotación ni clasificación, solo tiempos por carril.
- **De competición**: equipos o pilotos asignados a carriles con **rotación automática tras cada tanda**, como una carrera pero pensado para entrenar el formato de campeonato.

Elige la modalidad, asigna los carriles y pulsa **Empezar**. El cronometraje en directo funciona igual que en carrera (GO de la caja, vueltas, mejor/media por carril).

## 14. Ajustes
![img: 04-settings.png]

- **Fuente de datos**: elige de dónde llegan los cruces — **Simulación**, **DS-300** (una caja por puerto, con su nº de carriles), **DS-300 agrupador** (varias cajas por un solo puerto COM: indica **puerto**, **baud** —57600, 8N1— y **nº de cajas** 2/3/4 → 16/24/32 carriles) o **BART** por Bluetooth. Con el agrupador los carriles se numeran de corrido (caja 1 → 1–8, caja 2 → 9–16…) y una sola señal de salida arranca todas las cajas.
- **Circuitos**: define pistas guardadas (secuencia de carriles, tiempo mínimo).
- **Seguimiento público por internet**: publica las vistas públicas en internet para seguir la carrera desde fuera del local (ver la sección siguiente).
- **Licencia** e idioma (ES/EN).

**Historial de versiones.** En el **pie de todas las páginas** ves el número de **versión** de PitWall. Al pulsarlo se abre el **Historial de versiones** (`/changelog`), con lo **Añadido**, **Mejorado** y **Corregido** en cada actualización. La versión **sube con cada actualización**, así siempre sabes qué PitWall tienes y qué ha cambiado.

## 15. Seguimiento público por internet
![img: op-seguimiento-publico.png]

Por defecto las vistas de PitWall (el **directo**, los **Resultados** y **PitWall Lap**) solo se ven en la **red local**. Con el **Seguimiento público por internet** cada club puede **publicarlas en internet** para que pilotos y público sigan la carrera **desde fuera del local**, sin abrir puertos ni montar una VPN: PitWall levanta un **túnel Cloudflare propio** del club.

Está en **Ajustes → Seguimiento público por internet**. Hay **dos modos**:

- **Rápido.** PitWall genera una **URL temporal** (`*.trycloudflare.com`) al vuelo: **sin cuenta ni dominio**. Es la opción para una tarde suelta; ten en cuenta que la URL **cambia en cada arranque**.
- **Cloudflare propio.** Usas el **token del túnel** del club y **tu propio dominio**, con lo que la **URL es fija** y de marca. La propia pantalla trae una **guía paso a paso**, con enlaces al panel **Zero Trust** de Cloudflare y a la documentación oficial, para crear el túnel y pegar su token.

**Controles.** Botones **Arrancar** / **Parar** con el **estado** y la **URL en vivo** (para copiarla y compartirla). **Arrancar** aplica lo que tengas en pantalla en ese momento. Puedes activar el **autoarranque** para que el túnel se levante solo al abrir PitWall.

**Instalar cloudflared.** El túnel lo levanta la herramienta `cloudflared`. Si no está instalada, aparece el botón **Instalar cloudflared**, que **descarga la versión oficial** a la carpeta de datos de PitWall — **sin pedir permisos de administrador**.

> **Seguridad.** Desde fuera **solo se ven las vistas públicas** (directo, resultados y PitWall Lap). El **control de la app** (crear, dirigir o editar carreras) **queda bloqueado**: nadie de fuera puede tocar la carrera.

## 16. Glosario (operación)
- **Carrera**: el evento completo. Se compone de tandas.
- **Tanda**: grupo de participantes con su rotación; se compone de mangas.
- **Manga**: una tirada cronometrada (todos los carriles a la vez) de una duración.
- **Rotación**: cómo cambian de carril los participantes de una manga a otra.
- **Descanso**: manga en la que un participante no corre (hueco `0` en la secuencia).
- **Pasada**: recorrido completo de la secuencia de carriles; N pasadas = N× mangas.
- **Repetir carril**: correr cada carril N mangas seguidas, sumando vueltas.
- **GO**: la señal de salida (de la caja DS-300) que arranca la manga.
- **Vuelta fantasma**: vuelta marcada como no válida (no cuenta), restaurable.
- **Pole**: sesión de clasificación previa (opcional); todos ruedan por el mismo carril y su mejor vuelta fija la parrilla de salida.
- **Entrenamiento libre**: modo para registrar vueltas por carril sin equipos ni rotación (sesión abierta).
- **PitWall Lap**: vista móvil por equipo/piloto (sus vueltas cantadas y su posición).
- **PIN**: código por equipo para entrar a su panel en PitWall Lap.
- **Pt (tiempo mínimo)**: umbral por debajo del cual una vuelta se considera cruce fantasma y no cuenta.
- **Escenario**: pista guardada (circuitos, carriles, secuencia y tiempo mínimo) reutilizable en varias carreras.
- **Categoría**: clase de coche/piloto (GT, Turismo, Clásicos…); permite un Pt distinto por categoría.
- **Catálogo**: biblioteca reutilizable de pilotos, equipos y coches (importable por CSV).
- **QR de piloto**: código que identifica al piloto para registrar su turno al escanearlo.
- **Turno (shift)**: periodo que un piloto está al volante dentro de su equipo en resistencia.
- **DS-300**: la caja de cronometraje que detecta el paso por meta.
- **Importar tanda**: traer una prueba montada en PitWall Control (por JSON o por red LAN + PIN) para que PitWall autocree la carrera.
- **PitWall Control**: la app de gestión de campeonatos que monta la prueba y recibe los resultados de PitWall.
- **Seguimiento público por internet**: publicar las vistas públicas (directo, resultados, Lap) en internet con un túnel Cloudflare propio del club.
- **Túnel Cloudflare**: conexión que expone en internet las vistas públicas de PitWall sin abrir puertos (modo Rápido con URL temporal, o Cloudflare propio con dominio fijo).
- **Historial de versiones**: la página (`/changelog`) que abre el número de versión del pie, con lo añadido, mejorado y corregido en cada actualización.
