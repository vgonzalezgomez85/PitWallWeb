#!/usr/bin/env python3
"""Busca en internet carreras de slot en Europa con IA (DeepSeek + Tavily, o Claude)
y genera datos/carreras-auto.json para el buscador de carreras de pitwall.es.

Pensado para ejecutarse en el servidor una vez por semana (cron o systemd timer).
Solo usa la biblioteca estándar de Python 3.9+.

Uso:
  python3 buscar-carreras.py --salida /var/www/pitwall/datos/carreras-auto.json
  python3 buscar-carreras.py --salida prueba.json --max-lotes 1 --sin-clubes     # prueba barata
  python3 buscar-carreras.py --solo-clubes --estado clubes.json --max-clubes 5   # probar los clubes sin tocar el JSON

Además de los campeonatos, mantiene una lista de clubes de slot (--estado) y lee los calendarios de sus webs:
una vez al mes la IA busca clubes nuevos por país; cada semana se visitan las webs de los clubes conocidos.

Variables de entorno:
  PITWALL_PROVEEDOR   deepseek (por defecto) o claude
  DEEPSEEK_API_KEY    con deepseek
  TAVILY_API_KEY      con deepseek: buscador web (tavily.com, plan gratuito)
  ANTHROPIC_API_KEY   con claude
  PITWALL_MODELO      opcional (deepseek-chat / claude-opus-5-5 por defecto)

PitWall Web — AGPLv3 o posterior. Véase LICENSE.
"""
import argparse
import html as html_mod
import datetime as dt
import json
import os
import re
import sys
import tempfile
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request

PROVEEDOR = os.environ.get("PITWALL_PROVEEDOR", "deepseek").lower()
MODELO = os.environ.get("PITWALL_MODELO") or {"deepseek": "deepseek-chat", "claude": "claude-opus-5-5"}.get(PROVEEDOR, "")
CLAVES = {"deepseek": ["DEEPSEEK_API_KEY", "TAVILY_API_KEY"], "claude": ["ANTHROPIC_API_KEY"]}
AQUI = os.path.dirname(os.path.abspath(__file__))

# Países donde se hacen búsquedas abiertas para descubrir campeonatos que no están en la lista.
PAISES_DESCUBRIR = [
    ("España", "carreras de slot, resistencias de slot, campeonato de slot"),
    ("Portugal", "corridas de slot, campeonato de slot"),
    ("Italia", "gare di slot, campionato slot car"),
    ("Francia", "courses de slot, championnat slot racing"),
    ("Alemania", "Slotcar Rennen, Slotracing Meisterschaft"),
    ("Reino Unido", "slot car racing championship, slot racing endurance"),
    ("Países Bajos y Bélgica", "slotrace kampioenschap, slot racing"),
    ("Suiza y Austria", "Slotcar Rennen, Slotracing"),
    ("países nórdicos", "slot car racing championship"),
    ("Europa del Este", "slot car racing championship"),
    ("Europa (eventos internacionales)", "European slot car championship, slot endurance international"),
]

TIPOS = {"resistencia", "velocidad", "rally", "raid", "otro"}

# Europa geográfica amplia: lo que no esté aquí se descarta.
EUROPA = set("AD AL AT BA BE BG BY CH CY CZ DE DK EE ES FI FO FR GB GI GR HR HU IE IM IS IT LI LT LU LV MC MD ME MK MT NL NO PL PT RO RS SE SI SK SM TR UA VA XK".split())

SISTEMA = """Eres un documentalista experto en slot racing (coches de slot / scalextric / slot car racing, escalas 1/32 y 1/24) en Europa.
Tu trabajo es encontrar en internet fechas CONCRETAS de carreras de slot y devolverlas como datos.

Reglas estrictas:
- Solo carreras de SLOT (coches eléctricos en pista con carril guía). Nada de karting, automovilismo real, RC ni simracing.
- Solo CARRERAS: nada de ferias, bolsas de intercambio, exposiciones, cursos ni jornadas de puertas abiertas.
- Solo eventos en Europa.
- Solo fechas que aparezcan publicadas en una página que hayas consultado. Si no encuentras la fecha exacta, NO incluyas la carrera. Nunca deduzcas fechas de años anteriores.
- Cada carrera debe llevar en "enlace" la URL exacta de la página donde viste la fecha (el calendario, no la portada si la fecha está en otra página).
- "campeonato" es el nombre sin el año ni la temporada (p. ej. "Resisbarna", no "Resisbarna 2026").
- "notas" solo para información útil al piloto (formato, inscripción, horario); no comentes nada sobre el rango de fechas.
- Prefiere las webs oficiales del campeonato o club, foros de slot y calendarios publicados.
- Si una carrera dura varios días, usa "fecha" para el primero y "fecha_fin" para el último.

Al terminar de buscar, responde ÚNICAMENTE con un bloque <json>...</json> que contenga un array de objetos con estas claves:
  "fecha" (AAAA-MM-DD, obligatoria), "fecha_fin" (AAAA-MM-DD o null), "nombre" (obligatoria, nombre de la carrera o prueba),
  "campeonato" (nombre del campeonato o null si es una carrera suelta),
  "tipo" (uno de: "resistencia" para resistencias/endurance por horas, "velocidad" para sprint/mangas/F1/GT por vueltas,
          "rally" para rally slot por tramos, "raid" para raid/4x4/trial, "otro" si no encaja), "club", "circuito", "ciudad",
  "pais" (código ISO de 2 letras), "escala" ("1/32", "1/24"... o null), "categoria" (o null),
  "enlace" (URL obligatoria), "notas" (breve, o null).
Si no encuentras nada fiable, responde <json>[]</json>."""


