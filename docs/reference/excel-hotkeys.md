# Excel macro hotkeys

Это не стандартные shortcuts Excel. Это наши hotkeys для VBA/macros в рабочем
Excel workbook/template после PlanSwift output и ручного cleanup.

<figure markdown>
  ![Excel macro hotkeys map](../assets/images/reference/excel-hotkeys-map.svg)
  <figcaption>Excel macro hotkeys - что запускать после PlanSwift и перед check/output.</figcaption>
</figure>

!!! warning "Важно"
    Эти hotkeys работают только там, где подключены нужные macros. Если shortcut
    ничего не делает, проверь active workbook, включены ли macros, и не занят ли
    shortcut самим Excel/Windows.

## Macro hotkeys

| Hotkey | Macro / действие | Что делает |
| --- | --- | --- |
| <kbd>Ctrl</kbd>+<kbd>Q</kbd> | Delete selected cells | Удалить выделенные ячейки со сдвигом вверх. |
| <kbd>Ctrl</kbd>+<kbd>W</kbd> | Add selected cells | Добавить выделенные ячейки со сдвигом вверх. |
| <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>B</kbd> | Format Beams | Форматирование Beams после PlanSwift. |
| <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>J</kbd> | Format Joists | Форматирование Joists после PlanSwift. |
| <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>R</kbd> | Format Details | Форматирование Details после PlanSwift. |
| <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>F</kbd> | Sum same values | Суммирование одинаковых значений. |
| <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>W</kbd> | Write wall values | Запись значений стен в форму. |
| <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>Q</kbd> | Write area values | Запись значений площади в форму. |
| <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>K</kbd> / <kbd>К</kbd> | Insert detail rows left | Вставка в левую часть строк с деталями. |
| <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>L</kbd> | Add bolts block | Добавление блока с bolts со сдвигом вниз. |
| <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>T</kbd> | Check Spelling | Проверка орфографии. |
| <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>O</kbd> | Date | Выставить дату. |
| <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>V</kbd> | Validation cleanup | Убрать выпадающие списки. |
| <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>D</kbd> | Delete grey cells | Удалить grey cells. |
| <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>N</kbd> | Write to check | Записать в check. |
| <kbd>Ctrl</kbd>+<kbd>M</kbd> | Multiply all | Умножить всё, что есть в ячейке. |
| <kbd>Ctrl</kbd>+<kbd>E</kbd> | Delete 0 rows | Удалить строки, где в column `C` значение `0`. |
| <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>I</kbd> | Insert note | Чтобы вставить заметку, напиши `Note: text` и нажми shortcut. Работает только если в тексте есть слово `Note`. |

## По задачам

| Задача | Hotkeys |
| --- | --- |
| Cleanup cells / rows | <kbd>Ctrl</kbd>+<kbd>Q</kbd>, <kbd>Ctrl</kbd>+<kbd>W</kbd>, <kbd>Ctrl</kbd>+<kbd>E</kbd>, <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>D</kbd> |
| PlanSwift formatting | <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>B</kbd>, <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>J</kbd>, <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>R</kbd> |
| Forms / output write | <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>W</kbd>, <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>Q</kbd>, <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>N</kbd> |
| Helpers | <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>F</kbd>, <kbd>Ctrl</kbd>+<kbd>M</kbd>, <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>I</kbd> |
| Workbook finish | <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>O</kbd>, <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>T</kbd>, <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>V</kbd> |

## Быстрый порядок после PlanSwift

1. Выбери правильный output sheet и range.
2. Запусти formatting macro: Beams / Joists / Details.
3. Удали мусор: grey cells, zero rows, лишние validation dropdowns.
4. Запиши стены или площади в форму, если это часть workbook workflow.
5. Поставь дату, check spelling, затем write to check.

## Обычные Excel shortcuts

Для обычных встроенных shortcuts Excel смотри официальный список Microsoft:
[Keyboard shortcuts in Excel](https://support.microsoft.com/en-gb/office/keyboard-shortcuts-in-excel-1798d9d5-842a-42b8-9c99-9b7213f0040f).

## See also

- [Formulas and factors](formulas.md)
- [Quality checklist](../start/quality-checklist.md)
- [Workflow](../start/workflow.md)
