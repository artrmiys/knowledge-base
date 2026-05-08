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
- Сначала смотри на спецификацию стен — **из металла или из дерева** делаются интерьерные стены.
- Если в notes написано **`walls are panels`** — НЕ считаем (панели поставляются отдельно).
- If unit interior walls are metal studs, verify the spacing. Do not carry
  `24" o.c.` forward if the notes/spec require `16" o.c.`.
- Metal-stud door jambs inside units should match the metal-stud wall size
  (`2x4` or `2x6`) instead of using a generic jamb.

## Разметка по юнитам в PlanSwift (A 2x4 / A 2x6)

Когда здание состоит из юнитов (units), каждый юнит размечается **отдельно**.

1. В PlanSwift создаётся отдельная **папка `units`**.
2. Внутри каждого юнита добавляются типы стен по толщине доски:
    - **`A 2x4`** — интерьерная стена 2x4 (буква-префикс = код юнита, например `A`, `Q`, `SK`).
    - **`A 2x6`** — интерьерная стена 2x6.
3. На плане линия чертится вдоль стены по её толщине:
    - **~3½"** на плане → `A 2x4`.
    - **~5½"** на плане → `A 2x6`.
4. Каждая стена должна относиться **только к одному юниту**. Внешние стены НЕ включаются — только interior.

### Пример выгрузки в Takeoff

```
Unit A
  – A 2x4: 58.7 ft
  – A 2x6: 3.1 ft
```

### Учёт повторов юнитов

На общем плане этажа отметь, **сколько раз встречается каждый unit** (A, B, C…). Это нужно для последующего подсчёта в Excel через макрос **`C_UnitTable`** — он умножает длину стен юнита на количество повторов.

Используй чёткие имена групп (например, `Unit A — A 2x4`) — так удобнее экспортировать и анализировать.

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
