# Все функции программы

Страница собирается из кода программы скриптом tools/opc_inventory.py; не править руками.

Здесь перечислена каждая кнопка, пункт меню, клавиша, категория Settings и окно OurPlanCore 3.0, по месту в интерфейсе. Колонка "Подробно" ведёт на страницу раздела, где функция описана; пустая ячейка значит, что подробного описания в базе пока нет (проверка: `python tools/opc_coverage.py`). Одна и та же функция часто доступна с нескольких поверхностей (лента, меню, палитра, клавиша), поэтому повторы здесь нормальны.

Всего записей: 1089. С подробной страницей: 973. Пока без страницы: 0. Служебных и повторов, исключённых из проверки: 116.

## Нижняя полоса инструментов (40)

??? note "нижняя полоса, строка 1 (31)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Value` |  | нижняя полоса: нижняя полоса, строка 1 | Write only values for the same selected takeoff scope into one Excel column | [Инструменты замера](ourplancore-tools.md) |
    | `Excel` |  | нижняя полоса: нижняя полоса, строка 1 | Write the selected takeoff folder/item to the active cell in an already open Excel workbook | [Экспорт в Excel](ourplancore-excel.md) |
    | `Include takeoff comments in Excel export` |  | нижняя полоса: нижняя полоса, строка 1 | Include takeoff and measurement comments in Excel exports (filled = on; default = off) | [Экспорт в Excel](ourplancore-excel.md) |
    | `Pan` | `V` | нижняя полоса: нижняя полоса, строка 1 | Pan (V) | [Инструменты замера](ourplancore-tools.md) |
    | `Select` | `E` | нижняя полоса: нижняя полоса, строка 1 | Box select measurements (E). Ctrl+C copy, Ctrl+V paste | [Инструменты замера](ourplancore-tools.md) |
    | `Scale` | `S` | нижняя полоса: нижняя полоса, строка 1 | Set scale (S) | [Инструменты замера](ourplancore-tools.md) |
    | `Ruler` | `R` | нижняя полоса: нижняя полоса, строка 1 | Place a dimension/ruler markup on the PDF (R) | [Инструменты замера](ourplancore-tools.md) |
    | `Ruler Sheet Visibility` |  | нижняя полоса: нижняя полоса, строка 1 | Hide all ruler markups on this sheet | [Инструменты замера](ourplancore-tools.md) |
    | `Pitch` |  | нижняя полоса: нижняя полоса, строка 1 | Draw two points and show roof pitch as rise:12 | [Инструменты замера](ourplancore-tools.md) |
    | `Count` | `P` | нижняя полоса: нижняя полоса, строка 1 | Create a new Count item and start recording (P). Use the active target Record button to continue an existing item | [Инструменты замера](ourplancore-tools.md) |
    | `Similar` |  | нижняя полоса: нижняя полоса, строка 1 | Find similar symbols on this sheet, name the result, and add reviewed markers as a Count item | [Инструменты замера](ourplancore-tools.md) |
    | `P Line` |  | нижняя полоса: нижняя полоса, строка 1 | Create Count points along selected Line measurement(s) with a spacing | [Инструменты замера](ourplancore-tools.md) |
    | `Break` |  | нижняя полоса: нижняя полоса, строка 1 | Break selected Lines into separate one-segment measurements. The measured total does not change; Ctrl+Z restores them. Ctrl+Shift+B: Break, Ctrl+Shift+V: Break H/V | [Правка и привязки](ourplancore-editing.md) |
    | `Break H/V` |  | нижняя полоса: нижняя полоса, строка 1 | Break H/V: file horizontal and vertical segments into two new takeoffs (filled = on). Ctrl+Shift+V runs Break H/V directly | [Правка и привязки](ourplancore-editing.md) |
    | `Ends` |  | нижняя полоса: нижняя полоса, строка 1 | Place Count marks on both ends of every selected Line segment. Works on the sheet selection, or on one or more Line takeoffs selected in the Takeoffs tree | [Правка и привязки](ourplancore-editing.md) |
    | `Default Count display for newly created Count takeoffs` |  | нижняя полоса: нижняя полоса, строка 1 | Default Count display for newly created Count takeoffs |  |
    | `Line` | `L` | нижняя полоса: нижняя полоса, строка 1 | Create a new Line item and start recording (L). Use the active target Record button to continue an existing item | [Инструменты замера](ourplancore-tools.md) |
    | `Repeat Line` |  | нижняя полоса: нижняя полоса, строка 1 | Repeat Line: create a Line item, then draw separate two-point segments. Esc stops. | [Правка и привязки](ourplancore-editing.md) |
    | `Area` | `A` | нижняя полоса: нижняя полоса, строка 1 | Create a new Area item and start recording (A). Use the active target Record button to continue an existing item | [Инструменты замера](ourplancore-tools.md) |
    | `J Area` | `J` | нижняя полоса: нижняя полоса, строка 1 | Create a new Joist Area item and start recording (J) | [Инструменты замера](ourplancore-tools.md) |
    | `Beam` | `B` | нижняя полоса: нижняя полоса, строка 1 | Measure a beam length, create a Count item, and place the first Count mark (B) | [Инструменты замера](ourplancore-tools.md) |
    | `Repeat Beam` |  | нижняя полоса: нижняя полоса, строка 1 | Repeat Beam: measure and create each Beam, then draw the next. Esc stops. | [Правка и привязки](ourplancore-editing.md) |
    | `Open` | `O` | нижняя полоса: нижняя полоса, строка 1 | Measure an opening box, create a Count item, and place the Count mark in the center (O) | [Инструменты замера](ourplancore-tools.md) |
    | `Cut` | `X` | нижняя полоса: нижняя полоса, строка 1 | Cut Area holes or erase Line pieces (X, F9 toggles box) | [Правка и привязки](ourplancore-editing.md) |
    | `Merge` | `Ctrl+M` | нижняя полоса: нижняя полоса, строка 1 | Merge selected Takeoffs from all sheets, or selected measurement segments (Ctrl+M) | [Правка и привязки](ourplancore-editing.md) |
    | `Split` | `Ctrl+Shift+M` | нижняя полоса: нижняя полоса, строка 1 | Split whole Takeoffs across all sheets, or selected measurements or Count marks (Ctrl+Shift+M) | [Правка и привязки](ourplancore-editing.md) |
    | `Combine` |  | нижняя полоса: нижняя полоса, строка 1 | Boolean-combine two or more selected Areas: union, subtract, intersect, remove overlap, divide | [Правка и привязки](ourplancore-editing.md) |
    | `Snap` | `F3` | нижняя полоса: нижняя полоса, строка 1 | Snap to existing takeoff points (F3) | [Привязки и трассировка](ourplancore-snap-trace.md) |
    | `PDF` | `Ctrl+F3` | нижняя полоса: нижняя полоса, строка 1 | Snap to PDF vector corners and points (Ctrl+F3) | [Инструменты замера](ourplancore-tools.md) |
    | `Ortho` | `F8` | нижняя полоса: нижняя полоса, строка 1 | Lock drawing and editing horizontally/vertically (F8; Shift temporarily forces Ortho) | [Привязки и трассировка](ourplancore-snap-trace.md) |
    | `Box` | `F9` | нижняя полоса: нижняя полоса, строка 1 | Draw Line/Area measurements by two opposite box corners (F9) | [Инструменты замера](ourplancore-tools.md) |

??? note "нижняя полоса, строка 2 (9)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Flip H` |  | нижняя полоса: нижняя полоса, строка 2 | Mirror selected measurements/markups horizontally | [Правка и привязки](ourplancore-editing.md) |
    | `Flip V` |  | нижняя полоса: нижняя полоса, строка 2 | Mirror selected measurements/markups vertically | [Правка и привязки](ourplancore-editing.md) |
    | `Reset Rotate Selection` |  | нижняя полоса: нижняя полоса, строка 2 | Center rotate slider for another relative adjustment | [Инструменты замера](ourplancore-tools.md) |
    | `Set` |  | нижняя полоса: нижняя полоса, строка 2 | Apply scale | [Инструменты замера](ourplancore-tools.md) |
    | `Presets` |  | нижняя полоса: нижняя полоса, строка 2 | Common scale presets | [Инструменты замера](ourplancore-tools.md) |
    | `AI Settings` |  | нижняя полоса: нижняя полоса, строка 2 | OpenAI key status and model settings | [ИИ и терминалы](ourplancore-ai.md) |
    | `Fit page` | `F` | нижняя полоса: нижняя полоса, строка 2 | Fit page (F) | [Инструменты замера](ourplancore-tools.md) |
    | `Zoom in` | `Ctrl++` | нижняя полоса: нижняя полоса, строка 2 | Zoom in (Ctrl++) | [Горячие клавиши](ourplancore-shortcuts.md) |
    | `Zoom out` | `Ctrl+-` | нижняя полоса: нижняя полоса, строка 2 | Zoom out (Ctrl+-) | [Горячие клавиши](ourplancore-shortcuts.md) |

## Лента: верхние вкладки Main, Page, Annotation, Viewport, Display (69)

??? note "лента Main, JOB (5)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Open / Import` |  | лента: лента Main, JOB | Open jobs, switch job folders, create jobs, or import PDF/OurPlanCore/PlanSwift into the current job | [Проекты и сохранение](job-creation-storage.md) |
    | `PlanSwift` |  | лента: лента Main, JOB | Separate PlanSwift job converter | [Проекты и сохранение](job-creation-storage.md) |
    | `PDF Takeoffs` |  | лента: лента Main, JOB | Import PDF pages and measurement annotations as takeoffs | [Прочее](ourplancore-extras-other.md) |
    | `Save As` |  | лента: лента Main, JOB | Save the current project to a new location | [Проекты и сохранение](job-creation-storage.md) |
    | `In Progress` |  | лента: лента Main, JOB | Set this project's Job Tracker card to In Progress via the configured external command | [Проекты и сохранение](job-creation-storage.md) |

??? note "лента Main, PDF (6)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Export` |  | лента: лента Main, PDF | Export selected/all sheets to a PDF | [Дополнительно](ourplancore-extras.md) |
    | `Name` |  | лента: лента Main, PDF | Preview and apply PDF sheet names | [Листы (Pages)](ourplancore-pages.md) |
    | `Scale` |  | лента: лента Main, PDF | Preview and apply PDF sheet scale | [Листы (Pages)](ourplancore-pages.md) |
    | `Name+Scale` |  | лента: лента Main, PDF | Preview and apply PDF sheet names and scale | [Листы (Pages)](ourplancore-pages.md) |
    | `AI Fill` |  | лента: лента Main, PDF | Queue GPT fallback for missing PDF sheet metadata | [ИИ и терминалы](ourplancore-ai.md) |
    | `Crop Hints` |  | лента: лента Main, PDF | Draw reusable AI Fill crop boxes for sheet number and scale | [ИИ и терминалы](ourplancore-ai.md) |

??? note "лента Page, ADD (3)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Add Pages` |  | лента: лента Page, ADD | Import PDF pages into the current job | [Проекты и сохранение](job-creation-storage.md) |
    | `Blank Sheet` |  | лента: лента Page, ADD | Create an empty sheet in the current job without selecting a PDF | [Листы (Pages)](ourplancore-pages.md) |
    | `PDF Takeoffs` |  | лента: лента Page, ADD | Import PDF pages plus PDF measurement annotations into takeoffs | [Прочее](ourplancore-extras-other.md) |

??? note "лента Page, ROTATE (5)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Left` |  | лента: лента Page, ROTATE | Rotate the active page left | [Листы (Pages)](ourplancore-pages.md) |
    | `Right` |  | лента: лента Page, ROTATE | Rotate the active page right | [Листы (Pages)](ourplancore-pages.md) |
    | `180` |  | лента: лента Page, ROTATE | Rotate the active page 180 degrees | [Листы (Pages)](ourplancore-pages.md) |
    | `Level` |  | лента: лента Page, ROTATE | Reset page view to fit and clear temporary drawing input | [Листы (Pages)](ourplancore-pages.md) |
    | `Batch Rotate` |  | лента: лента Page, ROTATE | Rotate selected pages | [Листы (Pages)](ourplancore-pages.md) |

??? note "лента Page, FLIP (2)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Vertical` |  | лента: лента Page, FLIP | Flip the active page vertically | [Правка и привязки](ourplancore-editing.md) |
    | `Horizontal` |  | лента: лента Page, FLIP | Flip the active page horizontally | [Правка и привязки](ourplancore-editing.md) |

??? note "лента Page, IMAGE (4)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Invert` |  | лента: лента Page, IMAGE | Invert the active page colors | [Листы (Pages)](ourplancore-pages.md) |
    | `Copy` |  | лента: лента Page, IMAGE | Copy a rendered PNG of the active page to the clipboard | [Правка и привязки](ourplancore-editing.md) |
    | `Crop New Page` |  | лента: лента Page, IMAGE | Create a new page from the currently visible viewport area | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Crop to Sheet` |  | лента: лента Page, IMAGE | Crop to Sheet: copy boxed details from any sheets onto one target sheet at true scale; move and rotate them there with Select | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |

??? note "лента Page, PAGE (5)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Batch Rename` |  | лента: лента Page, PAGE | Rename selected pages in order | [Листы (Pages)](ourplancore-pages.md) |
    | `Batch Overlay` |  | лента: лента Page, PAGE | Pair sheets and apply overlay layers to multiple pages | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Set Origin` |  | лента: лента Page, PAGE | Mark the current visible page center as the page origin | [Листы (Pages)](ourplancore-pages.md) |
    | `Offset Origin` |  | лента: лента Page, PAGE | Nudge the stored page origin | [Листы (Pages)](ourplancore-pages.md) |
    | `Close Page` |  | лента: лента Page, PAGE | Close the active page tab | [Листы (Pages)](ourplancore-pages.md) |

??? note "лента Annotation, MARKUP TOOLS (9)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Highlighter` | `Shift+H` | лента: лента Annotation, MARKUP TOOLS | Draw a transparent highlighter box (Shift+H) | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Draw line` | `D` | лента: лента Annotation, MARKUP TOOLS | Draw a simple non-takeoff line markup (D) | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Arrow` |  | лента: лента Annotation, MARKUP TOOLS | Draw a simple non-takeoff arrow markup | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Box` |  | лента: лента Annotation, MARKUP TOOLS | Draw a simple non-takeoff box markup | [Привязки и трассировка](ourplancore-snap-trace.md) |
    | `Cloud` |  | лента: лента Annotation, MARKUP TOOLS | Draw a cloud annotation | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Area fill` |  | лента: лента Annotation, MARKUP TOOLS | Draw a filled color area annotation | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Hide area (white)` |  | лента: лента Annotation, MARKUP TOOLS | Hide area: cover part of the sheet with solid white (screen and PDF output) | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Note` | `N` | лента: лента Annotation, MARKUP TOOLS | Write a text note on the sheet (N) | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Style` |  | лента: лента Annotation, MARKUP TOOLS | Annotation tools, color, and thickness |  |

??? note "лента Annotation, STYLE (1)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Annotation line thickness` |  | лента: лента Annotation, STYLE | Annotation line thickness | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |

??? note "лента Viewport, LINES & AREA (4)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Line measurement thickness` |  | лента: лента Viewport, LINES & AREA | Line measurement thickness 0.25 - 4.0 | [Settings и модули](ourplancore-settings.md) |
    | `Count marker size` |  | лента: лента Viewport, LINES & AREA | Count marker size 0.25 - 4.0 | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Area boundary thickness` |  | лента: лента Viewport, LINES & AREA | Area boundary thickness 0.25 - 4.0 | [Settings и модули](ourplancore-settings.md) |
    | `Area fill opacity` |  | лента: лента Viewport, LINES & AREA | Area fill opacity 0 - 100 % | [Settings и модули](ourplancore-settings.md) |

??? note "лента Viewport, RULER / EXTRA (1)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Ruler screen thickness` |  | лента: лента Viewport, RULER / EXTRA | Ruler screen thickness 0.5 - 6 px | [Инструменты замера](ourplancore-tools.md) |

??? note "лента Viewport, PDF SNAP (1)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `PDF Snap Tab continuation radius` |  | лента: лента Viewport, PDF SNAP | PDF Snap Tab continuation radius 4 - 96 screen px | [Привязки и трассировка](ourplancore-snap-trace.md) |

??? note "лента Display, LABELS (7)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `All` |  | лента: лента Display, LABELS | Show every measurement label category | [Экспорт в Excel](ourplancore-excel.md) |
    | `Line` |  | лента: лента Display, LABELS | Show length label on each line measurement | [Правка и привязки](ourplancore-editing.md) |
    | `Area` |  | лента: лента Display, LABELS | Show area label on each area measurement | [Инструменты замера](ourplancore-tools.md) |
    | `Joist` |  | лента: лента Display, LABELS | Show joist summary and segment labels on area joist layouts | [Инструменты замера](ourplancore-tools.md) |
    | `Count` |  | лента: лента Display, LABELS | Show count label on each count measurement | [Инструменты замера](ourplancore-tools.md) |
    | `Value label size` |  | лента: лента Display, LABELS | Value label size 0.25 - 3.0 | [Settings и модули](ourplancore-settings.md) |
    | `w/ page` |  | лента: лента Display, LABELS | Off (default): labels keep a fixed screen size when zooming. On: labels grow/shrink with page zoom. | [Settings и модули](ourplancore-settings.md) |

??? note "лента Display, OVERLAYS / RENDER (10)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Show` |  | лента: лента Display, OVERLAYS / RENDER | Show or hide the legend overlay on the active sheet | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Legend: Size` |  | лента: лента Display, OVERLAYS / RENDER | Pick legend size preset | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Pos` |  | лента: лента Display, OVERLAYS / RENDER | Pick legend anchor (corner/edge of the sheet) | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Legend: w/page` |  | лента: лента Display, OVERLAYS / RENDER | Off (default): legend keeps a fixed screen size when zooming. On: legend grows/shrinks with page zoom. | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Header: Size` |  | лента: лента Display, OVERLAYS / RENDER | Pick header size preset | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Header: w/page` |  | лента: лента Display, OVERLAYS / RENDER | Off (default): header keeps a fixed screen size when zooming. On: header grows/shrinks with page zoom. | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Fast pan/zoom` |  | лента: лента Display, OVERLAYS / RENDER | Simplify overlays while panning or zooming. Faster on heavy sheets, off by default for full visual quality. | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `PDF layers` |  | лента: лента Display, OVERLAYS / RENDER | Enable the PDF Layers panel and per-page layer scanning. Off by default: pages render faster without layer discovery. | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Static image` |  | лента: лента Display, OVERLAYS / RENDER | On by default (PlanSwift-style): show each page as one fixed 150 DPI raster image with no live re-rendering while you zoom or pan. Turn on PDF layers to use the live layer renderer instead. Trade-off: the image softens above ~200% zoom - enable 'Black vector' for crisp linework. | [Привязки и трассировка](ourplancore-snap-trace.md) |
    | `Black vector` |  | лента: лента Display, OVERLAYS / RENDER | Draw crisp black vector linework on top of the static image, razor-sharp at any zoom. Only lines are vector - text, hatches and fills stay raster; scanned PDFs have no vectors to draw. | [Листы (Pages)](ourplancore-pages.md) |

??? note "лента Display, UNITS & VIEW (6)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `ft / sf` |  | лента: лента Display, UNITS & VIEW | Imperial units (ft / sf / ea). Off = metric. | [Settings и модули](ourplancore-settings.md) |
    | `Viewport PDF render RAM/quality profile` |  | лента: лента Display, UNITS & VIEW | Viewport PDF render RAM/quality profile Options: Balanced, High, Max. | [Settings и модули](ourplancore-settings.md) |
    | `Choose the background around the sheet` |  | лента: лента Display, UNITS & VIEW | Choose the background around the sheet Options: White, Gray, Dark. | [Settings и модули](ourplancore-settings.md) |
    | `Choose a softer page background tint` |  | лента: лента Display, UNITS & VIEW | Choose a softer page background tint Options: White, Soft gray, Medium gray, Dark gray, Warm, Soft green, Black. | [Settings и модули](ourplancore-settings.md) |
    | `Dark` |  | лента: лента Display, UNITS & VIEW | Toggle dark/light UI theme | [Settings и модули](ourplancore-settings.md) |
    | `Mouse-wheel zoom step per notch` |  | лента: лента Display, UNITS & VIEW | Mouse-wheel zoom step per notch 1.05 - 2.5x (PlanSwift-fast at 2x) | [Settings и модули](ourplancore-settings.md) |

## Полоса XL (Excel) справа от листа (21)

