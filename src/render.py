"""Build a ranking video (vertical Short or 16:9 long compilation) from a script + clips."""
from __future__ import annotations

import json
import shutil
from pathlib import Path

from PIL import ImageFont

from . import captions, graphics, tts
from .common import (ROOT, clips_dir_for, dims, find_clip, font_path, has_audio, is_long,
                     need, probe_duration, run)


def _boom(path: Path) -> Path:
    """Original bass hit (synthesized, no copyright)."""
    if not path.exists():
        run(["ffmpeg", "-y", "-f", "lavfi", "-i",
             "aevalsrc='0.9*sin(2*PI*(70-40*t)*t)*exp(-5*t)':s=48000:d=0.9",
             "-ac", "2", str(path)])
    return path


def segment_texts(script: dict) -> list[str]:
    items = script["items"]
    texts = []
    for i, it in enumerate(items):
        t = it["line"].strip()
        if i == 0 and script.get("hook"):
            t = f"{script['hook'].strip()} {t}"
        if i == len(items) - 1 and script.get("outro"):
            t = f"{t} {script['outro'].strip()}"
        texts.append(t)
    return texts


def render(script: dict, cfg: dict, *, clips_root: Path | None = None,
           out_root: Path | None = None) -> Path:
    need("ffmpeg")
    need("ffprobe")
    v = cfg["video"]
    long_fmt = is_long(script)
    W, H, max_clip = dims(cfg, script)
    FPS = v["fps"]
    font_file = font_path(cfg)
    font_name = ImageFont.truetype(font_file, 10).getname()[0]

    sid = script["id"]
    clips_dir = clips_dir_for(script, clips_root)
    out_dir = (out_root or ROOT / "output") / sid
    work = ROOT / "work" / sid
    shutil.rmtree(work, ignore_errors=True)
    work.mkdir(parents=True)
    out_dir.mkdir(parents=True, exist_ok=True)
    (work / "fonts").mkdir()
    shutil.copy(font_file, work / "fonts" / Path(font_file).name)
    boom = _boom(work / "boom.wav")

    items = script["items"]
    ranks = [int(i["rank"]) for i in items]
    revealed: dict[int, str] = {}
    seg_files = []
    texts = segment_texts(script)
    missing = []
    chapters: list[tuple[float, str]] = []
    t_cursor = 0.0

    for n, (it, text) in enumerate(zip(items, texts)):
        r = int(it["rank"])
        revealed[r] = it["label"]
        tag = f"s{n:02d}"

        voice = work / f"{tag}_voice.mp3"
        vdur, words = tts.speak(text, cfg, voice)

        clip = find_clip(clips_dir, it)
        start = float(it.get("start", 0))
        if clip and not long_fmt and "start" not in it:
            # Short cut from a longer clip (e.g. one shared with a long video): centre the window
            # on the key moment ("key" = second of the goal) or, by default, on the clip middle.
            full = probe_duration(clip)
            if full > max_clip:
                key = float(it["key"]) if "key" in it else full / 2
                start = round(min(max(0.0, key - max_clip * 0.6), full - max_clip), 2)
        if clip:
            avail = probe_duration(clip) - start
            want = float(it["end"]) - start if it.get("end") else avail
            clip_dur = max(1.0, min(want, avail, max_clip))
        else:
            missing.append(r)
            clip_dur = 0.0
        seg_dur = round(max(clip_dur, vdur + 0.35), 2)

        if long_fmt:
            ovl = graphics.overlay_long(work / f"{tag}_ovl.png", W=W, H=H, font_file=font_file,
                                        title=script["title_overlay"],
                                        handle=cfg["channel"]["handle"],
                                        rank=r, label=it["label"], total=max(ranks))
            ass = captions.write_ass(words, work / f"{tag}.ass", W=W, H=H, font_name=font_name,
                                     font_file=font_file, y=int(H * 0.89),
                                     size=cfg["long_video"].get("caption_size", 64))
        else:
            ovl = graphics.overlay(work / f"{tag}_ovl.png", W=W, H=H, font_file=font_file,
                                   title=script["title_overlay"], handle=cfg["channel"]["handle"],
                                   ranks=ranks, revealed=dict(revealed), current=r)
            ass = captions.write_ass(words, work / f"{tag}.ass", W=W, H=H, font_name=font_name,
                                     font_file=font_file)

        cmd = ["ffmpeg", "-y"]
        if clip:
            loop = ["-stream_loop", "-1"] if clip_dur < seg_dur else []
            cmd += [*loop, "-ss", f"{start}", "-t", f"{clip_dur if not loop else seg_dur}",
                    "-i", str(clip)]
            clip_audio = has_audio(clip)
        else:
            ph = graphics.placeholder(work / f"{tag}_ph.png", W=W, H=H, font_file=font_file,
                                      rank=r, hint=it.get("clip_hint", ""))
            cmd += ["-loop", "1", "-framerate", str(FPS), "-t", f"{seg_dur}", "-i", ph.name]
            clip_audio = False
        cmd += ["-i", ovl.name, "-i", voice.name, "-i", boom.name]
        if not clip_audio:
            cmd += ["-f", "lavfi", "-t", f"{seg_dur}", "-i", "anullsrc=r=48000:cl=stereo"]
        a_clip = "0:a" if clip_audio else "4:a"

        fc = (
            f"[0:v]fps={FPS},setsar=1,split=2[a][b];"
            f"[a]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},"
            f"gblur=sigma=28,eq=brightness=-0.12[bg];"
            f"[b]scale={W}:{H}:force_original_aspect_ratio=decrease[fg];"
            f"[bg][fg]overlay=(W-w)/2:(H-h)/2[v1];"
            f"[v1][1:v]overlay=0:0[v2];"
            f"[v2]ass={ass.name}:fontsdir=fonts,format=yuv420p[v];"
            f"[{a_clip}]aresample=48000,volume={v['clip_audio_volume']}[ca];"
            f"[2:a]aresample=48000,adelay=150|150,volume={cfg['voice'].get('volume', 1.0)}[va];"
            f"[3:a]aresample=48000,volume={v['boom_volume']}[ba];"
            f"[ca][va][ba]amix=inputs=3:duration=longest:normalize=0[aout]"
        )
        seg = work / f"{tag}.mp4"
        cmd += ["-filter_complex", fc, "-map", "[v]", "-map", "[aout]", "-t", f"{seg_dur}",
                "-r", str(FPS), "-c:v", "libx264", "-preset", "veryfast", "-crf", "20",
                "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                "-ac", "2", seg.name]
        run(cmd, cwd=work)
        seg_files.append(seg)
        chapters.append((t_cursor, f"#{r} {it['label']}"))
        t_cursor += probe_duration(seg)
        print(f"  #{r} {it['label']!r}: {seg_dur:.1f}s" + ("  (MISSING CLIP)" if not clip else ""))

    lst = work / "list.txt"
    lst.write_text("".join(f"file '{s.name}'\n" for s in seg_files))
    video = out_dir / "video.mp4"
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", lst.name, "-c", "copy",
         "-movflags", "+faststart", str(video)], cwd=work)
    run(["ffmpeg", "-y", "-ss", "1.0", "-i", str(video), "-frames:v", "1",
         str(out_dir / "thumbnail.jpg")])

    meta = dict(script["youtube"])
    meta["script_id"] = sid
    meta["duration_seconds"] = round(probe_duration(video), 2)
    meta["missing_clips"] = missing
    meta["format"] = script["format"]
    if long_fmt and len(chapters) >= 3:
        def mmss(t: float) -> str:
            return f"{int(t // 60)}:{int(t % 60):02d}"
        chap = "\n".join(f"{mmss(t)} {name}" for t, name in chapters)
        meta["description"] = f"{meta.get('description', '').rstrip()}\n\n{chap}\n"
    (out_dir / "metadata.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False))
    total = meta["duration_seconds"]
    print(f"✔ {video}  ({total:.1f}s)" + (f"  missing clips: {missing}" if missing else ""))
    if long_fmt:
        min_s = cfg["long_video"].get("min_minutes", 8) * 60
        if total < min_s:
            print(f"  ⚠ {total / 60:.1f} min — under {min_s / 60:.0f} min there are no mid-roll ads "
                  "(add items, longer lines or longer clips).")
    elif total > 60:
        print("  ⚠ longer than 60s — best Shorts are 25–40s (trim lines or max_clip_seconds).")
    return video
