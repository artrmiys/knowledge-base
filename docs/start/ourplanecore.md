# OurPlaneCore

OurPlaneCore - локальная программа для takeoff по PDF drawings. Идея простая:
собрать в одном окне то, что сейчас обычно разъезжается между PlanSwift,
Excel, ручными заметками, PDF viewer и отдельными проверками.

!!! note "Статус"
    Это рабочая внутренняя программа, а не публичный SaaS. Скриншоты ниже
    redacted: job name, sheet names и реальные takeoff names специально скрыты.
    Описания разделены на `уже работает`, `в разработке` и `планируется`, чтобы
    не путать текущий функционал с будущими идеями.

<figure markdown>
  ![OurPlaneCore main workspace](../assets/images/ourplanecore/ourplanecore-main-view-redacted.png)
  <figcaption>Main View: PDF viewport, Pages tree слева, Takeoffs tree справа, tools снизу.</figcaption>
</figure>

## Зачем нужна программа

OurPlaneCore должен стать рабочим местом estimator / takeoff specialist:

- быстро открыть job и PDF sheets;
- разложить sheets по folders в стиле PlanSwift;
- проверить sheet name и scale до измерений;
- делать `Count`, `Line`, `Area`, `J Area` и page markups прямо на PDF;
- видеть Pages, Takeoffs, Estimating, PDF layers и AI context в одном месте;
- экспортировать quantities в CSV/TXT/Excel или прямо в открытый workbook;
- постепенно добавлять AI как помощника с review, а не как скрытую магию.

Главная цель - не заменить инженера, а убрать ручной хаос: меньше прыжков между
окнами, меньше забытых sheets, меньше сломанного scale, больше проверяемых
evidence links.

### Для кого

| Пользователь | Что ему нужно | Как помогает OurPlaneCore |
| --- | --- | --- |
| Estimator | Быстро считать quantities и не терять структуру | PlanSwift-like Pages/Takeoffs, sections, totals, exports |
| Lead estimator | Проверять чужой takeoff и видеть, откуда quantity | Sheet links, source page, selected sections, notes, review tables |
| Developer / automation | Понимать, куда подключать rules и AI | Local files, JSON drafts, explicit services, no hidden cloud state |
| New team member | Быстро войти в E-Wood workflow | Standard folders, wiki links, names/scale checks, planned rule hints |

### Какие проблемы закрывает

| Проблема | Что происходит без программы | Что должно быть в программе |
| --- | --- | --- |
| Sheets названы хаотично | Нельзя быстро найти floor/section/detail | `Auto Name` + review + folders |
| Scale не проверен | `lf`/`sf` quantity становится мусором | `Auto Scale`, scale badge, Line/Area blocked without scale |
| Takeoff размазан | Непонятно, где стены, SQFTs, framing, trims | Standard folder templates and future auto routing |
| Excel ручной | Легко вставить не туда или потерять notes | `Current Excel`, `Report Builder`, preview before write |
| AI непроверяемый | Риск тихо применить неправильную geometry | AI Inbox, crops, drafts, accept/reject, source links |
| PDF scan не vector | Snap вроде включен, но не ловит линии | Separate `PDF Snap` status and future `Image Snap` |

## Карта продукта

<div class="grid cards" markdown>

-   :material-file-pdf-box: **PDF Workspace**

    ---

    Job, PDF sheets, page folders, tabs, PDF layers, overlay sheets, page scale,
    sheet legend, display settings и export PDF with measurements.

-   :material-table-edit: **Sheet Manager**

    ---

    Review-gated `Auto Name`, `Auto Scale`, confidence, `Why`, warnings,
    learned rules и apply checked rows.

-   :material-ruler-square: **Takeoff Tools**

    ---

    `Count`, `Line`, `Area`, `J Area`, `Scale`, `Select`, `Ruler`, markups,
    copy/paste, group move, section properties и active Record target.

-   :material-magnet-on: **Snap**

    ---

    Обычный `Snap` по нарисованным measurements и отдельный `PDF Snap` по
    vector geometry самого PDF или overlay PDF.

-   :material-folder-tree: **Pages / Takeoffs Tree**

    ---

    Две связанные структуры: слева sheets/folders, справа takeoff folders/items.
    Выбор на sheet подсвечивает takeoff, выбор takeoff подсвечивает sheets.

-   :material-chart-box-outline: **Estimating / Manager**

    ---

    Табличный обзор quantities, sections, units, notes, unit price, cost,
    current-sheet filter и export commands.

-   :material-microsoft-excel: **Report Builder**

    ---

    Excel-like workspace для будущей сборки report blocks из takeoff source
    rows в `TemplateCom.xlsm`.

-   :material-robot-outline: **AI Inbox / 3D Massing**

    ---

    AI requests, crop bookmarks, markers, SmartTrace drafts, marker feedback,
    reviewable 3D massing draft и source links.

</div>

## Ментальная модель

Программа построена вокруг job folder. Все важное хранится локально, рядом с
проектом, а не в облаке.

```text
<job>/
  Pages/            PDF sheet folders, renamed sheets, per-page metadata
  Takeoffs/         takeoff folders/items and measurements
  sources/          original imported PDFs
  AI_Context/       markers, crops, requests, responses, actions, learning
  Data.xml          takeoff item and folder metadata
```

