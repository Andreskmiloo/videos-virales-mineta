# Rutina de cada mañana (≈30–60 min)

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
7. **Sube programado** (1–3 al día, horas distintas):
   `python main.py upload output/<id> --publish-at 2026-11-22T15:00:00Z`
8. **A las 24–48 h** mira en YouTube Studio: retención, % que desliza, comentarios.
   Cuéntaselo a Claude para que los próximos guiones copien lo que funcionó.
9. Si llega un claim/strike → apúntalo en `docs/STRIKES.md`.

## Consejos
- Constancia > volumen loco: 1–3 Shorts buenos al día. Subir 20 iguales activa "contenido masivo".
- El #1 siempre el mejor clip. El hook en los primeros 2 segundos.
- Responde comentarios los primeros 30 min: ayuda al algoritmo.
