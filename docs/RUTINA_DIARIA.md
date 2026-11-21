# Rutina de cada mañana (≈30–60 min)

> **Semana tipo:** 1 recopilación larga (lunes) → `split` → 4 Shorts repartidos en la semana
> + 1–2 Shorts sueltos al día. Mismos clips, el doble de videos. Publicar 2–4 pm o 6–9 pm hora del Este (EE.UU.).

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
8. **A las ~48 h** apunta en `docs/RESULTADOS.csv` lo que dice YouTube Studio (shown in feed,
   viewed vs swiped, % medio visto, likes…) y compáralo con `docs/VIRALIDAD.md`.
   Claude lee ese archivo antes de escribir guiones nuevos para copiar lo que funcionó.
9. Si llega un claim/strike → apúntalo en `docs/STRIKES.md`.

## Consejos
- Constancia > volumen loco: 1–3 Shorts buenos al día. Subir 20 iguales activa "contenido masivo".
- El #1 siempre el mejor clip. El hook en los primeros 2 segundos.
- Responde comentarios los primeros 30 min: ayuda al algoritmo.