| Слой | Что хранит | Зачем |
| --- | --- | --- |
| `Pages` | Sheets, folders, `source.json`, `source_pdf.json`, layers, overlays | Правильные names, scale, PDF source и page-specific settings |
| `Takeoffs` | Folders, items, sections, measurements, notes, prices | Quantity structure и estimating tree |
| `Measure` | Points in PDF coords, type, color, page, scale | Геометрия, которую рисует пользователь |
| `AI` | Crops, markers, requests, responses, action drafts, feedback | Reviewable AI evidence без автоприменения |
| `Data` | Item/folder metadata | Совместимость с привычной takeoff-структурой |

!!! tip "Главная логика"
    `Page` отвечает за drawing context и scale. `Takeoff item` отвечает за то,
    что именно считается. `Measurement` связывает их: на каком sheet, с каким
    scale и в какой item записана геометрия.

### Data flow

```text
PDF import
  -> Pages tree
  -> source.json / source_pdf.json / layers.json
  -> Sheet Manager review
  -> checked rename/scale/folder apply
  -> active sheet in viewport
  -> Record into active takeoff item
  -> measurements.json / Data.xml
  -> Estimating / Takeoff Manager / Export
```

AI flow идет отдельно:

```text
User marker or crop
  -> AI_Context/crops + AI_Context/markers
  -> AI request JSON
  -> model response
  -> action draft
  -> user review
  -> accepted geometry or feedback only
```

### Что считается source of truth

| Данные | Source of truth | Почему |
| --- | --- | --- |
| Sheet name / scale | Page metadata after review | Sheet Manager показывает source, confidence и warning |
| Quantity | Measurements under takeoff item | Геометрия и scale сохраняются с measurement |
| Export rows | Takeoff tree + estimating rows | Export не должен считать по картинке заново |
| AI proposal | Action draft | Пока user не принял, это не реальный takeoff |
| Learning | Accepted/rejected feedback | Правила улучшаются только через проверенные решения |

## Основной workflow

1. Открыть или создать job.
2. Импортировать PDF sheets.
3. Проверить sheets в `Sheet Manager`: `Auto Name`, `Auto Scale`, warnings,
   confidence и `Why`.
4. Применить только checked rows, потом разложить sheets через `Sort A/S`,
   `D/Sec/WT`, `Auto Folders`.
5. Открыть sheet на `Main View`, проверить scale, layers, overlay и display.
6. Создать или выбрать takeoff item справа.
7. Включить `Record` и выполнить `Count`, `Line`, `Area` или `J Area`.
8. Проверить totals в `Takeoffs`, `Estimating` или `Takeoff Manager`.
9. Экспортировать в CSV/TXT/Excel или отправить selected rows в `Current Excel`.
10. Если нужен AI, сохранить markers/crops, получить draft, проверить и только
    потом apply.

## PlanSwift logic -> OurPlaneCore

| PlanSwift behavior | Что это значит для OurPlaneCore |
| --- | --- |
| Job открывает Pages, drawing canvas и Takeoffs | Первый экран после открытия job - рабочий takeoff screen, а не welcome page |
| Pages panel хранит sheets/folders | `Pages tree` слева, folders можно сортировать, двигать, переименовывать |
| Scale обязателен для Line/Area | Line/Area Record блокируется без scale; Count можно делать без scale |
| Takeoff item имеет fixed type | Item не должен смешивать `Line`, `Area` и `Count` в одном контейнере |
| Digitizer Record пишет в активный item | `Record` держит active target locked, случайный клик по другому item не перенаправляет измерения |
| Estimating показывает item totals | `Estimating` и `Takeoff Manager` показывают quantities, units, sections, notes, cost |
| Copy/paste помогает повторять geometry | `Select`, `Ctrl+C`, `Ctrl+V` переносят measurements на текущий sheet |

## UI philosophy

OurPlaneCore должен выглядеть как плотный рабочий инструмент, ближе к
PlanSwift / Bluebeam, а не как SaaS landing page.

- Верх: compact commands и status, без больших hero-панелей внутри app.
- Слева: Pages, Layers, sheet organization.
- Центр: PDF canvas, максимум пространства под drawing.
- Справа: Takeoffs, Properties, Estimating, Report Builder.
- Низ: status / AI Inbox / manager tabs, когда нужно.
- Все totals и coordinates должны быть tabular, чтобы числа не прыгали.
- Active tool, active target и Record state должны быть видны всегда.
- Ошибка должна говорить действие: `Set scale first`, `Select compatible item`,
  `Review warnings before apply`.

## Main View

Main View - главный экран для ручного takeoff.

| Зона | Для чего |
| --- | --- |
| `Pages tree` | Sheet folders, imported pages, PDF layers, overlays, page setup, repair links |
| `PDF viewport` | Pan/zoom, measurements, labels, snap, scale, markups, sheet legend |
| `Takeoffs tree` | Folders/items/sections, active target, Record, item properties |
| Bottom tools | `Pan`, `Select`, `Scale`, `Count`, `Line`, `Area`, `J Area`, `PDF Snap`, `Ortho` |
| Right workspace | `Estimating`, `Takeoff Manager`, `Report Builder`, `AI Inbox`, `3D Massing` |

### Record target

- Новый takeoff должен писаться только в выбранный active item.
- `Record` держит target locked, пока его не остановили.
- Если выбран не тот тип item, программа должна попросить создать/выбрать
  совместимый target.
- После Record удобно возвращаться в `Select`, чтобы двигать или проверять уже
  нарисованное.

