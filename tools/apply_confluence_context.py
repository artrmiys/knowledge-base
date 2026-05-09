"""Apply Confluence source notes and relationship maps to wiki pages.

This script is intentionally generated-data oriented:
- it keeps page-level context inside marker blocks;
- it creates a public Confluence Source Map page;
- it avoids publishing raw private download links or Atlassian people links.
"""

from __future__ import annotations

import html
import json
import posixpath
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
CONTENT_ROOT = ROOT / "imports" / "live-sources" / "confluence-work" / "pages"
IMAGE_ROOT = ROOT / "imports" / "live-sources" / "confluence-work-images" / "pages"
MANIFEST = DOCS / "assets" / "images" / "confluence" / "manifest.json"
SOURCE_MAP_PAGE = DOCS / "reference" / "confluence-source-map.md"
SPACE_CRAWL_MANIFEST = ROOT / "imports" / "live-sources" / "confluence-work" / "space_crawl_manifest.json"

START = "<!-- confluence-context:start -->"
END = "<!-- confluence-context:end -->"

sys.path.insert(0, str(ROOT / "tools"))
from apply_confluence_galleries import clean_title, target_for  # noqa: E402
from audit_confluence_usage import CONTENT_TARGETS  # noqa: E402


BOILERPLATE_PREFIXES = (
    "Обновлено ",
    "Автор:",
    "Показать просмотры",
    "Добавьте реакцию",
)
BOILERPLATE_LINES = {
    "Редактировать",
    "Поделиться",
    "Копировать ссылку",
    "Другие действия",
    "back_to_main_page",
    "back to main page",
    "Open",
    "Нажмите здесь, чтобы развернуть…",
    "Связанный контент",
    "Дополнительная информация",
}


@dataclass
class Export:
    title: str
    url: str
    page_id: str
    path: Path
    kind: str
    updated: str = ""
    notes: list[str] = field(default_factory=list)
    tables: list[str] = field(default_factory=list)
    related_urls: list[str] = field(default_factory=list)


@dataclass
class Source:
    title: str
    url: str
    page_id: str
    exports: list[Export] = field(default_factory=list)
    content_targets: set[str] = field(default_factory=set)
    image_targets: set[str] = field(default_factory=set)
    images: int = 0
    related_urls: set[str] = field(default_factory=set)


def page_id_from_url(url: str) -> str:
    if "/overview" in url:
        return "overview"
    match = re.search(r"/pages/(\d+)", url)
    return match.group(1) if match else ""


def md_link(from_doc: str, to_doc: str, label: str | None = None) -> str:
    from_dir = posixpath.dirname(from_doc.replace("\\", "/"))
    rel = posixpath.relpath(to_doc.replace("\\", "/"), from_dir or ".")
    return f"[{label or to_doc}]({rel})"


def extract_updated(text: str) -> str:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Обновлено "):
            return stripped.replace("Обновлено ", "", 1)
        if stripped.startswith("Updated:"):
            return stripped.replace("Updated:", "", 1).strip()
    return ""


def extract_links(text: str) -> list[str]:
    urls: list[str] = []
    for url in re.findall(r"https://redacted\.atlassian\.net/wiki/spaces/work/(?:pages/\d+/[^)\s]+|overview)", text):
        if "/download/attachments/" in url or "/history/" in url:
            continue
        urls.append(url.rstrip(")"))
    seen: set[str] = set()
    return [url for url in urls if not (url in seen or seen.add(url))]


def extract_text_block(text: str) -> str:
    if "## Text" not in text:
        return ""
    block = text.split("## Text", 1)[1]
    for marker in ("## Tables", "## Images", "## Links"):
        if marker in block:
            block = block.split(marker, 1)[0]
    if "Связанный контент" in block:
        block = block.split("Связанный контент", 1)[0]
    return block


def clean_notes(text: str, title: str) -> list[str]:
    notes: list[str] = []
    previous = ""
    for line in extract_text_block(text).splitlines():
        stripped = line.replace("\xa0", " ").strip()
        if not stripped:
            continue
        if stripped == title or stripped == clean_title(title):
            continue
        if stripped in BOILERPLATE_LINES:
            continue
        if any(stripped.startswith(prefix) for prefix in BOILERPLATE_PREFIXES):
            continue
        if stripped.startswith("Confluence page:") or stripped.startswith("Image attachments:"):
            continue
        if stripped == previous:
            continue
        notes.append(stripped)
        previous = stripped
    return notes


def extract_tables(text: str) -> list[str]:
    if "## Tables" not in text:
        return []
    block = text.split("## Tables", 1)[1]
    for marker in ("## Images", "## Links"):
        if marker in block:
            block = block.split(marker, 1)[0]
    tables: list[str] = []
    current: list[str] = []
    for line in block.splitlines():
        if line.startswith("### Table") and current:
            tables.append("\n".join(current).strip())
            current = [line]
        elif line.strip() or current:
            current.append(line)
    if current:
        tables.append("\n".join(current).strip())
    return [table for table in tables if "|" in table]


