"""Static inventory of every user-facing function of OurPlanCore.

Reads the program sources (no build, no run) and writes tools/opc_inventory.json.
With --page it also renders docs/reference/ourplancore-all-functions.md.

Usage (from the KB repo root, standard library only):
  python tools/opc_inventory.py                       # JSON only
  python tools/opc_inventory.py --page                # JSON + generated page
  python tools/opc_inventory.py --src E:\\path\\to\\ourplanecore

Surfaces collected (field "surface"):
  palette       Command Palette entries (MainWindow.CommandPalette.cs)
  f1            F1 shortcut guide (Models/KeyboardShortcutCatalog.cs)
  defaults      default key bindings whose id is not in the palette
                (Models/KeyboardShortcutDefaults.cs); palette ids get "shortcut"
  ribbon        top ribbon tabs Main / Page / Annotation / Viewport / Display (MainWindow.xaml)
  toolstrip     bottom tool strip, two rows (MainWindow.xaml)
  xl            the XL Excel strip right of the viewport (MainWindow.xaml)
  strip         left and right icon strips (MainWindow.SideStrips.cs, default sets)
  workspace     buttons, toggles and menus of the workspace tabs and side panels
                (MainWindow.xaml, Controls/*.xaml)
  context-menu  menus built in code (MakeMenuItem / MakeSubmenu / new MenuItem and
                helpers that forward a header parameter) plus XAML button menus
  panel         buttons built in code inside MainWindow.*.cs panels and windows
  settings      Settings categories and section headers (MainWindow.SettingsManager*.cs)
  dialog        dialog windows: title plus main buttons (Dialogs/*, code-built windows)

Each item: surface, group, title, shortcut, description, source (file:line),
optional id (palette command id), aliases (other labels of the same function),
dynamic (label is built at run time), key (stable key for the RU text file).

Not extractable statically (documented here on purpose): labels computed from
job data (legend group names, sheet targets, attach-window list), items whose
text is a loop variable over presets, and anything created by the viewport
control itself without a label.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import xml.parsers.expat
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SRC = Path(r"E:\---\OurPlanCore\ourplanecore")
JSON_OUT = ROOT / "tools" / "opc_inventory.json"
PAGE_OUT = ROOT / "docs" / "reference" / "ourplancore-all-functions.md"
RU_TEXT = ROOT / "tools" / "opc_descriptions_ru.json"

# ---------------------------------------------------------------- helpers


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def line_of(text: str, pos: int) -> int:
    return text.count("\n", 0, pos) + 1


def rel(path: Path, src: Path) -> str:
    try:
        return path.relative_to(src).as_posix()
    except ValueError:
        return path.as_posix()


def norm_title(text: str) -> str:
    text = text.replace("\u2026", "...").replace("\u2014", "-").replace("\u2013", "-")
    text = re.sub(r"\{[^}]*\}", " ", text)
    text = re.sub(r"\.\.\.$", "", text.strip())
    text = re.sub(r"\s+", " ", text).strip().lower()
    return text


def unquote(lit: str) -> str:
    """C# string literal (plain, verbatim or interpolated) to text."""
    lit = lit.strip()
    while lit[:1] in ("$", "@"):
        lit = lit[1:]
    if len(lit) >= 2 and lit[0] == '"' and lit[-1] == '"':
        lit = lit[1:-1]
    lit = lit.replace('\\"', '"').replace("\\n", " ").replace("\\\\", "\\")
    return lit


def balanced_span(text: str, open_pos: int) -> int:
    """Index just after the bracket that closes text[open_pos]."""
    pairs = {"(": ")", "{": "}", "[": "]"}
    depth = 0
    i = open_pos
    n = len(text)
    while i < n:
        ch = text[i]
        if ch == '"':
            j = i + 1
            while j < n:
                if text[j] == "\\":
                    j += 2
                    continue
                if text[j] == '"':
                    break
                j += 1
            i = j + 1
            continue
        if ch == "'" and i + 2 < n and text[i + 2] == "'":
            i += 3
            continue
        if ch == "/" and i + 1 < n and text[i + 1] == "/":
            j = text.find("\n", i)
            i = n if j < 0 else j
            continue
        if ch in pairs:
            depth += 1
        elif ch in ")}]":
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1
    return n


def split_args(inner: str) -> list[str]:
    """Split a C# argument list at top-level commas."""
    args, depth, cur, i, n = [], 0, [], 0, len(inner)
    while i < n:
        ch = inner[i]
        if ch == '"':
            j = i + 1
            while j < n:
                if inner[j] == "\\":
                    j += 2
                    continue
                if inner[j] == '"':
                    break
                j += 1
            cur.append(inner[i:j + 1])
            i = j + 1
            continue
        if ch in "([{":
            depth += 1
        elif ch in ")]}":
            depth -= 1
        if ch == "," and depth == 0:
            args.append("".join(cur).strip())
            cur = []
        else:
            cur.append(ch)
        i += 1
    if "".join(cur).strip():
        args.append("".join(cur).strip())
    return args


STRING_LIT = re.compile(r'\$?@?"(?:[^"\\]|\\.)*"')
IDENT = re.compile(r"^[A-Za-z_]\w*$")
METHOD_CALL = re.compile(r"^([A-Za-z_]\w*)\((.*)\)$", re.S)

# name -> expression text of simple string-returning methods, filled by index_string_methods
STRING_METHODS: dict[str, str] = {}
# "Type.Method(" -> list of literals the method can return (enum title switches)
EXPANDERS: dict[str, list[str]] = {}


def index_string_methods(src: Path) -> None:
    pat = re.compile(
        r"(?:private|internal|public|protected)\s+(?:static\s+)?string\??\s+(\w+)\s*\([^)]*\)\s*=>\s*([^;]+);", re.S)
    for path in list(src.glob("MainWindow.*.cs")) + list((src / "Controls").glob("*.cs")):
        text = read(path)
        for m in pat.finditer(text):
            STRING_METHODS.setdefault(m.group(1), m.group(2).strip())
    cds = src / "Models" / "CountDisplaySymbol.cs"
    if cds.exists():
        EXPANDERS["CountDisplaySymbol.Title("] = re.findall(r'=>\s*"([^"]+)"', read(cds))


def fill_holes(text: str, scope: str, depth: int) -> str:
    """Replace {expr} holes of an interpolated string by resolved text or '...'."""
    def repl(m):
        inner = m.group(1).split(":")[0].strip()
        if depth < 3:
            title, _, _ = resolve_expr(inner, scope, depth + 1)
            if not title.startswith("<"):
                return title
        return "{...}"
    return re.sub(r"\{([^{}]*)\}", repl, text)


def resolve_expr(expr: str, scope: str, depth: int = 0) -> tuple[str, list[str], bool]:
    """Turn a C# header expression into (title, aliases, dynamic)."""
    expr = expr.strip().rstrip(",")
    for key, options in EXPANDERS.items():
        if key in expr:
            return "Symbol: " + ", ".join(options), list(options), True
    lits = STRING_LIT.findall(expr)
    if lits:
        texts = []
        dyn = False
        for lit in lits:
            t = unquote(lit)
            if lit.startswith("$") or lit.startswith("@$"):
                dyn = True
                t = fill_holes(t, scope, depth)
            texts.append(re.sub(r"\s+", " ", t).strip())
        if len(lits) == 1 and expr == lits[0]:
            return texts[0], [], dyn
        if "?" in expr and ":" in expr and len(texts) >= 2:
            # ternary chain: the last literal is the default wording
            return texts[-1], [t for t in texts[:-1] if t], True
        return " ".join(t for t in texts if t).strip(), [], True
    if IDENT.match(expr) and scope and depth < 3:
        pat = re.compile(r"(?:string\??|var)\s+" + re.escape(expr) + r"\s*=\s*([^;]+);")
        hit = pat.search(scope)
        if hit:
            title, aliases, _ = resolve_expr(hit.group(1), scope, depth + 1)
            return title, aliases, True
    mc = METHOD_CALL.match(expr)
    if mc and mc.group(1) in STRING_METHODS and depth < 3:
        title, aliases, _ = resolve_expr(STRING_METHODS[mc.group(1)], "", depth + 1)
        return title, aliases, True
    return "<" + expr + ">", [], True


def humanize_name(name: str) -> str:
    name = re.sub(r"^(Btn|Chk|Cmb|Combo|Txt|Tgl|Rb|Lbl|Sld)", "", name)
    name = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", name)
    return name.strip()


SHORTCUT_IN_TEXT = re.compile(
    r"\(((?:Ctrl|Shift|Alt)\+[^()]{1,16}|F\d{1,2}|[A-Z]|Space|Esc|Delete|Enter|Tab)(?:[,;][^()]*)?\)")