### Select / edit

- `Select` - основной режим для проверки и редактирования.
- Drag-box выбирает несколько measurements на активном sheet.
- `Ctrl+Click` добавляет/убирает отдельные measurements.
- `Ctrl+C` / `Ctrl+V` копирует и вставляет выбранную геометрию.
- Body drag двигает весь выбранный measurement или группу.
- Vertex handles редактируют форму line/area.

### Command Palette и hotkeys

| Command | Shortcut | Статус / смысл |
| --- | --- | --- |
| `Command Palette` | `Ctrl+Shift+P` | Найти command без охоты по меню |
| `Save` | `Ctrl+S` | Явно сохранить job state |
| `Open Job Picker` | `Ctrl+Shift+O` | Recent jobs, pinned jobs, browse/create |
| `Count` | `P` | Quick-create Count target and Record |
| `Line` | `L` | Quick-create Line target and Record |
| `Area` | `A` | Quick-create Area target and Record |
| `J Area` | `J` | Quick-create joist Area target and Record |
| `Snap` | `F3` | Snap to app-created measurement geometry |
| `PDF Snap` | `Ctrl+F3` | Snap to vector PDF/overlay geometry |
| `Ortho` | `F8` | 90/45 degree constraint |
| `Copy / Paste` | `Ctrl+C` / `Ctrl+V` | Reuse selected measurements |
| `Delete` | `Delete` | Delete selected measurement/markup rows |

### Display / viewport rules

- Sheet paper может быть белым, серым или dark для комфорта.
- PDF export всегда должен использовать white paper, даже если viewport dark.
- Legend можно hide/show per sheet.
- Legend order сохраняется в page metadata.
- Hidden takeoffs on this sheet не рисуются на viewport и не попадают в PDF
  export.
- Cursor guide rays помогают попадать в точки на плотном drawing.
- Live dimensions при Line/Area/Ruler показывают feedback до finish.

## Pages и Sheet Manager

<figure markdown>
  ![OurPlaneCore Sheet Manager](../assets/images/ourplanecore/ourplanecore-sheet-manager-redacted.png)
  <figcaption>Sheet Manager: review table для Auto Name / Auto Scale перед применением.</figcaption>
</figure>

`Sheet Manager` нужен, чтобы не применять auto-renaming и auto-scale вслепую.

| Поле / действие | Что проверять |
| --- | --- |
| `Proposed Name` | Sheet label из PDF text, title block, AI fallback или manual source |
| `Scale` | Parsed scale, например `1/8" = 1' 0"` |
| `Confidence` | Насколько уверенно найдено имя или scale |
| `Why` | Почему предложен именно этот result |
| `Warnings` | Missing label, duplicate, conflict, no usable scale, skipped sheet |
| `Apply Checked` | Применять только строки, которые проверены |
| `Open JSON` | Диагностика `source_pdf.json` и learned rules |

### PDF Auto logic

- `Analyze PDF Metadata` читает title block и PDF text через deterministic
  extraction.
- `Auto Name` предлагает sheet names.
- `Auto Scale` предлагает scale.
- `Name+Scale` делает оба шага в одном preview.
- `AI Fill` нужен только когда deterministic parse не справился.
- Learned rules могут поднять confidence или заблокировать известный conflict.

### Page folders

- `Sort A/S` раскладывает `A` sheets в Arch, `S` sheets в Struct, trailing `-`
  sheets в others.
- `D/Sec/WT` вторым проходом отправляет details, sections, units и wall-type
  sheets в нужные места.
- `Auto Folders` может создавать типовые COM/EWP folders.
- Pages и folders можно двигать, rename/copy/cut/paste/duplicate/delete.

### Sheet metadata lifecycle

| Step | Что создается | Что проверять |
| --- | --- | --- |
| Import PDF | `source.json` | Original PDF, page index, imported page folder |
| Analyze | `source_pdf.json` | Sheet label, title, suffix, scale candidate, warnings |
| Layers scan | `layers.json` | Layer names, visible/hidden state, AI layer context |
| Preview | Sheet Manager rows | `Why`, confidence, duplicates, no-scale rows |
| Apply checked | Page rename/scale updates | Только verified rows |
| Learn | project/global learned rules | Conflict rules should remain reviewable |

### Folder templates

| Mode | Для чего | Что создает |
| --- | --- | --- |
| `Auto` | Быстро выбрать по job name | COM or EWP folders by detected naming |
| `COM` | Commercial jobs | Pages/Takeoffs folders for walls, framing, SQFTs, trims, etc. |
| `EWP` | EWP / Capital jobs | Arch/Struct/details/framing oriented folders |
| Manual | Когда job нестандартный | User сам создает/двигает folders |

Future routing should never replace manual control. Если item auto-routed wrong,
user must be able to move it back without fighting the app.

## Takeoff tools

| Tool | Quantity | Когда использовать |
| --- | --- | --- |
| `Count` | `ea` | Windows, doors, posts, beams count, hardware, повторяющиеся items |
| `Line` | `lf` | Walls, plates, blocking, trims, railing, linear scope |
| `Area` | `sf` | Sheathing, roof/floor areas, slab, drywall-like surfaces |
| `J Area` | joist count + total length | Joist layout inside polygon with spacing, pitch and rounding |
| `Scale` | page scale | Set/verify scale before Line/Area |
| `Ruler` | temporary check | Быстрая проверка расстояния без takeoff item |
| `Box/Arrow/Markup` | annotation | Визуальная пометка на sheet |

