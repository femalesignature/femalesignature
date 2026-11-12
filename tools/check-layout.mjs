// Prüft eine Seite in mehreren Breiten über das Chrome-DevTools-Protokoll.
//   node --experimental-websocket tools/check-layout.mjs http://localhost:3004/ [ausgabeordner]
// Meldet horizontales Überlaufen, zu kleine Tippziele und Bilder ohne Maße,
// und speichert pro Breite eine ganzseitige Aufnahme (PNG).
import { spawn } from 'node:child_process';
import { mkdirSync, writeFileSync } from 'node:fs';

const url = process.argv[2] || 'http://localhost:3004/';
const out = process.argv[3] || '/tmp/fs-layout';
const widths = [320, 360, 390, 414, 768, 1024, 1440, 1920];
mkdirSync(out, { recursive: true });

const chrome = spawn('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  ['--headless=new', '--remote-debugging-port=9333', '--hide-scrollbars', '--user-data-dir=/tmp/fs-chrome', 'about:blank'], { stdio: 'ignore' });
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
let target;
for (let i = 0; i < 50 && !target; i++) {
  await sleep(200);
  try { target = (await (await fetch('http://127.0.0.1:9333/json')).json()).find((t) => t.type === 'page'); } catch {}
}
const ws = new WebSocket(target.webSocketDebuggerUrl);
await new Promise((r) => ws.addEventListener('open', r));
let id = 0; const pending = new Map();
ws.addEventListener('message', (e) => { const m = JSON.parse(e.data); if (m.id && pending.has(m.id)) { pending.get(m.id)(m); pending.delete(m.id); } });
const send = (method, params = {}) => new Promise((r) => { const i = ++id; pending.set(i, r); ws.send(JSON.stringify({ id: i, method, params })); });
const evaluate = async (expr) => (await send('Runtime.evaluate', { expression: expr, returnByValue: true, awaitPromise: true })).result.result.value;

await send('Page.enable');
let fails = 0;
for (const w of widths) {
  const mobile = w < 768;
  await send('Emulation.setDeviceMetricsOverride', { width: w, height: mobile ? 800 : 900, deviceScaleFactor: 1, mobile });
  await send('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-reduced-motion', value: 'reduce' }] });
  await send('Page.navigate', { url });
  await sleep(1500);
  const r = await evaluate(`(() => {
    const vw = document.documentElement.clientWidth;
    const over = [...document.querySelectorAll('body *')].filter(el => {
      const b = el.getBoundingClientRect(); if (!b.width || el.closest('.hp,.skip')) return false;
      let p = el.parentElement, clipped = false;
      while (p && p !== document.body) { const s = getComputedStyle(p); if (/(hidden|auto|scroll|clip)/.test(s.overflowX)) { clipped = true; break; } p = p.parentElement; }
      return !clipped && getComputedStyle(el).position !== 'fixed' && (b.right > vw + 1 || b.left < -1);
    }).slice(0, 8).map(el => el.tagName.toLowerCase() + '.' + [...el.classList].join('.') + ' ' + Math.round(el.getBoundingClientRect().right));
    const small = [...document.querySelectorAll('a,button,input,textarea,summary')].filter(el => {
      const b = el.getBoundingClientRect(); const s = getComputedStyle(el);
      if (!b.width || s.visibility === 'hidden' || el.closest('[hidden]') || el.closest('.hp')) return false;
      if (el.closest('p,li,blockquote') && s.display === 'inline') return false;
      return b.height < 44 || b.width < 24;
    }).slice(0, 8).map(el => (el.textContent.trim().slice(0, 30) || el.getAttribute('aria-label') || el.tagName) + ' ' + Math.round(el.getBoundingClientRect().width) + 'x' + Math.round(el.getBoundingClientRect().height));
    const noDim = [...document.images].filter(i => !i.getAttribute('width') || !i.getAttribute('height')).map(i => i.src);
    return { vw, scrollW: document.documentElement.scrollWidth, height: document.documentElement.scrollHeight, over, small, noDim, h1: document.querySelectorAll('h1').length };
  })()`);
  const ok = r.scrollW <= r.vw && !r.over.length && !r.noDim.length && r.h1 === 1;
  if (!ok) fails++;
  console.log(`${String(w).padStart(4)}px  ${ok ? 'OK ' : 'FEHLER'}  Breite ${r.scrollW}/${r.vw}  H1 ${r.h1}` +
    (r.over.length ? `\n      ragt raus: ${r.over.join(' | ')}` : '') +
    (r.small.length ? `\n      Tippziel < 44px: ${r.small.join(' | ')}` : '') +
    (r.noDim.length ? `\n      Bild ohne Maße: ${r.noDim.join(' | ')}` : ''));
  const shot = await send('Page.captureScreenshot', { format: 'png', captureBeyondViewport: true, clip: { x: 0, y: 0, width: w, height: Math.min(r.height, 16000), scale: 1 } });
  writeFileSync(`${out}/${w}.png`, Buffer.from(shot.result.data, 'base64'));
}
ws.close(); chrome.kill();
process.exit(fails ? 1 : 0);