??? note "полоса XL (21)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `ALL` |  | полоса XL: полоса XL | Run ALL for one selected building/root: SQFT, Walls, Gables, Truss Heel, Parapet, Eve/Rakes, Openings, then framing floors and shifted Headers | [Экспорт в Excel](ourplancore-excel.md) |
    | `Legend (LG)` |  | полоса XL: полоса XL | Open the job-specific legend used by Beams, Posts, and Headers. ALL also exports framing floors. | [Экспорт в Excel](ourplancore-excel.md) |
    | `SQFT (SF)` |  | полоса XL: полоса XL | SQFT: append to J:L, select J:K, run A2_SQFT_calc | [Экспорт в Excel](ourplancore-excel.md) |
    | `Walls (WL)` |  | полоса XL: полоса XL | Walls: run A3, preserve mandatory A:H output rows, then delete zero rows | [Экспорт в Excel](ourplancore-excel.md) |
    | `Gables (GB)` |  | полоса XL: полоса XL | Gables: append to J:L, select J:K, run A2_SQFT_calc | [Экспорт в Excel](ourplancore-excel.md) |
    | `Truss Heel (TH)` |  | полоса XL: полоса XL | Truss Heel: append to J:L, select J:K, run A2_SQFT_calc | [Экспорт в Excel](ourplancore-excel.md) |
    | `Parapet (PP)` |  | полоса XL: полоса XL | Parapet: append to J:L, select J:K, run A4_Parapet | [Экспорт в Excel](ourplancore-excel.md) |
    | `Eve/Rakes (E/R)` |  | полоса XL: полоса XL | Eve/Rakes: Eve by LF descending, then Rake by LF descending; run A6_Eve_Rakes | [Экспорт в Excel](ourplancore-excel.md) |
    | `Openings (OP)` |  | полоса XL: полоса XL | Openings: append from Z158, run C_SumNearWindowValues per floor, then A5_Openings | [Экспорт в Excel](ourplancore-excel.md) |
    | `Sheathing (SH)` |  | полоса XL: полоса XL | Sheathing: run A7_walls_sheathing with the Zip / Ply / OSB text of column J (or 'wall sheathing = ...' from the LG legend); it keeps one sheathing system and removes the other rows. Runs after Walls in ALL. | [Экспорт в Excel](ourplancore-excel.md) |
    | `Shear walls (SW)` |  | полоса XL: полоса XL | Shear walls: stage shear walls/<floor>/shear and holdowns in J:L, fill the Shear Walls row (interior walls, ext walls use the wall sheathing) and one Holdowns row per holdown in each floor's walls block. | [Экспорт в Excel](ourplancore-excel.md) |
    | `Shaft walls (SHF)` |  | полоса XL: полоса XL | Shaft walls: stage the shaft wall lines and add (or update) the Shaft walls block above the first framing list: panels, CH and J channels from LF x wall height. | [Экспорт в Excel](ourplancore-excel.md) |
    | `Units (UN)` |  | полоса XL: полоса XL | Units: build the units table (Mark x 2x4/2x6/half sizes, per-floor counts and SUMPRODUCT totals) at the anchor set in Settings (AM3) from units/<Mark size> lines and units/<floor>/<Mark> counts. | [Экспорт в Excel](ourplancore-excel.md) |
    | `Balconies (BL)` |  | полоса XL: полоса XL | Balconies: one '#n Upper Balcony/Terrace List W' x L' N units' block per balcony size (and '#n Porch Framing List' per porch size) from SQFT areas named blcny / balcony / porch, copied from the template's #1 block. | [Экспорт в Excel](ourplancore-excel.md) |
    | `Framing (FR)` |  | полоса XL: полоса XL | Framing ALL for the selected building: posts, beams and joists replace their rows in each floor framing list (other template rows stay), headers go to the wall block one floor down, details are staged in J:L. A missing list (6th floor, balcony) is added. | [Экспорт в Excel](ourplancore-excel.md) |
    | `Posts (PS)` |  | полоса XL: полоса XL | Posts: replace the Posts rows in each framing list of the selected building. Uses the LG legend for sizes. | [Экспорт в Excel](ourplancore-excel.md) |
    | `Beams (BM)` |  | полоса XL: полоса XL | Beams: replace the Beam rows in each framing list of the selected building. Uses the LG legend for sizes. | [Экспорт в Excel](ourplancore-excel.md) |
    | `Headers (HD)` |  | полоса XL: полоса XL | Headers: rebuild the header rows of the wall block one floor below each framing floor; Wall Sheathing and the rows after it stay. | [Экспорт в Excel](ourplancore-excel.md) |
    | `Joists (JS)` |  | полоса XL: полоса XL | Joists: replace the Joist rows in each framing list; Extra joists of the same length join the row and short joists go on double stock (Settings). | [Экспорт в Excel](ourplancore-excel.md) |
    | `Details (DT)` |  | полоса XL: полоса XL | Details: stage the detail lines of each floor in J:L under a label row, once. A group already staged is left alone. | [Экспорт в Excel](ourplancore-excel.md) |
    | `Stairs (ST)` |  | полоса XL: полоса XL | Stairs: add the stair takeoffs before Subfloor of each framing list; a repeated export replaces them. | [Экспорт в Excel](ourplancore-excel.md) |

## Полосы значков слева и справа от листа (набор по умолчанию) (33)

??? note "левая полоса значков (14)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Open Selected in Tabs` |  | полоса значков: левая полоса значков | Open the selected Pages sheets as tabs. | [Листы (Pages)](ourplancore-pages.md) |
    | `Detach to Windows` |  | полоса значков: левая полоса значков | Open the selected Pages sheets in detached windows. | [Листы (Pages)](ourplancore-pages.md) |
    | `Tile on Monitor 2` |  | полоса значков: левая полоса значков | Tile the selected sheets on monitor 2. | [Workspace, Job Tracker, CLI](ourplancore-workspace.md) |
    | `Overlay` |  | полоса значков: левая полоса значков | Choose a matching sheet overlay for the active sheet. | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Move Overlay by Points` |  | полоса значков: левая полоса значков | Align the active sheet overlay by matching points. | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Name / Scale Setup` | `F5` | полоса значков: левая полоса значков | Open the manual Name / Scale window for the active sheet. | [Листы (Pages)](ourplancore-pages.md) |
    | `Sort Pages A-Z` |  | полоса значков: левая полоса значков | Sort children of the selected Pages folder (or root) alphabetically. | [Листы (Pages)](ourplancore-pages.md) |
    | `Sort Pages Z-A` |  | полоса значков: левая полоса значков | Sort children of the selected Pages folder (or root) in reverse alphabetical order. | [Листы (Pages)](ourplancore-pages.md) |
    | `Sort Pages A/S` |  | полоса значков: левая полоса значков | Move A sheets to Arch, S sheets to Struct, and trailing '-' sheets to others. | [Листы (Pages)](ourplancore-pages.md) |
    | `Sort Pages D/Sec/WT` |  | полоса значков: левая полоса значков | Move suffix sheets into details/sections/units and reorder v/wt/ft/sv/sw at Pages root. | [Листы (Pages)](ourplancore-pages.md) |
    | `Auto Page Folders` |  | полоса значков: левая полоса значков | Create the standard page folder tree. | [Листы (Pages)](ourplancore-pages.md) |
    | `Collapse Pages Tree` |  | полоса значков: левая полоса значков | Collapse all Pages nodes. | [Листы (Pages)](ourplancore-pages.md) |
    | `Expand Pages Tree` |  | полоса значков: левая полоса значков | Expand all Pages nodes. | [Инструменты замера](ourplancore-tools.md) |
    | `Configure the command strip (gear)` |  | полоса значков: левая полоса значков | Configure the left command strip: pick any commands for the strip. |  |

??? note "правая полоса значков (19)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Quick Calculator` |  | полоса значков: правая полоса значков | Toggle the slide-out calculator with feet-inches math. | [Workspace, Job Tracker, CLI](ourplancore-workspace.md) |
    | `New Takeoff Item` | `T` | полоса значков: правая полоса значков | Create a takeoff item under the selected/root folder. | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `New Takeoff Folder` |  | полоса значков: правая полоса значков | Create a takeoff folder under the selected/root folder. | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Record Active Takeoff` | `Space` | полоса значков: правая полоса значков | Start or stop recording into the active target item. | [Инструменты замера](ourplancore-tools.md) |
    | `Show Active Takeoff` |  | полоса значков: правая полоса значков | Scroll the Takeoffs tree to the active target item. | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Active Takeoff Properties` |  | полоса значков: правая полоса значков | Edit properties for the active target item. | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Merge Selected Takeoffs / Measurements` | `Ctrl+M` | полоса значков: правая полоса значков | Merge selected takeoff items from all sheets, or move selected measurement segments into another takeoff. | [Правка и привязки](ourplancore-editing.md) |
    | `Split Selected Takeoffs / Measurements` | `Ctrl+Shift+M` | полоса значков: правая полоса значков | Split whole takeoffs across all sheets, or move selected measurements or Count marks into a new takeoff. | [Правка и привязки](ourplancore-editing.md) |
    | `Sort Takeoffs A-Z` |  | полоса значков: правая полоса значков | Sort children of the selected Takeoffs folder (or root) alphabetically. | [Листы (Pages)](ourplancore-pages.md) |
    | `Sort Takeoffs Z-A` |  | полоса значков: правая полоса значков | Sort children of the selected Takeoffs folder (or root) in reverse alphabetical order. | [Листы (Pages)](ourplancore-pages.md) |
    | `Sort Takeoffs: Walls` |  | полоса значков: правая полоса значков | Sort wall takeoffs in the selected folder and subfolders: ext, corr, dem, then 2x6/2x4 sizes. | [Листы (Pages)](ourplancore-pages.md) |
    | `Sort Takeoffs: Details by Sheet` |  | полоса значков: правая полоса значков | Group detail takeoffs like 1/A501 by the sheet after the slash, ordered as in the Pages tree. | [Листы (Pages)](ourplancore-pages.md) |
    | `Auto Takeoff Tree` |  | полоса значков: правая полоса значков | Create the standard takeoff folder tree. | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Create Takeoffs From Pages` |  | полоса значков: правая полоса значков | Create top takeoff folders from CAPS page/folder names. | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Export to Current Excel` |  | полоса значков: правая полоса значков | Write selected takeoff folder/item rows to the active cell in an open Excel workbook. | [Экспорт в Excel](ourplancore-excel.md) |
    | `Collapse Takeoffs Tree` |  | полоса значков: правая полоса значков | Collapse all Takeoffs nodes. | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Expand Takeoffs Tree` |  | полоса значков: правая полоса значков | Expand all Takeoffs nodes. | [Инструменты замера](ourplancore-tools.md) |
    | `Configure the command strip (gear)` |  | полоса значков: правая полоса значков | Configure the right command strip: pick any commands for the strip. |  |
    | `Terminal (>_)` |  | полоса значков: правая полоса значков | Show / hide Codex and Claude terminals | [Консоль ИИ](ourplancore-ai-console.md) |

## Панели и вкладки рабочей области (168)

??? note "Main View, панель Pages (12)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Close other sheets and keep the main viewport sheet` |  | панель: Main View, панель Pages | Close every other sheet tab and all detached windows; keep the sheet shown in the main viewport | [Листы (Pages)](ourplancore-pages.md) |
    | `Close detached sheets on monitor 2` |  | панель: Main View, панель Pages | Close all detached sheet windows on monitor 2 | [Листы (Pages)](ourplancore-pages.md) |
    | `Tile M2` |  | панель: Main View, панель Pages | Open selected Pages sheets in detached windows and tile them on monitor 2 | [Листы (Pages)](ourplancore-pages.md) |
    | `Toggle vertical Tile M2 layout` |  | панель: Main View, панель Pages | Toggle vertical Tile M2 layout (filled = vertical) | [Листы (Pages)](ourplancore-pages.md) |
    | `Open` |  | панель: Main View, панель Pages | Open the selected Pages sheets | [Листы (Pages)](ourplancore-pages.md) |
    | `Refresh Pages tree` |  | панель: Main View, панель Pages | Refresh Pages tree | [Листы (Pages)](ourplancore-pages.md) |
    | `Collapse all Pages nodes` |  | панель: Main View, панель Pages | Collapse all Pages nodes | [Листы (Pages)](ourplancore-pages.md) |
    | `Expand all Pages nodes` |  | панель: Main View, панель Pages | Expand all Pages nodes | [Инструменты замера](ourplancore-tools.md) |
    | `New Folder` |  | панель: Main View, панель Pages | Create a new folder under the selected Pages folder | [Листы (Pages)](ourplancore-pages.md) |
    | `Name` |  | панель: Main View, панель Pages | Preview automatic names for the selected sheet or folder | [Листы (Pages)](ourplancore-pages.md) |
    | `Scale` |  | панель: Main View, панель Pages | Preview automatic scales for the selected sheet or folder | [Листы (Pages)](ourplancore-pages.md) |
    | `Name+Scale` |  | панель: Main View, панель Pages | Preview automatic names and scales for the selected sheet or folder | [Листы (Pages)](ourplancore-pages.md) |

??? note "Main View, панель Pages, быстрая строка (3)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Folder Template Mode` |  | панель: Main View, панель Pages, быстрая строка | Folder template mode for Pages and Takeoffs Options: Auto, COM, EWP. | [Листы (Pages)](ourplancore-pages.md) |
    | `+ New` |  | панель: Main View, панель Pages, быстрая строка | Create pages and folders | [Листы (Pages)](ourplancore-pages.md) |
    | `Setup` |  | панель: Main View, панель Pages, быстрая строка | Page setup and sorting actions | [Листы (Pages)](ourplancore-pages.md) |

??? note "Main View > Pages, панель Pages (1)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Match page folder case exactly` |  | панель: Main View > Pages, панель Pages | Match page folder case exactly | [Листы (Pages)](ourplancore-pages.md) |

??? note "Main View > PDF Layers, панель Pages (7)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Load` |  | панель: Main View > PDF Layers, панель Pages | Scan PDF layers for the active page on demand | [Привязки и трассировка](ourplancore-snap-trace.md) |
    | `All On` |  | панель: Main View > PDF Layers, панель Pages | Show all PDF layers on the active page | [Привязки и трассировка](ourplancore-snap-trace.md) |
    | `All Off` |  | панель: Main View > PDF Layers, панель Pages | Hide all PDF layers on the active page | [Привязки и трассировка](ourplancore-snap-trace.md) |
    | `Clear Hi` |  | панель: Main View > PDF Layers, панель Pages | Clear the layer highlight overlay | [Привязки и трассировка](ourplancore-snap-trace.md) |
    | `Layer Trace` |  | панель: Main View > PDF Layers, панель Pages | Isolate and trace the selected PDF layer | [Привязки и трассировка](ourplancore-snap-trace.md) |
    | `Full` |  | панель: Main View > PDF Layers, панель Pages | Cycle the layer-trace dimming (Full / dimmed / off) | [Привязки и трассировка](ourplancore-snap-trace.md) |
    | `Apply` |  | панель: Main View > PDF Layers, панель Pages |  | [Привязки и трассировка](ourplancore-snap-trace.md) |

??? note "Main View, панель Bookmarks (1)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Return Bookmarks to the tab list` |  | панель: Main View, панель Bookmarks | Return Bookmarks to the tab list | [Прочее](ourplancore-extras-other.md) |

??? note "Main View, панель Templates (1)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Return Templates to the tab list` |  | панель: Main View, панель Templates | Return Templates to the tab list |  |

??? note "Main View, стартовая карточка (проект не открыт) (4)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Open a recent job - Recently used` |  | панель: Main View, стартовая карточка (проект не открыт) | Pick from recently used jobs | [Проекты и сохранение](job-creation-storage.md) |
    | `New blank job - Start empty` |  | панель: Main View, стартовая карточка (проект не открыт) | Create an empty job; add sheets later | [Проекты и сохранение](job-creation-storage.md) |
    | `New job from PDFs - Import a folder of drawings` |  | панель: Main View, стартовая карточка (проект не открыт) | Create a job from a folder of PDF drawings | [Проекты и сохранение](job-creation-storage.md) |
    | `Open sample job - Explore a demo` |  | панель: Main View, стартовая карточка (проект не открыт) | Open the bundled sample job to explore | [Проекты и сохранение](job-creation-storage.md) |

??? note "Main View, строка Layer Trace (2)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Manual` |  | панель: Main View, строка Layer Trace | Toggle Manual / PDF Layer Trace mode in the viewport | [Привязки и трассировка](ourplancore-snap-trace.md) |
    | `Full` |  | панель: Main View, строка Layer Trace | Cycle Layer Trace mode (Tab while Layer Trace is on) | [Привязки и трассировка](ourplancore-snap-trace.md) |

??? note "Main View, панель Takeoffs (8)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Refresh Takeoffs tree` |  | панель: Main View, панель Takeoffs | Refresh Takeoffs tree | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Collapse all Takeoffs nodes` |  | панель: Main View, панель Takeoffs | Collapse all Takeoffs nodes | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Expand all Takeoffs nodes` |  | панель: Main View, панель Takeoffs | Expand all Takeoffs nodes | [Инструменты замера](ourplancore-tools.md) |
    | `New Folder` |  | панель: Main View, панель Takeoffs |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `New Item` | `T` | панель: Main View, панель Takeoffs | Create a takeoff item (T) | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Delete Empty` |  | панель: Main View, панель Takeoffs | Delete all takeoff items with zero measurement sections; Ctrl+Z restores the batch | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `More` |  | панель: Main View, панель Takeoffs | More takeoff actions | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Export` |  | панель: Main View, панель Takeoffs | Save or export quantities | [Дерево Takeoffs](ourplancore-takeoffs.md) |

??? note "Main View, панель Takeoffs, строка активной позиции (7)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Record` | `Space` | панель: Main View, панель Takeoffs, строка активной позиции | Start or stop recording into the active takeoff item (Space) | [Инструменты замера](ourplancore-tools.md) |
    | `More` |  | панель: Main View, панель Takeoffs, строка активной позиции | More active target actions | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Props` |  | панель: Main View, панель Takeoffs, строка активной позиции | Edit active takeoff item properties | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Find` |  | панель: Main View, панель Takeoffs, строка активной позиции | Show active takeoff item in the tree | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Sheet` |  | панель: Main View, панель Takeoffs, строка активной позиции | Choose a takeoff item measured on this sheet | [Листы (Pages)](ourplancore-pages.md) |
    | `Switch to next takeoff item` |  | панель: Main View, панель Takeoffs, строка активной позиции | Switch to next takeoff item | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Switch to previous takeoff item` |  | панель: Main View, панель Takeoffs, строка активной позиции | Switch to previous takeoff item | [Дерево Takeoffs](ourplancore-takeoffs.md) |

??? note "Main View, панель Takeoffs, дерево (1)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Match takeoff folder case exactly` |  | панель: Main View, панель Takeoffs, дерево | Match takeoff folder case exactly | [Дерево Takeoffs](ourplancore-takeoffs.md) |

??? note "Main View, AI Inbox (6)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Toggle AI Inbox` |  | панель: Main View, AI Inbox | Expand or collapse the AI Inbox | [ИИ и терминалы](ourplancore-ai.md) |
    | `+ Add` |  | панель: Main View, AI Inbox |  | [ИИ и терминалы](ourplancore-ai.md) |
    | `Run AI` |  | панель: Main View, AI Inbox |  | [ИИ и терминалы](ourplancore-ai.md) |
    | `More` |  | панель: Main View, AI Inbox | More AI Inbox actions | [ИИ и терминалы](ourplancore-ai.md) |
    | `Filter AI markers by type` |  | панель: Main View, AI Inbox | Filter AI markers by type | [ИИ и терминалы](ourplancore-ai.md) |
    | `Filter AI markers by sample kind` |  | панель: Main View, AI Inbox | Filter AI markers by sample kind | [ИИ и терминалы](ourplancore-ai.md) |

??? note "Sheet Manager, группа PDF (3)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Import PDF(s)` |  | панель: Sheet Manager, группа PDF | Add one or many PDF files to the current job | [Менеджеры](ourplancore-managers.md) |
    | `PDF Takeoffs` |  | панель: Sheet Manager, группа PDF | Import PDF measurement annotations into takeoff items | [Прочее](ourplancore-extras-other.md) |
    | `Export PDF` |  | панель: Sheet Manager, группа PDF | Export selected or all sheets to PDF | [PDF и сдача](ourplancore-pdf.md) |

??? note "Sheet Manager, группа Raster (3)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `PDF` |  | панель: Sheet Manager, группа Raster | Disable raster rendering for the selected sheets | [Привязки и трассировка](ourplancore-snap-trace.md) |
    | `Auto` |  | панель: Sheet Manager, группа Raster | Restore adaptive raster DPI for the selected sheets | [Листы (Pages)](ourplancore-pages.md) |
    | `Options...` |  | панель: Sheet Manager, группа Raster | Raster format, prepare, first-frame, cleanup, and cancel options | [Проекты и сохранение](job-creation-storage.md) |

??? note "Sheet Manager, группа Format (6)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Sheet Manager Raster Format Box` |  | панель: Sheet Manager, группа Format | Auto keeps the existing WebP-preferred cache behavior; PNG is useful for difficult raster-like PDFs Options: Auto, WebP, PNG. |  |
    | `Prepare` |  | панель: Sheet Manager, группа Format | Build the last selected DPI cache without changing PDF/raster state | [Менеджеры](ourplancore-managers.md) |
    | `First On` |  | панель: Sheet Manager, группа Format | Open selected raster sheets from the pre-rendered raster image as the first frame | [Менеджеры](ourplancore-managers.md) |
    | `First Off` |  | панель: Sheet Manager, группа Format | Keep selected raster sheets on the normal PDF/preview-first opening path | [Менеджеры](ourplancore-managers.md) |
    | `Clean` |  | панель: Sheet Manager, группа Format | Delete unused raster image variants for selected sheets; keeps the active raster image | [Проекты и сохранение](job-creation-storage.md) |
    | `Cancel` |  | панель: Sheet Manager, группа Format | Cancel background raster work after the current sheet finishes | [Привязки и трассировка](ourplancore-snap-trace.md) |

