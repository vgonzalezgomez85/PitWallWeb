#!/bin/zsh
S=/private/tmp/claude-501/-Users-victor-PitWall/851f0e14-d76b-41f0-8def-ac4284dac30e/scratchpad/video
lsof -tiTCP:3300 -sTCP:LISTEN | xargs kill 2>/dev/null; sleep 1
rm -rf $S/data && mkdir -p $S/data && cp $S/base/pitwall.db $S/data/pitwall.db
cd /Users/victor/PitWall && (PITWALL_DATA=$S/data PORT=3300 PITWALL_NO_AUTOBACKUP=1 PITWALL_DISABLE_PASSWORD=1 nohup node src/app.js > $S/srv.log 2>&1 &)
for i in $(seq 1 20); do curl -s -o /dev/null localhost:3300/ && break; sleep 0.5; done
curl -s -o /dev/null -w "srv %{http_code}\n" localhost:3300/
