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
- **Деплой:** workflow в [.github/workflows/deploy.yml](.github/workflows/deploy.yml) настроен на push в `main` и ручной запуск; успешную публикацию проверять отдельно.
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

```
project-root/
├── AGENTS.md                  ← этот файл, канон правил для Claude и Codex
├── CLAUDE.md                  ← одна строка-импорт `@AGENTS.md`, не дополнять
├── AGENT_NOTES.md             ← история решений и handoff (на старте не грузится, см. §12)
├── README.md                  ← короткое описание для людей
├── CHANGELOG.md               ← журнал изменений сайта (коммиты `docs(changelog)`)
├── AUDIT.md                   ← рабочий аудит контента/структуры
├── DESIGN_SYSTEM.md           ← заметки по дизайн-системе (токены, OurCore-скин)
├── .github/AGENTS.md          ← СТАРАЯ упрощённая копия этого файла (см. §13.6)
├── IMPORT_SOURCES.md          ← playbook по импорту из Trello/Confluence/Tilda
├── mkdocs.yml                 ← КОНФИГ САЙТА (тема, плагины, навигация)
├── .github/workflows/deploy.yml
├── overrides/                 ← custom_dir темы Material
│   └── partials/source.html   ← переопределённый partial (repo-ссылка в шапке)
├── tools/
│   └── trello_json_to_markdown.py   ← конвертер Trello JSON → MD
├── docs/                      ← КОНТЕНТ САЙТА
│   ├── index.md               ← главная (hero + маршруты по задачам)
│   ├── assets/
│   │   ├── images/            ← все картинки и схемы (см. раздел 7)
│   │   ├── js/zoom.js         ← клик-зум картинок (подключён в extra_javascript)
│   │   └── stylesheets/
│   │       ├── tokens.css     ← ИСТОЧНИК ПРАВДЫ для токенов (--ds-*, --md-*, шрифты)
│   │       └── extra.css      ← компоненты (.kb-hero, .kb-gallery, .kb-split, ...)
│   ├── start/                 ← Workflow, QA, takeoff tool, Client Rules, ...
│   ├── work/                  ← Walls, Framing, Sheathing, SQFTs, Trims
│   ├── work-types/            ← COM, EWP/Capital, Residential
│   └── reference/             ← Советы, Hangers, Formulas, Source Map
├── site/                      ← БИЛД (в .gitignore)
└── .venv/                     ← venv (в .gitignore)
```

**Никогда не коммить:** `site/`, `.venv/`, `mkdocs-serve*.log`, `_scratch_workbooks/`,
`imports/`, личные `.env`, `twist-*`/`probe-twist-*` снапшоты. Полный список — в `.gitignore`.

---

## 4. Навигация

Навигация задаётся **строго в [mkdocs.yml](mkdocs.yml) → `nav:`**. Обычные «авто-навигации» не используются — порядок и группировка важны.

### Топ-уровень (табы)

1. **Главная** — `index.md`
2. **Старт** — процесс, чек-листы, как пользоваться
3. **OurPlanCore** - хаб 3.0 и три уровня: "Каждый день", "Продвинутое", "Идеи и планы", плюс "Справка" (клавиши, проблемы, что нового)
4. **Работа** - типы работ, walls, framing, sheathing, SQFTs, trims; меню не сворачивать (см. AGENT_NOTES)
5. **Excel и DFL** - книга DFL, подписи строк, ноты, блоки, макросы, формулы
6. **Справочник** - советы, hangers, catalogs, термины; подраздел «Редактору KB»

Каноны программы и правила проверки версии перечислены в
[maintenance](docs/start/maintenance.md). Текущий аудит и постраничная глубина
проверки — [AUDIT.md](AUDIT.md) и [DOCUMENT_REGISTER.md](DOCUMENT_REGISTER.md).
Описание OurPlanCore сверено с 3.0.0 на 17.10.2026 (кадры `assets/images/ourplancore/v3/`). При следующем релизе
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

В `mkdocs.yml` уже подключены:

### Темы и режимы

- **Light + Dark** с авто-переключением и тоггл-кнопкой в шапке. Обе темы —
  первоклассные (dark-first по духу дизайн-кода).
- **OurCore-скин на структуре Design Code v0.2, но акцент — ЗЕЛЁНЫЙ** (по явному
  выбору пользователя: «зелёный было круто»). Закон цвета: **green
  `#1f9e38`(light)/`#2ad24b`(dark) = бренд/active/ссылка/selected/primary**;
  тёмно-зелёный (`#2e7d32`/`#56e070`) = узкий brand-маркер (1.5-px полоска под
  активной вкладкой, left-border активного пункта nav/TOC, маркеры списков,
  tip-callout). Статусы ok/warn/err. От v0.2 сохранены: плотность, ink-поверхности
  light+dark, callout-admonitions, скругления 6/8/12/16, нейтральная шапка.
  Декоративные `kb-st--*`/`kb-mk--*` → green/warn. Источник правды —
  `tokens.css` (`--ds-*` + Material `--md-*`), компоненты — `extra.css`. SVG-схемы
  используют accent `#2e7d32`. **Зелёный — основной; синий как primary не
  возвращать без явной просьбы.**
- Шрифты `Inter` (текст) + `JetBrains Mono` (код/числа), грузятся `@import` в
  `tokens.css`. Цифры — моно, tabular.
- Логотип/favicon — KB-глиф `assets/images/brand/icon-kb-128.png`.
- Иконка GitHub в шапке + edit-кнопка на каждой странице (`edit_uri`).

