"""Local receiver for authenticated browser source dumps.

The Playwright browser can read private Confluence/Trello pages after the user
logs in, but the shell cannot reuse those browser cookies.  This tiny local
HTTP server accepts already-extracted JSON from the browser and writes a raw
import dump under imports/live-sources/.
"""

from __future__ import annotations

import argparse
import base64
import json
import re
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OUT_ROOT = ROOT / "imports" / "live-sources"


def slugify(value: str, fallback: str = "page") -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9а-яё]+", "-", value, flags=re.IGNORECASE)
    value = value.strip("-")
    return (value[:90] or fallback).strip("-") or fallback


def table_to_markdown(rows: list[list[str]]) -> str:
    if not rows:
        return ""
    width = max(len(row) for row in rows)
    norm = [
        [(row[index] if index < len(row) else "").replace("|", "\\|") for index in range(width)]
        for row in rows
    ]
    header = norm[0]
    lines = [
        "| " + " | ".join(header) + " |",
        "| " + " | ".join(["---"] * width) + " |",
    ]
    lines.extend("| " + " | ".join(row) + " |" for row in norm[1:])
    return "\n".join(lines)


def write_image(image: dict[str, Any], folder: Path, stem: str, index: int) -> dict[str, Any]:
    data_url = image.get("dataUrl") or ""
    if not data_url.startswith("data:") or "," not in data_url:
        return {**image, "local": ""}
    meta, encoded = data_url.split(",", 1)
    mime = meta.split(";", 1)[0].replace("data:", "").lower()
    ext = {
        "image/jpeg": ".jpg",
        "image/jpg": ".jpg",
        "image/png": ".png",
        "image/gif": ".gif",
        "image/webp": ".webp",
        "image/svg+xml": ".svg",
    }.get(mime, ".bin")
    file_name = f"{stem}-{index:02d}{ext}"
    output = folder / file_name
    output.write_bytes(base64.b64decode(encoded))
    clean = {key: value for key, value in image.items() if key != "dataUrl"}
    clean["local"] = str(output.relative_to(OUT_ROOT)).replace("\\", "/")
    clean["file"] = file_name
    return clean


def page_to_markdown(page: dict[str, Any], images: list[dict[str, Any]]) -> str:
    title = page.get("title") or page.get("label") or "Imported Page"
    source_url = page.get("url") or ""
    imported = datetime.now(timezone.utc).isoformat()
    body = [f"# {title}", "", f"Source: {source_url}", "", f"Imported: {imported}", ""]

    text = (page.get("text") or "").strip()
    body.extend(["## Text", "", text or "_No text extracted._", ""])

    tables = page.get("tables") or []
    if tables:
        body.extend(["## Tables", ""])
        for table in tables:
            body.extend(
                [
                    f"### Table {(table.get('index') or 0) + 1}",
                    "",
                    table_to_markdown(table.get("rows") or []),
                    "",
                ]
            )

    body.extend(["## Images", ""])
    if images:
        for image in images:
            local = image.get("local") or ""
            alt = image.get("alt") or image.get("file") or "source image"
            source = image.get("src") or image.get("source") or ""
            if local:
                body.append(f"- ![{alt}](../{local})")
            else:
                body.append(f"- {alt}")
            if source:
                body.append(f"  Source: {source}")
    else:
        body.append("_No page images detected._")
    body.append("")

    links = page.get("links") or []
    if links:
        body.extend(["## Links", ""])
        for link in links:
            text = link.get("text") or link.get("href") or "link"
            href = link.get("href") or ""
            body.append(f"- [{text}]({href})")
        body.append("")

    return "\n".join(body)


class Receiver(BaseHTTPRequestHandler):
    server_version = "LiveSourceReceiver/1.0"

    def _cors(self) -> None:
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "content-type")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS, GET")

    def do_OPTIONS(self) -> None:  # noqa: N802
        self.send_response(204)
        self._cors()
        self.end_headers()

    def do_GET(self) -> None:  # noqa: N802
        self.send_response(200)
        self._cors()
        self.end_headers()
        self.wfile.write(b"ok")

    def do_POST(self) -> None:  # noqa: N802
        try:
            length = int(self.headers.get("content-length", "0"))
            payload = json.loads(self.rfile.read(length).decode("utf-8"))
            source = slugify(payload.get("source") or "source")
            out = OUT_ROOT / source
            pages_dir = out / "pages"
            images_dir = out / "images"
            pages_dir.mkdir(parents=True, exist_ok=True)
            images_dir.mkdir(parents=True, exist_ok=True)

            written_pages: list[dict[str, str]] = []
            for index, page in enumerate(payload.get("pages") or [], start=1):
                title = page.get("title") or page.get("label") or f"page-{index}"
                source_id = slugify(str(page.get("id") or ""), "")
                stem_bits = [f"{index:02d}"]
                if source_id:
                    stem_bits.append(source_id)
                stem_bits.append(slugify(title))
                stem = "-".join(stem_bits)
                page_images = [
                    write_image(image, images_dir, stem, image_index)
                    for image_index, image in enumerate(page.get("images") or [], start=1)
                ]
                md_path = pages_dir / f"{stem}.md"
                md_path.write_text(page_to_markdown(page, page_images), encoding="utf-8")
                written_pages.append(
                    {
                        "title": title,
                        "url": page.get("url") or "",
                        "file": str(md_path.relative_to(out)).replace("\\", "/"),
                    }
                )

            all_pages: list[dict[str, str]] = []
            for md_file in sorted(pages_dir.glob("*.md")):
                title = md_file.stem
                url = ""
                try:
                    for line in md_file.read_text(encoding="utf-8").splitlines()[:8]:
                        if line.startswith("# "):
                            title = line[2:].strip()
                        elif line.startswith("Source: "):
                            url = line.replace("Source: ", "", 1).strip()
                except OSError:
                    pass
                all_pages.append(
                    {
                        "title": title,
                        "url": url,
                        "file": str(md_file.relative_to(out)).replace("\\", "/"),
                    }
                )

            summary = {
                "source": payload.get("source"),
                "created_at": datetime.now(timezone.utc).isoformat(),
                "page_count": len(all_pages),
                "last_written": written_pages,
                "pages": all_pages,
            }
            (out / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

            self.send_response(200)
            self._cors()
            self.end_headers()
            self.wfile.write(json.dumps(summary, ensure_ascii=False).encode("utf-8"))
        except Exception as exc:  # pragma: no cover - diagnostic helper
            self.send_response(500)
            self._cors()
            self.end_headers()
            self.wfile.write(str(exc).encode("utf-8", errors="replace"))

    def log_message(self, format: str, *args: Any) -> None:
        return


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    server = ThreadingHTTPServer((args.host, args.port), Receiver)
    print(f"listening on http://{args.host}:{args.port}", flush=True)
    server.serve_forever()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
