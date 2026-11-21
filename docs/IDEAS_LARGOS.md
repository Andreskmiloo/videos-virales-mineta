# Ideas de videos largos (ranking) + plan de la idea #1 — 22-nov-2026

Fuentes: vidIQ (outliers de videos largos, keywords en EE.UU., notas de títulos), búsquedas web
en inglés (calendario, Mundial 2026, Puskás) y páginas de candidatos al Puskás
(Planet Football 02-oct-2026, GiveMeSport 04-nov-2026).

## Criterios
Demanda probada (outliers) · urgencia (ventana temporal) · encaje con público EE.UU. ·
riesgo de copyright · esfuerzo para conseguir clips · monetizable (narración propia).

## Ranking de ideas

| # | Idea (título de trabajo) | Por qué | Ventana | EE.UU. | Riesgo © |
|---|---|---|---|---|---|
| **1** | **Puskás 2026: 15 Goals That Could Win It** | Outliers recientes: "Puskas Goals 2026 – 20 nominees" 1,3M vistas, **531×** (canal de 5K subs); "25 Possible Candidates" 1,3M. Búsqueda "puskas award 2026" ≈ 9.500/mes. Título: **85/100** en vidIQ | **AHORA → gala FIFA** (en 2025 los nominados salieron el 13-nov y la gala fue el 16-dic; la fecha de 2026 no está confirmada) | Medio-alto (gol MLS de Gozo + goles del Mundial 2026) | Alto (goles recientes de ligas y Mundial) |
| 2 | **Every USMNT Goal at the 2026 World Cup, Ranked** 🇺🇸 | Récord de 30M+ espectadores en EE.UU.; tiro libre de Tillman vs Bosnia (el gol estadounidense más recordado), doblete de Balogun vs Paraguay, "Country Roads" | Dic–ene (nostalgia de fin de año) y siempre | **Máximo** | Alto (FIFA reclama mucho) |
| 3 | **Funniest Soccer Moments of 2026 (Ranked)** narrado | Canales de 1–5K subs con 500K–960K vistas y hasta **507×**. La mayoría NO narra → nuestra narración es la diferencia (y monetizable) | Siempre (serie) | Alto | Medio |
| 4 | **1 Legendary Goal From Every World Cup (1986–2026)** | Título: **92/100**. "LEGENDARY Goal of Every Year" hizo 127× | Siempre | Alto | Medio-alto |
| 5 | **Top 20 Soccer Goals With The Most Aura Ever** (ya escrito) | Título: **93/100**; "aura" probado (100M en Short) | Siempre | Alto | Medio (goles antiguos, menos reclamados) |
| 6 | **Best Soccer Goals of 2026 (Year in Review)** | Pico de búsquedas de recopilaciones anuales a finales de diciembre | 20-dic → 10-ene | Alto | Alto |
| 7 | **MLS Cup 2026 / Messi's Most Disrespectful MLS Moments** | Final de la MLS Cup el **18-dic** (FOX); Messi/Inter Miami = la audiencia más joven de la MLS | Semana del 18-dic | **Máximo** | Medio-alto |
| 8 | **1 in a Billion Soccer Moments Caught on Camera** | Original 471K vistas, 38× (canal de 4K subs) | Siempre | Alto | Medio |
| 9 | **1 Iconic Soccer Goal From EVERY MINUTE (1–90)** | Formato serie probado (318K–997K) | Siempre | Alto | Medio |
| 10 | **Top 30 Goalkeepers Who Chose Violence** (largo de comedia) | Mismo tono que nuestros Shorts; los porteros son el tema más fuerte de FootyRanks | Siempre | Alto | Medio |

**Calendario cercano:** ventana internacional 24-nov→5-dic · Champions jornada 6 ~8/9-dic ·
MLS Cup 18-dic · gala The Best/Puskás ~mediados de dic (sin confirmar) · Boxing Day 26-dic ·
fin de año = recopilaciones "Best of 2026".

## Recomendación de formato (en vez de 15 min)
**Video largo de 8–10 min + 4 Shorts del mismo material.**
- Con **8 min o más** ya hay anuncios a mitad de video. 15 min obligan a buscar ~30 clips (hay
  ~15 candidatos buenos al Puskás), bajan la retención y suben el riesgo de copyright.