??? note "Sheet Manager, группа Metadata (8)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Refresh` |  | панель: Sheet Manager, группа Metadata | Reload the sheet table from current page folders | [Листы (Pages)](ourplancore-pages.md) |
    | `Analyze` |  | панель: Sheet Manager, группа Metadata | Read PDF text/layers and preview sheet metadata | [Листы (Pages)](ourplancore-pages.md) |
    | `Auto Name` |  | панель: Sheet Manager, группа Metadata | Preview automatic sheet names | [Settings и модули](ourplancore-settings.md) |
    | `Auto Scale` |  | панель: Sheet Manager, группа Metadata | Preview automatic sheet scales | [Листы (Pages)](ourplancore-pages.md) |
    | `Name+Scale` |  | панель: Sheet Manager, группа Metadata | Preview names and scales together | [Листы (Pages)](ourplancore-pages.md) |
    | `AI Fill` |  | панель: Sheet Manager, группа Metadata | Queue GPT fallback for missing sheet metadata | [ИИ и терминалы](ourplancore-ai.md) |
    | `Crop Hints` |  | панель: Sheet Manager, группа Metadata | Draw reusable sheet number, title, and scale regions | [ИИ и терминалы](ourplancore-ai.md) |
    | `Apply Checked` |  | панель: Sheet Manager, группа Metadata | Apply checked rename/scale rows to the job | [Менеджеры](ourplancore-managers.md) |

??? note "Sheet Manager, группа Open (5)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Open Sheet` |  | панель: Sheet Manager, группа Open | Switch to the selected sheet in Main View | [Менеджеры](ourplancore-managers.md) |
    | `Open Tabs` |  | панель: Sheet Manager, группа Open | Open the selected sheets as viewport tabs | [Менеджеры](ourplancore-managers.md) |
    | `Detach` |  | панель: Sheet Manager, группа Open | Open the selected sheets in detached windows | [Листы (Pages)](ourplancore-pages.md) |
    | `Tile M2` |  | панель: Sheet Manager, группа Open | Open selected sheets in detached windows and tile them on monitor 2 | [Листы (Pages)](ourplancore-pages.md) |
    | `Open JSON` |  | панель: Sheet Manager, группа Open | Open the PDF metadata JSON for inspection | [ИИ и терминалы](ourplancore-ai.md) |

??? note "Sheet Manager, группа Organize (4)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Sort A/S` |  | панель: Sheet Manager, группа Organize | Sort A/S sheets inside the selected Pages folder; if no folder is selected, sort all Pages | [Листы (Pages)](ourplancore-pages.md) |
    | `D/Sec/WT` |  | панель: Sheet Manager, группа Organize | Sort suffix sheets inside the selected Pages folder; if no folder is selected, sort all Pages | [Листы (Pages)](ourplancore-pages.md) |
    | `Repair Links` |  | панель: Sheet Manager, группа Organize | Reconnect saved measurements to current page folders | [Листы (Pages)](ourplancore-pages.md) |
    | `Auto Folders` |  | панель: Sheet Manager, группа Organize | Create standard page folders under the selected Pages folder | [Листы (Pages)](ourplancore-pages.md) |

??? note "Takeoff Manager, группа File (1)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Save` |  | панель: Takeoff Manager, группа File | Save the current job | [Дерево Takeoffs](ourplancore-takeoffs.md) |

??? note "Takeoff Manager, группа Item (6)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Refresh` |  | панель: Takeoff Manager, группа Item | Reload the takeoff manager table | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Set Active` |  | панель: Takeoff Manager, группа Item | Make the selected takeoff item the active drawing target | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Properties` |  | панель: Takeoff Manager, группа Item | Edit the selected takeoff item's properties | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Open Estimating` |  | панель: Takeoff Manager, группа Item | Open the full estimating table window | [Менеджеры](ourplancore-managers.md) |
    | `New Folder` |  | панель: Takeoff Manager, группа Item | Create a takeoff folder | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `New Item` |  | панель: Takeoff Manager, группа Item | Create a takeoff item | [Дерево Takeoffs](ourplancore-takeoffs.md) |

??? note "Takeoff Manager, группа Tree (2)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Auto Tree` |  | панель: Takeoff Manager, группа Tree | Create a standard takeoff tree | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `From Pages` |  | панель: Takeoff Manager, группа Tree | Create takeoff folders/items from the page structure | [Дерево Takeoffs](ourplancore-takeoffs.md) |

??? note "Takeoff Manager, группа Export (4)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Export CSV` |  | панель: Takeoff Manager, группа Export | Export quantities to CSV | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `TXT` |  | панель: Takeoff Manager, группа Export | Export quantities to text | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Excel` |  | панель: Takeoff Manager, группа Export | Export quantities to Excel | [Экспорт в Excel](ourplancore-excel.md) |
    | `Current Excel` |  | панель: Takeoff Manager, группа Export | Write the selected takeoff folder/item to the active cell in an already open Excel workbook | [Экспорт в Excel](ourplancore-excel.md) |

??? note "Report Builder, группа Template (1)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Reload` |  | панель: Report Builder, группа Template | Reload TemplateCom.xlsm into the report builder table | [Менеджеры](ourplancore-managers.md) |

??? note "Report Builder, группа Table (1)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Refresh` |  | панель: Report Builder, группа Table | Refresh the report builder view | [Менеджеры](ourplancore-managers.md) |

??? note "Report Builder, группа Walls (1)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Apply Walls` |  | панель: Report Builder, группа Walls | Apply the A3 wall block rule to the selected source rows in J:K | [Менеджеры](ourplancore-managers.md) |

??? note "Materials, группа Extract (3)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Extract` |  | панель: Materials, группа Extract | Extract material evidence from the current job's source PDFs | [Менеджеры](ourplancore-managers.md) |
    | `Report Sheet` |  | панель: Materials, группа Extract | Create a copyable Materials Report sheet from the current job's existing pages | [Менеджеры](ourplancore-managers.md) |
    | `Refresh` |  | панель: Materials, группа Extract | Reload the latest material extraction output | [Менеджеры](ourplancore-managers.md) |

??? note "Materials, группа Open (4)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `JSON` |  | панель: Materials, группа Open | Open the full material extraction JSON | [Менеджеры](ourplancore-managers.md) |
    | `Rows CSV` |  | панель: Materials, группа Open | Open material evidence rows as CSV | [Менеджеры](ourplancore-managers.md) |
    | `Summary CSV` |  | панель: Materials, группа Open | Open grouped material summary as CSV | [Менеджеры](ourplancore-managers.md) |
    | `Folder` |  | панель: Materials, группа Open | Open the job material extraction output folder | [Дерево Takeoffs](ourplancore-takeoffs.md) |

??? note "AI Manager, группа Setup (2)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `AI Settings` |  | панель: AI Manager, группа Setup | Open model and key status settings | [ИИ и терминалы](ourplancore-ai.md) |
    | `+ Add` |  | панель: AI Manager, группа Setup | Add a manual AI observation or marker note | [ИИ и терминалы](ourplancore-ai.md) |

??? note "AI Manager, группа Review (4)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Refresh` |  | панель: AI Manager, группа Review | Reload the AI manager table | [ИИ и терминалы](ourplancore-ai.md) |
    | `Open Details` |  | панель: AI Manager, группа Review | Open details for the selected AI item | [ИИ и терминалы](ourplancore-ai.md) |
    | `Go to Page` |  | панель: AI Manager, группа Review | Switch to the selected item's source page | [ИИ и терминалы](ourplancore-ai.md) |
    | `Run AI` |  | панель: AI Manager, группа Review | Run AI for the selected eligible item | [ИИ и терминалы](ourplancore-ai.md) |

??? note "AI Manager, группа Batch (2)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Run New` |  | панель: AI Manager, группа Batch | Run all new queued AI bookmark requests | [ИИ и терминалы](ourplancore-ai.md) |
    | `Retry Failed` |  | панель: AI Manager, группа Batch | Retry failed AI bookmark requests | [ИИ и терминалы](ourplancore-ai.md) |

??? note "AI Manager, группа Markers (3)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Create Set` |  | панель: AI Manager, группа Markers | Create a named marker set from reviewed markers | [ИИ и терминалы](ourplancore-ai.md) |
    | `Marker Sets` |  | панель: AI Manager, группа Markers | Manage saved marker sets | [ИИ и терминалы](ourplancore-ai.md) |
    | `Export Markers` |  | панель: AI Manager, группа Markers | Export reviewed AI markers | [ИИ и терминалы](ourplancore-ai.md) |

??? note "3D, группа Build (5)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Auto` |  | панель: 3D, группа Build | Auto-build walls, sqft slabs, and RF/roof areas when available | [3D и менеджеры](ourplancore-3d.md) |
    | `Wall` |  | панель: 3D, группа Build | Build wall prisms from selected line takeoffs | [3D и менеджеры](ourplancore-3d.md) |
    | `Roof Base` |  | панель: 3D, группа Build | Create a roof footprint from selected area takeoffs | [3D крыша](ourplancore-3d-roof.md) |
    | `Select Edge` |  | панель: 3D, группа Build | Select roof base edges on the sheet; save per-edge pitch from the side panel | [3D крыша](ourplancore-3d-roof.md) |
    | `Generate Roof` |  | панель: 3D, группа Build | Build ridge, hip, and valley geometry from the saved per-edge roof pitches | [3D крыша](ourplancore-3d-roof.md) |

??? note "3D, группа Rafters (5)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Pick Faces` |  | панель: 3D, группа Rafters | Click roof faces in the 3D view to toggle rafters on each face | [3D крыша](ourplancore-3d-roof.md) |
    | `Whole Roof` |  | панель: 3D, группа Rafters | Lay rafters on every face of every generated roof | [3D крыша](ourplancore-3d-roof.md) |
    | `Rafter spacing o.c` |  | панель: 3D, группа Rafters | Rafter spacing o.c. (measured horizontally along the eave) | [3D крыша](ourplancore-3d-roof.md) |
    | `Rafter member size` |  | панель: 3D, группа Rafters | Rafter member size; depth extrudes below the roof plane and walls trim to the rafter underside | [3D крыша](ourplancore-3d-roof.md) |
    | `Clear` |  | панель: 3D, группа Rafters | Remove rafters from all roofs | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |

??? note "3D, группа Viewer (5)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Fit` |  | панель: 3D, группа Viewer | Fit the clean 3D viewer scene | [3D и менеджеры](ourplancore-3d.md) |
    | `Iso` |  | панель: 3D, группа Viewer | Show isometric view | [3D и менеджеры](ourplancore-3d.md) |
    | `Top` |  | панель: 3D, группа Viewer | Show top view | [3D и менеджеры](ourplancore-3d.md) |
    | `Front` |  | панель: 3D, группа Viewer | Show front view | [3D и менеджеры](ourplancore-3d.md) |
    | `Reset` |  | панель: 3D, группа Viewer | Reset the 3D camera view | [3D и менеджеры](ourplancore-3d.md) |

??? note "легенда XL (кнопка LG) (4)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Hide the Excel legend panel` |  | панель: легенда XL (кнопка LG) | Hide the Excel legend panel | [Экспорт в Excel](ourplancore-excel.md) |
    | `Add missing codes` |  | панель: легенда XL (кнопка LG) | Add a line for every post, beam and header code of this job that the legend does not have yet | [Экспорт в Excel](ourplancore-excel.md) |
    | `Save for job` |  | панель: легенда XL (кнопка LG) |  | [Экспорт в Excel](ourplancore-excel.md) |
    | `Clear` |  | панель: легенда XL (кнопка LG) |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |

??? note "Quick Calculator (1)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Hide the calculator panel` |  | панель: Quick Calculator | Hide the calculator panel |  |

??? note "панель Pages, вкладка Overlay (19)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Show overlay` |  | панель: панель Pages, вкладка Overlay |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Add...` |  | панель: панель Pages, вкладка Overlay |  | [Settings и модули](ourplancore-settings.md) |
    | `Open Source` |  | панель: панель Pages, вкладка Overlay |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Choose / Replace...` |  | панель: панель Pages, вкладка Overlay |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Next Match` |  | панель: панель Pages, вкладка Overlay |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Remove` |  | панель: панель Pages, вкладка Overlay |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Move active layer down` |  | панель: панель Pages, вкладка Overlay | Move active layer down |  |
    | `Move active layer up` |  | панель: панель Pages, вкладка Overlay | Move active layer up |  |
    | `Auto Fit` |  | панель: панель Pages, вкладка Overlay |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Find Best` |  | панель: панель Pages, вкладка Overlay |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Edit by Points` |  | панель: панель Pages, вкладка Overlay |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Reset` |  | панель: панель Pages, вкладка Overlay |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Red` |  | панель: панель Pages, вкладка Overlay | Red |  |
    | `Blue` |  | панель: панель Pages, вкладка Overlay | Blue |  |
    | `Green` |  | панель: панель Pages, вкладка Overlay | Green | [Settings и модули](ourplancore-settings.md) |
    | `Orange` |  | панель: панель Pages, вкладка Overlay | Orange |  |
    | `Magenta` |  | панель: панель Pages, вкладка Overlay | Magenta | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Gray` |  | панель: панель Pages, вкладка Overlay | Gray | [Settings и модули](ourplancore-settings.md) |
    | `Choose custom color` |  | панель: панель Pages, вкладка Overlay | Choose custom color |  |

??? note "панель терминала Codex / Claude (13)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Detach terminal to its own window` |  | панель: панель терминала Codex / Claude | Detach terminal to its own window; keep conversation running | [Консоль ИИ](ourplancore-ai-console.md) |
    | `Settings -> Terminals` |  | панель: панель терминала Codex / Claude | Settings -> Terminals | [Консоль ИИ](ourplancore-ai-console.md) |
    | `Terminal actions` |  | панель: панель терминала Codex / Claude | Terminal actions | [Консоль ИИ](ourplancore-ai-console.md) |
    | `Hide panel` |  | панель: панель терминала Codex / Claude | Hide panel; keep both conversations running | [Консоль ИИ](ourplancore-ai-console.md) |
    | `Codex` |  | панель: панель терминала Codex / Claude |  | [Консоль ИИ](ourplancore-ai-console.md) |
    | `Claude` |  | панель: панель терминала Codex / Claude |  | [Консоль ИИ](ourplancore-ai-console.md) |
    | `Run` |  | панель: панель терминала Codex / Claude | Run / resume using the selected E-Wood shortcut |  |
    | `Attach` |  | панель: панель терминала Codex / Claude | Attach an already open Git Bash / mintty window | [Консоль ИИ](ourplancore-ai-console.md) |
    | `Reasoning effort for the next launch` |  | панель: панель терминала Codex / Claude | Reasoning effort for the next launch. Quick: low; Balanced: medium; Deep: high. Existing sessions use their own controls. | [Консоль ИИ](ourplancore-ai-console.md) |
    | `Context` |  | панель: панель терминала Codex / Claude | Open the live plan context file | [Консоль ИИ](ourplancore-ai-console.md) |
    | `Paste context` |  | панель: панель терминала Codex / Claude | Paste the context message into the terminal without Enter; submit it at the assistant prompt | [Консоль ИИ](ourplancore-ai-console.md) |
    | `AI Inbox` |  | панель: панель терминала Codex / Claude | Open AI Inbox / AI Manager | [Консоль ИИ](ourplancore-ai-console.md) |
    | `AI Crop +` |  | панель: панель терминала Codex / Claude | Draw an AI crop and share its PNG with the terminal context | [Консоль ИИ](ourplancore-ai-console.md) |

## Контекстные меню и меню кнопок (369)

??? note "меню кнопки Combine, нижняя полоса, строка 1 (5)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Union` |  | меню: меню кнопки Combine, нижняя полоса, строка 1 | merge into one area | [Правка и привязки](ourplancore-editing.md) |
    | `Subtract` |  | меню: меню кнопки Combine, нижняя полоса, строка 1 | first minus the others | [Правка и привязки](ourplancore-editing.md) |
    | `Intersect` |  | меню: меню кнопки Combine, нижняя полоса, строка 1 | keep only the overlap | [Правка и привязки](ourplancore-editing.md) |
    | `Remove Overlap` |  | меню: меню кнопки Combine, нижняя полоса, строка 1 | trim double counting | [Правка и привязки](ourplancore-editing.md) |
    | `Divide` |  | меню: меню кнопки Combine, нижняя полоса, строка 1 | split into exclusive + overlap pieces | [Правка и привязки](ourplancore-editing.md) |

??? note "меню кнопки Open, Main View, панель Pages (2)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Open as Tabs` |  | меню: меню кнопки Open, Main View, панель Pages |  | [Листы (Pages)](ourplancore-pages.md) |
    | `Detach to windows` |  | меню: меню кнопки Open, Main View, панель Pages |  | [Листы (Pages)](ourplancore-pages.md) |

??? note "меню кнопки + New, Main View, панель Pages, быстрая строка (3)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `New Folder` |  | меню: меню кнопки + New, Main View, панель Pages, быстрая строка |  | [Листы (Pages)](ourplancore-pages.md) |
    | `Blank Sheet` |  | меню: меню кнопки + New, Main View, панель Pages, быстрая строка |  | [Листы (Pages)](ourplancore-pages.md) |
    | `Auto Folders` |  | меню: меню кнопки + New, Main View, панель Pages, быстрая строка |  | [Листы (Pages)](ourplancore-pages.md) |

??? note "меню кнопки Setup, Main View, панель Pages, быстрая строка (4)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Name / Scale...` |  | меню: меню кнопки Setup, Main View, панель Pages, быстрая строка |  | [Листы (Pages)](ourplancore-pages.md) |
    | `Sort: A -> Arch / S -> Struct` |  | меню: меню кнопки Setup, Main View, панель Pages, быстрая строка |  | [Листы (Pages)](ourplancore-pages.md) |
    | `Sort: D / Sec / WT suffix` |  | меню: меню кнопки Setup, Main View, панель Pages, быстрая строка |  | [Листы (Pages)](ourplancore-pages.md) |
    | `Repair page links` |  | меню: меню кнопки Setup, Main View, панель Pages, быстрая строка |  | [Листы (Pages)](ourplancore-pages.md) |

??? note "меню кнопки More, Main View, панель Takeoffs (3)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Roof Base from area` |  | меню: меню кнопки More, Main View, панель Takeoffs |  | [3D крыша](ourplancore-3d-roof.md) |
    | `Auto Tree` |  | меню: меню кнопки More, Main View, панель Takeoffs |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `From Pages` |  | меню: меню кнопки More, Main View, панель Takeoffs |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |

??? note "меню кнопки More (AI Inbox) (5)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Run New Bookmarks` |  | меню: меню кнопки More (AI Inbox) |  | [ИИ и терминалы](ourplancore-ai.md) |
    | `Retry Failed Bookmarks` |  | меню: меню кнопки More (AI Inbox) |  | [ИИ и терминалы](ourplancore-ai.md) |
    | `Create Marker Set` |  | меню: меню кнопки More (AI Inbox) |  | [ИИ и терминалы](ourplancore-ai.md) |
    | `Manage Marker Sets...` |  | меню: меню кнопки More (AI Inbox) |  | [ИИ и терминалы](ourplancore-ai.md) |
    | `Export Marker Context` |  | меню: меню кнопки More (AI Inbox) |  | [ИИ и терминалы](ourplancore-ai.md) |

??? note "меню записи AI Inbox (7)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Refresh Inbox` |  | меню: меню записи AI Inbox |  | [ИИ и терминалы](ourplancore-ai.md) |
    | `Open Details` |  | меню: меню записи AI Inbox |  | [ИИ и терминалы](ourplancore-ai.md) |
    | `Go to Page` |  | меню: меню записи AI Inbox |  | [ИИ и терминалы](ourplancore-ai.md) |
    | `Run AI Request` |  | меню: меню записи AI Inbox |  | [ИИ и терминалы](ourplancore-ai.md) |
    | `Open Project Context` |  | меню: меню записи AI Inbox |  | [ИИ и терминалы](ourplancore-ai.md) |
    | `Use in Codex / Claude terminal` |  | меню: меню записи AI Inbox |  | [Консоль ИИ](ourplancore-ai-console.md) |
    | `Refresh Inbox` |  | меню: меню записи AI Inbox |  | [ИИ и терминалы](ourplancore-ai.md) |

??? note "меню записи AI Inbox > Crop (4)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Open Crop` |  | меню: меню записи AI Inbox > Crop |  | [ИИ и терминалы](ourplancore-ai.md) |
    | `Open Crop Folder` |  | меню: меню записи AI Inbox > Crop |  | [ИИ и терминалы](ourplancore-ai.md) |
    | `Bookmark Crop For Batch AI` |  | меню: меню записи AI Inbox > Crop |  | [ИИ и терминалы](ourplancore-ai.md) |
    | `Open Bookmark JSON` |  | меню: меню записи AI Inbox > Crop |  |  |