def shortcut_from_text(text: str) -> str:
    if not text:
        return ""
    m = SHORTCUT_IN_TEXT.search(text)
    return m.group(1).strip() if m else ""


SIGNATURE = re.compile(
    r"^[ \t]*(?:\[[^\]]*\][ \t]*)*(?:private|public|internal|protected)\b[^;{}=()\n]*?\s(\w+)\s*\(([^;]*?)\)\s*(?:where[^{]*)?(?:=>|\{)",
    re.M | re.S)


def method_index(text: str) -> list[tuple[int, str, list[str]]]:
    """(start_pos, name, parameter names) of every method in a C# file."""
    out = []
    for m in SIGNATURE.finditer(text):
        params = []
        for p in split_args(m.group(2)):
            p = p.split("=")[0].strip()
            if p:
                params.append(p.split()[-1])
        out.append((m.start(), m.group(1), params))
    return out


def enclosing_method(methods, pos: int) -> tuple[str, int, list[str]]:
    name, start, params = "", 0, []
    for mpos, mname, mparams in methods:
        if mpos <= pos:
            name, start, params = mname, mpos, mparams
        else:
            break
    return name, start, params


def method_body(text: str, methods, pos: int) -> str:
    _, start, _ = enclosing_method(methods, pos)
    nxt = len(text)
    for mpos, _, _ in methods:
        if mpos > start:
            nxt = mpos
            break
    return text[start:nxt]


# ---------------------------------------------------------------- palette


def scan_palette(src: Path) -> tuple[list[dict], dict[str, str], dict[str, dict]]:
    path = src / "MainWindow.CommandPalette.cs"
    text = read(path)
    items: list[dict] = []
    handler_to_id: dict[str, str] = {}
    by_id: dict[str, dict] = {}
    for m in re.finditer(r"\n[ \t]+Add\(", text):
        start = m.end() - 1
        end = balanced_span(text, start)
        args = split_args(text[start + 1:end - 1])
        if len(args) < 5:
            continue
        cid = unquote(args[0])
        sc = args[3].strip()
        shortcut = unquote(sc[len("Shortcut("):-1]).upper() if sc.startswith("Shortcut(") else unquote(sc)
        item = {
            "surface": "palette",
            "group": unquote(args[2]),
            "title": unquote(args[1]),
            "shortcut": shortcut,
            "description": unquote(args[4]),
            "source": f"{rel(path, src)}:{line_of(text, start)}",
            "id": cid,
        }
        items.append(item)
        by_id[cid] = item
    counts: dict[str, set] = {}
    for m in re.finditer(r'case "([\w.]+)":\s*(\w+)\(', text):
        counts.setdefault(m.group(2), set()).add(m.group(1))
    for handler, ids in counts.items():
        if len(ids) == 1 and handler not in {"SetTool", "SelectWorkspaceTab", "SelectRightWorkspaceTab"}:
            handler_to_id[handler] = next(iter(ids))
    strips = read(src / "MainWindow.SideStrips.cs")
    for m in re.finditer(r'case "([\w.]+)":\s*(\w+)\(', strips):
        handler_to_id.setdefault(m.group(2), m.group(1))
    return items, handler_to_id, by_id


# ---------------------------------------------------------------- F1 and defaults


def scan_f1(src: Path) -> list[dict]:
    path = src / "Models" / "KeyboardShortcutCatalog.cs"
    text = read(path)
    items = []
    for m in re.finditer(r"\bSection\(", text):
        if text[max(0, m.start() - 40):m.start()].rstrip().endswith("KeyboardShortcutHelpSection"):
            continue
        end = balanced_span(text, m.end() - 1)
        body = text[m.end():end - 1]
        args = split_args(body)
        if not args:
            continue
        section = unquote(args[0])
        for im in re.finditer(r"\bItem\(", body):
            iend = balanced_span(body, im.end() - 1)
            iargs = split_args(body[im.end():iend - 1])
            if len(iargs) < 2:
                continue
            items.append({
                "surface": "f1",
                "group": section,
                "title": unquote(iargs[1]),
                "shortcut": unquote(iargs[0]),
                "description": unquote(iargs[2]) if len(iargs) > 2 else "",
                "source": f"{rel(path, src)}:{line_of(text, m.end() + im.start())}",
            })
    return items


KEY_DISPLAY = {
    "OemPlus": "+", "Add": "+", "OemMinus": "-", "Subtract": "-", "D0": "0", "NumPad0": "0",
    "OemOpenBrackets": "[", "OemCloseBrackets": "]", "Back": "Backspace", "Escape": "Esc",
}

DEFAULT_ID_TITLES = {
    "help.shortcuts": "Show / close the shortcut guide",
    "help.commands": "Open Command Palette",
    "view.collapseTrees": "Collapse Pages and Takeoffs trees",
    "tool.toggleBox": "Toggle Box mode",
    "edit.undo": "Undo viewport action / last point",
    "edit.selectAll": "Select all objects on active sheet",
    "edit.delete": "Delete the selected object",
    "edit.rename": "Rename the selected object's takeoff",
    "drawing.complete": "Complete the current drawing",
    "drawing.cancel": "Cancel the active action",
    "drawing.cycleTrace": "Cycle edge snap or trace mode / candidate",
    "drawing.advanceTrace": "Advance the trace workflow",
    "pages.copy": "Pages tree: copy", "pages.cut": "Pages tree: cut", "pages.paste": "Pages tree: paste",
    "pages.duplicate": "Pages tree: duplicate with the exact name",
    "pages.moveUp": "Pages tree: move up", "pages.moveDown": "Pages tree: move down",
    "pages.undoDelete": "Pages tree: restore the last deletion",
    "pages.rename": "Pages tree: rename page or folder", "pages.delete": "Pages tree: delete selected",
    "pages.clearSelection": "Pages tree: clear the selection",
    "takeoffs.copy": "Takeoffs tree: copy", "takeoffs.cut": "Takeoffs tree: cut", "takeoffs.paste": "Takeoffs tree: paste",
    "takeoffs.duplicate": "Takeoffs tree: duplicate with the exact name",
    "takeoffs.moveUp": "Takeoffs tree: move up", "takeoffs.moveDown": "Takeoffs tree: move down",
    "takeoffs.undoDelete": "Takeoffs tree: restore the last deletion",
    "takeoffs.rename": "Takeoffs tree: rename item, folder, or section",
    "takeoffs.delete": "Takeoffs tree: delete selected node(s)",
    "takeoffs.showSections": "Select section measurements on canvas",
    "bookmarks.open": "Open the selected bookmark", "bookmarks.delete": "Delete the selected bookmark",
    "inbox.open": "Open the selected AI entry",
    "roof.ridge": "Ridge guide", "roof.hip": "Hip guide", "roof.valley": "Valley guide",
    "roof.eave": "Eave guide", "roof.rake": "Rake guide", "roof.pitch": "Pitch guide",
    "roof.cancel": "Cancel guide / leave Roof mode", "roof.undo": "Remove the last guide point",
    "overlay.left": "Nudge the overlay left", "overlay.right": "Nudge the overlay right",
    "overlay.up": "Nudge the overlay up", "overlay.down": "Nudge the overlay down",
    "overlay.scaleUp": "Scale the overlay up", "overlay.scaleDown": "Scale the overlay down",
    "overlay.rotateLeft": "Rotate the overlay left", "overlay.rotateRight": "Rotate the overlay right",
    "overlay.reset": "Reset overlay transform",
    "overlay.fineLeft": "Fine nudge the overlay left", "overlay.fineRight": "Fine nudge the overlay right",
    "overlay.fineUp": "Fine nudge the overlay up", "overlay.fineDown": "Fine nudge the overlay down",
    "overlay.fineScaleUp": "Fine scale the overlay up", "overlay.fineScaleDown": "Fine scale the overlay down",
    "overlay.fineRotateLeft": "Fine rotate the overlay left", "overlay.fineRotateRight": "Fine rotate the overlay right",
    "overlay.fineReset": "Reset overlay transform (fine)",
}


F1_SECTION_CONTEXT = {
    "GLOBAL": ("Workspace", "Viewport"), "DRAWING TOOLS": ("Viewport", "Workspace"),
    "VIEWPORT & DRAWING": ("Viewport", "Workspace"), "PAGES TREE": ("Pages",), "TAKEOFFS TREE": ("Takeoffs",),
    "BOOKMARKS & AI INBOX": ("Bookmarks", "Inbox"), "SHEET OVERLAY": ("Overlay",), "3D ROOF GUIDE MODE": ("Roof",),
    "LAYER TRACE": ("Viewport",),
}


def gesture_key(text: str) -> str:
    t = text.strip().lower().replace("escape", "esc").replace("back", "backspace").replace("backspacespace", "backspace")
    return re.sub(r"\s+", "", t)