def read_export(path: Path, kind: str) -> Export | None:
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    title = lines[0].lstrip("# ").strip() if lines else path.stem
    match = re.search(r"^Source:\s*(\S+)", text, re.MULTILINE)
    if not match:
        return None
    url = match.group(1)
    return Export(
        title=title,
        url=url,
        page_id=page_id_from_url(url),
        path=path,
        kind=kind,
        updated=extract_updated(text),
        notes=clean_notes(text, title),
        tables=extract_tables(text),
        related_urls=extract_links(text),
    )


def read_sources() -> dict[str, Source]:
    sources: dict[str, Source] = {}
    for root, kind in ((CONTENT_ROOT, "content-md"), (IMAGE_ROOT, "image-md")):
        if not root.exists():
            continue
        for path in sorted(root.glob("*.md")):
            export = read_export(path, kind)
            if not export:
                continue
            source = sources.setdefault(
                export.url,
                Source(title=export.title, url=export.url, page_id=export.page_id),
            )
            source.exports.append(export)
            source.related_urls.update(export.related_urls)
            source.content_targets.update(CONTENT_TARGETS.get(export.page_id, []))

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    for item in manifest:
        url = item.get("page_url", "")
        source = sources.setdefault(
            url,
            Source(title=clean_title(item.get("page_title", "Confluence")), url=url, page_id=page_id_from_url(url)),
        )
        source.images += 1
        source.image_targets.add(target_for(item))

    return sources


def docs_for_source(source: Source) -> set[str]:
    return set(source.content_targets) | set(source.image_targets)


def relation_targets(source: Source, sources: dict[str, Source]) -> set[str]:
    targets: set[str] = set()
    for related_url in source.related_urls:
        related = sources.get(related_url)
        if not related:
            continue
        targets.update(docs_for_source(related))
    return targets


def source_role(source: Source, target: str) -> str:
    roles: list[str] = []
    if target in source.content_targets:
        roles.append("content")
    if target in source.image_targets:
        roles.append("images")
    return " + ".join(roles) if roles else "related"


def render_source_notes(source: Source, target: str) -> list[str]:
    lines: list[str] = []
    content_exports = [export for export in source.exports if export.kind == "content-md"]
    for export in content_exports:
        title = clean_title(export.title)
        lines.extend(
            [
                f'??? note "{title}"',
                f"    Source: `{export.url}`",
            ]
        )
        if export.updated:
            lines.append(f"    Updated in Confluence: `{export.updated}`")
        lines.append("")
        if export.notes:
            for note in export.notes:
                safe_note = note.replace("\n", " ").strip()
                lines.append(f"    - {safe_note}")
        else:
            lines.append("    - No reusable text notes were detected in the raw export.")
        if export.tables:
            lines.extend(["", "    Source tables:", ""])
            for table in export.tables:
                for table_line in table.splitlines():
                    lines.append(f"    {table_line}")
                lines.append("")
        lines.append("")
    return lines


def render_context(target: str, target_sources: list[Source], sources: dict[str, Source]) -> str:
    lines: list[str] = [
        START,
        "## Confluence Context",
        "",
        "Эта секция показывает, какие Confluence-страницы питают эту wiki-страницу и какие соседние темы связаны с ней через исходники.",
        "",
        "| Source | Role here | Images | Raw MD |",
        "| --- | --- | ---: | --- |",
    ]

    for source in sorted(target_sources, key=lambda s: clean_title(s.title).casefold()):
        raw = "<br>".join(
            f"`{str(export.path.relative_to(ROOT)).replace(chr(92), '/')}`"
            for export in sorted(source.exports, key=lambda e: e.kind)
        )
        raw = raw or "-"
        title = clean_title(source.title)
        lines.append(
            f"| [{title}]({source.url}) | {source_role(source, target)} | {source.images} | {raw} |"
        )

    related_docs: set[str] = set()
    for source in target_sources:
        related_docs.update(relation_targets(source, sources))
    related_docs.discard(target)

    if related_docs:
        lines.extend(["", "### Related Wiki Pages", ""])
        lines.append("| Wiki page | Why it is connected |")
        lines.append("| --- | --- |")
        for doc in sorted(related_docs):
            labels = []
            for source in target_sources:
                if doc in relation_targets(source, sources):
                    labels.append(clean_title(source.title))
            why = ", ".join(sorted(set(labels))) or "Confluence related link"
            lines.append(f"| {md_link(target, doc)} | linked from `{why}` |")

    note_lines: list[str] = []
    for source in target_sources:
        note_lines.extend(render_source_notes(source, target))
    if note_lines:
        lines.extend(["", "### Source Notes", ""])
        lines.extend(note_lines)

    lines.extend([END, ""])
    return "\n".join(lines)


