# AGENTS.md — Operating Manual for Estimating Knowledge Base

Этот файл — инструкция для любого агента (Claude Code, Codex или другого),
который будет дорабатывать или поддерживать этот проект. Он уже в контексте на
старте: Codex читает его сам, Claude получает через импорт в `CLAUDE.md`.

---

## 1. Что это за проект

**Estimating Knowledge Base** — рабочая wiki по estimating (takeoff, COM/EWP,
walls/framing/sheathing). Это **шпаргалка для конструктора**: краткие правила,
таблицы, и много схем/картинок.

- **Стек:** [MkDocs](https://www.mkdocs.org/) + [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).
- **Деплой:** a push to `main` does NOT update the site: Actions do not run (last run 2025-10-21, checked 2026-11-06); `gh-pages` is written by `mkdocs gh-deploy`. Publish with `.\tools\deploy.ps1` (strict build + gh-deploy of the working tree; dirty tree or divergence from origin: lesson `kb-main-diverged-publish-origin`). Check: a `Deployed <sha>` commit on `gh-pages`.
- **Прод-URL:** https://artrmiys.github.io/knowledge-base/
- **Репо:** repository URL
- **Источник контента:** Obsidian-vault `C:\Users\User\Documents\0.Obsidian` + Tilda + Trello + локальные правки.

---

## 2. Команды

Все команды запускать **из корня проекта** (`current repo root`).
Используется локальный venv `.venv`.

```powershell
# Чистый билд (используй для проверки перед коммитом)
.\.venv\Scripts\python.exe -m mkdocs build --strict

# Локальный preview (живой reload)
.\.venv\Scripts\python.exe -m mkdocs serve -a 127.0.0.1:8000
```

Локальный URL — **`http://127.0.0.1:8000/`**. `site_url` сейчас не задан в `mkdocs.yml`, чтобы не хранить branded project-page path в публичном тексте.

Зависимости (если venv удалён):

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -U mkdocs mkdocs-material mkdocs-material-extensions
```

---

## 3. Структура файлов

Канон правил `AGENTS.md` (`CLAUDE.md` = импорт), контент сайта в `docs/` (`start/`, `work/`, `work-types/`,
`reference/`, `assets/images/`, токены `assets/stylesheets/tokens.css`, компоненты `extra.css`), конфиг
`mkdocs.yml`, конвертеры в `tools/`, история решений `AGENT_NOTES.md`. Полное дерево: `AGENTS_REFERENCE.md` §3.

**Никогда не коммить:** `site/`, `.venv/`, `mkdocs-serve*.log`, `_scratch_workbooks/`,
`imports/`, личные `.env`, `twist-*`/`probe-twist-*` снапшоты. Полный список — в `.gitignore`.

---

## 4. Навигация

Навигация задаётся **строго в [mkdocs.yml](mkdocs.yml) → `nav:`**. Обычные «авто-навигации» не используются — порядок и группировка важны.

### Топ-уровень (табы)

Главная, Старт, OurPlanCore, OurPDF, Работа, Excel и DFL, Справочник. Что внутри каждого таба:
`AGENTS_REFERENCE.md` §4 (открыть перед правкой `nav`).

Каноны программы и правила проверки версии перечислены в
[maintenance](docs/start/maintenance.md). Текущий аудит и постраничная глубина
проверки — [AUDIT.md](AUDIT.md) и [DOCUMENT_REGISTER.md](DOCUMENT_REGISTER.md).
Текстовые сценарии OurPlanCore сверены с кодом 3.0.3 на 18.10.2026; кадры `assets/images/ourplancore/v3/` и ролики `assets/images/ourplancore/demo/` сняты на 3.0.2 17.10.2026 (ролики вставляются разметкой `video.kb-demo`). При следующем релизе
сверяй фактическое поведение и обновляй затронутые сценарии; дату нельзя менять
без проверки. Сохраняй старые URL `reference/ourplanecore/` и
`reference/job-creation-storage/`. Таблица клавиш имеет один канон:
`reference/ourplancore-shortcuts.md`.
Каждая функция программы должна быть описана: после каждого релиза запускай
`python tools/opc_inventory.py --page` (инвентарь из кода и страница
`reference/ourplancore-all-functions.md`) и `python tools/opc_coverage.py`
(код выхода 0 = всё описано). Не найденное дописывай на страницу по теме;
служебное и дубли - в `tools/opc_coverage_ignore.txt` с причиной.

### Правила нейминга в `nav`

- Подписи в меню — преимущественно **русские** для ориентиров (Старт, Работа,
  Справочник, Советы и важные вещи).
- Названия предметных страниц — **английские**, потому что термины приходят
  из чертежей: `Sill Plates`, `Joist`, `Beam`, `Hangers`, `Wall Sheathing`.
- Никаких эмодзи в названиях `nav` (вроде `◼️ Sill Plates`) — иконки только
  внутри страниц через `:material-*:`.

### Скрытые страницы (`not_in_nav`)

Файлы существуют на диске, но не показываются в меню:

Скрытые pending-импорты и source-map страницы удалены из рабочей версии. Не
добавляй такие страницы обратно без явной задачи на импорт/аудит источников.

---

## 5. Двуязычие — правило

- **Термины из чертежей — английские.** «Joist», «Rim Board», «Sheathing»,
  «FRT», «DHU», «ITS». Не переводить.
- **Объяснения — русские.** «Используй ITS, когда…», «Не множь дважды на 1.1…».
- **Заголовки страниц** — обычно EN (термин), но допустимо RU для процессных
  страниц («Workflow», «Quality Checklist», «Советы и важные вещи»).

Файл `docs/start/workflow.md` — пример страницы целиком на русском (это
процессная инструкция). Файл `docs/reference/hangers.md` — пример страницы
с английскими таблицами (это reference). Так и держать.

---

## 6. Material features, которые включены

Тема: зелёный OurCore-скин (урок `kb-theme-green-skin` в памяти knowledge-base); **синий как primary не
возвращать без явной просьбы**; шрифты `Inter` + `JetBrains Mono` через `tokens.css`. В страницах доступны
admonitions, табы, чеклисты, клавиши, иконки `:material-*:`, `attr_list` + `md_in_html`. Полный список
включённого: `AGENTS_REFERENCE.md` §6, канон `mkdocs.yml`.

---

## 7. Картинки и схемы — везде

Это **шпаргалка конструктора**, поэтому визуал важнее текста. На каждой
предметной странице ожидается хотя бы одна схема.

### Куда класть файлы

Папки по теме: `docs/assets/images/<walls|framing|roof|sheathing|hangers|trims>/` (`AGENTS_REFERENCE.md` §7).

- **Имена:** латиница, нижний регистр, тире. `exterior-2x6-section.png`.
- **Форматы:** PNG/SVG для схем, JPG/WEBP для фото, SVG предпочтительно для линий.
- **Размер:** ужимай до &lt;500 KB. Большие диаграммы можно SVG.
- **Не коммить:** скриншоты с email/UID/паролями/ценами.

### Шаблоны

Готовая разметка — в [docs/start/images-and-schemas.md](docs/start/images-and-schemas.md),
копируй оттуда, не сочиняй заново: одна картинка с подписью (`<figure markdown>`
+ `<figcaption>`), две колонки «текст + схема» (`.kb-split`), галерея
(`.kb-gallery`), большая схема на всю ширину (`.kb-schema-full`).

### Доступные CSS-классы (в [docs/assets/stylesheets/extra.css](docs/assets/stylesheets/extra.css))

Таблица классов (`.kb-hero`, `.kb-gallery`, `.kb-split`, `.kb-schema-full` и др.): `AGENTS_REFERENCE.md` §7.
Material `grid cards` тоже работает.

---

## 8. Конвенции страниц

### Заголовок и структура

- В каждом MD-файле — `#` H1 в самом начале (без frontmatter, кроме главной).
- Дальше `## H2`-секции: `Count`, `Check`, `Notes`, `Rules`, `Examples`.
- В конце — `## See also` со ссылками на смежные страницы (когда уместно).
- Главная скрывает sidebar/toc через frontmatter:
  ```yaml
  ---
  hide:
    - navigation
    - toc
  ---
  ```

### Тон

- Короткие bullet'ы и таблицы. Длинные параграфы — только в Workflow / How to use.
- Ссылки между страницами — **относительные**: `[Hangers](../reference/hangers.md)`, не абсолютные.
- Один смысл — одна страница. Если правило живёт в двух местах, держи короткую
  версию на topic page и полную в reference.

### Что недопустимо

- Прямое цитирование email, UID, цен, salary history, личных Dropbox-ссылок,
  Twist/ChatGPT private links, SSH/IP/credentials. Полный список — в `IMPORT_SOURCES.md`.
- Эмодзи в навигации.
- Дубли страниц по одной теме.
- Значки, которые выдают текст модели (просьба владельца 17.10.2026): длинное
  и среднее тире `—` `–`, стрелки `→` `←` `⇒` `↔`, точка-разделитель `·`,
  ёлочки `« »`. Вместо тире и стрелки ставь обычный дефис `-` или слово
  («идёт в», «потом»), кавычки прямые. Касается страниц, nav, подписей и
  текста внутри SVG. Проверка: `python tools/check_symbols.py`.

---

## 9. Импорт из внешних источников

Полный playbook — [IMPORT_SOURCES.md](IMPORT_SOURCES.md). Кратко:

Источники Tilda, Trello, Confluence, Obsidian и чем их брать: `AGENTS_REFERENCE.md` §9.

**Trello/Confluence без авторизации не отдадут содержимое** — попытки скрейпа
HTML вернут только JS-shell или 401. Не делай вид, что что-то импортировал —
если данных нет, фиксируй это в рабочей заметке импорта, а не в публичных
страницах сайта.

Конвертер Trello: команда в `AGENTS_REFERENCE.md` §9. Результат не идёт сразу в `docs/`. Сначала ревью в `imports/`, потом ручной
перенос только полезных правил в нужную topic page.

---

## 10. Деплой

CI [.github/workflows/deploy.yml](.github/workflows/deploy.yml) does not run on push now (see "Деплой" at the top). Order: commit, `git push origin main` (history), then `.\tools\deploy.ps1` (publication); the site updates in about a minute, check the `Deployed <sha>` commit on `gh-pages`. A push that changes only files outside `docs/` (AGENTS.md and the like) needs no publication.

⚠️ Никогда **не пушь без `mkdocs build --strict`** локально. Строгий билд ловит
broken links и опечатки в путях.

---

## 11. Чек-лист перед коммитом

- [ ] `.\.venv\Scripts\python.exe -m mkdocs build --strict` — без warnings/errors.
- [ ] Локальный preview — `http://127.0.0.1:8000/` — проверить визуально.
- [ ] В диффе нет `.venv`, `site/`, логов serve.
- [ ] Нет приватных данных (email/UID/credentials).
- [ ] `mkdocs.yml`'s `nav:` — новая страница добавлена в меню или в `not_in_nav`.

---

## 12. История важных решений и handoff

Вынесены в [AGENT_NOTES.md](AGENT_NOTES.md). Открой его **перед** правкой
дизайна, переименованием страниц, перемещением файлов и перед возобновлением
импорта: там записано, что уже откатывали и почему (overlay-фон, имя «Советы и
важные вещи», раскладка Sheathing по папкам, скрытый `Duplicate of Gable`,
карточная главная).

---

## 13. Тонкости / known issues

1. **`site_url` сейчас не задан.** Локальный preview живёт на `/`. Не возвращай branded project-page prefix без явной просьбы.
2-5. Справка: предупреждение Material про MkDocs 2.0, старый `animation.gif` в истории git (тяжёлые медиа только
   сжатыми или через LFS), поиск `en` + `ru`, иконки через `pymdownx.emoji`: `AGENTS_REFERENCE.md` §13.
6. **Канон мануала — этот `AGENTS.md`.** `CLAUDE.md` содержит только импорт
   `@AGENTS.md`. `.github/AGENTS.md` — старая упрощённая копия (в ней
   устаревшая палитра `accent: lime` вместо green): не считай её авторитетной,
   синхронизируй только по запросу.
7. **`font: false` в теме.** Material НЕ грузит Google Fonts. Шрифты `Inter` +
   `JetBrains Mono` приходят через `@import` в `tokens.css`. Не включай
   `theme.font` обратно — будет дубль загрузки.
8-9. Клик-зум картинок (`docs/assets/js/zoom.js`) и переопределённый `overrides/partials/source.html` (сверять с
   апстримом после апгрейда Material): `AGENTS_REFERENCE.md` §13.

---

## 14. Когда сомневаешься — спрашивай

Этот wiki — рабочий инструмент конкретного человека. Любые перестановки
больших разделов, переименования, удаления страниц или изменения дизайна —
**подтверждай у пользователя до того, как делать**. Особенно:

- Удаление файлов или массовый refactor навигации.
- Изменение цветов / шрифтов / hero-блока.
- Публичный пуш в GitHub (Actions автоматически задеплоит).
- Добавление новых плагинов MkDocs (нужно править `deploy.yml`).

Мелкие правки контента, добавление страниц, фиксы опечаток — можно делать
без подтверждения, но **обязательно** с финальным `mkdocs build --strict`.
