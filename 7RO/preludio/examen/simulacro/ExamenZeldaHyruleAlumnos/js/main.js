
        // ====================== CANVAS DE RUNAS SHEIKAH ======================
        const canvas = document.getElementById('runesCanvas');
        const ctx = canvas.getContext('2d');
        let width = canvas.width = canvas.offsetWidth;
        let height = canvas.height = canvas.offsetHeight;

        window.addEventListener('resize', () => {
            width = canvas.width = canvas.offsetWidth;
            height = canvas.height = canvas.offsetHeight;
        });

        const runeSymbols = "▲▼◆◇○●□■⌖⍟⎈⌬⌕⌗⌁⌇⍝⍢⍣⍤";
        const particles = [];
        for (let i = 0; i < 28; i++) {
            particles.push({
                x: Math.random() * width,
                y: Math.random() * height,
                char: runeSymbols[Math.floor(Math.random() * runeSymbols.length)],
                speed: 0.4 + Math.random() * 0.7,
                size: 11 + Math.random() * 12,
                opacity: 0.15 + Math.random() * 0.4
            });
        }

        function drawRunes() {
            ctx.clearRect(0, 0, width, height);
            ctx.font = '14px "Press Start 2P", monospace';
            particles.forEach(p => {
                ctx.fillStyle = `rgba(0, 229, 255, ${p.opacity})`;
                ctx.fillText(p.char, p.x, p.y);
                p.y -= p.speed;
                if (p.y < -20) {
                    p.y = height + 20;
                    p.x = Math.random() * width;
                    p.char = runeSymbols[Math.floor(Math.random() * runeSymbols.length)];
                }
            });
            requestAnimationFrame(drawRunes);
        }
        drawRunes();

        // ====================== SIMULADOR DE DIÁLOGO DE ESCENA ======================
        const dialogMessages = [
            "> Tableta Sheikah: Escaneando Centaleón Plateado... Debilidad Sagrada detectada.",
            "> Link desenvaina la Espada de Fuego. ¡Las runas de calor se activan!",
            "> ¡Alerta de guardia! El Centaleón prepara su embestida salvaje.",
            "> Consejo Sheikah: Consulta la tabla elemental para duplicar el impacto.",
            "> Recuerda: Vigila la durabilidad de tus armas en la alforja."
        ];
        let msgIndex = 0;
        const dialogEl = document.getElementById('sceneDialog');
        setInterval(() => {
            msgIndex = (msgIndex + 1) % dialogMessages.length;
            dialogEl.style.opacity = '0';
            setTimeout(() => {
                dialogEl.textContent = dialogMessages[msgIndex];
                dialogEl.style.opacity = '1';
            }, 300);
        }, 4500);

        // ====================== CRONÓMETRO DE EXAMEN (2:30:00) ======================
        let totalSeconds = 2 * 3600 + 30 * 60;
        let timerInterval = null;
        let isRunning = false;
        const timerDisplay = document.getElementById('timerDisplay');
        const timerToggleBtn = document.getElementById('timerToggleBtn');
        const timerResetBtn = document.getElementById('timerResetBtn');

        function updateTimerDisplay() {
            const h = Math.floor(totalSeconds / 3600).toString().padStart(2, '0');
            const m = Math.floor((totalSeconds % 3600) / 60).toString().padStart(2, '0');
            const s = (totalSeconds % 60).toString().padStart(2, '0');
            timerDisplay.textContent = `${h}:${m}:${s}`;
            timerDisplay.classList.toggle('warn', totalSeconds < 15 * 60 && totalSeconds > 0);
        }

        timerToggleBtn.addEventListener('click', () => {
            if (!isRunning) {
                isRunning = true;
                timerToggleBtn.textContent = '⏸ Pausar';
                timerToggleBtn.style.background = 'rgba(255, 119, 0, 0.3)';
                timerInterval = setInterval(() => {
                    if (totalSeconds > 0) {
                        totalSeconds--;
                        updateTimerDisplay();
                    } else {
                        clearInterval(timerInterval);
                        isRunning = false;
                        timerToggleBtn.textContent = '⏱ Tiempo Agotado';
                    }
                }, 1000);
            } else {
                isRunning = false;
                clearInterval(timerInterval);
                timerToggleBtn.textContent = '▶ Reanudar';
                timerToggleBtn.style.background = '';
            }
        });

        timerResetBtn.addEventListener('click', () => {
            clearInterval(timerInterval);
            isRunning = false;
            totalSeconds = 2 * 3600 + 30 * 60;
            timerToggleBtn.textContent = '▶ Iniciar Desafío';
            timerToggleBtn.style.background = '';
            updateTimerDisplay();
        });

        // ====================== SISTEMA DE CHECKLIST, ORBES Y PUNTUACIÓN ======================
        const STORAGE_KEY = 'zelda_exam_completed_steps';
        let completedSteps = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]');
        const orbIcons = document.querySelectorAll('.orb-icon');
        const currentScoreEl = document.getElementById('currentScore');

        function renderProgress() {
            let totalScore = 0;
            document.querySelectorAll('.step-card').forEach(card => {
                const stepNum = Number(card.dataset.step);
                const pts = parseFloat(card.dataset.pts);
                const btn = card.querySelector('.shrine-complete-btn');
                const isDone = completedSteps.includes(stepNum);

                card.classList.toggle('completed', isDone);
                if (btn) {
                    btn.classList.toggle('active', isDone);
                    btn.innerHTML = isDone ? '<span>✅</span> Orbe Conseguido' : '<span>🔵</span> Marcar Santuario Superado';
                }

                if (isDone) {
                    totalScore += pts;
                }
            });

            orbIcons.forEach(orb => {
                const s = Number(orb.dataset.step);
                orb.classList.toggle('active', completedSteps.includes(s));
            });

            currentScoreEl.textContent = totalScore.toFixed(1);
        }

        document.querySelectorAll('.step-card').forEach(card => {
            const btn = card.querySelector('.shrine-complete-btn');
            if (btn) {
                btn.addEventListener('click', () => {
                    const stepNum = Number(card.dataset.step);
                    if (completedSteps.includes(stepNum)) {
                        completedSteps = completedSteps.filter(x => x !== stepNum);
                    } else {
                        completedSteps.push(stepNum);
                        playChime(660, 0.12);
                    }
                    localStorage.setItem(STORAGE_KEY, JSON.stringify(completedSteps));
                    renderProgress();
                });
            }
        });
        renderProgress();

        // ====================== COPIADO DE CÓDIGO AL PORTAPAPELES ======================
        document.querySelectorAll('.copy-code-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                const targetId = btn.dataset.target;
                const pre = document.getElementById(targetId);
                if (pre) {
                    navigator.clipboard.writeText(pre.innerText).then(() => {
                        const original = btn.textContent;
                        btn.textContent = '✅ ¡Copiado!';
                        setTimeout(() => btn.textContent = original, 2000);
                    });
                }
            });
        });

        // ====================== WEB AUDIO API: SINTETIZADOR DE SONIDOS ======================
        let audioCtx = null;
        function getAudioContext() {
            if (!audioCtx) {
                audioCtx = new (window.AudioContext || window.webkitAudioContext)();
            }
            if (audioCtx.state === 'suspended') {
                audioCtx.resume();
            }
            return audioCtx;
        }

        function playChime(freq, duration) {
            try {
                const ctx = getAudioContext();
                const osc = ctx.createOscillator();
                const gain = ctx.createGain();
                osc.type = 'sine';
                osc.frequency.setValueAtTime(freq, ctx.currentTime);
                gain.gain.setValueAtTime(0.2, ctx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + duration);
                osc.connect(gain);
                gain.connect(ctx.destination);
                osc.start();
                osc.stop(ctx.currentTime + duration);
            } catch (e) {
                console.log(e);
            }
        }

        // Famoso jingle de secreto de Zelda (8 notas)
        function playZeldaSecretFanfare() {
            try {
                const ctx = getAudioContext();
                const notes = [
                    { f: 783.99, d: 0.12 }, // G5
                    { f: 739.99, d: 0.12 }, // F#5
                    { f: 622.25, d: 0.12 }, // D#5
                    { f: 440.00, d: 0.14 }, // A4
                    { f: 415.30, d: 0.14 }, // G#4
                    { f: 659.25, d: 0.14 }, // E5
                    { f: 830.61, d: 0.16 }, // G#5
                    { f: 1046.50, d: 0.45 } // C6
                ];
                let time = ctx.currentTime;
                notes.forEach(n => {
                    const osc = ctx.createOscillator();
                    const gain = ctx.createGain();
                    osc.type = 'triangle';
                    osc.frequency.setValueAtTime(n.f, time);
                    gain.gain.setValueAtTime(0.25, time);
                    gain.gain.exponentialRampToValueAtTime(0.001, time + n.d);
                    osc.connect(gain);
                    gain.connect(ctx.destination);
                    osc.start(time);
                    osc.stop(time + n.d);
                    time += n.d * 0.95;
                });
            } catch (e) {
                console.log(e);
            }
        }

        // ====================== EASTER EGG HOVER + "GG" -> IMAGEN ======================
