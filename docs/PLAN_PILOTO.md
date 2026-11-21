# Plan piloto: del canal actual a un canal de soccer (21-nov-2026 → 31-ene-2027)

Objetivo: probar formatos con datos reales, trabajando **solo los fines de semana (4–8 h)**, y decidir el
**31 de enero** si se formaliza. El canal es prácticamente un lienzo en blanco: se rehace desde cero.

## 0. Punto de partida (comprobado en la página pública del canal, nov-2026)
- Canal `UCdHWzgDZoQbgBDDFXYvcvXQ`, creado en 2019, **31 suscriptores**, con un @ genérico.
- 3 videos viejos en español que no son de fútbol: 2 de un juego (2020) y 1 de sep-2026 con 0 vistas.
- Esos 31 suscriptores no son público de soccer, así que convertir el canal no hace perder nada.
- Sí se gana la antigüedad de la cuenta y el que ya esté verificada.
- Cambiar de tema reajusta a quién recomienda YouTube. Hay creadores que hablan de ~2 meses, pero
  es un dato no oficial. Con el canal casi vacío no hay público viejo que lo frene.

## A. Dejar el canal listo (una sola vez, ~1 h, el primer fin de semana)
- [ ] **Videos viejos → privado** (no borrarlos): Studio → Contenido → Visibilidad.
- [ ] **Nombre y @ nuevos** en inglés: Studio → Personalización → Información básica.
  - Ojo: solo se permiten unos 2 cambios cada 14 días, y el @ viejo queda reservado unos 14 días.
  - Ideas de nombre (comprobar a mano que el @ esté libre; no copiar el nombre de otro canal):
    `Soccer Aura Ranked` · `Ranked Soccer` · `Top Bins Soccer` · `Soccer Verdict` · `Main Character Soccer`.
  - Ponerlos después en `config.yaml` (`channel.name` y `channel.handle`).
- [ ] **Foto de perfil y banner**: pedírselos a ChatGPT con el estilo de `docs/MINIATURAS.md`
  (amarillo `#FFD600`, negro y blanco, un balón o un número, sin caras de jugadores reales ni logos).
- [ ] **Descripción en inglés**, por ejemplo:
  "Soccer rankings with zero chill. Top 5s, Puskás picks, legends vs. today's stars — new Shorts every day."
  Poner "soccer" 2–3 veces.
- [ ] **País e idioma del canal**:
  - idioma: inglés;
  - país: **el real**, porque afecta a AdSense e impuestos (no fingir EE.UU.).
- [ ] **Verificar el teléfono** (Studio → Configuración → Canal → Funciones aptas). Desbloquea las
  miniaturas propias y los videos de más de 15 min.
- [ ] **Valores de subida por defecto**: categoría Sports, idioma inglés, visibilidad privada,
  etiquetas base `soccer, soccer shorts, soccer highlights, soccer ranking`.
- [ ] **Listas de reproducción**: "Soccer Rankings", "Puskás 2026", "Long Compilations".
- [ ] Revisar que no haya avisos ni strikes (Studio → Configuración → Canal → Funciones aptas).

## B. Ritmo: 1 Short al día + 1 largo cada 2 semanas
- **1 Short al día**, a las **7 pm ET**. Todos se hacen en lote el fin de semana y se programan.
- **1 largo (8–10 min) cada 2 semanas**, el domingo a las **3 pm ET**. Sus 4 Shorts (`split`) se reparten en días
  alternos la semana siguiente.
- ¿Por qué no más?
  - No hay una frecuencia oficial. Para canales que todavía prueban formatos, varias guías recomiendan
    3–7 Shorts por semana, mantenidos 90 días.
  - **La constancia pesa más que el volumen**: mejor 1 al día durante meses que 3 al día y parar.
  - El estudio de vidIQ (10M de canales) asocia subir más a menudo con crecer más, pero eso es correlación,
    no causa.

### Rutina del fin de semana (4–8 h)
| Cuándo | Qué | Tiempo |
|---|---|---|
| Sáb | Pedir a Claude: **"lee RESULTADOS.csv y escribe los 7 guiones de la semana"** | 10 min |
| Sáb | `python main.py check` → conseguir los clips (`docs/FUENTES_CLIPS.md`, `docs/LISTA_CLIPS.md`) | 1,5–2 h |
| Sáb | `python main.py render --all` → revisar cada video (checklist de `docs/GUIA_VISUAL.md`) | 1 h |
| Sáb | Programar los 7 Shorts (`upload ... --publish-at` o Studio) con las horas de `docs/CALENDARIO.md` | 30 min |
| Dom (semana de largo) | Clips del largo → render → miniatura (ChatGPT) → programar a las 3 pm ET | 2–3 h |
| Dom | Apuntar las métricas a 48 h en `docs/RESULTADOS.csv` | 15 min |