### Scale rules

- `Count` можно ставить без scale.
- `Line` и `Area` требуют sheet scale.
- Scale хранится per page и per measurement.
- Если measurement перенесен на другой sheet, scale нужно проверять особенно
  внимательно.
- В будущем нужен advanced mode для separate horizontal / vertical scale.

### Snap rules

| Mode | К чему snap | Hotkey |
| --- | --- | --- |
| `Snap` | Existing app measurements: endpoints, midpoints, intersections | `F3` |
| `PDF Snap` | Vector PDF geometry: PDF points, corners, line segments, overlay geometry | `Ctrl+F3` |
| `Ortho` | 90/45 degree constraint для Line/Area/Scale | `F8` |

`PDF Snap` работает только если PDF реально содержит vector geometry. Если sheet
это scan/raster image, у него может не быть PDF line/corner data. Для такого
случая нужен отдельный будущий `Image Snap`.

### Production scenarios

| Scenario | Recommended path |
| --- | --- |
| Exterior walls | `Line`, active `walls / floor walls` item, scale required |
| Windows / doors | `Count`, schedule cross-check, possible AI marker samples later |
| Wall sheathing | `Area` or `Line` depending on rule/source page |
| Roof SQFT | `Area`, verify pitch/slope rules before export |
| Joists | `J Area`, set direction, spacing, pitch and rounding |
| Interior trims | `Line` for Base/Crown, `Count` or schedule for doors/openings |
| Hardware / hangers | `Count`, future rule-check against joist/beam context |
| Existing to remain | Mark as note/status, do not count blindly |

### Measurement quality rules

- Every `Line` and `Area` needs known scale.
- Every `J Area` needs joist direction before ordered length is trusted.
- Repeated floors can reuse geometry, but floors should stay separate in output
  when the E-Wood rule says not to combine them.
- Count items should use user-facing `Count`, not internal `Point` wording.
- Notes should stay visible in manager/export so review comments are not lost.

## Joist Area

`J Area` - shortcut для joist layout. Он создает `Area` takeoff, включает joist
settings и сразу запускает area record.

- Default behavior: `Round Up Foot`, detailed area label off.
- После area polygon задается direction line параллельно joists.
- Joist lines clipped внутри polygon.
- Pitch, например `3:12`, применяется как slope factor до rounding.
- Quantity показывает ordered length и joist count.
- Copy/paste сохраняет joist settings и direction state.
- Если direction не задан, item должен показывать `set direction`, а не считать
  по случайному default angle.

## Takeoff Manager и Estimating

<figure markdown>
  ![OurPlaneCore Takeoff Manager](../assets/images/ourplanecore/ourplanecore-takeoff-manager-redacted.png)
  <figcaption>Takeoff Manager: items, totals, units, notes, folders и export commands.</figcaption>
</figure>

`Takeoff Manager` и `Estimating` - это проверка quantities без прыжков в Excel.

| Поле | Что значит |
| --- | --- |
| `Item` | Название takeoff item |
| `Type` | `Count`, `Line`, `Area`, `Joist` |
| `Sections` | Отдельные measurements внутри item |
| `Total` | Итоговая quantity |
| `Unit` | `ea`, `lf`, `sf` и т.д. |
| `Price / Cost` | Черновой estimating value |
| `Notes` | Видимые notes по item или section |
| `Folder` | Путь item внутри takeoff tree |

Что важно:

- Item rows и section rows должны быть reviewable.
- Section row может `Go to Page`, `Select on Canvas`, `Rename`, `Properties`,
  `Delete`.
- Current-sheet filter помогает проверять только активный sheet.
- Notes экспортируются, чтобы не терять рабочие комментарии.

### Takeoff tree behavior

- Folders can store defaults: color, measurement type, unit price, notes,
  prefix.
- New items inherit nearest folder defaults where useful.
- Multi-select supports move/copy/cut/paste/delete.
- Section/count rows are editable and can be moved between compatible items.
- A folder selection can select all nested active-sheet measurements.
- Sheet-linked rows under a page control legend order, not item identity.

### Future auto-routing

Auto-routing should help with naming, not trap the user.

| New item name | Target idea | Notes |
| --- | --- | --- |
| `1st`, `2nd`, `3rd`, `4th`, `5th`, `6th` | `sqfts` | Floor SQFT order should be stable |
| `deck`, `porch`, `blcny`, `balcony`, `cant` | `sqfts` | Exterior area groups after floors |
| `flat`, `rf`, `rf mtl` | `sqfts` / roof area group | Needs clear export ordering |
| `ext`, `cor`, `corr`, `dem`, `2x4`, `2x6`, `2x8` | `walls / <floor> walls` | Only when active sheet suffix is clear |
| unknown | Current selected folder | Better no-routing than wrong-routing |

Rule: match tokens, not random substrings. `cor` must not accidentally match
`corners`.

## Export и Excel

| Export | Статус | Для чего |
| --- | --- | --- |
| CSV | Работает | Табличный output с quantities, notes, scale, price/cost |
| TXT | Работает | PlanSwift-like text blocks для проверки/переноса |
| Excel `.xlsx` | Работает как отдельный export | Rows в стиле `Name / Value / Unit` |
| `Current Excel` | Работает | Пишет selected folder/item в уже открытый workbook от active cell |
| `Report Builder` | В разработке | Будущая сборка report blocks прямо внутри app |

