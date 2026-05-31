# OurPlaneCore

Локальная программа для takeoff по PDF — рабочее место estimator-а: PDF viewer,
Pages tree, Takeoffs tree, Estimating, Excel export и AI review в одном окне.
Близкий функциональный клон PlanSwift. Здесь — **каждая кнопка, ползунок и таб**
+ рабочий процесс от и до, обзор и архитектура.

!!! note "Статус"
    Внутренняя программа, не публичный SaaS. Скриншоты ниже redacted: job names,
    sheet names, real takeoff names — скрыты. Названия кнопок даны **как в
    интерфейсе** (англ.), пояснение — рус.; тултипы в программе совпадают с этим.

!!! abstract "Новое в программе (обновления мая 2026)"
    - **3D Roof по-новому** — таб `7 3D`: per-edge pitch вместо «Auto/Clear Roof».
      Помечаешь кромки roof base (`Select Edge`), задаёшь каждой свой pitch,
      `Generate Roof` строит ridge/hip/valley (включая вогнутые valleys),
      Revit-style envelope для U/S/L-крыш. См. [Таб 7 3D](#tab-7-3d).
    - **3D Massing — AI-черновик здания** — отдельная панель: `Build 3D Draft`,
      `3D From Takeoffs`, `AI 3D Sort`, `Review Roof`/`Review Openings`,
      `Accept 3D`. См. [3D Massing](#3d-massing).
    - **Новая модель выделения и vertex-grips** — `Ctrl` мультивыбор, `Alt`
      режим вершин, прямое перетаскивание ручек, `line cut`. См.
      [Редактирование](#editing).
    - **Page takeoff layers** — порядок (z-order) привязанных takeoff-слоёв на
      листе. **Job source selector** + переделанный `Open Job` диалог.
      См. [Прочее новое](#new-misc).

<figure markdown>
  ![1 Main View — общий вид](../assets/images/ourplanecore/opc-guide-main-view.png)
  <figcaption><code>1 Main View</code>: ribbon сверху, Pages-дерево слева, PDF-вьюпорт по центру, Takeoffs-дерево справа, tool strip снизу.</figcaption>
</figure>

## Что внутри { .kb-section-title .kb-st--cyan }

<div class="grid cards" markdown>

-   :material-file-pdf-box:{ .lg .middle .kb-mk--cyan } **PDF Workspace**

    ---

    Job, sheets, page folders, layers, overlays, scale, sheet legend, display
    settings, PDF export with measurements.

-   :material-table-edit:{ .lg .middle .kb-mk--magenta } **Sheet Manager**

    ---

    Review-gated `Auto Name` / `Auto Scale` / confidence / `Why` / warnings.
    Применяется только то, что отмечено галкой.

-   :material-ruler-square:{ .lg .middle .kb-mk--amber } **Takeoff Tools**

    ---

    `Count`, `Line`, `Area`, `J Area`, `Scale`, `Select`, `Ruler`, markups, copy/paste.

-   :material-folder-tree:{ .lg .middle .kb-mk--green } **Pages / Takeoffs**

    ---

    Слева sheets/folders, справа takeoff folders/items. Sheet selection
    подсвечивает takeoff items, и наоборот.

-   :material-chart-box-outline:{ .lg .middle .kb-mk--blue } **Estimating / Manager**

    ---

    Табличный обзор quantities, sections, units, notes, prices.
    Current-sheet filter, export commands.

-   :material-cube-outline:{ .lg .middle .kb-mk--orange } **3D Massing**

    ---

    Reviewable draft: footprint, walls, roof planes из markers/takeoffs.
    Не BIM, а visual QA для проверки openings/roof shape.

</div>

## От и до — рабочий процесс { .kb-section-title .kb-st--green }

1. **Создать / открыть job.** Таб `1 Main View` → `Open / Import`
   (++ctrl+o++) — открыть/создать job или импортировать PDF. Recent —
   ++ctrl+shift+o++.
2. **Импорт PDF.** `Open / Import` → добавить PDF (или таб `2 Sheet
   Manager` → `Import PDF(s)`).
3. **Метаданные листов.** Таб `2 Sheet Manager`: `Analyze` → `Auto Name` /
   `Auto Scale` / `Name+Scale` → проверить `Confidence` / `Why` /
   `Warnings` → `Apply Checked` (применяется **только** отмеченное).
   Нет данных в PDF → `AI Fill` (+ `Crop Hints` для зон номера/масштаба).
4. **Разложить листы.** `Sort A/S` → `D/Sec/WT` → `Auto Folders`.
   При сбитых связях measurements → `Repair Links`.
5. **Открыть лист.** Таб `1 Main View`, дерево `Pages` слева — выбрать
   sheet. Проверить scale (`Scale` tool) и слои (`PDF Layers`).
6. **Создать / выбрать takeoff item.** Справа дерево `Takeoffs` →
   `New Item` (или ++t++). Имя по правилам — [Как называть
   takeoffs](takeoff-naming.md).
7. **Рисовать.** Выбрать tool (`Count`/`Line`/`Area`/`J Area`), включить
   запись `Record` (++space++), обвести. `Scale` обязателен для Line/Area.
8. **Проверить.** Таб `3 Takeoff Manager` или `Open Estimating` — totals,
   sections, notes; `Current-sheet filter` — только активный лист.
9. **Экспорт.** Таб `3` → `Export CSV` / `TXT` / `Excel`, либо
   `Current Excel` — пишет в **уже открытый** workbook от активной ячейки
   (auto-save **нет**, проверка на пользователе).
10. **AI (опц.).** `AI Inbox` снизу: `+ Add` маркер/кроп → `Run AI` →
    review draft → accept. Quantity появляется **только** после accept.

## Верхние workspace-табы { .kb-section-title .kb-st--cyan }

| Таб | Назначение |
| --- | --- |
| `1 Main View` | Основное: PDF-вьюпорт, Pages слева, Takeoffs справа, AI Inbox снизу |
| `2 Sheet Manager` | Импорт/метаданные/раскладка листов, review-gated rename+scale |
| `3 Takeoff Manager` | Таблица quantities, sections, notes, экспорт |
| `4 Report Builder` | Сборка report-блоков из `TemplateCom.xlsm` (в разработке) |
| `5 Materials` | Извлечение material evidence + Materials Report sheet |
| `6 AI Manager` | AI-наблюдения, маркер-сеты, обучение, запуск/ретрай |
| `7 3D` | 3D massing: walls/roof build + 3D viewer |
| `8 Settings` | Редактируемые правила (см. ниже) |

## Лента над вьюпортом { .kb-section-title .kb-st--magenta }

### Таб `Main`

| Кнопка | Действие |
| --- | --- |
| `Open / Import` | Открыть job, сменить job-папку, создать job или импортировать PDF |
| `PlanSwift` | Отдельный конвертер PlanSwift-job |
| `Export` | Экспорт выбранных/всех листов в PDF |
| `Name` / `Scale` / `Name+Scale` | Превью и применение PDF-имён / масштаба / вместе |
| `AI Fill` | Очередь GPT-fallback для отсутствующих метаданных |
| `Crop Hints` | Переиспользуемые кроп-боксы для номера листа и масштаба |

<figure markdown>
  ![Ribbon Main](../assets/images/ourplanecore/opc-frag-ribbon-main.png)
  <figcaption>Ribbon <code>Main</code> + строка workspace-табов под ним.</figcaption>
</figure>

### Таб `Page`

| Кнопка | Действие |
| --- | --- |
| `Add Pages` | Импорт PDF-страниц в текущий job |
| `Batch Rename` | Переименовать выбранные страницы по порядку |
| `Left` / `Right` / `180` | Повернуть активную страницу |
| `Level` | Сброс вида к fit + очистка временного ввода |
| `Batch Rotate` | Повернуть выбранные страницы |
| `Vertical` / `Horizontal` | Отразить активную страницу |
| `Invert` | Инвертировать цвета страницы |
| `Crop New Page` | Новая страница из видимой области вьюпорта |
| `Copy` | PNG активной страницы в буфер |
| `Set Origin` / `Offset Origin` | Отметить/сдвинуть origin |
| `Close Page` | Закрыть вкладку страницы |

<figure markdown>
  ![Ribbon Page](../assets/images/ourplanecore/opc-frag-ribbon-page.png)
  <figcaption>Ribbon <code>Page</code>: Add Pages, Batch Rename, Rotate, Flip, Invert, Crop, Origin, Close.</figcaption>
</figure>

### Таб `PDF Output`

Настройки **экспортного рендера** PDF (как measurements/markups лягут в файл).

| Контрол | Действие |
| --- | --- |
| `Lines & Area` ползунки | Толщина/заливка линий и площадей в экспорте |
| `Labels` | Какие value-лейблы включать |
| Overlays `Legend` / `Header` | Включать легенду / заголовок масштаба |
| `Include` `Meas` / `Markups` | Включать замеры / аннотации в PDF |

<figure markdown>
  ![Ribbon PDF Output](../assets/images/ourplanecore/opc-frag-ribbon-pdf-output.png)
  <figcaption>Ribbon <code>PDF Output</code>: Lines &amp; Area, Labels, Overlays, Include Meas/Markups.</figcaption>
</figure>

### Таб `Viewport`

| Контрол | Действие |
| --- | --- |
| `All` / `Line` / `Area` / `Joist` / `Count` | Master + по типам: показ value-лейблов |
| `w/ page` (labels) | Лейблы масштабируются вместе со страницей |
| Legend: `Show` / `Size` / `Pos` / `w/page` | Легенда листа: показ, размер, позиция, масштаб |
| Scale header: `Size` / `w/page` | Размер заголовка масштаба |
| `Fast pan/zoom` | Упрощённая навигация (быстрее на тяжёлых PDF) |
| `ft / sf` | Imperial-единицы |
| `Viewport background` / `Page background` | Фон вьюпорта / страницы |
| `Dark` toggle | Тёмная тема |

## Панель инструментов (tool strip) { .kb-section-title .kb-st--green }

Нижняя строка под вьюпортом — основные инструменты и слайдеры выделения.

<figure markdown>
  ![Tool strip](../assets/images/ourplanecore/opc-frag-toolstrip.png)
  <figcaption>Tool strip: Pan/Select/Scale/Ruler · Annotation · Count/Line/Area/J Area/Cut · Record · Snap/PDF Snap/Ortho/Box · Fit/+/− · Flip · Rot/Scale ползунки · Scale/Set/Presets.</figcaption>
</figure>

| Кнопка | Tag / клавиша | Действие |
| --- | --- | --- |
| `Pan` | `pan` / ++v++ | Панорамирование |
| `Select` | `select` / ++e++ | Выбор/редактирование measurements |
| `Scale` | `scale` / ++s++ | Задать/проверить масштаб листа |
| `Ruler` | `ruler` / ++r++ | Временный замер без takeoff item |
| `Annotation ▾` (`Draw`/`Arrow`/`Box`/`Cloud`/`Area`/`Note`) | `drawline` ++d++ / `drawrect` ++b++ … | Аннотации поверх листа |
| `Count` | `point` / ++p++ | Счётный маркер (`ea`) |
| `Line` | `line` / ++l++ | Линейный замер (`lf`) |
| `Area` | `area` / ++a++ | Площадь (`sf`) |
| `J Area` | `joistarea` / ++j++ | Joist-раскладка (count + длина, direction/spacing/pitch) |
| `Cut` | `areacut` / ++x++ | Вырез из площади |
| `Snap` / `PDF Snap` / `Ortho` / `Box` | ++f3++ / ++ctrl+f3++ / ++f8++ / ++f9++ | Привязки и ограничения |
| `Fit` / `+` / `-` | ++f++ / ++ctrl+plus++ / ++ctrl+minus++ | Вписать / зум |
| `Flip H` / `Flip V` / `0` / `1x` | — | Отразить / сбросить поворот / сбросить масштаб выделения |
| `Set` (scale) / `▾ Presets` | — | Задать масштаб листа / пресеты |
| `AI Settings` | — | Модель и статус ключа OpenAI |

### Ползунки (sliders) { #polzunki }

| Ползунок | Диапазон | Что делает |
| --- | --- | --- |
| `Line thickness` | `0.25 – 4.0` | Толщина линий-замеров |
| `Point size` | `0.25 – 4.0` | Размер счётных маркеров |
| `Area edge` | `0.25 – 4.0` | Толщина границы площади |
| `Area fill` | `0 – 100 %` | Прозрачность заливки площади |
| `Label scale` | `0.5 – 3.0` | Размер value-лейблов |
| `Rotate selection` | `−180 … +180°` | Поворот выделенных measurements; `0` — сброс |
| `Scale selection` | `от 0.25×` | Масштаб выделенных measurements; `1x` — сброс |

!!! tip "Рядом с ползунком — поле ввода"
    У большинства ползунков есть текст-поле: впиши значение и `Enter` —
    точная установка без перетаскивания.

## Левая панель — Pages { .kb-section-title .kb-st--magenta }

| Контрол | Действие |
| --- | --- |
| `Open Tabs` / `Detach` / `Tile M2` | Открыть вкладками / в отдельных окнах / тайлинг на мониторе 2 |
| `Sort A/S` / `D/Sec/WT` | `A`→Arch, `S`→Struct, trailing `-`→Others; Details/Sections/Wall-Type |
| `Repair Links` | Переподключить сохранённые measurements к папкам страниц |
| `Page Setup` | Параметры страницы (плавающее окно) |
| `Folder template` (`Auto`/`COM`/`EWP`) | Шаблон папок для sheets |
| `New Page Folder` / `Auto Folders` | Создать папку / стандартные папки |
| Под-таб `PDF Layers` | `Load`, `On`, `Off`, `Clear Hi`, `Layer Trace` toggle, `Cycle`, `Apply` |

<figure markdown>
  ![Pages panel](../assets/images/ourplanecore/opc-frag-pages.png)
  <figcaption>Левая панель <code>Pages</code>: Tabs/Detach/Tile M2, под-табы Pages/PDF Layers/Bookmarks, дерево листов, Page Setup.</figcaption>
</figure>

## Правая панель — Takeoffs { .kb-section-title .kb-st--green }

| Контрол | Действие |
| --- | --- |
| `Record` | Вкл/выкл запись в активный item (++space++) |
| `More` / `Properties` / `Find` | Доп. действия / свойства / поиск item |
| `Sheet Next` / `Next` / `Previous` | Навигация по листам и items |
| `New Folder` / `New Item` | Создать папку / item |
| `Roof Base` | Создать roof-base слой |
| `Export ▾` | Меню экспорта |
| `Auto Tree` / `From Pages` | Стандартное дерево / из структуры страниц |

<figure markdown>
  ![Takeoffs panel](../assets/images/ourplanecore/opc-frag-takeoffs.png)
  <figcaption>Правая панель <code>Takeoffs</code>: активный item + Record, под-табы Takeoffs/Estimating/3D, дерево, New Folder/Item, Export.</figcaption>
</figure>

## Tools, scale и snap { .kb-section-title .kb-st--blue }

| Tool | Quantity | Когда |
| --- | --- | --- |
| `Count` | `ea` | Windows/doors/posts/beams count, hardware |
| `Line` | `lf` | Walls, plates, blocking, trims, railings |
| `Area` | `sf` | Sheathing, roof/floor area, slab, drywall |
| `J Area` | joist count + length | Joist layout с direction, spacing, pitch, rounding |
| `Scale` | page scale | Set/verify до Line/Area |
| `Ruler` | temp check | Проверить расстояние без takeoff item |

- `Count` можно ставить **без scale**. `Line` / `Area` **требуют sheet scale** —
  иначе record блокируется.
- Scale хранится **per page** и **per measurement**; при переносе measurement
  на другой sheet — пересчитывается.

| Snap | К чему | Когда работает |
| --- | --- | --- |
| `Snap` (++f3++) | Endpoints/midpoints/intersections **нарисованной** геометрии | Всегда |
| `PDF Snap` (++ctrl+f3++) | Vector PDF: corners, line segments, overlay | Только если PDF реально vector |
| `Ortho` (++f8++) | 90/45° constraint | Line/Area/Scale |

## Таб `2 Sheet Manager` { .kb-section-title .kb-st--orange }

Нужен, чтобы **не применять auto-renaming/scale вслепую**.

| Поле / кнопка | Что |
| --- | --- |
| `Import PDF(s)` / `Export PDF` / `Refresh` | Добавить/выгрузить PDF, перечитать таблицу |
| `Analyze` | Прочитать текст/слои PDF и показать превью метаданных |
| `Auto Name` / `Auto Scale` / `Name+Scale` | Превью авто-имён / масштаба / вместе |
| `AI Fill` / `Crop Hints` | GPT-fallback + кроп-боксы для номера/масштаба |
| `Proposed Name` / `Scale` / `Confidence` / `Why` / `Warnings` | Поля превью (что и почему предложено) |
| `Apply Checked` | Применить только отмеченные строки |
| `Sort A/S` / `D/Sec/WT` / `Auto Folders` / `Repair Links` | Раскладка и связи |

<figure markdown>
  ![Sheet Manager](../assets/images/ourplanecore/opc-guide-sheet-manager.png)
  <figcaption><code>2 Sheet Manager</code>: №, Proposed Name, Scale, Confidence, Why, Warnings + Apply Checked.</figcaption>
</figure>

## Таб `3 Takeoff Manager` { .kb-section-title .kb-st--violet }

| Кнопка | Действие |
| --- | --- |
| `Save` (++ctrl+s++) / `Refresh` | Сохранить job / перечитать таблицу |
| `Set Active` | Сделать item активной целью рисования |
| `Properties` / `Open Estimating` | Свойства / полное окно estimating |
| `New Folder` / `New Item` / `Auto Tree` / `From Pages` | Структура дерева |
| `Export CSV` / `TXT` / `Excel` | Экспорт quantities |
| `Current Excel` | Записать выбранное в активную ячейку **открытого** workbook |

<figure markdown>
  ![Takeoff Manager](../assets/images/ourplanecore/opc-guide-takeoff-manager.png)
  <figcaption><code>3 Takeoff Manager</code>: Item / Type / Sections / Total / Unit / Notes / Folder + экспорт.</figcaption>
</figure>

- **Notes** экспортируются — рабочие комментарии не теряются.
- **Multi-select** поддерживает move/copy/cut/paste/delete.

!!! warning "`Current Excel` не делает auto-save"
    Программа пишет строки, **проверка и save — на пользователе**. Это by design.

## Таб `4 Report Builder` { .kb-section-title .kb-st--green }

| Кнопка | Действие |
| --- | --- |
| `Reload` | Перезагрузить `TemplateCom.xlsm` в таблицу |
| `Refresh` | Обновить вид |
| `Apply Walls` | Применить A3 wall-block правило к выбранным строкам `J:K` |

<figure markdown>
  ![Report Builder](../assets/images/ourplanecore/opc-guide-report-builder.png)
  <figcaption><code>4 Report Builder</code>: сборка report-блоков из <code>TemplateCom.xlsm</code> (в разработке).</figcaption>
</figure>

## Таб `5 Materials` { .kb-section-title .kb-st--cyan }

| Кнопка | Действие |
| --- | --- |
| `Extract` | Извлечь material evidence из source-PDF job |
| `Report Sheet` | Создать копируемый Materials Report sheet |
| `Refresh` / `JSON` | Перечитать вывод / полный JSON |
| `Rows CSV` / `Summary CSV` | Строки evidence / сводка в CSV |
| `Folder` | Открыть папку вывода |

<figure markdown>
  ![Materials](../assets/images/ourplanecore/opc-guide-materials.png)
  <figcaption><code>5 Materials</code>: Extract / Report Sheet / JSON / Rows-Summary CSV.</figcaption>
</figure>

## Таб `6 AI Manager` { .kb-section-title .kb-st--magenta }

| Кнопка | Действие |
| --- | --- |
| `AI Settings` | Модель и статус ключа |
| `+ Add` / `Refresh` / `Open Details` / `Go to Page` | Наблюдения, навигация |
| `Run AI` / `Run New` / `Retry Failed` | Запуск AI по выбранному / всем новым / повтор неуспешных |
| `Create Set` / `Marker Sets` / `Export Markers` | Маркер-сеты и экспорт проверенных |

<figure markdown>
  ![AI Manager](../assets/images/ourplanecore/opc-guide-ai-manager.png)
  <figcaption><code>6 AI Manager</code>: наблюдения, Run AI / Run New / Retry Failed, маркер-сеты.</figcaption>
</figure>

## Таб `7 3D` — per-edge roof { #tab-7-3d .kb-section-title .kb-st--green }

| Кнопка | Группа | Действие |
| --- | --- | --- |
| `Auto` | Build | Авто-постройка walls + sqft slabs + RF/roof areas |
| `Wall` | Build | Стены-призмы из выбранных **line**-takeoff |
| `Roof Base` | Build | Roof footprint из выбранных **area**-takeoff |
| `Select Edge` | Build | Выбрать кромки roof base; задать **per-edge pitch** |
| `Generate Roof` | Build | Построить ridge/hip/valley из per-edge pitch |
| `Fit` / `Iso` / `Top` / `Front` / `Reset` | Viewer | Виды 3D-сцены |

!!! info "Per-edge roof workflow (Revit-style U/S/L крыши)"
    Старые `Auto Roof` / `Roof Edges` / `Clear Roof` заменены одним потоком:

    1. `Roof Base` — footprint из area-takeoff (RF/roof).
    2. `Select Edge` — кликаешь кромки footprint; для каждой помечаешь
       **defines slope** и задаёшь свой **pitch**. Кромка без slope — gable/rake.
    3. `Generate Roof` — солвер строит точный *lower-envelope*: ridge, hips и
       **valleys** (в т.ч. вогнутые), клиппит плоскости по mitered slope-доменам.
       Результат можно **затолкнуть обратно в takeoff-дерево** как roof-takeoff.

<figure markdown>
  ![3D](../assets/images/ourplanecore/opc-guide-3d.png)
  <figcaption><code>7 3D</code>: Build (Auto / Wall / Roof Base / Select Edge / Generate Roof) + Viewer.</figcaption>
</figure>

## 3D Massing — AI-черновик здания { #3d-massing .kb-section-title .kb-st--cyan }

Отдельная панель (под-таб `3D` справа): собирает **черновую 3D-модель здания**
из AI-маркеров или из takeoff'ов и даёт review-gated workflow до принятия.

| Кнопка | Действие |
| --- | --- |
| `Build 3D Draft` | Собрать `AI_Context/3d_massing/model.json` из AI-маркеров |
| `3D From Takeoffs` | Черновик из Line/Area замеров (Walls/Areas/Sqft) |
| `AI 3D Sort` | OpenAI сортирует role/level, затем детерминированно строит черновик |
| `3D Window` | Отдельное orbit-окно 3D |
| `Auto Roof` | Очередь reviewable AI-кандидатов roof-маркеров |
| `Review Roof` / `Review Openings` | Проверить тип крыши/pitch/guides и проёмы до принятия |
| `Accept 3D` | Пометить черновик как reviewed project context |
| `Open JSON` / `Fit` / `Iso` / `Top` / `Front` | model.json / виды |

!!! note "Порядок"
    `Build` / `From Takeoffs` / `AI 3D Sort` → (опц.) `Auto Roof` → `Review
    Roof` → `Review Openings` → `Accept 3D`. Кнопки review/accept активны
    только когда есть что ревьюить. Это **не BIM** — visual QA.

## Редактирование: выделение, vertex-grips, line cut { #editing .kb-section-title .kb-st--magenta }

Инструмент `Select` (++e++), прямое редактирование geometry во вьюпорте.

| Жест | Что делает |
| --- | --- |
| Клик по объекту | Выбрать один measurement |
| Box (рамка) | Выбрать пересечённые/охваченные measurements |
| ++ctrl++ + клик по новому | Добавить в мульти-выбор |
| ++ctrl++ + клик по выбранному | Выбрать **все его вершины** |
| ++shift++ + клик/box | Убрать из выбора |
| ++alt++ + клик/box | Режим **вершин (handles)** |
| Drag ручки | Двигать вершину(ы); ++shift++ — ортогонально |
| ++delete++ | Удалить объекты или ручки |

- **Direct vertex grips** — ручки видны прямо у выбранного measurement; count-маркеры тоже редактируются грипами.
- **Line cut** — разрез линии на месте (как area `Cut`, но для line-замеров).
- **Cut regions (area)** — вырез можно вставлять и за границей Area; paste якорится по верхнему-левому углу.

## Прочее новое { #new-misc .kb-section-title .kb-st--orange }

- **Page takeoff layers** — z-order привязанных takeoff-слоёв на листе (когда заливки area перекрывают линии).
- **Job source selector** — видимый переключатель источника job (read-only PlanSwift-источник виден явно).
- **Open Job — новый диалог** — ribbon-styled XAML; даты в инвариантном английском формате. Recent — ++ctrl+shift+o++.
- **Per-Monitor DPI v2** — корректный рендер на разных мониторах/масштабах.

## Export { .kb-section-title .kb-st--cyan }

| Export | Статус | Для чего |
| --- | --- | --- |
| CSV | ✅ | Табличный output: quantities, notes, scale, price |
| TXT | ✅ | PlanSwift-like text blocks |
| Excel `.xlsx` | ✅ | Rows в стиле `Name / Value / Unit` |
| `Current Excel` | ✅ | Пишет selected rows в **уже открытый** workbook от active cell |
| `Report Builder` | 🚧 В разработке | Полная сборка report блоков внутри app |

## AI safety rules { .kb-section-title .kb-st--magenta }

| Правило | Почему |
| --- | --- |
| AI output — **draft**, пока user не accept | Чтобы не появились quantities из ниоткуда |
| AI сохраняет request/response JSON | Можно открыть и проверить |
| AI хранит crop evidence | Видно по какому фрагменту drawing предложен result |
| AI создаёт **review rows**, не quantities | Quantities появляются только после accept |
| AI не показывает secrets | OpenAI key — found/missing, без значения |

## Mental model { .kb-section-title .kb-st--green }

Программа построена вокруг **job folder** — всё локально, ничего в облаке.

| Слой | Что хранит | Source of truth для |
| --- | --- | --- |
| `Pages` | Sheets, scale, layers | Sheet name + scale (после review) |
| `Takeoffs` | Folders, items, sections | Quantity structure |
| `Measure` | Геометрия в PDF coords | Конкретные числа quantities |
| `AI` | Crops, requests, drafts | Доказательства (НЕ quantities — пока не accepted) |

!!! tip "Главная логика"
    `Page` отвечает за drawing context и scale. `Takeoff item` — за то, что
    считается. `Measurement` связывает: на каком sheet, с каким scale, в какой
    item записана геометрия.

## «8 Settings» — редактируемые правила { .kb-section-title .kb-st--orange }

Верхний таб **8 Settings** — канонический дом для всех редактируемых шаблонов и
правил (поведение-определяющие константы не зашиты в код).

| Категория | Что настраивает |
| --- | --- |
| `Page Folders` | шаблон папок для sheets |
| `Auto Tree` / `From Pages` | авто-дерево takeoff / генерация из pages |
| `Sort A/S` / `Sort D/Sec/WT` | раскладка листов |
| `Auto Rename / Scale` | правила авто-имени и масштаба |
| `Defaults` | дефолты |

Каждая категория: live-редактор, `Reset to default`, `Save global default`,
`Save as this job`, `Apply`. Разрешение правила: **job override → global →
default** (`SettingsPresetStore`: global в `SmartContextStore/presets/`,
per-job в `<job>/AI_Context/settings/`).

<figure markdown>
  ![Settings](../assets/images/ourplanecore/opc-guide-settings.png)
  <figcaption><code>8 Settings</code>: live-редактор правила, Reset / Save global / Save as job / Apply.</figcaption>
</figure>

## Архитектура { .kb-section-title .kb-st--blue }

Для понимания, почему программа ведёт себя именно так (не для разработки).

- **Стек:** WPF desktop, `.NET 9` (`net9.0-windows`), `x64`. Namespace `OurPlaneCore`.
- **Three-panel shell** (`MainWindow` + `MainWindow.*.cs` partials): Pages tree слева, PDF viewport по центру (SkiaSharp-overlay), Takeoffs tree справа, AI Inbox снизу.
- **PDF-рендер в два слоя:** (1) статичная картинка страницы — Python-воркер (PyMuPDF, `pdf_layers_helper.py`) с layer-aware рендером; (2) overlay measurements — `PdfViewport` (SkiaSharp); fallback — Docnet/PDFium.
- **Геометрия:** `Line` = сумма отрезков × scale; `Area` = shoelace по полигону; `Count` = число маркеров. Каждый `Measurement` хранит свой `PageFolder` + scale.
- **Autosave** — debounce 500 мс после изменения measurement.
- **Настройки:** `%APPDATA%\OurPlaneCore\settings.json`; логи — `%APPDATA%\OurPlaneCore\logs\app-<yyyyMMdd>.log`.

| Слой данных | Модель | Хранит |
| --- | --- | --- |
| Job/pages | `OurPlaneCoreJob` (+ `JobStore`) | дерево job/page/folder |
| Measurement | `Measurement` | `SKPoint[]` в PDF-координатах + per-measure scale |
| Takeoff item | `TakeoffItem` | контейнер measurements |
| AI | `SmartContextStore` / `SmartLearningStore` | observations, requests/responses, обучение |
| OpenAI | `OpenAiRequestRunner` | HTTP к `/v1/responses`, ключ из `OPENAI_API_KEY` |

### Disk-модель

```text
<job>/
  Pages/        PDF sheet folders
  Takeoffs/     item folders, measurements.json
  sources/      исходные PDF
  AI_Context/   observations.jsonl, requests/, responses/, crops/, markers/, settings/
  Data.xml      per-folder item metadata
```

## Принципы разработки { .kb-section-title .kb-st--amber }

- **Local-first** — job и context на диске, ничего в облаке.
- **Review-gated** — automation показывает preview/warnings до apply.
- **Evidence-first** — AI result имеет crop/source/request/response link.
- **PlanSwift-like** — workflow привычен estimator-у.
- **No hidden magic** — если программа не уверена, она говорит почему.
- **Manual fallback** — ручной takeoff всегда работает, AI его не ломает.

## Сборка и обновление { .kb-section-title .kb-st--green }

```powershell
dotnet restore .\ourplanecore.sln
dotnet build   .\ourplanecore.sln
dotnet run --project .\ourplanecore.csproj
```

- Без параллельных билдов (lock в `obj\Debug\net9.0-windows`).
- Release single-file → `C:\Users\User\Desktop\updates\OurPlaneCore\ourplanecore.exe` (Desktop-ярлык указывает туда).
- «Запустилось ли» проверяют **не** по окну, а по `%APPDATA%\OurPlaneCore\logs\app-<date>.log` от последней `Application startup.` (процесс жив + нет `ERROR` после маркера + есть `Loaded takeoffs` / `Viewport`).

## Горячие клавиши { .kb-section-title .kb-st--blue }

=== "Global / tools"

    | Клавиша | Действие |
    | --- | --- |
    | ++ctrl+o++ / ++ctrl+shift+o++ | Open Job / Recent |
    | ++ctrl+s++ | Save |
    | ++ctrl+shift+p++ | Command Palette |
    | ++space++ | Старт/стоп записи в активный item |
    | ++t++ | Новый takeoff item |
    | ++b++ ++k++ | Add Bookmark (последовательность) |
    | ++v++ / ++e++ / ++s++ / ++r++ | Pan / Select / Scale / Ruler |
    | ++d++ / ++b++ | Draw Line / Box annotation |
    | ++p++ / ++l++ / ++a++ / ++j++ / ++x++ | Count / Line / Area / J Area / Cut |

=== "Viewport"

    | Клавиша | Действие |
    | --- | --- |
    | ++esc++ | Отмена draw/edit/Layer Trace/3D guide |
    | ++enter++ / ++tab++ | Layer Trace: дальше / цикл режима |
    | ++t++ | Toggle Layer Trace |
    | ++c++ | Завершить Line/Area/Cut |
    | ++backspace++ | Отменить последнюю точку |
    | ++delete++ | Удалить выбранное |
    | ++f++ | Fit page |
    | ++f3++ / ++ctrl+f3++ | Snap / PDF Snap |
    | ++f8++ / ++f9++ | Ortho / Box mode |
    | ++ctrl+plus++ / ++ctrl+minus++ | Зум +/− |
    | ++ctrl+z++ | Undo |
    | ++ctrl+a++ / ++ctrl+c++ / ++ctrl+v++ | Выбрать всё / копировать / вставить |

=== "Trees / 3D guides"

    | Клавиша | Действие |
    | --- | --- |
    | ++ctrl+c++ / ++ctrl+x++ / ++ctrl+v++ / ++ctrl+d++ | Copy / Cut / Paste / Duplicate |
    | ++ctrl+up++ / ++ctrl+down++ | Двигать узел вверх/вниз |
    | ++ctrl+enter++ | (Takeoffs) выбрать measurements секции на canvas |
    | ++f2++ / ++delete++ | Rename / Delete |
    | 3D Roof: ++r++ ++h++ ++v++ ++e++ ++k++ ++p++ | Ridge / Hip / Valley / Eave / Rake / Pitch guide |

## See also

- [Как называть takeoffs](takeoff-naming.md) — правила naming + auto-routing
- [Workflow](../start/workflow.md) · [Структура takeoff](../start/takeoff-structure.md)
- [Excel macro hotkeys](excel-hotkeys.md) — VBA shortcuts после export
- [Советы и важные вещи](boss-feedback-rules.md)
