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

## Стандартные Excel shortcuts { .kb-section-title .kb-st--amber }

Для встроенных Excel shortcuts — официальный список Microsoft:
[Keyboard shortcuts in Excel](https://support.microsoft.com/en-gb/office/keyboard-shortcuts-in-excel-1798d9d5-842a-42b8-9c99-9b7213f0040f).

## See also

- [Formulas and factors](formulas.md)
- [Quality checklist](../start/quality-checklist.md)
- [Workflow](../start/workflow.md)
