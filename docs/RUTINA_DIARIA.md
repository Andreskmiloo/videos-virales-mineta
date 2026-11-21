# Rutina de producción (paso a paso)

> **Durante el piloto (nov–ene) esto se hace en lote el fin de semana**, no cada mañana: ver `docs/PLAN_PILOTO.md`.
> Ritmo: 1 Short al día (7 pm ET) + 1 largo cada 2 semanas → `split` → 4 Shorts. Cuando haya más tiempo, se puede
> pasar a 1–2 Shorts al día.

1. **Guiones nuevos (5 min)** — elige una opción:
   - Pídeselo a Claude Code en este repo: *"investiga con vidIQ lo que está pegando hoy en
     fútbol y escribe 3 guiones nuevos en scripts/"*. (También se puede dejar programado.)
   - O con tu API key: `python main.py write --count 3 --trends notas.txt`
   - O pega `prompts/guionista.md` en ChatGPT/Codex y guarda el JSON en `scripts/`.
2. **Revisa los guiones** — cambia lo que no te haga gracia. Tú conoces a tu público.
3. **Ver qué clips hacen falta**: `python main.py check`
4. **Consigue los clips** (5–10 s cada uno) y ponlos en `clips/<id>/5.mp4 … 1.mp4`.
5. **Renderiza**: `python main.py render --all`
6. **Mira cada video entero** en `output/<id>/video.mp4`. ¿Se oye bien? ¿Engancha en 2 s?
7. **Sube programado** (1 al día durante el piloto; fechas en `docs/CALENDARIO.md`):
   `python main.py upload output/<id> --publish-at 2026-11-22T15:00:00Z`
8. **A las ~48 h** apunta en `docs/RESULTADOS.csv` lo que dice YouTube Studio (shown in feed,
   viewed vs swiped, % medio visto, likes…) y compáralo con `docs/VIRALIDAD.md`.
   Claude lee ese archivo antes de escribir guiones nuevos para copiar lo que funcionó.
9. Si llega un claim/strike → apúntalo en `docs/STRIKES.md`.

## Consejos
- Constancia > volumen loco: 1 Short bueno al día mantenido meses gana a 3 al día y parar. Subir 20 iguales activa "contenido masivo".
- El #1 siempre el mejor clip. El hook en los primeros 2 segundos.
- Responde comentarios los primeros 30 min: ayuda al algoritmo.