`Current Excel` не делает auto-save. Это правильно: программа пишет строки, а
пользователь сам проверяет workbook и сохраняет его.

### Export principles

- Export should be boring and predictable.
- Export should include notes when notes exist.
- Export should not silently combine floors or sections.
- Export should preserve enough page/section context to audit quantity later.
- Excel write should show where it wrote and should not save over user work.

### Report-ready output target

The long-term goal is not just "export table"; the real target is an E-Wood
report workflow:

```text
Takeoff tree
  -> normalized source rows
  -> report mapping
  -> preview target cells
  -> write to workbook
  -> user checks workbook
  -> user saves final file
```

## Report Builder

`Report Builder` - отдельный workspace для будущей Excel-like сборки reports.
Он не заменяет существующие exports, а строится рядом с ними.

Что уже есть:

- отдельный tab `4 Report Builder`;
- чтение local `TemplateCom.xlsm` и sheet `Detailed Frame List`;
- отображение Excel-like grid с columns `A-H` и `J-L`;
- template column widths и первые header rows;
- подсветка header, table-header, section и yellow input-block rows;
- cells можно показывать как рабочую таблицу;
- первый wall block prototype умеет применять selected source rows в target
  cells по шаблону.

Что планируется:

- связать takeoff folders/items с нужными report sections;
- добавить mapping для `walls`, `sqft`, `framing`, `openings`, `sheathing`,
  `trims`, `deck`, `roof`;
- сделать preview before write;
- показывать source rows и target cells рядом;
- сохранять mapping rules per project/client;
- оставить ручной контроль перед финальным Excel output.

!!! warning "Важно"
    `Report Builder` пока не должен ломать обычные CSV/TXT/Excel exports.
    Это отдельная поверхность для будущего Excel workflow.

### Report Builder target sections

| Section | Future mapping needs |
| --- | --- |
| `SQFTs` | Floors, deck, porch, balcony, cantilevered, roof, flat roof |
| `Walls` | Exterior, corridor, demising, furring, shaft, parapet, gable |
| `Openings` | Windows, doors, garage doors, MTL doors, headers |
| `Framing` | Beam, Joist, Post, blocking, rim/ribbon, steel beams |
| `Roof framing` | Ridge, hip, valley, rafters, overframes, canopy, dormer |
| `Sheathing` | Wall, floor, roof, gable, truss heel, shear wall |
| `Trims` | Base, Casing, Crown, door/window trims, balcony trims |
| `Hardware` | Hangers, bolts, washers, screws, anchor bolts |

### What "good" looks like

- User can see source takeoff rows.
- User can see target Excel cells.
- User can see formulas/values that will be written.
- User can apply only selected groups.
- User can reopen mapping and understand why a row went there.
- If workbook/template is missing, the app explains what file is expected.

## AI Inbox

AI в OurPlaneCore должен работать как помощник с evidence и review.

| Часть | Что делает |
| --- | --- |
| `AI markers` | User отмечает sample: corner, wall height, window, door, roof edge, ignore area |
| `Crops` | Программа сохраняет crop PNG и context вокруг marker/measurement |
| `AI requests` | JSON request лежит в `AI_Context/requests` |
| `AI responses` | Ответ сохраняется отдельно, его можно открыть и проверить |
| `Action drafts` | Proposed geometry не применяется сразу |
| `Review` | User принимает или отклоняет отдельные candidates |
| `Learning` | Accepted/rejected feedback сохраняется для будущих prompts |

Принцип: AI не должен тихо создавать quantities. Он предлагает draft, показывает
source/crop/JSON, а пользователь решает, что apply.

### Marker workflow

1. Поставить marker на sheet или на measurement.
2. Выбрать marker type: `exterior_corner`, `wall_height_sample`,
   `window_sample`, `door_sample`, `roof_edge_sample`, `ignore_area` и т.д.
3. Сохранить crop evidence.
4. Запустить `Find Similar From Marker` или собрать marker set.
5. Проверить candidates.
6. Accepted/rejected feedback идет в learning.

### AI safety rules

- AI output is draft until accepted.
- AI should save request/response JSON.
- AI should keep crop evidence.
- AI should show confidence and uncertainty.
- AI should create review rows, not direct quantities.
- AI should learn from accepted/rejected feedback.
- AI should not expose secrets, private paths, emails, UID, salary, or pricing.

### Good AI jobs

| Job | Why it fits |
| --- | --- |
| Find similar symbols | User gives marker examples, AI finds candidates |
| Title block fallback | Deterministic parser failed, AI reads crop |
| Missing-scope checklist | AI compares sheets/markers/wiki rules and asks questions |
| Roof draft hints | AI proposes roof guide candidates for review |
| Opening samples | AI groups similar windows/doors before user accepts |

### Bad AI jobs for now

| Job | Why not yet |
| --- | --- |
| Fully automatic estimate | Too risky without review and source links |
| Complex roof solver | Needs geometry review and human correction |
| Counting from blurred scan | Needs image-specific pipeline and confidence gates |
| Writing final workbook silently | Must preview and avoid overwriting user work |

## 3D Massing

`3D Massing` - не BIM и не Revit. Это reviewable draft, который помогает понять
building shape и связать plan/elevation/roof evidence.

Что уже есть в текущей логике:

