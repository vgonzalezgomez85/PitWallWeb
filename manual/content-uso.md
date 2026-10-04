# Manual de uso — PitWall (organización / dirección de carrera)

Guía para quien **opera** PitWall: montar la carrera, dirigirla en vivo, corregir vueltas y sacar resultados.

---

## 1. Introducción
![img: 01-home.png]

**PitWall** es el sistema de cronometraje y gestión de carreras de slot. Detecta el paso de cada coche por la línea de meta a través del hardware de cronometraje, con dos opciones compatibles:

- **DS-300** — por **puerto serie**. Puedes unir **hasta 6 circuitos** DS-300 en una sola carrera: cada caja cronometra sus carriles y PitWall los combina. Cada caja va por **su propio puerto** (una caja = un puerto).
- **DS-300 agrupador** — cuando un **aparato agrupador** junta **varias cajas DS-300 (de 2 a 4) en un solo puerto COM**. PitWall separa las cajas por su identificador de trama y numera los carriles de corrido (caja 1 → 1–8, caja 2 → 9–16, y así hasta **32 carriles** con 4 cajas). Una **única señal de salida** arranca todas las cajas a la vez.
- **BART (Policar)** — por **Bluetooth**. Admite **hasta el máximo de carriles que permita BART** (actualmente **32**). Con más de 8 carriles hacen falta **varios Master BART independientes** (p. ej. `BART_TRACK1`, `BART_TRACK2`…), uno por cada bloque de carriles: PitWall se conecta a cada uno por separado y numera los carriles de corrido, igual que con el agrupador DS-300.

Puedes usar cualquiera de estas fuentes; para PitWall el flujo de cruces es equivalente.

- La **pantalla de inicio** tiene un **menú lateral** con todas las secciones, agrupadas en **Competición** (Carreras, Entrenamientos, Estadísticas en vivo, Resultados, Lap, Control de pilotos, Control de neumáticos…), **Catálogo** (Pilotos, Equipos, Coches, Categorías y Escenarios, con cuántos tienes de cada) y **Sistema** (Ajustes, Base de datos, Sincronizar catálogo, Conexión ecosistema, Solución de problemas…). En la cabecera ves el estado de la fuente de datos (simulación, DS-300 conectado o sin conexión).
- Si hay una **carrera en curso**, arriba aparece su franja: **manga X de Y**, tanda, el **tiempo que queda** de la manga, las mangas hechas y —cuando ya está calculado— el **líder estimado**, con botones a **Directo de la manga**, **Pantalla TV**, **Estadísticas en vivo**, **Control de pilotos** (en campeonato), **Neumáticos** (si la carrera tiene juegos), **Registro de sucesos** y **Gestionar carrera**. Sin carrera en curso, la franja muestra la pole que esté en marcha o los atajos **Nueva carrera** / **Entreno libre**.
- Debajo tienes cuatro **accesos rápidos** (Nueva carrera, Entrenamientos, Resultados, Lap) y las **últimas carreras** con su acción directa (Directo, Resultados o Abrir).
- Cada sección se abre en **su propia ventana**: si la vuelves a pulsar, PitWall trae al frente la ventana que ya tenías abierta, sin recargarla. Así puedes tener a la vez el directo, la TV y las estadísticas. Con el interruptor **«Ventana nueva / Esta ventana»** del pie del menú eliges si prefieres abrirlo todo en la misma ventana, y en la cabecera una píldora te dice cuántas **ventanas** tienes abiertas.
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
- **Equipos** — nombre, color, país (con su bandera; junto a las banderas de país estándar hay banderas propias dibujadas para Catalunya y Euskadi), categoría (coloreada igual que en el directo), coche y miembros.
- **Coches** — marca, modelo y categoría.

Todos se pueden **importar en bloque desde CSV** (botones **Plantilla CSV** e **Importar CSV**, con vista previa de novedades vs. duplicados) y exportar.

![img: op-catalogo-pilotos.png]

![img: op-qr-pilotos.png]

![img: op-catalogo-equipos.png]

> Con **Exportar QR** imprimes las tarjetas QR de todos los pilotos (para el cambio de piloto por escaneo en resistencia — ver *Control de turnos*). El catálogo de equipos tiene su propio **Exportar QR**, que reparte esas mismas tarjetas **agrupadas por equipo** (nombre y categoría de cabecera), marcando "sin pilotos" los equipos vacíos y "⚠ sin perfil" a quien todavía no tiene piloto del club vinculado.

![img: op-qr-equipos.png]

> **Sincronizar catálogo con carreras pendientes.** Si cambias los **pilotos** o el **país** de un equipo en el catálogo *después* de crear una carrera, esos cambios no llegan solos a la carrera ya montada. Con **Sistema → Sincronizar catálogo** (menú lateral del inicio) —o el atajo **«Actualizar desde catálogo»** del menú **⋯** de la ficha de carrera, que solo aparece si la carrera es candidata— los vuelcas a todas las carreras que **aún no han arrancado ninguna manga**, sin pasar por «Editar tanda». PitWall empareja los equipos **por nombre**, deja la plantilla de cada carrera **idéntica al catálogo** (añade y quita pilotos hasta que coinciden — un "espejo exacto") y actualiza el país; antes de aplicar te muestra un **resumen de los cambios**, con una casilla por carrera. No toca la parrilla ni añade o elimina equipos, y solo actúa sobre carreras **en formato equipos**. La **categoría** no se sincroniza: siempre se lee en vivo del catálogo.

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

> **Conexión ecosistema.** Todo el puente con PitWall Control por red —enviar tandas y traer resultados— se puede **permitir o bloquear** de golpe desde **Sistema → Conexión ecosistema**, en el menú lateral del inicio. Viene **activado** de fábrica; si lo apagas, cualquier PitWall Control de la red queda rechazado (aunque el PIN sea correcto) hasta que lo vuelvas a activar. Ahí mismo puedes consultar también el PIN de emparejamiento.

