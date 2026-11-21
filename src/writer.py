"""Optional: draft new ranking scripts with the Claude API (needs ANTHROPIC_API_KEY).

You can skip this and paste prompts/guionista.md into ChatGPT/Claude/Codex instead.
"""
from __future__ import annotations

import datetime as dt
import json
import re
from pathlib import Path

from .common import ROOT

ITEM = {
    "type": "object",
    "properties": {
        "rank": {"type": "integer"},
        "label": {"type": "string"},
        "line": {"type": "string"},
        "clip_hint": {"type": "string"},
    },
    "required": ["rank", "label", "line", "clip_hint"],
    "additionalProperties": False,
}
SCRIPT = {
    "type": "object",
    "properties": {
        "slug": {"type": "string"},
        "title_overlay": {"type": "string"},
        "hook": {"type": "string"},
        "items": {"type": "array", "items": ITEM},
        "outro": {"type": "string"},
        "youtube": {
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "description": {"type": "string"},
                "tags": {"type": "array", "items": {"type": "string"}},
            },
            "required": ["title", "description", "tags"],
            "additionalProperties": False,
        },
    },
    "required": ["slug", "title_overlay", "hook", "items", "outro", "youtube"],
    "additionalProperties": False,
}
SCHEMA = {
    "type": "object",
    "properties": {"scripts": {"type": "array", "items": SCRIPT}},
    "required": ["scripts"],
    "additionalProperties": False,
}


def _existing_titles() -> list[str]:
    out = []
    for p in sorted((ROOT / "scripts").glob("*.json")):
        try:
            out.append(json.loads(p.read_text(encoding="utf-8"))["title_overlay"])
        except Exception:
            pass
    return out


def write_scripts(cfg: dict, count: int, trends: str = "") -> list[Path]:
    import anthropic

    guide = (ROOT / "prompts" / "guionista.md").read_text(encoding="utf-8")
    used = "\n".join(f"- {t}" for t in _existing_titles()) or "(none yet)"
    user = (
        f"{guide}\n\n## Already made (do NOT repeat these topics)\n{used}\n\n"
        f"## Fresh trend notes for today\n{trends or '(none provided — use evergreen + current-season angles)'}\n\n"
        f"Write {count} NEW scripts. Return JSON only."
    )
    client = anthropic.Anthropic()
    resp = client.beta.messages.create(
        model=cfg["writer"]["model"],
        max_tokens=16000,
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",
        output_config={"effort": cfg["writer"].get("effort", "high"),
                       "format": {"type": "json_schema", "schema": SCHEMA}},
        messages=[{"role": "user", "content": user}],
    )
    if resp.stop_reason == "refusal":
        raise SystemExit("The model declined this request; adjust the trend notes and retry.")
    if resp.stop_reason == "max_tokens":
        raise SystemExit("Output was cut off; ask for fewer scripts (--count).")
    text = next(b.text for b in resp.content if b.type == "text")
    data = json.loads(text)

    today = dt.date.today().isoformat()
    paths = []
    for s in data["scripts"]:
        slug = re.sub(r"[^a-z0-9]+", "-", s.pop("slug").lower()).strip("-")[:50]
        s = {"id": f"{today}_{slug}", **s}
        p = ROOT / "scripts" / f"{s['id']}.json"
        p.write_text(json.dumps(s, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        paths.append(p)
        print(f"✔ {p.relative_to(ROOT)}  — {s['title_overlay']}")
    return paths