def link_f1_to_ids(f1: list[dict], src: Path, palette_by_id: dict[str, dict], defaults: list[dict]) -> None:
    """Give F1 rows the command id(s) that own the same gesture in the same context."""
    text = read(src / "Models" / "KeyboardShortcutDefaults.cs")
    by_ctx_key: dict[tuple[str, str], list[str]] = {}
    for m in re.finditer(r'\["([\w.]+)"\]\s*=\s*\[([^\]]*)\]', text):
        cid = m.group(1)
        ctx = ""
        cm = re.search(r'"' + re.escape(cid) + r'"[^\n]*?=> KeyboardCommandContext\.(\w+)', text)
        if cm:
            ctx = cm.group(1)
        else:
            head = cid.split(".")[0]
            ctx = {"roof": "Roof", "overlay": "Overlay", "pages": "Pages", "takeoffs": "Takeoffs", "bookmarks": "Bookmarks",
                   "inbox": "Inbox", "tool": "Viewport", "drawing": "Viewport"}.get(head, "Workspace")
            if cid in ("view.fit", "view.zoomIn", "view.zoomOut", "edit.copyMeasurements", "edit.pasteMeasurements"):
                ctx = "Viewport"
        for k in split_args(m.group(2)):
            by_ctx_key.setdefault((ctx, gesture_key(key_display(unquote(k)))), []).append(cid)
    titles = {cid: it["title"] for cid, it in palette_by_id.items()}
    titles.update({it["id"]: it["title"] for it in defaults})
    for row in f1:
        ctxs = F1_SECTION_CONTEXT.get(row["group"], ())
        gestures = [row["shortcut"]]
        if " / " in row["shortcut"] and not row["shortcut"].startswith("Ctrl+Alt"):
            parts = row["shortcut"].split(" / ")
            prefix = parts[0].rsplit("+", 1)[0] + "+" if "+" in parts[0] else ""
            gestures = [parts[0]]
            for p in parts[1:]:
                gestures += [p] if "+" in p else [prefix + p, p]
        ids: list[str] = []
        for g in gestures:
            for ctx in ctxs:
                for cid in by_ctx_key.get((ctx, gesture_key(g)), []):
                    if cid not in ids:
                        ids.append(cid)
        if len(ids) == 1:
            row["id"] = ids[0]
        elif ids:
            row["ids"] = ids
        alias = [titles[c] for c in ids if c in titles and titles[c] != row["title"]]
        if alias:
            row["aliases"] = alias


def key_display(binding: str) -> str:
    return "+".join(KEY_DISPLAY.get(p, p) for p in binding.split("+"))


def scan_defaults(src: Path, palette_by_id: dict[str, dict]) -> list[dict]:
    path = src / "Models" / "KeyboardShortcutDefaults.cs"
    text = read(path)
    items = []
    for m in re.finditer(r'\["([\w.]+)"\]\s*=\s*\[([^\]]*)\]', text):
        cid = m.group(1)
        keys = [unquote(k) for k in split_args(m.group(2))]
        shown = []
        for k in keys:
            d = key_display(k)
            if d not in shown:
                shown.append(d)
        shortcut = " / ".join(shown)
        if cid in palette_by_id:
            if not palette_by_id[cid].get("shortcut"):
                palette_by_id[cid]["shortcut"] = shortcut
            continue
        cm = re.search(r'"' + re.escape(cid) + r'"[^\n]*?=> KeyboardCommandContext\.(\w+)', text)
        if cm:
            context = cm.group(1)
        else:
            head = cid.split(".")[0]
            context = {"roof": "Roof", "overlay": "Overlay", "pages": "Pages", "takeoffs": "Takeoffs",
                       "bookmarks": "Bookmarks", "inbox": "Inbox", "tool": "Viewport", "drawing": "Viewport",
                       "edit": "Viewport"}.get(head, "Workspace")
        items.append({
            "surface": "defaults",
            "group": context,
            "title": DEFAULT_ID_TITLES.get(cid, humanize_name(cid.split(".")[-1])),
            "shortcut": shortcut,
            "description": "Default key binding; editable in Settings > Keyboard Shortcuts.",
            "source": f"{rel(path, src)}:{line_of(text, m.start())}",
            "id": cid,
            "keys": keys,
        })
    return items


# ---------------------------------------------------------------- XAML


class XNode:
    __slots__ = ("tag", "attrs", "children", "parent", "line", "text")

    def __init__(self, tag, attrs, parent, line):
        self.tag, self.attrs, self.parent, self.line = tag, attrs, parent, line
        self.children: list[XNode] = []
        self.text = ""

    def ancestors(self):
        n = self.parent
        while n is not None:
            yield n
            n = n.parent

    def walk(self):
        yield self
        for c in self.children:
            yield from c.walk()

    def name(self):
        return self.attrs.get("Name", "")

    def style(self):
        return self.attrs.get("Style", "")


def parse_xaml(path: Path) -> XNode:
    parser = xml.parsers.expat.ParserCreate(namespace_separator="}")
    root: list[XNode] = []
    stack: list[XNode] = []

    def start(name, attrs):
        tag = name.split("}")[-1]
        a = {k.split("}")[-1]: v for k, v in attrs.items()}
        node = XNode(tag, a, stack[-1] if stack else None, parser.CurrentLineNumber)
        if stack:
            stack[-1].children.append(node)
        else:
            root.append(node)
        stack.append(node)

    def end(name):
        stack.pop()

    def chars(data):
        if stack and data.strip():
            stack[-1].text += data

    parser.StartElementHandler = start
    parser.EndElementHandler = end
    parser.CharacterDataHandler = chars
    parser.Parse(read(path).encode("utf-8"), True)
    return root[0]


CONTROL_TAGS = {"Button", "ToggleButton", "RadioButton", "CheckBox", "MenuItem", "ComboBox", "Slider"}
SKIP_UNDER = {"Style", "ControlTemplate", "DataTemplate", "Setter", "Trigger", "DataTrigger"}

HOST_LABELS = {
    "PagesPanel": "панель Pages", "PagesQuickBar": "панель Pages, быстрая строка",
    "TakeoffsPanel": "панель Takeoffs", "ActiveTakeoffTargetBar": "панель Takeoffs, строка активной позиции",
    "TakeoffsTreeHost": "панель Takeoffs, дерево", "InboxPanel": "AI Inbox", "ViewportHost": "вьюпорт",
    "NoJobOverlay": "стартовая карточка (проект не открыт)",
    "PageTabs": "вкладки листов", "BookmarksDockPanel": "панель Bookmarks", "TemplatesDockPanel": "панель Templates",
    "ViewportLayerTraceBar": "строка Layer Trace", "ExcelMacroExportPanel": "полоса XL", "LayersPanel": "PDF Layers",
    "TerminalPanelHost": "терминал", "QuickCalcHost": "Quick Calculator", "ExcelFramingLegendHost": "легенда XL",
    "MainStatusBar": "строка статуса", "ThreeDViewerViewportHost": "3D viewer",
}

CONTROL_FILE_LABELS = {
    "QuickCalcPanel.xaml": "Quick Calculator",
    "TerminalPanel.xaml": "панель терминала Codex / Claude",
    "SheetOverlayPropertiesPanel.xaml": "панель Pages, вкладка Overlay",
    "ExcelFramingLegendPanel.xaml": "легенда XL (кнопка LG)",
    "LiveInputRibbonSettings.xaml": "лента Viewport, live input",
    "KeyboardShortcutsOverlay.xaml": "шпаргалка F1",
    "JobPickerDialog.xaml": "окно Open Project",
    "JobLeaseConflictDialog.xaml": "окно Job Is Already Open",
}

XL_TITLES = {"LG": "Legend", "ALL": "ALL", "FR": "Framing"}
TOOL_TAG_LABELS: dict[str, str] = {}  # "drawhighlight" -> "Highlighter", from AddAnnotationToolItem calls


def index_tool_tags(src: Path) -> None:
    text = read(src / "MainWindow.ToolControls.cs")
    for m in re.finditer(r'AddAnnotationToolItem\(\w+,\s*"([^"]+)",\s*"([^"]+)"\)', text):
        TOOL_TAG_LABELS.setdefault(m.group(2), m.group(1))


def ribbon_group_label(node: XNode) -> str:
    for anc in node.ancestors():
        if anc.tag == "StackPanel" and "RibbonGroup}" in anc.style():
            for d in anc.walk():
                if d.tag == "TextBlock" and "RibbonGroupLabel" in d.style():
                    return d.attrs.get("Text", "")
    return ""