??? note "меню записи AI Inbox > Marker (8)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Edit Marker` |  | меню: меню записи AI Inbox > Marker |  | [ИИ и терминалы](ourplancore-ai.md) |
    | `Delete Marker` |  | меню: меню записи AI Inbox > Marker |  | [ИИ и терминалы](ourplancore-ai.md) |
    | `Find Similar From Marker` |  | меню: меню записи AI Inbox > Marker |  | [ИИ и терминалы](ourplancore-ai.md) |
    | `Create Marker Set From Filter` |  | меню: меню записи AI Inbox > Marker |  | [ИИ и терминалы](ourplancore-ai.md) |
    | `Manage Marker Sets...` |  | меню: меню записи AI Inbox > Marker |  | [ИИ и терминалы](ourplancore-ai.md) |
    | `Export Marker Context` |  | меню: меню записи AI Inbox > Marker |  | [ИИ и терминалы](ourplancore-ai.md) |
    | `Hide This Marker Type` |  | меню: меню записи AI Inbox > Marker |  | [ИИ и терминалы](ourplancore-ai.md) |
    | `Show All Marker Types` |  | меню: меню записи AI Inbox > Marker |  | [ИИ и терминалы](ourplancore-ai.md) |

??? note "меню записи AI Inbox > AI Response (5)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Add Manual AI Response` |  | меню: меню записи AI Inbox > AI Response |  | [ИИ и терминалы](ourplancore-ai.md) |
    | `Preview Action Draft` |  | меню: меню записи AI Inbox > AI Response |  | [ИИ и терминалы](ourplancore-ai.md) |
    | `Review Action Draft` |  | меню: меню записи AI Inbox > AI Response |  | [ИИ и терминалы](ourplancore-ai.md) |
    | `Apply Sheet Metadata Response` |  | меню: меню записи AI Inbox > AI Response |  | [ИИ и терминалы](ourplancore-ai.md) |
    | `Clear Action Preview` |  | меню: меню записи AI Inbox > AI Response |  | [ИИ и терминалы](ourplancore-ai.md) |

??? note "меню записи AI Inbox > Files (5)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Open Request JSON` |  | меню: меню записи AI Inbox > Files |  | [ИИ и терминалы](ourplancore-ai.md) |
    | `Open Layer JSON` |  | меню: меню записи AI Inbox > Files |  |  |
    | `Open Response JSON` |  | меню: меню записи AI Inbox > Files |  |  |
    | `Open Action Draft JSON` |  | меню: меню записи AI Inbox > Files |  |  |
    | `Open Marker JSON` |  | меню: меню записи AI Inbox > Files |  |  |

??? note "меню Count Display (символ метки Count) (1)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Symbol: Cross, Square, Star, Triangle, Diamond, Ring, Circle` |  | меню: меню Count Display (символ метки Count) |  | [Инструменты замера](ourplancore-tools.md) |

??? note "меню кнопки символа Count по умолчанию (нижняя полоса) (1)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Symbol: Cross, Square, Star, Triangle, Diamond, Ring, Circle` |  | меню: меню кнопки символа Count по умолчанию (нижняя полоса) |  | [Инструменты замера](ourplancore-tools.md) |

??? note "меню вьюпорта в отдельном окне листа (10)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Copy Measurement` |  | меню: меню вьюпорта в отдельном окне листа |  | [Правка и привязки](ourplancore-editing.md) |
    | `Show on This Sheet` |  | меню: меню вьюпорта в отдельном окне листа |  | [Листы (Pages)](ourplancore-pages.md) |
    | `Paste Measurements to This Sheet` |  | меню: меню вьюпорта в отдельном окне листа |  | [Правка и привязки](ourplancore-editing.md) |
    | `Takeoff Properties...` |  | меню: меню вьюпорта в отдельном окне листа |  | [Листы (Pages)](ourplancore-pages.md) |
    | `Measurement Properties...` |  | меню: меню вьюпорта в отдельном окне листа |  | [Листы (Pages)](ourplancore-pages.md) |
    | `Rename Measurement` |  | меню: меню вьюпорта в отдельном окне листа |  | [Правка и привязки](ourplancore-editing.md) |
    | `Use Area As Joists...` |  | меню: меню вьюпорта в отдельном окне листа |  | [Инструменты замера](ourplancore-tools.md) |
    | `Refresh Regular Joists in All Area Segments` |  | меню: меню вьюпорта в отдельном окне листа |  | [Инструменты замера](ourplancore-tools.md) |
    | `Set / Reset Joist Direction` |  | меню: меню вьюпорта в отдельном окне листа |  | [Инструменты замера](ourplancore-tools.md) |
    | `Delete Nearest Extra Joist` |  | меню: меню вьюпорта в отдельном окне листа |  | [Правка и привязки](ourplancore-editing.md) |

??? note "меню пресетов толщины линий (лента Viewport) (1)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Custom...` |  | меню: меню пресетов толщины линий (лента Viewport) |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |

??? note "меню пресетов размера точек (лента Viewport) (1)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Custom...` |  | меню: меню пресетов размера точек (лента Viewport) |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |

??? note "меню вьюпорта > размер легенды / шапки (1)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Custom...` |  | меню: меню вьюпорта > размер легенды / шапки |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |

??? note "меню кнопки Size (лента Display) (1)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Custom...` |  | меню: меню кнопки Size (лента Display) |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |

??? note "меню вьюпорта: легенда и подписи (4)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Scale Legend With Sheet` |  | меню: меню вьюпорта: легенда и подписи |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Scale Measurement Labels With Sheet` |  | меню: меню вьюпорта: легенда и подписи |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Scale Sheet Header With Sheet` |  | меню: меню вьюпорта: легенда и подписи |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Legend` |  | меню: меню вьюпорта: легенда и подписи |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |

??? note "меню строки Estimating (5)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Go to Page` |  | меню: меню строки Estimating |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Select on Canvas` |  | меню: меню строки Estimating |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Measurement Properties...` |  | меню: меню строки Estimating |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Rename Measurement` |  | меню: меню строки Estimating |  | [Правка и привязки](ourplancore-editing.md) |
    | `Delete Measurement` |  | меню: меню строки Estimating |  | [Правка и привязки](ourplancore-editing.md) |

??? note "меню кнопки Export (панель Takeoffs) (6)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Save` |  | меню: меню кнопки Export (панель Takeoffs) |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Save As...` |  | меню: меню кнопки Export (панель Takeoffs) |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Export CSV` |  | меню: меню кнопки Export (панель Takeoffs) |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Export TXT` |  | меню: меню кнопки Export (панель Takeoffs) |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Export Excel` |  | меню: меню кнопки Export (панель Takeoffs) |  | [Экспорт в Excel](ourplancore-excel.md) |
    | `Export to Current Excel` |  | меню: меню кнопки Export (панель Takeoffs) |  | [Экспорт в Excel](ourplancore-excel.md) |

??? note "меню кнопки Open / Import > Open A Project (1)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Open project...` |  | меню: меню кнопки Open / Import > Open A Project |  | [Проекты и сохранение](job-creation-storage.md) |

??? note "меню кнопки Open / Import > Create A New Job (8)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Blank project - start empty` |  | меню: меню кнопки Open / Import > Create A New Job |  | [Проекты и сохранение](job-creation-storage.md) |
    | `New project from a folder of PDFs...` |  | меню: меню кнопки Open / Import > Create A New Job |  | [Проекты и сохранение](job-creation-storage.md) |
    | `Import PDF Takeoffs...` |  | меню: меню кнопки Open / Import > Create A New Job |  | [Прочее](ourplancore-extras-other.md) |
    | `Sample job (demo to explore)` |  | меню: меню кнопки Open / Import > Create A New Job |  | [Проекты и сохранение](job-creation-storage.md) |
    | `Undo Last Page Sort` |  | меню: меню кнопки Open / Import > Create A New Job |  | [Правка и привязки](ourplancore-editing.md) |
    | `Undo Last Page Operation` |  | меню: меню кнопки Open / Import > Create A New Job |  | [Правка и привязки](ourplancore-editing.md) |
    | `Project Data Recovery...` |  | меню: меню кнопки Open / Import > Create A New Job |  | [Проекты и сохранение](job-creation-storage.md) |
    | `Manage job folders...` |  | меню: меню кнопки Open / Import > Create A New Job |  | [Проекты и сохранение](job-creation-storage.md) |

??? note "меню кнопки Open / Import > Import into the current job > Create A New Job (4)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `PDF file(s)...` |  | меню: меню кнопки Open / Import > Import into the current job > Create A New Job |  | [Проекты и сохранение](job-creation-storage.md) |
    | `Folder of PDFs...` |  | меню: меню кнопки Open / Import > Import into the current job > Create A New Job |  | [Проекты и сохранение](job-creation-storage.md) |
    | `OurPlanCore project...` |  | меню: меню кнопки Open / Import > Import into the current job > Create A New Job |  | [Проекты и сохранение](job-creation-storage.md) |
    | `PlanSwift project...` |  | меню: меню кнопки Open / Import > Import into the current job > Create A New Job |  | [Проекты и сохранение](job-creation-storage.md) |

??? note "меню кнопки Batch Rotate (лента Page) (3)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Rotate Selected Left` |  | меню: меню кнопки Batch Rotate (лента Page) |  | [Правка и привязки](ourplancore-editing.md) |
    | `Rotate Selected Right` |  | меню: меню кнопки Batch Rotate (лента Page) |  | [Правка и привязки](ourplancore-editing.md) |
    | `Rotate Selected 180` |  | меню: меню кнопки Batch Rotate (лента Page) |  | [Правка и привязки](ourplancore-editing.md) |

??? note "меню легенды листа > Legend Group (2)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `New Group...` |  | меню: меню легенды листа > Legend Group |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Main Legend` |  | меню: меню легенды листа > Legend Group |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |

??? note "меню папки в Pages (7)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Undo Last Page Delete` |  | меню: меню папки в Pages |  | [Правка и привязки](ourplancore-editing.md) |
    | `New Blank Sheet` |  | меню: меню папки в Pages |  | [Листы (Pages)](ourplancore-pages.md) |
    | `Batch Overlay...` |  | меню: меню папки в Pages |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `New Folder` |  | меню: меню папки в Pages |  | [Листы (Pages)](ourplancore-pages.md) |
    | `Rename Folder` |  | меню: меню папки в Pages |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Delete Folder` |  | меню: меню папки в Pages |  | [Правка и привязки](ourplancore-editing.md) |
    | `Open in Explorer` |  | меню: меню папки в Pages |  | [Листы (Pages)](ourplancore-pages.md) |

??? note "меню папки в Pages > Clipboard (3)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Copy Folder` |  | меню: меню папки в Pages > Clipboard |  | [Правка и привязки](ourplancore-editing.md) |
    | `Cut Folder` |  | меню: меню папки в Pages > Clipboard |  | [Правка и привязки](ourplancore-editing.md) |
    | `Paste Into Folder` |  | меню: меню папки в Pages > Clipboard |  | [Правка и привязки](ourplancore-editing.md) |

??? note "меню папки в Pages > Organize (13)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Auto Create Folders` |  | меню: меню папки в Pages > Organize |  | [Листы (Pages)](ourplancore-pages.md) |
    | `Move Up` |  | меню: меню папки в Pages > Organize |  | [Листы (Pages)](ourplancore-pages.md) |
    | `Move Down` |  | меню: меню папки в Pages > Organize |  | [Листы (Pages)](ourplancore-pages.md) |
    | `Sort Children A-Z` |  | меню: меню папки в Pages > Organize |  | [Листы (Pages)](ourplancore-pages.md) |
    | `Sort Children Z-A` |  | меню: меню папки в Pages > Organize |  | [Листы (Pages)](ourplancore-pages.md) |
    | `Sort Sheet Legends Auto in Folder` |  | меню: меню папки в Pages > Organize |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Sort Sheet Legends A-Z in Folder` |  | меню: меню папки в Pages > Organize |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Sort Sheet Legends by Key (before space) in Folder` |  | меню: меню папки в Pages > Organize |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Reset Sheet Legend Orders in Folder` |  | меню: меню папки в Pages > Organize |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Sort A/S in This Folder` |  | меню: меню папки в Pages > Organize |  | [Листы (Pages)](ourplancore-pages.md) |
    | `Sort D/Sec/WT in This Folder` |  | меню: меню папки в Pages > Organize |  | [Листы (Pages)](ourplancore-pages.md) |
    | `Undo Last Page Sort` |  | меню: меню папки в Pages > Organize |  | [Правка и привязки](ourplancore-editing.md) |
    | `Repair Measurement Links` |  | меню: меню папки в Pages > Organize |  | [Листы (Pages)](ourplancore-pages.md) |

??? note "меню папки в Pages > PDF Metadata (5)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Analyze PDF Metadata` |  | меню: меню папки в Pages > PDF Metadata |  | [Листы (Pages)](ourplancore-pages.md) |
    | `Auto Rename from PDF...` |  | меню: меню папки в Pages > PDF Metadata |  | [Правка и привязки](ourplancore-editing.md) |
    | `Auto Scale from PDF...` |  | меню: меню папки в Pages > PDF Metadata |  | [Листы (Pages)](ourplancore-pages.md) |
    | `Auto Rename + Scale from PDF...` |  | меню: меню папки в Pages > PDF Metadata |  | [Правка и привязки](ourplancore-editing.md) |
    | `Queue GPT Metadata Fallback` |  | меню: меню папки в Pages > PDF Metadata |  | [ИИ и терминалы](ourplancore-ai.md) |

??? note "меню папки в Pages > Learning (3)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Capture Final Learning Snapshot` |  | меню: меню папки в Pages > Learning |  |  |
    | `Review Project Learned Rules...` |  | меню: меню папки в Pages > Learning |  |  |
    | `Review Global Learned Rules...` |  | меню: меню папки в Pages > Learning |  |  |

??? note "меню листа в Pages (13)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Open in New Tab` |  | меню: меню листа в Pages |  | [Листы (Pages)](ourplancore-pages.md) |
    | `Open Selected in New Tabs` |  | меню: меню листа в Pages |  | [Листы (Pages)](ourplancore-pages.md) |
    | `Detach Sheet to Window` |  | меню: меню листа в Pages |  | [Листы (Pages)](ourplancore-pages.md) |
    | `Tile Sheet on Monitor 2` |  | меню: меню листа в Pages |  | [Листы (Pages)](ourplancore-pages.md) |
    | `Set Scale...` |  | меню: меню листа в Pages |  | [Листы (Pages)](ourplancore-pages.md) |
    | `Apply Current Sheet Scale` |  | меню: меню листа в Pages |  | [Листы (Pages)](ourplancore-pages.md) |
    | `Export Sheet to PDF...` |  | меню: меню листа в Pages |  | [PDF и сдача](ourplancore-pdf.md) |
    | `Rename Page` |  | меню: меню листа в Pages |  | [Листы (Pages)](ourplancore-pages.md) |
    | `Delete Page` |  | меню: меню листа в Pages |  | [Правка и привязки](ourplancore-editing.md) |
    | `Duplicate Page` |  | меню: меню листа в Pages |  | [Листы (Pages)](ourplancore-pages.md) |
    | `New Blank Sheet in Parent` |  | меню: меню листа в Pages |  | [Листы (Pages)](ourplancore-pages.md) |
    | `Change Sheet Size...` |  | меню: меню листа в Pages |  | [Листы (Pages)](ourplancore-pages.md) |
    | `Open Page Folder in Explorer` |  | меню: меню листа в Pages |  |  |

??? note "меню листа в Pages > Clipboard (3)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Copy Page` |  | меню: меню листа в Pages > Clipboard |  | [Правка и привязки](ourplancore-editing.md) |
    | `Cut Page` |  | меню: меню листа в Pages > Clipboard |  | [Правка и привязки](ourplancore-editing.md) |
    | `Paste Into Parent Folder` |  | меню: меню листа в Pages > Clipboard |  | [Правка и привязки](ourplancore-editing.md) |

??? note "меню листа в Pages > Organize (12)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Move Up` |  | меню: меню листа в Pages > Organize |  | [Листы (Pages)](ourplancore-pages.md) |
    | `Move Down` |  | меню: меню листа в Pages > Organize |  | [Листы (Pages)](ourplancore-pages.md) |
    | `Move to Folder...` |  | меню: меню листа в Pages > Organize |  | [Листы (Pages)](ourplancore-pages.md) |
    | `Sort Sheet Legend Auto` |  | меню: меню листа в Pages > Organize |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Sort Sheet Legend A-Z` |  | меню: меню листа в Pages > Organize |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Sort Sheet Legend by Key (before space)` |  | меню: меню листа в Pages > Organize |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Reset Sheet Legend Order` |  | меню: меню листа в Pages > Organize |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Legend Groups...` |  | меню: меню листа в Pages > Organize |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Copy Legend Groups to Selected Sheets` |  | меню: меню листа в Pages > Organize |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Sort A/S into Arch/Struct` |  | меню: меню листа в Pages > Organize |  | [Листы (Pages)](ourplancore-pages.md) |
    | `Sort D/Sec/WT by Suffix` |  | меню: меню листа в Pages > Organize |  | [Листы (Pages)](ourplancore-pages.md) |
    | `Repair Measurement Links` |  | меню: меню листа в Pages > Organize |  | [Листы (Pages)](ourplancore-pages.md) |

??? note "меню листа в Pages > PDF Metadata (6)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Analyze PDF Metadata` |  | меню: меню листа в Pages > PDF Metadata |  | [Листы (Pages)](ourplancore-pages.md) |
    | `Auto Rename from PDF...` |  | меню: меню листа в Pages > PDF Metadata |  | [Правка и привязки](ourplancore-editing.md) |
    | `Auto Scale from PDF...` |  | меню: меню листа в Pages > PDF Metadata |  | [Листы (Pages)](ourplancore-pages.md) |
    | `Auto Rename + Scale from PDF...` |  | меню: меню листа в Pages > PDF Metadata |  | [Правка и привязки](ourplancore-editing.md) |
    | `Queue GPT Metadata Fallback` |  | меню: меню листа в Pages > PDF Metadata |  | [ИИ и терминалы](ourplancore-ai.md) |
    | `Open source_pdf.json` |  | меню: меню листа в Pages > PDF Metadata |  |  |

??? note "меню листа в Pages > Learning (3)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Capture Final Learning Snapshot` |  | меню: меню листа в Pages > Learning |  |  |
    | `Review Project Learned Rules...` |  | меню: меню листа в Pages > Learning |  |  |
    | `Review Global Learned Rules...` |  | меню: меню листа в Pages > Learning |  |  |

??? note "меню вкладки листа (5)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Detach Tab to Window` |  | меню: меню вкладки листа |  | [Листы (Pages)](ourplancore-pages.md) |
    | `Tile Tab on Monitor 2` |  | меню: меню вкладки листа |  | [Листы (Pages)](ourplancore-pages.md) |
    | `Detach All ... Tabs to Windows` |  | меню: меню вкладки листа |  | [Листы (Pages)](ourplancore-pages.md) |
    | `Tile All ... Tabs on Monitor 2` |  | меню: меню вкладки листа |  | [Листы (Pages)](ourplancore-pages.md) |
    | `Close Tab` |  | меню: меню вкладки листа |  | [Листы (Pages)](ourplancore-pages.md) |

??? note "меню легенды листа (позиция под листом в Pages) (13)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Select Linked Takeoff` |  | меню: меню легенды листа (позиция под листом в Pages) |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Rename Linked Takeoff...` |  | меню: меню легенды листа (позиция под листом в Pages) |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Show on This Sheet` |  | меню: меню легенды листа (позиция под листом в Pages) |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Hide Selected on This Sheet` |  | меню: меню легенды листа (позиция под листом в Pages) |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Show Selected on This Sheet` |  | меню: меню легенды листа (позиция под листом в Pages) |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Move Backward` |  | меню: меню легенды листа (позиция под листом в Pages) |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Move Forward` |  | меню: меню легенды листа (позиция под листом в Pages) |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Move Up in Legend` |  | меню: меню легенды листа (позиция под листом в Pages) |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Move Down in Legend` |  | меню: меню легенды листа (позиция под листом в Pages) |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Sort Sheet Legend Auto` |  | меню: меню легенды листа (позиция под листом в Pages) |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Sort Sheet Legend A-Z` |  | меню: меню легенды листа (позиция под листом в Pages) |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Sort Sheet Legend by Key (before space)` |  | меню: меню легенды листа (позиция под листом в Pages) |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Reset Sheet Legend Order` |  | меню: меню легенды листа (позиция под листом в Pages) |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |

