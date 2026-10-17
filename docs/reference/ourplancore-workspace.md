# Workspace, Job Tracker, импорт проекта, CLI и модули

Здесь - то, что связывает OurPlanCore 3.0 с остальным рабочим процессом: общее рабочее пространство для второго компьютера, кнопка Job Tracker, импорт одного проекта в другой, консольный `OurPlanCoreCli` конвейера приёма и список модулей. Нужно при работе с ноутбука, при ревизиях и когда не хватает кнопки или вкладки.

## Workspace: общее рабочее пространство {#workspace}

<figure markdown>
  ![Settings, раздел Workspace](../assets/images/ourplancore/v3/settings-workspace.png)
  <figcaption markdown="span">Сервер и устройство, синхронизация, подключение другого компьютера, список проектов и диалогов.</figcaption>
</figure>

**Что это.** Частный сервер хранит общие правила и заметки, скилы агентов, пресеты настроек, выбранные сохранённые проекты и архивы диалогов Claude и Codex. Программа работает локально и синхронизируется в фоне; редактирование плана и терминал сервера не ждут. Локальная папка по умолчанию `Documents\OurPlanCore Workspace`; внутри `knowledge`, `skills`, `profile`, `projects`, `conversations` и `runtime` (рабочая проекция для ассистентов).

| Группа в `Settings > Workspace` | Кнопки и поля |
| --- | --- |
| This computer | `Use shared workspace`, имя устройства, `Local workspace folder`, `Automatic synchronization` с интервалом, категории (`Claude / Codex skills and supporting scripts`, `Shared conversation archives`), `Save`, `Sync now`, `Import this setup`, `Open local folder`, `Server status` |
| Workspace server | адрес сервера (хранится на каждом устройстве отдельно) |
| Connect another computer | `Create code for another computer` (одноразовый код на 10 минут), `Connect this computer` |
| Projects | `Share current saved project`, `Open selected`, `Review conflicts`, `Apply shared presets` |
| Conversations | `Continue selected`, `Setup on this computer`, `Import a Claude / Codex conversation` |

### Второй компьютер

1. На основном: `Settings > Workspace`, `Use shared workspace`, подключить устройство, `Import this setup` (исходные папки не меняются).
2. `Share current saved project` для нужного `.ourplan`: пакет уходит на сервер, следующие сохранения синхронизируются сами.
3. На втором: установить программу, в `Settings > Workspace` ввести адрес сервера и код из `Create code for another computer`, `Connect this computer`. Правила и скилы скачаются; проекты и диалоги - по запросу.
4. `Projects > Open selected` открывает общий проект. Для терминалов на новом компьютере нужны Git Bash и вход в CLI ассистента один раз.
5. Перед сменой компьютера: ++ctrl+s++, `Sync now`, дождаться статуса Synced.

### Конфликты и ограничения

- Конфликт сохраняет обе версии: `Review conflicts`, затем `Keep this computer`, `Use server version` или `Open preserved files`.
- Открытый проект серверной версией не заменяется; изменённый локальный файл при скачивании не перезаписывается.
- Удаление между устройствами не распространяется. Кешированные проекты и знания доступны офлайн.
- Общие пресеты применяются только кнопкой `Apply shared presets`; проектные копии настроек остаются сильнее; локальные пресеты перед этим бэкапятся.
- Диалог размером больше 256 MB пропускается с предупреждением, остальные синхронизируются (3.0).
- Ключи, вход в ассистентов и личные папки не импортируются и не синхронизируются.

## Job Tracker: кнопка In Progress

Модуль `Job Tracker` (группа Integrations) по умолчанию выключен: `Settings > Modules`, галка. После этого на ленте Main в группе JOB появляется кнопка `In Progress`.

1. Имя проекта должно начинаться с номера: `NN. Name`. Иначе в статусе: `'<имя>' has no leading project number (expected 'NN. Name'); Job Tracker was not updated.`
2. Кнопка берёт номер и запускает внешнюю команду конвейера; статус: `Setting Job Tracker card NN to In Progress...`, потом `Job Tracker: project NN set to In Progress.`
3. Команда правится в `Settings > Modules`: `Executable`, `Arguments (one per line)`, `Save`, `Reset` (возвращает команду конвейера по умолчанию). Подстановка `{number}` - номер проекта.

Карточка в done ставится конвейером при сдаче, не из программы.

## Импорт проекта OurPlanCore в открытый

`Main > Open / Import > Import into the current job > OurPlanCore project...`

1. `Choose .ourplan file...` или `Choose project folder...` (папка с `Data.xml`, `Pages`, `Takeoffs`).
2. Диалог готовит приватную копию и показывает число листов, takeoff и замеров; поле `Folder name in Pages and Takeoffs` - имя новых веток.
3. `Import`: всё добавляется отдельными папками в Pages и Takeoffs, существующее и настройки проекта не трогаются. Повторный импорт создаёт ещё одну ветку.
4. Откат: `Open / Import > Undo Last Page Operation`.