- 15 goles × ~32 s (jugada + gol + repetición + narración) ≈ 8 min.
- `split --size 4` → 4 Shorts (#15–12, #11–8, #7–4, #3–1) que llevan al video largo.

## Plan de la idea #1 — "Puskás 2026: 15 Goals That Could Win It"
Guion listo: `scripts/2026-11-22_puskas-2026-top15-long.json` (15 goles sacados de las listas citadas;
cada `clip_hint` dice qué buscar). Shorts: `scripts/…_p1 … _p4`.

**Día 1 (hoy-mañana)**
1. Revisa el guion. Hay 2 goles marcados **CHECK/WATCH IT FIRST** (Solanke y la fase del gol de Lopes Cabral).
2. Consigue los 15 clips de ~25–32 s cada uno (jugada, gol y 1 repetición) y guárdalos en
   `clips/2026-11-22_puskas-2026-top15-long/15.mp4 … 1.mp4`. Si están todos en un solo archivo,
   usa `clip` + `start`/`end` en cada item.
3. `python main.py check` → `python main.py render scripts/2026-11-22_puskas-2026-top15-long.json`.
4. Mira el video entero. Si dura menos de 8 min, el programa avisa: alarga los clips o añade menciones de honor.

**Día 2**
5. Miniatura con ChatGPT (`docs/MINIATURAS.md`, PROMPT A) a partir del fotograma del gol de Güler:
   texto "2026" + "PUSKAS?", con la trayectoria del balón como flecha amarilla.
6. Sube el largo (a mano en Studio): título, descripción con capítulos (salen solos en
   `metadata.json`) y miniatura. Publica entre las 2 y las 4 pm, hora del Este.

**Días 3–7**
7. Renderiza los 4 Shorts (`render --all`) y publica 1 al día. En cada Short, enlaza el video largo
   como "Related video" en Studio.
8. A las 48 h, apunta las métricas en `docs/RESULTADOS.csv`.

**Seguimiento (convierte la idea en serie)**
9. Cuando FIFA publique los nominados oficiales → video 2: **"Official Puskás 2026 Nominees, Ranked"**
   (reutiliza los clips que coincidan).
10. Tras la gala → Short rápido: "Did the right goal win?" (reacción y opinión).

## Riesgo de copyright de la idea #1 (aviso honesto)
Goles recientes de ligas y del Mundial = Content ID muy activo. Lo más probable es una **reclamación**
(los ingresos de ese video van al dueño), no un strike. Para reducir el riesgo:
- clips cortos y narración en todos;
- no usar música comercial;
- si una liga reclama mucho, quitar ese gol.

Anota cada reclamación en `docs/STRIKES.md`. Si el riesgo preocupa, empieza por la **idea #5**
(goles antiguos, ya escrita) y publica el Puskás después.

## Fuentes
- [Planet Football — Puskás 2026 contenders (02-oct-2026)](https://www.planetfootball.com/lists-and-rankings/puskas-award-2026-contenders-best-goals-of-the-year)
- [GiveMeSport — Puskás 2026 power rankings (04-nov-2026)](https://www.givemesport.com/puskas-award-power-rankings/)
- [The Best FIFA Football Awards 2025 (fechas del ciclo anterior)](https://en.wikipedia.org/wiki/The_Best_FIFA_Football_Awards_2025)
- [MLS Cup 2026 final el 18-dic](https://www.yardbarker.com/soccer/articles/mls_cup_2026_final_scheduled_for_dec_18/s1_17064_43604684)
- [Récord de audiencia del USMNT en el Mundial 2026 — Yahoo Sports](https://sports.yahoo.com/articles/usmnts-record-world-cup-run-070000262.html)
- [The Ringer — 29 razones por las que amamos el Mundial 2026](https://www.theringer.com/2026/07/20/world-cup/world-cup-fifa-2026-soccer-tournament-favorite-best-moments)
- [Las 50 mejores jugadas del Mundial 2026](https://www.kccrradio.com/2026/07/19/the-50-best-moments-of-the-2026-fifa-world-cup/)
- [Calendario 2026/27 — Yahoo Sports](https://ca.sports.yahoo.com/news/2026-27-football-calendar-every-061500812.html)
- [YouTube: el Mundial 2026 en cifras](https://blog.youtube/culture-and-trends/youtube-fifa-world-cup-2026-viewership-stats/)
