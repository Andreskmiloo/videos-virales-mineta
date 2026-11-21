# videos-virales-mineta ⚽

Generador de **YouTube Shorts de rankings de fútbol en inglés** (Top 5 → #1), al estilo de
FootyRanks / RankZilla: caja de título, lista de ranking que se va llenando, voz IA con humor,
subtítulos karaoke y golpe de bajo en cada puesto. Tú pones los clips; el programa hace el resto.

> Guía de trabajo y reglas: [CLAUDE.md](CLAUDE.md) · Rutina diaria: [docs/RUTINA_DIARIA.md](docs/RUTINA_DIARIA.md)
> · Investigación: [docs/INVESTIGACION.md](docs/INVESTIGACION.md)

## 1. Instalar (una vez)
1. Python 3.10+ y **FFmpeg** (https://ffmpeg.org/download.html — en Windows: `winget install ffmpeg`;
   en Mac: `brew install ffmpeg`).
2. En la carpeta del proyecto:
   ```bash
   pip install -r requirements.txt
   ```
3. Edita `config.yaml`: nombre y `@handle` de tu canal, voz, etc.

## 2. Hacer un video
```bash
python main.py check                                   # qué clips faltan
python main.py render scripts/2026-11-21_goals-broke-physics.json
python main.py render --all                            # todos los que tengan clips
python main.py render scripts/X.json --preview         # probar sin clips (tarjetas verdes)
```
Resultado: `output/<id>/video.mp4`, `thumbnail.jpg` y `metadata.json` (título, descripción, tags).

Voces que puedes poner en `config.yaml` → `voice.name`: `en-US-AndrewMultilingualNeural`,
`en-US-GuyNeural`, `en-US-ChristopherNeural`, `en-GB-RyanNeural`.

## 3. Guiones nuevos
- Formato: [docs/FORMATO_GUION.md](docs/FORMATO_GUION.md). Prompt para cualquier IA: [prompts/guionista.md](prompts/guionista.md).
- Con Claude API (opcional): `export ANTHROPIC_API_KEY=...` y `python main.py write --count 3`.

## 4. Subir a YouTube
1. En https://console.cloud.google.com crea un proyecto → activa **YouTube Data API v3** →
   *Credenciales* → *ID de cliente OAuth* tipo **App de escritorio** → descarga el JSON y
   guárdalo como `client_secret.json` en esta carpeta (no se sube a git).
2. Pon el ID de tu canal (UC…) en `config.yaml` → `channel.channel_id`.
3. `python main.py upload output/<id>` (la primera vez abre el navegador para iniciar sesión).
   Por defecto sube en **privado**. Para programar: `--publish-at 2026-11-22T15:00:00Z`.

## ⚠️ Importante
- Monetizar exige 1.000 subs + 10M vistas de Shorts en 90 días, y YouTube **no paga**
  compilaciones sin aporte propio. La voz con humor en cada clip es lo que lo hace tuyo.
- Clips cortos (5–10 s), nunca partidos enteros. Música solo de la biblioteca de YouTube.
- No hay garantía de viralidad ni de dinero: se aprende subiendo, midiendo y mejorando.