def leer_campeonatos():
    lotes = []
    with open(os.path.join(AQUI, "campeonatos.txt"), encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea or linea.startswith("#"):
                continue
            nombre, _, pista = linea.partition("|")
            lotes.append((nombre.strip(), pista.strip()))
    return lotes


def construir_lotes(desde, hasta):
    rango = f"entre el {desde.isoformat()} y el {hasta.isoformat()}"
    lotes = []
    for nombre, pista in leer_campeonatos():
        lotes.append((f"campeonato: {nombre}",
            f"Busca el calendario del campeonato de slot «{nombre}» ({pista}). "
            f"Quiero todas sus pruebas {rango}, con fecha, sede y enlace a la fuente. "
            f"Si el campeonato tiene otro nombre o no existe con ese nombre, dilo en 'notas' solo si encuentras el correcto."))
    for pais, palabras in PAISES_DESCUBRIR:
        lotes.append((f"descubrir: {pais}",
            f"Busca carreras y campeonatos de slot en {pais} {rango}. "
            f"Términos útiles: {palabras}. Incluye resistencias, campeonatos regionales y nacionales, "
            f"trofeos de clubes y eventos internacionales. Busca también calendarios de federaciones y asociaciones de slot."))
    return lotes


def post_json(url, cuerpo, cabeceras, intentos=5, timeout=600):
    """POST JSON con reintentos ante saturación o fallos de red."""
    datos = json.dumps(cuerpo).encode()
    for i in range(intentos):
        req = urllib.request.Request(url, data=datos, method="POST",
                                     headers={"content-type": "application/json", **cabeceras})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            detalle = e.read().decode(errors="replace")[:500]
            if e.code in (429, 500, 502, 503, 529) and i < intentos - 1:
                espera = int(e.headers.get("retry-after") or 0) or 20 * (i + 1)
                log(f"  {url.split('/')[2]} {e.code}, reintento en {espera}s")
                time.sleep(espera)
                continue
            raise RuntimeError(f"{url.split('/')[2]} {e.code}: {detalle}")
        except (urllib.error.URLError, TimeoutError) as e:
            if i < intentos - 1:
                time.sleep(20 * (i + 1))
                continue
            raise RuntimeError(f"red: {e}")


# ---------- Claude: busca y lee páginas él mismo (herramienta web_search del servidor) ----------

def preguntar_claude(prompt, sistema=None, buscar=True):
    """Una conversación (con búsqueda web si buscar=True). Devuelve (texto final, nº de búsquedas)."""
    cabeceras = {"x-api-key": os.environ["ANTHROPIC_API_KEY"], "anthropic-version": "2023-06-01"}
    pregunta = {"role": "user", "content": prompt}
    hecho, busquedas = [], 0
    for _ in range(6):
        cuerpo = {
            "model": MODELO,
            "max_tokens": 16000,
            "system": sistema or SISTEMA,
            "messages": [pregunta] + ([{"role": "assistant", "content": hecho}] if hecho else []),
        }
        if buscar:
            cuerpo["tools"] = [{"type": "web_search_20250305", "name": "web_search", "max_uses": 10}]
        resp = post_json("https://api.anthropic.com/v1/messages", cuerpo, cabeceras)
        busquedas += (resp.get("usage", {}).get("server_tool_use") or {}).get("web_search_requests", 0)
        hecho += resp.get("content", [])
        # Con herramientas del servidor la API puede pausar un turno largo: se continúa reenviándolo.
        if resp.get("stop_reason") == "pause_turn":
            continue
        texto = "".join(b.get("text", "") for b in hecho if b.get("type") == "text")
        return texto, busquedas
    raise RuntimeError("la conversación no terminó tras varias pausas")


# ---------- DeepSeek: no busca solo, así que le damos dos herramientas que ejecuta este script ----------
# buscar_web y leer_pagina van contra Tavily (tavily.com); leer_pagina intenta antes descargar la página directamente.

HERRAMIENTAS = [
    {"type": "function", "function": {
        "name": "buscar_web",
        "description": "Busca en internet. Devuelve títulos, URLs y un extracto de cada resultado.",
        "parameters": {"type": "object", "properties": {
            "consulta": {"type": "string", "description": "Texto a buscar, en el idioma del país"}},
            "required": ["consulta"]}}},
    {"type": "function", "function": {
        "name": "leer_pagina",
        "description": "Descarga una página web o PDF y devuelve su texto (recortado).",
        "parameters": {"type": "object", "properties": {
            "url": {"type": "string"}}, "required": ["url"]}}},
]
MAX_HERRAMIENTAS = 10         # llamadas a herramientas por lote
MAX_TEXTO = 30000             # caracteres de cada página que se le pasan al modelo


def tavily(ruta, cuerpo):
    return post_json(f"https://api.tavily.com/{ruta}", cuerpo,
                     {"authorization": f"Bearer {os.environ['TAVILY_API_KEY']}"}, intentos=3, timeout=90)


def buscar_web(consulta):
    r = tavily("search", {"query": consulta, "max_results": 8, "search_depth": "basic"})
    return [{"titulo": x.get("title"), "url": x.get("url"), "extracto": (x.get("content") or "")[:500]}
            for x in r.get("results", [])]


def html_a_texto(html):
    html = re.sub(r"(?is)<(script|style|noscript|svg|head)\b.*?</\1>", " ", html)
    html = re.sub(r"(?i)<br\s*/?>|</(p|div|li|tr|h\d|td|th)>", "\n", html)
    html = re.sub(r"<[^>]+>", " ", html)
    texto = html_mod.unescape(html)
    texto = re.sub(r"[ \t\r\f\v]+", " ", texto)
    return re.sub(r"\n\s*\n+", "\n", texto).strip()


def descargar(url):
    """Descarga directa de una página HTML. Devuelve (html, url final) o (None, url) si no es HTML o falla."""
    try:
        req = urllib.request.Request(url, headers={"user-agent": "Mozilla/5.0 (PitWall buscador de carreras; +https://www.pitwall.es)"})
        with urllib.request.urlopen(req, timeout=30) as r:
            tipo = r.headers.get("content-type", "")
            if "html" not in tipo and "text" not in tipo:
                return None, r.geturl()
            return r.read(3_000_000).decode(r.headers.get_content_charset() or "utf-8", "replace"), r.geturl()
    except Exception:
        return None, url


def leer_pagina(url):
    if not re.match(r"https?://", url or ""):
        return "URL no válida"
    html, _ = descargar(url)   # primero directo, que es gratis
    if html:
        texto = html_a_texto(html)
        # Webs hechas con JavaScript devuelven poco más que el menú: sin ningún año a la vista, mejor Tavily.
        if len(texto) > 300 and re.search(r"\b20\d\d\b", texto):
            return texto[:MAX_TEXTO]
    r = tavily("extract", {"urls": [url]})   # PDFs, webs con JavaScript o que bloquean descargas
    res = r.get("results") or []
    return (res[0].get("raw_content") or "")[:MAX_TEXTO] if res else "No se ha podido leer la página."


def preguntar_deepseek(prompt, sistema=None, buscar=True):
    """Bucle de herramientas compatible con la API de OpenAI. Devuelve (texto final, nº de búsquedas)."""
    cabeceras = {"authorization": f"Bearer {os.environ['DEEPSEEK_API_KEY']}"}
    mensajes = [{"role": "system", "content": (sistema or SISTEMA) + f"\nHoy es {dt.date.today().isoformat()}."},
                {"role": "user", "content": prompt}]
    usadas = busquedas = 0
    while True:
        cuerpo = {"model": MODELO, "messages": mensajes, "max_tokens": 8000, "temperature": 0.2}
        if not buscar:
            pass
        elif usadas < MAX_HERRAMIENTAS:
            cuerpo["tools"] = HERRAMIENTAS
        else:
            mensajes.append({"role": "user", "content": "Ya no puedes buscar más. Responde ahora con el bloque <json>."})
        msg = post_json("https://api.deepseek.com/chat/completions", cuerpo, cabeceras)["choices"][0]["message"]
        llamadas = msg.get("tool_calls") or []
        if not llamadas:
            return msg.get("content") or "", busquedas
        mensajes.append({"role": "assistant", "content": msg.get("content") or "", "tool_calls": llamadas})
        for t in llamadas:
            usadas += 1
            try:
                args = json.loads(t["function"].get("arguments") or "{}")
                if t["function"]["name"] == "buscar_web":
                    busquedas += 1
                    log(f"    buscar: {args.get('consulta')}")
                    salida = json.dumps(buscar_web(args.get("consulta", "")), ensure_ascii=False)
                elif t["function"]["name"] == "leer_pagina":
                    log(f"    leer:   {args.get('url')}")
                    salida = leer_pagina(args.get("url", ""))
                else:
                    salida = "Herramienta desconocida"
            except Exception as e:
                salida = f"Error: {e}"
            mensajes.append({"role": "tool", "tool_call_id": t["id"], "content": salida})


# ---------- Clubes de slot: se descubren una vez al mes y cada semana se leen sus calendarios ----------

SISTEMA_CLUBES = """Eres un documentalista experto en slot racing (coches de slot / scalextric / slot car racing) en Europa.
Tu trabajo es encontrar las WEBS PROPIAS de clubes de slot (asociaciones, clubes con pista, tiendas con pista que organizan carreras).

Reglas:
- Solo clubes de slot en Europa que tengan web propia. Nada de Facebook, Instagram, YouTube ni foros generales.
- Nada de karting, RC, simracing ni tiendas online sin pista.
- Si ves la página de calendario, agenda o eventos del club, ponla en "calendario".

Al terminar, responde ÚNICAMENTE con un bloque <json>...</json> con un array de objetos:
  "nombre" (obligatorio), "web" (URL de la portada, obligatoria), "calendario" (URL o null), "ciudad", "pais" (código ISO de 2 letras).
Si no encuentras nada fiable, responde <json>[]</json>."""

PAISES_CLUBES = [
    ("España", "club de slot, asociación slot, pista de slot, slot club"),
    ("Portugal", "clube de slot, pista de slot"),
    ("Italia", "slot club, pista slot, associazione slot car"),
    ("Francia", "club de slot racing, circuit routier miniature, slot racing club"),
    ("Alemania y Austria", "Slotcar Club, Slotracing Verein, Carrerabahn Verein"),
    ("Reino Unido e Irlanda", "slot car club, scalextric club"),
    ("Países Bajos y Bélgica", "slotracing club, slotrace vereniging, racebaan club"),
    ("Suiza", "Slotcar Club, slot racing club Suisse"),
    ("países nórdicos", "slot car club, bilbana klubb, autorata kerho"),
    ("Europa del Este", "slot car club, autodráha klub, klub slot"),
]

REDES = re.compile(r"(facebook|instagram|youtube|youtu\.be|tiktok|twitter|x\.com|whatsapp|wa\.me|linkedin|google\.|forum)", re.I)
CALENDARIO = re.compile(r"calend|agenda|event|carrer|cursa|race|course|gare|kalend|termin|rennen|wedstrijd|competic|campeonat|championship|programm?a|fixture|diary|kalenteri|tavling", re.I)
MAX_TEXTO_CLUB = 40000


def dominio(url):
    return urllib.parse.urlsplit(url).netloc.lower().removeprefix("www.")


def cargar_estado(ruta):
    try:
        with open(ruta, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return {"clubes": {}}


def leer_clubes_semilla():
    """Clubes que se añaden a mano en clubes.txt: web | nombre | ciudad | país."""
    out = []
    try:
        with open(os.path.join(AQUI, "clubes.txt"), encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if linea and not linea.startswith("#"):
                    p = [x.strip() for x in linea.split("|")] + ["", "", ""]
                    out.append({"web": p[0], "nombre": p[1] or dominio(p[0]), "ciudad": p[2], "pais": p[3].upper()})
    except OSError:
        pass
    return out


def anadir_club(estado, c, origen):
    web = (c.get("web") or "").strip()
    if not re.match(r"https?://", web) or REDES.search(dominio(web)):
        return False
    d = dominio(web)
    previo = estado["clubes"].get(d)
    club = previo or {"web": web, "alta": dt.date.today().isoformat(), "origen": origen, "fallos": 0}
    for k in ("nombre", "ciudad", "pais", "calendario"):
        v = c.get(k)
        if isinstance(v, str) and v.strip() and v.strip().lower() != "null" and not club.get(k):
            club[k] = v.strip()[:120]
    if club.get("calendario") and not re.match(r"https?://", club["calendario"]):
        club["calendario"] = urllib.parse.urljoin(web, club["calendario"])   # a veces viene como "/calendario/"
    if club.get("calendario") and dominio(club["calendario"]) != d:
        del club["calendario"]   # el calendario tiene que ser del mismo dominio que el club
    if previo and origen == "manual":
        club["fallos"] = 0
    estado["clubes"][d] = club
    return not previo


def descubrir_clubes(preguntar, estado):
    """Busca clubes nuevos por país. Devuelve (clubes nuevos, búsquedas gastadas)."""
    nuevos = busquedas = 0
    for i, (pais, palabras) in enumerate(PAISES_CLUBES, 1):
        log(f"[clubes {i}/{len(PAISES_CLUBES)}] descubrir: {pais}")
        try:
            texto, n = preguntar(
                f"Busca webs de clubes de slot en {pais}. Términos útiles: {palabras}. "
                f"Busca también listados de clubes en webs de federaciones, asociaciones o campeonatos de slot. "
                f"Quiero cuantos más mejor (hasta 30), con su web propia.", sistema=SISTEMA_CLUBES)
            busquedas += n
            lista = extraer_json(texto)
        except Exception as e:
            log(f"  ERROR: {e}")
            continue
        n_nuevos = sum(anadir_club(estado, c, "ia") for c in lista if isinstance(c, dict))
        nuevos += n_nuevos
        log(f"  {len(lista)} clubes, {n_nuevos} nuevos")
    estado["ultimo_descubrimiento"] = dt.date.today().isoformat()
    return nuevos, busquedas


# Muchos clubes publican el calendario como datos: schema.org (JSON-LD o microdatos), iCal / Google Calendar
# o plugins de eventos de WordPress que pintan el calendario con JavaScript. Eso se lee directamente, sin IA.

ICS = re.compile(r"""(?:href|src)=["']([^"']*(?:\.ics\b|webcal://|[?&]ical=1|calendar\.google\.com/calendar/(?:embed|ical))[^"']*)["']""", re.I)
PLUGINS_WP = {"eventon": "ajde_events", "modern-events-calendar": "mec-events", "mec-events": "mec-events"}
MAX_EVENTOS = 80


def get_json(url):
    try:
        req = urllib.request.Request(url, headers={"user-agent": "Mozilla/5.0 (PitWall buscador de carreras; +https://www.pitwall.es)"})
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except Exception:
        return None


def fecha_suelta(s):
    """Fecha de un texto ISO aunque venga sin ceros ("2026-9-18T00:00+2:00") o en formato iCal (20261016T180000Z)."""
    m = re.search(r"(\d{4})-(\d{1,2})-(\d{1,2})", s or "") or re.match(r"(\d{4})(\d{2})(\d{2})", s or "")
    try:
        return dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3))) if m else None
    except ValueError:
        return None