## 5. Tandas, participantes y rotación
![img: 34-tanda.png]

Una **tanda** agrupa a los participantes y su **rotación de carriles** por manga. Al añadir los **equipos/pilotos**, PitWall genera automáticamente todas las **mangas**.

**Cómo funciona la rotación.** Cada participante va cambiando de carril manga a manga siguiendo la secuencia configurada (p.ej. `1, 3, 5, 6, 4, 2`). Así todos pasan por todos los carriles y las condiciones se igualan.

- *Ejemplo (6 carriles, 6 pilotos):* en la manga 1 el piloto A corre el carril 1; en la manga 2, el 3; en la 3, el 5… hasta completar la vuelta a todos los carriles.

**Rotación a tu gusto.** PitWall propone una rotación equilibrada automáticamente, pero **puedes gestionarla como quieras**: reordena la **secuencia de carriles** a mano (arrastrando) para decidir exactamente por qué carril pasa cada participante en cada manga.

**Descansos.** Si hay **más participantes que carriles**, la secuencia incluye huecos (`0` / `DSC`) que son **descansos**: en esa manga ese participante no corre. PitWall los reparte de forma equilibrada, pero **también puedes colocarlos donde quieras** dentro de la rotación (arrástralos a la posición que prefieras).

**Carriles vacíos (menos participantes que carriles).** No hace falta llenar todos los carriles: puedes crear una tanda con **menos participantes que carriles** (basta con **uno**). Los carriles que sobran quedan libres, **sin coche fantasma** que aparezca en vueltas ni clasificación. Al crear la tanda eliges qué hacer con ellos:
- **Sobran los últimos** (por defecto): los carriles de **mayor número** quedan vacíos toda la carrera; nadie rueda por ellos.
- **El hueco rota**: el carril (o carriles) libre va **rotando manga a manga**, de modo que todos los participantes acaban pasando por los mismos carriles y la pista queda igual de justa que con la rejilla completa.

**Con pasadas / repetir carril:**
- *2 pasadas* → la secuencia entera se repite: `1,3,5,6,4,2, 1,3,5,6,4,2`.
- *Repetir carril 2* → cada carril, dos mangas seguidas: `1,1,3,3,5,5,6,6,4,4,2,2`.

## 6. Editar carrera, tandas y mangas

Después de crear una carrera puedes retocarla:
- **Editar carrera** — cambiar el **nombre** y, **mientras no haya vueltas registradas**, el **escenario**. Puedes **asignar** un escenario a una carrera que no lo tenía, **cambiarlo** por otro o **quitarlo**. Al **asignar** un escenario, la carrera hereda sus **carriles**, su **secuencia** de rotación y su **tiempo mínimo** (y las vueltas mínimas por **categoría**, si las tiene), y PitWall **regenera las tandas pendientes** con esa configuración; al **quitarlo**, la carrera pasa a **modo manual** conservando la configuración que tenía. Si ya hay vueltas, el escenario queda **bloqueado** (para no romper los datos).

![img: op-edit-carrera.png]

> Caso típico: **importas una tanda de PitWall Control** (que llega en modo manual) y luego la **editas para asignarle el escenario** de tu club, de modo que herede carriles, secuencia y tiempo mínimo de tu pista.

- **Reglas de resistencia (turnos y neumáticos)** — en una carrera de **resistencia**, y **mientras no se haya corrido ninguna manga**, Editar carrera te deja ajustar también las **reglas de turnos por piloto** (mínimo y máximo por piloto, máximo de turnos y bloqueo del final de manga) y los **neumáticos por equipo** (la dotación con la que arranca el control de neumáticos) — los mismos campos que fijaste en el asistente al crear la carrera. Así puedes corregir un número sin rehacer la carrera. En cuanto rueda la **primera manga**, esos campos se **bloquean** (atenuados y con un candado 🔒) para no descuadrar lo ya corrido; el **nombre** y el **escenario** siguen sus reglas de siempre. Si pones un **máximo por piloto menor que el mínimo**, PitWall te avisa.

- **Editar tanda** — cambiar los **nombres** de los participantes y, si la tanda aún no ha empezado, su composición. Si ya tiene mangas iniciadas, entra en **modo solo renombrar** (no se añaden ni quitan participantes, para no descuadrar la rotación).

![img: op-edit-tanda.png]

> Si solo quieres llevar a la carrera los cambios de **pilotos o país** hechos en el catálogo de equipos y la carrera **aún no ha arrancado**, no hace falta tocar «Editar tanda»: usa **Sistema → Sincronizar catálogo** (ver *Escenarios, categorías y catálogos*). Para una carrera que ya ha rodado alguna manga, «Editar tanda» en **modo solo renombrar** es la única vía.

- **Editar manga** — cambiar **quién corre en cada carril** en una manga concreta, sin regenerar toda la tanda (útil si un equipo no se presenta o hay un cambio de última hora).

## 7. Pole (clasificación previa)
![img: 44-pole-setup.png]

La **pole** es una vuelta clasificatoria **antes** de la carrera para decidir el orden de salida. Es opcional; se activa al crear la carrera (**Pole**) y se lanza desde la página de la carrera → **Configurar Pole Position**.