- draft JSON `AI_Context/3d_massing/model.json`;
- build draft from markers;
- footprint points, openings, roof summary, assumptions, unresolved questions;
- source-marker table и jump back to sheet;
- top-down footprint preview;
- simple WPF 3D shell: floor, walls, roof planes;
- Fit/Iso/Top/Front camera controls;
- roof guide review: type, pitch, confidence, notes, keep/reject;
- opening projection: window/door/opening markers to nearest wall faces;
- `Accept 3D` сохраняет reviewed state и snapshots.

Что это НЕ должно делать в первой версии:

- не считать framing quantities автоматически;
- не быть точной BIM geometry;
- не решать complex roof без review;
- не скрывать assumptions;
- не создавать takeoff items без подтверждения.

Будущая польза: если 3D draft reviewable, его можно использовать как project
context для AI, roof checks, opening consistency и missing-scope warnings.

### 3D Massing inputs

| Marker / source | Used for |
| --- | --- |
| `exterior_corner` | Footprint draft |
| `wall_height_sample` | Wall extrusion height |
| `roof_edge_sample` | Roof guide evidence |
| `ridge_sample` / `valley_sample` | Roof planes and guide direction |
| `roof_high_edge` / `roof_low_edge` | Shed/low-slope direction |
| `window_sample` / `door_sample` | Opening projection to wall faces |
| reviewed roof notes | Type, pitch, confidence, assumptions |

### 3D review checklist

- Footprint corners are in the right order.
- Wall height source is visible.
- Roof type is marked as reviewed or uncertain.
- Openings are on plausible wall faces.
- Rejected openings remain as evidence, not deleted history.
- Accepted 3D draft writes a timestamped snapshot.
- 3D geometry does not create estimating quantities by itself.

## Что уже работает

| Область | Статус |
| --- | --- |
| Job open/create/recent jobs | Работает |
| PDF import, render, tabs, page folders | Работает |
| PDF layers panel and layer context | Работает |
| Auto Name / Auto Scale preview | Работает, требует review |
| Scale calibration | Работает |
| Count / Line / Area / J Area | Работает |
| Select, edit, copy/paste, group move | Работает |
| Sheet legend and page takeoff visibility | Работает |
| Estimating table and Takeoff Manager | Работает |
| CSV/TXT/Excel export | Работает |
| Current Excel write | Работает, без auto-save |
| AI Inbox, markers, crops, action drafts | Работает как review workflow |
| 3D Massing draft and preview | Работает как черновой review tool |
| Report Builder | Первый useful slice, еще не финальный workflow |

## Ограничения сейчас

- `PDF Snap` зависит от vector PDF. Для scan/raster нужен будущий `Image Snap`.
- Auto Name / Auto Scale нельзя применять без просмотра warnings.
- `AI Fill` и SmartTrace drafts требуют review before apply.
- `Report Builder` еще не покрывает все final Excel blocks.
- Complex roof / valley / multi-roof geometry в 3D Massing требует улучшения.
- Separate horizontal/vertical scale еще не основной workflow.
- Финальный product name пока не закреплен публично.

## E-Wood rule engine idea

The wiki should eventually feed lightweight warnings into the program. Это не
должно быть hard-coded "AI magic"; это должны быть понятные rules with source
links.

| Rule idea | Warning example |
| --- | --- |
| Garage trim | Если room/sheet похож на garage и item `Base` / `Crown` добавлен, показать: `Garage usually has no Base/Crown unless plan/spec says otherwise` |
| MTL doors | Если schedule содержит `MTL Door`, проверить, что door count/report row не потерян |
| FRT | Если material/tag содержит `FRT`, подсветить, что это отдельный material/report bucket |
| Hangers | Если joists/beams counted but no hangers reviewed, предложить проверить Hangers page |
| Repeated floors | Если floor geometry copied, не объединять output floors без явного решения |
| Roof pitch | Если roof/joist quantity uses pitch, показать slope factor / rounding note |
| Existing to remain | Если note says existing/remain/by others, не count как new work без confirmation |

### Rule severity

| Severity | Meaning | UI behavior |
| --- | --- | --- |
| `info` | Просто подсказка | Small note in manager |
| `warning` | Нужно проверить перед export | Yellow row warning |
| `block` | Нельзя auto-apply | Row unchecked by default |
| `private` | Нельзя публиковать/export в wiki | Redacted or skipped |

## Roadmap

### Ближайшие задачи

- Довести `Report Builder` до рабочих mappings по основным E-Wood sections.
- Улучшить review UI для SmartTrace action drafts.
- Добавить cross-sheet batch search для marker-assisted `Find Similar`.
- Усилить learned-rule conflict details в Sheet Manager.
- Доделать complex roof / valley plane generation в `3D Massing`.
- Добавить snapshot/history picker для accepted 3D drafts.
- Добавить first-pass rule warnings: garage Base/Crown, FRT, MTL doors.
- Сделать auto-routing для SQFT and walls как reviewable behavior.

### Средний горизонт

- `Image Snap` для scanned/raster drawings.
- Больше PlanSwift parity: specialty tools, properties-first workflow, arc tool.
- Более сильные estimating templates и Excel/ClosedXML export.
- Dedicated bulk marker review panel.
- Richer Report Builder preview: source rows, target cells, validation messages.
- Client/project rule packs для COM/EWP/Residential workflows.
- Better packaging/update flow for non-developer users.
- Saved UI profiles for dense / focus / review modes.

### Большие идеи

