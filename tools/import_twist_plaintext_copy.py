from __future__ import annotations

import argparse
import re
import shutil
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


DATE_RE = re.compile(r"^\s*(\d{2}/\d{2}/\d{2})\s*$")
FILE_RE = re.compile(
    r"^\s*(?P<name>.+?\.(?:pdf|xlsx|xlsm|docx|zip|jpg|jpeg|png|gif|txt|csv))\s*$",
    re.I,
)
SIZE_RE = re.compile(r"^\s*\d+(?:[.,]\d+)?\s*(?:B|KB|MB|GB|BTXT)\s*$", re.I)
URL_RE = re.compile(r"https?://[^\s)>\]]+", re.I)
EMAIL_RE = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I)


@dataclass
class Block:
    index: int
    date: str
    text: str
    files: list[str]
    urls: list[str]
    emails: list[str]


def read_text(path: Path) -> str:
    data = path.read_bytes()
    for encoding in ("utf-8-sig", "utf-8", "cp1251", "latin-1"):
        try:
            return data.decode(encoding)
        except UnicodeDecodeError:
            continue
    return data.decode("utf-8", errors="replace")


def parse_blocks(text: str) -> list[Block]:
    blocks: list[Block] = []
    current_date = "undated"
    buffer: list[str] = []

    def flush() -> None:
        nonlocal buffer
        body = "\n".join(buffer).strip()
        if not body:
            buffer = []
            return
        files: list[str] = []
        lines = body.splitlines()
        for i, line in enumerate(lines):
            match = FILE_RE.match(line)
            if not match:
                continue
            name = match.group("name").strip()
            if i + 1 < len(lines) and SIZE_RE.match(lines[i + 1]):
                name = f"{name} ({lines[i + 1].strip()})"
            files.append(name)
        urls = sorted(set(URL_RE.findall(body)))
        emails = sorted(set(EMAIL_RE.findall(body)))
        blocks.append(
            Block(
                index=len(blocks) + 1,
                date=current_date,
                text=body,
                files=files,
                urls=urls,
                emails=emails,
            )
        )
        buffer = []

    for raw_line in text.splitlines():
        match = DATE_RE.match(raw_line)
        if match:
            flush()
            current_date = match.group(1)
            continue
        buffer.append(raw_line)
    flush()
    return blocks


def write_markdown(path: Path, source: Path, blocks: list[Block]) -> None:
    lines: list[str] = [
        "# Twist Manual Browser Copy",
        "",
        "!!! warning",
        "    Private local archive from manually copied Twist history. Do not publish without redaction.",
        "",
        f"- Source file: `{source}`",
        f"- Imported at: {datetime.now().isoformat(timespec='seconds')}",
        f"- Blocks/messages: {len(blocks)}",
        "",
        "## Timeline",
        "",
    ]
    for block in blocks:
        lines.append(f"### {block.index:04d} - {block.date}")
        if block.files:
            lines.append("")
            lines.append("Files mentioned:")
            for file_name in block.files:
                lines.append(f"- `{file_name}`")
        if block.urls:
            lines.append("")
            lines.append("URLs mentioned:")
            for url in block.urls:
                lines.append(f"- {url}")
        if block.emails:
            lines.append("")
            lines.append("Emails/private contact markers:")
            for email in block.emails:
                lines.append(f"- `{email}`")
        lines.append("")
        lines.append("```text")
        lines.append(block.text)
        lines.append("```")
        lines.append("")
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_audit(path: Path, source: Path, blocks: list[Block], raw_copy: Path, md_path: Path) -> None:
    dates = [block.date for block in blocks if block.date != "undated"]
    files = sorted({file for block in blocks for file in block.files})
    urls = sorted({url for block in blocks for url in block.urls})
    emails = sorted({email for block in blocks for email in block.emails})
    lines = [
        "# Manual Browser Copy Audit",
        "",
        "| Metric | Value |",
        "| --- | ---: |",
        f"| Blocks/messages | {len(blocks)} |",
        f"| First visible date | {dates[0] if dates else 'n/a'} |",
        f"| Last visible date | {dates[-1] if dates else 'n/a'} |",
        f"| Files mentioned | {len(files)} |",
        f"| URLs mentioned | {len(urls)} |",
        f"| Email/private contact markers | {len(emails)} |",
        "",
        "## Files",
        "",
        f"- Raw preserved copy: `{raw_copy}`",
        f"- Readable markdown: `{md_path}`",
        f"- Original source read: `{source}`",
        "",
        "## Privacy Boundary",
        "",
        "- This import stays under `imports/`, which is ignored by git.",
        "- It includes pasted private dialogue and may include pay/bank/contact data.",
        "- Use it as a local archive only until a separate redacted work extract is prepared.",
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Import a manually copied Twist plaintext history.")
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    out_dir: Path = args.output
    out_dir.mkdir(parents=True, exist_ok=True)

    stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    raw_copy = out_dir / f"twist-manual-copy-{stamp}.txt"
    shutil.copy2(args.input, raw_copy)

    text = read_text(raw_copy)
    blocks = parse_blocks(text)
    md_path = out_dir / f"twist-manual-copy-{stamp}.md"
    audit_path = out_dir / f"twist-manual-copy-{stamp}-AUDIT.md"
    write_markdown(md_path, raw_copy, blocks)
    write_audit(audit_path, raw_copy, blocks, raw_copy, md_path)

    print(f"raw_copy={raw_copy}")
    print(f"markdown={md_path}")
    print(f"audit={audit_path}")
    print(f"blocks={len(blocks)}")
    dates = [block.date for block in blocks if block.date != "undated"]
    if dates:
        print(f"date_range={dates[0]}..{dates[-1]}")
    print(f"files_mentioned={len({file for block in blocks for file in block.files})}")
    print(f"urls={len({url for block in blocks for url in block.urls})}")
    print(f"emails={len({email for block in blocks for email in block.emails})}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