let isHoveringTrigger = false;
let typedBuffer = '';
let keyTimer = null;
const triggerZone = document.getElementById('triggerZone');
const examFooter = document.querySelector('footer');
const sheikahLens = document.querySelector('.sheikah-indicator');
const secretStatus = document.getElementById('secretStatus');
const ggModal = document.getElementById('ggModal');
const entryModal = document.getElementById('entryModal');

function setHover(active) {
    isHoveringTrigger = active;
    typedBuffer = '';
    if (!secretStatus) return;
    secretStatus.textContent = active
        ? "Estado: ⚡ Frecuencia Ancestral Sintonizada · Terminal Receptiva..."
        : "Estado: Esperando sintonización de frecuencias...";
    secretStatus.style.color = active ? 'var(--sheikah-gold)' : 'var(--text-muted)';
}

[triggerZone, examFooter, sheikahLens].forEach(el => {
    if (!el) return;
    el.addEventListener('mouseenter', () => setHover(true));
    el.addEventListener('mouseleave', () => setHover(false));
});

function openModal(m) { m.classList.add('open'); document.body.classList.add('no-scroll'); }
function closeModals() {
    document.querySelectorAll('.gg-modal.open').forEach(m => m.classList.remove('open'));
    document.body.classList.remove('no-scroll');
}