??? note "меню слоя PDF (Pages > PDF Layers) (9)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Save Layer Info for AI` |  | меню: меню слоя PDF (Pages > PDF Layers) |  | [Привязки и трассировка](ourplancore-snap-trace.md) |
    | `Queue AI Request for This Layer` |  | меню: меню слоя PDF (Pages > PDF Layers) |  | [Привязки и трассировка](ourplancore-snap-trace.md) |
    | `Use for Layer Trace` |  | меню: меню слоя PDF (Pages > PDF Layers) |  | [Привязки и трассировка](ourplancore-snap-trace.md) |
    | `Trace Full Layer to Takeoff` |  | меню: меню слоя PDF (Pages > PDF Layers) |  | [Привязки и трассировка](ourplancore-snap-trace.md) |
    | `Trace Nearest Edge to Takeoff` |  | меню: меню слоя PDF (Pages > PDF Layers) |  | [Привязки и трассировка](ourplancore-snap-trace.md) |
    | `Trace Point to Takeoff` |  | меню: меню слоя PDF (Pages > PDF Layers) |  | [Привязки и трассировка](ourplancore-snap-trace.md) |
    | `Trace All Edges to Takeoff` |  | меню: меню слоя PDF (Pages > PDF Layers) |  | [Привязки и трассировка](ourplancore-snap-trace.md) |
    | `Show Layer` |  | меню: меню слоя PDF (Pages > PDF Layers) |  | [Привязки и трассировка](ourplancore-snap-trace.md) |
    | `Highlight Layer` |  | меню: меню слоя PDF (Pages > PDF Layers) |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |

??? note "меню вьюпорта: кроп (Crop to Sheet) (12)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Open Source Sheet (...)` |  | меню: меню вьюпорта: кроп (Crop to Sheet) |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Open Source Sheet (...)` |  | меню: меню вьюпорта: кроп (Crop to Sheet) |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Rotate Crop 90° Clockwise` |  | меню: меню вьюпорта: кроп (Crop to Sheet) |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Rotate Crop 90° Counterclockwise` |  | меню: меню вьюпорта: кроп (Crop to Sheet) |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Mirror Crop Horizontal` |  | меню: меню вьюпорта: кроп (Crop to Sheet) |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Mirror Crop Vertical` |  | меню: меню вьюпорта: кроп (Crop to Sheet) |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Reset Crop to 100% (true scale)` |  | меню: меню вьюпорта: кроп (Crop to Sheet) |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Opacity...` |  | меню: меню вьюпорта: кроп (Crop to Sheet) |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Bring to Front` |  | меню: меню вьюпорта: кроп (Crop to Sheet) |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Send to Back` |  | меню: меню вьюпорта: кроп (Crop to Sheet) |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Bring Forward` |  | меню: меню вьюпорта: кроп (Crop to Sheet) |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Send Backward` |  | меню: меню вьюпорта: кроп (Crop to Sheet) |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |

??? note "меню листа в Pages > Sheet Overlay (5)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Overlay Properties...` |  | меню: меню листа в Pages > Sheet Overlay |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Use This Sheet as Current Overlay` |  | меню: меню листа в Pages > Sheet Overlay |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Add This Sheet as New Overlay` |  | меню: меню листа в Pages > Sheet Overlay |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Overlay Properties...` |  | меню: меню листа в Pages > Sheet Overlay |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Clear Current Sheet Overlay` |  | меню: меню листа в Pages > Sheet Overlay |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |

??? note "меню слоя наложения (под листом в Pages) (7)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Overlay Properties...` |  | меню: меню слоя наложения (под листом в Pages) |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Open Overlay Sheet` |  | меню: меню слоя наложения (под листом в Pages) |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Show Overlay` |  | меню: меню слоя наложения (под листом в Pages) |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Open Overlay Sheet` |  | меню: меню слоя наложения (под листом в Pages) |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Move Layer Up` |  | меню: меню слоя наложения (под листом в Pages) |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Move Layer Down` |  | меню: меню слоя наложения (под листом в Pages) |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Remove Overlay Layer` |  | меню: меню слоя наложения (под листом в Pages) |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |

??? note "меню вьюпорта: наложение листа (3)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Overlay Properties...` |  | меню: меню вьюпорта: наложение листа |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Auto Fit Overlay` |  | меню: меню вьюпорта: наложение листа |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Fit by 2 Points` |  | меню: меню вьюпорта: наложение листа |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |

??? note "меню More активной позиции (панель Takeoffs) (5)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Properties...` |  | меню: меню More активной позиции (панель Takeoffs) |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Find in Tree` |  | меню: меню More активной позиции (панель Takeoffs) |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Sheet Targets...` |  | меню: меню More активной позиции (панель Takeoffs) |  | [Листы (Pages)](ourplancore-pages.md) |
    | `Previous Target` |  | меню: меню More активной позиции (панель Takeoffs) |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Next Target` |  | меню: меню More активной позиции (панель Takeoffs) |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |

??? note "меню Sheet активной позиции (панель Takeoffs) (1)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Next Sheet Target` |  | меню: меню Sheet активной позиции (панель Takeoffs) |  | [Листы (Pages)](ourplancore-pages.md) |

??? note "меню секции (замера) в Takeoffs (18)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Section Properties...` |  | меню: меню секции (замера) в Takeoffs |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Set Notes...` |  | меню: меню секции (замера) в Takeoffs |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Rename Section` |  | меню: меню секции (замера) в Takeoffs |  | [Правка и привязки](ourplancore-editing.md) |
    | `Go to Page` |  | меню: меню секции (замера) в Takeoffs |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Select on Canvas` |  | меню: меню секции (замера) в Takeoffs |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Merge Segment...` |  | меню: меню секции (замера) в Takeoffs |  | [Правка и привязки](ourplancore-editing.md) |
    | `Split Segment...` |  | меню: меню секции (замера) в Takeoffs |  | [Правка и привязки](ourplancore-editing.md) |
    | `Create Count Points Along ... Lines...` |  | меню: меню секции (замера) в Takeoffs |  | [Правка и привязки](ourplancore-editing.md) |
    | `Break ... Lines Into Segments` |  | меню: меню секции (замера) в Takeoffs |  | [Правка и привязки](ourplancore-editing.md) |
    | `Count Points At ... Line Ends...` |  | меню: меню секции (замера) в Takeoffs |  | [Правка и привязки](ourplancore-editing.md) |
    | `Create Line Grid...` |  | меню: меню секции (замера) в Takeoffs |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Refresh Regular Joists in All Area Segments` |  | меню: меню секции (замера) в Takeoffs |  | [Инструменты замера](ourplancore-tools.md) |
    | `Start Extra Joists Mode (D)` | `D` | меню: меню секции (замера) в Takeoffs |  | [Инструменты замера](ourplancore-tools.md) |
    | `Set / Reset Joist Direction` |  | меню: меню секции (замера) в Takeoffs |  | [Инструменты замера](ourplancore-tools.md) |
    | `Set Direction for All Areas` |  | меню: меню секции (замера) в Takeoffs |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Move Up` |  | меню: меню секции (замера) в Takeoffs |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Move Down` |  | меню: меню секции (замера) в Takeoffs |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Delete Section` |  | меню: меню секции (замера) в Takeoffs |  | [Правка и привязки](ourplancore-editing.md) |

??? note "меню позиции в Takeoffs (17)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Set Active Target` |  | меню: меню позиции в Takeoffs |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `New Section` |  | меню: меню позиции в Takeoffs |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Create Line Grid...` |  | меню: меню позиции в Takeoffs |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Trace Walls Inside Area...` |  | меню: меню позиции в Takeoffs |  | [Привязки и трассировка](ourplancore-snap-trace.md) |
    | `Create Count Points Along Lines...` |  | меню: меню позиции в Takeoffs |  | [Правка и привязки](ourplancore-editing.md) |
    | `Break Lines Into Segments` |  | меню: меню позиции в Takeoffs |  | [Правка и привязки](ourplancore-editing.md) |
    | `Count Points At Line Ends...` |  | меню: меню позиции в Takeoffs |  | [Правка и привязки](ourplancore-editing.md) |
    | `Find Similar...` |  | меню: меню позиции в Takeoffs |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Merge Selected Takeoffs...` |  | меню: меню позиции в Takeoffs |  | [Правка и привязки](ourplancore-editing.md) |
    | `Split Selected Takeoffs...` |  | меню: меню позиции в Takeoffs |  | [Правка и привязки](ourplancore-editing.md) |
    | `Undo Takeoff Merge / Split` |  | меню: меню позиции в Takeoffs |  | [Правка и привязки](ourplancore-editing.md) |
    | `Rename...` |  | меню: меню позиции в Takeoffs |  | [Правка и привязки](ourplancore-editing.md) |
    | `Delete item + measurements` |  | меню: меню позиции в Takeoffs |  | [Правка и привязки](ourplancore-editing.md) |
    | `Duplicate Item` |  | меню: меню позиции в Takeoffs |  | [Правка и привязки](ourplancore-editing.md) |
    | `Properties...` |  | меню: меню позиции в Takeoffs |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Bulk Properties...` |  | меню: меню позиции в Takeoffs |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Set Unit Price` |  | меню: меню позиции в Takeoffs |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |

??? note "меню позиции в Takeoffs > Joist (5)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Use Area As Joists...` |  | меню: меню позиции в Takeoffs > Joist |  | [Инструменты замера](ourplancore-tools.md) |
    | `Refresh Regular Joists in All Area Segments` |  | меню: меню позиции в Takeoffs > Joist |  | [Инструменты замера](ourplancore-tools.md) |
    | `Start Extra Joists Mode (D)` | `D` | меню: меню позиции в Takeoffs > Joist |  | [Инструменты замера](ourplancore-tools.md) |
    | `Set / Reset Joist Direction` |  | меню: меню позиции в Takeoffs > Joist |  | [Инструменты замера](ourplancore-tools.md) |
    | `Set Direction for All Areas` |  | меню: меню позиции в Takeoffs > Joist |  | [Инструменты замера](ourplancore-tools.md) |

??? note "меню позиции в Takeoffs > Clipboard (3)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Copy Item` |  | меню: меню позиции в Takeoffs > Clipboard |  | [Правка и привязки](ourplancore-editing.md) |
    | `Cut Item` |  | меню: меню позиции в Takeoffs > Clipboard |  | [Правка и привязки](ourplancore-editing.md) |
    | `Paste Into Parent Folder` |  | меню: меню позиции в Takeoffs > Clipboard |  | [Правка и привязки](ourplancore-editing.md) |

??? note "меню позиции в Takeoffs > Organize (2)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Move Up` |  | меню: меню позиции в Takeoffs > Organize |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Move Down` |  | меню: меню позиции в Takeoffs > Organize |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |

??? note "меню папки в Takeoffs (8)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `New Folder` |  | меню: меню папки в Takeoffs |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `New Item` |  | меню: меню папки в Takeoffs |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Rename Folder...` |  | меню: меню папки в Takeoffs |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Delete folder + children` |  | меню: меню папки в Takeoffs |  | [Правка и привязки](ourplancore-editing.md) |
    | `Folder Properties...` |  | меню: меню папки в Takeoffs |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Bulk Item Properties...` |  | меню: меню папки в Takeoffs |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Random Colors for Items` |  | меню: меню папки в Takeoffs |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Open in Explorer` |  | меню: меню папки в Takeoffs |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |

??? note "меню папки в Takeoffs > Clipboard (4)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Copy Folder` |  | меню: меню папки в Takeoffs > Clipboard |  | [Правка и привязки](ourplancore-editing.md) |
    | `Cut Folder` |  | меню: меню папки в Takeoffs > Clipboard |  | [Правка и привязки](ourplancore-editing.md) |
    | `Paste Into Folder` |  | меню: меню папки в Takeoffs > Clipboard |  | [Правка и привязки](ourplancore-editing.md) |
    | `Duplicate Folder` |  | меню: меню папки в Takeoffs > Clipboard |  | [Правка и привязки](ourplancore-editing.md) |

??? note "меню папки в Takeoffs > Organize (6)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Auto Create Tree` |  | меню: меню папки в Takeoffs > Organize |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Create Folders From Pages` |  | меню: меню папки в Takeoffs > Organize |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Move Up` |  | меню: меню папки в Takeoffs > Organize |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Move Down` |  | меню: меню папки в Takeoffs > Organize |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Sort Children A-Z` |  | меню: меню папки в Takeoffs > Organize |  | [Листы (Pages)](ourplancore-pages.md) |
    | `Sort Children Z-A` |  | меню: меню папки в Takeoffs > Organize |  | [Листы (Pages)](ourplancore-pages.md) |

??? note "меню корня Takeoffs (6)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Auto Create Tree` |  | меню: меню корня Takeoffs |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Create Folders From Pages` |  | меню: меню корня Takeoffs |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Paste Into Root` |  | меню: меню корня Takeoffs |  | [Правка и привязки](ourplancore-editing.md) |
    | `Sort Root A-Z` |  | меню: меню корня Takeoffs |  | [Листы (Pages)](ourplancore-pages.md) |
    | `Sort Root Z-A` |  | меню: меню корня Takeoffs |  | [Листы (Pages)](ourplancore-pages.md) |
    | `Open Takeoffs in Explorer` |  | меню: меню корня Takeoffs |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |

??? note "меню позиции в Takeoffs > 3D (2)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Wall` |  | меню: меню позиции в Takeoffs > 3D |  | [3D и менеджеры](ourplancore-3d.md) |
    | `Roof Base from Area` |  | меню: меню позиции в Takeoffs > 3D |  | [3D крыша](ourplancore-3d-roof.md) |

??? note "меню панели Templates (8)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Create New Takeoff` |  | меню: меню панели Templates |  | [Прочее](ourplancore-extras-other.md) |
    | `Add Folder` |  | меню: меню панели Templates |  | [Проекты и сохранение](job-creation-storage.md) |
    | `Add Line` |  | меню: меню панели Templates |  |  |
    | `Add Area` |  | меню: меню панели Templates |  |  |
    | `Add Count` |  | меню: меню панели Templates |  | [Инструменты замера](ourplancore-tools.md) |
    | `Edit` |  | меню: меню панели Templates |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Duplicate` |  | меню: меню панели Templates |  | [Правка и привязки](ourplancore-editing.md) |
    | `Delete` |  | меню: меню панели Templates |  | [Правка и привязки](ourplancore-editing.md) |

??? note "меню вьюпорта > 3D (3)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Create Roof Base from Areas` |  | меню: меню вьюпорта > 3D |  | [3D крыша](ourplancore-3d-roof.md) |
    | `Roof Edge Select` |  | меню: меню вьюпорта > 3D |  | [3D крыша](ourplancore-3d-roof.md) |
    | `Clear Roof Base` |  | меню: меню вьюпорта > 3D |  | [3D крыша](ourplancore-3d-roof.md) |

??? note "меню вьюпорта > 3D (ребро крыши) (4)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Add Edge to Selection` |  | меню: меню вьюпорта > 3D (ребро крыши) |  | [3D крыша](ourplancore-3d-roof.md) |
    | `Clear Edge Selection` |  | меню: меню вьюпорта > 3D (ребро крыши) |  | [3D крыша](ourplancore-3d-roof.md) |
    | `Set Edge as Eave + Pitch ...` |  | меню: меню вьюпорта > 3D (ребро крыши) |  | [3D крыша](ourplancore-3d-roof.md) |
    | `Set Edge as Rake` |  | меню: меню вьюпорта > 3D (ребро крыши) |  | [3D крыша](ourplancore-3d-roof.md) |

??? note "меню вьюпорта (правый клик по листу) (1)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Open Project Context` |  | меню: меню вьюпорта (правый клик по листу) |  | [Проекты и сохранение](job-creation-storage.md) |

??? note "меню вьюпорта: буфер замеров (4)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Copy Measurement` |  | меню: меню вьюпорта: буфер замеров |  | [Правка и привязки](ourplancore-editing.md) |
    | `Paste Measurements to This Sheet` |  | меню: меню вьюпорта: буфер замеров |  | [Правка и привязки](ourplancore-editing.md) |
    | `Merge Segment...` |  | меню: меню вьюпорта: буфер замеров |  | [Правка и привязки](ourplancore-editing.md) |
    | `Split Segment...` |  | меню: меню вьюпорта: буфер замеров |  | [Правка и привязки](ourplancore-editing.md) |

??? note "меню вьюпорта > AI Assist (точка листа) (12)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `AI crop here -> note` |  | меню: меню вьюпорта > AI Assist (точка листа) |  | [ИИ и терминалы](ourplancore-ai.md) |
    | `AI quick box here -> note` |  | меню: меню вьюпорта > AI Assist (точка листа) |  | [ИИ и терминалы](ourplancore-ai.md) |
    | `Save AI crop here` |  | меню: меню вьюпорта > AI Assist (точка листа) |  | [ИИ и терминалы](ourplancore-ai.md) |
    | `Save AI marker here` |  | меню: меню вьюпорта > AI Assist (точка листа) |  | [ИИ и терминалы](ourplancore-ai.md) |
    | `Ask AI about this point / area` |  | меню: меню вьюпорта > AI Assist (точка листа) |  | [ИИ и терминалы](ourplancore-ai.md) |
    | `Read text near point` |  | меню: меню вьюпорта > AI Assist (точка листа) |  | [ИИ и терминалы](ourplancore-ai.md) |
    | `Save observation here` |  | меню: меню вьюпорта > AI Assist (точка листа) |  | [ИИ и терминалы](ourplancore-ai.md) |
    | `Add as pending check` |  | меню: меню вьюпорта > AI Assist (точка листа) |  | [ИИ и терминалы](ourplancore-ai.md) |
    | `Suggest takeoff item here` |  | меню: меню вьюпорта > AI Assist (точка листа) |  | [ИИ и терминалы](ourplancore-ai.md) |
    | `Trace wall from this point` |  | меню: меню вьюпорта > AI Assist (точка листа) |  | [Привязки и трассировка](ourplancore-snap-trace.md) |
    | `Trace closed area` |  | меню: меню вьюпорта > AI Assist (точка листа) |  | [ИИ и терминалы](ourplancore-ai.md) |
    | `Check missed takeoffs on this page` |  | меню: меню вьюпорта > AI Assist (точка листа) |  | [ИИ и терминалы](ourplancore-ai.md) |

??? note "меню вьюпорта: разметка (annotation) (4)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Copy Markup` |  | меню: меню вьюпорта: разметка (annotation) |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Paste Markups Here` |  | меню: меню вьюпорта: разметка (annotation) |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Edit Note...` |  | меню: меню вьюпорта: разметка (annotation) |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Delete Markup` |  | меню: меню вьюпорта: разметка (annotation) |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |

??? note "меню вьюпорта > AI Assist (замер) (7)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `AI crop here -> note` |  | меню: меню вьюпорта > AI Assist (замер) |  | [ИИ и терминалы](ourplancore-ai.md) |
    | `Save measurement AI crop` |  | меню: меню вьюпорта > AI Assist (замер) |  | [ИИ и терминалы](ourplancore-ai.md) |
    | `Save measurement as AI marker` |  | меню: меню вьюпорта > AI Assist (замер) |  | [ИИ и терминалы](ourplancore-ai.md) |
    | `Explain measurement` |  | меню: меню вьюпорта > AI Assist (замер) |  | [ИИ и терминалы](ourplancore-ai.md) |
    | `Find similar` |  | меню: меню вьюпорта > AI Assist (замер) |  | [ИИ и терминалы](ourplancore-ai.md) |
    | `Link to observation` |  | меню: меню вьюпорта > AI Assist (замер) |  | [ИИ и терминалы](ourplancore-ai.md) |
    | `Create note from measurement` |  | меню: меню вьюпорта > AI Assist (замер) |  | [ИИ и терминалы](ourplancore-ai.md) |

??? note "меню Attach (терминал) (1)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Refresh` |  | меню: меню Attach (терминал) |  | [Консоль ИИ](ourplancore-ai-console.md) |

??? note "меню More (терминал) (2)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Detach to window` |  | меню: меню More (терминал) |  | [Консоль ИИ](ourplancore-ai-console.md) |
    | `Settings -> Terminals` |  | меню: меню More (терминал) |  | [Консоль ИИ](ourplancore-ai-console.md) |

