# OurPlaneCore

OurPlaneCore — локальная программа для takeoff по PDF drawings. Она собирает
страницы, PDF layers, измерения, takeoff tree, estimating rows и export в одном
окне, чтобы не прыгать между PlanSwift, Excel и ручными заметками.

!!! note "Статус"
    Это рабочая внутренняя программа, а не публичный SaaS. Скриншоты ниже
    redacted: job name, sheet names и реальные takeoff names специально скрыты.

<figure markdown>
  ![OurPlaneCore main workspace](../assets/images/ourplanecore/ourplanecore-main-view-redacted.png)
  <figcaption>Main View: PDF viewport, Pages tree слева, Takeoffs tree справа, tools снизу.</figcaption>
</figure>

## Что уже делает

<div class="grid cards" markdown>

-   :material-file-pdf-box: **PDF workspace**

    ---

    Открывает job, показывает PDF sheet, page folders, PDF layers, page setup,
    active sheet tabs и overlay/takeoff visibility.

-   :material-ruler-square: **Takeoff tools**

    ---

    Есть `Count`, `Line`, `Area`, `J Area`, `Ruler`, `Box`, `Cut`, `Record`,
    `Snap`, `PDF Snap`, `Ortho`, rotate/flip и scale controls.

-   :material-vector-line: **PDF Snap**

    ---

    Отдельный режим snap по vector PDF geometry: corners, points, line segments
    на sheet и overlay PDF. Raster/scan PDF пока требует отдельной логики.

-   :material-folder-tree: **Pages / Takeoffs tree**

    ---

    Pages tree хранит sheets/folders/layers. Takeoffs tree хранит folders,
    items, sections, quantities и active record target.

-   :material-table-edit: **Sheet Manager**

    ---

    Проверяет Auto Name, Auto Scale, confidence, source и warnings перед тем,
    как применять имена/scale к sheets.

-   :material-microsoft-excel: **Export**

    ---

    Есть CSV/TXT/Excel export и `Current Excel`: запись выбранного takeoff
    прямо в уже открытый workbook от active cell.

</div>

## Основной workflow

1. Открыть job и импортировать PDF.
2. В `Sheet Manager` проверить `Auto Name`, `Auto Scale`, warnings и применить
   только checked rows.
3. Разложить sheets по folders через `Auto Folders`, `Sort A/S`, `D/Sec/WT`.
4. На `Main View` включить нужные PDF layers / overlay, выставить scale и
   открыть нужный sheet.
5. Создать folder/item в `Takeoffs tree`, включить `Record`, выполнить takeoff.
6. Проверить totals в `Takeoffs` / `Estimating` / `Takeoff Manager`.
7. Экспортировать в CSV/TXT/Excel или отправить selected rows в `Current Excel`.

## Main View

Main View — рабочий экран для измерений.

| Зона | Для чего |
| --- | --- |
| `Pages tree` | Sheet folders, imported pages, PDF layers, page setup, repair links |
| `PDF viewport` | Pan/zoom, measurements, labels, legends, snap, scale, overlay |
| `Takeoffs tree` | Folders/items/sections, active target, record area, estimating tab |
| Bottom toolbar | Tools: `Pan`, `Select`, `Scale`, `Count`, `Line`, `Area`, `J Area`, `PDF Snap`, `Ortho` |

!!! tip "Практическое правило"
    Если ты рисуешь новый takeoff, сначала выбери item справа и включи
    `Record`. Если нужно просто двигать/проверять уже нарисованное — используй
    `Select`.

## Sheet Manager

<figure markdown>
  ![OurPlaneCore Sheet Manager](../assets/images/ourplanecore/ourplanecore-sheet-manager-redacted.png)
  <figcaption>Sheet Manager: review table для Auto Name / Auto Scale перед применением.</figcaption>
</figure>

`Sheet Manager` нужен, чтобы не применять auto-renaming вслепую.

| Колонка / кнопка | Что проверять |
| --- | --- |
| `Proposed Name` | Sheet label из PDF text, title block или manual source |
| `Scale` | Parsed scale, например `1/8" = 1'0"` |
| `Confidence` | Насколько уверенно программа нашла name/scale |
| `Why` | Почему предложено именно это имя/scale |
| `Warnings` | Sheet label missing, title not found, duplicate/same name, no usable scale |
| `Apply Checked` | Применять только строки, которые проверены |
| `Open JSON` | Открыть sheet metadata для диагностики |

## Takeoff Manager

<figure markdown>
  ![OurPlaneCore Takeoff Manager](../assets/images/ourplanecore/ourplanecore-takeoff-manager-redacted.png)
  <figcaption>Takeoff Manager: таблица items, totals, units, notes, folders и export commands.</figcaption>
</figure>

`Takeoff Manager` показывает job-level takeoffs в табличном виде.

| Поле | Что значит |
| --- | --- |
| `Item` | Название takeoff item |
| `Type` | `Count`, `Line`, `Area`, `Joist` |
| `Sections` | Сколько measurement sections у item |
| `Total` | Итоговая quantity по item |
| `Unit` | `ea`, `ft`, `sf` и т.д. |
| `Price / Cost` | Место для estimating values |
| `Notes` | Видимые notes по item |
| `Folder` | Полный путь item внутри takeoff tree |

## Joist Area

`J Area` — shortcut для joist layout. Он создаёт Area takeoff, включает joist
settings и сразу запускает area record.

- Direction задаётся отдельной линией по joist direction.
- Joists clipped внутри polygon.
- Quantity может считаться как total joist length + piece count.
- Spacing, rounding и label behavior задаются в item properties.

## Report Builder

`Report Builder` — отдельный workspace для будущего Excel-like report surface.
Он читает template workbook `TemplateCom.xlsm`, показывает rows/columns как
рабочую таблицу и постепенно связывает takeoff source rows с Excel output
blocks.

Сейчас важный статус: export commands не сломаны, `Report Builder` отдельный
от CSV/TXT/Excel export.

## Что пока помнить

- `PDF Snap` работает по vector PDF geometry. Если sheet — scan/raster, там
  может не быть PDF lines/corners для snap.
- Auto Name / Auto Scale надо проверять в `Sheet Manager`, не применять весь
  список без просмотра warnings.
- `Current Excel` пишет в active workbook/active cell и не auto-save workbook.
- Сначала делаем checked/reviewed workflow, потом automation. Это важнее, чем
  скрытая “магия”.

## Быстрые ссылки внутри wiki

- [Workflow](workflow.md)
- [Структура takeoff](takeoff-structure.md)
- [QA checklist](quality-checklist.md)
- [Как пользоваться wiki](how-to-use.md)
