# Formato de guion (`scripts/<id>.json`)

```json
{
  "id": "2026-11-21_goalkeepers-main-character",   // = nombre de la carpeta de clips
  "title_overlay": "Top Goalkeepers With Main Character Energy",  // caja blanca arriba
  "hook": "Number one should be illegal.",          // se dice sobre el clip #5
  "items": [
    {
      "rank": 5,
      "label": "Colombian Scorpion",                 // texto en la lista de ranking
      "line": "Bro saw the ball coming and chose cinema.",  // voz + subtítulos
      "clip_hint": "Higuita scorpion kick save, England vs Colombia, Wembley 1995",
      "clip": "5.mp4",      // opcional (por defecto busca 5.mp4/5.mov/...)
      "start": 2.5,         // opcional: segundo donde empieza el momento
      "end": 10.0           // opcional: segundo donde termina
    }
  ],
  "outro": "Who deserved number one? Comment.",       // se dice al final del #1
  "youtube": { "title": "...", "description": "...", "tags": ["..."] }
}
```

- Los items se ordenan solos de mayor a menor (5 → 1).
- Clips: `clips/<id>/5.mp4`, `4.mp4`, … `1.mp4`. Cualquier tamaño (horizontal o vertical);
  el programa lo encaja en 1080x1920 con fondo desenfocado.
- Si falta un clip, `render --preview` pone una tarjeta verde con el `clip_hint` para que
  veas el timing antes de conseguirlo.

## Videos largos (recopilaciones 16:9)
Mismos campos y además:
- `"format": "long"` → video 1920x1080, insignia "#N" + apodo, capítulos automáticos en la descripción.
- `line` puede ser más larga (2–3 frases, ~12–18 s); `line_short` = versión corta para los Shorts.
- 20 items con clips de ~15–18 s ≈ 6–7 min. Para **8 min o más** (anuncios a mitad de video) usa 25 items
  o clips más largos (`long_video.max_clip_seconds` en config.yaml).

## De un largo a Shorts
`python main.py split scripts/<largo>.json` crea `<id>_p1 … _p4` (5 puestos cada uno, con los números
reales #20–16, #15–11…). Los Shorts usan los clips del largo (`"clips_from"`), no hay que copiar nada.

## Un solo archivo de recopilación
Si tienes una recopilación larga en un único archivo, pon en cada item:
`"clip": "compilation.mp4", "start": 125.0, "end": 141.5` (segundos del momento).

## Momento clave (`key`)
`"key": 14.5` = segundo del gol/momento dentro del clip. Los Shorts cortados de clips largos centran
su ventana de ~10 s en `key` (sin `key`, en el centro del clip). Codex lo usará también para el zoom.
