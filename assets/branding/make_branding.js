// Genera logo (800x800) y banner (2560x1440) para cada opción de nombre del canal.
// Uso: node assets/branding/make_branding.js   (necesita Playwright/Chromium)
// Salida: assets/branding/<slug>/logo.png, banner.png, banner_safe_preview.png
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const FONTS = path.resolve(__dirname, '..', 'fonts');
const b64 = (f) => fs.readFileSync(path.join(FONTS, f)).toString('base64');
const fontCss = `
@font-face{font-family:Anton;src:url(data:font/ttf;base64,${b64('Anton-Regular.ttf')})}
@font-face{font-family:Bebas;src:url(data:font/ttf;base64,${b64('BebasNeue-Regular.ttf')})}
*{margin:0;padding:0;box-sizing:border-box}`;

// ---------- Balón de fútbol en SVG (pentágonos clásicos) ----------
function ball(id, R = 100) {
  const pt = (r, a) => [r * Math.cos(a), r * Math.sin(a)];
  const poly = (cx, cy, r, rot) =>
    Array.from({ length: 5 }, (_, i) => {
      const a = rot + (i * 2 * Math.PI) / 5;
      return [cx + r * Math.cos(a), cy + r * Math.sin(a)];
    });
  const toPath = (ps) => 'M' + ps.map((p) => p.map((v) => v.toFixed(2)).join(',')).join('L') + 'Z';
  const up = -Math.PI / 2;
  const s = R / 100;
  let d = toPath(poly(0, 0, 33 * s, up));
  let lines = '';
  for (let i = 0; i < 5; i++) {
    const a = up + (i * 2 * Math.PI) / 5;
    const [x1, y1] = pt(33 * s, a);
    const [x2, y2] = pt(64 * s, a);
    lines += `M${x1.toFixed(2)},${y1.toFixed(2)}L${x2.toFixed(2)},${y2.toFixed(2)}`;
    const [cx, cy] = pt(92 * s, a);
    const outer = poly(cx, cy, 29 * s, a + Math.PI); // un vértice apunta al centro
    d += toPath(outer);
    // costuras de los hexágonos hacia el borde
    for (const k of [2, 3]) {
      const [vx, vy] = outer[k];
      const [ex, ey] = [vx * 1.5, vy * 1.5];
      lines += `M${vx.toFixed(2)},${vy.toFixed(2)}L${ex.toFixed(2)},${ey.toFixed(2)}`;
    }
  }
  return `
  <defs>
    <radialGradient id="${id}-g" cx="38%" cy="32%" r="75%">
      <stop offset="0" stop-color="#ffffff"/><stop offset=".65" stop-color="#e9edf2"/><stop offset="1" stop-color="#9aa3ad"/>
    </radialGradient>
    <clipPath id="${id}-c"><circle r="${R}"/></clipPath>
  </defs>
  <circle r="${R}" fill="url(#${id}-g)"/>
  <g clip-path="url(#${id}-c)">
    <path d="${d}" fill="#14161a"/>
    <path d="${lines}" stroke="#14161a" stroke-width="${3.2 * s}" fill="none" stroke-linecap="round"/>
  </g>
  <circle r="${R - 1.5 * s}" fill="none" stroke="#0b0c0f" stroke-width="${3 * s}"/>`;
}

