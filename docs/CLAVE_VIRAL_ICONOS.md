# La clave viral con iconos (nov-2026)

Fuentes: vidIQ trending Shorts (desde 15-oct-2026, por vistas/hora), búsquedas de Google 2026 y encuestas de EE.UU.
Resumen: **lo que más vistas junta ahora es apilar en el título los nombres más buscados**, en Shorts de
6–25 s con un gancho emocional o de duda. Nosotros lo hacemos **con voz propia** para poder monetizar.

## 1. Jugadores actuales que más vistas traen (en orden)
| # | Jugador | Por qué | Uso |
|---|---|---|---|
| 1 | **Cristiano Ronaldo** | Jugador más buscado en Google 2026; ~680M en Instagram | En casi todos los títulos |
| 2 | **Messi** (Inter Miami) | El más popular **en EE.UU.** (52% quiere su camiseta) | Siempre en títulos para EE.UU. |
| 3 | **Lamine Yamal** | El sub-20 más buscado; audiencia joven | Videos solo de él + VS |
| 4 | **Neymar** | 3º en redes (~233M); skills y "respect" virales | VS, skills, respeto |
| 5 | **Mbappé** | Top búsquedas; rivalidad con Yamal/Haaland | VS, remates |
| 6 | **Haaland** | Remates potentes, memes de robot | Remates, "power shots" |
| 7 | **Kenan Yildiz** | Aparece ya en títulos VS con 377K vistas en canales pequeños | Nombre "sorpresa" en VS |
| 8 | Bellingham, Vinícius, Pulisic | Pulisic = gancho EE.UU. (USMNT) | Mezclar, no protagonistas solos aún |

Regla: **mínimo 3 de los 5 primeros en cada título VS**. "Ronaldo vs Messi" solo ya está saturado, así que siempre se añade alguien joven (Yamal, Yildiz).

## 2. Formatos que más vistas juntan ahora (y si nos sirven)
| Formato | Ejemplo real (vidIQ) | Vistas | ¿Lo hacemos? |
|---|---|---|---|
| **Respect / kindness** de iconos | "Respect Neymar, Ronaldo, Haaland, Yamal, Mbappé" | 2,64M en 4 días | **Sí**, con voz y ranking |
| **VS multi-icono** | "Ronaldo vs Messi vs Yildiz vs Odegaard…" (canal de 3.960 subs) | 377K + 207K | **Sí**: "¿quién remata mejor?" con voz |
| Reacción | "Cristiano Ronaldo" (reacción, 35K subs) | 1,95M | No (hace falta cara/cámara) |
| **Find / Guess the player** (serie diaria "DAY 44") | PitchPeek, GoalMystery (canales de 28–2K subs) | 33K–163K cada uno | **Sí**: plantilla quiz (Codex), gráficos propios = casi sin riesgo de copyright |
| Skills graciosas, 6 s | "Neymar x Messi Funny Skills 😂" | 397K | Sí, dentro de un ranking con voz |
| Título con historia | "Mbappe Ruined What Could've Been A Neymar Masterpiece 😭" | 365K | **Sí**: un momento + narración |
| Juego (FC / FC Mobile) | "Barcelona" FC Mobile | 552K | Posible: EA permite monetizar vídeos del juego con anuncios |
| Animado con IA de jugadores reales | "Target Challenge Ronaldo vs Messi" | hasta 213K | **No**: caras reales generadas (riesgo de etiqueta IA y de "inauthentic") |

Ojo: muchos de estos canales tienen **muchas vistas y poca interacción** (0,3–1%). Son granjas de highlights sin
voz, y esas vistas **no se cobran** ("reused content") y además atraen reclamaciones. Copiamos el gancho, no el método.

## 3. Fórmulas de título (copiar y cambiar nombres)
- `Ronaldo vs Messi vs Yamal vs Mbappé vs Haaland: Best Finish? 🤯`
- `Respect Moments: Ronaldo, Messi, Neymar, Yamal 🤝😭`
- `Lamine Yamal Did THIS At 17 😳`
- `[Jugador] Ruined [Jugador]'s Masterpiece 😭`
- `Find Ronaldo in 5 Seconds 👀 (Day 1)` → serie numerada diaria
- Siempre en "Soccer" en la descripción/etiquetas para EE.UU.; en el título los nombres pesan más.

## 4. Reglas para que pegue
1. **6–25 s** para VS/respect; 25–35 s para rankings. Clip de cada jugador ≤ 5–6 s.
2. El jugador más buscado **en el primer segundo** (o el #1 anunciado en el gancho).
3. Final abierto para que comenten: "Who's #1? Wrong answers only."
4. Series numeradas (Day 1, Day 2…) → el algoritmo y el público esperan el siguiente.
5. Voz propia + apodos + ranking en cada clip (transformación obligatoria, ver CLAUDE.md).

## 5. Plan de volumen (encaja con 1 Short/día del piloto)
| Día | Formato |
|---|---|
| Lun | VS multi-icono ("best finish", "best free kick", "best skill") |
| Mar | Un solo jugador actual (Yamal / Mbappé / Haaland) |
| Mié | Quiz "Find/Guess the player" (cuando esté la plantilla) — hasta entonces, respect |
| Jue | Ranking de leyendas (los guiones ya hechos) |
| Vie | Respect / wholesome con iconos |
| Sáb | Título con historia ("X ruined Y's masterpiece") |
| Dom | Corte del largo (`split`) o el VS que mejor haya ido, versión 2 |

Primeros guiones: `scripts/2026-12-03_icons-best-finish-vs.json`,
`scripts/2026-12-04_yamal-did-this-at-17.json`, `scripts/2026-12-05_icons-respect-moments.json`.

## Fuentes
- vidIQ `trending_videos` (Shorts, 15-oct → 20-nov-2026, consulta multi-icono, orden por vistas/hora).
- Google 2026, jugadores más buscados: https://www.fifaworldcupnews.com/most-searched-soccer-player-internet-2026/ ·
  https://theportugalnews.com/news/ronaldo-most-searched-name-in-football-google/40514
- Seguidores: https://www.epidemicsound.com/blog/most-followed-on-social-media/ ·
  https://thesun.ng/ronaldo-messi-neymar-top-list-of-footballers-with-most-social-media-influence-in-2026/
- EE.UU. (Messi 52%, Ronaldo 44%): https://stacker.com/stories/sports/world-cup-fever-has-changed-american-attitudes-toward-soccer ·
  https://heavy.com/sports/soccer/messi-way-more-popular-than-usmnt-star-legend-claims/
- Política de contenido de EA (monetizar con anuncios permitido): https://help.ea.com/en/articles/security-and-rules/ea-content-policy/
- YouTube, contenido alterado/IA: https://support.google.com/youtube/answer/14328491
