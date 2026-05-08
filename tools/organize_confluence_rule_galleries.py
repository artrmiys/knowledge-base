"""Convert imported Confluence galleries into rule-linked visual cards.

The generated Confluence blocks are useful as image archives, but on topic
pages they read like loose screenshots. This script rebuilds those blocks as
`kb-rule-card` galleries with a page-specific rule and note.
"""

from __future__ import annotations

import html
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


CONFIGS: dict[str, tuple[str, str, str]] = {
    "docs/work-types/com.md": (
        "COM - визуальная проверка",
        "Сверь COM scope, level split, loose material и финальный QA checklist.",
        "Если condition влияет на output, он должен быть отдельной строкой или явной note.",
    ),
    "docs/reference/source-map.md": (
        "Source Map - исходные screenshots",
        "Используй как карту источников, а не как рабочую страницу takeoff.",
        "Правила из source map переносим в topic pages; private данные не публикуем.",
    ),
    "docs/reference/boss-feedback-rules.md": (
        "QA feedback - визуальная проверка",
        "Преврати замечание в конкретный check перед отправкой.",
        "Если feedback повторяется, держи правило в основной секции страницы.",
    ),
    "docs/reference/hangers.md": (
        "Hanger - schedule/detail проверка",
        "Сверь hanger family, size, skew, top/face mount и support condition.",
        "Hanger не выбирается только по ширине: смотри material, bearing и detail.",
    ),
    "docs/work/deck/railing.md": (
        "Railing - визуальная проверка",
        "Проверь railing run, post condition, returns и connection points.",
        "Не смешивай railing LF с deck/balcony trim, если scope просит отдельно.",
    ),
    "docs/work/deck/balcony-trims.md": (
        "Balcony Trim - визуальная проверка",
        "Сверь fascia/trim runs, exposed edges и finish material.",
        "Trim на balcony держи отдельно от interior trims и framing.",
    ),
    "docs/work/deck/anchor-bolts.md": (
        "Anchor Bolt - визуальная проверка",
        "Проверь spacing, edge/corner conditions, washers и plate connection.",
        "Anchor bolts идут вместе с Sill Plates/Btm Plate rules, но output может быть отдельной строкой.",
    ),
    "docs/start/takeoff-structure.md": (
        "PlanSwift structure - визуальная проверка",
        "Сверь folders, naming и vertical/horizontal split перед output.",
        "Картинки нужны как контроль структуры, чтобы не смешать work types.",
    ),
    "docs/start/how-to-use.md": (
        "Workflow screenshot - визуальная проверка",
        "Проверь порядок действий: source, takeoff, Excel/output, QA.",
        "Screenshot не заменяет правило; он показывает, где проверить действие в workflow.",
    ),
    "docs/work/horizontal/roof-framing/valley.md": (
        "Valley - визуальная проверка",
        "Проверь inside roof intersection, length и material callout.",
        "Valley не смешивай с Hip: это внутреннее примыкание roof planes.",
    ),
    "docs/work/horizontal/roof-framing/roof-sheathing.md": (
        "Roof Sheathing - визуальная проверка",
        "Сверь roof planes, openings, overhangs и sheathing material/thickness.",
        "Не считай roof sheathing как простую footprint area, если planes/details дают другое.",
    ),
    "docs/work/horizontal/roof-framing/ridge.md": (
        "Ridge - визуальная проверка",
        "Проверь top roof line, support points, size и rounded length.",
        "Ridge length бери по правилу страницы, а не по случайной line на плане.",
    ),
    "docs/work/horizontal/roof-framing/overframes.md": (
        "Overframe - визуальная проверка",
        "Проверь hidden/framed-over roof areas, sleeper condition и sheathing overlap.",
        "Overframes легко пропустить, потому что они часто выглядят как второстепенная roof geometry.",
    ),
    "docs/work/horizontal/roof-framing/hip.md": (
        "Hip - визуальная проверка",
        "Проверь outside roof intersection, length и beam/rafter material.",
        "Hip не смешивай с Valley: это наружный угол roof planes.",
    ),
    "docs/work/horizontal/roof-framing/header.md": (
        "Roof Header - визуальная проверка",
        "Проверь opening/support condition, header size и connected rafters/hangers.",
        "Roof Header часто влияет на hangers и adjacent doubled rafters.",
    ),
    "docs/work/horizontal/roof-framing/dormer.md": (
        "Dormer - визуальная проверка",
        "Проверь dormer walls, roof framing, headers и sheathing scope.",
        "Dormer обычно затрагивает и walls, и roof, поэтому не прячь всё в один item.",
    ),
    "docs/work/horizontal/roof-framing/dbl-trpl-rafters.md": (
        "Double/Triple Rafters - визуальная проверка",
        "Проверь где rafters doubled/tripled, длину и support/hanger condition.",
        "Не считай как обычные rafters, если detail/schedule показывает built-up condition.",
    ),
    "docs/work/horizontal/roof-framing/canopy.md": (
        "Canopy - визуальная проверка",
        "Проверь small roof/canopy frame, attachment и sheathing/trim scope.",
        "Canopy часто отдельный scope: не теряй его внутри main roof.",
    ),
    "docs/work/horizontal/floor-framing/post.md": (
        "Post / Column - визуальная проверка",
        "Проверь post size, height, material и connection to beam/foundation.",
        "Post может быть wood, steel или by others; не угадывай без schedule/detail.",
    ),
    "docs/work/horizontal/floor-framing/beam.md": (
        "Beam - визуальная проверка",
        "Проверь size, ply count, length, bearing и hanger condition.",
        "Если картинка показывает special condition, перенеси его в output row или note.",
    ),
    "docs/work/vertical/openings/windows-doors.md": (
        "Window/Door Opening - визуальная проверка",
        "Проверь schedule, rough opening, header need и exterior-only scope.",
        "Openings не считай по символам вслепую, если schedule даёт размер/material/fire notes.",
    ),
    "docs/work/vertical/walls/unit.md": (
        "Unit Wall - визуальная проверка",
        "Проверь interior/unit wall type, height, thickness и scope boundary.",
        "Unit walls держи отдельно от corridor/demising/exterior walls.",
    ),
    "docs/work/vertical/walls/sill-plates.md": (
        "Sill Plate - визуальная проверка",
        "Проверь PT plate, anchor layout, washers, sill sealer и termite shield.",
        "Sill Plate rules связаны с concrete/foundation, но output может требовать отдельные rows.",
    ),
    "docs/work/vertical/walls/shaft.md": (
        "Shaft Wall - визуальная проверка",
        "Проверь fire/shaft wall type, layers, height и sheathing/gypsum requirements.",
        "Shaft walls не смешивай с обычными demising/unit walls.",
    ),
    "docs/work/vertical/walls/parapet.md": (
        "Parapet Wall - визуальная проверка",
        "Проверь parapet height, material, FRT rule и roof edge condition.",
        "Если exterior wall FRT, parapet/blocking тоже часто должны быть FRT.",
    ),
    "docs/work/vertical/walls/gable.md": (
        "Gable Wall - визуальная проверка",
        "Проверь triangular wall area, height breakpoints, studs/blocking и sheathing.",
        "Gable легко задвоить между wall framing и sheathing; держи scope отдельно.",
    ),
    "docs/work/vertical/walls/exterior.md": (
        "Exterior Wall - визуальная проверка",
        "Проверь wall type, height, sheathing/WRB, FRT и bottom-plate accessories.",
        "Картинка должна подтверждать конкретный layer/scope, а не просто лежать архивом.",
    ),
    "docs/work/vertical/walls/demising.md": (
        "Demising Wall - визуальная проверка",
        "Проверь double wall, fire/acoustic layers, height и side requirements.",
        "Demising не смешивай с Corridor или Unit wall, даже если stud size похож.",
    ),
    "docs/work/vertical/walls/corridor.md": (
        "Corridor Wall - визуальная проверка",
        "Проверь corridor side, double-wall condition, height и fire/sound requirements.",
        "Corridor walls часто отличаются от unit walls по layers и output naming.",
    ),
    "docs/work/vertical/sheathing/wall-sheathing.md": (
        "Wall Sheathing - визуальная проверка",
        "Проверь material/thickness, side, Zip/Densglass/FRT и shear schedule.",
        "Sheathing держи отдельной строкой, если product, side или location важны для review.",
    ),
    "docs/work/vertical/sheathing/truss-heel.md": (
        "Truss Heel - визуальная проверка",
        "Проверь vertical heel area, height и sheathing material.",
        "Truss Heel sheathing не прячь в roof sheathing или wall sheathing без note.",
    ),
    "docs/work/vertical/sheathing/floor.md": (
        "Floor-height Sheathing - визуальная проверка",
        "Проверь floor-height strips, box/full-height condition и supplied scope.",
        "Floor-height sheathing часто относится к COM loose material и требует отдельной строки.",
    ),
}


