"""Shared helpers: config, script loading, ffmpeg wrappers."""
from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
FONT_FALLBACKS = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    "/Library/Fonts/Arial Bold.ttf",
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "C:/Windows/Fonts/arialbd.ttf",
    "C:/Windows/Fonts/impact.ttf",
]


def load_config(path: Path | None = None) -> dict:
    with open(path or ROOT / "config.yaml", encoding="utf-8") as f:
        return yaml.safe_load(f)


def font_path(cfg: dict) -> str:
    for p in [cfg["video"].get("font"), *FONT_FALLBACKS]:
        if p and Path(p).exists():
            return p
    raise FileNotFoundError("No bold font found. Set video.font in config.yaml to a .ttf file.")


REQUIRED_ITEM_KEYS = {"rank", "label", "line"}


def load_script(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        s = json.load(f)
    for key in ("id", "title_overlay", "items", "youtube"):
        if key not in s:
            raise ValueError(f"{path}: missing '{key}'")
    for it in s["items"]:
        missing = REQUIRED_ITEM_KEYS - it.keys()
        if missing:
            raise ValueError(f"{path}: item {it} missing {missing}")
    s.setdefault("format", "short")
    if s["format"] not in ("short", "long"):
        raise ValueError(f"{path}: format must be 'short' or 'long'")
    # countdown order: highest rank first (5,4,3,2,1)
    s["items"] = sorted(s["items"], key=lambda i: -int(i["rank"]))
    return s


def is_long(script: dict) -> bool:
    return script.get("format", "short") == "long"


def dims(cfg: dict, script: dict) -> tuple[int, int, float]:
    """(width, height, max_clip_seconds) for the script's format."""
    sec = cfg["long_video"] if is_long(script) else cfg["video"]
    return sec["width"], sec["height"], sec["max_clip_seconds"]


def clips_dir_for(script: dict, clips_root: Path | None = None) -> Path:
    return (clips_root or ROOT / "clips") / script.get("clips_from", script["id"])


def need(binary: str) -> None:
    if not shutil.which(binary):
        raise SystemExit(f"'{binary}' not found. Install FFmpeg: https://ffmpeg.org/download.html")


def run(cmd: list[str], cwd: Path | None = None) -> None:
    res = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if res.returncode != 0:
        raise RuntimeError(f"Command failed: {' '.join(map(str, cmd))}\n{res.stderr[-2000:]}")


def probe_duration(path: Path) -> float:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
        capture_output=True, text=True, check=True,
    ).stdout.strip()
    return float(out)


def has_audio(path: Path) -> bool:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries", "stream=index",
         "-of", "csv=p=0", str(path)],
        capture_output=True, text=True,
    ).stdout.strip()
    return bool(out)


CLIP_EXTS = (".mp4", ".mov", ".mkv", ".webm", ".m4v")


def find_clip(clips_dir: Path, item: dict) -> Path | None:
    """Clip for an item: explicit item['clip'] or <rank>.<ext> inside clips/<script id>/."""
    if item.get("clip"):
        p = clips_dir / item["clip"]
        return p if p.exists() else None
    for ext in CLIP_EXTS:
        p = clips_dir / f"{item['rank']}{ext}"
        if p.exists():
            return p
    return None
