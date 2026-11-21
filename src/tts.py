"""Text-to-speech with word timings (for karaoke captions)."""
from __future__ import annotations

import asyncio
import re
from pathlib import Path

from .common import probe_duration, run

# A word timing is (start_seconds, end_seconds, word)
Words = list[tuple[float, float, str]]


async def _edge(text: str, voice: str, rate: str, out: Path) -> Words:
    import edge_tts

    words: Words = []
    comm = edge_tts.Communicate(text, voice, rate=rate, boundary="WordBoundary")
    with open(out, "wb") as f:
        async for chunk in comm.stream():
            if chunk["type"] == "audio":
                f.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                start = chunk["offset"] / 10_000_000
                dur = chunk["duration"] / 10_000_000
                words.append((start, start + dur, chunk["text"]))
    return words


def _silent(text: str, out: Path) -> Words:
    """Offline stand-in: silence with estimated timings. Only for testing the pipeline."""
    tokens = text.split()
    words, t = [], 0.1
    for w in tokens:
        d = 0.12 + 0.055 * len(re.sub(r"\W", "", w))
        words.append((t, t + d, w))
        t += d + 0.04
    run(["ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
         "-t", f"{t + 0.2:.2f}", "-c:a", "libmp3lame", str(out)])
    return words


def speak(text: str, cfg: dict, out: Path) -> tuple[float, Words]:
    """Writes speech to `out` (mp3). Returns (duration_seconds, word timings)."""
    v = cfg["voice"]
    if v.get("provider", "edge") == "silent":
        words = _silent(text, out)
    else:
        try:
            words = asyncio.run(_edge(text, v["name"], v.get("rate", "+0%"), out))
        except Exception as e:  # network/TLS/blocked
            raise RuntimeError(
                f"edge-tts failed ({e}). Check your internet, or set voice.provider: silent to test."
            ) from e
    return probe_duration(out), words
