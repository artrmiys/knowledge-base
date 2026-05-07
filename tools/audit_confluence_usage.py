"""Audit Confluence raw markdown exports against wiki usage.

This does not publish anything. It writes a durable audit report under imports/
so we can see which Confluence pages were exported and where their images/content
landed in the MkDocs wiki.
"""

from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MANIFEST = DOCS / "assets" / "images" / "confluence" / "manifest.json"
REPORT = ROOT / "imports" / "live-sources" / "confluence-work" / "USAGE_AUDIT.md"

sys.path.insert(0, str(ROOT / "tools"))
from apply_confluence_galleries import target_for  # noqa: E402


CONTENT_TARGETS: dict[str, list[str]] = {
    "58916937": ["work/vertical/walls/unit.md"],
    "63438852": ["work-types/residential.md"],
    "63537157": ["work-types/residential.md"],
    "65863695": ["start/takeoff-structure.md"],
    "72876034": ["start/takeoff-structure.md"],
    "90144784": ["work/vertical/sheathing/duplicate-of-gable.md"],
    "92110850": ["start/maintenance.md", "start/quality-checklist.md"],
    "154665001": ["start/how-to-use.md"],
    "154665008": ["reference/source-map.md"],
    "154828836": ["start/takeoff-structure.md"],
    "227934223": ["start/quality-checklist.md", "work-types/com.md"],
    "2162791": ["work-types/ewp-capital.md"],
    "2359297": ["work-types/com.md"],
    "63799300": ["work/vertical/walls/gable.md"],
    "65044582": ["work/vertical/openings/windows-doors.md"],
    "65044604": ["work/vertical/sheathing/wall-sheathing.md"],
    "65077308": ["work/vertical/walls/unit.md"],
    "65110035": ["start/takeoff-structure.md"],
    "65175555": ["start/takeoff-structure.md", "work/vertical/walls/exterior.md"],
    "65273857": ["work/vertical/walls/exterior.md"],
    "65273871": ["work/vertical/walls/corners.md"],
    "65306625": ["work/vertical/walls/corridor.md"],
    "65306639": ["work/vertical/walls/demising.md"],
    "65306653": ["work/vertical/walls/parapet.md"],
    "65306667": ["work/vertical/walls/shaft.md"],
    "65306681": ["work/vertical/walls/furring.md"],
    "65339393": ["work/vertical/openings/windows-doors.md"],
    "65339407": ["work/vertical/openings/headers.md"],
    "65831004": ["work/horizontal/floor-framing/post.md"],
    "65961989": [
        "start/takeoff-structure.md",
        "work/deck/anchor-bolts.md",
        "work/deck/balcony-trims.md",
        "work/deck/railing.md",
    ],
    "65962048": ["start/takeoff-structure.md"],
    "66093057": ["work/horizontal/roof-framing/ridge.md"],
    "66093067": ["work/horizontal/roof-framing/header.md"],
    "66093077": ["work/horizontal/roof-framing/dbl-trpl-rafters.md"],
    "66093087": ["work/horizontal/roof-framing/hip.md"],
    "66093097": ["work/horizontal/roof-framing/valley.md"],
    "66093107": ["work/horizontal/roof-framing/overframes.md"],
    "66125825": ["work/horizontal/roof-framing/canopy.md"],
    "66125835": ["work/horizontal/roof-framing/dormer.md"],
    "66125845": ["work/horizontal/roof-framing/roof-sheathing.md"],
    "67043361": ["work/deck/railing.md"],
    "67469321": ["work/deck/balcony-trims.md"],
    "72482856": ["work/deck/anchor-bolts.md"],
    "75333633": ["work/vertical/walls/sill-plates.md"],
    "89948162": ["work/vertical/sheathing/floor.md"],
    "89948176": ["work/vertical/sheathing/gable.md"],
    "89948190": ["work/vertical/sheathing/truss-heel.md"],
    "90144770": ["work/vertical/sheathing/wall-sheathing.md"],
    "90210306": ["work/vertical/sheathing/shear-wall.md"],
}


