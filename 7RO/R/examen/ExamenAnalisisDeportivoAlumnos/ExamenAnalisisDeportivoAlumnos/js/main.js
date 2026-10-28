'use strict';
/* ===== Examen NBA 2K25 · Introducción a R · motor común (profesor y alumnos) ===== */
const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => [...r.querySelectorAll(s)];
const MODE = document.body.dataset.mode || 'a';
const STORE = 'nba2k25_r_' + MODE;
let state = {}; try { state = JSON.parse(localStorage.getItem(STORE) || '{}'); } catch (e) { }
state.reqs = state.reqs || {}; state.medals = state.medals || {}; state.ans = state.ans || {};
const save = () => { try { localStorage.setItem(STORE, JSON.stringify(state)); } catch (e) { } };
const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;

/* ---------- sonido sintetizado (sin ficheros externos) ---------- */
let AC; const actx = () => AC || (AC = new (window.AudioContext || window.webkitAudioContext)());
function tone(f, t0, d, type = 'square', v = .08, f2) {
  try {
    const a = actx(), o = a.createOscillator(), g = a.createGain(); o.type = type; o.frequency.setValueAtTime(f, a.currentTime + t0);
    if (f2) o.frequency.exponentialRampToValueAtTime(f2, a.currentTime + t0 + d);
    g.gain.setValueAtTime(v, a.currentTime + t0); g.gain.exponentialRampToValueAtTime(.0001, a.currentTime + t0 + d);
    o.connect(g).connect(a.destination); o.start(a.currentTime + t0); o.stop(a.currentTime + t0 + d + .05);
  } catch (e) { }
}
function noise(d = .25, v = .12) {
  try {
    const a = actx(), b = a.createBuffer(1, a.sampleRate * d, a.sampleRate), ch = b.getChannelData(0);
    for (let i = 0; i < ch.length; i++) ch[i] = (Math.random() * 2 - 1) * (1 - i / ch.length);
    const s = a.createBufferSource(), f = a.createBiquadFilter(), g = a.createGain(); f.type = 'highpass'; f.frequency.value = 2500; g.gain.value = v;
    s.buffer = b; s.connect(f).connect(g).connect(a.destination); s.start();
  } catch (e) { }
}
const sfx = {
  tick: () => tone(880, 0, .05, 'triangle', .05),
  bounce: () => tone(140, 0, .12, 'sine', .14, 70),
  swish: () => noise(.28, .1),
  ok: () => { tone(660, 0, .1, 'triangle', .07); tone(990, .08, .14, 'triangle', .07); },
  ko: () => tone(180, 0, .18, 'sawtooth', .05),
  medal: () => [523, 659, 784, 1047].forEach((f, i) => tone(f, i * .08, .22, 'triangle', .08)),
  buzzer: () => { tone(220, 0, 1.1, 'sawtooth', .09); tone(223, 0, 1.1, 'square', .05); },
  fanfare: () => [392, 523, 659, 784, 659, 784, 1047].forEach((f, i) => tone(f, i * .12, .3, 'sawtooth', .06))
};

