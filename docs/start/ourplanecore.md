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

## Roadmap

### Ближайшие задачи

- Довести `Report Builder` до рабочих mappings по основным E-Wood sections.
- Улучшить review UI для SmartTrace action drafts.
- Добавить cross-sheet batch search для marker-assisted `Find Similar`.
- Усилить learned-rule conflict details в Sheet Manager.
- Доделать complex roof / valley plane generation в `3D Massing`.
- Добавить snapshot/history picker для accepted 3D drafts.

### Средний горизонт

- `Image Snap` для scanned/raster drawings.
- Больше PlanSwift parity: specialty tools, properties-first workflow, arc tool.
- Более сильные estimating templates и Excel/ClosedXML export.
- Dedicated bulk marker review panel.
- Richer Report Builder preview: source rows, target cells, validation messages.
- Client/project rule packs для COM/EWP/Residential workflows.

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