- **Participantes**: aparecen todos los inscritos en una **cuadrícula numerada** (1, 2, 3…) que se ajusta sola al ancho de la pantalla y rellena por columnas —coincidiendo con los grupos de circuito C1/C2/C3—. Ese orden es el orden en que saldrán a hacer su vuelta; puedes **arrastrar** cualquier participante a mano para cambiarlo, o pulsar **🎲 Aleatorio** para barajarlo entero.
- **Carril de pole**: **todos** hacen su vuelta clasificatoria por el **mismo carril** (para que sea comparable). Elígelo con **−/+** o con **🎲 Aleatorio**.
- **Cambio automático de piloto**: interruptor junto a **Omitir 1er cruce**. Con la casilla activa, al terminar el intento de un piloto el botón **Siguiente piloto** hace una cuenta atrás de 3 segundos y avanza solo, sin esperar el clic manual. Es una preferencia del puesto de control (se guarda en el propio navegador), no de la carrera.
- Pulsa **Empezar Pole**: cada participante entra por turnos, da su vuelta y PitWall registra su mejor tiempo. En el cronometraje puedes activar **Omitir 1er cruce (out-lap)** para no contar la vuelta de lanzamiento.
- **No se presenta**: si al participante de turno no se le ve por pista, el botón **No se presenta** lo salta. La primera vez lo manda al **final de la cola** —tendrá otra oportunidad cuando le vuelva a tocar—; si se le vuelve a saltar sin haber llegado a correr entre medias, queda marcado **Ausente** de verdad. Los ausentes no compiten por la pole con un 0.00 como si fuera la vuelta más rápida: aparecen aparte, en su propio bloque, tanto en la clasificación en vivo como en los resultados finales.

**Resultados de la pole.** Al terminar aparece **Resultados Pole** con la **clasificación final** (del más rápido al más lento, con el gap al líder y la **vuelta rápida**). Desde aquí puedes **✏️ Editar tiempos** si hubo un error, o seguir con **🚦 Asignar carriles de salida**.

![img: 46-pole-results.png]

**Asignar carriles después de la pole.** La pole no reparte carriles automáticamente: abre la pantalla **Elección de carril**, donde cada participante **elige** su carril **en orden de clasificación** — el **poleman** (el más rápido) elige primero, luego el 2º, y así sucesivamente. Es el clásico "el más rápido elige carril".

![img: 47-pole-lanes.png]

- El banner **Eligiendo ahora** indica a quién le toca; a la izquierda ves el **orden de elección** (la clasificación) y a la derecha los **carriles disponibles** (con su color).
- Cada uno pulsa el carril que quiere; ese carril desaparece de los disponibles y el turno pasa al siguiente.
- **Si hay más participantes que carriles**, aparecen huecos de **💤 Descanso**: quien elija descanso **no corre la manga 1** y **entra en la rotación desde la manga 2**.
- Cuando todos han elegido, pulsa **🏁 Crear Primera Tanda**: PitWall crea la tanda y genera todas las mangas con esa parrilla como punto de partida (el orden de elección define la posición inicial en la rotación de carriles). A partir de ahí, la carrera rota los carriles manga a manga como siempre (ver *Tandas y rotación*).

> La pole no puntúa en la carrera: solo decide **quién elige carril primero** y, con ello, la parrilla de salida de la primera manga.

**Los invitados pueden seguir la pole en directo.** El tablero de cronometraje de la pole —antes solo visible para quien la operaba— es accesible sin restricción de IP desde **Estadísticas en vivo**, y aparece una tarjeta nueva en la home de invitado mientras hay una pole en marcha. Es de **solo lectura**: se ocultan los controles (iniciar/parar/siguiente piloto) y se ve en tiempo real quién está en pista, el orden de salida y la clasificación provisional.

## 8. PitWall Lap — para los equipos
![img: 43-lap-pins.png]

Los equipos pueden seguir su carrera desde el móvil de **dos formas**, no excluyentes: la **vista web con PIN** (sin instalar nada, de solo lectura) o la **app nativa PitWall Lap** (se instala en el móvil, con voz y estrategia de neumáticos en vivo).

**Ya funciona durante la propia pole, no solo tras terminarla.** Los equipos (con su PIN) se crean al confirmar el asistente de la carrera, en vez de esperar a asignar los carriles al final de la pole. Así, cada equipo ve en su panel si le toca ahora, un cronómetro en vivo de su intento, sus vueltas y su mejor tiempo, con la voz cantando cada vuelta igual que en carrera; al terminar la pole, el panel pasa solo a mostrar su resultado (posición y tiempo).

**Vista web con PIN.**
- Entra en **PitWall Lap · PINs** de la carrera. Verás la dirección que los equipos abren en el móvil (p.ej. `http://<IP-del-servidor>:3000/lap/<id>`) y la tabla **EQUIPO → PIN**.
- Da a cada equipo **su PIN**. Al abrir la dirección e introducirlo, entran directamente a su panel: posición proyectada, gap al líder, vueltas, media y pit-stops, con voz incluida — de solo lectura, y solo para carreras de **resistencia** (el detalle completo está en el *Manual de estadísticas*, apartado *PitWall Lap: tu carrera en el móvil*).
- **Nuevo** regenera el PIN de un equipo (por si se filtró o quieren cambiarlo).
- **PIN de acceso — Activado / Desactivado.** En la misma hoja de PINs, un interruptor permite **quitar el PIN** de esta carrera. Con el PIN **desactivado**, cada equipo entra a su panel de timing **solo eligiéndose en la lista**, sin teclear nada (útil en eventos internos donde el PIN estorba). Los PINs **se conservan** por si lo vuelves a activar. Es un ajuste **por carrera** y viaja también al cronómetro esclavo BART al sincronizar la carrera (Race Link).
- **Seguimiento de rivales.** En su panel, cada equipo puede seguir **hasta 5 rivales** y comparar carril a carril vueltas, vuelta rápida y medias (solo de mangas terminadas). La lista se guarda por equipo, así que la comparten todos los móviles del box. Detalle en el *Manual de estadísticas*, apartado *PitWall Lap*.

> Los móviles deben estar en la **misma red** que el ordenador que hace de servidor. Usa la IP del equipo, no `localhost`, cuando lo abran desde el teléfono. Si quieres que los equipos sigan la carrera **desde fuera del local** (por internet), mira *Seguimiento público por internet*.

