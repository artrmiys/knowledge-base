"""Convert authenticated Trello full-board JSON exports into raw Markdown.

The export is captured from a logged-in browser through Trello's `/1/boards`
endpoint.  This importer preserves every card in a local, gitignored raw archive:
card metadata, descriptions, checklists, attachments, and board actions.
"""

from __future__ import annotations

import argparse
import base64
import json
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OUT_ROOT = ROOT / "imports" / "live-sources"


def slugify(value: str, fallback: str = "item") -> str:
    value = re.sub(r"\s+", " ", value or "").strip().lower()
    value = re.sub(r"[^a-z0-9а-яё]+", "-", value, flags=re.IGNORECASE)
    value = value.strip("-")
    return (value[:100] or fallback).strip("-") or fallback


def ext_for(mime: str, name: str) -> str:
    suffix = Path(name or "").suffix.lower()
    if suffix:
        return suffix
    return {
        "image/jpeg": ".jpg",
        "image/jpg": ".jpg",
        "image/png": ".png",
        "image/gif": ".gif",
        "image/webp": ".webp",
        "image/svg+xml": ".svg",
        "application/pdf": ".pdf",
    }.get((mime or "").split(";", 1)[0].lower(), ".bin")


def decode_data_url(data_url: str) -> tuple[str, bytes]:
    if not data_url.startswith("data:") or "," not in data_url:
        return "", b""
    meta, encoded = data_url.split(",", 1)
    mime = meta.replace("data:", "").split(";", 1)[0]
    return mime, base64.b64decode(encoded)


def card_url(card: dict[str, Any]) -> str:
    if card.get("url"):
        return card["url"]
    short = card.get("shortLink") or card.get("shortUrl") or ""
    return f"https://trello.com/c/{short}" if short else ""


