# Unit / Interior Walls

## Count

- Interior apartment walls by type and height.
- Studs, plates, blocking, and openings unless panelized or by others.
- Jamb blocking for interior doors.

## Rules

- Typical unit walls are 2x4, but structural schedules can override this.
- Exact stud heights matter on large COM jobs.
- Do not include gypsum for normal wall faces unless scope specifically asks.
- Split interior walls by floor when plans separate basement, first floor,
  second floor, attic/loft, chimney, dormer, or garage conditions.

## Check

- Kitchen blocking: 2x6, 4 pieces of 14' per kitchen.
- Bath blocking: 2x6, 1 piece of 14' per bathroom.
- Tile base in room schedules should be excluded when only wood base is needed.
- Studs PreCut should be visible on the left/output side when the Tilda checklist
  calls for it.

<!-- confluence-context:start -->
## Confluence Context

Эта секция показывает, какие Confluence-страницы питают эту wiki-страницу и какие соседние темы связаны с ней через исходники.

| Source | Role here | Images | Raw MD |
| --- | --- | ---: | --- |
| [Unit (внутрикомнатные стены)](https://ewood.atlassian.net/wiki/spaces/work/pages/65077308/Unit) | content + images | 1 | `imports/live-sources/confluence-work/pages/01-65077308-unit-внутрикомнатные-стены.md`<br>`imports/live-sources/confluence-work-images/pages/01-65077308-unit-внутрикомнатные-стены.md` |
| [Units](https://ewood.atlassian.net/spaces/work/pages/58916937/Units) | content | 0 | `imports/live-sources/confluence-work/pages/01-58916937-units.md` |

### Related Wiki Pages

| Wiki page | Why it is connected |
| --- | --- |
| [reference/source-map.md](../../../reference/source-map.md) | linked from `Unit (внутрикомнатные стены)` |
| [start/takeoff-structure.md](../../../start/takeoff-structure.md) | linked from `Unit (внутрикомнатные стены)` |
| [work/horizontal/floor-framing/joist.md](../../horizontal/floor-framing/joist.md) | linked from `Unit (внутрикомнатные стены)` |
| [work/vertical/walls/exterior.md](exterior.md) | linked from `Unit (внутрикомнатные стены)` |
| [work/vertical/walls/sill-plates.md](sill-plates.md) | linked from `Unit (внутрикомнатные стены)` |

### Source Notes

??? note "Units"
    Source: `https://ewood.atlassian.net/spaces/work/pages/58916937/Units`
    Updated in Confluence: `2025-05-24T22:28:01.787Z`

    - _No text extracted._

??? note "Unit (внутрикомнатные стены)"
    Source: `https://ewood.atlassian.net/wiki/spaces/work/pages/65077308/Unit`
    Updated in Confluence: `июн. 25, 2025`

    - 2
    - смотреть сделаны стены из металла или нет, подписаны на спецификации стен
    - Разметка интерьерных стен по юнитам (A 2x4 / A 2x6)
    - Когда здание состоит из юнитов (units):
    - Каждый юнит размечается отдельно.
    - В PlanSwift создается отдельная папка units
    - Если есть указание walls are panels - НЕ считаем
    - Внутри каждого юнита добавляются типы стен:
    - A 2x4 — интерьерная стена из доски 2x4
    - A 2x6 — интерьерная стена из доски 2x6
    - (буква "A"  указывает на тип interior walls, возможны различные варианты: Q 2x4, SK 2x6 - только краткое обозначение unit, и типа стены)
    - если указана стены ниже
    - Разметка на плане:
    - Линия чертится вдоль стены, соответствующей толщине:
    - – ~3½" → A 2x4
    - – ~5½" → A 2x6
    - Каждая стена должна относиться только к одному юниту.
    - Внешние стены не включаются — только интерьер.
    - Пример итогового подсчёта в Takeoff:
    - Unit A
    - – A 2x4: 58,7 ft
    - – A 2x6: 3,1 ft
    - Примечание:
    - Использовать чёткие имена групп (например: Unit A — A 2x4) удобно при экспорте и в дальнейшем анализе.
    - На общем плане этажа отметить каждый unit, чтобы узнать как часто каждый встречается на плане.
    - В дальнейшем это будет необходимо для подсчета в excel, с помощью макроса: C_UnitTable

<!-- confluence-context:end -->

<!-- confluence-gallery:start -->
## Confluence Images

Изображения из Confluence размещены на этой странице по исходной теме.
Подпись сохраняет группу-источник, чтобы можно было быстро проверить контекст.

| Source group | Images | Confluence |
| --- | ---: | --- |
| Unit (внутрикомнатные стены) | 1 | [source](https://ewood.atlassian.net/wiki/spaces/work/pages/65077308/Unit) |

<div class="kb-gallery">
  <a class="kb-gallery__item" href="../../../../assets/images/confluence/confluence-095.png" title="image-20250623-135522.png">
    <img src="../../../../assets/images/confluence/confluence-095.png" alt="Unit (внутрикомнатные стены) - unit/interior wall reference 01">
    <div class="kb-gallery__caption">unit/interior wall reference 01 (image, 50 KB raw)</div>
  </a>
</div>
<!-- confluence-gallery:end -->