**App nativa PitWall Lap (iOS/Android).** Es la vía completa: el piloto instala la app en su móvil y, al abrirla, elige la fuente (**PitWall** o el cronómetro **TicTac Slot** en solitario, sin servidor detrás) y **descubre el servidor sola** en la red local en unos segundos — sin URL ni PIN que repartir. Si el auto-descubrimiento falla, se introduce la IP a mano una vez y la app la recuerda para la próxima. Si el servidor tiene varias carreras o tandas activas, deja elegir; después el piloto elige su **nombre/equipo** de la lista para entrar a su panel.

Comparte con la vista web el cronometraje en vivo y la voz (vueltas, cambios de posición, medio-manga, avisos de tiempo y, en modo avanzado, medias/gaps/"media para subir" cada N minutos), y además ofrece:

- **Estrategia de neumáticos en vivo** (carreras de resistencia, con piloto seleccionado): recomienda cuándo cambiar —por degradación real de ritmo, o de forma **pautada** por vueltas/juegos restantes cuando la goma no pierde ritmo—, con consejo por posición y modelado de la goma de los rivales de delante y detrás. Si la carrera lleva el **control de neumáticos del servidor** (ver *Control de neumáticos de resistencia*) y el equipo casa por nombre, la dotación y los cambios los manda **PitWall Manager**: la app los muestra en vivo (juegos disponibles y último cambio) sin botones manuales. Sin control del servidor, el piloto lleva la cuenta a mano (juegos, cambios obligatorios, coste de parada) y confirma él mismo con **Cambié gomas**.
- **Pole**: pantalla propia para seguir tu vuelta de clasificación, el gap a la pole y la clasificación final, si la carrera la tiene.
- **Historial y Entrenamiento**: carreras pasadas (aunque no las siguieras en directo) y un modo de entrenamiento libre que graba tus tandas de rodaje (vueltas, mejor, media) en el propio móvil, con gráfica y comparación entre ellas.

> La app no usa PIN: cualquiera en la **misma red local** que descubra el servidor puede elegir cualquier equipo de la lista. Para acceso controlado o desde fuera de la pista, usa la vista web con PIN — la app siempre necesita red local, aunque publiques el túnel de *Seguimiento público por internet*.

## 9. Dirigir la carrera en vivo
![img: 20-live-timing.png]

Desde la página de la carrera:

1. **Armar la manga** (▶). Queda preparada esperando el **GO** de la caja.
2. **GO**: al dar la salida en la caja, aparece el **semáforo** y arranca el cronómetro. Cada circuito lleva su propio reloj (C1/C2/C3).
3. Durante la manga ves por carril: **total de vueltas**, **última**, **media**, **mejor**, y arriba el banner de **vuelta rápida**.
4. **Pausa / Reanudar / Parar** la manga cuando haga falta.
5. Al terminar (bandera o fin de tiempo), la manga se cierra y se prepara la **siguiente**.
6. Al acabar todas las mangas de una tanda, arranca la **siguiente tanda**.

**La ficha de la carrera es accesible con una manga en marcha.** Entrar en una carrera que tiene una manga en curso ya no te lleva directo al directo: ves su **ficha** (estado, clasificación proyectada, tandas…) con un enlace **«Manga N»** para saltar al directo cuando quieras. Al **dar el GO** desde la ficha, la pantalla sí salta sola al directo, y sigue sin poderse arrancar una segunda manga mientras otra corre.

**Elegir la vista.** Con el botón **Vista** eliges entre dos vistas: *Filas horizontales* (una fila por carril) o *Tarjetas con detalles* (una tarjeta por carril, legible de lejos). La antigua *Cuadrícula compacta* ya no existe: si la tenías elegida, se abren las tarjetas.

**Las tarjetas.** La **última vuelta** va en grande con el **total de vueltas** al lado y, debajo, mejor vuelta, media, Gap V y vueltas de la manga; las cifras se ajustan solas al tamaño de la tarjeta, haya 6, 24 o 40 equipos. La última vuelta sale en **morado con «RÉCORD CARRERA»** si es la vuelta rápida de la carrera y en **azul con «BOXES»** si fue una parada. Cada tarjeta muestra el **piloto al volante** con una **barra del tiempo que lleva conducido** frente al máximo por piloto (**ámbar** desde el 85 %, **roja** si lo pasa); si un carril no ha fichado, verás **«SIN PILOTO»** mientras corre la manga. También avisa de salidas, **paradas en boxes** («PIT 2») y **juegos de neumáticos** usados sobre el total («4/12»).

**Filas a dos columnas.** Si los equipos no caben en una columna, la vista de filas se reparte en **dos columnas**, cada una con su cabecera, para verlos **a todos a la vez** (hasta 40 en una pantalla de 1080p). En carreras con control de pilotos, cada fila lleva el **piloto debajo del equipo**.

**Orden del directo.** En **Ajustes → Preferencias → Orden del directo** eliges cómo se ordenan tarjetas y filas: por **clasificación estimada** (recomendado) o por **vueltas reales** (a igualdad, menos tiempo total). Con vueltas reales no se muestra el Gap V. La clasificación estimada del panel lateral no cambia.

**Clasificación estimada al lado.** En las dos vistas, el botón con icono de **panel lateral** (junto a **Vista**) abre o cierra la **clasificación estimada acoplada a la derecha** de las filas, como en TicTac: **#**, participante, **V. Proy.** (vueltas estimadas), **Total** (vueltas reales) y **Media**. PitWall recuerda si la dejaste abierta en cada carrera. De entrada el panel usa el **ancho automático** (el justo para leer los nombres enteros, como mucho el 40 % de la pantalla) y ajusta la letra para que quepan todos; si no caben, pasa de página cada 20 s. **Arrastrando su borde** eliges tú el ancho (si sobra sitio aparecen también **Gap V** y la tendencia) y con **doble clic en el borde** vuelve al automático. Las filas adaptan su letra al espacio que queda: el nombre del piloto tiene prioridad y, en ventanas muy estrechas, se ocultan primero Gap V, luego VLT y luego ÚLTIMA. En la vista de tarjetas, con el panel abierto las tarjetas quitan mejor vuelta, media y Gap V (ya están en la clasificación) y mantienen las vueltas de la manga bajo el total.