def evento(ini, fin, nombre, url, lugar=""):
    f1 = fecha_suelta(str(ini or ""))
    if not f1:
        return None
    return {"fecha": f1, "fin": fecha_suelta(str(fin or "")), "nombre": html_a_texto(str(nombre or ""))[:120],
            "url": url, "lugar": html_a_texto(str(lugar or ""))[:80]}


def eventos_html(html, url):
    """Eventos schema.org de una página: JSON-LD y, si no hay, microdatos (itemprop="startDate")."""
    out = []
    for bloque in re.findall(r"<script[^>]+application/ld\+json[^>]*>(.*?)</script>", html, re.S | re.I):
        try:
            pila = [json.loads(bloque.strip())]
        except ValueError:
            continue
        while pila:
            x = pila.pop()
            if isinstance(x, list):
                pila.extend(x)
            elif isinstance(x, dict):
                pila.extend(v for k, v in x.items() if k in ("@graph", "itemListElement", "item", "subEvent"))
                tipos = x.get("@type") if isinstance(x.get("@type"), list) else [x.get("@type")]
                if x.get("startDate") and any("Event" in str(t) for t in tipos):
                    lugar = x.get("location")
                    if isinstance(lugar, list):
                        lugar = lugar[0] if lugar else ""
                    if isinstance(lugar, dict):
                        lugar = lugar.get("name") or ""
                    out.append(evento(x.get("startDate"), x.get("endDate"), x.get("name"), x.get("url") or url, lugar))
    if not out:
        titulo = re.search(r"<title[^>]*>(.*?)</title>", html, re.S | re.I)
        for m in re.finditer(r"""itemprop=["']startDate["'][^>]*?(?:content|datetime)=["']([^"']+)|(?:content|datetime)=["']([^"']+)["'][^>]*itemprop=["']startDate""", html, re.I):
            antes = html[max(0, m.start() - 2500):m.start()]
            nombre = re.findall(r"""itemprop=["']name["'][^>]*?(?:content=["']([^"']+)["']|>([^<]{3,120})<)""", antes)
            nombre = next((a or b for a, b in reversed(nombre) if (a or b).strip()), titulo.group(1) if titulo else "")
            out.append(evento(m.group(1) or m.group(2), None, nombre, url))
    return [e for e in out if e]