def row_label(node: XNode) -> str:
    """RibbonRowLabel TextBlock in the same Grid row as node (Display / Viewport tabs)."""
    parent = node.parent
    if parent is None:
        return ""
    row = node.attrs.get("Grid.Row", "0")
    for s in parent.children:
        if s.tag == "TextBlock" and "RibbonRowLabel" in s.style() and s.attrs.get("Grid.Row", "0") == row:
            return s.attrs.get("Text", "")
    return ""


def manager_group_label(node: XNode) -> str:
    """Nearest preceding sibling TextBlock styled ManagerGroupLabel (walks up)."""
    cur = node
    while cur.parent is not None:
        siblings = cur.parent.children
        idx = siblings.index(cur)
        for s in reversed(siblings[:idx]):
            if s.tag == "TextBlock" and "ManagerGroupLabel" in s.style():
                return s.attrs.get("Text", "")
        cur = cur.parent
        if cur.tag in ("TabItem", "Window", "UserControl"):
            break
    return ""


def ok_attr(v: str) -> bool:
    return bool(v) and not v.startswith("{")


def tooltip_head(tip: str, max_words: int) -> str:
    head = re.split(r"[:(;]|\.(?=\s|$)", tip, maxsplit=1)[0].strip()
    if head and len(head.split()) <= max_words:
        return head
    return ""


def xaml_title(node: XNode, surface: str) -> str:
    tip = node.attrs.get("ToolTip", "")
    if not ok_attr(tip):
        tip = ""
    if node.tag == "Slider":
        return re.split(r"\s+\d", tip, maxsplit=1)[0].strip() if tip else humanize_name(node.name())
    cands = []
    c = node.attrs.get("Content", "")
    if ok_attr(c):
        cands.append(c)
    h = node.attrs.get("Header", "")
    if ok_attr(h):
        cands.append(h)
    texts = []
    for d in node.walk():
        if d is node or d.tag not in ("TextBlock", "Run", "AccessText"):
            continue
        if not ok_attr(d.attrs.get("Text", "")):
            continue
        if any(a.tag in ("ToolTip", "ContextMenu", "Button.ContextMenu") for a in d.ancestors() if a is not node):
            # text inside this node's own tooltip or sub-menu is not its label
            inside = False
            for a in d.ancestors():
                if a is node:
                    break
                if a.tag in ("ToolTip", "ContextMenu", "Button.ContextMenu"):
                    inside = True
            if inside:
                continue
        texts.append(d.attrs["Text"])
    if texts:
        cands.append(" - ".join(texts) if len(texts) > 1 else texts[0])
    glyph = next((x for x in cands if re.search(r"[A-Za-z0-9]", x)), "")
    if not glyph and node.attrs.get("Tag", "") in TOOL_TAG_LABELS:
        return TOOL_TAG_LABELS[node.attrs["Tag"]]
    if surface == "xl" and glyph:
        if glyph in XL_TITLES:
            t = XL_TITLES[glyph]
            return t if t == glyph else f"{t} ({glyph})"
        pre = tip.split(":")[0].strip() if ":" in tip else ""
        if pre and len(pre.split()) <= 4:
            return f"{pre} ({glyph})"
        return glyph
    if glyph and len(glyph) <= 2 and tip:
        head = tooltip_head(tip, 8)
        if head:
            return head
    an = node.attrs.get("AutomationProperties.Name", "")
    if ok_attr(an):
        cands.append(an)
    if tip:
        head = tooltip_head(tip, 6)
        if head:
            cands.append(head)
    nm = node.name()
    if nm:
        cands.append(humanize_name(nm))
    if tip:
        cands.append(re.split(r"[:(;]|\.(?=\s|$)", tip, maxsplit=1)[0].strip())
    for cand in cands:
        if re.search(r"[A-Za-z0-9]", cand):
            return re.sub(r"\s+", " ", cand).strip()
    return cands[0].strip() if cands else ""


def xaml_items(path: Path, src: Path, handler_to_id: dict[str, str]) -> list[dict]:
    root = parse_xaml(path)
    base = path.name
    items = []
    for node in root.walk():
        if node.tag not in CONTROL_TAGS:
            continue
        if any(a.tag in SKIP_UNDER or a.tag.endswith(".Resources") for a in node.ancestors()):
            continue
        anc = list(node.ancestors())
        names = [a.name() for a in anc]
        surface = "workspace"
        group_parts: list[str] = []
        if base == "MainWindow.xaml":
            if "TopMainTabs" in names:
                surface = "ribbon"
                tab = next((a.attrs.get("Header", "") for a in anc if a.tag == "TabItem"), "")
                group_parts = [f"лента {tab}", ribbon_group_label(node)]
            elif "BottomToolStrip" in names:
                surface = "toolstrip"
                strip = next(a for a in anc if a.name() == "BottomToolStrip")
                row_border = next(a for a in reversed(anc) if a.parent is strip)
                row = strip.children.index(row_border) + 1
                group_parts = [f"нижняя полоса, строка {row}"]
            elif "ExcelMacroExportPanel" in names:
                surface = "xl"
                group_parts = ["полоса XL"]
            elif "MainStatusBar" in names:
                group_parts = ["строка статуса"]
            else:
                tabs = [a.attrs.get("Header", "") for a in reversed(anc) if a.tag == "TabItem" and a.attrs.get("Header")]
                hosts = [HOST_LABELS[n] for n in names if n in HOST_LABELS]
                parts = []
                if tabs:
                    parts.append(" > ".join(tabs))
                if hosts:
                    parts.append(hosts[0])
                mg = manager_group_label(node)
                if mg:
                    parts.append(f"группа {mg}")
                group_parts = parts or ["окно"]
        else:
            group_parts = [CONTROL_FILE_LABELS.get(base, base)]
            if base.endswith("Dialog.xaml"):
                surface = "dialog"
            mg = manager_group_label(node)
            if mg:
                group_parts.append(f"группа {mg}")
        if node.tag == "Slider" and surface != "ribbon":
            continue
        parent_button = None
        if node.tag == "MenuItem":
            for a in anc:
                if a.tag in ("Button", "ToggleButton"):
                    parent_button = a
                    break
            surface = "context-menu"
            if parent_button is not None:
                group_parts = [f"меню кнопки {xaml_title(parent_button, 'workspace')}"] + [p for p in group_parts if p]
        title = xaml_title(node, surface)
        if not title:
            continue
        tip = node.attrs.get("ToolTip", "")
        if not ok_attr(tip):
            tip = ""
        if not tip and (len(title) <= 1 or not re.search(r"[A-Za-z]", title)):
            continue  # calculator keypad and similar glyph-only buttons
        desc = tip
        if node.tag == "ComboBox":
            opts = [c.attrs.get("Content", "") for c in node.children if c.tag == "ComboBoxItem" and c.attrs.get("Content")]
            if opts:
                desc = (desc + " " if desc else "") + "Options: " + ", ".join(opts) + "."
            if not tip and not opts:
                continue
        if node.tag == "CheckBox" and not tip and len(title) <= 2:
            continue
        if surface == "ribbon" and node.tag != "Slider":
            # the same short label twice in one ribbon group (Size / w/page rows): add the row label
            rl = row_label(node)
            if rl and rl.lower() not in title.lower():
                twins = [s for s in root.walk() if s is not node and s.tag == node.tag
                         and ribbon_group_label(s) == ribbon_group_label(node)
                         and (s.attrs.get("Content") == node.attrs.get("Content") and node.attrs.get("Content"))]
                if twins:
                    title = f"{rl}: {title}"
        if node.tag == "MenuItem" and " \u2014 " in title:
            title, extra = title.split(" \u2014 ", 1)
            desc = desc or extra
        shortcut = shortcut_from_text(tip) or shortcut_from_text(title)
        handler = node.attrs.get("Click", "") or node.attrs.get("Checked", "")
        cid = handler_to_id.get(handler, "") if base == "MainWindow.xaml" else ""
        item = {
            "surface": surface,
            "group": ", ".join(p for p in group_parts if p),
            "title": title,
            "shortcut": shortcut,
            "description": desc,
            "source": f"{rel(path, src)}:{node.line}",
            "control": node.tag,
        }
        if cid:
            item["id"] = cid
        if handler:
            item["handler"] = handler
        items.append(item)
    return items


# ---------------------------------------------------------------- code-built menus

MENU_CALLS = re.compile(r"\b(MakeMenuItem|MakeSubmenu|MakeMenuHeader|TemplateMenuItem)\(")
NEW_MENUITEM = re.compile(r"new MenuItem\s*\{")

