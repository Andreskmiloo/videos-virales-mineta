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
