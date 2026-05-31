# Unit / Interior Walls

## Что считать

- Interior apartment walls по type и height.
- Studs, plates, blocking и openings, если не panelized / by others.
- Jamb blocking для interior doors.

## Правила

- Typical unit walls — 2x4, но structural schedules могут override.
- Exact stud heights важны на больших COM jobs.
- Не включай gypsum для normal wall faces, если scope прямо не просит.
- Interior walls разделяй by floor, когда plans отдельно показывают basement,
  first floor, second floor, attic/loft, chimney, dormer или garage conditions.

## Проверить

- Kitchen blocking: 2x6, 4 pieces of 14' per kitchen.
- Bath blocking: 2x6, 1 piece of 14' per bathroom.
- Tile base в room schedules исключается, когда нужен только wood base.
- Studs PreCut должен быть видим на left/output side, если этого требует Tilda
  checklist.
- Сначала смотри на спецификацию стен — **из металла или из дерева** делаются интерьерные стены.
- Если в notes написано **`walls are panels`** — НЕ считаем (панели поставляются отдельно).
- Если unit interior walls — metal studs, проверь spacing. Не переноси
  `24" o.c.`, если notes/spec требуют `16" o.c.`.
- Metal-stud door jambs inside units должны совпадать с metal-stud wall size
  (`2x4` или `2x6`), а не generic jamb.

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

<figure markdown>
  ![Unit walls marked A 2x4 / A 2x6 in PlanSwift](../../../assets/images/confluence/confluence-095.png)
  <figcaption>Так это выглядит в PlanSwift: только interior-стены юнита, <span style="color:#c0392b">A 2x4 (красный)</span> и <span style="color:#2e7d32">A 2x6 (зелёный)</span>. Внешние стены не входят. Снизу — длины (58.7 / 3.1 ft) как в выгрузке выше.</figcaption>
</figure>

### Учёт повторов юнитов

На общем плане этажа отметь, **сколько раз встречается каждый unit** (A, B, C…). Это нужно для последующего подсчёта в Excel через макрос **`C_UnitTable`** — он умножает длину стен юнита на количество повторов.

Используй чёткие имена групп (например, `Unit A — A 2x4`) — так удобнее экспортировать и анализировать.

## See also

- [Corridor Walls](corridor.md) · [Demising Walls](demising.md) · [Windows & Doors](../openings/windows-doors.md) · [Формулы → Stud factors](../../../reference/formulas.md#stud-spacing-factors)
