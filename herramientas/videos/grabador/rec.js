// Grabador de tomas: Chrome headless por CDP (WebSocket nativo de Node), screencast a 1920x1080,
// cursor dibujado, y montaje de los fotogramas en un .mp4 con sus tiempos reales.
const { spawn, execFileSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const sleep = ms => new Promise(r => setTimeout(r, ms));

const CURSOR_JS = `(() => {
  if (window.__pwc) return; window.__pwc = 1;
  const mk = () => {
    if (document.getElementById('__pwcur')) return;
    const c = document.createElement('div'); c.id = '__pwcur';
    c.innerHTML = '<svg width="34" height="34" viewBox="0 0 24 24"><path d="M4 2l15 11-6.5 1 3.8 7.2-2.6 1.3-3.7-7.3L4 20z" fill="#fff" stroke="#000" stroke-width="1.3" stroke-linejoin="round"/></svg><span></span>';
    c.style.cssText = 'position:fixed;left:0;top:0;z-index:2147483647;pointer-events:none;transform:translate(-4px,-2px);';
    const r = c.querySelector('span');
    r.style.cssText = 'position:absolute;left:-14px;top:-16px;width:36px;height:36px;border-radius:50%;border:3px solid #F0404C;opacity:0;transform:scale(.4);transition:opacity .35s,transform .35s;';
    document.documentElement.appendChild(c);
    let p = null; try { p = JSON.parse(sessionStorage.getItem('__pwcur')); } catch (e) {}
    if (p) { c.style.left = p.x + 'px'; c.style.top = p.y + 'px'; }
  };
  const place = (x, y) => { const c = document.getElementById('__pwcur'); if (!c) return; c.style.left = x + 'px'; c.style.top = y + 'px'; try { sessionStorage.setItem('__pwcur', JSON.stringify({ x, y })); } catch (e) {} };
  addEventListener('mousemove', e => place(e.clientX, e.clientY), true);
  addEventListener('mousedown', e => { place(e.clientX, e.clientY); const r = document.querySelector('#__pwcur span'); if (!r) return; r.style.transition = 'none'; r.style.opacity = '1'; r.style.transform = 'scale(.4)'; requestAnimationFrame(() => { r.style.transition = 'opacity .45s,transform .45s'; r.style.opacity = '0'; r.style.transform = 'scale(1.6)'; }); }, true);
  if (document.readyState === 'loading') addEventListener('DOMContentLoaded', mk); else mk();
  setInterval(mk, 300);
})();`;

const SC = `(() => { const m = document.querySelector('main.main-content'); return (m && m.scrollHeight > m.clientHeight + 2) ? m : document.scrollingElement; })()`;
class Rec {
  constructor(dir) { this.dir = dir; this.frames = []; this.id = 0; this.cbs = new Map(); this.mouse = { x: 960, y: 540 }; }

  async start() {
    fs.rmSync(this.dir, { recursive: true, force: true });
    fs.mkdirSync(path.join(this.dir, 'f'), { recursive: true });
    const prof = path.join(this.dir, 'chrome');
    this.proc = spawn(CHROME, ['--headless=new', '--remote-debugging-port=9333', `--user-data-dir=${prof}`,
      '--window-size=1920,1080', '--hide-scrollbars', '--force-device-scale-factor=1', '--no-first-run',
      '--lang=es-ES', '--disable-features=Translate', 'about:blank'], { stdio: 'ignore' });
    let tabs;
    for (let i = 0; i < 50; i++) { try { tabs = await (await fetch('http://127.0.0.1:9333/json')).json(); break; } catch (e) { await sleep(200); } }
    const page = tabs.find(t => t.type === 'page');
    this.ws = new WebSocket(page.webSocketDebuggerUrl);
    await new Promise(r => this.ws.addEventListener('open', r));
    this.ws.addEventListener('message', ev => this._msg(JSON.parse(ev.data)));
    await this.send('Page.enable');
    await this.send('Runtime.enable');
    await this.send('Emulation.setDeviceMetricsOverride', { width: 1920, height: 1080, deviceScaleFactor: 1, mobile: false });
    await this.send('Page.addScriptToEvaluateOnNewDocument', { source: CURSOR_JS });
    await this.send('Page.setLifecycleEventsEnabled', { enabled: true });
  }

  _msg(m) {
    if (m.id && this.cbs.has(m.id)) { const { res, rej } = this.cbs.get(m.id); this.cbs.delete(m.id); m.error ? rej(new Error(JSON.stringify(m.error))) : res(m.result); return; }
    if (m.method === 'Page.screencastFrame') {
      const { data, metadata, sessionId } = m.params;
      this.send('Page.screencastFrameAck', { sessionId }).catch(() => {});
      if (!this.recording) return;
      const f = path.join(this.dir, 'f', String(this.frames.length).padStart(6, '0') + '.jpg');
      fs.writeFileSync(f, Buffer.from(data, 'base64'));
      this.frames.push({ f, t: metadata.timestamp });
    }
    if (m.method === 'Page.loadEventFired') this._loaded = true;
    if (m.method === 'Input.dragIntercepted') this._drag = m.params.data;
  }

  send(method, params = {}) {
    const id = ++this.id;
    this.ws.send(JSON.stringify({ id, method, params }));
    return new Promise((res, rej) => this.cbs.set(id, { res, rej }));
  }

  async go(url) {
    this._loaded = false;
    await this.send('Page.navigate', { url });
    for (let i = 0; i < 100 && !this._loaded; i++) await sleep(100);
    await sleep(500);
    await this.move(this.mouse.x, this.mouse.y, 1);
  }

  async waitNav(ms = 8000) {
    for (let i = 0; i < ms / 100 && !this._loaded; i++) await sleep(100);
    await sleep(400);
    await this.move(this.mouse.x, this.mouse.y, 1);
  }

  async eval(expr) {
    const r = await this.send('Runtime.evaluate', { expression: expr, awaitPromise: true, returnByValue: true });
    if (r.exceptionDetails) throw new Error('eval: ' + JSON.stringify(r.exceptionDetails).slice(0, 400));
    return r.result.value;
  }

  // Centro del elemento: selector CSS o {text, sel}
  async box(target) {
    const js = typeof target === 'string'
      ? `(() => { const e = document.querySelector(${JSON.stringify(target)}); if (!e) return null; const r = e.getBoundingClientRect(); return {x:r.x+r.width/2, y:r.y+r.height/2, w:r.width, h:r.height}; })()`
      : `(() => { const els = [...document.querySelectorAll(${JSON.stringify(target.sel || 'button,a,label,[role=option],input')})].filter(e => e.offsetParent !== null && e.textContent.trim().replace(/\\s+/g,' ').includes(${JSON.stringify(target.text)})); const e = els[${target.n || 0}]; if (!e) return null; const r = e.getBoundingClientRect(); return {x:r.x+r.width/2, y:r.y+r.height/2, w:r.width, h:r.height}; })()`;
    let b = await this.eval(js);
    if (!b) throw new Error('no encontrado: ' + JSON.stringify(target));
    if (b.y + b.h / 2 > 860 || b.y - b.h / 2 < 90) {
      const sy = await this.eval(SC + '.scrollTop');
      await this.scrollTo(Math.max(0, sy + b.y - 480), 700);
      await sleep(150);
      b = await this.eval(js);
    }
    return b;
  }

  async move(x, y, steps = 22) {
    const a = { ...this.mouse };
    for (let i = 1; i <= steps; i++) {
      const k = i / steps, e = k < .5 ? 2 * k * k : 1 - Math.pow(-2 * k + 2, 2) / 2;
      await this.send('Input.dispatchMouseEvent', { type: 'mouseMoved', x: a.x + (x - a.x) * e, y: a.y + (y - a.y) * e });
      await sleep(16);
    }
    this.mouse = { x, y };
  }

  async click(target, { pause = 250, steps } = {}) {
    this._loaded = false;
    const b = await this.box(target);
    await this.move(b.x, b.y, steps);
    await sleep(pause);
    await this.send('Input.dispatchMouseEvent', { type: 'mousePressed', x: b.x, y: b.y, button: 'left', clickCount: 1 });
    await sleep(70);
    await this.send('Input.dispatchMouseEvent', { type: 'mouseReleased', x: b.x, y: b.y, button: 'left', clickCount: 1 });
    await sleep(200);
  }

  // Arrastre HTML5 real: CDP intercepta el drag y lo reenvía con dispatchDragEvent.
  // Un clon del elemento sigue al puntero (el «fantasma» del sistema no sale en headless).
  async drag(src, dst, { steps = 34 } = {}) {
    const a = await this.box(src);
    await this.move(a.x, a.y);
    await sleep(250);
    await this.send('Input.setInterceptDrags', { enabled: true });
    this._drag = null;
    await this.send('Input.dispatchMouseEvent', { type: 'mousePressed', x: a.x, y: a.y, button: 'left', clickCount: 1 });
    for (let i = 1; i <= 6 && !this._drag; i++) { await this.send('Input.dispatchMouseEvent', { type: 'mouseMoved', x: a.x + i * 3, y: a.y + i * 2, button: 'left', buttons: 1 }); await sleep(30); }
    for (let i = 0; i < 30 && !this._drag; i++) await sleep(30);
    if (!this._drag) throw new Error('el arrastre no arrancó');
    const ghostSel = typeof src === 'string' ? src : null;
    await this.eval(`(() => { const g = document.createElement('div'); g.id='__pwghost'; const lab = ${JSON.stringify(typeof src === 'string' ? '' : src.text)}; g.textContent = lab; g.style.cssText='position:fixed;z-index:2147483646;pointer-events:none;padding:12px 18px;border-radius:10px;background:#1c1f27;border:1.5px solid #ef4651;color:#fff;font:600 19px Saira,sans-serif;box-shadow:0 18px 40px -10px rgba(0,0,0,.8);opacity:.95;transform:translate(14px,10px)'; document.documentElement.appendChild(g); })()`);
    const b = await this.box(dst);
    const from = { x: a.x + 18, y: a.y + 12 };
    await this.send('Input.dispatchDragEvent', { type: 'dragEnter', x: from.x, y: from.y, data: this._drag });
    for (let i = 1; i <= steps; i++) {
      const k = i / steps, e = k < .5 ? 2 * k * k : 1 - Math.pow(-2 * k + 2, 2) / 2;
      const x = from.x + (b.x - from.x) * e, y = from.y + (b.y - from.y) * e;
      await this.send('Input.dispatchDragEvent', { type: 'dragOver', x, y, data: this._drag });
      await this.eval(`(() => { const c = document.getElementById('__pwcur'); if (c) { c.style.left='${x}px'; c.style.top='${y}px'; } const g = document.getElementById('__pwghost'); if (g) { g.style.left='${x}px'; g.style.top='${y}px'; } })()`);
      await sleep(18);
    }
    await sleep(250);
    await this.send('Input.dispatchDragEvent', { type: 'drop', x: b.x, y: b.y, data: this._drag });
    await this.send('Input.dispatchMouseEvent', { type: 'mouseReleased', x: b.x, y: b.y, button: 'left', clickCount: 1 });
    await this.eval(`document.getElementById('__pwghost')?.remove()`);
    await this.send('Input.setInterceptDrags', { enabled: false });
    this.mouse = { x: b.x, y: b.y };
    await this.move(b.x + 1, b.y, 1);
    await sleep(250);
  }

  async type(text, delay = 85) {
    for (const ch of text) { await this.send('Input.insertText', { text: ch }); await sleep(delay + Math.random() * 40); }
  }

  async key(key, code, keyCode) {
    await this.send('Input.dispatchKeyEvent', { type: 'rawKeyDown', key, code, windowsVirtualKeyCode: keyCode });
    await this.send('Input.dispatchKeyEvent', { type: 'keyUp', key, code, windowsVirtualKeyCode: keyCode });
    await sleep(150);
  }

  async scrollTo(y, ms = 900) {
    const from = await this.eval(SC + '.scrollTop');
    const n = Math.max(1, Math.round(ms / 16));
    for (let i = 1; i <= n; i++) { const k = i / n, e = k < .5 ? 2 * k * k : 1 - Math.pow(-2 * k + 2, 2) / 2; await this.eval(SC + `.scrollTop = ${from + (y - from) * e}`); await sleep(16); }
  }
  async scrollToEl(sel, offset = 120, ms = 1200) {
    const y = await this.eval(`(() => { const sc = ${SC}; const e = document.querySelector(${JSON.stringify(sel)}); if (!e) return null; const top = sc === document.scrollingElement ? 0 : sc.getBoundingClientRect().top; return Math.max(0, e.getBoundingClientRect().top - top + sc.scrollTop - ${offset}); })()`);
    if (y != null) await this.scrollTo(y, ms);
  }

  async shot(file) { const r = await this.send('Page.captureScreenshot', { format: 'png' }); fs.writeFileSync(file, Buffer.from(r.data, 'base64')); }

  async recStart() {
    this.recording = true;
    await this.send('Page.startScreencast', { format: 'jpeg', quality: 92, maxWidth: 1920, maxHeight: 1080, everyNthFrame: 1 });
    this.t0 = Date.now();
    // Un fotograma de arranque aunque no cambie nada en pantalla
    await this.move(this.mouse.x + 1, this.mouse.y, 1);
  }

  mark(label) { (this.marks = this.marks || []).push({ label, s: (Date.now() - this.t0) / 1000 }); console.log('  marca', label, ((Date.now() - this.t0) / 1000).toFixed(1)); }

  async recStop(out) {
    await sleep(600);
    await this.move(this.mouse.x + 1, this.mouse.y, 1);
    await sleep(300);
    await this.send('Page.stopScreencast');
    this.recording = false;
    const fr = this.frames;
    const lines = [];
    for (let i = 0; i < fr.length; i++) {
      const d = i < fr.length - 1 ? Math.max(0.001, fr[i + 1].t - fr[i].t) : 1;
      lines.push(`file '${fr[i].f}'`, `duration ${d.toFixed(4)}`);
    }
    lines.push(`file '${fr[fr.length - 1].f}'`);
    const list = path.join(this.dir, 'frames.txt');
    fs.writeFileSync(list, lines.join('\n'));
    execFileSync('ffmpeg', ['-hide_banner', '-loglevel', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', list,
      '-vf', 'scale=1920:1080,fps=30,format=yuv420p', '-c:v', 'libx264', '-preset', 'medium', '-crf', '16', out], { stdio: 'inherit' });
    fs.writeFileSync(out.replace(/\.mp4$/, '.marcas.json'), JSON.stringify(this.marks || [], null, 1));
    const offset = fr.length ? 0 : 0;
    console.log('toma →', out, fr.length, 'fotogramas', offset);
  }

  async close() { try { this.ws.close(); } catch (e) {} try { this.proc.kill(); } catch (e) {} }
}

module.exports = { Rec, sleep };