/* ---------- utilidades de dibujo ---------- */
function fitCanvas(c) {
  const dpr = Math.min(2, devicePixelRatio || 1), w = c.clientWidth || 300, h = c.clientHeight || 150;
  if (c.width !== Math.round(w * dpr) || c.height !== Math.round(h * dpr)) { c.width = Math.round(w * dpr); c.height = Math.round(h * dpr); }
  const g = c.getContext('2d'); g.setTransform(dpr, 0, 0, dpr, 0, 0); return { g, w, h };
}
/* Balón dibujado en coordenadas relativas al radio: las costuras siempre quedan dentro y centradas. */
function drawBall(g, x, y, r, rot = 0, squash = 1) {
  g.save(); g.translate(x, y); g.scale(1 / Math.sqrt(squash), squash);
  const gr = g.createRadialGradient(-r * .35, -r * .4, r * .1, 0, 0, r);
  gr.addColorStop(0, '#ffb067'); gr.addColorStop(.55, '#f06a12'); gr.addColorStop(1, '#9c3a05');
  g.fillStyle = gr; g.beginPath(); g.arc(0, 0, r, 0, Math.PI * 2); g.fill();
  g.save(); g.clip(); g.rotate(rot);
  g.strokeStyle = 'rgba(28,14,6,.9)'; g.lineWidth = Math.max(1.2, r * .075); g.lineCap = 'round';
  g.beginPath(); g.moveTo(-r, 0); g.lineTo(r, 0); g.stroke();                 // costura horizontal
  g.beginPath(); g.moveTo(0, -r); g.lineTo(0, r); g.stroke();                 // costura vertical
  g.beginPath(); g.arc(-r * 1.32, 0, r * .98, -Math.PI / 2.4, Math.PI / 2.4); g.stroke(); // costura curva izq.
  g.beginPath(); g.arc(r * 1.32, 0, r * .98, Math.PI - Math.PI / 2.4, Math.PI + Math.PI / 2.4); g.stroke(); // dcha.
  g.restore();
  const hl = g.createRadialGradient(-r * .4, -r * .45, 0, -r * .4, -r * .45, r * .7);
  hl.addColorStop(0, 'rgba(255,255,255,.35)'); hl.addColorStop(1, 'rgba(255,255,255,0)');
  g.fillStyle = hl; g.beginPath(); g.arc(0, 0, r, 0, Math.PI * 2); g.fill();
  g.strokeStyle = 'rgba(60,20,0,.55)'; g.lineWidth = 1; g.stroke();
  g.restore();
}

