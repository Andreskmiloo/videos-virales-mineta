# Miniaturas (thumbnails) + prompt para ChatGPT

> En **Shorts** la miniatura casi no se ve (el feed reproduce solo). Importa en los **videos largos**
> y en búsquedas/pestaña del canal. Prioridad: miniatura de cada recopilación larga.

## Lo que hacen las miniaturas virales (análisis de 8 outliers de recopilaciones, nov-2026)
Videos analizados: "LEGENDARY Goal of Every Year (2000–2026)" (483K vistas, 127× breakout, canal de 5K subs),
"Puskas Goals 2026 – 20 Possible Nominees" (1,3M, 531×), "100 Insane Goals Already Happened in 2026/27" (285K, 65×),
"50 BANGER Goals Scored in 2026" (991K, 80×), "1 in a Billion Football Moments" (471K, 38×),
"Puskas Award 2026 • 25 Possible Candidates" (1,3M, 24×), "Best Goals in Football 2026/2027" (259K, 62×),
"1 Iconic Goal From EVERY MINUTE" (318K).

Patrones que se repiten:
1. **UN jugador recortado en acción extrema** (chilena, volea, disparo) o con **cara de shock**
   (manos en la cabeza, señalándose la sien). Nunca un grupo, nunca un plano lejano.
2. **Texto enorme de 1–3 palabras**, normalmente **un número** ("25", "50", "100", "2026") + palabra potente
   ("INSANE", "BEST GOALS", "PUSKAS"). Amarillo o blanco, contorno/sombra negra, a veces 3D.
3. **Texto detrás del jugador** (efecto profundidad: el jugador tapa parte de las letras).
4. **Fondo simple**: césped verde saturado o estadio desenfocado. Alto contraste y colores saturados.
5. **Un efecto extra como mucho**: rayo, flecha amarilla con la trayectoria del balón, "0.1%".
6. Composición: jugador en un lado (1/3), texto en el otro. Se lee perfecto en tamaño móvil.

Lo que NO hacen: mucho texto, frases largas, varios jugadores pequeños, colores apagados.

## Reglas para nuestras miniaturas
- 1280×720 (16:9), JPG/PNG < 2 MB.
- Máx. 3 palabras + 1 número. El texto NO repite el título, lo complementa.
- 1 jugador, 1 emoción/acción, 1 efecto. Saturado. Se tiene que entender en 1 segundo en un móvil.
- Probar 2–3 versiones (YouTube "Test & compare") y quedarse con la que gane.

## ⚠️ Antes de usar ChatGPT con jugadores reales
- ChatGPT puede negarse a **generar** la cara de un jugador real desde cero, y no debemos inventar
  escenas falsas de personas reales. **Lo seguro y mejor**: hacer captura de un fotograma de TU clip
  (el momento clave en alta calidad) y pedirle a ChatGPT que **lo edite** (recortar, texto, efectos).
- Evita escudos y logos grandes de clubes/ligas en la miniatura (marca registrada).
- La miniatura debe mostrar algo que **sí sale en el video** (si no, YouTube lo trata como engañoso).

## PROMPT A — editar un fotograma de tu clip (recomendado)
Sube a ChatGPT la captura y pega esto (cambia lo que va entre [ ]):

```
Create a YouTube thumbnail, 1280x720 (16:9), from the image I uploaded.

Style: viral soccer compilation thumbnail, like top sports YouTube channels. High contrast,
very saturated colors, sharp, clean, readable on a phone.

Composition:
- Cut out the main player from my image and place him on the [left/right] third, large,
  in his action pose, with a subtle white outline/glow so he pops.
- Background: bright saturated green pitch with a soft blurred stadium and light vignette.
- Big bold text on the other side: "[NUMBER]" on top in bright yellow (#FFD600) and
  "[1-2 WORDS]" below in white, heavy condensed sans-serif font, thick black outline and
  drop shadow, slightly 3D. Part of the text should go BEHIND the player for depth.
- One extra effect only: [yellow curved arrow showing the ball trajectory / small lightning
  bolts behind the player / glowing ball].

Rules: no club logos or league logos, no extra text, no watermark, keep the player's real
appearance from my image, do not add other people. Leave the bottom-right corner clear
(YouTube shows the video length there).
```

Ejemplos para [NUMBER] / [1-2 WORDS]:
- Top 20 aura → "20" / "MOST AURA"
- Puskás 2026 → "2026" / "PUSKAS?"
- 1 gol de cada Mundial → "1986–2026" / "LEGENDARY"
- Momentos 1 en un billón → "0.0001%" / "LUCK?"

## PROMPT B — sin foto (figura genérica, sin cara reconocible)
```
Create a YouTube thumbnail, 1280x720 (16:9), for a soccer compilation video titled
"[VIDEO TITLE]".
Show a dynamic soccer player (generic, not a real person, plain [color] kit with no logos,
face partly hidden by motion/shadow) doing a [bicycle kick / volley / long shot] on a bright
saturated green pitch with a blurred stadium at night, dramatic rim lighting.
Big bold text: "[NUMBER]" in yellow (#FFD600) and "[1-2 WORDS]" in white, heavy condensed
font, thick black outline, slight 3D, partly behind the player. One effect: [lightning /
trajectory arrow]. High contrast, viral YouTube style, no logos, no watermark, nothing in the
bottom-right corner.
```

## Después de generar
1. Mírala en pequeño (como en el móvil): ¿se lee el número y se entiende en 1 segundo?
2. Guárdala como `output/<id>/thumbnail_custom.jpg`.
3. Súbela en YouTube Studio y, si tienes acceso, usa "Test & compare" con 2–3 versiones.