window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') { closeModals(); return; }
    const hovering = isHoveringTrigger ||
        [triggerZone, examFooter, sheikahLens].some(el => el && el.matches(':hover'));
    if (!hovering) return;
    const key = e.key.toLowerCase();
    if (key === 'g') {
        typedBuffer += 'g';
        clearTimeout(keyTimer);
        keyTimer = setTimeout(() => { typedBuffer = ''; }, 2500);
        if (typedBuffer.endsWith('gg')) {
            typedBuffer = '';
            playZeldaSecretFanfare();
            openModal(ggModal);
        }
    } else if (!['shift', 'control', 'alt'].includes(key)) {
        typedBuffer = '';
    }
}, true);

document.querySelectorAll('.gg-modal').forEach(m => m.addEventListener('click', ev => {
    if (ev.target === m) closeModals();
}));
document.getElementById('ggClose').addEventListener('click', closeModals);
document.getElementById('entryClose').addEventListener('click', closeModals);

// ====================== BARRA DE PROGRESO DE SCROLL ======================
const scrollBar = document.getElementById('scrollBar');
window.addEventListener('scroll', () => {
    const h = document.documentElement.scrollHeight - innerHeight;
    scrollBar.style.width = (h > 0 ? (scrollY / h) * 100 : 0) + '%';
}, { passive: true });

// ====================== LUCIÉRNAGAS / ESPÍRITUS KOROK ======================
(function () {
    const c = document.getElementById('fireflies');
    const g = c.getContext('2d');
    let W, H;
    const fit = () => { W = c.width = innerWidth; H = c.height = innerHeight; };
    fit(); addEventListener('resize', fit);
    const flies = Array.from({ length: 45 }, () => ({
        x: Math.random() * innerWidth, y: Math.random() * innerHeight,
        r: 1 + Math.random() * 2.2, vx: (Math.random() - .5) * .3, vy: -.15 - Math.random() * .35,
        ph: Math.random() * 6.28, hue: Math.random() < .7 ? 175 : 50
    }));
    (function loop(t) {
        g.clearRect(0, 0, W, H);
        flies.forEach(f => {
            f.x += f.vx + Math.sin(t / 1500 + f.ph) * .3; f.y += f.vy;
            if (f.y < -10) { f.y = H + 10; f.x = Math.random() * W; }
            const a = .35 + .35 * Math.sin(t / 600 + f.ph);
            g.beginPath(); g.arc(f.x, f.y, f.r * 3, 0, 6.28);
            g.fillStyle = `hsla(${f.hue},100%,70%,${a * .25})`; g.fill();
            g.beginPath(); g.arc(f.x, f.y, f.r, 0, 6.28);
            g.fillStyle = `hsla(${f.hue},100%,80%,${a})`; g.fill();
        });
        requestAnimationFrame(loop);
    })(0);
})();

// ====================== HYRULE COMPENDIUM API ======================
const API = 'https://api.hyrule-compendium.com/v3/compendium/entry/';
const apiImg = n => API + encodeURIComponent(n) + '/image';

// Sprite de cada paso (objeto/criatura del compendio relacionado con el ejercicio)
const STEP_SPRITES = {
    1: 'master_sword', 2: 'flameblade', 3: 'hinox', 4: 'frostspear',
    5: 'hylian_shield', 6: 'silver_lynel', 7: 'guardian_stalker', 8: 'royal_claymore'
};
document.querySelectorAll('.step-card').forEach(card => {
    const name = STEP_SPRITES[card.dataset.step];
    const top = card.querySelector('.step-top');
    if (!name || !top) return;
    const img = document.createElement('img');
    img.className = 'step-sprite';
    img.loading = 'lazy';
    img.alt = name.replace(/_/g, ' ');
    img.src = apiImg(name);
    img.onerror = () => img.remove();
    top.appendChild(img);
});