- AI assistant, который читает sheets, markers и wiki rules и предлагает
  missing-scope checklist.
- Project pattern memory: accepted/rejected markers учат программу по конкретной
  работе, не создавая глобальную черную коробку.
- 3D massing как visual QA: openings, roof shape, wall heights, garage/porch
  consistency.
- Side-by-side report builder: takeoff source слева, Excel target справа.
- Rule-aware warnings: например, если в garage появились `Base` / `Crown`,
  программа должна подсветить это как подозрительное.
- Semi-automatic takeoff drafts: AI предлагает geometry, user принимает только
  проверенные pieces.
- Wiki-connected assistant: спросить "что проверить по Hangers / FRT / Trims"
  and get source-backed checklist.
- Cross-sheet consistency check: floor plan openings vs elevations vs door
  schedule.
- Client-specific packs: different defaults/rules for COM, EWP, Residential.
- Pattern transfer: copy reviewed marker definitions to a similar job without
  copying private drawings.

### Phase plan

| Phase | Goal | Done when |
| --- | --- | --- |
| 1. Manual takeoff core | Fast reliable drawing and editing | Count/Line/Area/J Area stable, scale safe, export works |
| 2. Sheet automation | Reduce setup time | Auto Name/Scale review catches most sheets and warnings are clear |
| 3. Takeoff organization | Less tree cleanup | Templates, auto-routing, folder defaults work without trapping user |
| 4. Report Builder MVP | Reduce Excel handwork | Source rows map to previewed workbook blocks with manual approval |
| 5. AI review workflow | Draft assistance | Markers/crops/actions are reviewable and feedback is stored |
| 6. 3D QA | Visual sanity check | Reviewed massing highlights footprint/roof/opening issues |
| 7. Rule engine | E-Wood knowledge inside app | Warnings are source-backed and never silently change quantities |
| 8. Packaging | Usable by non-developer | Install/update/run path does not require coding tools |

## QA matrix

| Area | Smoke test |
| --- | --- |
| Docs page | `mkdocs build --strict` and live page loads |
| App build | `dotnet build .\ourplanecore.sln /p:OutDir=.\cache\verify_build\ /p:UseAppHost=false` |
| PDF import | Import PDF, open first sheet, verify page render |
| Sheet Manager | Analyze, preview, apply checked rename/scale only |
| Scale | Line/Area blocked on unscaled sheet, Count allowed |
| Takeoff drawing | Count/Line/Area/J Area totals update |
| Edit/copy | Select, move, copy/paste to another sheet |
| PDF Snap | Vector sheet snaps to point/line; raster limitation is visible |
| Export | CSV/TXT/Excel and Current Excel preserve selected scope |
| AI | Request creates JSON, response creates draft, draft requires review |
| 3D | Build draft, review roof/openings, accept snapshot |
| Privacy | No unredacted screenshots or private source data in public docs |

## Release notes template

Каждый публичный или internal build should answer:

| Question | Answer should say |
| --- | --- |
| What changed? | User-facing behavior, not only file names |
| What is safe to use? | Confirmed workflows |
| What is still draft? | AI/3D/Report Builder limitations |
| What was verified? | Build/test/manual smoke commands |
| What can break? | Known risks and rollback notes |
| What data is private? | Screenshots, crops, job names, source PDFs |

## Module backlog

This is the practical "what to improve next" map. It is intentionally written
by module, so work can be split safely.

| Module | Next useful work |
| --- | --- |
| Job Picker | Better thumbnails, recent cleanup, job-root profiles, sample jobs by trade |
| Pages tree | Stronger drag/drop cues, folder templates by client, batch repair preview |
| Sheet Manager | Richer conflict explanations, retry failed AI fill, compare old/new names |
| PDF Layers | Better layer grouping, save layer meaning samples, layer-based takeoff hints |
| Viewport | Image Snap, magnifier, arc tool, cleaner high-zoom labels |
| Select/Edit | More predictable group transform, better undo stack, visible edit history |
| Takeoffs tree | Safer auto-routing, bulk properties, clearer invalid drop messages |
| Estimating | Sticky totals, richer filters, templates, export profiles |
| Report Builder | Full section mappings, preview target cells, write audit log |
| AI Inbox | Bulk review, confidence filters, source/evidence diff view |
| 3D Massing | Complex roof planes, snapshot comparison, source-linked object list |
| Rule engine | Garage trim warning, FRT/MTL/hanger checks, wiki source links |
| Packaging | Installer/update path, portable build, crash logs, user settings migration |

## Open decisions

| Decision | Why it matters | Current leaning |
| --- | --- | --- |
| Public product name | App says `OurPlaneCore`, older docs mention SmartTakeoffs | Keep neutral until final name is chosen |
| Exact Report Builder scope | Could become huge if it tries to replace Excel fully | Start as preview/write helper, not full spreadsheet clone |
| AI auto-apply | Faster but risky | Keep review-gated by default |
| Image Snap approach | Raster PDF needs different logic than vector PDF | Add separate mode, not inside `PDF Snap` |
| Rule source storage | Rules can live in code, wiki, JSON, or all three | Start with readable JSON linked back to wiki pages |
| Client profiles | COM/EWP/Residential rules differ | Use explicit profile, avoid guessing when uncertain |
| 3D geometry trust | 3D can look authoritative even when approximate | Always show assumptions/confidence/source markers |
| Workbook write strategy | Direct Excel write is powerful but dangerous | Preview first, write selected, never auto-save |

