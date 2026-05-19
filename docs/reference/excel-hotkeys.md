# Excel macro hotkeys

Это не стандартные Excel shortcuts. Это **VBA-macros**, подключённые к рабочему
workbook'у — для очистки, форматирования и записи после PlanSwift output.

!!! warning "Макросы должны быть включены"
    Если shortcut ничего не делает — проверь:
    1. Активный workbook содержит нужные macros.
    2. Macros включены (`File → Options → Trust Center → Macro Settings`).
    3. Shortcut не перехвачен Excel/Windows.

## По этапам workflow { .kb-section-title .kb-st--cyan }

<div class="grid cards kb-hotkey-cards" markdown>

-   :material-broom:{ .lg .middle .kb-mk--cyan } **Cleanup**

    ---

    | Hotkey | Действие |
    | --- | --- |
    | ++ctrl+q++ | Удалить ячейки (сдвиг вверх) |
    | ++ctrl+w++ | Вставить ячейки (сдвиг вверх) |
    | ++ctrl+e++ | Удалить строки, где column `C` = `0` |
    | ++ctrl+shift+d++ | Удалить grey cells |
    | ++ctrl+shift+v++ | Убрать validation dropdowns |

-   :material-format-list-bulleted-square:{ .lg .middle .kb-mk--magenta } **PlanSwift formatting**

    ---

    | Hotkey | Действие |
    | --- | --- |
    | ++ctrl+shift+b++ | Format **Beams** |
    | ++ctrl+shift+j++ | Format **Joists** |
    | ++ctrl+shift+r++ | Format **Details** |

-   :material-content-save-edit-outline:{ .lg .middle .kb-mk--amber } **Forms / output write**

    ---

    | Hotkey | Действие |
    | --- | --- |
    | ++ctrl+shift+w++ | Записать значения **walls** в форму |
    | ++ctrl+shift+q++ | Записать значения **area** в форму |
    | ++ctrl+shift+n++ | Write to **check** |

-   :material-tools:{ .lg .middle .kb-mk--green } **Helpers**

    ---

    | Hotkey | Действие |
    | --- | --- |
    | ++ctrl+shift+f++ | Суммировать одинаковые значения |
    | ++ctrl+m++ | Умножить всё в ячейке |
    | ++ctrl+shift+i++ | Вставить note (текст должен начинаться со слова `Note`) |
    | ++ctrl+shift+k++ | Вставить detail-строки слева |
    | ++ctrl+shift+l++ | Добавить блок **bolts** (сдвиг вниз) |

-   :material-check-decagram-outline:{ .lg .middle .kb-mk--blue } **Workbook finish**

    ---

    | Hotkey | Действие |
    | --- | --- |
    | ++ctrl+shift+o++ | Поставить дату |
    | ++ctrl+shift+t++ | Check Spelling |
    | ++ctrl+shift+v++ | Validation cleanup |

</div>

## Быстрый порядок после PlanSwift { .kb-section-title .kb-st--magenta }

1. Выбери правильный output sheet и range.
2. Запусти formatting: ++ctrl+shift+b++ Beams → ++ctrl+shift+j++ Joists → ++ctrl+shift+r++ Details.
3. Чисти мусор: ++ctrl+shift+d++ grey cells, ++ctrl+e++ zero rows, ++ctrl+shift+v++ validation dropdowns.
4. Запиши в форму: ++ctrl+shift+w++ walls / ++ctrl+shift+q++ area, если это часть workbook workflow.
5. Финал: ++ctrl+shift+o++ дата → ++ctrl+shift+t++ spell check → ++ctrl+shift+n++ write to check.

## Calc pipeline (A-series) { .kb-section-title .kb-st--cyan }

Расчётные макросы — запускаются по выделенному range, по порядку. Не имеют
Ctrl-хоткеев: запускай кнопкой или `Alt+F8`.

| Макрос | Что делает |
| --- | --- |
| `A1_UnitTable` | строит unit-таблицу из выделения |
| `A2_SQFT_calc` | SQFT + gable / truss heel |
| `A3_Walls_Calc_AllGroup` / `_OneGroup` | walls: все группы / одна группа |
| `A4_Parapet` (+ `X_ClearParapetTable`) | parapet walls |
| `A5_Openings` | openings calc |
| `A6_Eve_Rakes` | eve / rakes |
| `A7_wall_sheathing` | по тексту в `J`: Zip → удалить Ply/OSB/CDX+Tyvek (пишет в `O5`); Ply/OSB/CDX → удалить Zip+Zip Tape (пишет в `O3`) |
| `A8_SplitWallSuffixes_ByJ` | делит выделенные строки `J:L` на base-список (имена walls для A3) и список suffix/detail notes |
| `wall_panel` | wall panel расчёт |
| `Fame_only` | удаляет finish/trim-блоки, оставляет **только frame** (A:H, сдвиг вверх) |
| `Y_Run_First6` | один запуск всей цепочки `A1…A6` (toggle-константы внутри; `A1` идёт последним для безопасности — он перестраивает выделенный range) |
| `C_HeadersSort` | сортировка/раскладка headers (как `C_BeamsSort`/`C_JoistsSort`; J-mode + legend-строки `H5 - (2) 2x10`) |
| `C_RimBoardBlockingHangers` | rim board + blocking + hangers одним блоком |