![img: 20b-live-panel-estimada.png]

**Pantallas fijas de sala o TV.** Añadiendo parámetros a la dirección del directo, esa pantalla arranca siempre igual sin tocar lo guardado: `?side=standings` (panel abierto) o `?side=none` (cerrado), y `?view=1` o `?view=3` (*Filas horizontales* o *Tarjetas con detalles*; un enlace antiguo con `?view=2` abre también las tarjetas). Se pueden combinar: `?view=1&side=standings`.

**Distancia al líder y estimada provisional.** En las pantallas de clasificación (**Le Mans** y **estadísticas en vivo**) la distancia al líder se da **con la coma** y su equivalente **en segundos** —*"a 2,8 v (35,5\")"*—, no redondeada a vueltas enteras. Y si una estimada lleva un **asterisco naranja**, es que ese equipo sigue en su **primera manga** sin haber pasado del **60 %**: su referencia aún no está fijada y la cifra puede moverse. Todo esto se explica en detalle en el *Manual de estadísticas*.

**Cambiar de tanda, repetir una manga y finalizar.** Desde el propio directo tienes atajos sin salir de la pantalla:
- **Siguiente tanda** — cuando acaban las mangas de una tanda, pasa directamente a la siguiente.
- **Repetir manga** — si una manga se dio por mala (falsa salida, incidencia), la vuelves a lanzar con los mismos participantes y carriles.
- **Finalizar carrera** — cierra la carrera (la "bandera"): se congela la clasificación y se genera el resumen para resultados y para los móviles (PitWall Lap).

> Aviso **"Sin señal del DS-300"**: mientras esté, las vueltas **no se registran**. Revisa la conexión antes de dar el GO.

## 10. Sucesos de carrera

La página **🗒️ Sucesos** —accesible desde la ficha de la carrera y con un botón en la cabecera del directo— muestra, manga a manga, todo lo que va pasando durante la sesión en un formato fácil de leer: **GO** (también cuando se da en varias cajas por separado, circuito a circuito), **pausa y reanudado** por circuito, **fin de manga**, **cancelación**, **recuperación tras un corte**, **vueltas fantasma/ignoradas** y su **reasignación** al carril correcto, **salidas retroactivas** y los **fichajes de piloto** (QR, cambio en caliente o corrección manual).

Las mangas se muestran **compactadas por defecto** —solo la que está en marcha aparece abierta— y se despliegan con un clic en su cabecera. Un checkbox permite **ocultar los fichajes de piloto rutinarios** previos al GO cuando solo interesa el resto de sucesos.

> Con la manga en marcha, la página va **sumando los sucesos nuevos según ocurren**, sin recargar. Es la forma de reconstruir, después de una carrera, qué pasó y cuándo, sin tirar de memoria.

## 11. Control de turnos de piloto (campeonatos)

En carreras de **campeonato por equipos** puedes obligar reglas de reparto de volante entre los pilotos de un equipo. Se definen al crear la carrera:
- **Tiempo mínimo / máximo por piloto** — cada piloto debe rodar al menos X y como mucho Y.
- **Bloqueo tras un cambio** — un mínimo de tiempo sin volver a cambiar de piloto.
- **Máximo de turnos por piloto**.

Los **cambios de piloto** se registran escaneando el **QR del piloto** (o metiendo su código) al entrar a pista. Desde el directo abres **Control de turnos**, que muestra el **piloto actual por carril**, el **tiempo acumulado** de cada uno (avisando si incumple una regla) y el **histórico de turnos**; si un cambio se registró mal, puedes **corregir el tiempo** del turno.

> **La cámara del escáner en móviles y tablets (HTTPS local).** El escáner de QR usa la cámara, y el navegador solo la permite en **localhost** (el ordenador del operador) o por **HTTPS**. Un móvil o tablet que entra por la IP de la red (192.168.x.x) verá la cámara bloqueada, con el aviso *«La cámara necesita HTTPS o localhost»*. Para escanear desde esos dispositivos, activa **Ajustes → HTTPS local (cámara del escáner QR)**: PitWall abre un puerto seguro aparte (por defecto **3443**) sin tocar nada del funcionamiento normal, y hay que **reiniciar** el servidor una vez. Después, abre el control de pilotos por el enlace **`https://IP:3443/control/shifts`** (los tienes listos en esa misma sección de Ajustes).

> **El aviso de seguridad y cómo quitarlo.** La primera vez que un dispositivo abre el enlace `https://`, el navegador avisa una vez (**«conexión no privada → continuar»**); al aceptar, la cámara ya funciona. Si quieres que ese aviso no salga, **instala la CA de PitWall** en el dispositivo: en Ajustes tienes **Descargar CA** y la página **`/cert`** con la guía paso a paso para **iPhone/iPad, Android y Windows**. Instalar la CA una vez basta aunque cambie la IP de la red: PitWall reemite solo el certificado del servidor y el dispositivo sigue confiando.

## 12. Control de neumáticos de resistencia

En una carrera de **resistencia** puedes llevar la cuenta de los **juegos de neumáticos** que gasta cada equipo. La dotación —los juegos con los que **todos** parten— se fija al crear la carrera (asistente, paso 1, campo **«Neumáticos por equipo»**). Con **0** el control queda apagado y todo funciona como siempre.

Se abre de **dos formas**:
- Desde la carrera, con el botón **🛞 Neumáticos** (solo aparece en resistencia y con dotación mayor que 0).
- Como **kiosco** en `/control/tires` (en el menú de inicio: **Competición → Control de neumáticos**), que **detecta solo** la carrera de resistencia que esté en marcha —igual que el kiosco de turnos—. Es lo ideal para dejar abierto en una tablet junto al box.