### Навигация, поиск, Markdown extensions

Канон списка — `theme.features`, `plugins.search` и `markdown_extensions` в
`mkdocs.yml`; здесь только то, чем пользоваться.

- Навигация: табы сверху (sticky), заголовки разделов и section-index в
  сайдбаре, кнопка «вверх», стрелки prev/next в подвале.
- Поиск: подсказки, подсветка, share; языки индекса `en` + `ru`.
- В страницах работает: `!!! note "Заголовок"`, сворачиваемый `??? tip`,
  табы `=== "Tab 1"`, чеклисты `- [x]`, клавиши `++ctrl+s++`, `^^ins^^`,
  `==mark==`, `~~strike~~`, иконки `:material-wall:` /
  `:octicons-arrow-right-24:` / `:fontawesome-brands-github:`, вложенные
  code/admonition, подсветка кода, классы и HTML-блоки (`attr_list` +
  `md_in_html`), таблицы, `def_list`, сноски, `abbr`.

---

## 7. Картинки и схемы — везде

Это **шпаргалка конструктора**, поэтому визуал важнее текста. На каждой
предметной странице ожидается хотя бы одна схема.

### Куда класть файлы

```
docs/assets/images/
├── walls/
├── framing/
├── roof/
├── sheathing/
├── hangers/
└── trims/
```

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

| Класс | Что |
| --- | --- |
| `.kb-hero` | Большой баннер главной (gradient + кнопки) |
| `.kb-hero__btn`, `.kb-hero__btn--primary`, `.kb-hero__btn--ghost` | Кнопки в hero |
| `.kb-section-title` | Заголовок секции на главной (с горизонтальной линией) |
| `.kb-gallery` + `.kb-gallery__item` | Сетка миниатюр (контент или плейсхолдеры) |
| `.kb-gallery__item--placeholder` | Пунктирная карточка-заглушка |
| `.kb-gallery__caption` | Подпись под миниатюрой |
| `.kb-split` | Двухколоночный layout (text + schema), на мобиле в один столбец |
| `.kb-schema-full` | Картинка на всю ширину контента, с тенью |

Material's native `grid cards` (`<div class="grid cards" markdown>...`) тоже
работает — для главной и section-pages с большими карточками.

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

| Источник | Что нужно | Инструмент |
| --- | --- | --- |
| **Tilda** (public) | URL | `WebFetch` (через Claude) или ручной просмотр |
| **Trello** | JSON export или API token | `tools/trello_json_to_markdown.py` |
| **Confluence** | Space export HTML/XML или API token | конвертер на запрос |
| **Obsidian** | локальный путь | прямое чтение из `C:\Users\User\Documents\0.Obsidian` |

**Trello/Confluence без авторизации не отдадут содержимое** — попытки скрейпа
HTML вернут только JS-shell или 401. Не делай вид, что что-то импортировал —
если данных нет, фиксируй это в рабочей заметке импорта, а не в публичных
страницах сайта.

### Запуск конвертера Trello

```powershell
.\.venv\Scripts\python.exe tools\trello_json_to_markdown.py `
  --input C:\path\to\board.json `
  --output imports\trello
```

Результат не идёт сразу в `docs/`. Сначала ревью в `imports/`, потом ручной
перенос только полезных правил в нужную topic page.

---

## 10. Деплой

CI: [.github/workflows/deploy.yml](.github/workflows/deploy.yml)

```yaml
on: push (branches: [main])
- pip install mkdocs mkdocs-material mkdocs-material-extensions
- mkdocs gh-deploy --force --clean --remote-branch gh-pages
```

Ничего вручную пушить на gh-pages не надо. Просто `git push origin main` — Actions сам соберёт и задеплоит. Через ~1 минуту прод обновится.

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
2. **Material's marketing warning.** При каждом билде печатается длинный блок
   про MkDocs 2.0 — это маркетинг от squidfunk, к проекту отношения не имеет.
   Игнорируй.
3. **Большой `animation.gif` (18 МБ)** удалён из рабочей версии, но всё ещё
   может быть в git history. Не добавляй тяжёлые медиа без LFS или сжатия.
4. **Поиск на русском работает за счёт `plugins.search.lang: [en, ru]`.**
   Если нужно сербский/немецкий — добавлять туда же.
5. **Иконки `:material-*:` требуют `pymdownx.emoji` с Material extension.**
   Уже подключено. Если случайно удалить из `mkdocs.yml`, иконки превратятся
   в текст.
6. **Канон мануала — этот `AGENTS.md`.** `CLAUDE.md` содержит только импорт
   `@AGENTS.md`. `.github/AGENTS.md` — старая упрощённая копия (в ней
   устаревшая палитра `accent: lime` вместо green): не считай её авторитетной,
   синхронизируй только по запросу.
7. **`font: false` в теме.** Material НЕ грузит Google Fonts. Шрифты `Inter` +
   `JetBrains Mono` приходят через `@import` в `tokens.css`. Не включай
   `theme.font` обратно — будет дубль загрузки.
8. **Клик-зум картинок** — кастомный `docs/assets/js/zoom.js`, подключён через
   `extra_javascript`. Не плагин. Если зум сломался — смотри туда, не в mkdocs.yml.
9. **`overrides/partials/source.html`** переопределяет partial Material
   (`custom_dir: overrides`). После апгрейда `mkdocs-material` сверяй его с
   апстримом — изменённый upstream-partial может разойтись.

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