# (file, method) -> label shown as "group"; fallback is "file:method"
MENU_LABELS = {
    ("MainWindow.PagesCommands.cs", "BuildPagesContextMenu"): "меню папки в Pages",
    ("MainWindow.TakeoffsMenus.cs", "AttachContextMenu"): "меню позиции в Takeoffs",
    ("MainWindow.TakeoffsMenus.cs", "AttachFolderContextMenu"): "меню папки в Takeoffs",
    ("MainWindow.TakeoffsMenus.cs", "BuildTakeoffsRootContextMenu"): "меню корня Takeoffs",
    ("MainWindow.TakeoffsMenus.cs", "BuildTakeoff3DMenu"): "меню позиции в Takeoffs > 3D",
    ("MainWindow.TakeoffSections.cs", "BuildTakeoffSectionContextMenu"): "меню секции (замера) в Takeoffs",
    ("MainWindow.TakeoffsActiveTarget.cs", "BtnActiveTakeoffMore_Click"): "меню More активной позиции (панель Takeoffs)",
    ("MainWindow.TakeoffsActiveTarget.cs", "ShowActiveSheetTakeoffTargetMenu"): "меню Sheet активной позиции (панель Takeoffs)",
    ("MainWindow.PageTakeoffLegend.ContextMenu.cs", "BuildPageTakeoffContextMenu"): "меню легенды листа (позиция под листом в Pages)",
    ("MainWindow.PageLegendGroups.cs", "BuildPageTakeoffLegendGroupMenu"): "меню легенды листа > Legend Group",
    ("MainWindow.CountDisplay.cs", "BuildTakeoffCountDisplayMenu"): "меню позиции в Takeoffs",
    ("MainWindow.CountDisplay.cs", "BuildTakeoffSectionCountDisplayMenu"): "меню секции (замера) в Takeoffs",
    ("MainWindow.CountDisplay.cs", "BuildPageTakeoffCountDisplayMenu"): "меню легенды листа (позиция под листом в Pages)",
    ("MainWindow.CountDisplay.cs", "AddViewportCountDisplayMenuItem"): "меню вьюпорта: выбранный замер",
    ("MainWindow.CountDisplay.cs", "BuildCountDisplayMenu"): "меню Count Display (символ метки Count)",
    ("MainWindow.CountDisplay.cs", "BtnCountSymbolDefault_Click"): "меню кнопки символа Count по умолчанию (нижняя полоса)",
    ("MainWindow.ViewportCallbacks.cs", "OnViewportContextRequested"): "меню вьюпорта (правый клик по листу)",
    ("MainWindow.ViewportContextMenu.cs", "AddMeasurementClipboardMenuItems"): "меню вьюпорта: буфер замеров",
    ("MainWindow.ViewportContextMenu.cs", "AddPdfAiMenuItems"): "меню вьюпорта > AI Assist (точка листа)",
    ("MainWindow.ViewportContextMenu.cs", "AddMeasurementEditMenuItems"): "меню вьюпорта: выбранный замер",
    ("MainWindow.ViewportContextMenu.cs", "AddAnnotationEditMenuItems"): "меню вьюпорта: разметка (annotation)",
    ("MainWindow.ViewportContextMenu.cs", "AddMeasurementAiMenuItems"): "меню вьюпорта > AI Assist (замер)",
    ("MainWindow.DetachedSheets.cs", "OnDetachedViewportContextRequested"): "меню вьюпорта в отдельном окне листа",
    ("MainWindow.ThreeDRoof.cs", "AddViewportThreeDMenuItems"): "меню вьюпорта > 3D",
    ("MainWindow.ThreeDRoof.cs", "AddViewportThreeDRoofEdgeMenuItems"): "меню вьюпорта > 3D (ребро крыши)",
    ("MainWindow.SheetCrops.cs", "AddSheetCropMenuItems"): "меню вьюпорта: кроп (Crop to Sheet)",
    ("MainWindow.SheetOverlay.Menus.cs", "BuildSheetOverlayMenu"): "меню листа в Pages > Sheet Overlay",
    ("MainWindow.SheetOverlay.Menus.cs", "BuildPageOverlayContextMenu"): "меню слоя наложения (под листом в Pages)",
    ("MainWindow.SheetOverlay.Menus.cs", "AddCurrentSheetOverlayAdjustmentMenuItems"): "меню вьюпорта: наложение листа",
    ("MainWindow.DisplaySettings.OverlayMenus.cs", "AddSheetOverlayMenuItems"): "меню вьюпорта: легенда и подписи",
    ("MainWindow.DisplaySettings.OverlayMenus.cs", "BuildLegendMenuItem"): "меню вьюпорта: легенда и подписи",
    ("MainWindow.DisplaySettings.OverlayMenus.cs", "BuildLegendPositionMenu"): "меню вьюпорта > Legend > Legend Position",
    ("MainWindow.DisplaySettings.OverlayMenus.cs", "BuildOverlaySizeMenu"): "меню вьюпорта > размер легенды / шапки",
    ("MainWindow.DisplaySettings.OverlayMenus.cs", "ShowOverlaySizePopup"): "меню кнопки Size (лента Display)",
    ("MainWindow.DisplaySettings.OverlayMenus.cs", "BtnLegendPositionMenu_Click"): "меню кнопки Pos (лента Display)",
    ("MainWindow.DisplaySettings.MeasurementSizing.cs", "BtnStrokeSizePresets_Click"): "меню пресетов толщины линий (лента Viewport)",
    ("MainWindow.DisplaySettings.MeasurementSizing.cs", "BtnPointSizePresets_Click"): "меню пресетов размера точек (лента Viewport)",
    ("MainWindow.OpenImportMenu.cs", "BtnOpenImportMenu_Click"): "меню кнопки Open / Import",
    ("MainWindow.ExportMenu.cs", "BtnRightExportMenu_Click"): "меню кнопки Export (панель Takeoffs)",
    ("MainWindow.AiInbox.cs", "BtnInboxMore_Click"): "меню кнопки More (AI Inbox)",
    ("MainWindow.AiInbox.cs", "BuildObservationsContextMenu"): "меню записи AI Inbox",
    ("MainWindow.Templates.cs", "BuildTemplateNodeContextMenu"): "меню панели Templates",
    ("MainWindow.PdfLayers.cs", "BuildPdfLayerContextMenu"): "меню слоя PDF (Pages > PDF Layers)",
    ("MainWindow.PageTabs.cs", "BuildPageTabContextMenu"): "меню вкладки листа",
    ("MainWindow.PageImageTools.cs", "BtnPageBatchRotate_Click"): "меню кнопки Batch Rotate (лента Page)",
    ("MainWindow.Estimating.cs", "BuildEstimateContextMenu"): "меню строки Estimating",
    ("MainWindow.ToolControls.cs", "BtnAnnotationMenu_Click"): "меню Style (лента Annotation)",
    ("MainWindow.ToolControls.cs", "AddAnnotationThicknessMenu"): "меню Style > Thickness",
    ("MainWindow.ToolControls.cs", "AddAnnotationColorMenu"): "меню Style > Color",
    ("MainWindow.ToolControls.cs", "BtnScalePresets_Click"): "меню Presets масштаба (нижняя полоса)",
    ("TerminalPanel.xaml.cs", "ShowAttachChoices"): "меню Attach (терминал)",
    ("TerminalPanel.xaml.cs", "More_Click"): "меню More (терминал)",
}

# a method with two branches: items after the marker get another label
MENU_BRANCHES = [
    ("MainWindow.PagesCommands.cs", "BuildPagesContextMenu", r"else if \(item\.Tag is PageInfo page\)", "меню листа в Pages"),
]

MENU_FILE_SKIP = {"MainWindow.MenuHelpers.cs", "MainWindow.CustomShortcuts.Surfaces.cs"}

# what an unresolved {hole} means inside one method ("Copy {title}" of a markup)
HOLE_WORDS = {
    ("MainWindow.ViewportContextMenu.cs", "AddAnnotationEditMenuItems"): "Markup",
}