@dataclass
class PageExport:
    title: str
    url: str
    source_path: Path
    export_kind: str
    page_id: str


@dataclass
class PageRecord:
    title: str
    url: str
    page_id: str
    exports: list[PageExport] = field(default_factory=list)
    images: int = 0
    image_targets: set[str] = field(default_factory=set)
    content_targets: set[str] = field(default_factory=set)
    source_url_in_docs: bool = False


def page_id_from_url(url: str) -> str:
    if "/overview" in url:
        return "overview"
    match = re.search(r"/pages/(\d+)", url)
    return match.group(1) if match else ""


def read_export(path: Path, kind: str) -> PageExport | None:
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    title = lines[0].lstrip("# ").strip() if lines else path.stem
    match = re.search(r"^Source:\s*(\S+)", text, re.MULTILINE)
    if not match:
        return None
    url = match.group(1)
    return PageExport(title=title, url=url, source_path=path, export_kind=kind, page_id=page_id_from_url(url))


def read_exports() -> list[PageExport]:
    roots = [
        (ROOT / "imports" / "live-sources" / "confluence-work" / "pages", "content-md"),
        (ROOT / "imports" / "live-sources" / "confluence-work-images" / "pages", "image-md"),
        (ROOT / "imports" / "live-sources" / "confluence-work" / "snapshots", "snapshot"),
    ]
    pages: list[PageExport] = []
    for root, kind in roots:
        if not root.exists():
            continue
        for path in sorted(root.glob("*.md")):
            export = read_export(path, kind)
            if export:
                pages.append(export)
    return pages


def docs_text() -> str:
    return "\n".join(path.read_text(encoding="utf-8", errors="replace") for path in DOCS.rglob("*.md"))


def used_confluence_assets() -> set[str]:
    used: set[str] = set()
    pattern = re.compile(r"assets/images/confluence/(confluence-\d+\.[a-zA-Z0-9]+)")
    for path in DOCS.rglob("*.md"):
        text = path.read_text(encoding="utf-8", errors="replace")
        if "<!-- confluence-gallery:start -->" not in text:
            continue
        used.update(pattern.findall(text))
    return used


def generated_gallery_pages() -> int:
    return sum(
        1
        for path in DOCS.rglob("*.md")
        if "<!-- confluence-gallery:start -->" in path.read_text(encoding="utf-8", errors="replace")
    )


def build_records() -> tuple[dict[str, PageRecord], dict[str, int], set[str], set[str]]:
    records: dict[str, PageRecord] = {}
    all_docs = docs_text()
    exports = read_exports()

    for export in exports:
        key = export.url
        record = records.setdefault(
            key,
            PageRecord(title=export.title, url=export.url, page_id=export.page_id),
        )
        record.exports.append(export)
        record.content_targets.update(CONTENT_TARGETS.get(export.page_id, []))
        record.source_url_in_docs = export.url in all_docs

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    image_count_by_url: dict[str, int] = defaultdict(int)
    for item in manifest:
        url = item.get("page_url", "")
        title = item.get("page_title", "Confluence")
        image_count_by_url[url] += 1
        record = records.setdefault(
            url,
            PageRecord(title=title, url=url, page_id=page_id_from_url(url)),
        )
        record.images += 1
        record.image_targets.add(target_for(item))
        record.source_url_in_docs = url in all_docs

    manifest_assets = {item["asset"] for item in manifest}
    used_assets = used_confluence_assets()
    return records, image_count_by_url, manifest_assets, used_assets


def status_for(record: PageRecord) -> str:
    if record.images and record.image_targets and record.images > 0:
        if record.content_targets:
            return "used: content target + image gallery"
        return "used: image gallery"
    if record.content_targets:
        if record.source_url_in_docs:
            return "used: content target + source URL"
        return "mapped: content target, source URL not cited"
    return "review: exported/source known, no wiki target mapping"


def format_paths(paths: set[str]) -> str:
    return "<br>".join(sorted(paths)) if paths else "-"