// ---------- Las 3 marcas ----------
const BRANDS = [
  {
    slug: 'soccer-aura-ranked',
    name: 'SOCCER AURA RANKED',
    handle: '@SoccerAuraRanked',
    bg1: '#1a0633', bg2: '#05010c', accent: '#ffc83d', accent2: '#a855f7',
    logo: () => `
      <svg viewBox="-400 -400 800 800" width="800" height="800">
        <defs>
          <radialGradient id="aura" r="50%"><stop offset="0" stop-color="#ffd36b" stop-opacity=".95"/>
            <stop offset=".45" stop-color="#a855f7" stop-opacity=".75"/><stop offset="1" stop-color="#1a0633" stop-opacity="0"/></radialGradient>
          <radialGradient id="bgL" r="70%"><stop offset="0" stop-color="#2b0b52"/><stop offset="1" stop-color="#05010c"/></radialGradient>
        </defs>
        <rect x="-400" y="-400" width="800" height="800" fill="url(#bgL)"/>
        <circle r="330" fill="url(#aura)"/>
        ${[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11].map((i) => `<path d="M0,-150 L18,-320 L-18,-320Z" fill="#ffd36b" opacity=".55" transform="rotate(${i * 30 + 15})"/>`).join('')}
        <circle r="168" fill="none" stroke="#ffc83d" stroke-width="10" opacity=".9"/>
        <circle r="190" fill="none" stroke="#a855f7" stroke-width="5" opacity=".7"/>
        <g transform="translate(0,10)">${ball('lb', 150)}</g>
        <!-- corona -->
        <path d="M-95,-150 L-120,-250 L-55,-200 L0,-275 L55,-200 L120,-250 L95,-150Z" fill="#ffc83d" stroke="#05010c" stroke-width="10" stroke-linejoin="round"/>
        <circle cx="0" cy="-282" r="14" fill="#ffc83d" stroke="#05010c" stroke-width="7"/>
        <text x="0" y="262" text-anchor="middle" font-family="Anton" font-size="118" fill="#ffffff" stroke="#05010c" stroke-width="14" paint-order="stroke" letter-spacing="6">AURA</text>
      </svg>`,
  },
  {
    slug: 'main-character-soccer',
    name: 'MAIN CHARACTER SOCCER',
    handle: '@MainCharacterSoccer',
    bg1: '#3a0508', bg2: '#070102', accent: '#ff3b30', accent2: '#ffb020',
    logo: () => `
      <svg viewBox="-400 -400 800 800" width="800" height="800">
        <defs>
          <linearGradient id="beam" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff4c2" stop-opacity=".9"/><stop offset="1" stop-color="#fff4c2" stop-opacity="0.05"/></linearGradient>
          <radialGradient id="bgM" r="70%"><stop offset="0" stop-color="#5a0a10"/><stop offset="1" stop-color="#070102"/></radialGradient>
          <radialGradient id="floor" r="50%"><stop offset="0" stop-color="#fff4c2" stop-opacity=".8"/><stop offset="1" stop-color="#fff4c2" stop-opacity="0"/></radialGradient>
        </defs>
        <rect x="-400" y="-400" width="800" height="800" fill="url(#bgM)"/>
        <path d="M-40,-400 L40,-400 L230,250 L-230,250Z" fill="url(#beam)"/>
        <ellipse cx="0" cy="240" rx="250" ry="45" fill="url(#floor)"/>
        <text x="0" y="95" text-anchor="middle" font-family="Anton" font-size="370" fill="#ff3b30" stroke="#070102" stroke-width="22" paint-order="stroke" letter-spacing="-6" opacity=".95">MC</text>
        <g transform="translate(0,205)">${ball('mb', 95)}</g>
        <path d="M0,-340 L16,-298 L60,-298 L25,-272 L38,-230 L0,-256 L-38,-230 L-25,-272 L-60,-298 L-16,-298Z" fill="#ffb020" stroke="#070102" stroke-width="6" stroke-linejoin="round"/>
      </svg>`,
  },
  {
    slug: 'ranked-soccer',
    name: 'RANKED SOCCER',
    handle: '@RankedSoccer',
    bg1: '#03361f', bg2: '#010a06', accent: '#39ff88', accent2: '#ffffff',
    logo: () => `
      <svg viewBox="-400 -400 800 800" width="800" height="800">
        <defs>
          <radialGradient id="bgR" r="70%"><stop offset="0" stop-color="#075c34"/><stop offset="1" stop-color="#010a06"/></radialGradient>
        </defs>
        <rect x="-400" y="-400" width="800" height="800" fill="url(#bgR)"/>
        <!-- líneas del campo -->
        <g stroke="#39ff88" stroke-width="6" fill="none" opacity=".35">
          <circle r="250"/><line x1="-400" y1="0" x2="400" y2="0"/>
        </g>
        <text x="-30" y="160" text-anchor="middle" font-family="Anton" font-size="460" fill="#ffffff" stroke="#010a06" stroke-width="24" paint-order="stroke" letter-spacing="-8">#1</text>
        <g transform="translate(205,110)">${ball('rb', 82)}</g>
        <rect x="-230" y="200" width="460" height="70" rx="14" fill="#39ff88" stroke="#010a06" stroke-width="8"/>
        <text x="0" y="254" text-anchor="middle" font-family="Anton" font-size="56" fill="#010a06" letter-spacing="10">RANKED</text>
      </svg>`,
  },
];

// ---------- Banner ----------
// Zona segura (se ve en todos los dispositivos): 1546x423 centrada en 2560x1440.
const SAFE = { w: 1546, h: 423, x: (2560 - 1546) / 2, y: (1440 - 423) / 2 };