Зачем: собрать корпуса из разных проектов или подтянуть старую работу в ревизию. Ссылки кропов на листы другого проекта при импорте не переназначаются.

## OurPlanCoreCli: консоль конвейера

Отдельная программа без окна, которой пользуется конвейер приёма и сдачи; эстиматор её не запускает, но видит результат: проект приходит уже с именами листов, папками и точками W/F/S/U, PDF при сдаче собирается по корпусам.

| Команда | Что делает | Опции |
| --- | --- | --- |
| `create` | новый `.ourplan` из PDF; с `--base-project` - пакет ревизии поверх оригинального проекта | `--name`, `--package`, `--pdf` (несколько), `--raster-dpi` (150), `--no-raster`, `--base-project`, `--import-folder REV`, `--report` |
| `inspect` | отчёт о листах, папках и замерах пакета | `--package`, `--report` |
| `apply-sheets` | применить имена, папки, масштаб и точки листов из JSON; делает бэкап пакета | `--package`, `--sheets`, `--dry-run`, `--report` |
| `export-pdf` | PDF только с листами, где есть замеры; `--grouping auto` делит по корпусам из зелёной точки, `--grouping single` - один файл | `--package`, `--out`, `--grouping`, `--dry-run`, `--overwrite`, `--report` |
| `excel-plan` | план экспорта в Excel по дереву | `--package`, `--scope <путь под Takeoffs>`, `--report` |

Каждая команда печатает один JSON; коды выхода: 0 успех, 1 ошибка команды, 2 ошибка вызова. Команды, меняющие пакет, отказываются работать при открытой программе: `Refused to ...: OurPlanCore is running. Close it first.` Экспорт берёт настройки PDF Output из проекта: Opac, легенда и её группы, наложения, кропы и маски.

## Модули {#modules}

<figure markdown>
  ![Settings, раздел Modules](../assets/images/ourplancore/v3/settings-modules.png)
  <figcaption markdown="span">Галки модулей по группам, пресеты и команда Job Tracker внизу.</figcaption>
</figure>

`Settings > Modules`, пресеты `Current default`, `All modules on`, `Takeoff Only`, `Minimal`; Apply, Save global, Save for this job, Clear job override, Reset.

| Модуль | Группа | По умолчанию | Что включает |
| --- | --- | --- | --- |
| Annotations | Productivity | вкл | лента Annotation: Highlight, Draw Line, Arrow, Box, Cloud, Area, Hide, Note; кропы и маски в PDF |
| PDF Layers | Documents | вкл | под-таб PDF Layers, подсветка слоёв, Layer Trace |
| Sheet Overlay | Documents | вкл | под-таб Overlay, Batch Overlay |
| Sheet Manager | Documents | выкл | вкладка Sheet Manager; кнопки Name, Scale, Name+Scale на ленте Main |
| Takeoff Manager | Takeoff | выкл | вкладка Takeoff Manager |
| Advanced Takeoff Tools | Takeoff | вкл | Similar, P Line, Combine, Beam, Openings, Break, Ends |
| Takeoff Automation | Takeoff | вкл | Auto Tree, From Pages, автосоздание |
| Takeoff Templates | Takeoff | вкл | вкладка Templates |
| Estimating | Takeoff | вкл | вкладка Estimating и окно Estimating |
| Report Builder | Output | выкл | вкладка Report Builder |
| Materials | Output | выкл | вкладка Materials |
| AI | Assistance | выкл | AI Inbox, AI Manager, AI crop, маркеры, AI по штампу |
| 3D | Assistance | выкл | вкладка 3D и под-таб 3D в Takeoffs |
| Bookmarks | Productivity | вкл | под-таб Bkm, закладки и кропы-закладки |
| Quick Calculator | Productivity | вкл | калькулятор футов и дюймов |
| PDF Output | Output | вкл | лента PDF Output, Preview, экспорт |
| Detached Sheets | Documents | вкл | открепленные окна листов, Tile M2 |
| Excel Integration | Output | вкл | полоса XL, Value, Excel |
| Job Tracker | Integrations | выкл | кнопка In Progress |

Выключенный модуль прячет кнопки и вкладку; клавиша на его команду не срабатывает. Проектная копия модулей сильнее глобальной.

## См. также

- [Проекты и сохранение](job-creation-storage.md)
- [ИИ в программе](ourplancore-ai.md) - терминалы и Agent Bridge
- [Settings: все категории](ourplancore-settings.md)
- [Экспорт PDF](ourplancore-pdf.md) - ручной экспорт из окна
- [Процесс работы](../start/workflow.md) - приём и сдача
