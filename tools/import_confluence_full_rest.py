"""Convert a full Confluence REST export into local raw Markdown/HTML files.

This importer intentionally writes into `imports/`, which is gitignored.  Public
wiki pages should continue to use curated/safe scripts; this file preserves the
complete raw archive, including private pages, without publishing them.
"""

from __future__ import annotations

import argparse
import html
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "imports" / "live-sources" / "confluence-work-full"
PRIVATE_IDS = {
    "1933705": "private salary/conditions page",
    "227966993": "contains pay/vacation conditions mixed with estimating notes",
}


class TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"p", "div", "br", "li", "tr", "h1", "h2", "h3", "h4"}:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        text = html.unescape(data).strip()
        if text:
            self.parts.append(text)

    def text(self) -> str:
        joined = " ".join(self.parts)
        joined = re.sub(r"[ \t\r\f\v]+", " ", joined)
        joined = re.sub(r"\n\s+", "\n", joined)
        joined = re.sub(r"\n{3,}", "\n\n", joined)
        return joined.strip()


def html_to_text(value: str) -> str:
    parser = TextExtractor()
    parser.feed(value or "")
    return parser.text()


def slugify(value: str, fallback: str = "page") -> str:
    value = re.sub(r"\s+", " ", value or "").strip().lower()
    value = re.sub(r"[^a-z0-9а-яё]+", "-", value, flags=re.IGNORECASE)
    value = value.strip("-")
    return (value[:100] or fallback).strip("-") or fallback


def page_url(page: dict[str, Any]) -> str:
    links = page.get("_links") or {}
    webui = links.get("webui") or ""
    if webui.startswith("http"):
        return webui
    base = links.get("base") or "https://ewood.atlassian.net/wiki"
    return base.rstrip("/") + "/" + webui.lstrip("/")


def labels_for(page: dict[str, Any]) -> list[str]:
    labels = (((page.get("metadata") or {}).get("labels") or {}).get("results") or [])
    return [label.get("name") or "" for label in labels if label.get("name")]


def render_page(page: dict[str, Any], private_reason: str = "") -> str:
    body = page.get("body") or {}
    storage_html = ((body.get("storage") or {}).get("value") or "").strip()
    view_html = ((body.get("view") or {}).get("value") or "").strip()
    export_html = ((body.get("export_view") or {}).get("value") or "").strip()
    ancestors = " > ".join(a.get("title") or "" for a in page.get("ancestors") or [] if a.get("title"))
    version = page.get("version") or {}
    lines = [
        f"# {page.get('title') or 'Confluence Page'}",
        "",
        f"Source: {page_url(page)}",
        "",
        f"Page ID: `{page.get('id')}`",
        "",
        f"Updated: `{version.get('when') or ''}`",
        "",
    ]
    if private_reason:
        lines.extend([f"Private import reason: {private_reason}", ""])
    if ancestors:
        lines.extend([f"Ancestors: {ancestors}", ""])
    labels = labels_for(page)
    if labels:
        lines.extend(["Labels:", *[f"- {label}" for label in labels], ""])

    lines.extend(["## View Text", "", html_to_text(view_html) or "_No visible body text._", ""])

    attachments = page.get("attachments") or []
    lines.extend(["## Attachments", ""])
    if attachments:
        lines.extend(["| Attachment | Media type | Size | Download path |", "| --- | --- | ---: | --- |"])
        for attachment in attachments:
            links = attachment.get("_links") or {}
            download = links.get("download") or ""
            media_type = ((attachment.get("metadata") or {}).get("mediaType") or "")
            size = ((attachment.get("extensions") or {}).get("fileSize") or "")
            lines.append(f"| {attachment.get('title') or ''} | {media_type} | {size} | `{download}` |")
        lines.append("")
    else:
        lines.extend(["_No attachments._", ""])

    lines.extend(["## Storage HTML", "", "```html", storage_html, "```", ""])
    lines.extend(["## View HTML", "", "```html", view_html, "```", ""])
    lines.extend(["## Export View HTML", "", "```html", export_html, "```", ""])
    return "\n".join(lines)


def write_pages(payload: dict[str, Any], output: Path) -> list[dict[str, Any]]:
    public_dir = output / "pages-public"
    private_dir = output / "pages-private"
    public_dir.mkdir(parents=True, exist_ok=True)
    private_dir.mkdir(parents=True, exist_ok=True)
    records: list[dict[str, Any]] = []

    for index, page in enumerate(payload.get("pages") or [], start=1):
        page_id = str(page.get("id") or "")
        private_reason = PRIVATE_IDS.get(page_id, "")
        folder = private_dir if private_reason else public_dir
        path = folder / f"{index:02d}-{page_id}-{slugify(page.get('title') or 'page')}.md"
        path.write_text(render_page(page, private_reason), encoding="utf-8", newline="\n")
        records.append(
            {
                "id": page_id,
                "title": page.get("title") or "",
                "url": page_url(page),
                "private": bool(private_reason),
                "private_reason": private_reason,
                "attachments": len(page.get("attachments") or []),
                "file": str(path.relative_to(output)).replace("\\", "/"),
            }
        )
    return records


def write_summary(payload: dict[str, Any], output: Path, records: list[dict[str, Any]]) -> None:
    attachment_count = sum(record["attachments"] for record in records)
    summary = {
        "source": payload.get("source"),
        "exported_at": payload.get("exportedAt"),
        "pages": len(records),
        "public_pages": len([record for record in records if not record["private"]]),
        "private_pages": len([record for record in records if record["private"]]),
        "attachments": attachment_count,
        "records": records,
    }
    (output / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        "# Confluence Full REST Export Audit",
        "",
        f"- Pages exported: **{summary['pages']}**",
        f"- Public/safe raw pages: **{summary['public_pages']}**",
        f"- Private raw pages: **{summary['private_pages']}**",
        f"- Attachment metadata rows: **{summary['attachments']}**",
        "",
        "Private pages are stored in `pages-private/` inside gitignored `imports/`",
        "and must not be copied into public `docs/`.",
        "",
        "| Scope | Title | Attachments | Raw MD | Source |",
        "| --- | --- | ---: | --- | --- |",
    ]
    for record in records:
        scope = "private" if record["private"] else "public"
        title = record["title"] if not record["private"] else f"{record['title']} (private)"
        lines.append(f"| {scope} | {title} | {record['attachments']} | `{record['file']}` | {record['url']} |")
    (output / "AUDIT.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    payload = json.loads(args.input.read_text(encoding="utf-8"))
    args.output.mkdir(parents=True, exist_ok=True)
    records = write_pages(payload, args.output)
    write_summary(payload, args.output, records)
    print(f"confluence_pages={len(records)} output={args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
