# OurPlanCore 3.0

OurPlanCore - программа для замеров по PDF-чертежам: лист, масштаб, замер, дерево Takeoffs, потом экспорт в Excel DFL и PDF. Здесь карта окна, устройство раздела и путь от открытого проекта до сдачи.

<figure markdown>
  ![Окно OurPlanCore с открытым листом](../assets/images/ourplancore/v3/window-map.png)
  <figcaption markdown="span">Окно целиком, зоны пронумерованы: 1 ленты, 2 Pages, 3 лист, 4 Takeoffs, 5 полоса инструментов, 6 полоса XL, 7 строка статуса. Подробно в таблице ниже.</figcaption>
</figure>

## Карта окна { #window-map }

| # | Зона | Что там | Подробно |
| --- | --- | --- | --- |
| 1 | Ленты команд | `Main`, `Page`, `Annotation`, `PDF Output`, `Viewport`, `Display`; ниже строка режимов `Main View`, `Settings` и вкладки менеджеров (видны при включённых модулях) | [Начало работы](ourplancore-start.md) |
| 2 | Панель Pages | дерево папок и листов, кнопки `+ New`, `Setup`, `Name`, `Scale`, `Name+Scale`, поиск; под-вкладки `PDF Layers`, `Overlay`, `Bookmarks` | [Листы](ourplancore-pages.md) |
| 3 | Лист | вкладки открытых листов и сам чертёж; под заголовком Scale точки W/F/S/U и замок кропов | [Листы](ourplancore-pages.md), [Инструменты](ourplancore-tools.md) |
| 4 | Панель Takeoffs | зелёная и красная точки корня, строка активной позиции с `Record`, `Total`, `New Item`, вкладки `Takeoffs`, `Estimating`, `Templates` | [Дерево Takeoffs](ourplancore-takeoffs.md) |
| 5 | Нижняя полоса инструментов | строка 1: `Pan`, `Select`, `Scale`, `Ruler`, `Count`, `Line`, `Area`, `J Area`, `Beam`, `Open`, `Cut`, `Snap`, `Ortho`, `Box`; строка 2: `Transform`, `Scale: 1:N`, `Presets`, `Fit` | [Инструменты](ourplancore-tools.md) |
| 6 | Полоса XL | кнопки экспорта в Excel: `ALL`, `LG`, `SF`, `WL` ... `ST`; рядом кнопка `>_` терминала | [Экспорт в Excel](ourplancore-excel.md) |
| 7 | Строка статуса | `<лист>`, `Scale:`, `Zoom:`, `Mode:`, `Takeoff: ... (Route: W 1st)`, `Save: Saved hh:mm:ss`, сообщение последней команды | [Проекты и сохранение](job-creation-storage.md) |

Строка `Takeoff:` показывает, куда пойдёт следующий замер, `Save:` - сохранён ли проект. Эти две подписи стоит проверять чаще других.

## Как устроен раздел

Три уровня: что нужно каждый день, что ускоряет работу, и куда программа идёт дальше.

<div class="grid cards" markdown>

-   **Каждый день**

    ---

    - [Начало работы](ourplancore-start.md): где программа, обновление, стартовый экран, демо-проект, F1
    - [Проекты и сохранение](job-creation-storage.md): новый проект, импорт, файл `.ourplan`, автосохранение
    - [Листы (Pages)](ourplancore-pages.md): папки, имена, масштаб, точки W/F/S/U
    - [Инструменты замера](ourplancore-tools.md): Line, Area, Count, J Area, Beam, Openings и остальные
    - [Дерево Takeoffs](ourplancore-takeoffs.md): корень корпуса, Record, копирование, поиск
    - [Имена и автомаршрут](takeoff-naming.md): почему позиция легла в эту папку
    - [Экспорт в Excel](ourplancore-excel.md): полоса XL и шаблон TemplateCom
    - [PDF и сдача](ourplancore-pdf.md): Export PDF, PDF Output, Preview

-   **Продвинутое**

    ---

    - [Маршрутизация: настройки](ourplancore-routing.md)
    - [Правка takeoffs: Merge, Split, Break, Ends](ourplancore-edit-takeoffs.md)
    - [Листы: кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md)
    - [Settings и модули](ourplancore-settings.md)
    - [AI-помощь и терминалы](ourplancore-ai.md)
    - [Workspace: второй компьютер](ourplancore-workspace.md)
    - [3D и крыша](ourplancore-3d.md)

-   **Идеи и планы**

    ---

    - [Куда идёт программа](ourplancore-ideas.md): веб-версия, AI-такеофф, паритет с PlanSwift, что отклонено

-   **Справка**

    ---

    - [Горячие клавиши](ourplancore-shortcuts.md)
    - [Решение проблем](ourplancore-troubleshooting.md)
    - [Что нового](ourplancore-changelog.md)

</div>

## Путь: открыл проект, сдал работу