def remove_existing(text: str) -> str:
    start = text.find(START)
    if start == -1:
        return text.rstrip() + "\n"
    end = text.find(END, start)
    if end == -1:
        raise ValueError("Found confluence context start marker without end marker")
    end += len(END)
    return (text[:start].rstrip() + "\n\n" + text[end:].lstrip()).rstrip() + "\n"


def insert_context(text: str, context: str) -> str:
    gallery = "<!-- confluence-gallery:start -->"
    if gallery in text:
        before, after = text.split(gallery, 1)
        return before.rstrip() + "\n\n" + context.rstrip() + "\n\n" + gallery + after
    return text.rstrip() + "\n\n" + context


def apply_contexts(sources: dict[str, Source]) -> int:
    by_target: dict[str, list[Source]] = defaultdict(list)
    for source in sources.values():
        for target in docs_for_source(source):
            if (DOCS / target).exists():
                by_target[target].append(source)

    changed = 0
    for target, target_sources in sorted(by_target.items()):
        path = DOCS / target
        old = path.read_text(encoding="utf-8")
        base = remove_existing(old)
        new = insert_context(base, render_context(target, target_sources, sources))
        if new != old:
            path.write_text(new, encoding="utf-8", newline="\n")
            changed += 1
            print(f"updated: {target} ({len(target_sources)} sources)")
        else:
            print(f"unchanged: {target} ({len(target_sources)} sources)")
    return changed


def generate_source_map(sources: dict[str, Source]) -> None:
    by_doc: dict[str, list[Source]] = defaultdict(list)
    for source in sources.values():
        for doc in docs_for_source(source):
            by_doc[doc].append(source)

    lines: list[str] = [
        "# Confluence Source Map",
        "",
        "Эта страница показывает, какие Confluence-страницы уже выгружены, куда они попали в wiki, и какие связи между темами были найдены.",
        "",
        "## Coverage",
        "",
        f"- Confluence source URLs tracked: **{len(sources)}**",
        f"- Wiki pages with Confluence context: **{len(by_doc)}**",
        f"- Public images mapped into topic pages: **{sum(source.images for source in sources.values())}**",
        "",
    ]

    if SPACE_CRAWL_MANIFEST.exists():
        crawl = json.loads(SPACE_CRAWL_MANIFEST.read_text(encoding="utf-8"))
        skipped = crawl.get("skipped_private") or []
        lines.extend(
            [
                "## Full Space Crawl",
                "",
                f"- Confluence pages found in `work` space: **{crawl.get('space_page_count', 0)}**",
                f"- Safe missing pages imported after full crawl: **{len(crawl.get('newly_written') or [])}**",
                f"- Private/sensitive pages intentionally not published: **{len(skipped)}**",
                "",
            ]
        )
        if skipped:
            lines.extend(["| Skipped source | Reason |", "| --- | --- |"])
            for row in skipped:
                lines.append(f"| `{row.get('title', '')}` | {row.get('reason', '')} |")
            lines.append("")
        written = crawl.get("newly_written") or []
        if written:
            lines.extend(["Imported in the full crawl pass:", ""])
            for row in written:
                lines.append(f"- `{row.get('title', '')}` -> `{row.get('file', '')}`")
            lines.append("")

    lines.extend(
        [
            "## Wiki Pages",
            "",
            "| Wiki page | Source pages | Images |",
            "| --- | ---: | ---: |",
        ]
    )
    for doc, doc_sources in sorted(by_doc.items()):
        images = sum(source.images for source in doc_sources if doc in source.image_targets)
        lines.append(f"| {md_link('reference/confluence-source-map.md', doc)} | {len(doc_sources)} | {images} |")

    lines.extend(
        [
            "",
            "## Source Pages",
            "",
            "| Confluence source | Role | Wiki target(s) | Images | Related wiki pages |",
            "| --- | --- | --- | ---: | --- |",
        ]
    )
    for source in sorted(sources.values(), key=lambda s: clean_title(s.title).casefold()):
        targets = sorted(docs_for_source(source))
        target_links = "<br>".join(md_link("reference/confluence-source-map.md", doc) for doc in targets) or "-"
        roles = []
        if source.content_targets:
            roles.append("content")
        if source.image_targets:
            roles.append("images")
        related_docs = sorted(relation_targets(source, sources) - set(targets))
        related_links = "<br>".join(md_link("reference/confluence-source-map.md", doc) for doc in related_docs[:12]) or "-"
        if len(related_docs) > 12:
            related_links += f"<br>...and {len(related_docs) - 12} more"
        lines.append(
            f"| [{clean_title(source.title)}]({source.url}) | {' + '.join(roles) or 'source'} | {target_links} | {source.images} | {related_links} |"
        )

    SOURCE_MAP_PAGE.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print(f"source-map: {SOURCE_MAP_PAGE.relative_to(ROOT)}")


def main() -> int:
    sources = read_sources()
    changed = apply_contexts(sources)
    generate_source_map(sources)
    print(f"sources={len(sources)} changed_pages={changed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