class CsFile:
    """One C# file with the per-file state needed to label menu items."""

    def __init__(self, path: Path, src: Path):
        self.path = path
        self.name = path.name
        self.rel = rel(path, src)
        self.text = read(path)
        self.methods = method_index(self.text)
        self.spans: list[tuple[int, int, str]] = []
        self.var_headers: dict[tuple[str, str], str] = {}
        self.captions: list[tuple[int, str, str]] = []
        self._index_containers()

    def method_at(self, pos):
        return enclosing_method(self.methods, pos)

    def body_at(self, pos):
        return method_body(self.text, self.methods, pos)

    def _index_containers(self):
        text = self.text
        for m in re.finditer(r"\bMakeSubmenu\(", text):
            if text[max(0, m.start() - 20):m.start()].rstrip().endswith("MenuItem"):
                continue
            end = balanced_span(text, m.end() - 1)
            args = split_args(text[m.end():end - 1])
            if args:
                hdr, _, _ = resolve_expr(args[0], self.body_at(m.start()))
                self.spans.append((m.start(), end, hdr))
        for m in re.finditer(r"(?:var|MenuItem)\s+(\w+)\s*=\s*(MakeSubmenu\(|new MenuItem\s*\{)", text):
            meth, _, _ = self.method_at(m.start())
            end = balanced_span(text, m.end() - 1)
            inner = text[m.end():end - 1]
            if m.group(2).startswith("MakeSubmenu"):
                args = split_args(inner)
                hdr = resolve_expr(args[0], self.body_at(m.start()))[0] if args else ""
            else:
                hm = re.search(r"Header\s*=\s*(.+?)(?:,\s*\n|\n|$)", inner, re.S)
                hdr = resolve_expr(hm.group(1), self.body_at(m.start()))[0] if hm else ""
            if hdr and not hdr.startswith("<"):
                self.var_headers[(meth, m.group(1))] = hdr
        for m in re.finditer(r"\bMakeMenuHeader\(", text):
            if text[max(0, m.start() - 20):m.start()].rstrip().endswith("MenuItem"):
                continue
            end = balanced_span(text, m.end() - 1)
            args = split_args(text[m.end():end - 1])
            meth, _, _ = self.method_at(m.start())
            if args:
                self.captions.append((m.start(), meth, unquote(args[0]).title()))

    def label_for(self, pos: int) -> str:
        text = self.text
        meth, body_start, _ = self.method_at(pos)
        label = MENU_LABELS.get((self.name, meth), f"{self.name}:{meth}")
        for bf, bm, marker, after in MENU_BRANCHES:
            if bf == self.name and bm == meth and re.search(marker, text[body_start:pos]):
                label = after
        parts = [label]
        for s_start, s_end, hdr in self.spans:
            if s_start < pos < s_end and hdr and hdr.lower() not in label.lower():
                parts.append(hdr)
        before = text[max(0, pos - 80):pos]
        vm = re.search(r"(\w+)\.Items\.Add\(\s*$", before)
        if vm and (meth, vm.group(1)) in self.var_headers:
            hdr = self.var_headers[(meth, vm.group(1))]
            if hdr.lower() not in " ".join(parts).lower():
                parts.append(hdr)
        cap = ""
        for cpos, cmeth, ctext in self.captions:
            if cmeth == meth and cpos < pos:
                cap = ctext
        if cap:
            parts.append(cap)
        return " > ".join(dict.fromkeys(p for p in parts if p))


def scan_code_menus(src: Path, handler_to_id: dict[str, str]) -> list[dict]:
    items = []
    paths = sorted(src.glob("MainWindow.*.cs")) + sorted((src / "Controls").glob("*.cs"))
    files = [CsFile(p, src) for p in paths if p.name not in MENU_FILE_SKIP and "MenuItem" in read(p)]
    forwarders: dict[str, int] = {}  # helper method -> index of its header parameter
    seen_sources: set[str] = set()

    def add_item(f: CsFile, pos: int, header_expr: str, enabled_expr: str, action_text: str, label_pos: int | None = None):
        label_file = f
        scope = f.body_at(pos)
        title, aliases, dynamic = resolve_expr(header_expr, scope)
        meth, _, params = f.method_at(pos)
        if title.startswith("<") and title.endswith(">"):
            ident = title[1:-1]
            if IDENT.match(ident) and ident in params and meth not in ("MakeMenuItem", "MakeSubmenu", "TemplateMenuItem"):
                forwarders[meth] = params.index(ident)
            return
        if enabled_expr.strip() == "false" and re.search(r"\(\)\s*=>\s*\{\s*\}", action_text):
            return
        title = re.sub(r"\s+", " ", title).strip()
        if not re.search(r"[A-Za-z]", title) or title.startswith("{...}"):
            return  # loop variable over presets: no stable label
        title = title.replace("{...}", HOLE_WORDS.get((f.name, meth), "...")).replace(" ...", " ...").strip()
        title = re.sub(r"\s+", " ", title)
        src_key = f"{f.rel}:{line_of(f.text, pos)}"
        if src_key in seen_sources:
            return
        seen_sources.add(src_key)
        handler = ""
        hm = re.search(r"\b(Btn\w+_Click|\w+)\(", action_text or "")
        if hm:
            handler = hm.group(1)
        cid = handler_to_id.get(handler, "") if handler else ""
        item = {
            "surface": "context-menu",
            "group": label_file.label_for(label_pos if label_pos is not None else pos),
            "title": title,
            "shortcut": shortcut_from_text(title),
            "description": "",
            "source": src_key,
        }
        if aliases:
            item["aliases"] = [a for a in aliases if a and a != title]
            if not item["aliases"]:
                del item["aliases"]
        if dynamic:
            item["dynamic"] = True
        if cid:
            item["id"] = cid
        items.append(item)

    for f in files:
        text = f.text
        for m in MENU_CALLS.finditer(text):
            kind = m.group(1)
            if text[max(0, m.start() - 20):m.start()].rstrip().endswith("MenuItem"):
                continue
            if kind in ("MakeSubmenu", "MakeMenuHeader"):
                continue
            end = balanced_span(text, m.end() - 1)
            args = split_args(text[m.end():end - 1])
            if not args:
                continue
            enabled = args[1] if kind == "MakeMenuItem" and len(args) > 1 else "true"
            action = args[2] if kind == "MakeMenuItem" and len(args) > 2 else (args[1] if len(args) > 1 else "")
            add_item(f, m.start(), args[0], enabled, action)
        for m in NEW_MENUITEM.finditer(text):
            before = text[max(0, m.start() - 60):m.start()]
            vm = re.search(r"(?:var|MenuItem)\s+(\w+)\s*=\s*$", before)
            init_end = balanced_span(text, m.end() - 1)
            init = text[m.end():init_end - 1]
            if vm:
                var = vm.group(1)
                body = f.body_at(m.start())
                if re.search(r"\b" + re.escape(var) + r"\.Items\.Add\(", body) or re.search(r"\(\s*" + re.escape(var) + r"\s*,", body):
                    continue  # a container; its children carry the functions
            if re.search(r"IsEnabled\s*=\s*false", init):
                continue
            hm = re.search(r"Header\s*=\s*(.+?)(?:,\s*\n|\n|$)", init, re.S)
            if not hm:
                continue
            add_item(f, m.start(), hm.group(1).strip().rstrip(","), "true", init)

    # helpers that forward a header parameter: one item per call site
    for helper, idx in forwarders.items():
        pat = re.compile(r"\b" + re.escape(helper) + r"\(")
        for f in files:
            for m in pat.finditer(f.text):
                if f.text[max(0, m.start() - 40):m.start()].rstrip().endswith(("MenuItem", "void", "bool")):
                    continue  # the definition
                end = balanced_span(f.text, m.end() - 1)
                args = split_args(f.text[m.end():end - 1])
                if len(args) <= idx:
                    continue
                add_item(f, m.start(), args[idx], "true", " ".join(args[idx + 1:]))
    return items


# ---------------------------------------------------------------- code-built panels (buttons)

PANEL_LABELS = {
    "MainWindow.MassingPanel.cs": "панель 3D Massing (AI Inbox)",
    "MainWindow.ThreeDSidePanel.cs": "боковая панель 3D",
    "MainWindow.Estimating.cs": "правая панель, вкладка Estimating",
    "MainWindow.AiObservationDetails.cs": "окно Observation Details",
    "MainWindow.ActiveTakeoffBuilding.cs": "панель Takeoffs, выбор корпуса",
    "MainWindow.PageTabs.cs": "вкладки листов",
    "MainWindow.TakeoffsProperties.cs": "окно Takeoff Item Properties",
    "MainWindow.TakeoffsBulkProperties.cs": "окно Bulk Properties",
    "MainWindow.PdfOutputPreview.cs": "окно Export PDF (предпросмотр)",
    "MainWindow.Templates.cs": "панель Templates",
    "MainWindow.ViewportCallbacks.cs": "вьюпорт",
    "MainWindow.MeasurementMergeSplit.cs": "окно Merge Into Takeoff",
    "MainWindow.PdfImport.cs": "окно Import PDF Options",
    "MainWindow.PlanSwiftImport.cs": "окно PlanSwift Import Complete",
    "MainWindow.TakeoffsSplit.cs": "окно Split Selected Takeoffs",
    "MainWindow.Utilities.cs": "окно ввода",
}
GENERIC_BUTTONS = {"ok", "cancel", "close", "apply", "save", "yes", "no", "run", "create", "import",
                   "export", "merge", "split", "trace", "x"}


