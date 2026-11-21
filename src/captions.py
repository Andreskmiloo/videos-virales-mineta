"""Karaoke-style captions (.ass): 1-3 words on screen, current word in yellow."""
from __future__ import annotations

from pathlib import Path

Words = list[tuple[float, float, str]]


def _ts(t: float) -> str:
    t = max(t, 0)
    h, rem = divmod(t, 3600)
    m, s = divmod(rem, 60)
    return f"{int(h)}:{int(m):02d}:{s:05.2f}"


def _esc(w: str) -> str:
    return w.replace("\\", "").replace("{", "(").replace("}", ")")


def write_ass(words: Words, out: Path, *, W: int, H: int, font_name: str, font_file: str,
              y: int | None = None, max_words: int = 3, size: int = 92) -> Path:
    from PIL import ImageFont

    measure = ImageFont.truetype(font_file, size)
    y = y or int(H * 0.56)
    head = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,{font_name},{size},&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,7,3,5,40,40,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    lines = []
    # group words into chunks
    chunks: list[Words] = []
    cur: Words = []
    for w in words:
        cur.append(w)
        if len(cur) >= max_words or w[2].endswith((".", "!", "?", ",")):
            chunks.append(cur)
            cur = []
    if cur:
        chunks.append(cur)

    for chunk in chunks:
        for i, (s, e, _) in enumerate(chunk):
            # keep the chunk on screen until the next word starts (no flicker)
            end = chunk[i + 1][0] if i + 1 < len(chunk) else e + 0.08
            parts = []
            for j, (_, _, word) in enumerate(chunk):
                word = _esc(word.upper())
                parts.append("{\\c&H00D6FF&}" + word + "{\\c&HFFFFFF&}" if j == i else word)
            plain = " ".join(w[2].upper() for w in chunk)
            width = measure.getlength(plain) * 1.08  # + outline
            fs = size if width <= W - 80 else int(size * (W - 80) / width)
            pop = "{\\fscx112\\fscy112\\t(0,90,\\fscx100\\fscy100)}" if i == 0 else ""
            text = f"{{\\pos({W // 2},{y})\\fs{fs}}}{pop}" + " ".join(parts)
            lines.append(f"Dialogue: 0,{_ts(s)},{_ts(end)},Cap,,0,0,0,,{text}")
    out.write_text(head + "\n".join(lines) + "\n", encoding="utf-8")
    return out
