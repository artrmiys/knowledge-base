"""Place imported Confluence images onto the closest wiki topic pages.

The importer keeps raw/source metadata in docs/assets/images/confluence/manifest.json.
This script adds a generated gallery block to each target markdown page.
Generated blocks are delimited by markers so they can be safely refreshed.
"""

from __future__ import annotations

import argparse
import html
import json
from collections import defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MANIFEST = DOCS / "assets" / "images" / "confluence" / "manifest.json"

START = "<!-- confluence-gallery:start -->"
END = "<!-- confluence-gallery:end -->"


def clean_title(title: str) -> str:
    return (
        title.replace("◼️", "")
        .replace("◼", "")
        .replace("\u200b", "")
        .strip()
    )


def target_for(item: dict[str, Any]) -> str:
    """Return a docs-relative markdown path for a Confluence image item."""
    title = clean_title(item.get("page_title", ""))
    key = title.casefold()

    if "anchor bolts" in key:
        return "work/deck/anchor-bolts.md"
    if "balcony trims" in key:
        return "work/deck/balcony-trims.md"
    if "railing" in key:
        return "work/deck/railing.md"

    if "com commercial" in key:
        return "work-types/com.md"

    if key == "---" or "need to sort" in key:
        return "reference/boss-feedback-rules.md"
    if "dictionary" in key or "materials" in key:
        return "reference/source-map.md"
    if "excel" in key or "planswift" in key:
        return "start/how-to-use.md"
    if key == "work" or key.startswith("work -"):
        return "start/takeoff-structure.md"
    if "vertical constructions" in key or key == "walls":
        return "start/takeoff-structure.md"
    if "roof framing" in key:
        return "start/takeoff-structure.md"

    if "hanger" in key:
        return "reference/hangers.md"

    if "beam" in key:
        return "work/horizontal/floor-framing/beam.md"
    if "joist" in key:
        return "work/horizontal/floor-framing/joist.md"
    if "post" in key:
        return "work/horizontal/floor-framing/post.md"

    if "ridge" in key:
        return "work/horizontal/roof-framing/ridge.md"
    if "header" in key:
        return "work/horizontal/roof-framing/header.md"
    if "dbl trpl rafters" in key:
        return "work/horizontal/roof-framing/dbl-trpl-rafters.md"
    if "hip" in key:
        return "work/horizontal/roof-framing/hip.md"
    if "valley" in key:
        return "work/horizontal/roof-framing/valley.md"
    if "overframes" in key:
        return "work/horizontal/roof-framing/overframes.md"
    if "canopy" in key:
        return "work/horizontal/roof-framing/canopy.md"
    if "dormer" in key:
        return "work/horizontal/roof-framing/dormer.md"
    if "roof sheathing" in key:
        return "work/horizontal/roof-framing/roof-sheathing.md"

    if "openings" in key:
        return "work/vertical/openings/windows-doors.md"
    if "sill plates" in key:
        return "work/vertical/walls/sill-plates.md"
    if key.startswith("exterior"):
        return "work/vertical/walls/exterior.md"
    if key.startswith("corridor"):
        return "work/vertical/walls/corridor.md"
    if key.startswith("demising"):
        return "work/vertical/walls/demising.md"
    if key.startswith("unit"):
        return "work/vertical/walls/unit.md"
    if key.startswith("parapet"):
        return "work/vertical/walls/parapet.md"
    if key.startswith("shaft"):
        return "work/vertical/walls/shaft.md"
    if key.startswith("gable"):
        return "work/vertical/walls/gable.md"

    if key.startswith("floor"):
        return "work/vertical/sheathing/floor.md"
    if "truss heel" in key:
        return "work/vertical/sheathing/truss-heel.md"
    if key == "sheathing" or "wall sheathing" in key:
        return "work/vertical/sheathing/wall-sheathing.md"
    if "shear wall" in key:
        return "work/vertical/sheathing/shear-wall.md"

    return "reference/confluence-image-archive.md"


def relative_asset_path(target: str, asset: str) -> str:
    page_parts = Path(target).with_suffix("").parts
    return "../" * len(page_parts) + f"assets/images/confluence/{asset}"


def raw_kb(size: int | None) -> str:
    if not size:
        return "unknown size"
    kb = max(1, round(size / 1024))
    return f"{kb} KB raw"