BLOCK_RE = re.compile(
    r"<!-- confluence-gallery:start -->.*?<!-- confluence-gallery:end -->",
    re.S,
)
ITEM_RE = re.compile(
    r'<a class="kb-gallery__item" href="([^"]+)" title="([^"]*)">\s*'
    r'<img src="([^"]+)" alt="([^"]*)">\s*'
    r'<div class="kb-gallery__caption">([^<]*)</div>\s*'
    r"</a>",
    re.S,
)
SOURCE_ROW_RE = re.compile(
    r"\| ([^|\n]+?) \|\s*([0-9]+)\s*\| \[source\]\(([^)]+)\) \|"
)


def read_head(path: str) -> str | None:
    try:
        data = subprocess.check_output(
            ["git", "show", f"HEAD:{path}"],
            cwd=ROOT,
            stderr=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError:
        return None
    return data.decode("utf-8")


def extract_source_block(path_key: str, current_text: str) -> str | None:
    current_match = BLOCK_RE.search(current_text)
    if current_match and ITEM_RE.search(current_match.group(0)):
        return current_match.group(0)

    head_text = read_head(path_key)
    if head_text:
        head_match = BLOCK_RE.search(head_text)
        if head_match:
            return head_match.group(0)
    return None


def build_block(path_key: str, old_block: str) -> str | None:
    items = ITEM_RE.findall(old_block)
    if not items:
        return None

    topic, rule, note = CONFIGS[path_key]
    sources = SOURCE_ROW_RE.findall(old_block)

    lines = [
        "<!-- confluence-gallery:start -->",
        "## Визуальная проверка",
        "",
        "Эти картинки уже привязаны к правилам страницы. Используй их как быстрые",
        "checkpoint-ы перед output: сначала прочитай правило выше, потом открой нужную",
        "карточку и проверь похожий condition на плане/schedule.",
        "",
    ]

    if sources:
        lines.append('??? info "Источник картинок"')
        for group, count, url in sources:
            lines.append(f"    - {group.strip()}: [{count} карт. Confluence]({url})")
        lines.append("")

    lines.append('<div class="kb-rule-gallery">')
    for index, (href, title_attr, src, _alt, _caption) in enumerate(items, 1):
        card_title = topic if len(items) == 1 else f"{topic} {index:02d}"
        card_alt = f"{card_title}: {rule}"
        lines.extend(
            [
                f'  <a class="kb-rule-card" href="{href}" title="{html.escape(title_attr, quote=True)}">',
                f'    <img src="{src}" alt="{html.escape(card_alt, quote=True)}">',
                '    <div class="kb-rule-card__body">',
                f'      <div class="kb-rule-card__title">{html.escape(card_title, quote=False)}</div>',
                f'      <div class="kb-rule-card__rule">{html.escape(rule, quote=False)}</div>',
                f'      <div class="kb-rule-card__note">{html.escape(note, quote=False)}</div>',
                "    </div>",
                "  </a>",
            ]
        )
    lines.extend(["</div>", "<!-- confluence-gallery:end -->"])
    return "\n".join(lines)


def main() -> None:
    changed: list[str] = []
    for path_key in CONFIGS:
        path = ROOT / path_key
        if not path.exists():
            continue
        current_text = path.read_text(encoding="utf-8-sig")
        source_block = extract_source_block(path_key, current_text)
        if not source_block:
            continue
        new_block = build_block(path_key, source_block)
        if not new_block:
            continue
        new_text, count = BLOCK_RE.subn(new_block, current_text, count=1)
        if count and new_text != current_text:
            path.write_text(new_text, encoding="utf-8", newline="\n")
            changed.append(path_key)

    print(f"updated={len(changed)}")
    for path_key in changed:
        print(path_key)


if __name__ == "__main__":
    main()