/* ---------- pabellón del hero: tiro a canasta en canvas ---------- */
(function () {
  const c = $('#court'); if (!c) return; const board = $('#arenaPts');
  let pts = 0, ball, phase = 'idle', T = 0, net = 0, flash = 0, shooter = .2, made = 0, lastFrame = performance.now(), visible = true, popTxt = null;
  new IntersectionObserver(e => visible = e[0].isIntersecting).observe(c);
  function geom(w, h) {
    const floor = h * .86, r = Math.max(9, Math.min(w, h) * .048);
    const rim = { x: w * .78, y: h * .36, rx: r * 1.55, ry: r * .42 };
    return { floor, r, rim };
  }
  function rest(w, h) { const G = geom(w, h); ball = { x: w * .24, y: G.floor - G.r, vx: 0, vy: 0, rot: 0, sq: 1 }; phase = 'idle'; }
  function newShot(w, h) {
    if (phase !== 'idle') return;                    // un tiro cada vez, solo al hacer clic
    const G = geom(w, h); shooter = Math.min(.45, Math.max(.1, ball.x / w));
    ball = { x0: w * shooter, y0: G.floor - G.r * 2.6, x: w * shooter, y: G.floor - G.r * 2.6, vx: 0, vy: 0, rot: ball.rot, sq: 1 };
    T = 0; phase = 'shot';
  }
  function court(g, w, h, G) {
    const sky = g.createLinearGradient(0, 0, 0, h); sky.addColorStop(0, '#0a1222'); sky.addColorStop(.62, '#16233c'); sky.addColorStop(.63, '#7a4a22'); sky.addColorStop(1, '#3b220e');
    g.fillStyle = sky; g.fillRect(0, 0, w, h);
    // focos del pabellón
    for (let i = 0; i < 5; i++) { const x = w * (.1 + i * .2), gr = g.createRadialGradient(x, 0, 0, x, 0, h * .55); gr.addColorStop(0, 'rgba(255,230,190,.16)'); gr.addColorStop(1, 'rgba(255,230,190,0)'); g.fillStyle = gr; g.fillRect(0, 0, w, h * .62); g.fillStyle = 'rgba(255,240,210,.8)'; g.beginPath(); g.arc(x, 8, 3, 0, 7); g.fill(); }
    // grada
    g.fillStyle = 'rgba(255,255,255,.035)'; for (let y = h * .2; y < h * .6; y += 9) for (let x = (y / 9 % 2) * 6; x < w; x += 12) g.fillRect(x, y, 3, 3);
    // parquet en perspectiva
    const top = h * .63; g.save(); g.beginPath(); g.rect(0, top, w, h - top); g.clip();
    for (let i = 0; i < 26; i++) { const t = i / 26; g.fillStyle = i % 2 ? 'rgba(255,210,150,.06)' : 'rgba(0,0,0,.06)'; g.beginPath(); g.moveTo(w * .5 + (t - .5) * w * .7, top); g.lineTo(w * .5 + (t + 1 / 26 - .5) * w * .7, top); g.lineTo(w * .5 + (t + 1 / 26 - .5) * w * 2.6, h); g.lineTo(w * .5 + (t - .5) * w * 2.6, h); g.fill(); }
    g.strokeStyle = 'rgba(255,255,255,.55)'; g.lineWidth = 2;
    g.beginPath(); g.moveTo(0, top + 2); g.lineTo(w, top + 2); g.stroke();
    g.beginPath(); g.ellipse(G.rim.x, top + 4, w * .42, (h - top) * .9, 0, Math.PI * .5, Math.PI * 1.02); g.stroke(); // línea de 3
    g.fillStyle = 'rgba(226,54,75,.28)'; g.beginPath(); g.moveTo(G.rim.x - w * .1, top + 2); g.lineTo(G.rim.x + w * .1, top + 2); g.lineTo(G.rim.x + w * .16, h * .97); g.lineTo(G.rim.x - w * .16, h * .97); g.closePath(); g.fill(); g.stroke(); // zona
    g.restore();
    const refl = g.createLinearGradient(0, top, 0, h); refl.addColorStop(0, 'rgba(255,255,255,.08)'); refl.addColorStop(1, 'rgba(0,0,0,.35)'); g.fillStyle = refl; g.fillRect(0, top, w, h - top);
  }
  function hoopBack(g, G) {
    const { rim, r } = G, bw = rim.rx * 3.1, bh = rim.rx * 2;
    g.fillStyle = '#20283a'; g.fillRect(rim.x + rim.rx * 1.9, rim.y - bh * .2, 6, G.floor - rim.y + bh * .2); // poste
    g.fillStyle = 'rgba(220,235,255,.18)'; g.strokeStyle = '#e8eefb'; g.lineWidth = 3;
    g.beginPath(); g.roundRect ? g.roundRect(rim.x - bw / 2, rim.y - bh * .9, bw, bh, 4) : g.rect(rim.x - bw / 2, rim.y - bh * .9, bw, bh); g.fill(); g.stroke();
    g.strokeStyle = flash > 0 ? `rgba(255,179,71,${.5 + flash})` : '#ff7a1a'; g.lineWidth = 2.5; g.strokeRect(rim.x - rim.rx * .7, rim.y - bh * .55, rim.rx * 1.4, bh * .48);
    g.strokeStyle = '#d9480f'; g.lineWidth = 3; g.beginPath(); g.ellipse(rim.x, rim.y, rim.rx, rim.ry, 0, Math.PI, Math.PI * 2); g.stroke();
  }
  function hoopFront(g, G, t) {
    const { rim } = G, depth = rim.rx * 1.7, sway = Math.sin(t * 22) * net * rim.rx * .12, pinch = 1 - net * .25;
    g.strokeStyle = 'rgba(255,255,255,.8)'; g.lineWidth = 1.2;
    for (let i = 0; i <= 8; i++) {
      const a = Math.PI * i / 8, x1 = rim.x - Math.cos(a) * rim.rx, y1 = rim.y + Math.sin(a) * rim.ry * .2;
      const x2 = rim.x - Math.cos(a) * rim.rx * .55 * pinch + sway, y2 = rim.y + depth * (1 + net * .15);
      g.beginPath(); g.moveTo(x1, y1); g.quadraticCurveTo((x1 + x2) / 2 + sway * .5, (y1 + y2) / 2, x2, y2); g.stroke();
      if (i < 8) { const a2 = Math.PI * (i + 1) / 8; g.beginPath(); g.moveTo((x1 + x2) / 2 + sway * .5, (y1 + y2) / 2); g.lineTo((rim.x - Math.cos(a2) * rim.rx + rim.x - Math.cos(a2) * rim.rx * .55 * pinch + sway) / 2, (y1 + y2) / 2 + 2); g.stroke(); }
    }
    g.strokeStyle = '#ff7a1a'; g.lineWidth = 3.5; g.beginPath(); g.ellipse(rim.x, rim.y, rim.rx, rim.ry, 0, 0, Math.PI); g.stroke();
  }
  function shadow(g, x, floor, y, r) { const k = Math.max(.2, 1 - (floor - y) / 300); g.fillStyle = `rgba(0,0,0,${.35 * k})`; g.beginPath(); g.ellipse(x, floor + r * .15, r * 1.1 * k, r * .28 * k, 0, 0, 7); g.fill(); }
  function step(now) {
    requestAnimationFrame(step);
    const dt = Math.min(.033, (now - lastFrame) / 1000); lastFrame = now; if (!visible) return;
    const { g, w, h } = fitCanvas(c), G = geom(w, h); if (!ball) rest(w, h);
    net = Math.max(0, net - dt * 1.4); flash = Math.max(0, flash - dt * 1.5);
    if (phase === 'idle') { ball.y = G.floor - G.r; ball.x = Math.min(ball.x, w * .6); }
    else if (phase === 'shot') {
      T += dt / 1.15; const t = Math.min(1, T), tx = G.rim.x, ty = G.rim.y - G.r * .6, apex = Math.min(G.rim.y, ball.y0) - h * .28;
      ball.x = ball.x0 + (tx - ball.x0) * t;
      ball.y = (1 - t) * (1 - t) * ball.y0 + 2 * (1 - t) * t * (apex * 2 - (ball.y0 + ty) / 2) + t * t * ty;
      ball.rot -= dt * 9;
      if (t >= 1) { phase = 'drop'; ball.vx = 0; ball.vy = 120; }
    } else if (phase === 'drop' || phase === 'bounce') {
      ball.vy += 1500 * dt; ball.x += ball.vx * dt; ball.y += ball.vy * dt; ball.rot += ball.vx * dt * .05;
      if (phase === 'drop' && ball.y > G.rim.y + G.r * .2 && !ball.scored) { ball.scored = true; net = 1; flash = .5; made++; const three = shooter < .2; pts += three ? 3 : 2; popTxt = { t: 1, v: three ? '+3' : '+2' }; if (board) board.textContent = String(pts).padStart(3, '0'); sfx.swish(); }
      if (ball.y > G.floor - G.r) {
        ball.y = G.floor - G.r; ball.sq = .78; if (Math.abs(ball.vy) > 160) sfx.bounce();
        ball.vy *= -.58; ball.vx = phase === 'drop' ? -(60 + Math.random() * 80) : ball.vx * .9; phase = 'bounce';
        if (Math.abs(ball.vy) < 90) { phase = 'roll'; T = 0; }
      }
    } else if (phase === 'roll') {
      T += dt; ball.x += ball.vx * dt; ball.vx *= .97; ball.rot += ball.vx * dt / G.r; if (Math.abs(ball.vx) < 4 || T > 2.5) { ball.y = G.floor - G.r; phase = 'idle'; }
    }
    ball.sq += (1 - ball.sq) * Math.min(1, dt * 14);
    court(g, w, h, G); hoopBack(g, G); shadow(g, ball.x, G.floor, ball.y, G.r);
    const behind = phase === 'drop' && ball.y > G.rim.y - G.r * .6;
    if (behind) { drawBall(g, ball.x, ball.y, G.r, ball.rot, ball.sq); hoopFront(g, G, now / 1000); }
    else { hoopFront(g, G, now / 1000); drawBall(g, ball.x, ball.y, G.r, ball.rot, ball.sq); }
    if (popTxt) { popTxt.t -= dt * .9; g.globalAlpha = Math.max(0, popTxt.t); g.fillStyle = '#ffb347'; g.font = `400 ${Math.round(G.r * 2)}px Anton, Impact, sans-serif`; g.textAlign = 'center'; g.fillText(popTxt.v, G.rim.x, G.rim.y - G.r * 3 - (1 - popTxt.t) * 30); g.globalAlpha = 1; if (popTxt.t <= 0) popTxt = null; }
  }
  c.closest('.arena').addEventListener('click', () => { if (phase !== 'idle') return; const { w, h } = fitCanvas(c); newShot(w, h); sfx.tick(); });
  requestAnimationFrame(step);
})();

