"""Upload a rendered Short to YouTube (Data API v3, OAuth)."""
from __future__ import annotations

import json
from pathlib import Path

from .common import ROOT

SCOPES = ["https://www.googleapis.com/auth/youtube.upload",
          "https://www.googleapis.com/auth/youtube.readonly"]


def _service():
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build

    secret = ROOT / "client_secret.json"
    token = ROOT / "token.json"
    creds = Credentials.from_authorized_user_file(str(token), SCOPES) if token.exists() else None
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not secret.exists():
                raise SystemExit("client_secret.json missing — see README section 'Subir a YouTube'.")
            creds = InstalledAppFlow.from_client_secrets_file(str(secret), SCOPES).run_local_server(port=0)
        token.write_text(creds.to_json())
    return build("youtube", "v3", credentials=creds)


def upload(out_dir: Path, cfg: dict, *, publish_at: str | None = None, force: bool = False) -> str:
    from googleapiclient.http import MediaFileUpload

    meta = json.loads((out_dir / "metadata.json").read_text(encoding="utf-8"))
    if meta.get("missing_clips") and not force:
        raise SystemExit(f"Video has placeholder cards for ranks {meta['missing_clips']}. "
                         "Add the clips and render again (or pass --force).")
    yt = _service()

    want = cfg["channel"].get("channel_id")
    if want:
        mine = yt.channels().list(part="id", mine=True).execute().get("items", [])
        if want not in [c["id"] for c in mine]:
            raise SystemExit(f"Logged-in account does not own channel {want}. "
                             "Delete token.json and log in with the right account.")

    up = cfg["upload"]
    title = meta["title"][:100]
    desc = meta.get("description", "")
    if "#shorts" not in (title + desc).lower():
        desc += "\n\n#shorts"
    status = {"privacyStatus": up["privacy"], "selfDeclaredMadeForKids": up["made_for_kids"]}
    if publish_at:  # scheduled release requires private
        status.update(privacyStatus="private", publishAt=publish_at)
    body = {
        "snippet": {"title": title, "description": desc, "tags": meta.get("tags", [])[:30],
                    "categoryId": up["category_id"], "defaultLanguage": "en",
                    "defaultAudioLanguage": "en"},
        "status": status,
    }
    media = MediaFileUpload(str(out_dir / "video.mp4"), chunksize=-1, resumable=True,
                            mimetype="video/mp4")
    req = yt.videos().insert(part="snippet,status", body=body, media_body=media)
    resp = None
    while resp is None:
        _, resp = req.next_chunk()
    vid = resp["id"]
    meta["uploaded_video_id"] = vid
    (out_dir / "metadata.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False))
    print(f"✔ uploaded: https://youtube.com/shorts/{vid}  ({status['privacyStatus']})")
    return vid