def scan_code_buttons(src: Path, handler_to_id: dict[str, str]) -> list[dict]:
    items = []
    for path in sorted(src.glob("MainWindow.*.cs")):
        if "SettingsManager" in path.name or path.name == "MainWindow.SideStrips.cs":
            continue
        text = read(path)
        for m in re.finditer(r"new Button\b\s*(?:\(\))?\s*\{", text):
            end = balanced_span(text, m.end() - 1)
            init = text[m.end():end - 1]
            cm = re.search(r'Content\s*=\s*"([^"]+)"', init)
            if not cm:
                continue
            title = cm.group(1)
            if title.lower() in GENERIC_BUTTONS:
                continue
            tm = re.search(r'ToolTip\s*=\s*"([^"]+)"', init)
            after = text[end:end + 400]
            hm = re.search(r"Click\s*\+=\s*\(?[^)]*\)?\s*=>\s*(\w+)\(", after)
            handler = hm.group(1) if hm else ""
            item = {
                "surface": "panel",
                "group": PANEL_LABELS.get(path.name, path.name),
                "title": title,
                "shortcut": "",
                "description": tm.group(1) if tm else "",
                "source": f"{rel(path, src)}:{line_of(text, m.start())}",
            }
            if handler in handler_to_id:
                item["id"] = handler_to_id[handler]
            items.append(item)
    return items


# ---------------------------------------------------------------- side strips


def scan_strips(src: Path, palette_by_id: dict[str, dict]) -> list[dict]:
    path = src / "MainWindow.SideStrips.cs"
    text = read(path)
    catalog: dict[str, dict] = {}
    for m in re.finditer(r'new(?:\s+SideStripCommandInfo)?\("([\w.]+)",\s*"([^"]*)",\s*"([^"]*)",\s*"([^"]*)",\s*"([^"]*)"\)', text):
        catalog[m.group(1)] = {"title": m.group(2), "group": m.group(3), "shortcut": m.group(4), "description": m.group(5)}
    items = []
    for var, label in (("LeftStripDefaultCommands", "левая полоса значков"),
                       ("RightStripDefaultCommands", "правая полоса значков")):
        m = re.search(re.escape(var) + r"\s*=\s*\[(.*?)\];", text, re.S)
        if not m:
            continue
        for im in re.finditer(r'"([\w.]+)"', m.group(1)):
            cid = im.group(1)
            info = catalog.get(cid) or palette_by_id.get(cid)
            if not info:
                continue
            items.append({
                "surface": "strip",
                "group": label,
                "title": info["title"],
                "shortcut": palette_by_id.get(cid, {}).get("shortcut", info.get("shortcut", "")),
                "description": info.get("description", ""),
                "source": f"{rel(path, src)}:{line_of(text, m.start() + im.start())}",
                "id": cid,
            })
    for m in re.finditer(r'"(Configure the (left|right) command strip)"', text):
        items.append({
            "surface": "strip",
            "group": f"{'левая' if m.group(2) == 'left' else 'правая'} полоса значков",
            "title": "Configure the command strip (gear)",
            "shortcut": "",
            "description": m.group(1) + ": pick any commands for the strip.",
            "source": f"{rel(path, src)}:{line_of(text, m.start())}",
        })
    m = re.search(r'ToolTip = "(Show / hide Codex and Claude terminals)"', text)
    if m:
        items.append({
            "surface": "strip", "group": "правая полоса значков", "title": "Terminal (>_)",
            "shortcut": "", "description": m.group(1), "source": f"{rel(path, src)}:{line_of(text, m.start())}",
            "id": "view.terminal",
        })
    return items


# ---------------------------------------------------------------- settings


def scan_settings(src: Path) -> list[dict]:
    main = src / "MainWindow.SettingsManager.cs"
    text = read(main)
    items = []
    cats = []
    m = re.search(r"SettingsCategories\s*=\s*\[(.*?)\];", text, re.S)
    if m:
        for cm in re.finditer(r'"([^"]+)"', m.group(1)):
            cats.append(cm.group(1))
            items.append({
                "surface": "settings", "group": "Settings, категория", "title": cm.group(1), "shortcut": "",
                "description": "Settings category (default, presets, per-job override).",
                "source": f"{rel(main, src)}:{line_of(text, m.start() + cm.start())}",
            })
    builder_to_cat: dict[str, str] = {}
    for cm in re.finditer(r'"([^"]+)"\s*=>\s*(\w+)\(\)', text):
        builder_to_cat[cm.group(2)] = cm.group(1)
    dm = re.search(r"_\s*=>\s*(\w+)\(\)", text)
    if dm and cats:
        builder_to_cat[dm.group(1)] = cats[-1]
    files = sorted(src.glob("MainWindow.SettingsManager*.cs"))
    texts = {p: read(p) for p in files}
    methods = {p: method_index(t) for p, t in texts.items()}

    def category_of(method: str, depth: int = 0) -> str:
        if method in builder_to_cat:
            return builder_to_cat[method]
        if depth > 3:
            return ""
        for p, t in texts.items():
            for cm in re.finditer(r"\b" + re.escape(method) + r"\(", t):
                caller, _, _ = enclosing_method(methods[p], cm.start())
                if caller and caller != method:
                    cat = category_of(caller, depth + 1)
                    if cat:
                        return cat
        return ""

    for p, t in texts.items():
        for hm in re.finditer(r"\bHeader\(\s*\"([^\"]+)\"\s*\)", t):
            meth, _, _ = enclosing_method(methods[p], hm.start())
            if meth == "Header":
                continue
            cat = category_of(meth) or "?"
            title = hm.group(1)
            if title in cats and cat == title:
                continue
            items.append({
                "surface": "settings", "group": f"Settings > {cat}", "title": title, "shortcut": "",
                "description": "Section of the settings panel.",
                "source": f"{rel(p, src)}:{line_of(t, hm.start())}",
            })
    return items


# ---------------------------------------------------------------- dialogs


def scan_dialogs(src: Path) -> list[dict]:
    items = []
    paths = sorted((src / "Dialogs").glob("*.cs")) + sorted((src / "Dialogs").glob("*.xaml"))
    paths += [p for p in sorted(src.glob("MainWindow.*.cs")) if 'Title = "' in read(p)]
    seen = set()
    for path in paths:
        text = read(path)
        if path.suffix == ".xaml":
            tm = re.search(r'\bTitle="([^"]+)"', text)
            titles = [(tm.group(1), tm.start())] if tm else []
            buttons = re.findall(r'<Button[^>]*?Content="([^"{}]+)"', text)
        else:
            titles = [(m.group(1), m.start()) for m in re.finditer(r'\bTitle = "([^"]+)"', text)
                      if not re.search(r"(Open|Save)(File|Folder)Dialog", text[max(0, m.start() - 80):m.start()])]
            buttons = []
            for bm in re.finditer(r"new Button\b[^;{]*\{", text):
                end = balanced_span(text, bm.end() - 1)
                cm = re.search(r'Content\s*=\s*"([^"]+)"', text[bm.end():end])
                if cm:
                    buttons.append(cm.group(1))
            for bm in re.finditer(r'Button\s+\w+\s*=\s*new\(\)\s*\{[^}]*?Content\s*=\s*"([^"]+)"', text):
                buttons.append(bm.group(1))
        main_buttons = [b for b in dict.fromkeys(buttons) if b.lower() not in GENERIC_BUTTONS]
        for idx, (title, pos) in enumerate(titles):
            key = (path.name, title)
            if key in seen:
                continue
            seen.add(key)
            desc = ""
            if idx == 0 and main_buttons:
                desc = "Buttons: " + ", ".join(main_buttons) + "."
            group = "окно" if path.parent.name == "Dialogs" else "окно (строится в коде главного окна)"
            items.append({
                "surface": "dialog", "group": group, "title": title, "shortcut": "", "description": desc,
                "source": f"{rel(path, src)}:{line_of(text, pos)}",
            })
    return items


# ---------------------------------------------------------------- assemble


def make_key(item: dict) -> str:
    if item.get("id"):
        return item["id"]
    return f"{item['surface']}|{norm_title(item['title'])}"