/* ---------- foco de luz, reveal, scroll, menú activo ---------- */
addEventListener('pointermove', e => { document.body.style.setProperty('--mx', e.clientX + 'px'); document.body.style.setProperty('--my', e.clientY + 'px'); }, { passive: true });
const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }), { threshold: .06 });
$$('.reveal').forEach(el => io.observe(el));
const spy = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) $$('.quick a').forEach(a => a.classList.toggle('active', a.getAttribute('href') === '#' + e.target.id)); }), { rootMargin: '-40% 0px -55% 0px' });
$$('main section[id]').forEach(s => spy.observe(s));
addEventListener('scroll', () => { const p = scrollY / Math.max(1, document.documentElement.scrollHeight - innerHeight); $('#scrollBar').style.width = (p * 100) + '%'; }, { passive: true });
function toast(t) { const el = $('#toast'); if (!el) return; el.textContent = t; el.classList.add('show'); clearTimeout(toast.k); toast.k = setTimeout(() => el.classList.remove('show'), 1900); }

/* ---------- consola R animada (vista previa del dataset) ---------- */
(function () {
  const pre = $('#rcon'); if (!pre) return; const lines = JSON.parse(pre.dataset.lines); let started = false;
  const go = () => {
    if (started) return; started = true; pre.innerHTML = ''; let li = 0;
    const next = () => {
      if (li >= lines.length) { pre.insertAdjacentHTML('beforeend', '<span class="p">&gt; </span><span class="caret"></span>'); return; }
      const L = lines[li++];
      if (L.cmd) { const span = document.createElement('span'); pre.insertAdjacentHTML('beforeend', '<span class="p">&gt; </span>'); pre.appendChild(span); let i = 0; (function k() { span.textContent = L.cmd.slice(0, ++i); if (i < L.cmd.length) setTimeout(k, reduced ? 0 : 22); else { pre.insertAdjacentText('beforeend', '\n'); setTimeout(next, 250); } })(); }
      else { pre.insertAdjacentText('beforeend', L.out + '\n'); setTimeout(next, reduced ? 0 : 40); }
    };
    next();
  };
  new IntersectionObserver(e => { if (e[0].isIntersecting) go(); }, { threshold: .4 }).observe(pre);
})();

