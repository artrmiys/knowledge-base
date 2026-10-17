"""Check that every OurPlanCore function from tools/opc_inventory.json is described in the KB.

Usage (from the KB repo root):
  python tools/opc_coverage.py                 # report to stdout, exit 1 if something is missing
  python tools/opc_coverage.py --report out.md # also write the report as Markdown
  python tools/opc_coverage.py --json out.json # machine-readable result per item

Pages searched: docs/reference/ourplanecore.md, ourplancore-*.md (except the generated
ourplancore-all-functions.md), job-creation-storage.md, takeoff-naming.md.

How an item counts as described:
  1. its title (or an alias: another label of the same command id, the palette title)
     appears in a page in backticks: `Title`  (strong, case-insensitive);
  2. or appears as a whole phrase, case-insensitive, on word boundaries;
  3. or, for phrases of 6+ letters, appears with punctuation and spaces removed.
  Single generic words ("Open", "Refresh", "Size") count only in backticks.
  4. Items with a key also match on the gesture in the KB notation ++ctrl+alt+left++;
     for ambiguous keys (Esc, Delete, F2, Ctrl+Z, single letters) the same line must name
     the function (an English word of the title or its Russian stem, see RU_STEMS).
The best page is the one with the most hits; ties go to the more specific page.

Exceptions live in tools/opc_coverage_ignore.txt, one per line with a reason:
  surface:title      # reason      (title compared without case, dots and dashes; * = any surface)
  id:command.id      # reason
  source:<prefix>    # reason      (file path prefix inside the program sources)
  group:<text>       # reason      (group label contains text, without case)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs" / "reference"
INVENTORY = ROOT / "tools" / "opc_inventory.json"
IGNORE = ROOT / "tools" / "opc_coverage_ignore.txt"
GENERATED_PAGE = "ourplancore-all-functions.md"

# page order for ties: specific pages first, hub last
PAGE_ORDER = [
    "ourplancore-tools.md", "ourplancore-pages.md", "ourplancore-takeoffs.md", "ourplancore-excel.md",
    "ourplancore-pdf.md", "ourplancore-editing.md", "ourplancore-edit-takeoffs.md", "ourplancore-sheets-advanced.md",
    "ourplancore-snap-trace.md", "ourplancore-settings.md", "ourplancore-routing.md", "takeoff-naming.md",
    "ourplancore-buildings.md", "ourplancore-ai.md", "ourplancore-ai-console.md", "ourplancore-workspace.md",
    "ourplancore-3d.md", "ourplancore-3d-roof.md", "ourplancore-managers.md", "ourplancore-extras.md",
    "ourplancore-extras-other.md", "ourplancore-split-by-sheets.md", "job-creation-storage.md",
    "ourplancore-start.md", "ourplancore-shortcuts.md", "ourplancore-troubleshooting.md",
    "ourplancore-changelog.md", "ourplancore-ideas.md", "ourplanecore.md",
]


def norm(text: str) -> str:
    text = text.replace("…", "...").replace("—", "-").replace("–", "-")
    text = re.sub(r"\{[^}]*\}", " ", text)
    text = re.sub(r"\.\.\.$", "", text.strip())
    return re.sub(r"\s+", " ", text).strip().lower()


def alnum(text: str) -> str:
    return re.sub(r"[^a-z0-9а-яё]+", "", text.lower())


class Page:
    def __init__(self, path: Path):
        self.name = path.name
        self.text = path.read_text(encoding="utf-8")
        self.lower = self.text.lower()
        self.alnum = alnum(self.text)
        self.codes = [c.lower() for c in re.findall(r"`([^`\n]+)`", self.text)]
        try:
            self.rank = PAGE_ORDER.index(self.name)
        except ValueError:
            self.rank = len(PAGE_ORDER) - 1  # unknown new page: before the hub


def load_pages() -> list[Page]:
    names = {"ourplanecore.md", "job-creation-storage.md", "takeoff-naming.md"}
    names |= {p.name for p in DOCS.glob("ourplancore-*.md")}
    names.discard(GENERATED_PAGE)
    return [Page(DOCS / n) for n in sorted(names) if (DOCS / n).exists()]


def load_ignore(path: Path = IGNORE) -> list[tuple[str, str, str]]:
    rules = []
    if not path.exists():
        return rules
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        body, _, reason = line.partition("#")
        body = body.strip()
        kind, _, value = body.partition(":")
        if kind in ("id", "source", "group") and value:
            rules.append((kind, value.strip(), reason.strip()))
        elif kind == "*" or kind:
            rules.append(("title", (kind.strip(), norm(value)), reason.strip()))
    return rules


def ignored_reason(item: dict, rules) -> str:
    for kind, value, reason in rules:
        if kind == "id" and item.get("id") == value:
            return reason or "ignored"
        if kind == "source" and item["source"].startswith(value):
            return reason or "ignored"
        if kind == "group" and value.lower() in item.get("group", "").lower():
            return reason or "ignored"
        if kind == "title":
            surface, title = value
            if (surface == "*" or surface == item["surface"]) and norm(item["title"]) == title:
                return reason or "ignored"
    return ""


GENERIC_WORDS = {
    "all", "set", "open", "refresh", "clear", "reset", "apply", "size", "pos", "fit", "top", "iso", "front", "auto",
    "wall", "line", "area", "count", "joist", "show", "dark", "left", "right", "180", "level", "copy", "invert",
    "vertical", "horizontal", "name", "scale", "export", "save", "edit", "delete", "duplicate", "rename",
    "properties", "more", "setup", "load", "full", "manual", "sheet", "record", "find", "props", "jump", "crop",
    "reload", "folder", "json", "presets", "value", "excel", "pdf", "snap", "ortho", "box", "cut", "merge", "split",
    "break", "ends", "combine", "select", "pan", "ruler", "pitch", "similar", "beam", "open", "note", "style",
    "highlight", "close", "cancel", "ok", "import", "detach", "remove", "add", "new", "none", "custom", "legend",
    "layer", "preview", "run", "analyze", "prepare", "clean", "options", "roof base", "new item", "new folder",
}


def is_generic(title: str) -> bool:
    t = norm(title).rstrip(".")
    return t in GENERIC_WORDS or (len(alnum(t)) <= 3) or (" " not in t and len(t) <= 6)


def candidates(item: dict, palette_titles: dict[str, str]) -> list[tuple[str, bool]]:
    """(phrase, generic?) pairs to look for."""
    out = []
    seen = set()

    def add(text):
        t = norm(text).rstrip(".").strip()
        t = re.sub(r"\s*\(\.\.\.\)$", "", t)
        if len(t) >= 2 and t not in seen:
            seen.add(t)
            out.append((t, is_generic(t)))

    add(item["title"])
    # "Legend: Size" also as "Size"; XL "SQFT (SF)" also as "SQFT" and "SF"
    m = re.match(r"^(.*)\s\(([^()]+)\)$", item["title"])
    if m:
        add(m.group(1))
        if item["surface"] == "xl":
            add(m.group(2))
    if ": " in item["title"]:
        add(item["title"].split(": ", 1)[1])
    for a in item.get("aliases", []):
        add(a)
    for cid in [item.get("id")] + item.get("ids", []):
        if cid and cid in palette_titles:
            add(palette_titles[cid])
    return out


def phrase_regex(phrase: str) -> re.Pattern:
    return re.compile(r"(?<![a-z0-9а-яё])" + re.escape(phrase) + r"(?![a-z0-9а-яё])")


# ---------------------------------------------------------------- key gestures (++ctrl+alt+left++ notation)

KEY_TOKENS = {"esc": "esc", "escape": "esc", "del": "delete", "backspace": "backspace", "back": "backspace",
              "space": "space", "enter": "enter", "tab": "tab", "-": "minus", "+": "plus", "[": "bracket-left",
              "]": "bracket-right", "0": "0"}
# gestures that mean different things in different places: a page line must also name the function
AMBIGUOUS = {"esc", "enter", "delete", "tab", "f2", "backspace", "space", "ctrl+z", "ctrl+c", "ctrl+x", "ctrl+v",
             "ctrl+d", "ctrl+a", "ctrl+up", "ctrl+down", "up", "down", "shift", "ctrl", "alt", "ctrl+shift", "minus"}
STOP_WORDS = {"the", "with", "from", "into", "this", "that", "your", "only", "then", "when", "while", "after",
              "selected", "current", "active", "sheet", "page", "pages", "takeoff", "takeoffs", "item", "items",
              "object", "objects", "measurement", "measurements", "mode", "tool", "last", "point", "every",
              "toggle", "start", "stop", "create", "open", "show", "close", "drawing", "folder", "section",
              "tree", "trees", "exact", "name", "entry", "result", "results", "list", "lists", "default"}
# English verb of a title -> Russian stems that KB pages use for it
RU_STEMS = {
    "delete": ["удал"], "rename": ["переимен", "rename"], "copy": ["копир", "copy"], "paste": ["встав", "paste"],
    "cut": ["вырез", "cut"], "duplicate": ["дубл", "duplicate"], "move": ["перемест", "сдвиг", "move"],
    "restore": ["верн", "восстанов"], "undo": ["верн", "отмен", "откат", "undo"], "select": ["выдел", "выбр", "select"],
    "complete": ["заверш", "complete"], "cancel": ["отмен", "выйти", "выход", "cancel"], "collapse": ["сверн", "collapse"],
    "zoom": ["зум", "масштаб", "zoom"], "fit": ["впис", "целиком", "fit"], "save": ["сохран", "save"],
    "scale": ["масштаб", "scale"], "nudge": ["сдвиг", "сдвин"], "rotate": ["поворот", "поверн", "rotate"],
    "reset": ["сброс", "верн", "reset"], "clear": ["сброс", "снять", "очист", "clear"], "advance": ["следующ", "шаг"],
    "cycle": ["цикл", "перекл"], "hide": ["спрят", "скры", "hide"], "record": ["запис", "record"],
    "guide": ["guide"], "snap": ["snap", "привяз"], "ortho": ["ortho"], "box": ["бокс", "box"], "merge": ["merge"],
    "split": ["split"], "break": ["break"], "bookmark": ["закладк", "bookmark"], "palette": ["palette", "палитр"],
    "fine": ["мелк", "точн", "shift"], "overlay": ["overlay", "наложен"], "ridge": ["ridge"], "hip": ["hip"],
    "valley": ["valley"], "eave": ["eave"], "rake": ["rake"], "pitch": ["pitch"], "trace": ["trace", "трасс"],
    "remove": ["убр", "удал", "remove"], "range": ["диапазон", "range"], "marquee": ["рамк", "marquee"],
    "section": ["секци", "section"], "canvas": ["лист", "canvas"], "all": ["всё", "все", "all"],
    "import": ["import", "импорт"], "recent": ["недавн", "recent"], "new": ["нов", "new"], "location": ["путь", "папк", "location"],
    "shortcut": ["клавиш", "shortcut"], "help": ["справк", "шпаргалк", "help"], "command": ["команд", "command"],
}


def split_keys(part: str) -> list[str]:
    if part.endswith("++"):
        keys = part[:-2].split("+") + ["+"]
    elif part.endswith("+-"):
        keys = part[:-2].split("+") + ["-"]
    else:
        keys = part.split("+") if part != "+" else ["+"]
    return [KEY_TOKENS.get(k.lower(), k.lower()) for k in keys if k != ""]


def gesture_variants(shortcut: str) -> list[tuple[str, ...]]:
    """Each variant is a tuple of substrings that must all be on one page line.

    "Ctrl+Alt+Right" gives ("++ctrl+alt+right++",), ("++ctrl+alt+", "++right++") for the
    abbreviated "++ctrl+alt+left++ / ++right++" style, and a raw "`ctrl+alt+right`" form;
    "Ctrl+Alt+Shift+Left" also accepts "++ctrl+alt+left++" together with "++shift++".
    """
    variants: list[tuple[str, ...]] = []
    for seq in shortcut.split(" / "):
        seq = seq.strip()
        if not seq or seq.lower() in ("+ shift", "shift / ctrl+click", "shift+click", "ctrl+click", "ctrl+shift+click",
                                      "alt+drag", "ctrl+alt+drag", "ctrl+alt+arrows"):
            continue
        parts = [p.strip() for p in seq.split(",")]  # "B, K" sequence: both keys on the line
        full = tuple("++" + "+".join(split_keys(p)) + "++" for p in parts)
        variants.append(full)
        arrow = tuple(t.replace("+left++", "+arrow-left++").replace("+right++", "+arrow-right++")
                      .replace("+up++", "+arrow-up++").replace("+down++", "+arrow-down++") for t in full)
        if arrow != full:
            variants.append(arrow)
        if len(parts) == 1:
            keys = split_keys(parts[0])
            raw = parts[0].lower()
            variants.append(("`" + raw + "`",))
            if len(keys) >= 2:
                mods, key = keys[:-1], keys[-1]
                variants.append(("++" + "+".join(mods) + "+", "++" + key + "++"))
                variants.append(("`" + "+".join(mods) + "+", "`" + key + "`"))
                if "shift" in mods and len(mods) > 1:
                    rest = [m for m in mods if m != "shift"]
                    variants.append(("++" + "+".join(rest + [key]) + "++", "++shift++"))
                    variants.append(("++" + "+".join(rest) + "+", "++" + key + "++", "++shift++"))
    return variants


def is_ambiguous(variant: tuple[str, ...]) -> bool:
    inner = variant[0].strip("+`")
    return inner in AMBIGUOUS or (len(inner) == 1)


def title_keywords(item: dict) -> list[str]:
    words = []
    for text in [item["title"]] + item.get("aliases", []):
        for w in re.findall(r"[a-z]{3,}", text.lower()):
            if w not in STOP_WORDS:
                words.append(w)
                words += RU_STEMS.get(w, [])
    group = item.get("group", "").lower()
    for ctx, stems in (("roof", ["roof", "крыш"]), ("overlay", ["overlay", "наложен"]), ("trace", ["trace", "трасс"]),
                       ("pages", ["pages", "лист"]), ("takeoffs", ["takeoffs", "позици"]), ("bookmark", ["bookmark", "закладк"]),
                       ("inbox", ["inbox"])):
        if ctx in group:
            words += stems
    return list(dict.fromkeys(words))


def gesture_hits(page: Page, item: dict) -> int:
    shortcut = item.get("shortcut", "")
    if not shortcut:
        return 0
    keywords = title_keywords(item)
    hit_lines: set[int] = set()
    for variant in gesture_variants(shortcut):
        need_keyword = is_ambiguous(variant) or len(variant) > 1
        for no, line in enumerate(page.lower.splitlines()):
            if all(t in line for t in variant):
                if need_keyword and not any(k in line for k in keywords):
                    continue
                hit_lines.add(no)
    return len(hit_lines)


def score_page(page: Page, cands, item: dict | None = None) -> tuple[int, str]:
    """(score, how) for one page."""
    score = 0
    how = ""
    if item is not None:
        g = gesture_hits(page, item)
        if g:
            score += 2 * g
            how = "gesture"
    for phrase, generic in cands:
        code_hits = sum(1 for c in page.codes if c == phrase or (len(phrase) >= 4 and phrase in c))
        if code_hits:
            score += 3 * code_hits
            how = how or "backtick"
            continue
        if generic:
            continue
        hits = len(phrase_regex(phrase).findall(page.lower))
        if hits:
            score += hits
            how = how or "phrase"
            continue
        a = alnum(phrase)
        if len(a) >= 6 and a in page.alnum:
            score += 1
            how = how or "loose"
    return score, how


def item_uids(items: list[dict]) -> list[str]:
    """Unique id per inventory row: the source, plus #n when several rows share one source line."""
    seen: dict[str, int] = {}
    uids = []
    for it in items:
        n = seen.get(it["source"], 0) + 1
        seen[it["source"]] = n
        uids.append(it["source"] if n == 1 else f"{it['source']}#{n}")
    return uids


