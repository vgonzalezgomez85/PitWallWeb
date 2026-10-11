#!/usr/bin/env python3
"""Busca en internet carreras de slot en Europa con IA (DeepSeek + Tavily, o Claude)
y genera datos/carreras-auto.json para el buscador de carreras de pitwall.es.

Pensado para ejecutarse en el servidor una vez por semana (cron o systemd timer).
Solo usa la biblioteca estándar de Python 3.8+.

Uso:
  python3 buscar-carreras.py --salida /var/www/pitwall/datos/carreras-auto.json
  python3 buscar-carreras.py --salida prueba.json --max-lotes 1     # prueba barata

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

def preguntar_claude(prompt):
    """Una conversación con búsqueda web. Devuelve (texto final, nº de búsquedas)."""
    cabeceras = {"x-api-key": os.environ["ANTHROPIC_API_KEY"], "anthropic-version": "2023-06-01"}
    pregunta = {"role": "user", "content": prompt}
    hecho, busquedas = [], 0
    for _ in range(6):
        resp = post_json("https://api.anthropic.com/v1/messages", {
            "model": MODELO,
            "max_tokens": 16000,
            "system": SISTEMA,
            "tools": [{"type": "web_search_20250305", "name": "web_search", "max_uses": 10}],
            "messages": [pregunta] + ([{"role": "assistant", "content": hecho}] if hecho else []),
        }, cabeceras)
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


def leer_pagina(url):
    if not re.match(r"https?://", url or ""):
        return "URL no válida"
    try:  # primero directo, que es gratis
        req = urllib.request.Request(url, headers={"user-agent": "Mozilla/5.0 (PitWall buscador de carreras; +https://www.pitwall.es)"})
        with urllib.request.urlopen(req, timeout=30) as r:
            tipo = r.headers.get("content-type", "")
            if "html" in tipo or "text" in tipo:
                texto = html_a_texto(r.read(3_000_000).decode(r.headers.get_content_charset() or "utf-8", "replace"))
                if len(texto) > 300:
                    return texto[:MAX_TEXTO]
    except Exception:
        pass
    r = tavily("extract", {"urls": [url]})   # PDFs, webs con JavaScript o que bloquean descargas
    res = r.get("results") or []
    return (res[0].get("raw_content") or "")[:MAX_TEXTO] if res else "No se ha podido leer la página."


def preguntar_deepseek(prompt):
    """Bucle de herramientas compatible con la API de OpenAI. Devuelve (texto final, nº de búsquedas)."""
    cabeceras = {"authorization": f"Bearer {os.environ['DEEPSEEK_API_KEY']}"}
    mensajes = [{"role": "system", "content": SISTEMA + f"\nHoy es {dt.date.today().isoformat()}."},
                {"role": "user", "content": prompt}]
    usadas = busquedas = 0
    while True:
        cuerpo = {"model": MODELO, "messages": mensajes, "max_tokens": 8000, "temperature": 0.2}
        if usadas < MAX_HERRAMIENTAS:
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
    ap.add_argument("--salida", required=True, help="ruta de carreras-auto.json")
    ap.add_argument("--meses", type=int, default=12, help="meses hacia delante a buscar (12)")
    ap.add_argument("--max-lotes", type=int, default=0, help="limitar nº de búsquedas, para pruebas")
    args = ap.parse_args()

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

    encontradas, fallos, total_busquedas = {}, 0, 0
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
        validas = [c for c in (limpiar(x, desde, hasta) for x in brutas) if c]
        for c in validas:
            previa = encontradas.get(c["id"])
            if not previa or len(c) > len(previa):   # entre duplicados, la más completa
                encontradas[c["id"]] = c
        log(f"  {len(validas)} válidas de {len(brutas)} ({n} búsquedas)")

    if fallos > len(lotes) / 2:
        sys.exit(f"Han fallado {fallos} de {len(lotes)} lotes: no se sobrescribe {args.salida}")

    carreras = sorted(encontradas.values(), key=lambda c: (c["fecha"], c["nombre"]))
    escribir_atomico(args.salida, {
        "generado": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "modelo": f"{PROVEEDOR}/{MODELO}",
        "busquedas_web": total_busquedas,
        "lotes_fallidos": fallos,
        "carreras": carreras,
    })
    log(f"OK: {len(carreras)} carreras en {args.salida} ({total_busquedas} búsquedas web, {fallos} lotes fallidos)")


if __name__ == "__main__":
    main()
