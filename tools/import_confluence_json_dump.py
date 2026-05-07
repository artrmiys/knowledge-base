"""Import authenticated Confluence JSON dumps saved from Playwright.

The browser owns the Atlassian login cookies, so Playwright writes JSON dumps
to disk and this script turns safe pages into raw Markdown imports. Sensitive
pages are recorded as skipped metadata only.
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "imports" / "live-sources" / "confluence-work"
PAGES_DIR = OUT / "pages"
CRAWL_MANIFEST = OUT / "space_crawl_manifest.json"

PRIVATE_IDS = {
    "1933705": "private salary/conditions page",
    "227966993": "contains pay/vacation conditions mixed with estimating notes",
}


def slugify(value: str, fallback: str = "page") -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9а-яё]+", "-", value, flags=re.IGNORECASE)
    value = value.strip("-")
    return (value[:90] or fallback).strip("-") or fallback


def table_to_markdown(rows: list[list[str]]) -> str:
    if not rows:
        return ""
    width = max(len(row) for row in rows)
    normalized = []
    for row in rows:
        normalized.append(
            [
                (row[index] if index < len(row) else "").replace("|", "\\|")
                for index in range(width)
            ]
        )
    lines = [
        "| " + " | ".join(normalized[0]) + " |",
        "| " + " | ".join(["---"] * width) + " |",
    ]
    lines.extend("| " + " | ".join(row) + " |" for row in normalized[1:])
    return "\n".join(lines)


def page_to_markdown(page: dict[str, Any]) -> str:
    title = page.get("title") or "Confluence Page"
    source = page.get("url") or ""
    updated = page.get("updated") or ""
    ancestors = page.get("ancestors") or []
    imported = datetime.now(timezone.utc).isoformat()
    ancestor_text = " > ".join(a.get("title", "") for a in ancestors if a.get("title"))

    body = [
        f"# {title}",
        "",
        f"Source: {source}",
        "",
        f"Imported: {imported}",
        "",
    ]
    if updated:
        body.extend([f"Updated: {updated}", ""])
    if ancestor_text:
        body.extend([f"Ancestors: {ancestor_text}", ""])

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

    body.extend(["## Images", "", "_No page images detected._", ""])

    links = page.get("links") or []
    if links:
        body.extend(["## Links", ""])
        for link in links:
            text = link.get("text") or link.get("href") or "link"
            href = link.get("href") or ""
            body.append(f"- [{text}]({href})")
        body.append("")

    return "\n".join(body)


def existing_page_ids() -> set[str]:
    ids: set[str] = set()
    for path in PAGES_DIR.glob("*.md"):
        text = path.read_text(encoding="utf-8", errors="replace")
        match = re.search(r"/pages/(\d+)", text)
        if match:
            ids.add(match.group(1))
    return ids


def write_pages(payload_path: Path) -> list[dict[str, str]]:
    payload = json.loads(payload_path.read_text(encoding="utf-8"))
    PAGES_DIR.mkdir(parents=True, exist_ok=True)
    existing = existing_page_ids()
    written: list[dict[str, str]] = []
    for page in payload.get("pages") or []:
        page_id = str(page.get("id") or "")
        if page_id in PRIVATE_IDS:
            continue
        if page_id in existing:
            continue
        stem = f"01-{page_id}-{slugify(page.get('title') or 'page')}"
        path = PAGES_DIR / f"{stem}.md"
        path.write_text(page_to_markdown(page), encoding="utf-8", newline="\n")
        written.append(
            {
                "id": page_id,
                "title": page.get("title") or "",
                "url": page.get("url") or "",
                "file": str(path.relative_to(ROOT)).replace("\\", "/"),
            }
        )
    return written


def write_manifest(space_pages_path: Path, safe_pages_path: Path, written: list[dict[str, str]]) -> None:
    space = json.loads(space_pages_path.read_text(encoding="utf-8"))
    safe = json.loads(safe_pages_path.read_text(encoding="utf-8"))
    pages = space.get("pages") or []
    skipped = [
        {
            "id": str(page.get("id") or ""),
            "title": page.get("title") or "",
            "url": page.get("webui") or "",
            "reason": PRIVATE_IDS[str(page.get("id") or "")],
        }
        for page in pages
        if str(page.get("id") or "") in PRIVATE_IDS
    ]
    payload = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "space_page_count": len(pages),
        "safe_dump_page_count": len(safe.get("pages") or []),
        "newly_written": written,
        "skipped_private": skipped,
        "pages": pages,
    }
    CRAWL_MANIFEST.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--space-pages", required=True, type=Path)
    parser.add_argument("--safe-pages", required=True, type=Path)
    args = parser.parse_args()

    written = write_pages(args.safe_pages)
    write_manifest(args.space_pages, args.safe_pages, written)
    print(f"written={len(written)}")
    for row in written:
        print(f"{row['id']} {row['title']} -> {row['file']}")
    print(f"manifest={CRAWL_MANIFEST}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
