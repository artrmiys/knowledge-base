"""Свернуть kb-rule-gallery блоки в читаемые блоки.

Логика:
- Templated (все карточки с одинаковым title/rule/note) → чистый grid в <details>.
- Unique → стек "описание + картинка" (kb-figure-row) в открытом <details>.

Запуск:
  .\.venv\Scripts\python.exe tools\fold_confluence_galleries.py
"""

from __future__ import annotations

import re
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent / "docs"

# Страницы, которые форсируем в row-layout (даже если контент шаблонный):
# хотим единообразие визуала с Interior trims.
FORCE_ROWS_PREFIXES = [
    "work/horizontal/roof-framing/",
]

GALLERY_OPEN = '<div class="kb-rule-gallery">'

CARD_RE = re.compile(
    r'<a class="kb-rule-card"\s+href="([^"]+)"[^>]*>\s*'
    r'<img\s+src="([^"]+)"\s+alt="([^"]*)"[^>]*>\s*'
    r'<div class="kb-rule-card__body">\s*'
    r'<div class="kb-rule-card__title">(.*?)</div>\s*'
    r'<div class="kb-rule-card__rule">(.*?)</div>\s*'
    r'<div class="kb-rule-card__note">(.*?)</div>\s*'
    r'</div>\s*</a>',
    re.DOTALL,
)

OPEN_DIV_RE = re.compile(r'<div\b')
CLOSE_DIV_RE = re.compile(r'</div>')


def find_balanced_div(text: str, start: int) -> int:
    """Given index of '<div ...>' opening, return index just after the matching '</div>'."""
    depth = 1
    j = text.find('>', start) + 1
    while j < len(text) and depth > 0:
        next_open = OPEN_DIV_RE.search(text, j)
        next_close = CLOSE_DIV_RE.search(text, j)
        if not next_close:
            return -1
        if next_open and next_open.start() < next_close.start():
            depth += 1
            j = next_open.end()
        else:
            depth -= 1
            j = next_close.end()
    return j if depth == 0 else -1


def transform_gallery(inner: str, force_rows: bool = False) -> str:
    cards = CARD_RE.findall(inner)
    if not cards:
        return f'{GALLERY_OPEN}{inner}</div>'

    rules = {c[4].strip() for c in cards}
    notes = {c[5].strip() for c in cards}
    # Шаблонный шум: если ВСЕ карточки имеют одинаковые rule+note (титлы могут
    # отличаться только нумерацией "01", "02" — это всё равно шум).
    is_templated = len(rules) <= 1 and len(notes) <= 1
    if force_rows:
        is_templated = False
    n = len(cards)

    if is_templated:
        figures = "\n".join(
            f'    <a class="kb-figure" href="{href}" target="_blank" rel="noopener">'
            f'<img src="{src}" alt="{alt}" loading="lazy"></a>'
            for href, src, alt, _t, _r, _n in cards
        )
        return (
            f'<details class="kb-figures">\n'
            f'  <summary>Показать {n} иллюстраций</summary>\n'
            f'  <div class="kb-figure-grid">\n'
            f'{figures}\n'
            f'  </div>\n'
            f'</details>'
        )

    rows = []
    for href, src, alt, title, rule, note in cards:
        title = title.strip()
        rule = rule.strip()
        note = note.strip()
        text_parts = []
        if title:
            text_parts.append(f'      <div class="kb-figure-row__title">{title}</div>')
        if rule:
            text_parts.append(f'      <div class="kb-figure-row__rule">{rule}</div>')
        if note:
            text_parts.append(f'      <div class="kb-figure-row__note">{note}</div>')
        text_html = "\n".join(text_parts)
        rows.append(
            f'  <figure class="kb-figure-row">\n'
            f'    <figcaption class="kb-figure-row__text">\n'
            f'{text_html}\n'
            f'    </figcaption>\n'
            f'    <a class="kb-figure-row__image" href="{href}" target="_blank" rel="noopener">'
            f'<img src="{src}" alt="{alt}" loading="lazy"></a>\n'
            f'  </figure>'
        )
    rows_html = "\n".join(rows)
    return (
        f'<details class="kb-figures kb-figures--rows" open>\n'
        f'  <summary>Скрыть {n} правил с иллюстрациями</summary>\n'
        f'{rows_html}\n'
        f'</details>'
    )


def process_file(path: Path) -> tuple[bool, int, int]:
    text = path.read_text(encoding="utf-8")
    if GALLERY_OPEN not in text:
        return False, 0, 0

    rel_posix = path.relative_to(DOCS).as_posix()
    force_rows = any(rel_posix.startswith(p) for p in FORCE_ROWS_PREFIXES)

    out_parts = []
    pos = 0
    templated = 0
    unique = 0
    while True:
        i = text.find(GALLERY_OPEN, pos)
        if i == -1:
            out_parts.append(text[pos:])
            break
        out_parts.append(text[pos:i])
        end = find_balanced_div(text, i)
        if end == -1:
            out_parts.append(text[i:])
            break
        inner = text[i + len(GALLERY_OPEN):end - len('</div>')]
        cards = CARD_RE.findall(inner)
        if cards:
            rules = {c[4].strip() for c in cards}
            notes = {c[5].strip() for c in cards}
            if not force_rows and len(rules) <= 1 and len(notes) <= 1:
                templated += 1
            else:
                unique += 1
        out_parts.append(transform_gallery(inner, force_rows=force_rows))
        pos = end

    new_text = "".join(out_parts)
    if new_text != text:
        path.write_text(new_text, encoding="utf-8")
        return True, templated, unique
    return False, templated, unique


def main() -> None:
    changed = 0
    total_t = 0
    total_u = 0
    for md in sorted(DOCS.rglob("*.md")):
        ok, t, u = process_file(md)
        if ok:
            changed += 1
            tag = []
            if t:
                tag.append(f"templated x{t}")
            if u:
                tag.append(f"unique x{u}")
            print(f"  updated: {md.relative_to(DOCS)}  [{', '.join(tag)}]")
            total_t += t
            total_u += u

    print(f"\nUpdated {changed} files. Templated galleries: {total_t}. Unique: {total_u}.")


if __name__ == "__main__":
    main()