/* ---------- imágenes de jugadores y logos (CDN NBA) con respaldo ---------- */
$$('.pcard img').forEach(img => img.addEventListener('error', () => { const d = document.createElement('div'); d.className = 'ini'; d.textContent = img.alt.split(' ').map(x => x[0]).join('').slice(0, 2); img.replaceWith(d); }, { once: true }));
$$('.logos img').forEach(img => img.addEventListener('error', () => img.remove(), { once: true }));

/* ---------- cronómetro (120 min) con bocina ---------- */
(function () {
  let total = (+document.body.dataset.minutes || 120) * 60, run = false, iv; const start = total;
  const d = $('#timer'), b = $('#timerBtn'), r = $('#timerReset');
  const upd = () => { const hh = total / 3600 | 0, m = total % 3600 / 60 | 0, s = total % 60; d.textContent = [hh, m, s].map(x => String(x).padStart(2, '0')).join(':'); d.classList.toggle('warn', total < 900 && total > 0); };
  b.onclick = () => {
    if (!run) { run = true; b.textContent = '⏸ Pausar'; b.classList.add('on'); iv = setInterval(() => { if (--total <= 0) { total = 0; clearInterval(iv); run = false; b.textContent = '⏱ Final del partido'; b.classList.remove('on'); sfx.buzzer(); toast('🚨 ¡Bocina! Se acabó el tiempo'); } upd(); }, 1000); }
    else { clearInterval(iv); run = false; b.textContent = '▶ Reanudar'; b.classList.remove('on'); }
  };
  r.onclick = () => { clearInterval(iv); run = false; total = start; b.textContent = '▶ Iniciar'; b.classList.remove('on'); upd(); };
  upd();
})();