def eventos_ics(texto, url):
    out = []
    texto = re.sub(r"\r?\n[ \t]", "", texto)   # líneas plegadas del formato iCal
    for bloque in re.findall(r"BEGIN:VEVENT(.*?)END:VEVENT", texto, re.S):
        campos = {}
        for linea in bloque.splitlines():
            clave, _, valor = linea.partition(":")
            campos.setdefault(clave.split(";")[0].upper(), valor.replace("\\,", ",").replace("\\n", " ").strip())
        out.append(evento(campos.get("DTSTART"), campos.get("DTEND"), campos.get("SUMMARY"), campos.get("URL") or url, campos.get("LOCATION")))
    return [e for e in out if e]


def eventos_estructurados(paginas_html, desde, hasta):
    """Eventos con fecha publicados como datos en la web del club. Devuelve líneas de texto para la IA."""
    eventos, enlaces_ics = [], []
    portada_url, portada = paginas_html[0]
    for url, html in paginas_html:
        eventos += eventos_html(html, url)
        for href in ICS.findall(html):
            href = urllib.parse.urljoin(url, html_mod.unescape(href)).replace("webcal://", "https://")
            if "calendar.google.com/calendar/embed" in href:
                cal = urllib.parse.parse_qs(urllib.parse.urlsplit(href).query).get("src", [""])[0]
                href = f"https://calendar.google.com/calendar/ical/{urllib.parse.quote(cal)}/public/basic.ics" if cal else ""
            if href and href not in enlaces_ics:
                enlaces_ics.append(href)
    for href in enlaces_ics[:2]:
        texto, _ = descargar(href)
        if texto and "BEGIN:VCALENDAR" in texto:
            eventos += eventos_ics(texto, portada_url)
    origen = "{0.scheme}://{0.netloc}".format(urllib.parse.urlsplit(portada_url))
    todo = " ".join(h for _, h in paginas_html).lower()
    if "wp-content" in todo:
        if "tribe-events" in todo or "the-events-calendar" in todo:
            r = get_json(f"{origen}/wp-json/tribe/events/v1/events?per_page=50&start_date={desde.isoformat()}") or {}
            for e in r.get("events") or []:
                eventos.append(evento(e.get("start_date"), e.get("end_date"), e.get("title"), e.get("url"),
                                      (e.get("venue") or {}).get("venue") if isinstance(e.get("venue"), dict) else ""))
        tipo = next((t for marca, t in PLUGINS_WP.items() if marca in todo), None)
        if tipo:   # EventON / MEC: la lista sale de la API de WordPress y la fecha de la página de cada evento
            for e in (get_json(f"{origen}/wp-json/wp/v2/{tipo}?per_page=40&_fields=link,title") or [])[:40]:
                h, f = descargar(e.get("link") or "")
                if h:
                    for ev in eventos_html(h, f):
                        ev["nombre"] = ev["nombre"] or html_a_texto((e.get("title") or {}).get("rendered", ""))
                        eventos.append(ev)
    vistos, lineas = set(), []
    for e in sorted((e for e in eventos if e and desde <= e["fecha"] <= hasta), key=lambda e: e["fecha"]):
        clave = (e["fecha"], slug(e["nombre"]))
        if clave in vistos or not e["nombre"]:
            continue
        vistos.add(clave)
        fechas = e["fecha"].isoformat() + (f"–{e['fin'].isoformat()}" if e["fin"] and e["fin"] > e["fecha"] else "")
        lineas.append(" | ".join((fechas, e["nombre"], e["lugar"], e["url"])))
    return lineas[:MAX_EVENTOS]


