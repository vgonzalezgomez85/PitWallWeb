# PitWall en 1 minuto — píldoras de vídeo

Vídeos horizontales (1920×1080), cortos: alrededor de 1 minuto (pasarse un poco no importa). **De momento solo en español** (2026-10-22): otros idiomas obligan a regrabar la pantalla con la interfaz en ese idioma; se deja para más adelante.

---

## 1. Lista de píldoras

Ordenadas como alguien aprende el programa (✅ = montada, en `~/Movies/PitWall píldoras/`). ⏱ = las que pueden pasar del minuto si no se recortan (entre paréntesis, cómo partirlas).

### A · Primeros pasos
| Nº | Píldora | Qué se ve | Sección del manual |
|---|---|---|---|
| 01 | Guarda tu pista (escenarios) ✅ | Circuitos y carriles, secuencia de rotación, colores, vuelta mínima (Pt), trazado | Uso §2 |
| 02 | Conectar el cronómetro ✅ | Ajustes → Fuente de datos: DS, agrupador, BART, TicTac, Simulación; asignar el escenario | Uso §17 |
| 03 | La pantalla de inicio ✅ | Buscador «Ir a…» (⌘K), franja de la carrera, mosaicos, barra de ventanas | Uso §1 |
| 04 | Modo básico o avanzado ✅ | Personalizar: los cinco diseños y el modo básico | Uso §1 |

### B · Preparar la carrera
| Nº | Píldora | Qué se ve | Sección |
|---|---|---|---|
| 05 | ~~Colores de los carriles~~ (descartada) | Colores propios del escenario y globales | Uso §2, §17 |
| 06 | Pilotos, equipos y coches ✅ | Alta de fichas, bandera, importar CSV, buscador | Uso §2 |
| 07 | Crear una carrera sprint ✅ | El asistente paso a paso hasta Confirmar | Uso §3 |
| 08 | Tandas y rotación ✅ | Participantes, descansos DSC, carriles vacíos (08a rotación · 08b carriles vacíos) | Uso §5 |
| 09 | Traer la prueba de PitWall Control | Importar tanda por fichero o por red con PIN | Uso §4 |

### C · Correr
| Nº | Píldora | Qué se ve | Sección |
|---|---|---|---|
| 10 | Pole position ✅ | Montar la pole, cronometrarla, saltar a quien no se presenta, elegir carril | Uso §7 |
| 11 | El GO y el directo ✅ | Semáforo, tarjetas por carril, clasificación estimada (11a tarjetas · 11b estimada al lado) | Uso §9 |
| 12 | ~~Pausa, stop y fin de manga~~ (dentro de la 11) | Botones, vuelta de bandera, paso a la manga siguiente | Uso §9 |
| 13 | ~~Pantalla de TV y otra pantalla~~ (descartada) | TV para el público, Ajustes → Ventanas y pantallas | Uso §9, §17 |
| 14 | ~~Estadísticas en vivo ⏱~~ (descartada) | Ritmo, consistencia, proyección (14a manga · 14b toda la carrera) | Estadísticas |
| 15 | Corregir vueltas ✅ | Añadir y quitar vueltas con la manga en marcha y cerrada | Uso §14 |
| 16 | ~~PitWall Lap para los equipos~~ (descartada) | PIN del equipo, el móvil canta las vueltas, seguir rivales | Lap |

### D · Después de la carrera
| Nº | Píldora | Qué se ve | Sección |
|---|---|---|---|
| 17 | Resultados y exportar ✅ | Pestañas de resultados, Excel, PDF | Uso §15 |
| 18 | ~~El nombre y el logo del club~~ (descartada) | Preferencias → Nombre y logo; cómo sale en Excel, TV y QR | Uso §17 |
| 19 | ~~Llevarte una carrera y hacer copias~~ (descartada) | Exportar/importar .pwrace, copia de seguridad | Uso §17 |

### E · Entrenar
| Nº | Píldora | Qué se ve | Sección |
|---|---|---|---|
| 20 | Entreno libre ✅ | Abrirlo, las 10 mejores / 10 últimas, vista compacta | Uso §16 |
| 21 | ~~Entreno de competición~~ (descartada) | Equipos del catálogo, tiempos por piloto | Uso §16 |

### F · Resistencia
| Nº | Píldora | Qué se ve | Sección |
|---|---|---|---|
| 22 | ~~Carrera de resistencia: las reglas~~ (descartada) | Mínimo/máximo por piloto, turnos, sin cambios al final | Uso §3, §11 |
| 23 | ~~Cambio de piloto con QR~~ (descartada) | Tarjetas QR, escanear en el control de pilotos | Uso §11 |
| 24 | ~~Control de neumáticos~~ (descartada) | Juegos por equipo, historial, aviso en el directo | Uso §12 |

### G · Para el club
| Nº | Píldora | Qué se ve | Sección |
|---|---|---|---|
| 25 | ~~Contraseña de acceso~~ (descartada) | Proteger Sistema y Catálogo; Entrar / Bloquear | Uso §17 |
| 26 | ~~Seguir la carrera por internet~~ (descartada) | Seguimiento online con túnel | Uso §18 |

Total: 26 píldoras (unas 30 si se parten las ⏱).

---

## 2. Cómo se graban