def compute(inv: dict, pages: list[Page], rules) -> dict:
    palette_titles = {it["id"]: it["title"] for it in inv["items"] if it["surface"] == "palette"}
    result = {"items": {}, "described": 0, "missing": 0, "ignored": 0, "pages": [p.name for p in pages]}
    uids = item_uids(inv["items"])
    for uid, it in zip(uids, inv["items"]):
        reason = ignored_reason(it, rules)
        entry = {"status": "", "page": "", "how": "", "reason": reason}
        if reason:
            entry["status"] = "ignored"
            result["ignored"] += 1
        cands = candidates(it, palette_titles)
        best = (0, "", None)
        preferred = suggest_page(it)
        for page in pages:
            score, how = score_page(page, cands, it)
            # The page the function belongs to by topic wins when it mentions the
            # function at all; otherwise the page that mentions it most.
            if score > 0 and page.name == preferred:
                best = (float("inf"), how, page)
                break
            if score > best[0] or (score == best[0] and score > 0 and page.rank < best[2].rank):
                best = (score, how, page)
        if best[0] > 0:
            entry["page"] = best[2].name
            entry["how"] = best[1]
            if not reason:
                entry["status"] = "described"
                result["described"] += 1
        elif not reason:
            entry["status"] = "missing"
            result["missing"] += 1
        result["items"][uid] = entry
    return result


