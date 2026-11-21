#!/usr/bin/env python3
"""Football ranking Shorts — CLI.

  python main.py check                     # which clips are missing for each script
  python main.py render scripts/X.json     # build output/X/video.mp4
  python main.py render --all              # every script whose clips are complete
  python main.py upload output/X           # upload (private by default)
  python main.py write --count 3           # draft new scripts with Claude API (optional)
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from src.common import ROOT, find_clip, load_config, load_script


def _scripts(paths: list[str], all_: bool) -> list[Path]:
    if all_ or not paths:
        return sorted((ROOT / "scripts").glob("*.json"))
    return [Path(p) for p in paths]


def cmd_check(args, cfg):
    ready = 0
    for p in _scripts(args.scripts, True):
        s = load_script(p)
        d = ROOT / "clips" / s["id"]
        missing = [i for i in s["items"] if not find_clip(d, i)]
        if not missing:
            ready += 1
            print(f"READY   {s['id']}")
            continue
        print(f"MISSING {s['id']}  → put clips in clips/{s['id']}/")
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
            d = ROOT / "clips" / s["id"]
            if any(not find_clip(d, i) for i in s["items"]):
                print(f"skip {s['id']} (clips missing — use --preview to render with placeholders)")
                continue
        print(f"▶ {s['id']}")
        render(s, cfg)


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

    w = sub.add_parser("write")
    w.add_argument("--count", type=int, default=3)
    w.add_argument("--trends", help="text file with today's trend notes")

    args = ap.parse_args()
    cfg = load_config(Path(args.config) if args.config else None)
    {"check": cmd_check, "render": cmd_render, "upload": cmd_upload, "write": cmd_write}[args.cmd](args, cfg)


if __name__ == "__main__":
    sys.exit(main())
