"""Write a durable coverage report for authenticated Confluence/Trello imports."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
IMPORTS = ROOT / "imports" / "live-sources"
REPORT = IMPORTS / "FULL_SOURCE_AUDIT.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    confluence = load(IMPORTS / "confluence-work-full" / "summary.json")
    trello_int = load(IMPORTS / "trello-int-trims-full" / "summary.json")
    trello_important = load(IMPORTS / "trello-important-changes-full" / "summary.json")

    lines = [
        "# Full Live Source Coverage Audit",
        "",
        "Generated from authenticated browser exports. This report lives under",
        "`imports/`, so it is local-only and not published by MkDocs.",
        "",
        "## Summary",
        "",
        "| Source | Pages/cards | Attachments | Downloaded | Notes |",
        "| --- | ---: | ---: | ---: | --- |",
        (
            f"| Confluence `work` space | {confluence['pages']} pages "
            f"({confluence['public_pages']} public/raw, {confluence['private_pages']} private/raw) | "
            f"{confluence['attachments']} | 175 raw image files already present | "
            "Full REST body export, private pages kept out of public docs |"
        ),
        (
            f"| Trello `int trims` | {trello_int['cards']} cards | "
            f"{trello_int['attachments']} | {trello_int['downloaded_attachments']} | "
            f"{trello_int['actions']} actions, {trello_int['comments']} comments |"
        ),
        (
            f"| Trello `изменения очень важно` | {trello_important['cards']} cards "
            f"({trello_important['open_cards']} open, {trello_important['closed_cards']} closed) | "
            f"{trello_important['attachments']} | {trello_important['downloaded_attachments']} | "
            f"{trello_important['actions']} actions, {trello_important['comments']} comments |"
        ),
        "",
        "## Public Boundary",
        "",
        "- Public wiki source maps cite counts, relationships, and safe source URLs.",
        "- Private Confluence pages are stored only in `imports/live-sources/confluence-work-full/pages-private/`.",
        "- Trello cards with private/tooling links are redacted in `docs/reference/trello-source-map.md`.",
        "- Credentials, cookies, tokens, invite links, and salary/payment details must not be copied into `docs/`.",
        "",
        "## Raw Archive Locations",
        "",
        "| Source | Raw location |",
        "| --- | --- |",
        "| Confluence full REST JSON | `imports/live-sources/confluence-work/confluence-work-full-rest-export-2026-05-07.json` |",
        "| Confluence full markdown | `imports/live-sources/confluence-work-full/` |",
        "| Confluence raw attachment images | `imports/live-sources/confluence-work-images/images/` |",
        "| Trello int trims full JSON | `imports/live-sources/trello-int-trims/trello-int-trims-full-with-attachments-2026-05-07.json` |",
        "| Trello int trims full markdown/assets | `imports/live-sources/trello-int-trims-full/` |",
        "| Trello important changes full JSON | `imports/live-sources/trello-important-changes/trello-important-changes-full-with-attachments-2026-05-07.json` |",
        "| Trello important changes full markdown/assets | `imports/live-sources/trello-important-changes-full/` |",
        "",
        "## Public Wiki Maps",
        "",
        "- `docs/reference/confluence-source-map.md`",
        "- `docs/reference/confluence-image-archive.md`",
        "- `docs/reference/trello-source-map.md`",
        "- `docs/reference/source-map.md`",
        "",
    ]
    REPORT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"wrote {REPORT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
