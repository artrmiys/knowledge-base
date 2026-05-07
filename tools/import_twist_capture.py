from __future__ import annotations

import argparse
import hashlib
import json
import mimetypes
import re
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


ATTACHMENT_RE = re.compile(r"(files\.twist\.com|twistusercontent|twistcdn)", re.I)
NOISE_IMAGE_RE = re.compile(r"(twemoji|_s60\.jpg|_s195\.jpg|/assets/svg/)", re.I)
EMAIL_RE = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I)
URL_RE = re.compile(r"https?://[^\s)>\]]+", re.I)


@dataclass
class ImageRef:
    src: str
    alt: str = ""
    local_path: str | None = None
    download_status: str = "pending"
    message_indices: list[int] = field(default_factory=list)


@dataclass
class Message:
    index: int
    key: str
    text: str
    body_text: str
    times: list[str]
    images: list[dict[str, Any]]
    links: list[dict[str, Any]]
    source_labels: list[str] = field(default_factory=list)


def norm_text(value: str) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def stable_message_key(row: dict[str, Any]) -> str:
    text = norm_text(row.get("text") or row.get("bodyText") or "")
    image_urls = [
        img.get("src", "")
        for img in row.get("images", [])
        if is_attachment_image(img.get("src", ""))
    ]
    raw = text + "\n" + "\n".join(sorted(image_urls))
    return hashlib.sha256(raw.encode("utf-8", "ignore")).hexdigest()[:16]


def is_attachment_image(url: str) -> bool:
    if not url:
        return False
    return bool(ATTACHMENT_RE.search(url)) and not NOISE_IMAGE_RE.search(url)


def extension_from_response(url: str, content_type: str | None) -> str:
    parsed = urlparse(url)
    suffix = Path(parsed.path).suffix
    if suffix and 1 < len(suffix) <= 8:
        return suffix.lower()
    if content_type:
        guessed = mimetypes.guess_extension(content_type.split(";")[0].strip())
        if guessed:
            return guessed
    return ".bin"


def download(url: str, out_without_ext: Path) -> tuple[str | None, str]:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 Twist private archive importer",
            "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            data = response.read()
            ext = extension_from_response(url, response.headers.get("Content-Type"))
    except urllib.error.HTTPError as exc:
        return None, f"http-error-{exc.code}"
    except Exception as exc:  # noqa: BLE001 - importer should keep going
        return None, f"error-{type(exc).__name__}: {exc}"

    digest = hashlib.sha256(data).hexdigest()[:10]
    path = out_without_ext.with_name(out_without_ext.name + f"-{digest}{ext}")
    path.write_bytes(data)
    return str(path), "downloaded"


def load_messages(capture: dict[str, Any]) -> list[Message]:
    seen: dict[str, Message] = {}
    ordered_keys: list[str] = []
    if capture.get("rows") and not capture.get("chunks"):
        capture = {
            **capture,
            "chunks": [
                {
                    "label": "manual-browser-export",
                    "rows": capture.get("rows", []),
                }
            ],
        }
    for chunk in capture.get("chunks", []):
        label = chunk.get("label", "chunk")
        for row in chunk.get("rows", []):
            text = row.get("text") or ""
            body = row.get("bodyText") or ""
            if not norm_text(text) and not row.get("images"):
                continue
            key = stable_message_key(row)
            if key not in seen:
                seen[key] = Message(
                    index=len(ordered_keys) + 1,
                    key=key,
                    text=text,
                    body_text=body,
                    times=list(dict.fromkeys(row.get("times", []))),
                    images=row.get("images", []),
                    links=row.get("links", []),
                    source_labels=[label],
                )
                ordered_keys.append(key)
            else:
                message = seen[key]
                if label not in message.source_labels:
                    message.source_labels.append(label)
                for img in row.get("images", []):
                    src = img.get("src")
                    if src and all(existing.get("src") != src for existing in message.images):
                        message.images.append(img)
                for link in row.get("links", []):
                    href = link.get("href")
                    if href and all(existing.get("href") != href for existing in message.links):
                        message.links.append(link)

    messages = [seen[key] for key in ordered_keys]
    # Chunks were captured while scrolling upward, but each chunk DOM is top-to-bottom.
    # Sort by the first source label order and row order already preserved by capture.
    for i, message in enumerate(messages, start=1):
        message.index = i
    return messages


