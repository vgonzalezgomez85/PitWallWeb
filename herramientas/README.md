# Buscador de carreras: búsqueda automática con IA

`buscar-carreras.py` pregunta a una IA por carreras de slot en Europa y escribe
`datos/carreras-auto.json`. La página `carreras*.html` mezcla ese fichero con `datos/carreras-manuales.json`
(las que añades tú, que van en el repo). Esta carpeta no se publica: `deploy.sh` la excluye, y tampoco
toca `datos/carreras-auto.json` del servidor.

- **Campeonatos que se buscan por nombre**: `campeonatos.txt` (uno por línea).
- **Búsquedas abiertas por país** para descubrir campeonatos nuevos: `PAISES_DESCUBRIR` en el script.
- **Clubes de slot** cuya web se revisa cada semana: `clubes.txt` (a mano) más los que descubre la IA.
- **Carreras manuales y ocultar errores de la IA**: `../datos/carreras-manuales.json`.

## Clubes

Además de los campeonatos, el script mantiene una lista de clubes de slot con web propia:

- **Una vez al mes** busca clubes nuevos por país (`PAISES_CLUBES`): 10 lotes con búsqueda web que
  añaden los que no estuvieran. Los que trae la IA se guardan en el fichero de estado (`--estado`;
  en el servidor, `/var/lib/pitwall-carreras/clubes.json`), no en el repo.
- **Cada semana** visita la web de cada club: descarga la portada y hasta tres páginas de
  calendario/agenda/eventos del mismo dominio (gratis, sin gastar Tavily) y le pasa el texto a la IA
  para que saque las carreras. Solo gasta un crédito de Tavily por club si la web es de JavaScript o
  no se puede descargar. Si ninguna página habla del año en curso o del siguiente, ni se pregunta.
- Un club que falla 4 semanas seguidas deja de visitarse. `--max-clubes` limita cuántos se visitan
  por ejecución (250 por defecto, ordenados por el que hace más tiempo que no se mira).
- `clubes.txt` es para los que quieres fijar a mano: `web | nombre | ciudad | país`. Solo la web es
  obligatoria (si la web es directamente el calendario, mejor). Se vuelven a mirar siempre, aunque la
  IA deje de encontrarlos.

Para probar solo los clubes, sin tocar el JSON de carreras:

```bash
python3 buscar-carreras.py --solo-clubes --estado /tmp/clubes.json --max-clubes 5
python3 buscar-carreras.py --solo-clubes --estado /tmp/clubes.json --descubrir-clubes   # fuerza el descubrimiento
```

## IA y buscador

Por defecto usa **DeepSeek** (`deepseek-chat`) como modelo y **Tavily** (tavily.com, 1.000 búsquedas
gratis al mes) como buscador: DeepSeek decide qué buscar y qué páginas leer, y el script ejecuta esas
búsquedas y lecturas por él. También puede usar **Claude**, que busca por sí mismo: pon
`PITWALL_PROVEEDOR=claude` y `ANTHROPIC_API_KEY=...` en el fichero de claves.

## En el servidor (LXC pitwall-web) — ya instalado

- Script: `/opt/pitwall-carreras/` (copia de esta carpeta)
- Claves: `/etc/pitwall-carreras.env` (solo root)
- Temporizador: `pitwall-carreras.timer`, cada lunes a las 5:00 UTC
- Clubes conocidos: `/var/lib/pitwall-carreras/clubes.json` (lo crea systemd con `StateDirectory`;
  está fuera de `/opt` para que el `rsync --delete` de abajo no se lo lleve por delante)
- Resultado: `/var/www/pitwall/datos/carreras-auto.json`

El servicio llama al script así (línea `ExecStart` de `pitwall-carreras.service`):

```
ExecStart=/usr/bin/python3 /opt/pitwall-carreras/buscar-carreras.py --salida /var/www/pitwall/datos/carreras-auto.json --estado /var/lib/pitwall-carreras/clubes.json
```

Poner las claves (edita las líneas `DEEPSEEK_API_KEY=` y `TAVILY_API_KEY=`):

```bash
ssh -t pitwall-web nano /etc/pitwall-carreras.env
```

Prueba barata (un solo lote) y primera ejecución completa:

```bash
ssh pitwall-web 'set -a; . /etc/pitwall-carreras.env; set +a; python3 /opt/pitwall-carreras/buscar-carreras.py --salida /tmp/prueba.json --max-lotes 1 && cat /tmp/prueba.json'
ssh pitwall-web 'systemctl start pitwall-carreras.service; journalctl -u pitwall-carreras.service -n 50 --no-pager'
```

Si cambias `campeonatos.txt`, `clubes.txt` o el script, vuelve a copiarlo:

```bash
rsync -az --delete --exclude .DS_Store herramientas/ pitwall-web:/opt/pitwall-carreras/ && ssh pitwall-web chown -R root:root /opt/pitwall-carreras
```

## Coste

Cada ejecución son unos 18 lotes con hasta 10 búsquedas o lecturas de página cada uno (`MAX_HERRAMIENTAS`).
Con DeepSeek el coste de tokens es muy bajo. En Tavily gastan créditos las búsquedas y las páginas que no
se pueden descargar directamente: en el peor caso unos 180 por ejecución, así que una ejecución semanal
cabe en los 1.000 gratis al mes. El JSON generado apunta cuántas búsquedas se hicieron (`busquedas_web`).

A eso se suman los clubes: cada club visitado es una consulta al modelo (hasta 40.000 caracteres de texto,
`MAX_TEXTO_CLUB`) que no gasta Tavily salvo que la web sea de JavaScript. Los 10 lotes del descubrimiento
mensual sí hacen búsquedas. El JSON apunta cuántos clubes se visitaron (`clubes_visitados`) y cuántas
carreras salieron de ellos (`carreras_de_clubes`).