**Imagen**
- 1920×1080 a 30 fps. En la pantalla Retina del Mac se graba a 3840×2160 y se reduce: el texto queda más nítido.
- La app de escritorio a pantalla completa, o el navegador sin barras con la ventana a 1920×1080. Zoom de página al 110-125 % para que se lea bien en un portátil.
- Modo Concentración activado (sin notificaciones), puntero un poco más grande y un círculo al hacer clic.
- Una base de datos **de demostración** aparte: nombres de club bonitos y una carrera a medias, siempre igual, para que cada toma salga idéntica y no salgan datos reales del club. La de verdad se aparta con una copia `.backup` y con PitWall cerrado.
- Sin hardware: el emulador del DS-300 (banco de pruebas) y la carrera simulada.

**Voz e idiomas** (para cuando se hagan otras versiones)
- La interfaz tiene que estar en el idioma de la voz, así que **la pantalla se graba una vez por idioma**. Para que no sea un castigo, los clics los hace un guion automático en el navegador: misma toma, mismo ritmo, solo cambia el idioma.
- PitWall habla español, inglés e italiano. **El francés no está en la app** (sí en los manuales): el vídeo en francés tendría que mostrar la interfaz en inglés, o antes hay que traducir la app.
- Voces: el español lo grabas tú. Para el italiano, Emanuele Palena (el traductor) es la opción natural. Inglés y francés: una persona nativa o una voz sintética neuronal (las de calidad son de pago; las voces del Mac son gratis pero se notan artificiales).
- Unas 120-140 palabras por minuto en español. El inglés ocupa un 10-15 % menos y el italiano y el francés algo más, así que el guion español se deja en 55 s para que quepan todos.

**Montaje**
- Portada de 2 s con el logo y el título, la toma con zooms a la zona importante, y 2 s de cierre con «Siguiente: …».
- Subtítulos `.srt` en cada idioma (se pueden quemar en la imagen para redes sociales).
- Música de fondo suave, sin letra y libre de derechos.

---

## 3. Guion de la píldora 02 — Conectar el cronómetro

**Objetivo**: que quien acaba de instalar PitWall sepa elegir su aparato y comprobar que llegan los datos.
**Duración**: 56 s · **Palabras**: ~125
**Preparación**: emulador del DS-300 en marcha (su puerto sale en la lista); PitWall con la fuente en «Sin conexión»; interface TicTac del emulador para la toma de 0:33.

| Tiempo | Pantalla y acción | Voz |
|---|---|---|
| 0:00-0:03 | Portada: «PitWall en 1 minuto · Conectar el cronómetro» | — |
| 0:03-0:09 | Inicio. Zoom a la píldora de estado de la cabecera, que dice «Sin conexión». | Antes de la primera carrera, dile a PitWall de dónde llegan las vueltas. Esta píldora te dice si el cronómetro está conectado. |
| 0:09-0:12 | Clic en **Ajustes** (mosaico de Sistema). | Entramos en Ajustes. |
| 0:12-0:20 | **Fuente de datos**. El puntero recorre las tarjetas despacio: DS, DS-300 agrupador, BART, TicTac, Simulación. | Aquí eliges tu aparato: un DS por puerto serie, varias cajas en un agrupador, BART por Bluetooth o el interface TicTac por USB. |
| 0:20-0:33 | Tarjeta **DS**. Modelo **DS-300** (zoom: el baud pasa solo a 56000). Puerto de la lista. Carriles: 8. Se ve plegado «Opciones avanzadas del puerto», sin abrirlo. | Con un DS, elige el modelo y la velocidad se pone sola. Escoge el puerto de la lista y cuántos carriles tiene tu pista. Lo demás ya viene bien de fábrica. |
| 0:33-0:40 | Tarjeta **TicTac**: zoom al estado «✓ TicTacSlot detectado por USB». | Con TicTac no hay nada que configurar: enchúfalo y PitWall lo encuentra solo. |
| 0:40-0:45 | Vuelve a la tarjeta DS. Clic en **Guardar y aplicar** en la barra de abajo. | Pulsa Guardar y aplicar. No hace falta reiniciar. |
| 0:45-0:53 | Inicio. Zoom a la píldora, ahora «DS-300 conectado» en verde, y al estado del enlace abajo a la derecha. | De vuelta al inicio, el verde confirma que ya llegan los datos. ¿Solo quieres probar? Elige Simulación. |
| 0:53-0:56 | Cierre: logo + «Siguiente: crea tu primera carrera». | Siguiente: crea tu primera carrera. |

**Texto completo de la voz** (para grabar de un tirón):

> Antes de la primera carrera, dile a PitWall de dónde llegan las vueltas. Esta píldora te dice si el cronómetro está conectado. Entramos en Ajustes.
> Aquí eliges tu aparato: un DS por puerto serie, varias cajas en un agrupador, BART por Bluetooth o el interface TicTac por USB.
> Con un DS, elige el modelo y la velocidad se pone sola. Escoge el puerto de la lista y cuántos carriles tiene tu pista. Lo demás ya viene bien de fábrica.
> Con TicTac no hay nada que configurar: enchúfalo y PitWall lo encuentra solo.
> Pulsa Guardar y aplicar. No hace falta reiniciar.
> De vuelta al inicio, el verde confirma que ya llegan los datos. ¿Solo quieres probar? Elige Simulación.
> Siguiente: crea tu primera carrera.

---

## 4. Montaje

Los scripts están en `montaje/` (necesitan `ffmpeg` y Google Chrome):

- Cada píldora es un `.json` con la grabación de origen, los encuadres (recortes del 4K) y los tramos: desde/hasta, encuadre, velocidad y rótulo.
- `node montaje/render.js montaje/p01-escenario.json` genera los rótulos con Chrome (fuentes y logo de PitWall) y monta el MP4 en 1920×1080 a 30 fps.
- Grabar en 4K con la ventana grande: así se puede ampliar hasta 2× sin perder nitidez.