??? note "меню Style (лента Annotation) (8)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Highlighter` |  | меню: меню Style (лента Annotation) |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Draw line` |  | меню: меню Style (лента Annotation) |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Arrow` |  | меню: меню Style (лента Annotation) |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Box` |  | меню: меню Style (лента Annotation) |  | [Привязки и трассировка](ourplancore-snap-trace.md) |
    | `Cloud` |  | меню: меню Style (лента Annotation) |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Area fill` |  | меню: меню Style (лента Annotation) |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Hide area (white)` |  | меню: меню Style (лента Annotation) |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Note` |  | меню: меню Style (лента Annotation) |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |

??? note "меню вьюпорта: выбранный замер (16)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Takeoff Properties...` |  | меню: меню вьюпорта: выбранный замер |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Measurement Properties...` |  | меню: меню вьюпорта: выбранный замер |  | [Дополнительно](ourplancore-extras.md) |
    | `Trace Walls Inside Area...` |  | меню: меню вьюпорта: выбранный замер |  | [Привязки и трассировка](ourplancore-snap-trace.md) |
    | `Use Area As Joists...` |  | меню: меню вьюпорта: выбранный замер |  | [Инструменты замера](ourplancore-tools.md) |
    | `Refresh Regular Joists in All Area Segments` |  | меню: меню вьюпорта: выбранный замер |  | [Инструменты замера](ourplancore-tools.md) |
    | `Start Extra Joists Mode (D)` | `D` | меню: меню вьюпорта: выбранный замер |  | [Инструменты замера](ourplancore-tools.md) |
    | `Delete Nearest Extra Joist` |  | меню: меню вьюпорта: выбранный замер |  | [Правка и привязки](ourplancore-editing.md) |
    | `Set / Reset Joist Direction` |  | меню: меню вьюпорта: выбранный замер |  | [Инструменты замера](ourplancore-tools.md) |
    | `Set Direction for All Areas` |  | меню: меню вьюпорта: выбранный замер |  | [Дополнительно](ourplancore-extras.md) |
    | `Create Count Points Along ... Lines...` |  | меню: меню вьюпорта: выбранный замер |  | [Правка и привязки](ourplancore-editing.md) |
    | `Break ... Lines Into Segments` |  | меню: меню вьюпорта: выбранный замер |  | [Правка и привязки](ourplancore-editing.md) |
    | `Count Points At ... Line Ends...` |  | меню: меню вьюпорта: выбранный замер |  | [Правка и привязки](ourplancore-editing.md) |
    | `Rename Measurement` |  | меню: меню вьюпорта: выбранный замер |  | [Правка и привязки](ourplancore-editing.md) |
    | `Insert Vertex Here` |  | меню: меню вьюпорта: выбранный замер |  | [Правка и привязки](ourplancore-editing.md) |
    | `Remove Nearest Vertex` |  | меню: меню вьюпорта: выбранный замер |  | [Правка и привязки](ourplancore-editing.md) |
    | `Delete Measurement` |  | меню: меню вьюпорта: выбранный замер |  | [Правка и привязки](ourplancore-editing.md) |

## Кнопки панелей и окон, которые строятся в коде (20)

??? note "окно Observation Details (6)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Go to Page` |  | панель: окно Observation Details |  | [ИИ и терминалы](ourplancore-ai.md) |
    | `Open Crop` |  | панель: окно Observation Details |  | [ИИ и терминалы](ourplancore-ai.md) |
    | `Request JSON` |  | панель: окно Observation Details |  | [ИИ и терминалы](ourplancore-ai.md) |
    | `Run AI` |  | панель: окно Observation Details |  | [ИИ и терминалы](ourplancore-ai.md) |
    | `AI Response` |  | панель: окно Observation Details |  | [ИИ и терминалы](ourplancore-ai.md) |
    | `Project Context` |  | панель: окно Observation Details |  | [ИИ и терминалы](ourplancore-ai.md) |

??? note "панель 3D Massing (AI Inbox) (12)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Build 3D Draft` |  | панель: панель 3D Massing (AI Inbox) | Build AI_Context/3d_massing/model.json from current AI markers | [3D и менеджеры](ourplancore-3d.md) |
    | `3D From Takeoffs` |  | панель: панель 3D Massing (AI Inbox) | Build 3D draft from Walls/Areas/Sqft level Line/Area measurements |  |
    | `AI 3D Sort` |  | панель: панель 3D Massing (AI Inbox) | Send takeoff metadata to OpenAI for structured role/level sorting, then build the 3D draft deterministically |  |
    | `3D Window` |  | панель: панель 3D Massing (AI Inbox) | Open a separate orbitable 3D viewport with saved marker points |  |
    | `Auto Roof` |  | панель: панель 3D Massing (AI Inbox) | Queue reviewable AI roof marker candidates from the active sheet |  |
    | `Review Roof` |  | панель: панель 3D Massing (AI Inbox) | Review and save roof type, pitch, notes, and guide points before accepting roof geometry | [3D и менеджеры](ourplancore-3d.md) |
    | `Review Openings` |  | панель: панель 3D Massing (AI Inbox) | Review projected door/window/opening markers before accepting the 3D draft |  |
    | `Accept 3D` |  | панель: панель 3D Massing (AI Inbox) | Mark the current 3D massing draft as reviewed project context | [3D и менеджеры](ourplancore-3d.md) |
    | `Open JSON` |  | панель: панель 3D Massing (AI Inbox) | Open AI_Context/3d_massing/model.json | [ИИ и терминалы](ourplancore-ai.md) |
    | `Jump` |  | панель: панель 3D Massing (AI Inbox) | Open the source marker sheet |  |
    | `Marker JSON` |  | панель: панель 3D Massing (AI Inbox) | Open the selected source marker JSON |  |
    | `Crop` |  | панель: панель 3D Massing (AI Inbox) | Open the selected source marker crop | [Консоль ИИ](ourplancore-ai-console.md) |

??? note "окно Export PDF (предпросмотр) (1)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Preview` |  | панель: окно Export PDF (предпросмотр) | Preview the current sheet's exported PDF. Updates live when PDF Output settings change. | [PDF и сдача](ourplancore-pdf.md) |

??? note "окно PlanSwift Import Complete (1)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Open Report` |  | панель: окно PlanSwift Import Complete |  |  |

## Палитра команд (Ctrl+Shift+P) (126)

??? note "File (28)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Open / Import` | `Ctrl+O` | палитра команд: File | Open the job picker. The top toolbar button also contains PDF import. | [Проекты и сохранение](job-creation-storage.md) |
    | `Open Project File` |  | палитра команд: File | Open a portable .ourplan project file. | [Проекты и сохранение](job-creation-storage.md) |
    | `Open Recent Job` | `Ctrl+Shift+O` | палитра команд: File | Open the Recent Jobs picker. | [Проекты и сохранение](job-creation-storage.md) |
    | `Open Jobs Folder` |  | палитра команд: File | Open a root folder that contains multiple jobs. | [Проекты и сохранение](job-creation-storage.md) |
    | `New PDF Job` |  | палитра команд: File | Create a new OurPlanCore job from a folder of PDFs. | [Проекты и сохранение](job-creation-storage.md) |
    | `Blank Job` |  | палитра команд: File | Create an empty OurPlanCore job without selecting PDFs. | [Проекты и сохранение](job-creation-storage.md) |
    | `Create Sample Job` |  | палитра команд: File | Create and open a guided local sample project. | [Проекты и сохранение](job-creation-storage.md) |
    | `Import PlanSwift Job` |  | палитра команд: File | Convert a read-only PlanSwift job into a new OurPlanCore job. | [Проекты и сохранение](job-creation-storage.md) |
    | `Import PlanSwift to Current Job` |  | палитра команд: File | Import a read-only PlanSwift job under 01. planswift in the current job. | [Проекты и сохранение](job-creation-storage.md) |
    | `Import PDF(s)` |  | палитра команд: File | Import one or many PDF files into the current job. | [Проекты и сохранение](job-creation-storage.md) |
    | `Import PDF Folder` |  | палитра команд: File | Recursively import every PDF file from a selected folder into the current job. | [Проекты и сохранение](job-creation-storage.md) |
    | `Import PDF Takeoffs` |  | палитра команд: File | Create a new job from PDF takeoffs or import PDF rulers/takeoffs into the current job. | [Прочее](ourplancore-extras-other.md) |
    | `Export PDF` |  | палитра команд: File | Export selected/all sheets to a PDF. | [PDF и сдача](ourplancore-pdf.md) |
    | `Save` | `Ctrl+S` | палитра команд: File | Save current takeoff data. | [Проекты и сохранение](job-creation-storage.md) |
    | `Save As` | `Ctrl+Shift+S` | палитра команд: File | Save the active project to a new location using its current format. | [Проекты и сохранение](job-creation-storage.md) |
    | `Export CSV` |  | палитра команд: File | Export takeoff rows to CSV. | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Export TXT` |  | палитра команд: File | Export selected/all takeoffs in PlanSwift text format. | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Export Excel` |  | палитра команд: File | Export selected/all takeoffs to .xlsx columns J/K/L from J10. | [Экспорт в Excel](ourplancore-excel.md) |
    | `Export to Current Excel` |  | палитра команд: File | Write selected takeoff folder/item rows to the active cell in an open Excel workbook. | [Экспорт в Excel](ourplancore-excel.md) |
    | `Export Values to Current Excel` |  | палитра команд: File | Write only the Value column for the same selected takeoff scope. | [Экспорт в Excel](ourplancore-excel.md) |
    | `Excel Macro: SQFT` |  | палитра команд: File | Append selected SQFT rows to TemplateCom and run A2_SQFT_calc. | [Экспорт в Excel](ourplancore-excel.md) |
    | `Excel Macro: Walls` |  | палитра команд: File | Append selected wall rows with numeric floor groups and run A3_Walls_Calc_AllGroup. | [Экспорт в Excel](ourplancore-excel.md) |
    | `Excel Macro: Openings` |  | палитра команд: File | Append openings from Z158, group near window values per floor, then run A5_Openings. | [Экспорт в Excel](ourplancore-excel.md) |
    | `Excel Macro: Gables` |  | палитра команд: File | Append selected Gables rows and run A2_SQFT_calc. | [Экспорт в Excel](ourplancore-excel.md) |
    | `Excel Macro: Truss Heel` |  | палитра команд: File | Append selected Truss Heel rows and run A2_SQFT_calc. | [Экспорт в Excel](ourplancore-excel.md) |
    | `Excel Macro: Parapet` |  | палитра команд: File | Append selected Parapet rows and run A4_Parapet. | [Экспорт в Excel](ourplancore-excel.md) |
    | `Excel Macro: Eve / Rakes` |  | палитра команд: File | Append selected Eves and Rakes rows and run A6_Eve_Rakes. | [Экспорт в Excel](ourplancore-excel.md) |
    | `Excel Macro: ALL` |  | палитра команд: File | Run the configured Excel macro sequence for one selected building/root. | [Экспорт в Excel](ourplancore-excel.md) |

??? note "View (14)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Fit Page` | `F` | палитра команд: View | Fit the active page to the viewport. | [Инструменты замера](ourplancore-tools.md) |
    | `Zoom In` | `Ctrl++` | палитра команд: View | Zoom into the active page. | [Горячие клавиши](ourplancore-shortcuts.md) |
    | `Zoom Out` | `Ctrl+-` | палитра команд: View | Zoom out of the active page. | [Горячие клавиши](ourplancore-shortcuts.md) |
    | `Add Bookmark` | `B, K` | палитра команд: View | Name and save the active sheet and current zoom/pan as a bookmark. | [Горячие клавиши](ourplancore-shortcuts.md) |
    | `Hide / Show All Takeoffs` |  | палитра команд: View | Toggle current takeoffs on the active sheet. New measurements stay visible. | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Hide Selected Takeoffs Only` | `H` | палитра команд: View | Turn off visibility for the whole takeoff of each selected segment on this sheet. No selection leaves visibility unchanged; use the takeoff visibility switch to show it again. | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Toggle Dark Theme` |  | палитра команд: View | Switch between light and dark UI theme. | [Начало работы](ourplancore-start.md) |
    | `Page Background` |  | палитра команд: View | Open page background presets. | [Settings и модули](ourplancore-settings.md) |
    | `Toggle AI Inbox` |  | палитра команд: View | Collapse or expand the AI Inbox panel. | [ИИ и терминалы](ourplancore-ai.md) |
    | `Quick Calculator` |  | палитра команд: View | Toggle the slide-out calculator with feet-inches math. | [Workspace, Job Tracker, CLI](ourplancore-workspace.md) |
    | `Codex / Claude Terminal` |  | палитра команд: View | Show or hide the terminal panel with live plan, AI crop and bookmark context. | [Консоль ИИ](ourplancore-ai-console.md) |
    | `Show Takeoffs Tab` |  | палитра команд: View | Select the Takeoffs workspace tab. | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Show Estimating Tab` |  | палитра команд: View | Select the Estimating workspace tab. | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Show 3D Tab` |  | палитра команд: View | Select the right-side 3D wall viewer tab. | [3D и менеджеры](ourplancore-3d.md) |

??? note "Workspace (7)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Show Main View` |  | палитра команд: Workspace | Switch to the drawing canvas workspace. | [Проекты и сохранение](job-creation-storage.md) |
    | `Show Sheet Manager` |  | палитра команд: Workspace | Switch to the sheet table / PDF metadata workspace. | [Листы (Pages)](ourplancore-pages.md) |
    | `Show Takeoff Manager` |  | палитра команд: Workspace | Switch to the takeoff item manager workspace. | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Show Report Builder` |  | палитра команд: Workspace | Switch to the spreadsheet-style report builder workspace. | [Менеджеры](ourplancore-managers.md) |
    | `Show Materials` |  | палитра команд: Workspace | Switch to the material extraction workspace. | [Менеджеры](ourplancore-managers.md) |
    | `Show AI Manager` |  | палитра команд: Workspace | Switch to the AI inbox and marker manager workspace. | [ИИ и терминалы](ourplancore-ai.md) |
    | `Show 3D Viewer` |  | палитра команд: Workspace | Switch to the clean 3D viewer workspace. | [3D и менеджеры](ourplancore-3d.md) |

??? note "Tools (22)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Select Tool` | `E` | палитра команд: Tools | Use box selection and measurement editing. | [Инструменты замера](ourplancore-tools.md) |
    | `Pan Tool` | `V` | палитра команд: Tools | Use left-button panning; right-button pan still works. | [Инструменты замера](ourplancore-tools.md) |
    | `Scale Tool` | `S` | палитра команд: Tools | Draw a calibration line for sheet scale. | [Инструменты замера](ourplancore-tools.md) |
    | `Ruler Tool` | `R` | палитра команд: Tools | Measure a temporary distance without creating a takeoff. | [Инструменты замера](ourplancore-tools.md) |
    | `Pitch Tool` |  | палитра команд: Tools | Draw a two-point roof-slope line and show its rise per 12. | [Инструменты замера](ourplancore-tools.md) |
    | `Highlighter Tool` | `Shift+H` | палитра команд: Tools | Draw a transparent highlighter markup. | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Draw Line / Extra Joists` | `D` | палитра команд: Tools | D toggles continuous Extra Joists for one selected Joist Area segment; otherwise it selects Draw Line. | [Инструменты замера](ourplancore-tools.md) |
    | `Draw Box Tool` |  | палитра команд: Tools | Draw a page annotation box. | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Note Tool` | `N` | палитра команд: Tools | Write a text note on the active sheet. | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Count Tool` | `P` | палитра команд: Tools | Record count marks into a takeoff item. | [Инструменты замера](ourplancore-tools.md) |
    | `Similar Count` |  | палитра команд: Tools | Find look-alike symbols on the active sheet, name the result, and add reviewed markers as a Count item. | [Инструменты замера](ourplancore-tools.md) |
    | `Points Along Line(s)` |  | палитра команд: Tools | Create Count points along the selected Line measurement(s) at a spacing. | [Правка и привязки](ourplancore-editing.md) |
    | `Line Tool` | `L` | палитра команд: Tools | Record line measurements into a takeoff item. | [Инструменты замера](ourplancore-tools.md) |
    | `Area Tool` | `A` | палитра команд: Tools | Record area measurements into a takeoff item. | [Инструменты замера](ourplancore-tools.md) |
    | `J Area Tool` | `J` | палитра команд: Tools | Create a joist area takeoff and record area measurements. | [Инструменты замера](ourplancore-tools.md) |
    | `Beam Tool` | `B` | палитра команд: Tools | Measure a beam length, create a Count item, and place the first Count mark. | [Инструменты замера](ourplancore-tools.md) |
    | `Openings Tool` | `O` | палитра команд: Tools | Measure an opening box, create a size-only Count item, and place the mark in the center. | [Инструменты замера](ourplancore-tools.md) |
    | `Area Cut Tool` | `X` | палитра команд: Tools | Cut a hole out of the selected area measurement. | [Правка и привязки](ourplancore-editing.md) |
    | `Toggle Record` | `Space` | палитра команд: Tools | Toggle digitizer record mode for the current drawing tool. | [Инструменты замера](ourplancore-tools.md) |
    | `Toggle Snap` | `F3` | палитра команд: Tools | Toggle snap to existing takeoff points. | [Привязки и трассировка](ourplancore-snap-trace.md) |
    | `Toggle PDF Snap` | `Ctrl+F3` | палитра команд: Tools | Toggle snap to PDF vector corners and points. | [Привязки и трассировка](ourplancore-snap-trace.md) |
    | `Toggle Ortho` | `F8` | палитра команд: Tools | Toggle horizontal/vertical Ortho; Shift temporarily forces it. | [Привязки и трассировка](ourplancore-snap-trace.md) |

??? note "Edit (12)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Copy Selected Measurements` | `Ctrl+C` | палитра команд: Edit | Copy the selected measurements. | [Правка и привязки](ourplancore-editing.md) |
    | `Paste Measurements` | `Ctrl+V` | палитра команд: Edit | Paste copied measurements to the active page. | [Правка и привязки](ourplancore-editing.md) |
    | `Merge Selected Takeoffs / Measurements` | `Ctrl+M` | палитра команд: Edit | Merge selected takeoff items from all sheets, or move selected measurement segments into another takeoff. | [Правка и привязки](ourplancore-editing.md) |
    | `Split Selected Takeoffs / Measurements` | `Ctrl+Shift+M` | палитра команд: Edit | Split whole takeoffs across all sheets, or move selected measurements or Count marks into a new takeoff. | [Правка и привязки](ourplancore-editing.md) |
    | `Break Lines Into Segments` | `Ctrl+Shift+B` | палитра команд: Edit | Split every selected multi-segment Line into one measurement per segment in its own takeoff, whatever the H/V dot. The measured total does not change. | [Правка и привязки](ourplancore-editing.md) |
    | `Break Lines Into Horizontal / Vertical` | `Ctrl+Shift+V` | палитра команд: Edit | Break H/V: file every segment of the selected Lines into '<takeoff> - Horizontal' and '<takeoff> - Vertical', whatever the H/V dot. | [Правка и привязки](ourplancore-editing.md) |
    | `Count Points At Line Ends` |  | палитра команд: Edit | Place a Count mark on both ends of every selected Line segment; each source takeoff gets its own Count takeoff. | [Правка и привязки](ourplancore-editing.md) |
    | `Combine Areas: Union` |  | палитра команд: Edit | Merge the selected Areas into one. | [Правка и привязки](ourplancore-editing.md) |
    | `Combine Areas: Subtract` |  | палитра команд: Edit | Subtract the later-selected Areas from the first-selected one. | [Правка и привязки](ourplancore-editing.md) |
    | `Combine Areas: Intersect` |  | палитра команд: Edit | Keep only the region shared by all selected Areas. | [Правка и привязки](ourplancore-editing.md) |
    | `Combine Areas: Remove Overlap` |  | палитра команд: Edit | Trim overlaps between selected Areas so nothing is counted twice; the first-selected Area wins. | [Правка и привязки](ourplancore-editing.md) |
    | `Combine Areas: Divide` |  | палитра команд: Edit | Split selected Areas into exclusive parts plus a separate overlap area. | [Правка и привязки](ourplancore-editing.md) |

??? note "Pages (13)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Sort Pages A-Z` |  | палитра команд: Pages | Sort children of the selected Pages folder (or root) alphabetically. | [Листы (Pages)](ourplancore-pages.md) |
    | `Sort Pages Z-A` |  | палитра команд: Pages | Sort children of the selected Pages folder (or root) in reverse alphabetical order. | [Листы (Pages)](ourplancore-pages.md) |
    | `Sort Pages A/S` |  | палитра команд: Pages | Move A sheets to Arch, S sheets to Struct, and trailing '-' sheets to others. | [Листы (Pages)](ourplancore-pages.md) |
    | `Blank Sheet` |  | палитра команд: Pages | Create an empty sheet in the current job. | [Листы (Pages)](ourplancore-pages.md) |
    | `Sort Pages D/Sec/WT` |  | палитра команд: Pages | Move suffix sheets into details/sections/units and reorder v/wt/ft/sv/sw at Pages root. | [Листы (Pages)](ourplancore-pages.md) |
    | `Repair Measurement Links` |  | палитра команд: Pages | Reconnect stale measurement page links after page renames/imports. | [Листы (Pages)](ourplancore-pages.md) |
    | `Auto Page Folders` |  | палитра команд: Pages | Create the standard page folder tree. | [Листы (Pages)](ourplancore-pages.md) |
    | `Auto Name PDF` |  | палитра команд: Pages | Preview and apply PDF sheet names. | [Листы (Pages)](ourplancore-pages.md) |
    | `Auto Scale PDF` |  | палитра команд: Pages | Preview and apply PDF sheet scales. | [Листы (Pages)](ourplancore-pages.md) |
    | `Auto Name + Scale PDF` |  | палитра команд: Pages | Preview and apply PDF sheet names and scales. | [Листы (Pages)](ourplancore-pages.md) |
    | `Set Scale` | `F4` | палитра команд: Pages | Set one scale on the selected sheets, or on the active sheet when there is no Pages selection. | [Листы (Pages)](ourplancore-pages.md) |
    | `Name / Scale Setup` | `F5` | палитра команд: Pages | Open the manual Name / Scale window for the active sheet. | [Листы (Pages)](ourplancore-pages.md) |
    | `AI Fill PDF Metadata` |  | палитра команд: Pages | Queue GPT fallback for missing sheet metadata. | [ИИ и терминалы](ourplancore-ai.md) |

??? note "Sheets (3)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Overlay` |  | палитра команд: Sheets | Choose a matching sheet overlay for the active sheet. | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Batch Overlay` |  | палитра команд: Sheets | Pair target and overlay sheets across the whole job. | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Move Overlay by Points` |  | палитра команд: Sheets | Align the active sheet overlay by matching points. | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |

