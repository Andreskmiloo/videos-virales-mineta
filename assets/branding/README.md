# Branding del canal (3 opciones)

Regenerar: `node assets/branding/make_branding.js` (usa Playwright + las fuentes de `assets/fonts/`).

| Carpeta | Nombre | @ propuesto | Idea |
|---|---|---|---|
| `soccer-aura-ranked/` | Soccer Aura Ranked | @SoccerAuraRanked | Tendencia "aura" (top de FootyRanks: 100M); morado/dorado |
| `main-character-soccer/` | Main Character Soccer | @MainCharacterSoccer | "Main Character Energy" (título 84/100 en vidIQ); rojo |
| `ranked-soccer/` | Ranked Soccer | @RankedSoccer | Formato ranking, corto y claro; verde |

Cada carpeta tiene:
- `logo.png` — foto de perfil 800x800 (YouTube la muestra en círculo de 98 px).
- `banner.png` — 2560x1440, <6 MB.
- `banner_safe_preview.png` — la zona que se ve en todos los dispositivos (1546x423, centrada).
  Comprobar el recorte en YouTube Studio al subirlo.

Antes de elegir: comprobar en YouTube que el @ está libre. Luego poner nombre y @ en `config.yaml`
y editar `BRANDS` en `make_branding.js` si cambia el @.
Sin caras de jugadores ni escudos de clubes. Fuentes Anton y Bebas Neue: licencia OFL (`assets/fonts/OFL-*.txt`).
