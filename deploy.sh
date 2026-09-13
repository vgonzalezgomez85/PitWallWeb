#!/bin/bash
# Sincroniza el contenido de este repo con el servidor de casa (LXC pitwall-web)
# y corrige permisos para que Caddy pueda servir los ficheros.
set -euo pipefail
cd "$(dirname "$0")"

rsync -az --delete \
  --exclude '.git' --exclude '.DS_Store' --exclude '.impeccable' --exclude '.vscode' --exclude 'deploy.sh' \
  ./ pitwall-web:/var/www/pitwall/

ssh pitwall-web "chown -R www-data:www-data /var/www/pitwall && chmod -R go+rX /var/www/pitwall"

echo "Desplegado en https://www.pitwall.es"