??? note "Materials (1)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Extract Materials` |  | палитра команд: Materials | Extract material evidence and schedules from the current job PDFs. | [Менеджеры](ourplancore-managers.md) |

??? note "PDF Layers (3)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `PDF Layers All On` |  | палитра команд: PDF Layers | Turn all active page PDF layers on. | [Привязки и трассировка](ourplancore-snap-trace.md) |
    | `PDF Layers All Off` |  | палитра команд: PDF Layers | Turn all active page PDF layers off. | [Привязки и трассировка](ourplancore-snap-trace.md) |
    | `Clear PDF Layer Highlights` |  | палитра команд: PDF Layers | Clear highlighted PDF layers. | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |

??? note "Takeoffs (15)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `New Takeoff Folder` |  | палитра команд: Takeoffs | Create a takeoff folder under the selected/root folder. | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `New Takeoff Item` | `T` | палитра команд: Takeoffs | Create a takeoff item under the selected/root folder. | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Refresh Takeoffs Tree` |  | палитра команд: Takeoffs | Reload the Takeoffs tree from the current job folder. | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Show Active Takeoff` |  | палитра команд: Takeoffs | Scroll the Takeoffs tree to the active target item. | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Active Takeoff Properties` |  | палитра команд: Takeoffs | Edit properties for the active target item. | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Record Active Takeoff` | `Space` | палитра команд: Takeoffs | Start or stop recording into the active target item. | [Инструменты замера](ourplancore-tools.md) |
    | `Previous Takeoff Target` |  | палитра команд: Takeoffs | Switch the active target to the previous takeoff item. | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Next Takeoff Target` |  | палитра команд: Takeoffs | Switch the active target to the next takeoff item. | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Next Sheet Takeoff Target` |  | палитра команд: Takeoffs | Switch to the next takeoff item measured on the active sheet. | [Листы (Pages)](ourplancore-pages.md) |
    | `Sort Takeoffs A-Z` |  | палитра команд: Takeoffs | Sort children of the selected Takeoffs folder (or root) alphabetically. | [Листы (Pages)](ourplancore-pages.md) |
    | `Sort Takeoffs Z-A` |  | палитра команд: Takeoffs | Sort children of the selected Takeoffs folder (or root) in reverse alphabetical order. | [Листы (Pages)](ourplancore-pages.md) |
    | `Sort Takeoffs: Walls` |  | палитра команд: Takeoffs | Sort wall takeoffs in the selected folder and subfolders: ext, corr, dem, then 2x6/2x4 sizes. | [Листы (Pages)](ourplancore-pages.md) |
    | `Sort Takeoffs: Details by Sheet` |  | палитра команд: Takeoffs | Group detail takeoffs like 1/A501 by the sheet after the slash, ordered as in the Pages tree. | [Листы (Pages)](ourplancore-pages.md) |
    | `Auto Takeoff Tree` |  | палитра команд: Takeoffs | Create the standard takeoff folder tree. | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Create Takeoffs From Pages` |  | палитра команд: Takeoffs | Create top takeoff folders from CAPS page/folder names. | [Дерево Takeoffs](ourplancore-takeoffs.md) |

??? note "AI (8)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `OpenAI Settings` |  | палитра команд: AI | Review key status and AI model settings. | [ИИ и терминалы](ourplancore-ai.md) |
    | `Add AI Observation` |  | палитра команд: AI | Save a manual AI observation for the active job/page. | [ИИ и терминалы](ourplancore-ai.md) |
    | `Run Selected AI Request` |  | палитра команд: AI | Run the selected AI Inbox request. | [ИИ и терминалы](ourplancore-ai.md) |
    | `Run New Crop Bookmarks` |  | палитра команд: AI | Send only new crop bookmarks to OpenAI. | [ИИ и терминалы](ourplancore-ai.md) |
    | `Retry Failed Crop Bookmarks` |  | палитра команд: AI | Retry only failed crop bookmarks. | [ИИ и терминалы](ourplancore-ai.md) |
    | `Create Marker Set` |  | палитра команд: AI | Save the current marker filters as a marker set. | [ИИ и терминалы](ourplancore-ai.md) |
    | `Manage Marker Sets` |  | палитра команд: AI | Open marker set management. | [ИИ и терминалы](ourplancore-ai.md) |
    | `Export Marker Context` |  | палитра команд: AI | Export visible marker context JSON. | [ИИ и терминалы](ourplancore-ai.md) |

## Справка по клавишам (F1) (91)

??? note "GLOBAL (18)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Show / close this shortcut guide` | `F1` | F1: GLOBAL |  | [Горячие клавиши](ourplancore-shortcuts.md) |
    | `Close help or cancel the active action` | `Esc` | F1: GLOBAL |  | [Инструменты замера](ourplancore-tools.md) |
    | `Open / import a job` | `Ctrl+O` | F1: GLOBAL |  | [Проекты и сохранение](job-creation-storage.md) |
    | `Open Recent Jobs` | `Ctrl+Shift+O` | F1: GLOBAL |  | [Проекты и сохранение](job-creation-storage.md) |
    | `Save the current job` | `Ctrl+S` | F1: GLOBAL |  | [Проекты и сохранение](job-creation-storage.md) |
    | `Save the current project to a new location` | `Ctrl+Shift+S` | F1: GLOBAL |  | [Проекты и сохранение](job-creation-storage.md) |
    | `Merge selected measurement segments` | `Ctrl+M` | F1: GLOBAL |  | [Правка и привязки](ourplancore-editing.md) |
    | `Split measurements / Count marks` | `Ctrl+Shift+M` | F1: GLOBAL |  | [Правка и привязки](ourplancore-editing.md) |
    | `Break selected Lines into segments` | `Ctrl+Shift+B` | F1: GLOBAL |  | [Правка и привязки](ourplancore-editing.md) |
    | `Break selected Lines into Horizontal / Vertical takeoffs` | `Ctrl+Shift+V` | F1: GLOBAL |  | [Правка и привязки](ourplancore-editing.md) |
    | `Open Command Palette` | `Ctrl+Shift+P` | F1: GLOBAL |  | [Горячие клавиши](ourplancore-shortcuts.md) |
    | `Start / stop Record` | `Space` | F1: GLOBAL |  | [Инструменты замера](ourplancore-tools.md) |
    | `Create a new takeoff item` | `T` | F1: GLOBAL |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Hide selected takeoffs only` | `H` | F1: GLOBAL | One selected segment hides its whole takeoff on this sheet. Restore with its visibility switch. No selection: no change. Roof guide keeps H for Hip | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Add a bookmark` | `B, K` | F1: GLOBAL | Press in sequence within 0.9 sec | [Горячие клавиши](ourplancore-shortcuts.md) |
    | `Set scale on selected sheet(s)` | `F4` | F1: GLOBAL |  | [Листы (Pages)](ourplancore-pages.md) |
    | `Open Name / Scale` | `F5` | F1: GLOBAL |  | [Листы (Pages)](ourplancore-pages.md) |
    | `Collapse Pages and Takeoffs trees` | `-` | F1: GLOBAL |  | [Горячие клавиши](ourplancore-shortcuts.md) |

??? note "DRAWING TOOLS (14)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Pan` | `V` | F1: DRAWING TOOLS |  | [Инструменты замера](ourplancore-tools.md) |
    | `Select` | `E` | F1: DRAWING TOOLS |  | [Инструменты замера](ourplancore-tools.md) |
    | `Scale` | `S` | F1: DRAWING TOOLS |  | [Инструменты замера](ourplancore-tools.md) |
    | `Ruler` | `R` | F1: DRAWING TOOLS |  | [Инструменты замера](ourplancore-tools.md) |
    | `Highlighter` | `Shift+H` | F1: DRAWING TOOLS |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Draw Line / Extra Joists` | `D` | F1: DRAWING TOOLS | One selected Joist Area: toggle continuous mode; D or Esc exits | [Инструменты замера](ourplancore-tools.md) |
    | `Beam` | `B` | F1: DRAWING TOOLS |  | [Инструменты замера](ourplancore-tools.md) |
    | `Openings` | `O` | F1: DRAWING TOOLS |  | [Инструменты замера](ourplancore-tools.md) |
    | `Note` | `N` | F1: DRAWING TOOLS |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Count` | `P` | F1: DRAWING TOOLS |  | [Инструменты замера](ourplancore-tools.md) |
    | `Line` | `L` | F1: DRAWING TOOLS |  | [Инструменты замера](ourplancore-tools.md) |
    | `Area` | `A` | F1: DRAWING TOOLS |  | [Инструменты замера](ourplancore-tools.md) |
    | `Joist Area` | `J` | F1: DRAWING TOOLS |  | [Инструменты замера](ourplancore-tools.md) |
    | `Area Cut` | `X` | F1: DRAWING TOOLS |  | [Правка и привязки](ourplancore-editing.md) |

??? note "VIEWPORT & DRAWING (15)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Complete the current drawing` | `C` | F1: VIEWPORT & DRAWING |  | [Горячие клавиши](ourplancore-shortcuts.md) |
    | `Fit sheet to viewport` | `F` | F1: VIEWPORT & DRAWING |  | [Инструменты замера](ourplancore-tools.md) |
    | `Rename the selected object's takeoff` | `F2` | F1: VIEWPORT & DRAWING |  | [Правка и привязки](ourplancore-editing.md) |
    | `Toggle takeoff-point Snap` | `F3` | F1: VIEWPORT & DRAWING |  | [Привязки и трассировка](ourplancore-snap-trace.md) |
    | `Toggle PDF vector Snap` | `Ctrl+F3` | F1: VIEWPORT & DRAWING |  | [Привязки и трассировка](ourplancore-snap-trace.md) |
    | `Toggle Ortho` | `F8` | F1: VIEWPORT & DRAWING |  | [Привязки и трассировка](ourplancore-snap-trace.md) |
    | `Temporarily force Ortho` | `Shift` | F1: VIEWPORT & DRAWING | While drawing or editing | [Привязки и трассировка](ourplancore-snap-trace.md) |
    | `Toggle Box mode` | `F9` | F1: VIEWPORT & DRAWING |  | [Привязки и трассировка](ourplancore-snap-trace.md) |
    | `Zoom in` | `Ctrl++` | F1: VIEWPORT & DRAWING |  | [Горячие клавиши](ourplancore-shortcuts.md) |
    | `Zoom out` | `Ctrl+-` | F1: VIEWPORT & DRAWING |  | [Горячие клавиши](ourplancore-shortcuts.md) |
    | `Undo viewport action / last point` | `Ctrl+Z / Backspace` | F1: VIEWPORT & DRAWING |  | [Правка и привязки](ourplancore-editing.md) |
    | `Select all objects on active sheet` | `Ctrl+A` | F1: VIEWPORT & DRAWING |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Copy selected measurements / markups` | `Ctrl+C` | F1: VIEWPORT & DRAWING |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Paste at the pointer` | `Ctrl+V` | F1: VIEWPORT & DRAWING |  | [Правка и привязки](ourplancore-editing.md) |
    | `Delete the selected object` | `Delete` | F1: VIEWPORT & DRAWING |  | [Правка и привязки](ourplancore-editing.md) |

??? note "SELECTION MODIFIERS (3)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Add to / toggle selection` | `Ctrl` | F1: SELECTION MODIFIERS |  | [3D крыша](ourplancore-3d-roof.md) |
    | `Remove from selection` | `Ctrl+Shift` | F1: SELECTION MODIFIERS |  | [Горячие клавиши](ourplancore-shortcuts.md) |
    | `Select vertices / handles` | `Alt` | F1: SELECTION MODIFIERS | Click or box-select | [Горячие клавиши](ourplancore-shortcuts.md) |

??? note "PAGES TREE (10)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Clear the Pages selection` | `Esc` | F1: PAGES TREE |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Copy / cut / paste` | `Ctrl+C / X / V` | F1: PAGES TREE |  | [Правка и привязки](ourplancore-editing.md) |
    | `Duplicate with the exact name` | `Ctrl+D` | F1: PAGES TREE |  | [Правка и привязки](ourplancore-editing.md) |
    | `Move page, folder, or legend row` | `Ctrl+Up / Down` | F1: PAGES TREE |  | [Листы (Pages)](ourplancore-pages.md) |
    | `Restore the last Pages deletion` | `Ctrl+Z` | F1: PAGES TREE |  | [Листы (Pages)](ourplancore-pages.md) |
    | `Rename page or folder` | `F2` | F1: PAGES TREE |  | [Правка и привязки](ourplancore-editing.md) |
    | `Delete selected page(s) / folder(s)` | `Delete` | F1: PAGES TREE |  | [Правка и привязки](ourplancore-editing.md) |
    | `Select a range` | `Shift+click` | F1: PAGES TREE |  |  |
    | `Toggle one row` | `Ctrl+click` | F1: PAGES TREE |  |  |
    | `Add a range` | `Ctrl+Shift+click` | F1: PAGES TREE |  |  |

??? note "TAKEOFFS TREE (9)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Copy / cut / paste` | `Ctrl+C / X / V` | F1: TAKEOFFS TREE |  | [Правка и привязки](ourplancore-editing.md) |
    | `Duplicate with the exact name` | `Ctrl+D` | F1: TAKEOFFS TREE |  | [Правка и привязки](ourplancore-editing.md) |
    | `Move item, folder, or section` | `Ctrl+Up / Down` | F1: TAKEOFFS TREE |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Select section measurements on canvas` | `Ctrl+Enter` | F1: TAKEOFFS TREE |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Restore the last takeoff-tree deletion` | `Ctrl+Z` | F1: TAKEOFFS TREE |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Rename item, folder, or section` | `F2` | F1: TAKEOFFS TREE |  | [Правка и привязки](ourplancore-editing.md) |
    | `Delete selected node(s)` | `Delete` | F1: TAKEOFFS TREE |  | [Правка и привязки](ourplancore-editing.md) |
    | `Range / toggle selection` | `Shift / Ctrl+click` | F1: TAKEOFFS TREE |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Start marquee selection from a row` | `Alt+drag` | F1: TAKEOFFS TREE |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |

??? note "BOOKMARKS & AI INBOX (2)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Open the selected bookmark / AI entry` | `Enter` | F1: BOOKMARKS & AI INBOX |  | [Горячие клавиши](ourplancore-shortcuts.md) |
    | `Delete the selected bookmark` | `Delete` | F1: BOOKMARKS & AI INBOX |  | [ИИ и терминалы](ourplancore-ai.md) |

??? note "SHEET OVERLAY (6)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Move the overlay` | `Ctrl+Alt+drag` | F1: SHEET OVERLAY |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Nudge the overlay` | `Ctrl+Alt+Arrows` | F1: SHEET OVERLAY |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Scale the overlay` | `Ctrl+Alt++ / -` | F1: SHEET OVERLAY |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Rotate the overlay` | `Ctrl+Alt+[ / ]` | F1: SHEET OVERLAY |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Reset overlay transform` | `Ctrl+Alt+0` | F1: SHEET OVERLAY |  | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Use fine movement / scale / rotation` | `+ Shift` | F1: SHEET OVERLAY |  |  |

??? note "3D ROOF GUIDE MODE (8)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Ridge guide` | `R` | F1: 3D ROOF GUIDE MODE |  | [3D крыша](ourplancore-3d-roof.md) |
    | `Hip guide` | `H` | F1: 3D ROOF GUIDE MODE |  | [3D крыша](ourplancore-3d-roof.md) |
    | `Valley guide` | `V` | F1: 3D ROOF GUIDE MODE |  | [3D крыша](ourplancore-3d-roof.md) |
    | `Eave guide` | `E` | F1: 3D ROOF GUIDE MODE |  | [3D крыша](ourplancore-3d-roof.md) |
    | `Rake guide` | `K` | F1: 3D ROOF GUIDE MODE |  | [3D крыша](ourplancore-3d-roof.md) |
    | `Pitch guide` | `P` | F1: 3D ROOF GUIDE MODE |  | [3D крыша](ourplancore-3d-roof.md) |
    | `Remove the last guide point` | `Backspace / Ctrl+Z` | F1: 3D ROOF GUIDE MODE |  | [Правка и привязки](ourplancore-editing.md) |
    | `Cancel guide / leave Roof mode` | `Esc` | F1: 3D ROOF GUIDE MODE |  | [3D крыша](ourplancore-3d-roof.md) |

??? note "LAYER TRACE (3)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Cycle edge snap or trace mode / candidate` | `Tab` | F1: LAYER TRACE | After Layer Trace is enabled from its toolbar | [Привязки и трассировка](ourplancore-snap-trace.md) |
    | `Advance the trace workflow` | `Enter` | F1: LAYER TRACE |  | [Привязки и трассировка](ourplancore-snap-trace.md) |
    | `Cancel trace step / leave Layer Trace` | `Esc` | F1: LAYER TRACE |  | [Инструменты замера](ourplancore-tools.md) |

??? note "DIALOGS & LISTS (3)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Accept / open the selected result` | `Enter` | F1: DIALOGS & LISTS |  |  |
    | `Close the active dialog` | `Esc` | F1: DIALOGS & LISTS |  |  |
    | `Navigate palette / picker results` | `Up / Down` | F1: DIALOGS & LISTS |  |  |

## Клавиши по умолчанию, которых нет в палитре (61)

??? note "Workspace (3)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Show / close the shortcut guide` | `F1` | клавиша: Workspace | Default key binding; editable in Settings > Keyboard Shortcuts. | [Горячие клавиши](ourplancore-shortcuts.md) |
    | `Open Command Palette` | `Ctrl+Shift+P` | клавиша: Workspace | Default key binding; editable in Settings > Keyboard Shortcuts. | [Проекты и сохранение](job-creation-storage.md) |
    | `Collapse Pages and Takeoffs trees` | `-` | клавиша: Workspace | Default key binding; editable in Settings > Keyboard Shortcuts. | [Горячие клавиши](ourplancore-shortcuts.md) |

??? note "Viewport (9)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Toggle Box mode` | `F9` | клавиша: Viewport | Default key binding; editable in Settings > Keyboard Shortcuts. | [Привязки и трассировка](ourplancore-snap-trace.md) |
    | `Undo viewport action / last point` | `Ctrl+Z / Backspace` | клавиша: Viewport | Default key binding; editable in Settings > Keyboard Shortcuts. | [Правка и привязки](ourplancore-editing.md) |
    | `Select all objects on active sheet` | `Ctrl+A` | клавиша: Viewport | Default key binding; editable in Settings > Keyboard Shortcuts. | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Delete the selected object` | `Delete` | клавиша: Viewport | Default key binding; editable in Settings > Keyboard Shortcuts. | [Правка и привязки](ourplancore-editing.md) |
    | `Rename the selected object's takeoff` | `F2` | клавиша: Viewport | Default key binding; editable in Settings > Keyboard Shortcuts. | [Правка и привязки](ourplancore-editing.md) |
    | `Complete the current drawing` | `C` | клавиша: Viewport | Default key binding; editable in Settings > Keyboard Shortcuts. | [Горячие клавиши](ourplancore-shortcuts.md) |
    | `Cancel the active action` | `Esc` | клавиша: Viewport | Default key binding; editable in Settings > Keyboard Shortcuts. | [Инструменты замера](ourplancore-tools.md) |
    | `Cycle edge snap or trace mode / candidate` | `Tab` | клавиша: Viewport | Default key binding; editable in Settings > Keyboard Shortcuts. | [Привязки и трассировка](ourplancore-snap-trace.md) |
    | `Advance the trace workflow` | `Enter` | клавиша: Viewport | Default key binding; editable in Settings > Keyboard Shortcuts. | [Привязки и трассировка](ourplancore-snap-trace.md) |

??? note "Pages (10)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Pages tree: copy` | `Ctrl+C` | клавиша: Pages | Default key binding; editable in Settings > Keyboard Shortcuts. | [Правка и привязки](ourplancore-editing.md) |
    | `Pages tree: cut` | `Ctrl+X` | клавиша: Pages | Default key binding; editable in Settings > Keyboard Shortcuts. | [Правка и привязки](ourplancore-editing.md) |
    | `Pages tree: paste` | `Ctrl+V` | клавиша: Pages | Default key binding; editable in Settings > Keyboard Shortcuts. | [Правка и привязки](ourplancore-editing.md) |
    | `Pages tree: duplicate with the exact name` | `Ctrl+D` | клавиша: Pages | Default key binding; editable in Settings > Keyboard Shortcuts. | [Правка и привязки](ourplancore-editing.md) |
    | `Pages tree: move up` | `Ctrl+Up` | клавиша: Pages | Default key binding; editable in Settings > Keyboard Shortcuts. | [Листы (Pages)](ourplancore-pages.md) |
    | `Pages tree: move down` | `Ctrl+Down` | клавиша: Pages | Default key binding; editable in Settings > Keyboard Shortcuts. | [Листы (Pages)](ourplancore-pages.md) |
    | `Pages tree: restore the last deletion` | `Ctrl+Z` | клавиша: Pages | Default key binding; editable in Settings > Keyboard Shortcuts. | [Листы (Pages)](ourplancore-pages.md) |
    | `Pages tree: rename page or folder` | `F2` | клавиша: Pages | Default key binding; editable in Settings > Keyboard Shortcuts. | [Правка и привязки](ourplancore-editing.md) |
    | `Pages tree: delete selected` | `Delete` | клавиша: Pages | Default key binding; editable in Settings > Keyboard Shortcuts. | [Правка и привязки](ourplancore-editing.md) |
    | `Pages tree: clear the selection` | `Esc` | клавиша: Pages | Default key binding; editable in Settings > Keyboard Shortcuts. | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |

