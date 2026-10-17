# Дополнительные возможности

Здесь собрано то, что в OurPlanCore 3.0 есть, но в повседневном замере E-Wood почти не нужно: привязки и трассировка, вкладки менеджеров, 3D, закладки, калькулятор, импорт старых работ. Страницы уровней "Каждый день" и "Продвинутое" держат про эти функции одну строку со ссылкой сюда, чтобы не отвлекать от стен, площадей и framing. Если функция понадобилась, всё описано на страницах этого уровня.

## Что сюда вошло и почему

Критерии отбора (решение владельца 17.10.2026):

1. **Модуль выключен по умолчанию** в `Settings > Modules`: Sheet Manager, Takeoff Manager, Report Builder, Materials, AI, 3D, Job Tracker. Без включения модуля кнопок и вкладок нет.
2. **Функции нет в рабочих правилах замера.** Ни один из скилов по стенам, проёмам, framing, кровле, shear walls и units не упоминает Snap, Ortho, Box, Layer Trace, Wall Trace, закладки, калькулятор, открепленные окна, шаблоны деревьев и импорт PlanSwift. Канон замера держится на Line, Area, Count, J Area, Beam, Openings, Record, точках листа, полосе XL и Export PDF.
3. **Функцию заменил более новый путь.** Report Builder уступил полосе XL, AI 3D Massing заменила детерминированная крыша по рёбрам, вставка PDF Takeoffs и PlanSwift нужна только для старых работ.

Что остаётся на своих уровнях: инструменты Line, Area, Count, J Area, Beam, Openings, Pitch, Ruler, Record и копирование; точки W/F/S/U; полоса XL; Export PDF и Preview; правка и привязки одной связкой (Cut, Merge, Split, Break, Ends, Combine, Similar, P Line, Snap, Ortho, Box) на странице [Правка и привязки](ourplancore-editing.md); Crop to Sheet, маска Hide, Overlay, группы легенды; 3D-крыша; Settings; консоль ИИ и Agent Bridge; Workspace.

## Таблица функций

