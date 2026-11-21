# AGENTS.md (Codex / ChatGPT / other agents)

Read **CLAUDE.md** first — it holds the project goals, working agreements, anti-strike rules
and research notes. Everything there applies to you too.

Quick summary:
- English football ranking Shorts (Top 5 → #1). User speaks Spanish; videos are in English.
- The user supplies clips in `clips/<script-id>/5.mp4 … 1.mp4`. Never download match footage.
- New scripts go in `scripts/` following `docs/FORMATO_GUION.md` and `prompts/guionista.md`.
- Render: `python main.py render scripts/<id>.json` (use `--silent` offline, `--preview` without clips).
- Never upload public without user review. Never create channels to evade a YouTube ban.
- Never commit clips, `.env`, `client_secret*.json`, `token*.json`.
