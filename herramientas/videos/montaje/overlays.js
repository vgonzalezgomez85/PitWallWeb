// Genera los rótulos (PNG 1920x1080) de una píldora con Chrome headless.
// Uso: node overlays.js <píldora.json> <carpeta-salida>
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');

const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const W = __dirname;
const specFile = process.argv[2], outDir = path.resolve(process.argv[3]);
const spec = JSON.parse(fs.readFileSync(specFile, 'utf8'));
fs.mkdirSync(outDir, { recursive: true });

const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const font = (fam, w, f) => `@font-face{font-family:'${fam}';font-weight:${w};src:url('file://${W}/${f}') format('woff2');}`;
const FONTS = [
  font('Saira Condensed', 800, 'saira-condensed-800-latin.woff2'),
  font('Saira Condensed', 800, 'saira-condensed-800-latin-ext.woff2'),
  font('Inter', 500, 'inter-500-latin.woff2'), font('Inter', 500, 'inter-500-latin-ext.woff2'),
  font('Inter', 700, 'inter-700-latin.woff2'), font('Inter', 700, 'inter-700-latin-ext.woff2'),
].join('');
const RED = '#ef4651';
const base = `${FONTS} *{margin:0;box-sizing:border-box} html,body{width:1920px;height:1080px;overflow:hidden}`;

function card({ kicker, title, sub }) {
  return `<style>${base} body{background:radial-gradient(1200px 700px at 50% 45%,#1a1b20,#050506);color:#fff;font-family:Inter;
    display:flex;flex-direction:column;align-items:center;justify-content:center;gap:34px}
    img{width:380px} .k{font:800 34px 'Saira Condensed';letter-spacing:.18em;color:${RED};text-transform:uppercase}
    h1{font:800 104px/1 'Saira Condensed';letter-spacing:.01em;text-align:center;max-width:1500px}
    p{font:500 34px Inter;color:#aab2bd;text-align:center;max-width:1300px}
    .bar{width:120px;height:6px;background:${RED};border-radius:3px}</style>
    <img src="file://${W}/pitwall-logo.svg"><div class="bar"></div>
    ${kicker ? `<div class="k">${esc(kicker)}</div>` : ''}<h1>${esc(title)}</h1>${sub ? `<p>${esc(sub)}</p>` : ''}`;
}

function caption({ step, total, text, sub, pos }) {
  return `<style>${base} body{background:transparent;font-family:Inter}
    .box{position:absolute;${pos === 'right' ? 'right:64px;bottom:72px;max-width:620px' : `left:64px;${pos === 'top' ? 'top' : 'bottom'}:72px;max-width:1240px`};display:flex;align-items:stretch;
      background:rgba(12,13,16,.92);border-radius:14px;overflow:hidden;box-shadow:0 18px 50px rgba(0,0,0,.55);
      border:1px solid rgba(255,255,255,.08)}
    .n{background:${RED};color:#fff;font:800 44px 'Saira Condensed';padding:0 26px;display:flex;align-items:center}
    .n small{font-size:24px;opacity:.75;margin-left:4px}
    .t{padding:22px 32px 24px} .m{font:700 40px/1.2 Inter;color:#fff}
    .s{font:500 27px/1.35 Inter;color:#b6bec9;margin-top:8px}</style>
    <div class="box">${step ? `<div class="n">${step}<small>/${total}</small></div>` : ''}
    <div class="t"><div class="m">${esc(text)}</div>${sub ? `<div class="s">${esc(sub)}</div>` : ''}</div></div>`;
}

const shots = [];
spec.segments.forEach((s, i) => {
  if (s.card) shots.push({ name: `card-${i}`, html: card(s.card), opaque: true });
  if (s.caption) shots.push({ name: `cap-${i}`, html: caption(s.caption) });
});
for (const sh of shots) {
  const html = path.join(outDir, sh.name + '.html');
  fs.writeFileSync(html, `<!doctype html><html><head><meta charset="utf-8"></head><body>${sh.html}</body></html>`);
  execFileSync(CHROME, ['--headless=new', '--disable-gpu', '--hide-scrollbars', '--force-device-scale-factor=1',
    '--window-size=1920,1080', '--default-background-color=00000000', '--allow-file-access-from-files',
    `--screenshot=${path.join(outDir, sh.name + '.png')}`, 'file://' + html], { stdio: 'ignore' });
}
console.log('rótulos:', shots.map(s => s.name).join(' '));