# ---------------------------------------------------------------- suggestions for missing items

SUGGEST_RULES = [
    # (regex on "surface|group|title", page)
    (r"calculator|bookmark|template|planswift|pdf takeoffs|detach|tile m2|monitor 2", "ourplancore-extras-other.md"),
    (r"терминал|codex|claude|terminal|attach", "ourplancore-ai-console.md"),
    (r"3d.*(roof|rafter|edge|eave|rake|pitch|ridge)|roof base|roof|rafter", "ourplancore-3d-roof.md"),
    (r"3d|massing|wall from|viewer", "ourplancore-3d.md"),
    (r"\bai\b|inbox|marker|observation|openai|gpt|learned|learning|crop hint|ai fill|metadata fallback", "ourplancore-ai.md"),
    (r"excel|\bxl\b|macro|legend xl|templatecom|sqft \(|walls \(wl|framing \(fr", "ourplancore-excel.md"),
    (r"settings", "ourplancore-settings.md"),
    (r"export pdf|export sheet|pdf export|output preview|print", "ourplancore-pdf.md"),
    (r"overlay|наложен|легенд|legend|crop|кроп|mask|hide area|annotation|разметк|markup|highlight|cloud|arrow|draw box|note", "ourplancore-sheets-advanced.md"),
    (r"layer|trace|snap|ortho|box mode", "ourplancore-snap-trace.md"),
    (r"merge|split|break|combine|points|ends|line grid|transform|flip|mirror|rotate selected|scale selected|undo|paste|copy|cut|clipboard|delete|duplicate|rename", "ourplancore-editing.md"),
    (r"joist|extra joists|beam|opening|count|line tool|area tool|ruler|pitch|scale tool|select tool|pan|record|tool|нижняя полоса", "ourplancore-tools.md"),
    (r"pages|листа|папки в pages|лента page|sheet manager|page|sheet|blank|rotate|invert|origin|name|scale|suffix|arch|struct|sort", "ourplancore-pages.md"),
    (r"takeoff|позиции|секции|папки в takeoffs|estimat|unit price|active|target|folder|item|tree", "ourplancore-takeoffs.md"),
    (r"materials|report builder|template|manager", "ourplancore-managers.md"),
    (r"job|project|open / import|save|recent|recover|workspace|lease|storage|planswift|import|sample", "job-creation-storage.md"),
    (r"f1|shortcut|клавиш|defaults", "ourplancore-shortcuts.md"),
    (r"bookmark|zoom|fit|theme|dark|display|viewport|label|background|calculator|detach|tile|tab|strip|полоса|панель|workspace|inbox", "ourplancore-workspace.md"),
]