def paginas_club(club, desde, hasta):
    """Portada + páginas de calendario/agenda/eventos del mismo dominio.
    Devuelve ([(url, texto)], [líneas de eventos estructurados])."""
    html, final = descargar(club["web"])
    if not html or len(html_a_texto(html)) < 300:
        # web hecha con JavaScript (o que no deja descargar): solo entonces se gasta un crédito de Tavily
        if not os.environ.get("TAVILY_API_KEY"):
            return []
        url = club.get("calendario") or club["web"]
        res = tavily("extract", {"urls": [url]}).get("results") or []
        texto = (res[0].get("raw_content") or "") if res else ""
        return ([(url, texto)] if texto else []), []
    d = dominio(final)
    vistas = {final.rstrip("/")}
    candidatas = []
    if club.get("calendario") and club["calendario"].rstrip("/") not in vistas:
        candidatas.append(club["calendario"])
    for href, texto in re.findall(r"""<a\b[^>]*href=["']([^"'#]+)["'][^>]*>(.*?)</a>""", html, re.S | re.I):
        url = urllib.parse.urljoin(final, html_mod.unescape(href.strip()))
        etiqueta = html_a_texto(texto)[:60]
        if (re.match(r"https?://", url) and dominio(url) == d and not url.lower().endswith((".pdf", ".jpg", ".png"))
                and CALENDARIO.search(url + " " + etiqueta) and url.rstrip("/") not in vistas
                and url not in candidatas):
            candidatas.append(url)
    paginas_html = [(final, html)]
    for url in candidatas[:3]:
        h, f = descargar(url)
        if h:
            paginas_html.append((f, h))
    try:
        eventos = eventos_estructurados(paginas_html, desde, hasta)
    except Exception as e:   # que un calendario raro no impida leer el texto de la web
        log(f"  calendario estructurado: {e}")
        eventos = []
    return [(u, html_a_texto(h)) for u, h in paginas_html], eventos