def main() -> int:
    records, image_count_by_url, manifest_assets, used_assets = build_records()
    exports = read_exports()
    content_exports = [p for p in exports if p.export_kind == "content-md"]
    image_exports = [p for p in exports if p.export_kind == "image-md"]
    snapshot_exports = [p for p in exports if p.export_kind == "snapshot"]

    all_export_urls = {p.url for p in exports}
    image_urls = set(image_count_by_url)
    records_without_target = [r for r in records.values() if status_for(r).startswith("review:")]
    mapped_no_source = [r for r in records.values() if status_for(r).startswith("mapped:")]
    unused_assets = sorted(manifest_assets - used_assets)
    extra_assets = sorted(used_assets - manifest_assets)

    lines: list[str] = [
        "# Confluence Usage Audit",
        "",
        "Generated by `tools/audit_confluence_usage.py`.",
        "",
        "## Summary",
        "",
        f"- Content markdown exports: **{len(content_exports)}**",
        f"- Image markdown exports: **{len(image_exports)}**",
        f"- Snapshot markdown exports: **{len(snapshot_exports)}**",
        f"- Unique Confluence source URLs exported to markdown: **{len(all_export_urls)}**",
        f"- Unique Confluence source URLs with imported images: **{len(image_urls)}**",
        f"- Public Confluence image assets in manifest: **{len(manifest_assets)}**",
        f"- Public Confluence image assets used in wiki galleries: **{len(used_assets)}**",
        f"- Wiki pages with generated Confluence galleries: **{generated_gallery_pages()}**",
        f"- Unused public image assets: **{len(unused_assets)}**",
        f"- Extra gallery assets not in manifest: **{len(extra_assets)}**",
        f"- Exported/source URLs with no wiki target mapping: **{len(records_without_target)}**",
        f"- Content-mapped URLs where the source URL is not cited in docs: **{len(mapped_no_source)}**",
        "",
        "## Verdict",
        "",
    ]

    if not unused_assets and not records_without_target:
        lines.append("All imported Confluence public image assets are used, and every exported/source URL has a wiki target mapping.")
    else:
        lines.append("There are items to review before calling the Confluence import completely done.")
    if mapped_no_source:
        lines.append("Some content pages are mapped to wiki topics but do not yet cite the Confluence source URL directly in the public docs.")

    lines.extend(
        [
            "",
            "## Exported / Source Pages",
            "",
            "| Status | Source title | Images | Wiki target(s) | Source URL | Raw export(s) |",
            "| --- | --- | ---: | --- | --- | --- |",
        ]
    )

    for record in sorted(records.values(), key=lambda r: (status_for(r), r.title.casefold(), r.url)):
        targets = set(record.content_targets) | set(record.image_targets)
        raw_exports = "<br>".join(
            f"{e.export_kind}: `{e.source_path.relative_to(ROOT)}`" for e in sorted(record.exports, key=lambda e: str(e.source_path))
        ) or "-"
        lines.append(
            "| {status} | {title} | {images} | {targets} | {url} | {raw} |".format(
                status=status_for(record),
                title=record.title.replace("|", "\\|"),
                images=record.images,
                targets=format_paths(targets).replace("|", "\\|"),
                url=record.url,
                raw=raw_exports.replace("|", "\\|"),
            )
        )

    if unused_assets:
        lines.extend(["", "## Unused Public Image Assets", ""])
        lines.extend(f"- `{asset}`" for asset in unused_assets)

    if extra_assets:
        lines.extend(["", "## Extra Gallery Assets", ""])
        lines.extend(f"- `{asset}`" for asset in extra_assets)

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")

    print(f"report={REPORT}")
    print(f"content_md={len(content_exports)} image_md={len(image_exports)} unique_export_urls={len(all_export_urls)}")
    print(f"manifest_assets={len(manifest_assets)} used_assets={len(used_assets)} unused_assets={len(unused_assets)}")
    print(f"records_without_target={len(records_without_target)} mapped_no_source_url={len(mapped_no_source)}")
    return 1 if unused_assets or records_without_target else 0


if __name__ == "__main__":
    raise SystemExit(main())