def collect_images(messages: list[Message]) -> dict[str, ImageRef]:
    images: dict[str, ImageRef] = {}
    for message in messages:
        for image in message.images:
            src = image.get("src") or ""
            if not is_attachment_image(src):
                continue
            ref = images.setdefault(src, ImageRef(src=src, alt=image.get("alt") or ""))
            if message.index not in ref.message_indices:
                ref.message_indices.append(message.index)
    return images


def link_is_private(text: str, href: str) -> bool:
    haystack = f"{text} {href}".lower()
    return bool(EMAIL_RE.search(haystack) or "zoom.us" in haystack or "teams." in haystack)


def write_dialogue(
    path: Path,
    capture: dict[str, Any],
    messages: list[Message],
    images: dict[str, ImageRef],
    root: Path,
) -> None:
    lines: list[str] = []
    lines.append("# Twist Thread 1337560 - Private Dialogue Archive")
    lines.append("")
    lines.append("!!! warning")
    lines.append("    Private local archive. Do not publish this file to `docs/` without a manual privacy pass.")
    lines.append("")
    lines.append(f"- Source URL: {capture.get('url') or capture.get('final', {}).get('url', '')}")
    lines.append(f"- Captured at: {capture.get('final', {}).get('savedAt', '')}")
    lines.append(f"- Messages: {len(messages)}")
    lines.append(f"- Attachment images: {len(images)}")
    lines.append("")
    lines.append("## Messages")
    lines.append("")
    for message in messages:
        lines.append(f"### Message {message.index:03d}")
        if message.times:
            lines.append(f"- Time/date visible: {', '.join(message.times)}")
        lines.append(f"- Capture chunks: {', '.join(message.source_labels[:8])}")
        text = message.text.strip()
        if text:
            lines.append("")
            lines.append("```text")
            lines.append(text)
            lines.append("```")
        attachment_images = [
            image for image in message.images if is_attachment_image(image.get("src") or "")
        ]
        if attachment_images:
            lines.append("")
            lines.append("Attachments/images tied to this message:")
            for image in attachment_images:
                src = image.get("src") or ""
                ref = images.get(src)
                local = ref.local_path if ref else None
                local_display = ""
                if local:
                    try:
                        local_display = Path(local).resolve().relative_to(root.resolve()).as_posix()
                    except ValueError:
                        local_display = local
                alt = image.get("alt") or Path(urlparse(src).path).name or "image"
                lines.append(f"- `{alt}` -> `{local_display or ref.download_status if ref else 'not-downloaded'}`")
                lines.append(f"  Source: {src}")
        private_links = [
            link for link in message.links if link_is_private(link.get("text", ""), link.get("href", ""))
        ]
        if private_links:
            lines.append("")
            lines.append("Private links/contact data seen in this message:")
            for link in private_links:
                lines.append(f"- {link.get('text') or '(link)'} -> {link.get('href')}")
        lines.append("")
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_work_extract(path: Path, messages: list[Message], images: dict[str, ImageRef], root: Path) -> None:
    keywords = re.compile(
        r"joist|rim|shear|draft stop|resilient|furring|metal|stud|framing|"
        r"plate|track|FRT|MSTI|CS14|beam|deck|porch|label|ETA|due|bottom|floor|"
        r"truss|hanger|double|single|takeoff|sheet|file|PDF",
        re.I,
    )
    lines: list[str] = []
    lines.append("# Twist 1337560 - Work Extract Draft")
    lines.append("")
    lines.append("This is a private draft extracted from the full dialogue. It still needs manual cleanup before anything is copied into public wiki pages.")
    lines.append("")
    for message in messages:
        text = norm_text(message.text)
        if not text or not keywords.search(text):
            continue
        lines.append(f"## Message {message.index:03d}")
        if message.times:
            lines.append(f"- Time/date visible: {', '.join(message.times)}")
        lines.append("")
        lines.append(text)
        attachment_images = [
            image for image in message.images if is_attachment_image(image.get("src") or "")
        ]
        if attachment_images:
            lines.append("")
            lines.append("Images:")
            for image in attachment_images:
                ref = images.get(image.get("src") or "")
                if not ref or not ref.local_path:
                    continue
                try:
                    rel = Path(ref.local_path).resolve().relative_to(root.resolve()).as_posix()
                except ValueError:
                    rel = ref.local_path
                lines.append(f"- `{image.get('alt') or 'image'}` -> `{rel}`")
        lines.append("")
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_audit(
    path: Path,
    capture: dict[str, Any],
    messages: list[Message],
    images: dict[str, ImageRef],
    screenshot_dir: Path,
) -> None:
    screenshots = sorted(screenshot_dir.glob("*.png"))
    private_link_count = sum(
        1
        for message in messages
        for link in message.links
        if link_is_private(link.get("text", ""), link.get("href", ""))
    )
    downloaded = sum(1 for ref in images.values() if ref.download_status == "downloaded")
    lines = [
        "# Twist 1337560 Import Audit",
        "",
        "| Metric | Value |",
        "| --- | ---: |",
        f"| Capture chunks | {len(capture.get('chunks', []))} |",
        f"| Unique message rows | {len(messages)} |",
        f"| Attachment image URLs | {len(images)} |",
        f"| Downloaded attachments | {downloaded} |",
        f"| Viewport screenshots | {len(screenshots)} |",
        f"| Private links/contact markers | {private_link_count} |",
        "",
        "## Privacy Boundary",
        "",
        "- Everything here is under `imports/`, which is ignored by git.",
        "- `dialogue.md` is a complete private archive draft.",
        "- `WORK_EXTRACT_DRAFT.md` is still private and must be manually redacted before use in `docs/`.",
        "- Cookies, tokens, localStorage, and sessionStorage were not exported.",
        "",
        "## Files",
        "",
        "- `raw/thread-capture-scroll-up.json` - full DOM/text capture from scrolling upward.",
        "- `dialogue.md` - readable message archive with image links tied to message numbers.",
        "- `WORK_EXTRACT_DRAFT.md` - work-related draft notes from the dialogue.",
        "- `attachments/manifest.json` - original image URL to local file map.",
        "- `screenshots/` - viewport proof while scrolling upward.",
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Convert private Twist browser capture into local markdown archive.")
    parser.add_argument("--capture", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--download", action="store_true")
    args = parser.parse_args()

    capture_path: Path = args.capture
    output_dir: Path = args.output
    attachments_dir = output_dir / "attachments"
    attachments_dir.mkdir(parents=True, exist_ok=True)

    capture = json.loads(capture_path.read_text(encoding="utf-8"))
    messages = load_messages(capture)
    images = collect_images(messages)

    if args.download:
        for idx, (url, ref) in enumerate(images.items(), start=1):
            local, status = download(url, attachments_dir / f"twist-image-{idx:03d}")
            ref.local_path = local
            ref.download_status = status

    manifest = {
        "source_url": capture.get("url") or capture.get("final", {}).get("url", ""),
        "message_count": len(messages),
        "attachment_image_count": len(images),
        "images": [
            {
                "index": idx,
                "src": ref.src,
                "alt": ref.alt,
                "local_path": ref.local_path,
                "download_status": ref.download_status,
                "message_indices": ref.message_indices,
            }
            for idx, ref in enumerate(images.values(), start=1)
        ],
    }
    (attachments_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    (output_dir / "thread-text.txt").write_text(
        "\n\n---\n\n".join(message.text.strip() for message in messages if message.text.strip()) + "\n",
        encoding="utf-8",
    )
    write_dialogue(output_dir / "dialogue.md", capture, messages, images, output_dir)
    write_work_extract(output_dir / "WORK_EXTRACT_DRAFT.md", messages, images, output_dir)
    write_audit(output_dir / "AUDIT.md", capture, messages, images, output_dir / "screenshots")

    print(f"messages={len(messages)}")
    print(f"attachment_images={len(images)}")
    print(f"downloaded={sum(1 for ref in images.values() if ref.download_status == 'downloaded')}")
    print(f"output={output_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