def carreras_de_club(preguntar, club, desde, hasta):
    """Carreras de un club: con el texto de su web si se puede descargar; si no, dejando que la IA la busque."""
    nombre = club.get("nombre") or dominio(club["web"])
    sitio = ", ".join(x for x in (club.get("ciudad"), club.get("pais")) if x)
    encargo = (f"club de slot «{nombre}»" + (f" ({sitio})" if sitio else "")
               + f". Extrae las carreras de slot con fecha entre el {desde.isoformat()} y el {hasta.isoformat()}. "
               "En 'club' pon el nombre del club. Incluye pruebas de campeonatos, trofeos, resistencias y carreras abiertas; "
               "no incluyas entrenamientos libres, horarios de apertura ni sesiones sociales sin competición.")
    paginas, eventos = paginas_club(club, desde, hasta)
    años = (str(desde.year), str(hasta.year), str(dt.date.today().year))
    texto, total = [], 0
    if eventos:
        log(f"  {len(eventos)} eventos en el calendario de la web")
        bloque = "\n".join(eventos)
        texto.append("### Eventos con fecha publicados en el calendario de la web (fecha | título | lugar | enlace)\n"
                     "Usa la fecha y el enlace de cada línea tal cual. Si el título es solo una categoría (p. ej. «F1» o «GT»), "
                     f"llama a la carrera «Carrera de club: <categoría>».\n{bloque}")
        total += len(bloque)
    for url, t in paginas:
        if not any(a in t for a in años):
            continue
        trozo = t[:min(15000, MAX_TEXTO_CLUB - total)]
        texto.append(f"### {url}\n{trozo}")
        total += len(trozo)
    if texto:
        prompt = (f"Este es el texto de la web del {encargo} En 'enlace' pon la URL donde aparece la fecha "
                  "(la de la línea del evento o la de la página que empieza por ###).\n\n" + "\n\n".join(texto))
        buscar = False
    elif paginas:
        return []   # nada de este año ni del siguiente: ni se pregunta a la IA
    elif PROVEEDOR == "claude":
        urls = ", ".join(u for u in (club["web"], club.get("calendario")) if u)
        prompt = f"Busca la web del {encargo} Su web es {urls}; en 'enlace' pon la URL donde viste la fecha."
        buscar = True
    else:
        raise RuntimeError("web no accesible")
    respuesta, _ = preguntar(prompt, buscar=buscar)
    brutas = extraer_json(respuesta)
    for c in brutas:
        if isinstance(c, dict):
            c.setdefault("club", club.get("nombre"))
            if not c.get("pais") and club.get("pais"):
                c["pais"] = club["pais"]
            if not c.get("ciudad") and club.get("ciudad"):
                c["ciudad"] = club["ciudad"]
    return brutas