??? note "Takeoffs (10)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Takeoffs tree: copy` | `Ctrl+C` | клавиша: Takeoffs | Default key binding; editable in Settings > Keyboard Shortcuts. | [Правка и привязки](ourplancore-editing.md) |
    | `Takeoffs tree: cut` | `Ctrl+X` | клавиша: Takeoffs | Default key binding; editable in Settings > Keyboard Shortcuts. | [Правка и привязки](ourplancore-editing.md) |
    | `Takeoffs tree: paste` | `Ctrl+V` | клавиша: Takeoffs | Default key binding; editable in Settings > Keyboard Shortcuts. | [Правка и привязки](ourplancore-editing.md) |
    | `Takeoffs tree: duplicate with the exact name` | `Ctrl+D` | клавиша: Takeoffs | Default key binding; editable in Settings > Keyboard Shortcuts. | [Правка и привязки](ourplancore-editing.md) |
    | `Takeoffs tree: move up` | `Ctrl+Up` | клавиша: Takeoffs | Default key binding; editable in Settings > Keyboard Shortcuts. | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Takeoffs tree: move down` | `Ctrl+Down` | клавиша: Takeoffs | Default key binding; editable in Settings > Keyboard Shortcuts. | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Takeoffs tree: restore the last deletion` | `Ctrl+Z` | клавиша: Takeoffs | Default key binding; editable in Settings > Keyboard Shortcuts. | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Takeoffs tree: rename item, folder, or section` | `F2` | клавиша: Takeoffs | Default key binding; editable in Settings > Keyboard Shortcuts. | [Правка и привязки](ourplancore-editing.md) |
    | `Takeoffs tree: delete selected node(s)` | `Delete` | клавиша: Takeoffs | Default key binding; editable in Settings > Keyboard Shortcuts. | [Правка и привязки](ourplancore-editing.md) |
    | `Select section measurements on canvas` | `Ctrl+Enter` | клавиша: Takeoffs | Default key binding; editable in Settings > Keyboard Shortcuts. | [Дерево Takeoffs](ourplancore-takeoffs.md) |

??? note "Bookmarks (2)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Open the selected bookmark` | `Enter` | клавиша: Bookmarks | Default key binding; editable in Settings > Keyboard Shortcuts. | [Горячие клавиши](ourplancore-shortcuts.md) |
    | `Delete the selected bookmark` | `Delete` | клавиша: Bookmarks | Default key binding; editable in Settings > Keyboard Shortcuts. | [Правка и привязки](ourplancore-editing.md) |

??? note "Inbox (1)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Open the selected AI entry` | `Enter` | клавиша: Inbox | Default key binding; editable in Settings > Keyboard Shortcuts. | [Горячие клавиши](ourplancore-shortcuts.md) |

??? note "Roof (8)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Ridge guide` | `R` | клавиша: Roof | Default key binding; editable in Settings > Keyboard Shortcuts. | [3D крыша](ourplancore-3d-roof.md) |
    | `Hip guide` | `H` | клавиша: Roof | Default key binding; editable in Settings > Keyboard Shortcuts. | [3D крыша](ourplancore-3d-roof.md) |
    | `Valley guide` | `V` | клавиша: Roof | Default key binding; editable in Settings > Keyboard Shortcuts. | [3D крыша](ourplancore-3d-roof.md) |
    | `Eave guide` | `E` | клавиша: Roof | Default key binding; editable in Settings > Keyboard Shortcuts. | [3D крыша](ourplancore-3d-roof.md) |
    | `Rake guide` | `K` | клавиша: Roof | Default key binding; editable in Settings > Keyboard Shortcuts. | [3D крыша](ourplancore-3d-roof.md) |
    | `Pitch guide` | `P` | клавиша: Roof | Default key binding; editable in Settings > Keyboard Shortcuts. | [3D крыша](ourplancore-3d-roof.md) |
    | `Cancel guide / leave Roof mode` | `Esc` | клавиша: Roof | Default key binding; editable in Settings > Keyboard Shortcuts. | [3D крыша](ourplancore-3d-roof.md) |
    | `Remove the last guide point` | `Backspace / Ctrl+Z` | клавиша: Roof | Default key binding; editable in Settings > Keyboard Shortcuts. | [Правка и привязки](ourplancore-editing.md) |

??? note "Overlay (18)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Nudge the overlay left` | `Ctrl+Alt+Left` | клавиша: Overlay | Default key binding; editable in Settings > Keyboard Shortcuts. | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Nudge the overlay right` | `Ctrl+Alt+Right` | клавиша: Overlay | Default key binding; editable in Settings > Keyboard Shortcuts. | [Горячие клавиши](ourplancore-shortcuts.md) |
    | `Nudge the overlay up` | `Ctrl+Alt+Up` | клавиша: Overlay | Default key binding; editable in Settings > Keyboard Shortcuts. | [Горячие клавиши](ourplancore-shortcuts.md) |
    | `Nudge the overlay down` | `Ctrl+Alt+Down` | клавиша: Overlay | Default key binding; editable in Settings > Keyboard Shortcuts. | [Горячие клавиши](ourplancore-shortcuts.md) |
    | `Scale the overlay up` | `Ctrl+Alt++` | клавиша: Overlay | Default key binding; editable in Settings > Keyboard Shortcuts. | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Scale the overlay down` | `Ctrl+Alt+-` | клавиша: Overlay | Default key binding; editable in Settings > Keyboard Shortcuts. | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Rotate the overlay left` | `Ctrl+Alt+[` | клавиша: Overlay | Default key binding; editable in Settings > Keyboard Shortcuts. | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Rotate the overlay right` | `Ctrl+Alt+]` | клавиша: Overlay | Default key binding; editable in Settings > Keyboard Shortcuts. | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Reset overlay transform` | `Ctrl+Alt+0` | клавиша: Overlay | Default key binding; editable in Settings > Keyboard Shortcuts. | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Fine nudge the overlay left` | `Ctrl+Alt+Shift+Left` | клавиша: Overlay | Default key binding; editable in Settings > Keyboard Shortcuts. | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Fine nudge the overlay right` | `Ctrl+Alt+Shift+Right` | клавиша: Overlay | Default key binding; editable in Settings > Keyboard Shortcuts. | [Горячие клавиши](ourplancore-shortcuts.md) |
    | `Fine nudge the overlay up` | `Ctrl+Alt+Shift+Up` | клавиша: Overlay | Default key binding; editable in Settings > Keyboard Shortcuts. | [Горячие клавиши](ourplancore-shortcuts.md) |
    | `Fine nudge the overlay down` | `Ctrl+Alt+Shift+Down` | клавиша: Overlay | Default key binding; editable in Settings > Keyboard Shortcuts. | [Горячие клавиши](ourplancore-shortcuts.md) |
    | `Fine scale the overlay up` | `Ctrl+Alt+Shift++` | клавиша: Overlay | Default key binding; editable in Settings > Keyboard Shortcuts. | [Горячие клавиши](ourplancore-shortcuts.md) |
    | `Fine scale the overlay down` | `Ctrl+Alt+Shift+-` | клавиша: Overlay | Default key binding; editable in Settings > Keyboard Shortcuts. | [Горячие клавиши](ourplancore-shortcuts.md) |
    | `Fine rotate the overlay left` | `Ctrl+Alt+Shift+[` | клавиша: Overlay | Default key binding; editable in Settings > Keyboard Shortcuts. | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Fine rotate the overlay right` | `Ctrl+Alt+Shift+]` | клавиша: Overlay | Default key binding; editable in Settings > Keyboard Shortcuts. | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Reset overlay transform (fine)` | `Ctrl+Alt+Shift+0` | клавиша: Overlay | Default key binding; editable in Settings > Keyboard Shortcuts. | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |

## Settings: категории и разделы (45)

??? note "Settings, категория (20)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Modules` |  | Settings: Settings, категория | Settings category (default, presets, per-job override). | [Settings и модули](ourplancore-settings.md) |
    | `Page Folders` |  | Settings: Settings, категория | Settings category (default, presets, per-job override). | [Settings и модули](ourplancore-settings.md) |
    | `Blank Sheets` |  | Settings: Settings, категория | Settings category (default, presets, per-job override). | [Settings и модули](ourplancore-settings.md) |
    | `Auto Tree` |  | Settings: Settings, категория | Settings category (default, presets, per-job override). | [Settings и модули](ourplancore-settings.md) |
    | `From Pages` |  | Settings: Settings, категория | Settings category (default, presets, per-job override). | [Settings и модули](ourplancore-settings.md) |
    | `Takeoff Templates` |  | Settings: Settings, категория | Settings category (default, presets, per-job override). | [Settings и модули](ourplancore-settings.md) |
    | `Sheet Takeoff Routing` |  | Settings: Settings, категория | Settings category (default, presets, per-job override). | [Settings и модули](ourplancore-settings.md) |
    | `Takeoff Name Routing` |  | Settings: Settings, категория | Settings category (default, presets, per-job override). | [Settings и модули](ourplancore-settings.md) |
    | `Takeoff Colors` |  | Settings: Settings, категория | Settings category (default, presets, per-job override). | [Settings и модули](ourplancore-settings.md) |
    | `AI Crop Notes` |  | Settings: Settings, категория | Settings category (default, presets, per-job override). | [ИИ и терминалы](ourplancore-ai.md) |
    | `Sort A/S` |  | Settings: Settings, категория | Settings category (default, presets, per-job override). | [Settings и модули](ourplancore-settings.md) |
    | `Sort D/Sec/WT` |  | Settings: Settings, категория | Settings category (default, presets, per-job override). | [Settings и модули](ourplancore-settings.md) |
    | `Auto Rename / Scale` |  | Settings: Settings, категория | Settings category (default, presets, per-job override). | [Settings и модули](ourplancore-settings.md) |
    | `Excel Actions` |  | Settings: Settings, категория | Settings category (default, presets, per-job override). | [Экспорт в Excel](ourplancore-excel.md) |
    | `Project Storage` |  | Settings: Settings, категория | Settings category (default, presets, per-job override). | [Settings и модули](ourplancore-settings.md) |
    | `Agent Bridge` |  | Settings: Settings, категория | Settings category (default, presets, per-job override). | [Settings и модули](ourplancore-settings.md) |
    | `Terminals` |  | Settings: Settings, категория | Settings category (default, presets, per-job override). | [Консоль ИИ](ourplancore-ai-console.md) |
    | `Workspace` |  | Settings: Settings, категория | Settings category (default, presets, per-job override). | [Settings и модули](ourplancore-settings.md) |
    | `Keyboard Shortcuts` |  | Settings: Settings, категория | Settings category (default, presets, per-job override). | [Settings и модули](ourplancore-settings.md) |
    | `Defaults` |  | Settings: Settings, категория | Settings category (default, presets, per-job override). | [Settings и модули](ourplancore-settings.md) |

??? note "Settings > Defaults (6)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Beam annotation line` |  | Settings: Settings > Defaults | Section of the settings panel. | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Viewport interaction` |  | Settings: Settings > Defaults | Section of the settings panel. | [Settings и модули](ourplancore-settings.md) |
    | `Background performance` |  | Settings: Settings > Defaults | Section of the settings panel. | [Settings и модули](ourplancore-settings.md) |
    | `Tree display` |  | Settings: Settings > Defaults | Section of the settings panel. | [Settings и модули](ourplancore-settings.md) |
    | `Display & export defaults` |  | Settings: Settings > Defaults | Section of the settings panel. | [Settings и модули](ourplancore-settings.md) |
    | `Sheet Manager raster DPI presets` |  | Settings: Settings > Defaults | Section of the settings panel. | [Settings и модули](ourplancore-settings.md) |

??? note "Settings > Excel Actions (4)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Excel macro actions` |  | Settings: Settings > Excel Actions | Section of the settings panel. | [Экспорт в Excel](ourplancore-excel.md) |
    | `Floor folder matching` |  | Settings: Settings > Excel Actions | Section of the settings panel. | [Экспорт в Excel](ourplancore-excel.md) |
    | `Framing folders -> Excel blocks` |  | Settings: Settings > Excel Actions | Section of the settings panel. | [Экспорт в Excel](ourplancore-excel.md) |
    | `Walls extras: sheathing, shear walls, shaft, units, balconies` |  | Settings: Settings > Excel Actions | Section of the settings panel. | [Экспорт в Excel](ourplancore-excel.md) |

??? note "Settings > Project Storage (6)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Project format` |  | Settings: Settings > Project Storage | Section of the settings panel. | [Settings и модули](ourplancore-settings.md) |
    | `Current project` |  | Settings: Settings > Project Storage | Section of the settings panel. | [Settings и модули](ourplancore-settings.md) |
    | `Storage breakdown` |  | Settings: Settings > Project Storage | Section of the settings panel. | [Settings и модули](ourplancore-settings.md) |
    | `Safe compact preview` |  | Settings: Settings > Project Storage | Section of the settings panel. | [Settings и модули](ourplancore-settings.md) |
    | `Review-only findings` |  | Settings: Settings > Project Storage | Section of the settings panel. | [Settings и модули](ourplancore-settings.md) |
    | `Details` |  | Settings: Settings > Project Storage | Section of the settings panel. | [Settings и модули](ourplancore-settings.md) |

??? note "Settings > Auto Rename / Scale (4)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Deterministic Auto Name / Scale policy` |  | Settings: Settings > Auto Rename / Scale | Section of the settings panel. | [Settings и модули](ourplancore-settings.md) |
    | `Evidence, confidence, and preservation` |  | Settings: Settings > Auto Rename / Scale | Section of the settings panel. | [Settings и модули](ourplancore-settings.md) |
    | `Suffix generation rules (first enabled match wins)` |  | Settings: Settings > Auto Rename / Scale | Section of the settings panel. | [Settings и модули](ourplancore-settings.md) |
    | `Learned rules (lower-priority evidence)` |  | Settings: Settings > Auto Rename / Scale | Section of the settings panel. | [Settings и модули](ourplancore-settings.md) |

??? note "Settings > Sheet Takeoff Routing (3)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Levels` |  | Settings: Settings > Sheet Takeoff Routing | Section of the settings panel. | [Маршрутизация и правила](ourplancore-routing.md) |
    | `Rows` |  | Settings: Settings > Sheet Takeoff Routing | Section of the settings panel. | [Settings и модули](ourplancore-settings.md) |
    | `Tool destinations` |  | Settings: Settings > Sheet Takeoff Routing | Section of the settings panel. | [Маршрутизация и правила](ourplancore-routing.md) |

??? note "Settings > Workspace (2)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Connect another computer` |  | Settings: Settings > Workspace | Section of the settings panel. | [Workspace, Job Tracker, CLI](ourplancore-workspace.md) |
    | `Projects` |  | Settings: Settings > Workspace | Section of the settings panel. | [Settings и модули](ourplancore-settings.md) |

## Окна и диалоги (46)

??? note "окно Job Is Already Open (3)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Open Read-Only` |  | окно: окно Job Is Already Open | Open without saving or modifying this job | [Проекты и сохранение](job-creation-storage.md) |
    | `Retry` |  | окно: окно Job Is Already Open | Check the lease again | [ИИ и терминалы](ourplancore-ai.md) |
    | `Take Over` |  | окно: окно Job Is Already Open | Replace the current lease after an additional confirmation | [Проекты и сохранение](job-creation-storage.md) |

??? note "окно Open Project (5)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `+ Add folder` |  | окно: окно Open Project | Add a folder containing OurPlanCore jobs | [Проекты и сохранение](job-creation-storage.md) |
    | `Remove folder` |  | окно: окно Open Project | Remove the selected source folder from this list. Files stay on disk. | [Проекты и сохранение](job-creation-storage.md) |
    | `Open` |  | окно: окно Open Project |  | [Проекты и сохранение](job-creation-storage.md) |
    | `PDF project` |  | окно: окно Open Project | Create a new project from PDFs | [Проекты и сохранение](job-creation-storage.md) |
    | `Blank project` |  | окно: окно Open Project | Create an empty project | [Проекты и сохранение](job-creation-storage.md) |

??? note "окно (27)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Create Line Grid` |  | окно: окно |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Batch Overlay` |  | окно: окно | Buttons: Apply overlays. | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Command Palette` |  | окно: окно |  | [Начало работы](ourplancore-start.md) |
    | `Estimating` |  | окно: окно |  | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Recover Keyboard Shortcuts` |  | окно: окно |  |  |
    | `Keyboard Shortcuts` |  | окно: окно |  | [Settings и модули](ourplancore-settings.md) |
    | `Rename Legend Group` |  | окно: окно |  |  |
    | `Count Points At Line Ends` |  | окно: окно |  | [Правка и привязки](ourplancore-editing.md) |
    | `Marker Sets` |  | окно: окно | Buttons: Apply Filter, Rename..., Delete, Open JSON. | [ИИ и терминалы](ourplancore-ai.md) |
    | `Rename Marker Set` |  | окно: окно |  |  |
    | `Review Opening Projections` |  | окно: окно | Buttons: Keep All, Reject All, Save Reviewed Openings. |  |
    | `Paste Measurements` |  | окно: окно |  | [Правка и привязки](ourplancore-editing.md) |
    | `OpenAI Settings` |  | окно: окно | Buttons: Save Key To User Env, Clear User Env Key. | [ИИ и терминалы](ourplancore-ai.md) |
    | `Import OurPlanCore into Current Job` |  | окно: окно | Buttons: Choose .ourplan file..., Choose project folder.... | [Проекты и сохранение](job-creation-storage.md) |
    | `Overlay Color` |  | окно: окно | Buttons: Use Color. |  |
    | `Page Setup` |  | окно: окно |  | [Листы (Pages)](ourplancore-pages.md) |
    | `Export PDF` |  | окно: окно | Buttons: All, None. | [PDF и сдача](ourplancore-pdf.md) |
    | `Import PDF Takeoffs` |  | окно: окно | Buttons: Scan / Preview, Browse.... | [Прочее](ourplancore-extras-other.md) |
    | `Create Count Points Along Line(s)` |  | окно: окно |  | [Правка и привязки](ourplancore-editing.md) |
    | `Project Data Recovery` |  | окно: окно |  | [Проекты и сохранение](job-creation-storage.md) |
    | `Review Roof Draft` |  | окно: окно | Buttons: Keep All, Reject All, Save Reviewed Roof. |  |
    | `Crop to Sheet` |  | окно: окно | Buttons: Start Cropping, Existing sheet, New blank sheet. | [Кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md) |
    | `Choose Sheet Overlay Candidate` |  | окно: окно | Buttons: Use Selected, Use + Review Overlay, Use + Open Source, Use + Edit Transform, Use + Edit by Points. |  |
    | `Takeoff Folder Properties` |  | окно: окно | Buttons: None. | [Дерево Takeoffs](ourplancore-takeoffs.md) |
    | `Trace Walls Inside Area` |  | окно: окно |  | [Привязки и трассировка](ourplancore-snap-trace.md) |
    | `Job Is Already Open` |  | окно: окно | Buttons: Open Read-Only, Retry, Take Over. | [Проекты и сохранение](job-creation-storage.md) |
    | `Open Project` |  | окно: окно | Buttons: + Add folder, Remove folder, Open, PDF project, Blank project. | [Проекты и сохранение](job-creation-storage.md) |

??? note "окно (строится в коде главного окна) (11)"

    | Функция | Клавиша | Где в интерфейсе | Что делает | Подробно |
    | --- | --- | --- | --- | --- |
    | `Create Marker Set` |  | окно: окно (строится в коде главного окна) |  | [ИИ и терминалы](ourplancore-ai.md) |
    | `Merge Into Takeoff` |  | окно: окно (строится в коде главного окна) |  | [Правка и привязки](ourplancore-editing.md) |
    | `Import PDF Options` |  | окно: окно (строится в коде главного окна) |  | [Проекты и сохранение](job-creation-storage.md) |
    | `PlanSwift Import Complete` |  | окно: окно (строится в коде главного окна) | Buttons: Open Report. |  |
    | `Sheet Overlay Transform` |  | окно: окно (строится в коде главного окна) |  |  |
    | `Takeoff Item Properties` |  | окно: окно (строится в коде главного окна) |  | [Инструменты замера](ourplancore-tools.md) |
    | `Split Selected Takeoffs` |  | окно: окно (строится в коде главного окна) |  | [Правка и привязки](ourplancore-editing.md) |
    | `Create Takeoff From Template` |  | окно: окно (строится в коде главного окна) |  |  |
    | `Add Template Preset` |  | окно: окно (строится в коде главного окна) |  |  |
    | `Edit Template Preset` |  | окно: окно (строится в коде главного окна) |  |  |
    | `Workspace conflicts` |  | окно: окно (строится в коде главного окна) |  |  |

