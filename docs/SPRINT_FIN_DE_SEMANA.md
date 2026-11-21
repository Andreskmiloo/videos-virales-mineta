# Sprint de fin de semana: canal funcionando el domingo por la noche

Objetivo realista: el domingo por la noche tener **1 video largo + 4–5 Shorts publicados** y
**6–8 Shorts programados** para toda la semana. Las vistas de un canal que arranca llegan en tandas:
YouTube prueba cada Short con poca gente y, si retiene, lo abre a más. **Constancia > subir 20 de golpe**
(subir muchos iguales de una vez parece contenido masivo).

## SÁBADO

### Bloque 1 — Preparación (1 h)
- [ ] Instalar Python + FFmpeg y luego `pip install -r requirements.txt` (README §1).
- [ ] Canal: revisar que no tenga strikes, verificar el teléfono, nombre/@/foto/banner/descripción
      en inglés, ocultar los videos viejos (ver la conversación o README).
- [ ] Poner nombre y @ en `config.yaml`.
- [ ] Probar: `python main.py render scripts/2026-11-21_goals-broke-physics.json --preview`
      (sin clips; comprueba que la voz suena).

### Bloque 2 — Primeros 3 Shorts (2–3 h) · clips fáciles de encontrar (goles clásicos famosos)
1. `2026-11-21_goals-broke-physics` (Roberto Carlos 1997, Zlatan 2012, Ronaldo knuckleball…)
2. `2026-11-21_goalkeepers-main-character` (Higuita, Neuer, Chilavert…)
3. `2026-11-22_puskas-2026-top15-long_p4` (Güler 68 m, Álvarez, Lopes Cabral) ← tema caliente

`python main.py check` → conseguir clips de 5–10 s → `python main.py render --all` → mirar cada uno.

### Bloque 3 — Publicar (30 min)
- [ ] Publicar **2 Shorts** entre las 6 y las 9 pm hora del Este (el #3, Puskás, primero).
- [ ] Programar el 3º para el domingo a mediodía (hora del Este).

## DOMINGO

### Bloque 4 — Video largo Puskás (3–4 h)
- [ ] Clips de 25–32 s para los 15 goles en `clips/2026-11-22_puskas-2026-top15-long/`
      (los Shorts _p1–_p4 los reutilizan; el _p4 ya usa los mismos).
- [ ] `python main.py render scripts/2026-11-22_puskas-2026-top15-long.json` → mirarlo entero (≥8 min).
- [ ] Miniatura con ChatGPT (`docs/MINIATURAS.md`, PROMPT A, fotograma del gol de Güler).
- [ ] Publicar el largo **a las 2–4 pm hora del Este** con la descripción de `metadata.json` (capítulos incluidos).

### Bloque 5 — Llenar la semana (1–2 h)
- [ ] `render --all` para los Shorts `_p1`, `_p2`, `_p3`, más `penalty-run-ups` y `celebrations-too-early`.
- [ ] Programar **1–2 Shorts al día de lunes a jueves** (alternando las 2–4 pm y las 6–9 pm, hora del Este).
- [ ] En cada Short del Puskás: "Related video" → el video largo.

## Lunes y siguientes días (15 min/día)
- Responder comentarios en los primeros 30 min de cada publicación.
- A las 48 h, apuntar las métricas en `docs/RESULTADOS.csv` y pedirle a Claude la siguiente tanda de guiones.
