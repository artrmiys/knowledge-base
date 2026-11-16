# Workspace: второй компьютер

!!! info "Только в полной версии"
    В OurPlanCore Lite нет Workspace: ни раздела `Settings > Workspace`, ни фоновой синхронизации. Проект в Lite передают копией сохранённого файла `.ourplan` ([Проекты и сохранение](job-creation-storage.md#file)). Чем версии отличаются: [Lite и полная версия](ourplancore-lite.md).

Здесь - общее рабочее пространство полной версии: частный сервер, второй компьютер, общие проекты, пресеты и беседы ассистентов. Нужно при работе с ноутбука. Импорт одного проекта в другой описан в [Проекты и сохранение](job-creation-storage.md#import-project), консоль конвейера `OurPlanCoreCli` - [там же](job-creation-storage.md#cli), список модулей - в [Settings, Modules](ourplancore-settings.md#modules), кнопка Job Tracker - в [Менеджеры](ourplancore-managers.md#job-tracker).

## Workspace: общее рабочее пространство {#workspace}

Скриншота этого раздела нет намеренно: на нём всегда видны адрес сервера, имя компьютера и названия рабочих проектов.

**Что это.** Частный сервер хранит общие правила и заметки, скилы агентов, пресеты настроек, выбранные сохранённые проекты и архивы диалогов Claude и Codex. Программа работает локально и синхронизируется в фоне; редактирование плана и терминал сервера не ждут. Локальная папка по умолчанию `Documents\OurPlanCore Workspace`; внутри `knowledge`, `skills`, `profile`, `projects`, `conversations` и `runtime` (рабочая проекция для ассистентов).

| Группа в `Settings > Workspace` | Кнопки и поля |
| --- | --- |
| This computer | `Use shared workspace`, имя устройства, `Local workspace folder`, `Automatic synchronization` с интервалом, категории (`Claude / Codex skills and supporting scripts`, `Shared conversation archives`), `Save`, `Sync now`, `Import this setup`, `Open local folder`, `Server status` |
| Workspace server | адрес сервера (хранится на каждом устройстве отдельно) |
| Connect another computer | `Create code for another computer` (одноразовый код на 10 минут), `Connect this computer` |
| Projects | `Share current saved project`, `Open selected`, `Review conflicts`, `Apply shared presets` |
| Conversations | `Continue selected`, `Setup on this computer`, `Import a Claude / Codex conversation` |

### Как подключить второй компьютер { #second-pc }

Зачем: продолжить тот же проект с ноутбука с теми же правилами и беседами ассистентов.
Нужно: программа установлена на обоих компьютерах; адрес сервера известен.

1. На основном откройте **Settings > Workspace**, поставьте **Use shared workspace**, подключите устройство и нажмите **Import this setup** (исходные папки не меняются).
2. Нажмите **Share current saved project** для нужного `.ourplan`: пакет уходит на сервер, следующие сохранения синхронизируются сами.
3. На втором впишите в **Settings > Workspace** адрес сервера и код из **Create code for another computer**, нажмите **Connect this computer**. Правила и скилы скачаются; проекты и диалоги - по запросу.
4. Нажмите **Projects > Open selected**: общий проект открыт. Для терминалов на новом компьютере нужны Git Bash и вход в CLI ассистента один раз ([консоль ИИ](ourplancore-ai-console.md)).
5. Перед сменой компьютера нажмите ++ctrl+s++, затем **Sync now** и дождитесь статуса Synced.

Результат: оба компьютера видят один проект, пресеты и беседы; статус `Synced` в Settings > Workspace.

### Конфликты и ограничения

- Конфликт сохраняет обе версии: `Review conflicts`, затем `Keep this computer`, `Use server version` или `Open preserved files`.
- Открытый проект серверной версией не заменяется; изменённый локальный файл при скачивании не перезаписывается.
- Удаление между устройствами не распространяется. Кешированные проекты и знания доступны офлайн.
- Общие пресеты применяются только кнопкой `Apply shared presets`; проектные копии настроек остаются сильнее; локальные пресеты перед этим бэкапятся.
- Диалог размером больше 256 MB пропускается с предупреждением, остальные синхронизируются (3.0).
- Ключи, вход в ассистентов и личные папки не импортируются и не синхронизируются.

## Модули { #modules }

Список модулей переехал: [Settings, Modules](ourplancore-settings.md#modules).

## OurPlanCoreCli { #cli }

Консоль конвейера переехала: [Проекты и сохранение, OurPlanCoreCli](job-creation-storage.md#cli).

## См. также

- [Консоль ИИ и терминал](ourplancore-ai-console.md): беседы из панели `>_` и их продолжение на втором компьютере
- [ИИ в программе](ourplancore-ai.md): Agent Bridge
- [Settings: все категории](ourplancore-settings.md)
- [Проекты и сохранение](job-creation-storage.md)
