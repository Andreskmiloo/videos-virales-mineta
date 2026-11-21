# Primer fin de semana del piloto (21–22 nov)

Rutina general y plan hasta enero: `docs/PLAN_PILOTO.md`. Fechas exactas: `docs/CALENDARIO.md`.
Ritmo: **1 Short al día** (programado a las 7 pm ET) **+ el largo Puskás el domingo a las 3 pm ET**.
Constancia antes que volumen: no subir muchos de golpe.

## SÁBADO (3–4 h)

### Bloque 1: preparación (1 h)
- [ ] Instalar Python y FFmpeg, y luego `pip install -r requirements.txt` (README §1).
- [ ] Dejar el canal listo (checklist A de `docs/PLAN_PILOTO.md`):
  - videos viejos en privado;
  - nombre, @, foto, banner y descripción en inglés;
  - verificar el teléfono.
- [ ] Poner el nombre y el @ en `config.yaml`.
- [ ] Probar `python main.py render scripts/2026-11-21_goals-broke-physics.json --preview`
  (no necesita clips; sirve para comprobar que la voz suena).

### Bloque 2: los Shorts de la semana (2–3 h)
Shorts del sábado 21 al viernes 27 (ver `docs/CALENDARIO.md`):
- `_p4` del Puskás;
- `goals-broke-physics`;
- `goalkeepers-main-character`;
- `wholesome-moments`;
- más `_p1`, `_p2` y `_p3`, que salen de los clips del largo (puedes dejarlos para el domingo).

Pasos: `python main.py check` → clips de 5–10 s → `python main.py render --all` → revisar cada video.
- [ ] Programar el `_p4` (hoy a las 7 pm ET) y el resto según el calendario.

## DOMINGO (2–4 h)

### Bloque 3: largo Puskás
- [ ] Clips de 25–32 s de los 15 goles en `clips/2026-11-22_puskas-2026-top15-long/`.
- [ ] `python main.py render scripts/2026-11-22_puskas-2026-top15-long.json`, y verlo entero (≥8 min).
- [ ] `render` de `_p1`, `_p2` y `_p3`. Usan los mismos clips del largo.
- [ ] Miniatura con ChatGPT: `docs/MINIATURAS.md`, PROMPT A, con un fotograma del gol de Güler.
- [ ] Programarlo a las **3 pm ET** con la descripción de `metadata.json` (los capítulos ya vienen incluidos).
- [ ] En cada Short del Puskás, poner el largo como "Related video".

### Bloque 4: métricas (15 min)
- Responder los comentarios en los primeros 30 min de cada publicación.
- A las 48 h, apuntar las métricas en `docs/RESULTADOS.csv`.
- El próximo sábado, pedirle a Claude la siguiente tanda de guiones.
