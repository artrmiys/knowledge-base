from __future__ import annotations

import argparse
import base64
import hashlib
import json
import mimetypes
import re
from pathlib import Path


DATA_URL_RE = re.compile(r"^data:(?P<mime>[^;,]+)?(?:;charset=[^;,]+)?;base64,(?P<data>.*)$", re.S)


def extension_for_mime(mime: str) -> str:
    if mime == "image/png":
        return ".png"
    if mime in {"image/jpeg", "image/jpg"}:
        return ".jpg"
    if mime == "image/webp":
        return ".webp"
    if mime == "image/gif":
        return ".gif"
    if mime == "image/svg+xml":
        return ".svg"
    return mimetypes.guess_extension(mime) or ".bin"


def main() -> int:
    parser = argparse.ArgumentParser(description="Decode browser-authenticated Twist images from data URLs.")
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    payload = json.loads(args.input.read_text(encoding="utf-8"))
    out_dir: Path = args.output
    out_dir.mkdir(parents=True, exist_ok=True)

    manifest = []
    for item in payload.get("results", []):
        data_url = item.get("dataUrl") or ""
        match = DATA_URL_RE.match(data_url)
        record = {
            "index": item.get("index"),
            "url": item.get("url"),
            "status": item.get("status"),
            "ok": item.get("ok"),
            "content_type": item.get("contentType"),
            "reported_size": item.get("size"),
        }
        if not match:
            record["decode_status"] = "missing-data-url"
            record["error"] = item.get("error")
            manifest.append(record)
            continue

        mime = match.group("mime") or item.get("contentType") or "application/octet-stream"
        data = base64.b64decode(match.group("data"))
        digest = hashlib.sha256(data).hexdigest()[:12]
        ext = extension_for_mime(mime)
        filename = f"twist-auth-image-{int(item.get('index') or 0):03d}-{digest}{ext}"
        path = out_dir / filename
        path.write_bytes(data)
        record.update(
            {
                "decode_status": "written",
                "mime": mime,
                "size": len(data),
                "sha256": hashlib.sha256(data).hexdigest(),
                "local_path": str(path),
            }
        )
        manifest.append(record)

    (out_dir / "manifest-browser-auth.json").write_text(
        json.dumps(
            {
                "source": str(args.input),
                "count": len(manifest),
                "written": sum(1 for row in manifest if row.get("decode_status") == "written"),
                "images": manifest,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"count={len(manifest)}")
    print(f"written={sum(1 for row in manifest if row.get('decode_status') == 'written')}")
    print(f"output={out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