const COMP_ENTRIES = ['bokoblin', 'lizalfos', 'blue_lizalfos', 'silver_lynel', 'hinox', 'guardian_stalker',
    'master_sword', 'flameblade', 'frostspear', 'thunderblade', 'hylian_shield', 'royal_claymore'];
const compGrid = document.getElementById('compGrid');
const entryBody = document.getElementById('entryBody');
const esc = s => String(s ?? '').replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

compGrid.innerHTML = COMP_ENTRIES.map(() => '<div class="comp-card skeleton"></div>').join('');

Promise.allSettled(COMP_ENTRIES.map(n =>
    fetch(API + encodeURIComponent(n)).then(r => { if (!r.ok) throw 0; return r.json(); })
)).then(results => {
    const cards = [];
    results.forEach((r, i) => {
        if (r.status !== 'fulfilled' || !r.value.data || !r.value.data.name) return;
        cards.push(r.value.data);
    });
    if (!cards.length) {
        compGrid.innerHTML = '<p class="comp-error">📡 La Tableta Sheikah no pudo conectar con el compendio (sin conexión). El examen sigue siendo totalmente funcional.</p>';
        return;
    }
    compGrid.innerHTML = '';
    cards.forEach((d, idx) => {
        const el = document.createElement('button');
        el.type = 'button';
        el.className = 'comp-card';
        el.dataset.cat = d.category;
        el.style.animationDelay = (idx * 60) + 'ms';
        const stat = d.hearts_dropped !== undefined ? '' : '';
        const badge = d.category === 'monsters' ? '👹 Monstruo' : '⚔️ Equipo';
        const power = d.properties && d.properties.attack ? `<span class="comp-stat">ATQ ${d.properties.attack}</span>` : '';
        el.innerHTML = `<div class="comp-img"><img loading="lazy" src="${esc(d.image)}" alt="${esc(d.name)}"></div>
            <div class="comp-name">${esc(d.name)}</div>
            <div class="comp-meta"><span class="tag-badge">${badge}</span>${power}</div>`;
        el.addEventListener('click', () => {
            const locs = (d.common_locations || []).join(', ') || 'Desconocida';
            const drops = (d.drops || []).join(', ') || '—';
            const props = d.properties ? Object.entries(d.properties).map(([k, v]) => `<li><b>${esc(k)}</b>: ${esc(v)}</li>`).join('') : '';
            entryBody.innerHTML = `<div class="entry-grid"><img src="${esc(d.image)}" alt="${esc(d.name)}">
                <div><h3>${esc(d.name)}</h3><p>${esc(d.description)}</p>
                <p><b>📍 Localizaciones:</b> ${esc(locs)}</p><p><b>🎁 Botín:</b> ${esc(drops)}</p>
                ${props ? `<ul class="entry-props">${props}</ul>` : ''}</div></div>`;
            playChime(880, 0.15);
            openModal(entryModal);
        });
        compGrid.appendChild(el);
    });
});

document.getElementById('compFilters').addEventListener('click', ev => {
    const b = ev.target.closest('button'); if (!b) return;
    document.querySelectorAll('#compFilters button').forEach(x => x.classList.toggle('active', x === b));
    const f = b.dataset.filter;
    compGrid.querySelectorAll('.comp-card').forEach(c => { c.style.display = (f === 'all' || c.dataset.cat === f) ? '' : 'none'; });
});

// ====================== LLUVIA DE RUPIAS AL COMPLETAR LOS 7 SANTUARIOS ======================
let celebrated = false;
document.addEventListener('click', ev => {
    if (!ev.target.closest('.shrine-complete-btn')) return;
    const all = [1, 2, 3, 4, 5, 6, 7].every(n => completedSteps.includes(n));
    if (all && !celebrated) { celebrated = true; rupeeRain(); playZeldaSecretFanfare(); }
    if (!all) celebrated = false;
});
function rupeeRain() {
    const colors = ['#00e676', '#00b0ff', '#ff1744', '#ffc400', '#d500f9'];
    for (let i = 0; i < 60; i++) {
        const r = document.createElement('div');
        r.className = 'rupee';
        r.style.left = Math.random() * 100 + 'vw';
        r.style.background = colors[i % colors.length];
        r.style.animationDuration = (2 + Math.random() * 2.5) + 's';
        r.style.animationDelay = (Math.random() * 1.2) + 's';
        document.body.appendChild(r);
        setTimeout(() => r.remove(), 6000);
    }
}
