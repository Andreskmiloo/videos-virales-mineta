"""Overlay graphics (title box + ranking list) drawn with Pillow."""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

YELLOW = (255, 214, 0, 255)
WHITE = (255, 255, 255, 255)
RED = (255, 59, 48, 255)
BLACK = (0, 0, 0, 255)


def _wrap(draw: ImageDraw.ImageDraw, text: str, font, max_w: int) -> list[str]:
    lines, cur = [], ""
    for word in text.split():
        test = f"{cur} {word}".strip()
        if draw.textlength(test, font=font) <= max_w:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def _fit_font(draw, text, font_file, start, max_w, max_lines):
    size = start
    while size > 30:
        font = ImageFont.truetype(font_file, size)
        lines = _wrap(draw, text, font, max_w)
        if len(lines) <= max_lines:
            return font, lines
        size -= 4
    font = ImageFont.truetype(font_file, size)
    return font, _wrap(draw, text, font, max_w)


def overlay(
    out: Path, *, W: int, H: int, font_file: str, title: str, handle: str,
    ranks: list[int], revealed: dict[int, str], current: int | None,
) -> Path:
    """Transparent full-frame PNG: title box on top, numbered list bottom-left.

    ranks: all rank numbers in the video, e.g. [1,2,3,4,5]
    revealed: rank -> label already shown (current included)
    current: rank being shown now (highlighted in red with an arrow)
    """
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    # --- title box ---
    font, lines = _fit_font(d, title.upper(), font_file, 64, W - 200, 2)
    line_h = font.size + 12
    box_h = line_h * len(lines) + 50
    top = 170
    d.rounded_rectangle([60, top, W - 60, top + box_h], radius=28, fill=WHITE,
                        outline=YELLOW, width=8)
    y = top + 25
    for ln in lines:
        w = d.textlength(ln, font=font)
        d.text(((W - w) / 2, y), ln, font=font, fill=BLACK)
        y += line_h
    hfont = ImageFont.truetype(font_file, 34)
    hw = d.textlength(handle, font=hfont)
    d.text(((W - hw) / 2, top + box_h + 14), handle, font=hfont, fill=WHITE,
           stroke_width=3, stroke_fill=BLACK)

    # --- ranking list ---
    rfont = ImageFont.truetype(font_file, 58)
    row = 92
    y0 = H - 200 - row * len(ranks)
    for i, r in enumerate(sorted(ranks)):
        y = y0 + i * row
        x = 60
        is_cur = r == current
        if is_cur:  # arrow
            d.polygon([(x - 40, y + 14), (x - 40, y + 50), (x - 10, y + 32)], fill=RED)
        num_color = RED if is_cur else YELLOW
        d.text((x, y), f"{r}.", font=rfont, fill=num_color, stroke_width=5, stroke_fill=BLACK)
        if r in revealed:
            label = revealed[r]
            lf = rfont
            max_w = W - x - 110 - 40
            size = 58
            while d.textlength(label, font=lf) > max_w and size > 30:
                size -= 4
                lf = ImageFont.truetype(font_file, size)
            d.text((x + 100, y + (58 - size) // 2), label, font=lf,
                   fill=RED if is_cur else WHITE, stroke_width=5, stroke_fill=BLACK)
    img.save(out)
    return out


def placeholder(out: Path, *, W: int, H: int, font_file: str, rank: int, hint: str) -> Path:
    """Card shown when a clip is missing, so you can preview timing before finding clips."""
    img = Image.new("RGB", (W, H), (20, 60, 30))
    d = ImageDraw.Draw(img)
    for x in range(0, W, 120):  # pitch stripes
        if (x // 120) % 2:
            d.rectangle([x, 0, x + 119, H], fill=(24, 72, 36))
    big = ImageFont.truetype(font_file, 90)
    msg = f"MISSING CLIP #{rank}"
    d.text(((W - d.textlength(msg, font=big)) / 2, H * 0.27), msg, font=big, fill=YELLOW,
           stroke_width=4, stroke_fill=BLACK)
    small = ImageFont.truetype(font_file, 44)
    y = H * 0.27 + 130
    for ln in _wrap(d, hint or "", small, W - 160)[:6]:
        d.text(((W - d.textlength(ln, font=small)) / 2, y), ln, font=small, fill=WHITE)
        y += 58
    img.save(out)
    return out