def extraer_json(texto):
    m = re.search(r"<json>\s*(.*?)\s*</json>", texto, re.S)
    crudo = m.group(1) if m else texto
    crudo = re.sub(r"^```(?:json)?|```$", "", crudo.strip(), flags=re.M).strip()
    if not crudo.startswith("["):  # a veces el modelo escribe texto alrededor: nos quedamos con el array
        i, j = crudo.find("["), crudo.rfind("]")
        if i < 0 or j < i:
            raise ValueError("la respuesta no trae un array JSON: " + texto[:200].replace("\n", " "))
        crudo = crudo[i:j + 1]
    datos = json.loads(crudo)
    if not isinstance(datos, list):
        raise ValueError("la respuesta no es un array")
    return datos


def slug(s):
    s = unicodedata.normalize("NFD", str(s or "")).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def fecha(s):
    try:
        return dt.date.fromisoformat(str(s))
    except (TypeError, ValueError):
        return None


def limpiar(c, desde, hasta):
    """Valida una carrera de la IA. Devuelve el dict limpio o None si no es aprovechable."""
    if not isinstance(c, dict):
        return None
    f1, f2 = fecha(c.get("fecha")), fecha(c.get("fecha_fin"))
    nombre = (c.get("nombre") or "").strip()
    enlace = (c.get("enlace") or "").strip()
    pais = (c.get("pais") or "").strip().upper()
    if not f1 or not nombre or not re.match(r"https?://", enlace):
        return None
    if f1 < desde or f1 > hasta:
        return None
    if pais and pais not in EUROPA:
        return None
    if f2 and (f2 < f1 or (f2 - f1).days > 10):
        f2 = None
    out = {"fecha": f1.isoformat()}
    if f2 and f2 != f1:
        out["fecha_fin"] = f2.isoformat()
    out["nombre"] = nombre[:140]
    for k in ("campeonato", "club", "circuito", "ciudad", "escala", "categoria", "notas"):
        v = c.get(k)
        if isinstance(v, str) and v.strip() and v.strip().lower() not in ("null", "none", "n/a"):
            out[k] = v.strip()[:200]
    if "campeonato" in out:  # "Resisbarna 2026" → "Resisbarna", para que el filtro no cambie cada temporada
        out["campeonato"] = re.sub(r"\s*[-–(]?\s*(temporada\s+)?20\d\d(\s*[/-]\s*(20)?\d\d)?\s*\)?\s*$", "", out["campeonato"], flags=re.I) or out["campeonato"]
    if out.get("circuito") and out.get("circuito") == out.get("club"):
        del out["circuito"]
    tipo = str(c.get("tipo") or "").strip().lower()
    out["tipo"] = tipo if tipo in TIPOS else "otro"
    if pais:
        out["pais"] = pais
    out["enlace"] = enlace
    out["id"] = "-".join(p for p in (slug(out.get("campeonato") or nombre), out["fecha"], slug(out.get("ciudad") or out.get("club"))) if p)
    return out


def escribir_atomico(ruta, datos):
    os.makedirs(os.path.dirname(os.path.abspath(ruta)), exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(os.path.abspath(ruta)), suffix=".tmp")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=1)
    os.chmod(tmp, 0o644)
    os.replace(tmp, ruta)


