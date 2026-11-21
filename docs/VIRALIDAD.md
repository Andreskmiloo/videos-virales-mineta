# Márgenes de viralidad — YouTube Shorts (nov-2026)

Tres niveles de confianza:
- 🟢 **Oficial** (YouTube lo publica)
- 🟡 **Estudios/heurísticas** de terceros (muestras grandes, pero no oficiales; se contradicen a veces)
- 🔵 **Nuestros datos** (vidIQ sobre FootyRanks, RankZilla, Golazo Fx y outliers del mes)

> La referencia más fiable termina siendo **la mediana de tus últimos 10–20 Shorts**.
> Estos márgenes son el punto de partida; se ajustan con tus resultados en `docs/RESULTADOS.csv`.

## 1. Cómo decide YouTube (🟢 + 🟡)
- 🟢 Studio muestra **Shown in feed** (veces mostrado) y **Viewed vs. swiped away**
  (% que se quedó vs % que deslizó). Son las dos métricas del feed de Shorts.
- 🟡 Señales de ranking más citadas: % que no desliza, % medio visto (APV), replays,
  satisfacción (likes, comentarios, compartidos, encuestas).
- 🟡 Desde mar-2025 las "vistas" de Shorts cuentan cada reproducción; las **vistas comprometidas**
  (engaged views) son la métrica vieja y estricta, y son las que cuentan para **pagar** (YPP).
- 🟡 Funciona por tandas: muestra el Short a un grupo pequeño; si retiene, lo abre a más.
  Leer métricas tras **~48 h y ≥1.000 "shown in feed"**.

## 2. Los márgenes (tabla para revisar cada video)

| Métrica (YouTube Studio) | 🔴 Muere | 🟠 Normal | 🟢 Bueno | 🚀 Viral | Fuente |
|---|---|---|---|---|---|
| **Viewed vs swiped away** | < 50% | 50–60% | 60–70% | **≥ 70–80%** | 🟡 estudio 5.400 Shorts: <60% rinde mal, 70–90% rinde mejor |
| **% medio visto (APV)** | < 50% | 50–70% | 70–90% | **> 100%** (gente lo repite) | 🟡 |
| **Like / vista** | < 1% | 1–2% | 2–4% | **≥ 3–6%** | 🔵 outliers fútbol del mes: 2–6%; FootyRanks top: 1,6–2,6% |
| **Breakout** (vistas ÷ mediana del canal) | < 1× | 1–3× | 3–10× | **≥ 10×** | 🔵 vidIQ |
| **Duración** | > 60 s | 45–60 s | 30–45 s | **15–35 s** | 🟡 108K Shorts: pico en 11–20 s y cae >30 s; 🔵 refs: 26 s, 30–35 s, 43–57 s |

Notas 🔵 de nuestros datos:
- RankZilla vive en 0,9–1,2% de like/vista con cientos de millones de vistas: con mucho volumen
  el % de likes baja; **para canal pequeño apunta a ≥3%**.
- Granjas de contenido / reuploads suelen estar en 0,2–1% → si estamos ahí, el contenido no conecta.
- Golazo Fx: todos sus videos duran exactamente 26 s → fórmula fija que se repite.

## 3. Qué palancas mueven cada métrica (aplicar en guion y edición)
| Si falla… | Palanca |
|---|---|
| Swiped away alto | Hook en 0–2 s: el clip #5 debe tener acción YA (no intro), título claro arriba, frase de curiosidad ("Number one should be illegal"). |
| APV bajo | Clips de ≤ 6–8 s, cortar tiempos muertos, cada puesto mejor que el anterior, #1 = el mejor. |
| Pocos replays | Final que conecta con el inicio (loop), terminar justo tras el pico del #1, sin despedidas largas. |
| Pocos likes/comentarios | Ranking debatible a propósito, outro que pregunta ("Who deserved #1?"), apodos que la gente quiera corregir. |
| Breakout < 1× | Tema/título más específico y de tendencia (mirar outliers del día con vidIQ). |

## 4. Reglas que meto en cada guion (resumen)
1. Hablar ≤ 110 palabras; objetivo **25–40 s**.
2. Hook ≤ 10 palabras sobre el clip con acción inmediata.
3. Escalada 5 → 1, el #1 claramente el mejor.
4. Outro ≤ 10 palabras que provoque comentario y permita loop.
5. Humor/opinión propia en cada clip (también evita "reused content").

## Fuentes
- 🟢 [Understand your content reach and engagement — YouTube Help](https://support.google.com/youtube/answer/12220281?hl=en)
- 🟢 [YouTube Analytics basics — YouTube Help](https://support.google.com/youtube/answer/9002587?hl=en)
- 🟢 [Lanzamiento de "Viewed vs Swiped Away" — YouTube Community](https://support.google.com/youtube/community-video/273390203/new-youtube-shorts-metric-viewed-vs-swiped-away?hl=en)
- 🟡 [Estudio 3.300M vistas / 5.400 Shorts (Medium)](https://medium.com/@antoinelacombled/cracking-the-youtube-shorts-algorithm-a-study-of-3-3-billion-views-4711fdf7931b)
- 🟡 [Quso.ai: duración, 108.138 Shorts](https://quso.ai/research/youtube-shorts-length)
- 🟡 [OverseerOS: duración, 16.537 Shorts](https://www.overseeros.com/blog/best-youtube-shorts-length)
- 🟡 [Adobe Express: encuesta duración 2026](https://www.adobe.com/express/learn/blog/youtube-shorts-length-study)
- 🟡 [1of10: métricas de Shorts](https://1of10.com/blog/youtube-shorts-analytics/)
- 🟡 [Gyre: cambio en el conteo de vistas](https://gyre.pro/blog/youtube-shorts-view-count-update-impact-strategy-what-to-do-next)
- 🟡 [Retensis: métricas y benchmarks](https://retensis.com/blog/youtube-shorts-analytics-metrics-explained)