## Glossary

| Term | Meaning in this program |
| --- | --- |
| `Job` | Local project folder with Pages, Takeoffs, source PDFs and context files |
| `Page` / `Sheet` | One imported PDF page shown in the viewport |
| `Pages tree` | Left tree for sheets, folders, layers and sheet-linked takeoff rows |
| `Takeoffs tree` | Right tree for takeoff folders, items, sections and quantities |
| `Takeoff item` | Fixed-type container: Count, Line, Area or Joist Area |
| `Measurement` | Actual geometry on a sheet: points, line, polygon or count marker |
| `Section` | One completed measurement under an item; an item can have many sections |
| `Record` | Mode where clicks create new measurement geometry into active target |
| `Active target` | The takeoff item that receives new measurements |
| `ScaleMetersPerPt` | Stored conversion from PDF points to real-world units |
| `PDF Snap` | Snap mode that uses vector geometry extracted from the PDF itself |
| `Snap` | Snap mode that uses geometry already drawn in the app |
| `J Area` | Area item with joist layout settings and direction line |
| `Sheet Manager` | Review table for Auto Name / Auto Scale / warnings |
| `AI Inbox` | Review surface for AI requests, markers, crops and draft actions |
| `Action draft` | AI-proposed geometry or command that is not applied yet |
| `3D Massing` | Approximate source-linked 3D review model, not estimating-grade BIM |
| `Report Builder` | Future Excel-like report assembly workspace |
| `Current Excel` | Write selected takeoff rows into already open workbook at active cell |

## Example future workflows

### COM wall takeoff

1. Import plan set.
2. Run `Auto Name + Scale`.
3. Review names/scales and apply checked.
4. `Sort A/S` and `D/Sec/WT`.
5. Create standard COM Takeoffs folders.
6. On `1st` sheet, create `ext 2x6 x`; future auto-routing places it under
   `walls / 1st floor walls`.
7. Draw exterior wall lines with scale + PDF Snap.
8. Add `cor`, `dem`, `shaft`, `parapet` separately.
9. Check Takeoff Manager totals by floor.
10. Send rows to Report Builder / Current Excel.

### Interior trims review

1. Create `Interior Trims` folder.
2. Add `Base`, `Casing`, `Crown`, door/window trim items.
3. Use room/schedule evidence where available.
4. Rule engine checks: garage usually has no `Base` and no `Crown` unless
   plans/spec explicitly say otherwise.
5. MTL doors and special openings get separate review notes.
6. Export keeps notes so exceptions are not lost.

### AI-assisted openings

1. User marks a typical `window_sample` and `door_sample`.
2. AI runs `Find Similar From Marker`.
3. Candidates appear as review rows and dashed preview geometry.
4. User accepts/rejects candidates.
5. Accepted candidates become real Count measurements.
6. Rejected examples go into feedback so next run improves.

### 3D massing sanity check

1. User places exterior corner markers.
2. User adds wall height samples from elevation/section.
3. User adds roof/ridge/valley markers where obvious.
4. Build `3D Massing` draft.
5. Review footprint, roof guides and projected openings.
6. Accept snapshot as project context.
7. Use it for visual QA and future AI prompts, not direct quantity.

## Принципы разработки

- Local-first: job и context files лежат на диске.
- Review-gated: automation показывает preview и warnings до apply.
- Evidence-first: AI result должен иметь crop/source/request/response link.
- PlanSwift-like: user-facing workflow должен быть привычным estimator-у.
- No hidden magic: если программа не уверена, она должна сказать почему.
- Не показывать secrets: OpenAI key status можно показывать как found/missing,
  но не сам key.
- Не ломать ручной workflow ради AI. Manual takeoff всегда должен оставаться
  надежным fallback.

## Для разработчика

| Ownership | Основные файлы / сервисы |
| --- | --- |
| PDF viewport | `Controls/PdfViewport.*`, `Models/PdfGeometrySnapService.cs` |
| PDF render/layers | `Models/PdfLayerRenderService.cs`, `Tools/pdf_layers_helper.py` |
| Pages metadata | `Models/PdfSheetMetadataService.cs`, `MainWindow.Pages*.cs` |
| Takeoffs tree | `MainWindow.Takeoffs*.cs`, `Models/TakeoffItem.cs` |
| Measurements | `Models/Measurement.cs`, viewport selection/edit partials |
| Excel/report | `MainWindow.ReportBuilder.cs`, `Models/ReportTemplateService.cs` |
| AI Inbox | `MainWindow.AiInbox.cs`, `Models/SmartContextStore.cs`, `Models/OpenAiRequestRunner.cs` |
| 3D Massing | `MainWindow.MassingWorkflow.cs`, `Models/SmartMassingDraftService.cs` |
| Settings | `Models/AppSettingsStore.cs`, settings dialogs |

Перед релизом или большим изменением:

```powershell
dotnet build .\ourplanecore.sln /p:OutDir=.\cache\verify_build\ /p:UseAppHost=false
```

В этой wiki перед push всегда проверять:

```powershell
.\.venv\Scripts\python.exe -m mkdocs build --strict
```

## Быстрые ссылки внутри wiki

- [Workflow](workflow.md)
- [Структура takeoff](takeoff-structure.md)
- [QA checklist](quality-checklist.md)
- [Как пользоваться wiki](how-to-use.md)
- [Images & schemas](images-and-schemas.md)