def log(msg):
    print(msg, flush=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--salida", help="ruta de carreras-auto.json (obligatoria salvo con --solo-clubes)")
    ap.add_argument("--meses", type=int, default=12, help="meses hacia delante a buscar (12)")
    ap.add_argument("--max-lotes", type=int, default=0, help="limitar nº de búsquedas, para pruebas")
    ap.add_argument("--estado", help="fichero JSON con los clubes conocidos (sin él no se miran clubes)")
    ap.add_argument("--sin-clubes", action="store_true", help="no mirar las webs de los clubes")
    ap.add_argument("--solo-clubes", action="store_true", help="no mirar los campeonatos, solo los clubes")
    ap.add_argument("--descubrir-clubes", action="store_true", help="buscar clubes nuevos aunque no toque este mes")
    ap.add_argument("--max-clubes", type=int, default=250, help="máximo de webs de clubes a visitar (250)")
    args = ap.parse_args()

    if not args.salida and not args.solo_clubes:
        ap.error("--salida es obligatorio (solo se puede omitir con --solo-clubes)")
    if args.solo_clubes and not args.estado:
        ap.error("--solo-clubes necesita --estado")
    if args.sin_clubes and args.solo_clubes:
        ap.error("--sin-clubes y --solo-clubes se contradicen")

    if PROVEEDOR not in CLAVES:
        sys.exit(f"PITWALL_PROVEEDOR debe ser deepseek o claude, no {PROVEEDOR!r}")
    faltan = [k for k in CLAVES[PROVEEDOR] if not os.environ.get(k)]
    if faltan:
        sys.exit("Faltan variables de entorno: " + ", ".join(faltan))
    preguntar = preguntar_deepseek if PROVEEDOR == "deepseek" else preguntar_claude

    hoy = dt.date.today()
    desde = hoy - dt.timedelta(days=30)          # conserva lo del último mes para "mostrar pasadas"
    hasta = hoy + dt.timedelta(days=31 * args.meses)
    lotes = construir_lotes(desde, hasta)
    if args.max_lotes:
        lotes = lotes[:args.max_lotes]
    if args.solo_clubes:
        lotes = []

    encontradas, fallos, total_busquedas = {}, 0, 0

    def guardar(brutas):
        validas = [c for c in (limpiar(x, desde, hasta) for x in brutas) if c]
        for c in validas:
            previa = encontradas.get(c["id"])
            if not previa or len(c) > len(previa):   # entre duplicados, la más completa
                encontradas[c["id"]] = c
        return validas

    for i, (titulo, prompt) in enumerate(lotes, 1):
        log(f"[{i}/{len(lotes)}] {titulo}")
        try:
            texto, n = preguntar(prompt)
            total_busquedas += n
            brutas = extraer_json(texto)
        except Exception as e:  # un lote fallido no debe tumbar el resto
            fallos += 1
            log(f"  ERROR: {e}")
            continue
        validas = guardar(brutas)
        log(f"  {len(validas)} válidas de {len(brutas)} ({n} búsquedas)")

    if fallos > len(lotes) / 2:
        sys.exit(f"Han fallado {fallos} de {len(lotes)} lotes: no se sobrescribe {args.salida}")

    clubes_vistos = carreras_clubes = 0
    if args.estado and not args.sin_clubes:
        estado = cargar_estado(args.estado)
        for c in leer_clubes_semilla():
            anadir_club(estado, c, "manual")
        ultimo = fecha(estado.get("ultimo_descubrimiento"))
        if args.descubrir_clubes or not ultimo or (hoy - ultimo).days >= 28:
            nuevos, n = descubrir_clubes(preguntar, estado)
            total_busquedas += n
            log(f"Clubes nuevos: {nuevos} ({n} búsquedas) · en total {len(estado['clubes'])}")
            escribir_atomico(args.estado, estado)
        # primero los que hace más tiempo que no se visitan; los que fallan muchas veces seguidas se dejan de mirar
        cola = sorted((c for c in estado["clubes"].values() if c.get("fallos", 0) < 4),
                      key=lambda c: c.get("visto", ""))[:args.max_clubes]
        for i, club in enumerate(cola, 1):
            log(f"[club {i}/{len(cola)}] {club.get('nombre') or club['web']}")
            try:
                brutas = carreras_de_club(preguntar, club, desde, hasta)
                club["fallos"] = 0
            except Exception as e:
                club["fallos"] = club.get("fallos", 0) + 1
                log(f"  ERROR: {e}")
                brutas = []
            club["visto"] = hoy.isoformat()
            validas = guardar(brutas)
            club["carreras"] = len(validas)
            clubes_vistos += 1
            carreras_clubes += len(validas)
            if validas:
                log(f"  {len(validas)} carreras")
        escribir_atomico(args.estado, estado)

    carreras = sorted(encontradas.values(), key=lambda c: (c["fecha"], c["nombre"]))
    if args.salida:
        escribir_atomico(args.salida, {
            "generado": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
            "modelo": f"{PROVEEDOR}/{MODELO}",
            "busquedas_web": total_busquedas,
            "lotes_fallidos": fallos,
            "clubes_visitados": clubes_vistos,
            "carreras_de_clubes": carreras_clubes,
            "carreras": carreras,
        })
    log(f"OK: {len(carreras)} carreras"
        + (f" en {args.salida}" if args.salida else " (solo prueba, no se escribe el JSON)")
        + f" ({total_busquedas} búsquedas web, {fallos} lotes fallidos, "
        f"{clubes_vistos} clubes visitados con {carreras_clubes} carreras)")


if __name__ == "__main__":
    main()
