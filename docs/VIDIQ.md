# Cómo exprimir vidIQ (con plan de 150 créditos/mes)

El plan actual da **150 créditos al mes** (se renuevan el día 21). Cada llamada cuesta
5 créditos (ver un video: 10–25). Sin estrategia se acaban en dos días, así que los usamos
solo donde vidIQ da algo que no podemos sacar gratis.

## Presupuesto mensual (≈150)
| Uso | Herramienta | Coste | Frecuencia | Total/mes |
|---|---|---|---|---|
| Qué está explotando en Shorts de fútbol | `vidiq_outliers` (short, en, este mes) | 5 | 1/semana | 20 |
| Qué explota en TikTok/Reels (llega antes a YouTube) | `vidiq_instagram_tiktok_outlier_search` | 5 | 1/semana | 20 |
| Lo más rápido ahora mismo | `vidiq_trending_videos` (recentVphEngaged) | 5 | 1/semana | 20 |
| Puntuar el título antes de subir | `vidiq_score_title` | 5 | solo los 1–2 mejores de la semana | 40 |
| Qué pide la audiencia en comentarios | `vidiq_comment_insights` (discover/validate) | 5 | 2/mes | 10 |
| Diseccionar un viral nuevo | `vidiq_watch_shortform_content` | 10 | 2/mes | 20 |
| Reserva | — | — | — | 20 |

**Gratis:** `vidiq_balance`, `vidiq_job_poll`, `vidiq_trend_categories`.
Si una búsqueda no devuelve nada, vidIQ devuelve los créditos.

## Lo que ya sacamos (21-nov-2026)
- **Puntuación de título:** "Top Goalkeepers With Main Character Energy 🧤😈" = **84/100**
  (Short). El formato "Top + concepto meme + emoji" puntúa alto.
- **Comentarios de la audiencia** (425 canales del nicho, 4.978 comentarios encontrados, muestra de 240 hilos):
  - Piden **jugadores concretos y de actualidad**: "más Bellingham brothers" (229 likes),
    "más Anthony Gordon, solo sale 3 segundos", "más Mbangula". → Meter caras nuevas de la temporada.
  - La mayor queja es que **no se vea el momento clave**: "highlights sin el penalti" (1.062 likes),
    "7 goles en 3 min es criminal" (1.177 likes). → Cada clip debe mostrar la jugada completa.
  - Rechazo al teatro y a la falta de deportividad ("players with no shame") → buen tema para
    rankings tipo "Top dives that deserved an Oscar", con humor.
  - También piden listas muy concretas y raras ("best players whose surnames start and end
    with a vowel") → ideas de ranking inesperadas generan comentarios.
- Las categorías de outliers (`guess_the`, `tier_list`, `rating`) no dieron resultados para fútbol en
  Shorts → el formato **quiz/tier list de fútbol está poco explotado**: es una oportunidad, pero sin datos que lo validen.

## Cómo lo usa Claude cada semana
1. `outliers` + `tiktok/reels` + `trending` → 5–10 temas candidatos.
2. Cruzar con `docs/RESULTADOS.csv` (lo que nos funcionó) y búsqueda web (noticias de la semana).
3. Escribir guiones → `score_title` solo al mejor título de cada tanda (hay que estar por encima de 75).
4. Guardar los hallazgos aquí y en CLAUDE.md.