**Fin de semana sin tiempo:** el mínimo viable son 3 Shorts programados (lunes, miércoles y viernes).
**Nunca** subir muchos de golpe para compensar: YouTube castiga lo masivo y repetitivo.

## C. Calendario de pruebas: una variable cada 2 semanas
Comparar solo los Shorts **nuevos** de cada bloque. Los Shorts que salen de un largo (`_p1`–`_p4`) son una
serie aparte y se miran por separado.

| Fines de semana (producción) | Qué se prueba en los Shorts | Largo del bloque |
|---|---|---|
| 21–22 nov y 28–29 nov | **Rankings de leyendas** (guiones ya escritos) | Puskás 2026 (dom 22-nov) |
| 5–6 dic y 12–13 dic | **Jugadores de actualidad**: Messi/Inter Miami, USMNT, figuras del momento | Top 20 Aura (dom 6-dic) |
| 19–20 dic y 26–27 dic | **Fin de año**: "Best / Funniest of 2026" (en diciembre suben esas búsquedas) | Funniest Soccer Moments of 2026 (dom 20-dic) |
| 2–3 ene y 9–10 ene | **Conceptos originales**: quiz "Guess the player", "What if…" | Every USMNT Goal at the 2026 World Cup (dom 3-ene) |
| 16–17 ene y 23–24 ene | **Repetir el formato ganador** con variaciones | Versión 2 del largo con mejores datos (dom 17-ene) |
| 30–31 ene | **Revisión final y decisión (punto D)** | — |

## D. Decisión del 31 de enero (fijada antes de empezar, para no engañarnos)
Datos en `docs/RESULTADOS.csv` (a 48 h, con ≥1.000 "shown in feed").

| Resultado | Condición | Qué se hace |
|---|---|---|
| **Formalizar** | Al menos una: un Short con breakout ≥10× o >10K vistas · viewed vs swiped ≥70% en 3+ Shorts · ≥300 suscriptores | Rutina fija, AdSense listo para cuando llegue el YPP y valorar el 2º canal (`docs/ESTRATEGIA.md`) |
| **Ajustar** | Ninguna de las anteriores, pero el % medio visto es ≥70% | Cambiar de formato o de sub-nicho (`docs/NICHOS.md`), 4 semanas más |
| **Repensar** | Casi todo por debajo del 50% en viewed vs swiped | Parar y replantear el concepto antes de seguir invirtiendo tiempo |

Cifras honestas:
- con ~60–70 Shorts, lo normal es acabar entre unos cientos y pocos miles de suscriptores;
- el YPP (1.000 subs + 10M de vistas de Shorts en 90 días) **no se promete** para enero;
- el piloto sirve para saber **qué formato funciona**, no para cobrar ya.

## E. Fechas especiales
- **Jue 26-nov, Thanksgiving**: mucha gente en casa con el móvil. Ese día sale el Short "wholesome" a las 3 pm ET.
- **Gala FIFA The Best / Puskás**: en cuanto salgan los nominados oficiales, guion "Official Puskás 2026 Nominees, Ranked".
- **Navidad (24–25 dic)**: dejar todo programado el 19–20 dic. Si el finde 26–27 no se puede trabajar, ya está cubierto.
- **Año nuevo**: el finde 2–3 ene empieza el bloque de conceptos originales (la plantilla quiz debe estar lista antes).

## F. Reglas del piloto
- Todo se sube en **privado** o programado y **el usuario lo revisa antes** de que salga.
- Siguen las reglas anti-strike de `CLAUDE.md`:
  - clips de 10 s como máximo;
  - voz propia en cada clip;
  - nada de música con copyright.
- Si llega un claim, anotarlo en `docs/STRIKES.md`.

## Fuentes (investigación web, nov-2026)
- Frecuencia y constancia:
  - https://vidiq.com/research/youtube-upload-frequency-study/
  - https://fluxnote.io/guides/youtube-shorts-optimal-upload-frequency-2026
  - https://fluxnote.io/guides/youtube-shorts-consistency-vs-quantity-2026
  - https://air.io/en/youtube-hacks/how-often-should-you-post-shorts-to-grow-faster
- Primeros videos de un canal: https://vidiq.com/research/youtube-first-10-videos-study/
- Reutilizar un canal viejo o cambiarle el tema:
  - https://uppbeat.io/blog/creator-questions/should-you-revive-an-old-youtube-channel-or-start-a-new-one/
  - https://www.overseeros.com/blog/youtube-channel-pivot-strategy
  - https://vidiq.com/blog/post/channel-refresh-youtube-growth/
  - https://www.opus.pro/blog/audience-content-fit-youtube-algorithm
- Crecer en YouTube: https://metricool.com/how-to-grow-on-youtube/