| Функция | Модуль, по умолчанию | Когда пригодится | Страница |
| --- | --- | --- | --- |
| Snap, PDF Snap, Ortho, Box | без модуля, кнопки всегда на полосе | точный контур по векторному чертежу, прямые углы, прямоугольник двумя кликами | [Правка и привязки](ourplancore-editing.md) |
| PDF Layers, Layer Trace | PDF Layers, включён | стены или контур лежат отдельным слоем PDF | [Привязки и трассировка](ourplancore-snap-trace.md#layers) |
| Trace Walls Inside Area | Advanced Takeoff Tools, включён | векторный план: центрлинии стен внутри площади одним действием | [Привязки и трассировка](ourplancore-snap-trace.md#wall-trace) |
| Trace wall from this point, Trace closed area, Check missed takeoffs | AI, выключен | запросы в AI Inbox на трассу или проверку | [Привязки и трассировка](ourplancore-snap-trace.md#ai-trace) |
| Sheet Manager | Sheet Manager, выключен | массовая правка имён, масштаба и растра таблицей; `Crop Hints`, `AI Fill` | [Менеджеры](ourplancore-managers.md#sheet-manager) |
| Takeoff Manager | Takeoff Manager, выключен | дерево Takeoffs как таблица с ценами | [Менеджеры](ourplancore-managers.md#takeoff-manager) |
| Report Builder | Report Builder, выключен | старый путь стен в `TemplateCom.xlsm` | [Менеджеры](ourplancore-managers.md#report-builder) |
| Materials | Materials, выключен | список материалов из дерева в CSV | [Менеджеры](ourplancore-managers.md#materials) |
| AI Inbox, AI Manager, маркеры | AI, выключен | очередь запросов к модели, образцы символов | [Менеджеры](ourplancore-managers.md#ai-manager) |
| Job Tracker, кнопка `In Progress` | Job Tracker, выключен | карточка проекта в трекере из программы | [Менеджеры](ourplancore-managers.md#job-tracker) |
| 3D: стены и крыша, Roof Qty | 3D, выключен | увидеть рёбра сложной крыши в объёме | [3D и Massing](ourplancore-3d.md) |
| AI 3D Massing | выключен в коде | нет, архив | [3D и Massing](ourplancore-3d.md#massing) |
| Bookmarks | Bookmarks, включён | возвращаться к месту на большом листе | [Прочее](ourplancore-extras-other.md#bookmarks) |
| Quick Calculator | Quick Calculator, включён | сложить футы, дюймы и дроби без выхода из программы | [Прочее](ourplancore-extras-other.md#calculator) |
| Detached Sheets, `Tile M2` | Detached Sheets, включён | второй монитор, два листа рядом | [Прочее](ourplancore-extras-other.md#detached) |
| Similar по всем листам | Advanced Takeoff Tools, включён | один символ на десятках листов | [Правка и привязки](ourplancore-editing.md) |
| Takeoff Templates | Takeoff Templates, включён | повторяющиеся заготовки позиций | [Прочее](ourplancore-extras-other.md#templates) |
| Импорт PlanSwift, Import PDF Takeoffs | без модуля | старая работа из PlanSwift или PDF с чужими аннотациями | [Прочее](ourplancore-extras-other.md#import) |

## Как включить модуль { #enable }

1. `Settings > Modules`: галка у модуля, `Apply` (до перезапуска) или `Save global default`; `Save as this job` включает модуль только в открытом проекте.
2. Пресеты `Current default`, `All modules on`, `Takeoff Only`, `Minimal` ставят весь набор сразу; `Reset` возвращает встроенный.
3. Включённый модуль добавляет свою вкладку в строку режимов (Sheet Manager, Takeoff Manager, Report Builder, Materials, AI Manager, 3D) или кнопки на ленту (`Name`, `Scale`, `Name+Scale`, `In Progress`).
4. Выключенный модуль прячет кнопки и вкладку; клавиша на спрятанную команду не срабатывает.

Полный список модулей с группами: [Workspace и модули](ourplancore-workspace.md#modules).

## Редкие пункты меню замера на листе { #measurement-menu }

ПКМ по замеру на листе открывает меню правки; копирование, Merge, Split и другие частые пункты описаны на странице [Правка и привязки](ourplancore-editing.md). Здесь пункты, которые нужны редко:

| Пункт | Что делает | Когда нужно |
| --- | --- | --- |
| `Takeoff Properties...` | окно свойств всей позиции, как ПКМ по позиции в Takeoffs | поменять имя, цвет или Notes позиции, не ища её в дереве |
| `Section Properties...` (у Count `Count Properties...`) | имя и `Notes` одного замера (секции); у замера без позиции в дереве пункт серый и называется `Measurement Properties...` | подписать один кусок позиции, например `per S2.1` |
| `Set / Reset Joist Direction` | у Area: направление joists двумя кликами на этом замере | развернуть шаг joists в одной зоне |
| `Set Direction for All Areas` | у Area: направление рисуется один раз двумя кликами на этом замере и ставится всем Area-замерам этой позиции на всех листах; позиция становится joist-позицией | много зон перекрытия с одним направлением, как у [J Area](ourplancore-tools.md#jarea) |

Пункты joists видны у Area при включённом модуле Advanced Takeoff Tools (включён по умолчанию); те же два пункта есть в ПКМ по позиции в Takeoffs. Комментарии `Notes` идут в Excel при включённой точке на кнопке `Excel` ([комментарии в Excel](ourplancore-excel.md#notes)).

## Страницы уровня

<div class="grid cards" markdown>

-   **[Привязки и трассировка](ourplancore-snap-trace.md)**

    ---

    Вкладка PDF Layers и Layer Trace; Trace Walls Inside Area; запросы трассы через AI Inbox. Сами привязки Snap, PDF Snap, Ortho, Box вместе с правкой замеров: [Правка и привязки](ourplancore-editing.md).

-   **[Менеджеры](ourplancore-managers.md)**

    ---

    Sheet Manager, Takeoff Manager, Report Builder, Materials, AI Inbox и AI Manager, Job Tracker: вкладки, которые включаются в `Settings > Modules`.

-   **[3D и Massing](ourplancore-3d.md)**

    ---

    Стены и крыша из замеров, Roof Qty и Roof Takeoff, что выключено и почему.

-   **[Прочее](ourplancore-extras-other.md)**

    ---

    Bookmarks, Quick Calculator, открепленные окна и `Tile M2`, Similar по всем листам, Templates, импорт PlanSwift и PDF Takeoffs.

</div>

## См. также

- [OurPlanCore 3.0: хаб раздела](ourplanecore.md)
- [Settings и модули](ourplancore-settings.md), [Workspace и модули](ourplancore-workspace.md#modules)
- [Идеи и планы](ourplancore-ideas.md): что из дополнительного ещё в разработке
