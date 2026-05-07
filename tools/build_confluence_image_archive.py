"""Build a public Confluence image archive from authenticated raw imports.

Raw images are downloaded into imports/live-sources/confluence-work-images by
the logged-in browser.  This script prepares lighter site assets and generates
a Markdown gallery page for the wiki.
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW_ROOT = ROOT / "imports" / "live-sources" / "confluence-work-images"
RAW_IMAGES = RAW_ROOT / "images"
RAW_PAGES = RAW_ROOT / "pages"
OUT_IMAGES = ROOT / "docs" / "assets" / "images" / "confluence"
OUT_PAGE = ROOT / "docs" / "reference" / "confluence-image-archive.md"
MANIFEST = OUT_IMAGES / "manifest.json"

COPY_LIMIT = 900_000


@dataclass
class ImageItem:
    raw_file: Path
    out_file: Path
    title: str
    page_title: str
    page_url: str
    converted: bool
    raw_size: int


def slug_text(value: str) -> str:
    value = re.sub(r"\s+", " ", value).strip()
    return value or "Confluence image"


def page_records() -> list[dict[str, str]]:
    records: list[dict[str, str]] = []
    image_re = re.compile(r"!\[(?P<title>[^\]]*)\]\(\.\./confluence-work-images/images/(?P<file>[^)]+)\)")
    source_re = re.compile(r"^Source: (?P<url>.+)$", re.MULTILINE)
    h1_re = re.compile(r"^# (?P<title>.+)$", re.MULTILINE)

    for page in sorted(RAW_PAGES.glob("*.md")):
        text = page.read_text(encoding="utf-8")
        page_title = slug_text((h1_re.search(text) or {}).groupdict().get("title", "") if h1_re.search(text) else page.stem)
        page_url = (source_re.search(text) or {}).groupdict().get("url", "") if source_re.search(text) else ""
        for match in image_re.finditer(text):
            records.append(
                {
                    "file": match.group("file"),
                    "title": slug_text(match.group("title")),
                    "page_title": page_title,
                    "page_url": page_url,
                }
            )
    return records


def convert_with_ffmpeg(source: Path, dest: Path) -> bool:
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        return False
    dest.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        ffmpeg,
        "-y",
        "-i",
        str(source),
        "-frames:v",
        "1",
        "-vf",
        "scale='if(gt(iw,1600),1600,iw)':-2",
        "-q:v",
        "4",
        str(dest),
    ]
    result = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return result.returncode == 0 and dest.exists() and dest.stat().st_size > 0


def build_assets() -> list[ImageItem]:
    OUT_IMAGES.mkdir(parents=True, exist_ok=True)
    records = page_records()
    by_file = {record["file"]: record for record in records}
    items: list[ImageItem] = []

    for index, raw_file in enumerate(sorted(RAW_IMAGES.glob("*")), start=1):
        if not raw_file.is_file():
            continue
        record = by_file.get(raw_file.name, {})
        title = slug_text(record.get("title", raw_file.name))
        page_title = slug_text(record.get("page_title", "Confluence"))
        page_url = record.get("page_url", "")
        raw_size = raw_file.stat().st_size
        ext = raw_file.suffix.lower()
        converted = False

        if raw_size <= COPY_LIMIT and ext in {".png", ".jpg", ".jpeg", ".gif", ".webp"}:
            out_file = OUT_IMAGES / f"confluence-{index:03d}{ext}"
            shutil.copy2(raw_file, out_file)
        else:
            out_file = OUT_IMAGES / f"confluence-{index:03d}.jpg"
            converted = convert_with_ffmpeg(raw_file, out_file)
            if not converted:
                out_file = OUT_IMAGES / f"confluence-{index:03d}{ext}"
                shutil.copy2(raw_file, out_file)

        items.append(ImageItem(raw_file, out_file, title, page_title, page_url, converted, raw_size))

    return items


def build_markdown(items: list[ImageItem]) -> str:
    lines = [
        "# Confluence Image Archive",
        "",
        "Source: `https://ewood.atlassian.net/wiki/spaces/work/overview?homepageId=1933591`",
        "",
        f"Imported working Confluence images: **{len(items)}**.",
        "",
        "Large GIF/PNG attachments were converted to lightweight preview images for the",
        "public wiki. Raw originals are preserved under",
        "`imports/live-sources/confluence-work-images/images/`.",
        "",
        "The private `salary - conditions` page is intentionally excluded.",
        "",
    ]

    groups: dict[str, list[ImageItem]] = {}
    for item in items:
        groups.setdefault(item.page_title, []).append(item)

    for page_title, group in groups.items():
        lines.extend([f"## {page_title}", ""])
        page_url = next((item.page_url for item in group if item.page_url), "")
        if page_url:
            lines.extend([f"Source page: `{page_url}`", ""])
        lines.append('<div class="kb-gallery">')
        for item in group:
            rel = "../../assets/images/confluence/" + item.out_file.name
            note = "preview" if item.converted else "image"
            caption = f"{item.title} ({note}, {item.raw_size // 1024} KB raw)"
            lines.extend(
                [
                    f'  <a class="kb-gallery__item" href="{rel}">',
                    f'    <img src="{rel}" alt="{item.title}">',
                    f'    <div class="kb-gallery__caption">{caption}</div>',
                    "  </a>",
                ]
            )
        lines.extend(["</div>", ""])

    return "\n".join(lines)


def main() -> int:
    items = build_assets()
    OUT_PAGE.write_text(build_markdown(items), encoding="utf-8")
    manifest = [
        {
            "asset": item.out_file.name,
            "raw": item.raw_file.name,
            "title": item.title,
            "page_title": item.page_title,
            "page_url": item.page_url,
            "converted_preview": item.converted,
            "raw_size": item.raw_size,
        }
        for item in items
    ]
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"wrote {len(items)} images to {OUT_IMAGES}")
    print(f"wrote archive {OUT_PAGE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