function bannerHtml(b, logoPng) {
  const confetti = Array.from({ length: 22 }, (_, i) => {
    const x = (i * 619) % 2560, y = (i * 383) % 1440, r = 30 + ((i * 37) % 70);
    if (x > SAFE.x - 120 && x < SAFE.x + SAFE.w + 120 && y > SAFE.y - 120 && y < SAFE.y + SAFE.h + 120) return '';
    return `<g transform="translate(${x},${y}) rotate(${i * 47})" opacity=".18">${ball('c' + i, r)}</g>`;
  }).join('');
  return `<!doctype html><html><head><style>${fontCss}
  body{width:2560px;height:1440px;overflow:hidden;background:radial-gradient(ellipse at 50% 50%, ${b.bg1} 0%, ${b.bg2} 70%);font-family:Anton;color:#fff;position:relative}
  svg.bg{position:absolute;inset:0}
  .safe{position:absolute;left:${SAFE.x}px;top:${SAFE.y}px;width:${SAFE.w}px;height:${SAFE.h}px;display:flex;align-items:center;justify-content:center;gap:56px;padding:0 30px}
  .logo{width:340px;height:340px;border-radius:50%;border:10px solid ${b.accent};box-shadow:0 0 60px ${b.accent}aa;flex:none;object-fit:cover}
  .txt{display:flex;flex-direction:column;justify-content:center;min-width:0}
  .name{font-family:Bebas;font-size:66px;letter-spacing:6px;color:${b.accent};line-height:1;white-space:nowrap}
  .name span{color:#ffffffcc;font-size:46px;letter-spacing:3px;margin-left:14px}
  .sub{display:flex;align-items:center;gap:26px;margin:14px 0 34px}
  .btn{background:#ff0033;border-radius:26px;padding:4px 44px 0;font-size:150px;line-height:1.12;letter-spacing:4px;box-shadow:0 14px 0 #8a001c, 0 0 50px #ff003388;transform:rotate(-2deg)}
  .bell{width:120px;height:120px;flex:none}
  .goal{font-size:72px;letter-spacing:2px;line-height:1.05;color:#fff;text-shadow:0 6px 0 #000}
  .goal b{color:${b.accent};font-weight:normal}
  .bar{margin-top:14px;height:26px;width:860px;border-radius:13px;background:#ffffff22;border:3px solid #ffffff55;overflow:hidden}
  .bar i{display:block;height:100%;width:100%;background:repeating-linear-gradient(90deg, ${b.accent} 0 40px, ${b.accent}99 40px 80px)}
  </style></head><body>
  <svg class="bg" width="2560" height="1440" viewBox="0 0 2560 1440">
    <g stroke="${b.accent}" stroke-width="6" fill="none" opacity=".16">
      <line x1="1280" y1="0" x2="1280" y2="1440"/><circle cx="1280" cy="720" r="420"/>
      <rect x="40" y="380" width="300" height="680"/><rect x="2220" y="380" width="300" height="680"/>
      <rect x="40" y="40" width="2480" height="1360"/>
    </g>
    ${confetti}
  </svg>
  <div class="safe">
    <img class="logo" src="data:image/png;base64,${logoPng.toString('base64')}">
    <div class="txt">
      <div class="name">${b.name} <span>${b.handle}</span></div>
      <div class="sub"><div class="btn">SUBSCRIBE</div>
        <svg class="bell" viewBox="0 0 24 24"><path fill="${b.accent}" stroke="#000" stroke-width=".8" d="M12 22a2.5 2.5 0 0 0 2.45-2h-4.9A2.5 2.5 0 0 0 12 22zm7-6V11a7 7 0 0 0-5.5-6.84V3.5a1.5 1.5 0 0 0-3 0v.66A7 7 0 0 0 5 11v5l-2 2v1h18v-1z"/></svg>
      </div>
      <div class="goal">HELP ME HIT <b>1,000 SUBS</b> ⚽</div>
    </div>
  </div>
  </body></html>`;
}

(async () => {
  const browser = await chromium.launch();
  for (const b of BRANDS) {
    const out = path.join(__dirname, b.slug);
    fs.mkdirSync(out, { recursive: true });
    const page = await browser.newPage({ viewport: { width: 800, height: 800 } });
    await page.setContent(`<!doctype html><html><head><style>${fontCss}body{background:#000}</style></head><body>${b.logo()}</body></html>`);
    await page.evaluate(() => document.fonts.ready);
    const logoPng = await page.screenshot({ path: path.join(out, 'logo.png') });
    await page.close();

    const bp = await browser.newPage({ viewport: { width: 2560, height: 1440 } });
    await bp.setContent(bannerHtml(b, logoPng));
    await bp.evaluate(() => document.fonts.ready);
    await bp.screenshot({ path: path.join(out, 'banner.png') });
    // Vista de cómo se verá en el móvil (solo la zona segura)
    await bp.screenshot({ path: path.join(out, 'banner_safe_preview.png'), clip: { x: SAFE.x, y: SAFE.y, width: SAFE.w, height: SAFE.h } });
    await bp.close();
    console.log('ok', b.slug);
  }
  await browser.close();
})();