!!! tip "Порядок"
    `A1` чистит/перестраивает выделение, поэтому `A2…A6` читают исходное
    выделение **до** `A1`. `Y_Run_First6` это уже учитывает. Вручную —
    запускай `A2…A6`, затем `A1`.

## Новые insert-хелперы { .kb-section-title .kb-st--green }

| Макрос | Действие |
| --- | --- |
| `B_FrameOC_InsertOneRow` | вставляет одну frame-OC строку под выделенной |
| `B_Plate2_InsertOneRow` | вставляет одну Plate2-строку под выделенной |
| `Y_add_2400V48` | по 2-колоночному лук-апу проставляет `2400 V48` note-значения |
| `B_Balcony_Insert_Template_FromText` | полный balcony-каркас по `b 12x30` |

Полное описание trim/frame insert-блоков —
[Trim macros](../work/exterior-trims/macros.md) и
[Deck / Porch / Balcony Frame](../work/deck/deck-porch-balcony-frame.md).

## Section navigation (Ctrl / Alt + F) { .kb-section-title .kb-st--blue }

`BindNavHotkeys` (Workbook_Open) вешает прыжки по section-заголовкам. Это
быстрый способ скакать по большому output-листу.

<div class="grid cards kb-hotkey-cards" markdown>

-   :material-arrow-down-bold-box:{ .lg .middle .kb-mk--cyan } **Ctrl + F — Walls**

    ---

    | Hotkey | Section |
    | --- | --- |
    | ++ctrl+f1++ … ++ctrl+f5++ | 1st … 5th Floor Walls |
    | ++ctrl+f6++ / ++ctrl+f7++ | Gable Walls #1 / #2 |
    | ++ctrl+f8++ | Parapet Walls |
    | ++ctrl+f9++ | Wall Materials |
    | ++ctrl+f11++ / ++ctrl+f12++ | Foundation / Basement Floor Walls |

-   :material-arrow-down-bold-box-outline:{ .lg .middle .kb-mk--magenta } **Alt + F — Framing / roof**

    ---

    | Hotkey | Section |
    | --- | --- |
    | ++alt+f1++ … ++alt+f4++ | 1st … 4th Floor Framing List |
    | ++alt+f5++ | Loft Framing List |
    | ++alt+f6++ / ++alt+f7++ | Roof Frame list / Roof System Misc |
    | ++alt+f10++ | Roof Products |
    | ++alt+f11++ / ++alt+f12++ | Soffits and Fascias / Exterior Trims |

-   :material-arrow-down-bold-box:{ .lg .middle .kb-mk--green } **Alt + Shift + F**

    ---

    | Hotkey | Section |
    | --- | --- |
    | ++alt+shift+f1++ | Interior Doors&Trims |
    | ++alt+shift+f2++ | Drywall & Insulation |
    | ++alt+shift+f8++ | Balcony (по заливке #99CC00/#FABF8F) |
    | ++alt+shift+f9++ | Porch (по заливке #99CC00/#FABF8F) |

</div>

!!! warning "Не работает — проверь"
    Nav-хоткеи вешает `Workbook_Open`. Если не прыгает: workbook с макросами
    открыт, macros enabled, и заголовок section написан точно (`1st Floor
    Walls`, `Exterior Trims` и т.д.). `Z_Dont_use_Run_ByPriority` —
    устаревший, не использовать.

## Стандартные Excel shortcuts { .kb-section-title .kb-st--amber }

Для встроенных Excel shortcuts — официальный список Microsoft:
[Keyboard shortcuts in Excel](https://support.microsoft.com/en-gb/office/keyboard-shortcuts-in-excel-1798d9d5-842a-42b8-9c99-9b7213f0040f).

## See also

- [Trim macros](../work/exterior-trims/macros.md) — `C_TrimsCalc`, jamb / pavers / balcony insert
- [Deck / Porch / Balcony Frame](../work/deck/deck-porch-balcony-frame.md) — frame insert / sort макросы
- [Formulas and factors](formulas.md)
- [Quality checklist](../start/quality-checklist.md)
- [Workflow](../start/workflow.md)
