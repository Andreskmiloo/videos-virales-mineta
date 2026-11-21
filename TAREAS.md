# Tablero de tareas (Claude · Codex · ChatGPT · humano)

Todas las IAs leen este archivo al empezar y lo actualizan al terminar.
Formato: `- [ ] tarea — responsable — notas`. Al acabar: `- [x]` + qué se hizo + commit.

## Reparto de roles
| Quién | Hace | No hace |
|---|---|---|
| **Humano (dueño del canal)** | Consigue los clips, revisa cada video, sube y publica, apunta las métricas en `docs/RESULTADOS.csv` | — |
| **Claude Code** | **Organización**: investigación, estrategia, guiones, calendario (`docs/CALENDARIO.md`), lista de clips (`docs/LISTA_CLIPS.md`), revisión de calidad, docs | Publicar sin revisión del humano |
| **Codex** | **Lo visual y arreglar videos** (con el programa y/o Astra): `docs/GUIA_VISUAL.md`, errores de render/instalación en el PC, mejoras de código y tests | Cambiar estrategia o reglas de CLAUDE.md sin avisar |
| **ChatGPT** | Miniaturas (prompt en `docs/MINIATURAS.md`), variantes de títulos, ideas rápidas | Escribir en el repo |

## Reglas para trabajar en equipo
1. **Antes de empezar**: `git pull`. **Al terminar**: commit pequeño y claro + `git push`.
2. Tomar una tarea = poner tu nombre en ella y hacer push (así la otra IA no la duplica).
3. No reescribir lo que hizo la otra IA sin motivo; si algo está mal, anotarlo aquí.
4. Reglas no negociables: las de `CLAUDE.md` (anti-strike, no evadir baneos, revisión humana, no commitear clips ni credenciales).

## Piloto 21-nov → 31-ene (ver `docs/PLAN_PILOTO.md`)
Ritmo: 1 Short al día (7 pm ET) + 1 largo cada 2 semanas (domingo 3 pm ET), todo en lote el fin de semana.

## En curso
- [ ] Dejar el canal listo (checklist A de `docs/PLAN_PILOTO.md`) y poner nombre y @ en `config.yaml` — humano
- [ ] Finde 21–22 nov: Shorts del 21 al 27 + largo Puskás, según `docs/SPRINT_FIN_DE_SEMANA.md` — humano
- [ ] Clips en el orden de `docs/LISTA_CLIPS.md` y publicación según `docs/CALENDARIO.md` — humano
- [ ] Primer render real en el PC (con voz edge-tts) y reportar errores — humano + Codex
- [ ] Cada domingo: métricas a 48 h en `docs/RESULTADOS.csv` — humano

## Pendiente (visual + código) — Codex (prioridad en `docs/GUIA_VISUAL.md`)
- [ ] Fuente con más impacto en los videos — Codex — Anton y Bebas Neue ya están en `assets/fonts/` (OFL); falta usarlas en `config.yaml`/`graphics.py`
- [ ] Transición corta + whoosh entre puestos — Codex
- [ ] Barra de progreso en Shorts — Codex
- [ ] Revisar y arreglar cada video del fin de semana antes de publicarlo (checklist de la guía) — Codex + humano
- [ ] `upload`: probar con credenciales reales y documentar el aviso de "proyecto no verificado = privado" — Codex
- [ ] Música de fondo opcional desde la biblioteca de audio de YouTube (archivo local en `assets/music/`, volumen bajo) — Codex
- [ ] Zoom suave (punch-in) en el momento clave (campo `key` por item, ya existe) — Codex
- [ ] Tests básicos: `load_script`, `split`, `captions.write_ass` (pytest) — Codex
- [ ] Plantilla **quiz** ("Guess the player"): cuenta atrás + respuesta revelada — Claude diseña, Codex implementa — **lista antes del 2-ene** (bloque de conceptos originales)

## Pendiente (contenido) — Claude (según el calendario de pruebas de `docs/PLAN_PILOTO.md`)
- [ ] Finde 5–6 dic: Shorts de **actualidad** con el plan semanal de `docs/CLAVE_VIRAL_ICONOS.md` (Messi/Inter Miami, USMNT, figuras del momento) para los días libres del bloque 2
- [ ] Tras los nominados oficiales del Puskás: guion "Official Puskás 2026 Nominees, Ranked"
- [ ] Finde 19–20 dic: largo "Funniest Soccer Moments of 2026 (Ranked)" (idea #3) + Shorts de fin de año
- [ ] Finde 2–3 ene: largo "Every USMNT Goal at the 2026 World Cup, Ranked" (idea #2) + Shorts quiz/"What if"
- [ ] 30–31 ene: informe de decisión con los datos de `docs/RESULTADOS.csv` (punto D del plan)
- [ ] Analizar las primeras métricas (`docs/RESULTADOS.csv`) y ajustar guiones

## Hecho
- [x] Investigación "clave viral con iconos" + jugadores actuales con más vistas (`docs/CLAVE_VIRAL_ICONOS.md`) y 3 Shorts de iconos actuales para el 3–5 dic — Claude
- [x] Branding: 3 nombres + logo y banner "SUBSCRIBE / help me hit 1,000 subs" para cada uno en `assets/branding/` — Claude
- [x] Pipeline de render (Shorts + largos 16:9 + split) — Claude
- [x] Investigación de canales, nichos, viralidad, EE.UU., títulos y miniaturas — Claude
- [x] Guiones: 8 Shorts, Top 20 aura (largo + 4 Shorts), Puskás 2026 (largo + 4 Shorts) — Claude
