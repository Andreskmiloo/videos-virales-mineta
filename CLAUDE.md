# CLAUDE.md — videos-virales-mineta

Guía de trabajo para Claude (y cualquier IA: Codex, ChatGPT) en este proyecto.
Leer completo antes de tocar nada.

## Objetivo
Canal de **YouTube Shorts de fútbol en INGLÉS**, formato **ranking (Top 5 → #1)**,
con ideas originales y actuales, hecho de forma casi automática para crecer y monetizar.

## Cómo trabajamos (acuerdos con el usuario)
- El usuario habla en **español**: responderle en español. Los **videos y guiones van en inglés**.
- **El usuario consigue los clips**; Claude investiga tendencias, escribe los guiones y
  mantiene el código que monta y sube los videos. Codex/ChatGPT pueden ayudar con el mismo repo.
- **Investigar de verdad**: usar vidIQ (MCP) como fuente principal de datos de YouTube/TikTok/Reels,
  pero **no fiarse solo de vidIQ** — contrastar con búsqueda web y fuentes oficiales
  (YouTube Help, políticas) y citar fuentes.
- Rutina objetivo: **cada mañana** se generan guiones nuevos basados en lo que está pegando,
  el usuario pone los clips, se renderiza, **el usuario revisa** y se sube (privado/programado).
- Ser honesto con números y riesgos; no prometer viralidad ni dinero.

## Límites (no negociables)
- **No crear canales nuevos para evadir un cierre/baneo** de YouTube (va contra las normas y
  arriesga la cuenta de Google/AdSense). La estrategia es **evitar strikes**, no esquivarlos.
- No descargar ni redistribuir partidos/highlights por nuestra cuenta; los clips los aporta el usuario.
- No subir nada en público sin revisión del usuario (por defecto `privacy: private`).
- Nunca commitear clips, `.env`, `client_secret*.json` ni `token*.json`.

## Reglas anti-strike / anti-desmonetización (aplicar en cada guion)
- Cada clip ≤ ~8-10 s, solo el momento clave; nunca partidos o resúmenes enteros.
- **Transformación obligatoria**: voz en off original con humor/opinión en CADA clip,
  apodos propios, ranking, subtítulos, efectos. Compilaciones sin narración = "reused content".
- Variar formatos y textos (YouTube castiga lo "masivo/repetitivo": política *inauthentic content*, jul-2025).
- Música: solo de la biblioteca de audio de YouTube/Shorts o sin música (el sonido del clip va bajo).
- Si llega un claim/strike: anotarlo en `docs/STRIKES.md` (fecha, video, quién reclamó, tipo de clip)
  y ajustar las reglas aquí.

## Lo que aprendimos de los canales de referencia (nov-2026, vidIQ)
- **FootyRanks** (UCLQc7gcDAXeMOCsRvCgSX4Q): 648K subs en ~22 meses. Títulos
  "Top [adjetivo meme] [situación concreta] in Football 💀😭", 43-57 s, 5-6 clips de 8-10 s,
  lista numerada abajo-izquierda, apodos graciosos ("Bald French"=Zidane), voz IA con jerga
  (aura, cooking, bro thinks he's him), golpe de bajo en cada gol. Top: "Top Goals with most Aura" 100M.
- **RankZilla** (UCrVKjyaxfIOps6f1xV5D1nQ): 3,19M subs, no es solo fútbol. Rankings 30-35 s,
  5 clips de 5-7 s, título "DON'T CHECK THE SOUND 😭😭" repetido, escalada de intensidad, SFX meme.
- **Golazo Fx** (UCvK7EhgkPVhpoGYEZEKkodg): canal creado 22-ago-2026 → 119K subs y 164M vistas
  en 3 meses. Formato fijo de 26 s "[Jugador] Prime 🤯" (leyendas: Valverde, Pelé, R. Carlos…).
  Es un *edit* SIN voz: música phonk, build-up de entrenamiento → drop del beat en ~0:09 con
  goles, speed ramping, color grade contrastado, solo un texto fijo "[Jugador] Prime."
  Crece rapidísimo, pero edits solo-música son el caso de mayor riesgo de "reused content"
  para monetizar → si lo copiamos, añadir siempre algo propio (texto con dato/stat, voz corta).
- Tendencias del mes en Shorts: "Ranking Unexpected Football Edits", "Most Wholesome Football
  Moments", "Ranking Most Relatable Football Moments"; en Reels/TikTok: rankings con stats
  sorprendentes y "Top 3 moments that could be in movies".
- RPM de Shorts de fútbol: aprox. 0,03–0,30 USD por 1.000 vistas (fuentes de terceros). Hace falta
  volumen MUY alto; YPP exige 1.000 subs + 10M vistas de Shorts en 90 días (o 4.000 h).

## Márgenes de viralidad (detalle y fuentes en `docs/VIRALIDAD.md`)
- Viewed vs swiped away: muere <50% · normal 50–60% · bueno 60–70% · **viral ≥70–80%**.
- % medio visto (APV): bueno 70–90% · **viral >100%** (replays/loop).
- Like/vista: canal pequeño apuntar a **≥3%** (outliers de fútbol del mes 2–6%; granjas 0,2–1%).
- Breakout (vistas ÷ mediana del canal): **≥10× = viral**.
- Duración objetivo **25–40 s**; estudios dan pico en 11–30 s y caída pasado 30 s.
- Leer métricas a las ~48 h y con ≥1.000 "shown in feed". El usuario anota resultados en
  `docs/RESULTADOS.csv`; **antes de escribir guiones nuevos, leer ese CSV** y repetir lo que
  supera los márgenes / abandonar lo que no. Con datos propios, recalibrar estos márgenes.

## Vistas vs suscriptores / sub-nichos (detalle en `docs/NICHOS.md`)
- En Shorts YouTube paga por vista, no por suscriptor. Ratio vistas medias ÷ subs:
  canales jóvenes en racha 20–75×, maduros ~8× (FootyRanks, RankZilla), estancados ~1×.
- El mejor ratio lo tienen edits sin voz y highlights viejos, pero esas vistas **no se cobran**
  (reused content) y se llevan claims → no es nuestro camino.
- Nuestro foco: **rankings con voz** (interacción 1,6–2,1%) y **conceptos originales**
  ("What if", crossovers, quizzes, historias en 30 s), que llegan hasta 175× de breakout y 3,6%
  de interacción con riesgo de copyright casi cero.

## vidIQ (detalle y presupuesto en `docs/VIDIQ.md`)
- Plan de **150 créditos/mes** (se renueva el día 21); casi todo cuesta 5 y ver un video 10–25.
  Mirar `vidiq_balance` (gratis) antes de gastar y seguir el presupuesto de `docs/VIDIQ.md`.
- Hallazgos de comentarios: la audiencia pide **jugadores de actualidad** (Bellingham brothers,
  Anthony Gordon, Mbangula…) y odia que **no se vea el momento clave** → clips completos.
- Título de referencia: "Top Goalkeepers With Main Character Energy 🧤😈" = 84/100. Objetivo: ≥75.

## Estructura del proyecto
- `main.py` — CLI: `check`, `render`, `upload`, `write`.
- `src/` — `tts.py` (voz edge-tts + tiempos por palabra), `graphics.py` (caja de título + lista de
  ranking con Pillow), `captions.py` (subtítulos karaoke .ass), `render.py` (FFmpeg),
  `upload.py` (YouTube Data API), `writer.py` (guiones con Claude API, opcional).
- `scripts/*.json` — un guion por video (formato en `docs/FORMATO_GUION.md`).
- `clips/<id-del-guion>/5.mp4 … 1.mp4` — clips del usuario (no se suben a git).
- `output/<id>/video.mp4` + `metadata.json` — resultados.
- `prompts/guionista.md` — prompt para escribir guiones (sirve para Claude, ChatGPT o Codex).

## Notas técnicas
- En el contenedor cloud de Claude, edge-tts no funciona (el proxy no permite WebSockets):
  para probar usar `voice.provider: silent`. En el PC del usuario edge-tts sí funciona.
- Modelo para `write`: `claude-opus-5-5` (config `writer.model`).
- Verificar renders con `ffprobe` y capturas de frames antes de dar algo por bueno.
