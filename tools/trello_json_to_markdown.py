from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^\w\s.-]+", "", value, flags=re.UNICODE)
    value = re.sub(r"[\s_]+", "-", value, flags=re.UNICODE)
    value = value.strip(".-")
    return value or "untitled"


def md_escape(value: str) -> str:
    return value.replace("\r\n", "\n").replace("\r", "\n").strip()


def checklist_map(board: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    by_card: dict[str, list[dict[str, Any]]] = {}
    for checklist in board.get("checklists", []):
        card_id = checklist.get("idCard")
        if not card_id:
            continue
        by_card.setdefault(card_id, []).append(checklist)
    return by_card


def write_card(card: dict[str, Any], checklists: list[dict[str, Any]]) -> str:
    lines: list[str] = []
    name = md_escape(card.get("name", "Untitled card"))
    lines.append(f"## {name}")
    lines.append("")

    url = card.get("shortUrl") or card.get("url")
    if url:
        lines.append(f"Source: {url}")
        lines.append("")

    labels = [label.get("name") for label in card.get("labels", []) if label.get("name")]
    if labels:
        lines.append("Labels: " + ", ".join(labels))
        lines.append("")

    desc = md_escape(card.get("desc", ""))
    if desc:
        lines.append(desc)
        lines.append("")

    for checklist in checklists:
        checklist_name = md_escape(checklist.get("name", "Checklist"))
        lines.append(f"### {checklist_name}")
        lines.append("")
        for item in checklist.get("checkItems", []):
            checked = "x" if item.get("state") == "complete" else " "
            item_name = md_escape(item.get("name", ""))
            lines.append(f"- [{checked}] {item_name}")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def convert(input_path: Path, output_dir: Path) -> list[Path]:
    board = json.loads(input_path.read_text(encoding="utf-8-sig"))
    board_name = board.get("name") or input_path.stem
    board_dir = output_dir / slugify(board_name)
    board_dir.mkdir(parents=True, exist_ok=True)

    lists = {item["id"]: item for item in board.get("lists", []) if not item.get("closed")}
    cards_by_list: dict[str, list[dict[str, Any]]] = {list_id: [] for list_id in lists}
    for card in board.get("cards", []):
        if card.get("closed"):
            continue
        list_id = card.get("idList")
        if list_id in cards_by_list:
            cards_by_list[list_id].append(card)

    by_card = checklist_map(board)
    written: list[Path] = []

    index_lines = [f"# {board_name}", "", f"Source export: `{input_path}`", ""]
    for list_id, trello_list in lists.items():
        list_name = trello_list.get("name", "Untitled list")
        filename = f"{slugify(list_name)}.md"
        index_lines.append(f"- [{list_name}]({filename})")

        lines = [f"# {list_name}", "", f"Board: {board_name}", ""]
        for card in cards_by_list.get(list_id, []):
            lines.append(write_card(card, by_card.get(card.get("id"), [])))

        out_path = board_dir / filename
        out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
        written.append(out_path)

    index_path = board_dir / "index.md"
    index_path.write_text("\n".join(index_lines).rstrip() + "\n", encoding="utf-8")
    written.insert(0, index_path)
    return written


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert Trello board JSON export to reviewable Markdown.")
    parser.add_argument("--input", required=True, type=Path, help="Path to Trello board JSON export.")
    parser.add_argument("--output", required=True, type=Path, help="Output directory for generated Markdown.")
    args = parser.parse_args()

    written = convert(args.input, args.output)
    for path in written:
        print(path)


if __name__ == "__main__":
    main()