La pantalla es una **rejilla con todos los equipos**. Cada casilla muestra el nombre del equipo y dos números: **Disponibles** y **Usados**.

- **Un clic en la casilla = entregar un juego**: baja uno los disponibles, sube uno los usados y queda **anotado en qué manga y en qué minuto:segundo de carrera** se hizo el cambio (se sella con la manga en marcha y su reloj; si en ese momento no hay ninguna corriendo, se guarda sin tiempo).
- El **lápiz** de cada casilla abre el **historial** de ese equipo, donde puedes **borrar** un registro (el juego vuelve a Disponibles), **editar** su manga y su tiempo (mm:ss) o **añadir uno a mano** (manga, tiempo y una nota).

Los contadores **no se guardan a pelo**: se **calculan** a partir de los registros (dotación menos entregas), así que deshacer nunca deja descuadres. Si un equipo se pasa de su cupo, sus **Disponibles** pueden quedar en **negativo y en rojo** —pensado para cuando das un juego extra fuera de dotación.

En la cabecera, junto a la dotación, el botón **🗒️ Historial de cambios** abre —en una **pestaña nueva**— una **página** con el **registro global de toda la carrera** (no el de un solo equipo). Se presenta como una **tabla en columnas** (hasta **tres columnas**) que aprovecha el ancho de la pantalla para verlo casi **sin scroll**. Los cambios salen **agrupados por manga**: se listan **todas las mangas**, y las que no tuvieron ningún cambio aparecen marcadas como **«— sin cambios de neumáticos —»**. Dentro de cada manga, cada entrega muestra el **equipo** (con su punto de color y su nombre), **qué número de juego** era para ese equipo (**juego N de la dotación**, contando por orden cronológico —1, 2, 3…—, en **rojo** si se pasó de su cupo) y el **minuto:segundo de carrera**. Los cambios sin manga asignada van a un grupo **«Sin manga»** al final. Es de **solo lectura** —para borrar, editar o añadir a mano se sigue usando el lápiz de cada equipo— y se **refresca en vivo** mientras se dan neumáticos.

**En la vista en directo**, cada tarjeta de equipo muestra un indicador **🛞 con el número de juegos de neumáticos usados**, junto a los avisos de **salidas (⚠️)** y **pit-stops (🔧)**. Se **actualiza al instante** —sin recargar— en cuanto anotas un cambio en el control de neumáticos, y **destella** cuando el número sube. Solo aparece en carreras de **resistencia con control de neumáticos**, y funciona con la manga **en marcha o en espera**.

> Todo se sincroniza al instante entre las pantallas abiertas, y el indicador de **manga:tiempo** late con la carrera.

## 13. Verificaciones técnicas de PitWall Control

Si el club pasa la **verificación técnica** de los coches con **PitWall Control**, ese resultado también puede llegar a PitWall — por el mismo puente de red que las tandas, con el mismo PIN y el mismo interruptor de **Conexión ecosistema** (ver *Importar una tanda de PitWall Control*).

Manga a manga, Control envía el **snapshot** de lo que tiene verificado por equipo: **pesos** (inicial, final y mínimo del coche), **motor** (tipo, rpm, ums), **piñón/corona** (marca, dientes, diámetro, material), **llantas** delantera y trasera, **trencilla**, **suspensión**, **bancada**, **chasis**, **neumático**, si quedó **validado** o no, y **observaciones** —con sus fotos, si las hay.

**Cómo se ve en PitWall.** En cuanto llega el primer envío, la página de la carrera muestra el botón **🔍 Verificaciones**, que lleva a una pantalla con todas las verificaciones **agrupadas por manga**.

> **Solo consulta.** En PitWall no se edita ni se da de alta ninguna verificación: todo se hace desde PitWall Control. Cada envío nuevo **sustituye por completo** las verificaciones de esa carrera (no se van sumando entregas sueltas).

> **A qué carrera van.** Si Control indica explícitamente la carrera, PitWall las asocia a esa. Si no, busca una carrera existente con el **nombre exacto** de la prueba; si tampoco encuentra coincidencia, **crea automáticamente** una carrera mínima para que las verificaciones tengan dónde vivir —el mismo comportamiento que al importar una tanda.

## 14. Vuelta a vuelta y correcciones (añadir / quitar vueltas)
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

> **Vueltas fantasma automáticas.** Una vuelta por debajo del **Pt** (tiempo mínimo) se marca como **fantasma** y el carril que la generó **nunca** la cuenta. PitWall ya no la reasigna a ojo: la **retiene** y solo se la asigna al carril que **confirma** haberse saltado un cruce (cuando ese carril pasa con una vuelta de ~el doble de su media). Si nadie lo confirma, se queda aquí como **fantasma** para que la revises a mano. Con **varios circuitos** (agrupador DS-300 o varios Master BART), la asignación automática **nunca cruza de un circuito a otro**: un fantasma solo puede certificarse en un carril de su mismo circuito, nunca en el de otro (son pistas físicamente distintas).

## 15. Resultados y exports
![img: 10-results-comparativa.png]

Al terminar (o en cualquier momento) entra en **Resultados**:

- **Comparativa** (parrilla): por participante, cada carril con **Rápida / Media / Consistencia / Salidas / Pit-stops**. En carreras de **pasadas/repetir-carril**, cada carril se desglosa en sus **ocurrencias** (1/2, 2/2) para comparar.
- **Progresión / Posiciones / Gap al líder / Gap (rejilla) / Estadísticas avanzadas**: distintas vistas de análisis (se explican en detalle en el *Manual de estadísticas*).
- **Exports**: **Excel**, **Puntos (xlsx/csv)**, **Control (csv)**, **Exportar para GitHub**, **PDF**.
- **Exportar a Excel** (resultados, puntos e informe de turnos) **solo funciona con la carrera parada o finalizada**: no se puede sacar el Excel mientras una manga está en marcha (ese cálculo es pesado y frenaría el cronometraje, con riesgo de perder un cruce). Si una manga arranca justo mientras se generaba, la exportación se cancela y basta con repetirla al acabar.