def suggest_page(item: dict) -> str:
    text = f"{item['surface']}|{item.get('group', '')}|{item['title']}".lower()
    for pattern, page in SUGGEST_RULES:
        if re.search(pattern, text):
            return page
    return "ourplancore-extras.md"


def render_report(inv: dict, res: dict, rules) -> str:
    items = inv["items"]
    total = len(items)
    lines = ["# Покрытие функций OurPlanCore страницами KB", ""]
    lines.append(f"Всего записей инвентаря: {total}. Описано: {res['described']}. "
                 f"Не найдено: {res['missing']}. Исключено (tools/opc_coverage_ignore.txt): {res['ignored']}.")
    lines.append(f"Страницы: {', '.join(res['pages'])}.")
    lines.append("")
    lines.append("## По поверхностям")
    lines.append("")
    lines.append("| Поверхность | Всего | Описано | Не найдено | Исключено |")
    lines.append("| --- | --- | --- | --- | --- |")
    per: dict[str, list[int]] = {}
    uids = item_uids(items)
    for uid, it in zip(uids, items):
        st = res["items"][uid]["status"]
        row = per.setdefault(it["surface"], [0, 0, 0, 0])
        row[0] += 1
        row[{"described": 1, "missing": 2, "ignored": 3}[st]] += 1
    for s, row in per.items():
        lines.append(f"| {s} | {row[0]} | {row[1]} | {row[2]} | {row[3]} |")
    lines.append("")
    missing = [it for uid, it in zip(uids, items) if res["items"][uid]["status"] == "missing"]
    by_page: dict[str, list[dict]] = {}
    for it in missing:
        by_page.setdefault(suggest_page(it), []).append(it)
    lines.append(f"## Не описано: {len(missing)} записей, по страницам, куда они ложатся")
    lines.append("")
    for page in sorted(by_page, key=lambda p: -len(by_page[p])):
        rows = by_page[page]
        lines.append(f"### {page} ({len(rows)})")
        lines.append("")
        lines.append("| Поверхность | Где | Функция | Клавиша | Описание из кода | Источник |")
        lines.append("| --- | --- | --- | --- | --- | --- |")
        for it in rows:
            desc = it.get("description", "").replace("|", "/")
            if len(desc) > 110:
                desc = desc[:107] + "..."
            lines.append(f"| {it['surface']} | {it.get('group', '').replace('|', '/')} | `{it['title'].replace('|', '/')}` | "
                         f"{it.get('shortcut', '')} | {desc} | {it['source']} |")
        lines.append("")
    return "\n".join(lines) + "\n"


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--inventory", default=str(INVENTORY))
    ap.add_argument("--report", help="write the Markdown report here")
    ap.add_argument("--json", help="write per-item results here")
    ap.add_argument("--quiet", action="store_true", help="print only the totals")
    args = ap.parse_args()
    inv = json.loads(Path(args.inventory).read_text(encoding="utf-8"))
    rules = load_ignore()
    res = compute(inv, load_pages(), rules)
    report = render_report(inv, res, rules)
    if args.report:
        Path(args.report).write_text(report, encoding="utf-8", newline="\n")
    if args.json:
        Path(args.json).write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    if args.quiet:
        print(f"total {len(inv['items'])}, described {res['described']}, missing {res['missing']}, ignored {res['ignored']}")
    else:
        print(report)
    return 1 if res["missing"] else 0


if __name__ == "__main__":
    sys.exit(main())