/* ---------- ejercicios: criterios, medallas, nota y shot chart ---------- */
const exs = $$('.ex'); const medalsBar = $('#medals');
exs.forEach(ex => { const m = document.createElement('a'); m.className = 'medal'; m.href = '#' + ex.id; m.textContent = ex.dataset.code; m.title = ex.dataset.title; m.dataset.ex = ex.id; medalsBar.appendChild(m); });
const claimed = id => !!state.medals[id];
const shot = { spots: [] };
function shotChart() {
  const c = $('#shotchart'); if (!c) return; const { g, w, h } = fitCanvas(c), n = exs.length;
  const s = w / 500, hx = 250 * s, hy = 52 * s;
  g.clearRect(0, 0, w, h);
  const fl = g.createLinearGradient(0, 0, 0, h); fl.addColorStop(0, '#5a3517'); fl.addColorStop(1, '#2c1a0b'); g.fillStyle = fl; g.beginPath(); g.roundRect ? g.roundRect(0, 0, w, h, 16 * s) : g.rect(0, 0, w, h); g.fill();
  g.fillStyle = 'rgba(255,255,255,.035)'; for (let x = 0; x < w; x += 18 * s) g.fillRect(x, 0, 1, h);
  g.strokeStyle = 'rgba(255,255,255,.6)'; g.lineWidth = 2 * s;
  g.strokeRect(10 * s, 10 * s, w - 20 * s, h - 20 * s);
  g.fillStyle = 'rgba(226,54,75,.25)'; g.fillRect(hx - 80 * s, 10 * s, 160 * s, 180 * s); g.strokeRect(hx - 80 * s, 10 * s, 160 * s, 180 * s);
  g.beginPath(); g.arc(hx, 190 * s, 60 * s, 0, Math.PI); g.stroke();
  const a3 = Math.atan2(89.5, 220); // línea de triple: esquinas rectas + arco de 237.5 alrededor del aro
  g.beginPath(); g.moveTo(30 * s, 10 * s); g.lineTo(30 * s, (52 + 89.5) * s); g.arc(hx, hy, 237.5 * s, Math.PI - a3, a3, true); g.lineTo(470 * s, 10 * s); g.stroke();
  g.beginPath(); g.arc(hx, h - 10 * s, 60 * s, Math.PI, 0); g.stroke();
  g.strokeStyle = '#ff7a1a'; g.lineWidth = 3 * s; g.beginPath(); g.arc(hx, hy, 9 * s, 0, 7); g.stroke();
  g.strokeStyle = '#fff'; g.lineWidth = 3 * s; g.beginPath(); g.moveTo(hx - 30 * s, 40 * s); g.lineTo(hx + 30 * s, 40 * s); g.stroke();
  // 14 posiciones de tiro: 4 bajo el aro, 5 de media distancia y 5 triples (2 esquinas + 3 en el arco)
  const P = [];
  [.2, .4, .6, .8].forEach(a => P.push([250 + Math.cos(Math.PI * a) * 85, 52 + Math.sin(Math.PI * a) * 85]));
  [.08, .29, .5, .71, .92].forEach(a => P.push([250 + Math.cos(Math.PI * a) * 168, 52 + Math.sin(Math.PI * a) * 168]));
  P.push([450, 62]); [.27, .5, .73].forEach(a => P.push([250 + Math.cos(Math.PI * a) * 275, 52 + Math.sin(Math.PI * a) * 275])); P.push([50, 62]);
  shot.spots = P.slice(0, n).map(([x, y]) => ({ x: x * s, y: y * s }));
  exs.forEach((ex, i) => {
    const p = shot.spots[i]; if (!p) return; const b = $$('input[type=checkbox]', ex), v = b.filter(x => x.checked).length / b.length, R = 15 * s;
    g.fillStyle = 'rgba(5,8,15,.75)'; g.beginPath(); g.arc(p.x, p.y, R, 0, 7); g.fill();
    if (claimed(ex.id)) drawBall(g, p.x, p.y, R, i);
    else { g.strokeStyle = 'rgba(255,255,255,.25)'; g.lineWidth = 2.5 * s; g.beginPath(); g.arc(p.x, p.y, R, 0, 7); g.stroke(); if (v > 0) { g.strokeStyle = '#ffb347'; g.beginPath(); g.arc(p.x, p.y, R, -Math.PI / 2, -Math.PI / 2 + v * Math.PI * 2); g.stroke(); } }
    g.fillStyle = claimed(ex.id) ? '#fff' : '#cfd7ea'; g.font = `700 ${Math.round(10 * s)}px JetBrains Mono, monospace`; g.textAlign = 'center'; g.textBaseline = 'middle';
    if (!claimed(ex.id)) g.fillText(ex.dataset.code, p.x, p.y);
    else { g.fillStyle = '#fff'; g.fillText(ex.dataset.code, p.x, p.y + R + 9 * s); }
  });
}
(function () { const c = $('#shotchart'); if (!c) return; c.addEventListener('click', e => { const r = c.getBoundingClientRect(), x = e.clientX - r.left, y = e.clientY - r.top; const i = shot.spots.findIndex(p => Math.hypot(p.x - x, p.y - y) < 20); if (i >= 0) exs[i].scrollIntoView({ behavior: 'smooth', block: 'start' }); }); addEventListener('resize', shotChart); })();
function render() {
  let score = 0;
  exs.forEach(ex => {
    const b = $$('input[type=checkbox]', ex), done = b.filter(x => x.checked).length, all = done === b.length, btn = $('.claim', ex);
    $('.prog i', ex).style.width = (done / b.length * 100) + '%';
    if (claimed(ex.id) && !all) delete state.medals[ex.id];
    const got = claimed(ex.id); btn.disabled = !all; btn.classList.toggle('got', got); ex.classList.toggle('done', got);
    btn.textContent = got ? '🏀 ¡Canasta! Ejercicio superado' : all ? '🏀 Lanzar: dar por completado' : `🔒 Faltan ${b.length - done} criterio${b.length - done === 1 ? '' : 's'}`;
    $(`.medal[data-ex="${ex.id}"]`).classList.toggle('on', got);
    if (got) score += +ex.dataset.pts;
  });
  $('#score').textContent = score.toFixed(1); shotChart();
}
let celebrated = false;
exs.forEach(ex => {
  ex.addEventListener('change', e => { const cb = e.target; if (!cb.dataset.k) return; if (cb.checked) state.reqs[cb.dataset.k] = 1; else delete state.reqs[cb.dataset.k]; save(); render(); sfx.tick(); });
  $('.claim', ex).onclick = () => {
    state.medals[ex.id] = !state.medals[ex.id]; if (!state.medals[ex.id]) delete state.medals[ex.id]; save(); render();
    if (claimed(ex.id)) { sfx.swish(); sfx.medal(); toast(`🏀 ${ex.dataset.code} · +${(+ex.dataset.pts).toFixed(1)} pts`); }
    const all = exs.every(x => claimed(x.id)); if (all && !celebrated) { celebrated = true; balls(); sfx.fanfare(); toast('🏆 ¡Partido perfecto! 10 / 10'); } if (!all) celebrated = false;
  };
  $$('input[type=checkbox]', ex).forEach(cb => cb.checked = !!state.reqs[cb.dataset.k]);
});