def description_for(title: str) -> str:
    key = clean_title(title).casefold()

    if "anchor bolts" in key:
        return "anchor bolt detail/reference"
    if "balcony trims" in key:
        return "balcony trim reference"
    if "railing" in key:
        return "railing reference"

    if "com commercial" in key:
        return "COM takeoff workflow/reference"
    if key == "---" or "need to sort" in key:
        return "unsorted field rule/reference"
    if "dictionary" in key:
        return "dictionary reference"
    if "materials" in key:
        return "material reference"
    if "excel" in key:
        return "Excel workflow screenshot"
    if "planswift" in key:
        return "PlanSwift workflow screenshot"
    if key == "work" or key.startswith("work -"):
        return "takeoff structure reference"
    if "vertical constructions" in key:
        return "vertical construction overview"
    if key == "walls":
        return "wall type overview"
    if "roof framing" in key:
        return "roof framing overview"

    if "hanger" in key:
        return "hanger schedule/detail reference"

    if "beam" in key:
        return "beam takeoff/reference"
    if "joist series" in key:
        return "joist series/reference"
    if "joist" in key:
        return "joist layout/reference"
    if "post" in key:
        return "post/column reference"

    if "ridge" in key:
        return "ridge reference"
    if "header" in key:
        return "roof header reference"
    if "dbl trpl rafters" in key:
        return "double/triple rafter reference"
    if "hip" in key:
        return "hip rafter/reference"
    if "valley" in key:
        return "valley rafter/reference"
    if "overframes" in key:
        return "overframe reference"
    if "canopy" in key:
        return "canopy framing reference"
    if "dormer" in key:
        return "dormer framing reference"
    if "roof sheathing" in key:
        return "roof sheathing reference"

    if "openings" in key:
        return "opening schedule/reference"
    if "sill plates" in key:
        return "sill plate / anchor layout reference"
    if key.startswith("exterior"):
        return "exterior wall detail/reference"
    if key.startswith("corridor"):
        return "corridor wall reference"
    if key.startswith("demising"):
        return "demising wall reference"
    if key.startswith("unit"):
        return "unit/interior wall reference"
    if key.startswith("parapet"):
        return "parapet wall reference"
    if key.startswith("shaft"):
        return "shaft/fire wall reference"
    if key.startswith("gable"):
        return "gable wall reference"

    if key.startswith("floor"):
        return "floor-height sheathing reference"
    if "truss heel" in key:
        return "truss heel sheathing reference"
    if key == "sheathing" or "wall sheathing" in key:
        return "wall sheathing reference"
    if "shear wall" in key:
        return "shear wall sheathing reference"

    return "Confluence visual reference"


def group_summary(items: list[dict[str, Any]]) -> str:
    groups: dict[tuple[str, str], int] = defaultdict(int)
    for item in items:
        groups[(clean_title(item.get("page_title", "Confluence")), item.get("page_url", ""))] += 1

    lines = ["| Source group | Images | Confluence |", "| --- | ---: | --- |"]
    for (title, url), count in sorted(groups.items(), key=lambda row: row[0][0].casefold()):
        label = html.escape(title or "Confluence")
        link = f"[source]({url})" if url else "source"
        lines.append(f"| {label} | {count} | {link} |")
    return "\n".join(lines)


def render_gallery(target: str, items: list[dict[str, Any]]) -> str:
    lines: list[str] = [
        START,
        "## Confluence Images",
        "",
        "Изображения из Confluence размещены на этой странице по исходной теме.",
        "Подпись сохраняет группу-источник, чтобы можно было быстро проверить контекст.",
        "",
        group_summary(items),
        "",
        '<div class="kb-gallery">',
    ]

    counters: dict[str, int] = defaultdict(int)
    for item in items:
        title = clean_title(item.get("page_title", "Confluence"))
        counters[title] += 1
        number = counters[title]
        asset_path = relative_asset_path(target, item["asset"])
        attachment = item.get("title") or item.get("asset") or "attachment"
        mode = "preview" if item.get("converted_preview") else "image"
        subject = description_for(title)
        caption = f"{subject} {number:02d} ({mode}, {raw_kb(item.get('raw_size'))})"
        alt = f"{title} - {subject} {number:02d}"
        lines.extend(
            [
                (
                    f'  <a class="kb-gallery__item" href="{html.escape(asset_path)}" '
                    f'title="{html.escape(attachment)}">'
                ),
                f'    <img src="{html.escape(asset_path)}" alt="{html.escape(alt)}">',
                f'    <div class="kb-gallery__caption">{html.escape(caption)}</div>',
                "  </a>",
            ]
        )

    lines.extend(["</div>", END, ""])
    return "\n".join(lines)


def remove_existing_block(text: str) -> str:
    start = text.find(START)
    if start == -1:
        return text.rstrip() + "\n"
    end = text.find(END, start)
    if end == -1:
        raise ValueError("Found gallery start marker without end marker")
    end += len(END)
    return (text[:start].rstrip() + "\n\n" + text[end:].lstrip()).rstrip() + "\n"


def write_page(target: str, items: list[dict[str, Any]], dry_run: bool) -> bool:
    path = DOCS / target
    if not path.exists():
        raise FileNotFoundError(path)

    old = path.read_text(encoding="utf-8")
    base = remove_existing_block(old)
    new = base.rstrip() + "\n\n" + render_gallery(target, items)
    if new == old:
        return False
    if not dry_run:
        path.write_text(new, encoding="utf-8", newline="\n")
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    by_target: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in manifest:
        by_target[target_for(item)].append(item)

    changed = 0
    for target in sorted(by_target):
        items = by_target[target]
        touched = write_page(target, items, args.dry_run)
        changed += int(touched)
        status = "would update" if args.dry_run and touched else "updated" if touched else "unchanged"
        print(f"{status}: {target} ({len(items)} images)")

    print(f"targets={len(by_target)} changed={changed} images={len(manifest)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
