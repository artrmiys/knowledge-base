"""Find (and optionally replace) symbols that make the KB text look machine-written.

The owner asked (17.10.2026) to keep the site free of long dashes, arrows,
separator dots and guillemets, and to use a plain hyphen or a word instead.

Usage (from the repo root):
  python tools/check_symbols.py          # report, exit 1 if anything is found
  python tools/check_symbols.py --fix    # replace in place, then report the rest

Scanned: docs/**/*.md, mkdocs.yml, docs/assets/images/**/*.svg (text only).
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# symbol -> replacement used by --fix
REPLACE = {
    "—": "-",   # em dash
    "–": "-",   # en dash
    "→": "-",   # right arrow
    "←": "-",   # left arrow
    "⇒": "-",   # double right arrow
    "↔": "-",   # left-right arrow
    "➜": "-",   # heavy arrow
    "·": ",",   # middle dot
    "«": '"',   # guillemet left
    "»": '"',   # guillemet right
}
PATTERN = re.compile("|".join(map(re.escape, REPLACE)))
# arrow icons (:octicons-arrow-right-24: and the like) look the same as arrows
ARROW_ICON = re.compile(r":[a-z]+-(?:[a-z]+-)*arrow-[a-z0-9-]+: ?")


def files():
    yield ROOT / "mkdocs.yml"
    yield from sorted((ROOT / "docs").rglob("*.md"))
    yield from sorted((ROOT / "docs" / "assets" / "images").rglob("*.svg"))


def fix_text(text):
    # " — " and " → " become " - ", a dash glued to words becomes "-"
    text = ARROW_ICON.sub("", text)
    return PATTERN.sub(lambda m: REPLACE[m.group(0)], text)


def main():
    # Windows consoles default to cp1251 and cannot print the symbols we report
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    fix = "--fix" in sys.argv
    found = 0
    for path in files():
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        if fix and (PATTERN.search(text) or ARROW_ICON.search(text)):
            path.write_text(fix_text(text), encoding="utf-8", newline="")
            text = path.read_text(encoding="utf-8")
        for no, line in enumerate(text.splitlines(), 1):
            hits = PATTERN.findall(line) + [h.strip() for h in ARROW_ICON.findall(line)]
            if hits:
                found += len(hits)
                rel = path.relative_to(ROOT).as_posix()
                print(f"{rel}:{no}: {''.join(sorted(set(hits)))}  {line.strip()[:90]}")
    print(f"symbols left: {found}")
    sys.exit(1 if found else 0)


if __name__ == "__main__":
    main()