/* ---------- comprobador de resultados (respuestas guardadas como huella, no en claro) ---------- */
const SALT = 'nba2k25|';
function fnv(str) { let h = 0x811c9dc5; for (const b of new TextEncoder().encode(str)) { h ^= b; h = Math.imul(h, 0x01000193) >>> 0; } return h.toString(16).padStart(8, '0'); }
function norm(v, dp) {
  v = String(v).trim();
  if (dp !== undefined && dp !== '') { const n = parseFloat(v.replace(',', '.').replace(/[^0-9.\-]/g, '')); return isNaN(n) ? '' : n.toFixed(+dp); }
  return v.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/["'`]/g, '').replace(/\s+/g, ' ').trim();
}
const ansEls = $$('.ans');
function hits() { const ok = ansEls.filter(a => a.classList.contains('ok')).length; const el = $('#hits'); if (el) el.innerHTML = `🎯 Resultados <b>${ok}</b>/${ansEls.length}`; }
ansEls.forEach(a => {
  const inp = $('input', a), st = $('.st', a), key = a.dataset.k;
  const check = (sound) => {
    const v = norm(inp.value, a.dataset.dp); a.classList.remove('ok', 'ko');
    if (!v) { st.textContent = ''; } else if (fnv(SALT + v) === a.dataset.h) { a.classList.add('ok'); st.textContent = '✅'; if (sound) sfx.ok(); }
    else { a.classList.add('ko'); st.textContent = '❌'; if (sound) sfx.ko(); }
    state.ans[key] = inp.value; save(); hits();
  };
  inp.value = state.ans[key] || ''; if (inp.value) check(false);
  inp.addEventListener('keydown', e => { if (e.key === 'Enter') check(true); });
  inp.addEventListener('change', () => check(true));
});
hits(); render();

/* ---------- lluvia de balones al completar el examen ---------- */
function balls() {
  const c = $('#fx'); const { g, w, h } = fitCanvas(c);
  const P = Array.from({ length: 60 }, () => ({ x: Math.random() * w, y: -40 - Math.random() * h * .6, vx: (Math.random() - .5) * 120, vy: 0, r: 10 + Math.random() * 16, rot: Math.random() * 6, b: 0 }));
  let last = performance.now(), T = 0;
  (function l(now) {
    const dt = Math.min(.033, (now - last) / 1000); last = now; T += dt; g.clearRect(0, 0, w, h);
    P.forEach(p => { p.vy += 1100 * dt; p.x += p.vx * dt; p.y += p.vy * dt; p.rot += p.vx * dt / p.r; if (p.y > h - p.r && p.b < 3) { p.y = h - p.r; p.vy *= -.62; p.b++; } drawBall(g, p.x, p.y, p.r, p.rot); });
    if (T < 4.5) requestAnimationFrame(l); else g.clearRect(0, 0, w, h);
  })(last);
}

/* ---------- copiar código de la solución ---------- */
$$('.copy').forEach(b => b.onclick = () => { const t = $('#' + b.dataset.t).innerText; navigator.clipboard?.writeText(t).then(() => { b.textContent = '✅ Copiado'; setTimeout(() => b.textContent = '📋 Copiar', 1400); }); });

/* ---------- zona secreta: hover + "gg" ---------- */
(function () {
  let hov = false, typed = '', kt; const zone = $('#triggerZone'), st = $('#secretStatus');
  const targets = [zone, $('footer'), $('#timer')].filter(Boolean), sol = $('#solutionContainer'), modal = $('#ggModal');
  targets.forEach(t => { t.addEventListener('mouseenter', () => { hov = true; if (st && t === zone) st.textContent = 'Estado: pizarra activa, esperando jugada…'; }); t.addEventListener('mouseleave', () => { hov = false; typed = ''; if (st && t === zone) st.textContent = 'Estado: esperando jugada…'; }); });
  const close = () => { if (!modal) return; modal.classList.remove('open'); document.body.classList.remove('no-scroll'); };
  addEventListener('keydown', e => {
    if (e.key === 'Escape') { close(); return; }
    if (!hov || (e.target && e.target.tagName === 'INPUT')) return;
    const k = e.key.toLowerCase();
    if (k === 'g') {
      typed += 'g'; clearTimeout(kt); kt = setTimeout(() => typed = '', 2500);
      if (typed.endsWith('gg')) {
        typed = ''; sfx.buzzer(); balls();
        if (sol) { sol.classList.add('show'); if (st) st.textContent = '🔓 Solución desplegada al final de la página'; setTimeout(() => sol.scrollIntoView({ behavior: 'smooth' }), 150); }
        else if (modal) { modal.classList.add('open'); document.body.classList.add('no-scroll'); }
      }
    } else if (!['shift', 'control', 'alt'].includes(k)) typed = '';
  });
  if (modal) { modal.addEventListener('click', e => { if (e.target === modal) close(); }); $('#ggClose').onclick = close; }
})();

/* ---------- intro de vídeo sobre fondo negro (primera visita) ---------- */
(function () {
  const box = $('#intro'), v = $('#introVideo'); if (!box || !v) return;
  const root = document.documentElement;
  const close = () => { v.pause(); box.classList.add('out'); setTimeout(() => { root.classList.remove('intro-on'); box.classList.remove('out', 'blocked'); }, 700); };
  const start = () => {
    root.classList.add('intro-on'); box.classList.remove('out', 'blocked'); v.currentTime = 0; v.muted = true; $('#introSound').textContent = '🔇 Activar sonido';
    const p = v.play(); if (p && p.catch) p.catch(() => box.classList.add('blocked'));
  };
  v.addEventListener('ended', close);
  v.addEventListener('error', () => { root.classList.remove('intro-on'); });   // si falta el vídeo, se entra directamente
  $('#introSkip').onclick = close;
  $('#introPlay').onclick = () => { box.classList.remove('blocked'); v.muted = false; $('#introSound').textContent = '🔊 Silenciar'; v.play(); };
  $('#introSound').onclick = () => { v.muted = !v.muted; $('#introSound').textContent = v.muted ? '🔇 Activar sonido' : '🔊 Silenciar'; };
  addEventListener('keydown', e => { if (e.key === 'Escape' && root.classList.contains('intro-on')) close(); });
  const again = $('#introAgain'); if (again) again.onclick = e => { e.stopPropagation(); start(); };
  if (root.classList.contains('intro-on')) start();
})();
