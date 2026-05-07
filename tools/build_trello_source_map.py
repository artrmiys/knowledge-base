"""Generate a public Trello source map from local full Trello raw exports."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUT = DOCS / "reference" / "trello-source-map.md"
IMPORT_ROOT = ROOT / "imports" / "live-sources"
SUMMARIES = [
    IMPORT_ROOT / "trello-int-trims-full" / "summary.json",
    IMPORT_ROOT / "trello-important-changes-full" / "summary.json",
]


def rel_doc(path: str, label: str | None = None) -> str:
    return f"[{label or path}]({path})"


def sensitive_title(title: str) -> bool:
    key = (title or "").casefold()
    return any(
        marker in key
        for marker in (
            "join.slack",
            "shared_invite",
            "slack.com",
            "ewood.atlassian.net/l/c",
            "password",
            "token",
            "ssh",
            "salary",
        )
    )


def safe_card_title(title: str) -> str:
    if sensitive_title(title):
        return "[private/tooling link card redacted]"
    title = re.sub(r"\s+", " ", title or "").strip()
    return title or "Untitled card"


def target_for(source: str, list_name: str, title: str) -> str:
    key = f"{list_name} {title}".casefold()
    if source == "trello-int-trims":
        if "baseboard" in key:
            return rel_doc("../work/interior-trims/base.md", "Base")
        if "crown" in key:
            return rel_doc("../work/interior-trims/crown.md", "Crown")
        if "door" in key or "cased" in key or "opening" in key:
            return rel_doc("../work/interior-trims/door-window-trim.md", "Door and Window Trim")
        return rel_doc("../work/interior-trims/overview.md", "Interior Trims")

    if sensitive_title(title):
        return "raw only"

    related: list[str] = [rel_doc("../start/important-changes.md", "Important Changes")]
    topic_rules = [
        (("roof", "rafter", "rake", "ajs"), "../work/horizontal/roof-framing/roof-sheathing.md", "Roof Framing"),
        (("balcony", "porch", "deck"), "../work/deck/balcony-trims.md", "Deck / Balcony"),
        (("ewp", "lvl", "tji", "joist", "beam"), "../work/horizontal/floor-framing/joist.md", "Floor Framing"),
        (("blocking", "bracing"), "../work/horizontal/floor-framing/details/blocking.md", "Blocking"),
        (("sheathing", "sheating", "box"), "../work/vertical/sheathing/box-sheathing.md", "Sheathing"),
        (("sqft", "soffit", "vinyl", "cantilevered"), "../work/sqfts/cantilevered.md", "SQFTs"),
        (("post",), "../work/horizontal/floor-framing/post.md", "Post"),
        (("washer", "anchor", "hdu", "simpson"), "../work/deck/anchor-bolts.md", "Anchors / Hangers"),
        (("material", "spaces", "spelling", "excel"), "../reference/boss-feedback-rules.md", "QA / Output"),
    ]
    for markers, path, label in topic_rules:
        if any(marker in key for marker in markers):
            related.append(rel_doc(path, label))
            break
    return "<br>".join(related)


def source_url(summary: dict[str, Any]) -> str:
    if summary.get("board_url"):
        return summary["board_url"]
    source = summary.get("source")
    if source == "trello-int-trims":
        return "https://trello.com/b/TyUKA0Zw/int-trims"
    return "https://trello.com/b/wDztpnZg/изменения-очень-важно"


def render_board(summary: dict[str, Any]) -> list[str]:
    source = summary["source"]
    title = "Interior Trims" if source == "trello-int-trims" else "Important Changes"
    lines = [
        f"## {title}",
        "",
        f"Source board: `{source_url(summary)}`",
        "",
        f"- Cards: **{summary['cards']}** ({summary['open_cards']} open, {summary['closed_cards']} closed)",
        f"- Lists: **{summary['lists']}**",
        f"- Attachments: **{summary['attachments']}**",
        f"- Downloaded attachments: **{summary['downloaded_attachments']}**",
        f"- Actions: **{summary['actions']}**",
        f"- Comments: **{summary['comments']}**",
        "",
        "| List | Card | Attachments | Wiki relation | Raw MD |",
        "| --- | --- | ---: | --- | --- |",
    ]
    for record in summary.get("pages") or []:
        name = safe_card_title(record.get("name") or "")
        is_sensitive = sensitive_title(record.get("name") or "")
        card_cell = name if is_sensitive else f"[{name}]({record.get('url') or ''})"
        raw_cell = "local raw archive only" if is_sensitive else f"`imports/live-sources/{source}-full/{record.get('file')}`"
        lines.append(
            "| "
            + " | ".join(
                [
                    record.get("list") or "",
                    card_cell.replace("|", "\\|"),
                    str(record.get("attachments") or 0),
                    target_for(source, record.get("list") or "", record.get("name") or ""),
                    raw_cell,
                ]
            )
            + " |"
        )
    lines.append("")
    return lines


def main() -> int:
    lines = [
        "# Trello Source Map",
        "",
        "Эта страница показывает полный Trello coverage: какие доски выгружены,",
        "сколько карточек/картинок есть в raw archive, и куда эти правила связаны",
        "в wiki. Raw exports лежат в `imports/` и не публикуются на GitHub Pages.",
        "",
        "Карточки с приватными/tooling ссылками редактируются в публичной таблице,",
        "но остаются в локальном raw archive.",
        "",
    ]
    for summary_path in SUMMARIES:
        summary = json.loads(summary_path.read_text(encoding="utf-8"))
        lines.extend(render_board(summary))
    OUT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"wrote {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