def build_inventory(src: Path) -> dict:
    index_string_methods(src)
    index_tool_tags(src)
    palette, handler_to_id, by_id = scan_palette(src)
    f1 = scan_f1(src)
    defaults = scan_defaults(src, by_id)
    link_f1_to_ids(f1, src, by_id, defaults)
    xaml = xaml_items(src / "MainWindow.xaml", src, handler_to_id)
    for cx in sorted((src / "Controls").glob("*.xaml")):
        xaml += xaml_items(cx, src, handler_to_id)
    for dx in sorted((src / "Dialogs").glob("*.xaml")):
        xaml += [i for i in xaml_items(dx, src, handler_to_id) if i["title"].lower() not in GENERIC_BUTTONS]
    menus = scan_code_menus(src, handler_to_id)
    buttons = scan_code_buttons(src, handler_to_id)
    strips = scan_strips(src, by_id)
    settings = scan_settings(src)
    dialogs = scan_dialogs(src)
    items = palette + f1 + defaults + xaml + strips + menus + buttons + settings + dialogs
    titles_by_id: dict[str, list[str]] = {}
    for it in items:
        if it.get("id"):
            titles_by_id.setdefault(it["id"], [])
            if it["title"] not in titles_by_id[it["id"]]:
                titles_by_id[it["id"]].append(it["title"])
    for it in items:
        it["key"] = make_key(it)
        if it.get("id"):
            extra = [t for t in titles_by_id[it["id"]] if t != it["title"]]
            if extra:
                it["aliases"] = list(dict.fromkeys(it.get("aliases", []) + extra))
    counts: dict[str, int] = {}
    for it in items:
        counts[it["surface"]] = counts.get(it["surface"], 0) + 1
    return {
        "generated_by": "tools/opc_inventory.py",
        "src": str(src),
        "counts": counts,
        "total": len(items),
        "items": items,
    }


# ---------------------------------------------------------------- page

SURFACE_RU = {
    "toolstrip": ("Нижняя полоса инструментов", "нижняя полоса"),
    "ribbon": ("Лента: верхние вкладки Main, Page, Annotation, Viewport, Display", "лента"),
    "xl": ("Полоса XL (Excel) справа от листа", "полоса XL"),
    "strip": ("Полосы значков слева и справа от листа (набор по умолчанию)", "полоса значков"),
    "workspace": ("Панели и вкладки рабочей области", "панель"),
    "context-menu": ("Контекстные меню и меню кнопок", "меню"),
    "panel": ("Кнопки панелей и окон, которые строятся в коде", "панель"),
    "palette": ("Палитра команд (Ctrl+Shift+P)", "палитра команд"),
    "f1": ("Справка по клавишам (F1)", "F1"),
    "defaults": ("Клавиши по умолчанию, которых нет в палитре", "клавиша"),
    "settings": ("Settings: категории и разделы", "Settings"),
    "dialog": ("Окна и диалоги", "окно"),
}
SURFACE_ORDER = ["toolstrip", "ribbon", "xl", "strip", "workspace", "context-menu", "panel",
                 "palette", "f1", "defaults", "settings", "dialog"]


def clean(text: str) -> str:
    """Text safe for the KB: no long dashes, arrows, guillemets, middle dots, table pipes."""
    repl = {"\u2014": "-", "\u2013": "-", "\u2192": "->", "\u2190": "<-", "\u21d2": "->", "\u2194": "<->",
            "\u279c": "->", "\u00b7": ",", "\u00ab": '"', "\u00bb": '"', "\u2026": "...", "\u21bb": "Repeat",
            "\u2500": "-", "\u25b6": "", "\u25be": "", "|": "\\|"}
    for a, b in repl.items():
        text = text.replace(a, b)
    return re.sub(r"\s+", " ", text).strip()


PAGE_LABELS = {
    "ourplanecore.md": "хаб OurPlanCore", "ourplancore-start.md": "Начало работы",
    "job-creation-storage.md": "Проекты и сохранение", "ourplancore-pages.md": "Листы (Pages)",
    "ourplancore-tools.md": "Инструменты замера", "ourplancore-takeoffs.md": "Дерево Takeoffs",
    "takeoff-naming.md": "Имена и автомаршрут", "ourplancore-excel.md": "Экспорт в Excel",
    "ourplancore-pdf.md": "PDF и сдача", "ourplancore-routing.md": "Маршрутизация и правила",
    "ourplancore-edit-takeoffs.md": "Merge, Split, Break", "ourplancore-sheets-advanced.md": "Кропы, маска, наложения, легенда",
    "ourplancore-settings.md": "Settings и модули", "ourplancore-ai.md": "ИИ и терминалы",
    "ourplancore-ai-console.md": "Консоль ИИ", "ourplancore-workspace.md": "Workspace, Job Tracker, CLI",
    "ourplancore-3d.md": "3D и менеджеры", "ourplancore-3d-roof.md": "3D крыша", "ourplancore-shortcuts.md": "Горячие клавиши",
    "ourplancore-troubleshooting.md": "Решение проблем", "ourplancore-changelog.md": "Что нового",
    "ourplancore-buildings.md": "Корпуса", "ourplancore-extras.md": "Дополнительно", "ourplancore-extras-other.md": "Прочее",
    "ourplancore-managers.md": "Менеджеры", "ourplancore-snap-trace.md": "Привязки и трассировка",
    "ourplancore-split-by-sheets.md": "Разбивка по листам", "ourplancore-editing.md": "Правка и привязки",
    "ourplancore-ideas.md": "Идеи и планы",
}


def page_label(page: str) -> str:
    name = page.split("#")[0]
    return PAGE_LABELS.get(name, name.replace(".md", ""))


def ru_text(ru: dict, it: dict) -> str:
    for k in (it["key"], f"{it['surface']}|{norm_title(it['title'])}", f"*|{norm_title(it['title'])}"):
        if k in ru and ru[k]:
            return ru[k]
    return ""


def render_page(inv: dict, coverage: dict, ru: dict) -> str:
    lines = [
        "# Все функции программы",
        "",
        "Страница собирается из кода программы скриптом tools/opc_inventory.py; не править руками.",
        "",
        "Здесь перечислена каждая кнопка, пункт меню, клавиша, категория Settings и окно OurPlanCore 3.0, "
        "по месту в интерфейсе. Колонка \"Подробно\" ведёт на страницу раздела, где функция описана; "
        "пустая ячейка значит, что подробного описания в базе пока нет "
        "(проверка: `python tools/opc_coverage.py`). Одна и та же функция часто доступна с нескольких "
        "поверхностей (лента, меню, палитра, клавиша), поэтому повторы здесь нормальны.",
        "",
        f"Всего записей: {inv['total']}. С подробной страницей: {coverage.get('described', 0)}. "
        f"Пока без страницы: {coverage.get('missing', 0)}. Служебных и повторов, исключённых из проверки: {coverage.get('ignored', 0)}.",
        "",
    ]
    by_source = coverage.get("items", {})
    items = inv["items"]
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from opc_coverage import item_uids  # noqa: E402

    for it, uid in zip(items, item_uids(items)):
        it["_uid"] = uid
    for surface in SURFACE_ORDER:
        rows = [i for i in items if i["surface"] == surface]
        if not rows:
            continue
        title, where = SURFACE_RU[surface]
        lines.append(f"## {title} ({len(rows)})")
        lines.append("")
        groups: dict[str, list[dict]] = {}
        for it in rows:
            groups.setdefault(it["group"] or "-", []).append(it)
        for group, grows in groups.items():
            lines.append(f'??? note "{clean(group)} ({len(grows)})"')
            lines.append("")
            lines.append("    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |")
            lines.append("    | --- | --- | --- | --- | --- |")
            for it in grows:
                cov = by_source.get(it["_uid"], {})
                page = cov.get("page", "")
                link = f"[{page_label(page)}]({page})" if page else ""
                desc = ru_text(ru, it) or clean(it["description"])
                sc = f"`{clean(it['shortcut'])}`" if it.get("shortcut") else ""
                where_text = f"{where}: {it['group']}" if it["group"] else where
                lines.append(
                    f"    | `{clean(it['title'])}` | {sc} | {clean(where_text)} | {clean(desc)} | {link} |")
            lines.append("")
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------- main


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--src", default=str(DEFAULT_SRC), help="OurPlanCore source folder")
    ap.add_argument("--out", default=str(JSON_OUT), help="inventory JSON path")
    ap.add_argument("--page", action="store_true", help="also render docs/reference/ourplancore-all-functions.md")
    args = ap.parse_args()
    src = Path(args.src)
    if not (src / "MainWindow.xaml").exists():
        print(f"source folder not found or not OurPlanCore: {src}")
        return 2
    inv = build_inventory(src)
    out = Path(args.out)
    out.write_text(json.dumps(inv, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"inventory: {inv['total']} items -> {out}")
    for k in SURFACE_ORDER:
        if k in inv["counts"]:
            print(f"  {k:13} {inv['counts'][k]}")
    if args.page:
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        import opc_coverage  # noqa: E402

        coverage = opc_coverage.compute(inv, opc_coverage.load_pages(), opc_coverage.load_ignore())
        ru = json.loads(RU_TEXT.read_text(encoding="utf-8")) if RU_TEXT.exists() else {}
        PAGE_OUT.write_text(render_page(inv, coverage, ru), encoding="utf-8", newline="\n")
        missing_ru = sum(1 for it in inv["items"] if not ru_text(ru, it))
        print(f"page: {PAGE_OUT} (записей без русского описания: {missing_ru})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