def by_id(items: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {str(item.get("id")): item for item in items if item.get("id")}


def actions_for_card(actions: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for action in actions:
        card = (action.get("data") or {}).get("card") or {}
        card_id = card.get("id")
        if card_id:
            grouped[str(card_id)].append(action)
    return grouped


def markdown_list(values: list[str]) -> str:
    if not values:
        return "_None._"
    return "\n".join(f"- {value}" for value in values)


def write_attachments(payload: dict[str, Any], output: Path) -> dict[str, list[dict[str, Any]]]:
    images_dir = output / "attachments"
    images_dir.mkdir(parents=True, exist_ok=True)
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    counters: dict[str, int] = defaultdict(int)

    for item in payload.get("downloadedAttachments") or []:
        card_id = str(item.get("cardId") or "")
        if not card_id:
            continue
        counters[card_id] += 1
        record = {key: value for key, value in item.items() if key != "dataUrl"}
        data_url = item.get("dataUrl") or ""
        if item.get("ok") and data_url:
            mime, data = decode_data_url(data_url)
            short = item.get("shortLink") or card_id
            stem = f"{slugify(short)}-{counters[card_id]:02d}-{slugify(item.get('name') or 'attachment')}"
            file_name = stem + ext_for(mime or item.get("mimeType", ""), item.get("name", ""))
            path = images_dir / file_name
            path.write_bytes(data)
            record["local"] = str(path.relative_to(output)).replace("\\", "/")
            record["file"] = file_name
            record["decodedBytes"] = len(data)
        grouped[card_id].append(record)
    return grouped


def render_card(
    card: dict[str, Any],
    list_name: str,
    labels: list[str],
    members: list[str],
    checklists: list[dict[str, Any]],
    actions: list[dict[str, Any]],
    attachments: list[dict[str, Any]],
) -> str:
    lines = [
        f"# {card.get('name') or 'Untitled card'}",
        "",
        f"Source: {card_url(card)}",
        "",
        f"Imported: {datetime.now(timezone.utc).isoformat()}",
        "",
        "## Card Metadata",
        "",
        f"- Board list: {list_name or '_unknown_'}",
        f"- Card ID: `{card.get('id') or ''}`",
        f"- Short link: `{card.get('shortLink') or ''}`",
        f"- Closed: `{card.get('closed')}`",
        f"- Due: `{card.get('due') or ''}`",
        f"- Start: `{card.get('start') or ''}`",
        f"- Date last activity: `{card.get('dateLastActivity') or ''}`",
        f"- Position: `{card.get('pos') or ''}`",
        "",
        "Labels:",
        markdown_list(labels),
        "",
        "Members:",
        markdown_list(members),
        "",
        "## Description",
        "",
        (card.get("desc") or "_No description._").strip() or "_No description._",
        "",
    ]

    if checklists:
        lines.extend(["## Checklists", ""])
        for checklist in checklists:
            lines.extend([f"### {checklist.get('name') or 'Checklist'}", ""])
            for item in checklist.get("checkItems") or []:
                checked = "x" if item.get("state") == "complete" else " "
                lines.append(f"- [{checked}] {item.get('name') or ''}")
            lines.append("")

    lines.extend(["## Attachments", ""])
    if attachments:
        for attachment in attachments:
            local = attachment.get("local")
            name = attachment.get("name") or attachment.get("file") or "attachment"
            source = attachment.get("url") or ""
            if local and (attachment.get("mimeType") or "").startswith("image/"):
                lines.append(f"- ![{name}](../{local})")
            elif local:
                lines.append(f"- [{name}](../{local})")
            else:
                status = f"download failed: {attachment.get('status')}" if attachment.get("ok") is False else "not downloaded"
                lines.append(f"- {name} ({status})")
            if source:
                lines.append(f"  Source: {source}")
            if attachment.get("bytes") or attachment.get("decodedBytes"):
                lines.append(f"  Bytes: `{attachment.get('decodedBytes') or attachment.get('bytes')}`")
    else:
        lines.append("_No attachments._")
    lines.append("")

    lines.extend(["## Actions", ""])
    if actions:
        for action in sorted(actions, key=lambda row: row.get("date") or ""):
            action_type = action.get("type") or "action"
            date = action.get("date") or ""
            member = ((action.get("memberCreator") or {}).get("fullName") or "").strip()
            text = (((action.get("data") or {}).get("text") or "")).strip()
            suffix = f" - {text}" if text else ""
            member_text = f" by {member}" if member else ""
            lines.append(f"- `{date}` `{action_type}`{member_text}{suffix}")
    else:
        lines.append("_No actions in export._")
    lines.append("")

    return "\n".join(lines)


def write_pages(payload: dict[str, Any], output: Path) -> list[dict[str, Any]]:
    board = payload["board"]
    lists = by_id(board.get("lists") or [])
    label_map = by_id(board.get("labels") or [])
    member_map = by_id(board.get("members") or [])
    checklists_by_card: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for checklist in board.get("checklists") or []:
        checklists_by_card[str(checklist.get("idCard") or "")].append(checklist)
    actions_by_card = actions_for_card(board.get("actions") or [])
    attachments_by_card = write_attachments(payload, output)

    pages_dir = output / "pages"
    pages_dir.mkdir(parents=True, exist_ok=True)
    records: list[dict[str, Any]] = []
    cards = sorted(board.get("cards") or [], key=lambda row: (str(row.get("idList") or ""), float(row.get("pos") or 0)))
    for index, card in enumerate(cards, start=1):
        card_id = str(card.get("id") or "")
        list_name = lists.get(str(card.get("idList") or ""), {}).get("name", "")
        labels = [
            label_map.get(str(label_id), {}).get("name") or str(label_id)
            for label_id in card.get("idLabels") or []
        ]
        members = [
            member_map.get(str(member_id), {}).get("fullName") or str(member_id)
            for member_id in card.get("idMembers") or []
        ]
        short = card.get("shortLink") or card_id
        stem = f"{index:02d}-{slugify(short)}-{slugify(card.get('name') or 'card')}"
        path = pages_dir / f"{stem}.md"
        path.write_text(
            render_card(
                card=card,
                list_name=list_name,
                labels=labels,
                members=members,
                checklists=checklists_by_card.get(card_id, []),
                actions=actions_by_card.get(card_id, []),
                attachments=attachments_by_card.get(card_id, []),
            ),
            encoding="utf-8",
            newline="\n",
        )
        records.append(
            {
                "id": card_id,
                "shortLink": short,
                "name": card.get("name") or "",
                "list": list_name,
                "url": card_url(card),
                "closed": bool(card.get("closed")),
                "attachments": len(card.get("attachments") or []),
                "downloadedAttachments": len(attachments_by_card.get(card_id, [])),
                "file": str(path.relative_to(output)).replace("\\", "/"),
            }
        )
    return records


def write_summary(payload: dict[str, Any], output: Path, records: list[dict[str, Any]]) -> None:
    board = payload["board"]
    actions = board.get("actions") or []
    checklists = board.get("checklists") or []
    cards = board.get("cards") or []
    downloaded = payload.get("downloadedAttachments") or []
    comments = [action for action in actions if action.get("type") == "commentCard"]
    summary = {
        "source": payload.get("source"),
        "created_at": datetime.now(timezone.utc).isoformat(),
        "exported_at": payload.get("exportedAt"),
        "board_id": board.get("id"),
        "board_name": board.get("name"),
        "board_url": board.get("url"),
        "lists": len(board.get("lists") or []),
        "cards": len(cards),
        "open_cards": len([card for card in cards if not card.get("closed")]),
        "closed_cards": len([card for card in cards if card.get("closed")]),
        "attachments": sum(len(card.get("attachments") or []) for card in cards),
        "downloaded_attachments": len([item for item in downloaded if item.get("ok")]),
        "failed_attachments": len([item for item in downloaded if item.get("ok") is False]),
        "actions": len(actions),
        "comments": len(comments),
        "checklists": len(checklists),
        "check_items": sum(len(checklist.get("checkItems") or []) for checklist in checklists),
        "pages": records,
    }
    (output / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        f"# Trello Full Export Audit — {board.get('name')}",
        "",
        f"Source board: `{board.get('url')}`",
        "",
        f"- Cards: **{summary['cards']}**",
        f"- Lists: **{summary['lists']}**",
        f"- Attachments in API: **{summary['attachments']}**",
        f"- Attachments downloaded: **{summary['downloaded_attachments']}**",
        f"- Failed attachment downloads: **{summary['failed_attachments']}**",
        f"- Actions: **{summary['actions']}**",
        f"- Comments: **{summary['comments']}**",
        f"- Checklists: **{summary['checklists']}**",
        "",
        "| List | Card | Attachments | Raw MD |",
        "| --- | --- | ---: | --- |",
    ]
    for record in records:
        lines.append(
            f"| {record['list']} | [{record['name']}]({record['url']}) | {record['attachments']} | `{record['file']}` |"
        )
    (output / "AUDIT.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    payload = json.loads(args.input.read_text(encoding="utf-8"))
    source = payload.get("source") or slugify(payload.get("board", {}).get("name") or args.input.stem)
    output = args.output or OUT_ROOT / f"{source}-full"
    output.mkdir(parents=True, exist_ok=True)
    records = write_pages(payload, output)
    write_summary(payload, output, records)
    print(f"source={source} cards={len(records)} output={output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