1. **Открыть проект.** `Main > Open / Import > Open project...` или плитка `Open a recent job` на стартовом экране. Проект приходит уже с именами листов и точками W/F/S/U. [Проекты](job-creation-storage.md)
2. **Проверить листы.** Раскрыть `00. imported/Arch`, открыть план этажа, сверить `Scale:` в статусе и точку под заголовком Scale (`Route: W 1st`). Листы без имён (`Page N`) назвать руками и поставить масштаб `S`. [Листы](ourplancore-pages.md)
3. **Дерево Takeoffs.** `More > Auto Tree` даёт корни COM-шаблона; несколько корпусов - папка на каждый, зелёная точка на текущем. [Дерево](ourplancore-takeoffs.md), [канон дерева](../start/takeoff-structure.md)
4. **Замеры по scope.** Один scope на проход листа: стены `L`, проёмы `O`, площади `A`, joists `J`, балки `B`, посты и holdowns `P`. `Space` продолжает выбранную позицию. [Инструменты](ourplancore-tools.md), порядок замеров в [процессе работы](../start/workflow.md)
5. **Имена позиций.** Имя несёт числа для Excel: `ext 2x6 9.09`, `4.3x7.8 d`, `rf 6`, `eve 24 main`. Новая позиция сама ложится в папку по точке листа и имени. [Имена и автомаршрут](takeoff-naming.md), [форматы имён](../start/takeoff-structure.md)
6. **Проверка.** Вкладка `Estimating`, `Total` у позиции, легенда листа (`Organize > Sort Sheet Legend by Key`), `H` скрывает готовое, `Delete Empty` убирает пустые позиции. [Дерево](ourplancore-takeoffs.md)
7. **Excel.** Открыть книгу корпуса из `TemplateCom.xlsm`, выделить корпус в Takeoffs, нажать `ALL` на полосе XL или кнопки по шагам; `LG` заполнить до экспорта. [Экспорт в Excel](ourplancore-excel.md), [книга DFL](dfl-overview.md)
8. **PDF и сдача.** `Ctrl+S`, спрятать лишнее (`H`, маска Hide), `PDF Output > Preview`, затем `Main > Export`: только листы с замерами, отдельный PDF на корпус. Дальше processed xlsx и `Changes.txt` для ревизии. [PDF и сдача](ourplancore-pdf.md), [сдача](../start/workflow.md)

## Что появилось в 3.0 { #whats-new }

Если работал в прежней версии, вот что изменилось в повседневных действиях. Полный список по сборкам - [Что нового](ourplancore-changelog.md).

| Было | Стало | Где читать |
| --- | --- | --- |
| новую позицию раскладывали по этажам руками | точка W/F/S/U на листе ставится по имени листа и раскладывает новые позиции сама; строка `Route:` в статусе | [Листы](ourplancore-pages.md#dots), [Имена и автомаршрут](takeoff-naming.md) |
| `eve`, `prpt`, `gable`, Openings ложились куда попало | правила по имени и инструменту (`Settings > Takeoff Name Routing`) | [Маршрутизация: настройки](ourplancore-routing.md) |
| один корень Takeoffs | зелёная и красная точки выбирают корпус для новых позиций; вставка копий зеркалит папки | [Дерево Takeoffs](ourplancore-takeoffs.md#root) |
| `H` был маркером | `H` скрывает позицию на листе, маркер на `Shift+H` | [Дерево Takeoffs](ourplancore-takeoffs.md#hide) |
| Merge и Split только сегментов | Merge и Split целых позиций из дерева, Break и Ends для линий | [Правка takeoffs](ourplancore-edit-takeoffs.md) |
| Excel руками по кускам | полоса XL: `ALL` и кнопки по секциям, framing, легенда `LG`, точка "комментарии" | [Экспорт в Excel](ourplancore-excel.md) |
| детали узлов искали по листам | `Crop to Sheet` собирает узлы на чистый лист, маска `Hide` убирает лишнее, `Opac` в PDF | [Листы: продвинутое](ourplancore-sheets-advanced.md) |
| имена листов проверяли по одному | `Name+Scale` по всему комплекту, OCR сканов, чтение штампа моделью | [Листы](ourplancore-pages.md) |
| помощь ИИ только через кропы | терминалы Claude и Codex в окне (`>_`), Agent Bridge, общий Workspace на два компьютера | [AI-помощь](ourplancore-ai.md), [Workspace](ourplancore-workspace.md) |

## Куда переехали старые разделы { #tools }

Прежняя длинная страница разошлась по новым. Инструменты и привязки Snap - [Инструменты замера](ourplancore-tools.md); выделение, копирование и правка - [Дерево Takeoffs](ourplancore-takeoffs.md) и [Правка takeoffs](ourplancore-edit-takeoffs.md); модули и Settings - [Settings и модули](ourplancore-settings.md); клавиши - [Горячие клавиши](ourplancore-shortcuts.md); создание job и файлы на диске - [Проекты и сохранение](job-creation-storage.md).

## См. также

- [Процесс работы](../start/workflow.md): от папки клиента до `.Finished`
- [Дерево takeoff и имена листов](../start/takeoff-structure.md): канон папок и имён
- [Частые ошибки: листы и дерево](../start/common-mistakes.md#pages)
