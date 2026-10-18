# Начало работы

Здесь: где лежит программа и как обновляется, что видно при первом запуске, как открыть демо-проект и что в нём попробовать, где искать команды (F1, палитра) и где живут настройки. Нужно в первый день и после каждого обновления. Учиться по шагам - [Первые шаги: 10 уроков](ourplancore-course.md).

## Где программа и как обновляется

| Что | Где |
| --- | --- |
| Запуск | ярлык OurPlanCore на рабочем столе |
| Сама программа | один файл `ourplancore.exe` в папке `Desktop\updates\OurPlanCore` |
| Обновление | в ту же папку кладётся новый `ourplancore.exe`; прежний остаётся рядом как `.bak` для отката |
| Шаблоны Excel | в той же папке: `TemplateCom.xlsm`, `TemplateResidential.xlsm` |
| Версия | в заголовке окна: `OurPlanCore 3.0.0 - <проект>`; то же в свойствах файла и в первой строке `Version ...` лога `%APPDATA%\OurPlanCore\logs\app-<дата>.log`; что изменилось - [Что нового](ourplancore-changelog.md) |

Проекты, настройки и шаблоны от обновления не зависят: они лежат отдельно (см. [Где лежат настройки](#settings)).

!!! warning "Откат на .bak"
    Старая сборка читает кропы (Crop to Sheet) и маски Hide как обычную разметку и при сохранении теряет их поля. Откатился - не сохраняй проект с кропами, пока не вернулся на свежую сборку.

## Первый запуск и стартовый экран

<figure markdown>
  ![Стартовый экран без проекта](../assets/images/ourplancore/v3/start-screen.png)
  <figcaption markdown="span">Четыре плитки. `Open / Import` на ленте Main доступен всегда, `F1` показывает клавиши.</figcaption>
</figure>

| Плитка | Что делает |
| --- | --- |
| `Open a recent job` | список недавних проектов и папок с работами |
| `New blank job` | пустой проект, листы добавляются потом |
| `New job from PDFs` | проект из папки с PDF-чертежами |
| `Open sample job` | демо-проект для знакомства |

Дальше работа идёт в `Main View`: слева Pages, в центре лист, справа Takeoffs, внизу полоса инструментов. Карта окна - на [хабе раздела](ourplanecore.md#window-map).

## Демо-проект: экскурсия { #demo }

<figure markdown>
  <video class="kb-demo" loop muted playsinline preload="none" poster="../../assets/images/ourplancore/demo/d-open-sample.png"><source src="../../assets/images/ourplancore/demo/d-open-sample.mp4" type="video/mp4"></video>
  <figcaption markdown="span">Демонстрация: `Open sample job` на стартовой карточке создаёт демо-проект; дальше листы W, F, S и U со своими легендами и вкладка 3D.</figcaption>
</figure>

Демо-проект - учебная работа без клиентских данных. На нём пробуют каждую кнопку, не боясь испортить: его можно создать заново в любой момент. По нему же идёт курс [Первые шаги: 10 уроков](ourplancore-course.md).

### Как открыть демо-проект

Зачем: получить проект с листами, точками и деревом по канону, где можно учиться.
Нужно: программа запущена; проект открывать не обязательно.

1. Нажмите плитку **Open sample job** на стартовом экране или откройте **Main > Open / Import > Sample job (demo to explore)**; тот же пункт есть ссылкой `Sample` внизу диалога **Open project...**.
2. Дождитесь статуса `Sample project created: OurPlanCore Guide Sample.`: программа создаёт проект в папке работ и сразу открывает его.
3. Раскройте в Pages папку `00. Guide` и щёлкните лист плана.

Результат: в заголовке окна `OurPlanCore 3.0.x - OurPlanCore Guide Sample`, слева листы, справа дерево Takeoffs с готовыми позициями, в статусе `Scale:` и `Route:`.

### Что внутри

<!-- CHECK-DEMO -->

| Что | Где смотреть | Зачем |
| --- | --- | --- |
| Карточки-подсказки `00. Guide` | листы-картинки в начале папки Pages | карта окна, лент и панелей прямо в программе |
| План с точкой W, структурный план с точкой F, копия под shear walls с точкой S, план юнита с точкой U | листы в `00. Guide`, точки под заголовком Scale | как раскладывается комплект ([раскладка по листам](ourplancore-split-by-sheets.md)) |
| Дерево по канону: `sqfts`, `walls/1st floor walls`, `framing/1st floor framing/...`, `openings`, `shear walls`, `eves rakes` | панель Takeoffs | имена позиций с числами для Excel, папки по этажам |
| Контур крыши `rf 6` с карнизами | план кровли и `sqfts`, `eves rakes` | заготовка для 3D-крыши ([3D-крыша](ourplancore-3d-roof.md)) |
| Заметка `Start here...` и наблюдения в AI Inbox | лист плана, панель Inbox при модуле AI | пример разметки и записей ИИ |

Точный состав демо после выпуска 3.0.1 сверяется по самому проекту: названия позиций и листов в таблице ориентировочные.

### Что попробовать по шагам

1. **Листы и точки.** Откройте план, прочитайте `Route: W 1st` в статусе; нажмите `F2` и верните то же имя: точка не меняется. Сделайте копию листа (`Ctrl+D`), переименуйте в `... sw`, щёлкните точку S. [Раскладка по листам](ourplancore-split-by-sheets.md#copy-dot)
2. **Роутинг.** Нажмите `L`, впишите имя `ext 2x6 9.09`, посмотрите строку назначения в диалоге New Item, нарисуйте два клика и `C`: позиция стоит в `walls/1st floor walls`. [Имена и автомаршрут](takeoff-naming.md)
3. **Инструменты.** На том же плане `O` по двери, `A` по комнате, `X` вырез в площади; на структурном листе `J` зона joists и `B` балка от опоры до опоры. [Инструменты](ourplancore-tools.md)
4. **Легенда.** `Display > Legend Show`, затем ПКМ по листу `Organize > Sort Sheet Legend by Key`; `H` на позиции прячет её с листа, точка у позиции под листом в Pages возвращает. [Дерево Takeoffs](ourplancore-takeoffs.md#hide)
5. **Кропы и маска.** `Page > Blank Sheet`, затем `Page > Crop to Sheet` с плана на пустой лист; `Annotation > Hide` боксом по лишнему. [Листы: продвинутое](ourplancore-sheets-advanced.md)
6. **3D.** Включите модуль 3D, выделите `rf 6`, вкладка 3D, `Roof Base`, `Auto`, `Iso`. [3D-крыша](ourplancore-3d-roof.md)
7. **Экспорт.** `PDF Output > Preview`, `Main > Export` одного листа; при открытой копии `TemplateCom.xlsm` - полоса XL, кнопка `WL`. [PDF и сдача](ourplancore-pdf.md), [Экспорт в Excel](ourplancore-excel.md)

### Испортил демо, что дальше

Всё можно: удалять позиции, двигать листы, менять точки, чистить дерево `Delete Empty`. Чтобы начать с чистого листа, снова нажмите **Open sample job**: программа создаёт новую копию с уникальным именем (`OurPlanCore Guide Sample (2)`), старая остаётся в папке работ; удалить её можно из проводника через `Open in Explorer` или оставить как свою песочницу. Настройки программы (`Settings`) демо не трогает, глобальные правила остаются вашими.

## F1 и палитра команд

<figure markdown>
  ![Палитра команд](../assets/images/ourplancore/v3/command-palette.png)
  <figcaption markdown="span">`Ctrl+Shift+P`: любая команда по имени, с текущей клавишей рядом.</figcaption>
</figure>

| Клавиша | Что открывает |
| --- | --- |
| `F1` | шпаргалка клавиш поверх окна; закрывается `Esc` |
| `Ctrl+Shift+P` | палитра команд: категории File, View, Workspace, Tools, Edit, Pages, Sheets, Takeoffs, AI; набери часть названия и `Enter` |
| `Ctrl+O` | `Open / Import`; `Ctrl+Shift+O` - недавние проекты |

Команда без клавиши (например `Ends`, `Toggle Dark Theme`, `Hide / Show All Takeoffs`) запускается из палитры или получает клавишу в `Settings > Keyboard Shortcuts`. Клавиши работают по физическим кнопкам в английской и русской раскладке. Полный список - [Горячие клавиши](ourplancore-shortcuts.md).

<figure markdown>
  <video class="kb-demo" loop muted playsinline preload="none" poster="../../assets/images/ourplancore/demo/d-command-palette.png"><source src="../../assets/images/ourplancore/demo/d-command-palette.mp4" type="video/mp4"></video>
  <figcaption markdown="span">Демонстрация: ++ctrl+shift+p++, набрать `show all`, ++enter++: команда `Hide / Show All Takeoffs` прячет все замеры листа, второй запуск показывает их.</figcaption>
</figure>

## Тема и вид листа

Лента `Display`:

| Кнопка | Что делает |
| --- | --- |
| `Dark` | тёмная тема окна |
| `Paper` | тон бумаги листа: White, Soft gray, Medium gray, Dark gray, Warm, Soft green, Black |
| `Edge` | фон вокруг листа: White, Gray, Dark |
| `Static image`, `DPI` | лист как один растр (по умолчанию включено, 150 DPI); `Black vector` рисует вектор чёрным |
| `Legend Show / Size / Pos` | легенда замеров на листе |
| `Zoom` | шаг колеса мыши |

Тёмная тема удобна на длинных сессиях, но проверять цвета позиций перед PDF лучше на белой бумаге: PDF печатается на белом.

## Как сделать первый замер { #first-run }

Зачем: за пять минут пройти путь от открытого проекта до сохранённой позиции.
Нужно: проект с именованными листами (из приёма или демо).

1. Нажмите `Ctrl+O` и выберите **Open project...** ([проекты](job-creation-storage.md)).
2. Раскройте в Pages `00. imported/Arch`, откройте план этажа, прочитайте в статусе `Scale:` и точку под заголовком Scale ([листы](ourplancore-pages.md)).
3. Нажмите `L`, назовите позицию `ext 2x6 9.09`, обведите наружные стены, нажмите `C` ([инструменты](ourplancore-tools.md)).
4. Найдите в Takeoffs, куда легла позиция: `walls/1st floor walls` при точке W 1 ([имена и автомаршрут](takeoff-naming.md)).
5. Выделите позицию, нажмите `Space`, дорисуйте ещё участок: Record продолжает позицию, а не создаёт новую ([дерево](ourplancore-takeoffs.md)).
6. Нажмите `Ctrl+S` и дождитесь `Save: Saved hh:mm:ss`.

Результат: позиция с двумя секциями в `walls/1st floor walls`, `Total` в LFT, проект сохранён. Дальше по шагам: [Первые шаги: 10 уроков](ourplancore-course.md).

## Что означают сущности

<figure markdown>
  ![Проект, лист, позиция и замер](../assets/images/ourplanecore/project-workflow.svg)
  <figcaption markdown="span">Лист задаёт чертёж и масштаб, позиция (takeoff item) - что считаем, замер связывает их. Это схема данных, не снимок окна.</figcaption>
</figure>

| Сущность | Роль |
| --- | --- |
| Project / Job | весь проект: листы, дерево Takeoffs, настройки проекта, исходные PDF; один файл `.ourplan` |
| Page / Sheet | лист с масштабом, точкой W/F/S/U, легендой и наложениями |
| Takeoff item (позиция) | именованный контейнер замеров одного типа: Line, Area, Count, Joist Area |
| Measurement (замер) | геометрия на конкретном листе; одна позиция может собирать замеры с нескольких листов |
| Annotation (разметка) | пометки без количества: Highlight, Draw Line, Arrow, Box, Cloud, Note, Hide |

## Где лежат настройки { #settings }

| Что | Где |
| --- | --- |
| Общие настройки, клавиши, логи | `%APPDATA%\OurPlanCore` (`settings.json`, папка `logs`) |
| Пресеты правил (маршрутизация, клавиши), кеши, терминалы | `%LOCALAPPDATA%\OurPlanCore` |
| Настройки конкретного проекта | внутри проекта в `AI_Context/settings` |
| Проекты | папка работ, которую показывает `Open project...` (`Manage job folders...` добавляет папки) |

Каждый раздел `Settings` имеет `Reset`, `Save global default` и `Save as this job`: правило можно переопределить для одного проекта, не трогая общее. Какие разделы есть - [Settings и модули](ourplancore-settings.md). Часть вкладок (Sheet Manager, Takeoff Manager, Report Builder, Materials, AI, 3D, Job Tracker) по умолчанию выключена и включается в `Settings > Modules`; что они делают и когда нужны - [Дополнительные возможности](ourplancore-extras.md).

## См. также

- [OurPlanCore 3.0: хаб раздела](ourplanecore.md)
- [Процесс работы](../start/workflow.md)
- [Решение проблем](ourplancore-troubleshooting.md)
