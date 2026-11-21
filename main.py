#!/usr/bin/env python3
"""Football ranking Shorts — CLI.

  python main.py check                     # which clips are missing for each script
  python main.py render scripts/X.json     # build output/X/video.mp4
  python main.py render --all              # every script whose clips are complete
  python main.py upload output/X           # upload (private by default)
  python main.py split scripts/LONG.json   # long compilation -> Shorts (Part 1..N)
  python main.py write --count 3           # draft new scripts with Claude API (optional)
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from src.common import ROOT, clips_dir_for, find_clip, is_long, load_config, load_script


def _scripts(paths: list[str], all_: bool) -> list[Path]:
    if all_ or not paths:
        return sorted((ROOT / "scripts").glob("*.json"))
    return [Path(p) for p in paths]


def cmd_check(args, cfg):
    ready = 0
    for p in _scripts(args.scripts, True):
        s = load_script(p)
        d = clips_dir_for(s)
        missing = [i for i in s["items"] if not find_clip(d, i)]
        if not missing:
            ready += 1
            print(f"READY   {s['id']}")
            continue
        print(f"MISSING {s['id']}  → put clips in clips/{d.name}/")
        for i in missing:
            print(f"   {i['rank']}.mp4  {i.get('clip_hint', '')}")
    print(f"\n{ready} script(s) ready to render.")


def cmd_render(args, cfg):
    from src.render import render

    if args.silent:
        cfg["voice"]["provider"] = "silent"
    for p in _scripts(args.scripts, args.all):
        s = load_script(p)
        if args.all and not args.preview:
            d = clips_dir_for(s)
            if any(not find_clip(d, i) for i in s["items"]):
                print(f"skip {s['id']} (clips missing — use --preview to render with placeholders)")
                continue
        print(f"▶ {s['id']}")
        render(s, cfg)


def cmd_split(args, cfg):
    src = load_script(Path(args.script))
    if not is_long(src):
        raise SystemExit("split expects a script with \"format\": \"long\"")
    items = src["items"]  # already in countdown order (highest rank first)
    parts = [items[i:i + args.size] for i in range(0, len(items), args.size)]
    top = max(int(i["rank"]) for i in items)
    yt = src["youtube"]
    for k, chunk in enumerate(parts, 1):
        last = k == len(parts)
        lo, hi = int(chunk[-1]["rank"]), int(chunk[0]["rank"])
        short = {
            "id": f"{src['id']}_p{k}",
            "format": "short",
            "clips_from": src.get("clips_from", src["id"]),
            "title_overlay": f"{src['title_overlay']} (Part {k})",
            "hook": chunk[0].get("hook_short") or (
                f"Part {k} of the top {top}." + (" Number one is insane." if last else "")),
            "items": [{key: it[key] for key in ("rank", "label", "clip_hint", "clip", "start", "end")
                       if key in it} | {"line": it.get("line_short") or it["line"]}
                      for it in chunk],
            "outro": (src.get("outro") or "Who deserved number one? Comment.") if last
                     else f"Full top {top} on the channel.",
            "youtube": {
                "title": f"{yt['title']} (Part {k}: #{hi}-#{lo})"[:100],
                "description": f"Part {k} of {len(parts)}. Full top {top} on the channel.\n\n"
                               + yt.get("description", "") + "\n#shorts",
                "tags": yt.get("tags", []) + ["shorts"],
            },
        }
        out = ROOT / "scripts" / f"{short['id']}.json"
        out.write_text(json.dumps(short, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"✔ {out.relative_to(ROOT)}  (#{hi} → #{lo})")


def cmd_upload(args, cfg):
    from src.upload import upload

    for d in args.dirs:
        upload(Path(d), cfg, publish_at=args.publish_at, force=args.force)


def cmd_write(args, cfg):
    from src.writer import write_scripts

    trends = Path(args.trends).read_text(encoding="utf-8") if args.trends else ""
    write_scripts(cfg, args.count, trends)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    ap.add_argument("--config", help="path to config.yaml")
    sub = ap.add_subparsers(dest="cmd", required=True)

    c = sub.add_parser("check")
    c.add_argument("scripts", nargs="*")

    r = sub.add_parser("render")
    r.add_argument("scripts", nargs="*")
    r.add_argument("--all", action="store_true")
    r.add_argument("--preview", action="store_true", help="render even with missing clips")
    r.add_argument("--silent", action="store_true", help="no TTS (offline test)")

    u = sub.add_parser("upload")
    u.add_argument("dirs", nargs="+")
    u.add_argument("--publish-at", help="schedule, ISO 8601 UTC e.g. 2026-11-22T15:00:00Z")
    u.add_argument("--force", action="store_true")

    sp = sub.add_parser("split", help="long compilation script -> Short scripts")
    sp.add_argument("script")
    sp.add_argument("--size", type=int, default=5)

    w = sub.add_parser("write")
    w.add_argument("--count", type=int, default=3)
    w.add_argument("--trends", help="text file with today's trend notes")

    args = ap.parse_args()
    cfg = load_config(Path(args.config) if args.config else None)
    {"check": cmd_check, "render": cmd_render, "split": cmd_split, "upload": cmd_upload,
     "write": cmd_write}[args.cmd](args, cfg)


if __name__ == "__main__":
    sys.exit(main())
