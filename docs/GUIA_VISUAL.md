# Guía visual (para Codex — dueño de lo visual y del arreglo de videos)

Codex se encarga del aspecto final de los videos y de arreglar los que salgan mal (con el programa
y/o con el editor que use el humano, p. ej. Astra). Claude prepara guiones, calendario y lista de clips.

## Identidad actual (mantener coherencia en todo el canal)
| Elemento | Valor actual | Dónde |
|---|---|---|
| Amarillo de marca | `#FFD600` | `src/graphics.py` (YELLOW), subtítulos `&H00D6FF&` en `src/captions.py` |
| Rojo "puesto actual" | `#FF3B30` | `src/graphics.py` (RED) |
| Caja de título | blanca, borde amarillo, texto negro, mayúsculas | `graphics.overlay()` / `overlay_long()` |
| Lista de ranking (Short) | abajo-izquierda, números amarillos, el puesto actual en rojo con flecha | `graphics.overlay()` |
| Insignia (largo) | "#N" negro sobre amarillo + apodo blanco | `graphics.overlay_long()` |
| Subtítulos | 1–3 palabras, MAYÚSCULAS, palabra actual en amarillo, contorno negro | `src/captions.py` |
| Fuente | DejaVu Sans Bold (cambiable en `config.yaml → video.font`) | |
| Golpe de bajo | en cada puesto nuevo (sintetizado, sin copyright) | `render._boom()` |

## Mejoras visuales prioritarias (en este orden)
1. **Fuente con más impacto**: Anton / Bebas Neue / Montserrat ExtraBold (Google Fonts, licencia OFL).
   Guardarla en `assets/fonts/` y apuntar `video.font` a ella. Comprobar que no se sale de la pantalla.
2. **Zoom suave (punch-in) en el momento clave**: campo opcional `key` por item (segundo del gol;
   los Shorts ya lo usan para centrar el corte) → zoom 100→112% durante ~0,6 s en `key`.
3. **Transición** de 0,15–0,25 s entre puestos (flash blanco o whip) + "whoosh" sintetizado.
4. **Barra de progreso** fina arriba en los Shorts (sube la retención al ver cuánto falta).
5. **Música de fondo opcional** muy baja (−25 dB), solo de la biblioteca de audio de YouTube
   (`assets/music/`, nunca música comercial).
6. Miniaturas de los largos: seguir `docs/MINIATURAS.md`.

## Reglas al arreglar videos
- La **voz con comentario** y el ranking deben quedar SIEMPRE (son lo que hace el video monetizable).
- El gol/momento clave tiene que verse **completo** en cada clip.
- Nada de logos de clubes en miniaturas ni música con copyright.
- Shorts: 25–45 s ideal. Largos: ≥ 8 min.
- Probar cada cambio con `python main.py render <script> --preview` y mirar fotogramas
  (Short 1080×1920, largo 1920×1080) antes de hacer commit.
- Si se edita a mano en un editor externo, exportar en H.264 + AAC, 30 fps, misma resolución, y
  guardar como `output/<id>/video_final.mp4` (sin borrar `video.mp4`).

## Checklist de calidad antes de publicar (Codex + humano)
- [ ] Engancha en 0–2 s (acción ya en pantalla + hook)
- [ ] Se lee el título y la lista en el móvil
- [ ] Subtítulos sincronizados, sin salirse
- [ ] Volumen: voz clara por encima del sonido del clip
- [ ] El #1 es claramente el mejor momento
- [ ] Sin pantallas negras, cortes raros ni tarjetas "MISSING CLIP"