**Resultados públicos.** Hay una página abierta —**Resultados**, en el menú de inicio— donde cualquiera puede consultar (sin tocar nada ni poder editar) los resultados de las carreras **finalizadas**. Es la que compartes con pilotos y público para que miren la clasificación y las estadísticas de la carrera.

![img: op-resultados-publicos.png]

## 16. Entrenamiento
![img: 40-training.png]

Además de las carreras, PitWall tiene un modo **Entrenamiento** (desde la pantalla de inicio) para rodar sin montar una competición completa. Hay dos modalidades:

- **Entrenamiento libre**: registra **vueltas por carril sin estructura de equipos**. Ideal para sesiones abiertas donde cada uno prueba coche y pista; no hay rotación ni clasificación, solo tiempos por carril.
- **De competición**: equipos o pilotos asignados a carriles con **rotación automática tras cada tanda**, como una carrera pero pensado para entrenar el formato de campeonato.

Elige la modalidad, asigna los carriles y pulsa **Empezar**. El cronometraje en directo funciona igual que en carrera (GO de la caja, vueltas, mejor/media por carril).

**Los entrenos de competición se guardan.** Al **caer la bandera de cada heat**, PitWall guarda una fila por cada carril que ha rodado, con su **participante**, sus **vueltas**, su **mejor vuelta** y su **media**. Los participantes que **descansan** y los carriles **sin cruces** no dejan fila. Un **stop forzado no guarda** ese heat: se descarta y se repite entero.

Desde el setup del entreno de competición, el enlace **Ver entrenos guardados** abre la lista de sesiones (**fecha**, **nº de heats**, **participantes**, **vueltas** y **mejor vuelta**), con la más reciente arriba. Al pulsar una sesión ves su detalle con dos bloques:

- **Clasificación** de la sesión: gana quien **más vueltas suma** en todos sus heats y, a igualdad, quien tenga la **mejor vuelta**. La **media** es la de **todas** sus vueltas, ponderada por heat (un heat de 40 vueltas pesa lo que debe frente a uno de 3).
- **Heat a heat**: el desglose de cada heat, carril a carril.

Cada sesión se puede **borrar** desde su detalle. Si paras la sesión con **STOP** y llegó a guardar algún heat, PitWall te lleva directamente a **sus** resultados.

> El **entrenamiento libre** no guarda resultados: es una sesión abierta de tiempos por carril.

## 17. Ajustes
![img: 04-settings.png]

La **Configuración** se organiza con un **menú lateral**: **Fuente de datos**, **Preferencias**, **Red local**, **Seguimiento online**, **Integraciones** y **Diagnóstico**. Cada sección va en su pantalla, el menú lleva puntos de estado (cronómetro, túnel, modo debug) y, al guardar, vuelves a la sección en la que estabas. Abajo, una **barra fija de guardado** te avisa de los **cambios sin guardar** y de cuáles **necesitan reiniciar** PitWall (solo la interfaz de red y HTTPS; el resto se aplica al guardar).

- **Fuente de datos**: elige de dónde llegan los cruces — **Simulación**, **DS-300** (una caja por puerto, con su nº de carriles), **DS-300 agrupador** (varias cajas por un solo puerto COM: indica **puerto**, **baud** —57600, 8N1— y **nº de cajas** 2/3/4 → 16/24/32 carriles) o **BART** por Bluetooth (se conecta por **BLE directo** por defecto; queda **TCP** en la lista para el emulador o un puente BLE→TCP). Con el agrupador los carriles se numeran de corrido (caja 1 → 1–8, caja 2 → 9–16…) y una sola señal de salida arranca todas las cajas. Si usas **varios Master BART** (uno por cada bloque de carriles), añade una fila por cada uno con su **nombre BLE** (p. ej. `BART_TRACK1`, `BART_TRACK2`…) y su **nº de carriles**: se numeran de corrido igual que las cajas DS-300 del agrupador, y cada Master hay que emparejarlo por separado.
- **Configuración del puerto, sin líos**: en cada circuito DS-300 (y en el agrupador) de un vistazo solo ves **Puerto** y **Baud rate**. El **puerto** se elige de la lista de puertos detectados; si el tuyo no aparece, con **«Escribir el path a mano»** lo tecleas (p. ej. `COM3` o `/dev/ttys003`). El **baud rate** es un desplegable con las velocidades habituales (9600–921600), con **«Escribir a mano»** para un valor fuera de lista. Los ajustes finos de la conexión serie (**Data bits, Paridad, Stop bits, Control de flujo**) están plegados en **«Opciones avanzadas del puerto»**: por defecto **8N1** y casi nunca hay que tocarlos.
- **Preferencias**: el **Orden del directo** (por clasificación estimada o por vueltas reales; ver *Dirigir la carrera en vivo*).
- **Red local**: interfaz de red, restringir el acceso web y HTTPS local (para la cámara del QR).
- **Seguimiento público por internet**: publica las vistas públicas en internet para seguir la carrera desde fuera del local (ver la sección siguiente).
- **Integraciones** (compatibilidad Infolap, que se activa y desactiva al momento) y **Diagnóstico** (modo debug y herramientas para investigar un problema).
- El **idioma** (ES/EN) se cambia desde el pie de página.

**Base de datos.** En **Sistema → Base de datos** (`/database`) tienes un menú con **Resumen** (cuántas carreras, equipos, pilotos, circuitos y vueltas hay, y el tamaño del fichero), **Exp. / Imp. carrera**, **Copia de seguridad** y **Restaurar copia**.

**Exportar e importar una carrera.** Para llevarte a tu PC una carrera que has corrido en otro club sin mover la base de datos entera. **Exportar carrera** descarga un archivo **`.pwrace`** con todo: equipos, pilotos, tandas, mangas, vueltas, turnos de piloto, neumáticos, sucesos, verificaciones con fotos, pole y categorías (una 24 h de 150.000 vueltas ocupa unos 3 MB). **Importar carrera** la añade como **carrera nueva, al momento y sin reiniciar**, sin tocar tus otras carreras; si su circuito no existe en este PC, se crea.
- No se puede importar **dos veces la misma carrera**: PitWall avisa y te enlaza a la que ya tienes.
- No se exporta una carrera con una **manga sin cerrar**: ciérrala o cancélala antes en **Solución de problemas → Mangas atascadas**.
- Una carrera que venía **en curso** entra como **pendiente**, para que nunca se quede con el GO del DS-300 de este PC.
- Exportar e importar esperan a que **no haya una manga en marcha**, igual que la exportación a Excel.

![img: op-database-carrera.png]

**Copia de seguridad de la base de datos.** En **Copia de seguridad** y **Restaurar copia** puedes **descargar** un snapshot completo de tus datos (`.db`) y, si algún día hace falta recuperar una instalación o mover PitWall a otro PC, **subir** una copia para restaurarla: la subida se valida (tiene que ser una base de datos SQLite real) y queda "pendiente" — no sustituye nada al momento, se aplica solo al **cerrar PitWall del todo y volver a abrirlo**, y antes de aplicarla se guarda automáticamente una copia de los datos que tenías. Puedes cancelar una importación pendiente en cualquier momento antes de reiniciar.

**Historial de versiones.** En el **pie de todas las páginas** ves el número de **versión** de PitWall. Al pulsarlo se abre el **Historial de versiones** (`/changelog`), con lo **Añadido**, **Mejorado** y **Corregido** en cada actualización. La versión **sube con cada actualización**, así siempre sabes qué PitWall tienes y qué ha cambiado.

## 18. Seguimiento público por internet
![img: op-seguimiento-publico.png]

Por defecto las vistas de PitWall (el **directo**, los **Resultados** y la **vista web de PitWall Lap**) solo se ven en la **red local**. Con el **Seguimiento público por internet** cada club puede **publicarlas en internet** para que pilotos y público sigan la carrera **desde fuera del local**, sin abrir puertos ni montar una VPN: PitWall levanta un **túnel Cloudflare propio** del club.

> La **app nativa** de PitWall Lap no pasa por este túnel: siempre necesita estar en la **misma red local** que el servidor, la publiques o no en internet.

Está en **Ajustes → Seguimiento público por internet**. Hay **dos modos**:

- **Rápido.** PitWall genera una **URL temporal** (`*.trycloudflare.com`) al vuelo: **sin cuenta ni dominio**. Es la opción para una tarde suelta; ten en cuenta que la URL **cambia en cada arranque**.
- **Cloudflare propio.** Usas el **token del túnel** del club y **tu propio dominio**, con lo que la **URL es fija** y de marca. La propia pantalla trae una **guía paso a paso**, con enlaces al panel **Zero Trust** de Cloudflare y a la documentación oficial, para crear el túnel y pegar su token.

**Controles.** Botones **Arrancar** / **Parar** con el **estado** y la **URL en vivo** (para copiarla y compartirla). **Arrancar** aplica lo que tengas en pantalla en ese momento. Puedes activar el **autoarranque** para que el túnel se levante solo al abrir PitWall.

**Instalar cloudflared.** El túnel lo levanta la herramienta `cloudflared`. Si no está instalada, aparece el botón **Instalar cloudflared**, que **descarga la versión oficial** a la carpeta de datos de PitWall — **sin pedir permisos de administrador**.

> **Seguridad.** Desde fuera **solo se ven las vistas públicas** (directo, resultados y la vista web de PitWall Lap). El **control de la app** (crear, dirigir o editar carreras) **queda bloqueado**: nadie de fuera puede tocar la carrera.

## 19. Glosario (operación)
- **Carrera**: el evento completo. Se compone de tandas.
- **Tanda**: grupo de participantes con su rotación; se compone de mangas.
- **Manga**: una tirada cronometrada (todos los carriles a la vez) de una duración.
- **Rotación**: cómo cambian de carril los participantes de una manga a otra.
- **Descanso**: manga en la que un participante no corre (hueco `0` en la secuencia).
- **Pasada**: recorrido completo de la secuencia de carriles; N pasadas = N× mangas.
- **Repetir carril**: correr cada carril N mangas seguidas, sumando vueltas.
- **GO**: la señal de salida (de la caja DS-300) que arranca la manga.
- **Vuelta fantasma**: vuelta marcada como no válida (no cuenta), restaurable.
- **Salida (⚠️)**: vuelta que tarda más que la vuelta rápida de ese piloto en ese carril durante la manga + 1,5 s (como las «vueltas lentas» de TicTac); si tarda el doble de su media limpia o más, es parada en boxes (🔧). En directo es provisional: al mejorar la rápida, vueltas anteriores pueden pasar a ser salida.
- **Pole**: sesión de clasificación previa (opcional); todos ruedan por el mismo carril y su mejor vuelta fija la parrilla de salida.
- **Sucesos**: página (🗒️) con el registro manga a manga de todo lo que pasa en la carrera —GO, pausas, fin de manga, vueltas fantasma, fichajes de piloto…—, en vivo.
- **Entrenamiento libre**: modo para registrar vueltas por carril sin equipos ni rotación (sesión abierta).
- **PitWall Lap**: seguimiento por equipo/piloto desde el móvil (vueltas cantadas, posición y, en la app, estrategia de neumáticos) — como vista web con PIN o como app nativa instalada.
- **PIN**: código por equipo para entrar a su panel en la vista web de PitWall Lap (la app nativa no lo usa: descubre el servidor sola en la red local).
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
