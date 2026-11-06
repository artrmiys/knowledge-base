# AGENTS_REFERENCE.md - справка к AGENTS.md базы знаний

Блоки перенесены из `AGENTS.md` дословно 2026-11-06, чтобы цепочка правил агентов уложилась в бюджет
(context-care). Правила и запреты остались в `AGENTS.md`; здесь только справка, открывать по ссылке из него.

## 3. Структура файлов: полное дерево

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

## 4. Навигация: топ-уровень (табы)

1. **Главная** — `index.md`
2. **Старт** — процесс, чек-листы, как пользоваться
3. **OurPlanCore** - хаб 3.0 и три уровня: "Каждый день", "Продвинутое", "Идеи и планы", плюс "Справка" (клавиши, проблемы, что нового)
4. **OurPDF** - просмотр и разметка PDF: окно, измерения (главная страница), связь с Excel, комментарии и сохранение, страницы и правка, наложение, кроп, вид и настройки, клавиши, нейросети; сверено с OurPDF 0.9.27
5. **Работа** - типы работ, walls, framing, sheathing, SQFTs, trims; меню не сворачивать (см. AGENT_NOTES)
6. **Excel и DFL** - книга DFL, подписи строк, ноты, блоки, макросы, формулы
7. **Справочник** - советы, hangers, catalogs, термины; подраздел «Редактору KB»

## 6. Material features: темы, навигация, поиск, Markdown extensions

В `mkdocs.yml` уже подключены:

### Темы и режимы

- **Light + Dark** с авто-переключением и тоггл-кнопкой в шапке. Обе темы —
  первоклассные (dark-first по духу дизайн-кода).
- **OurCore-скин (Design Code v0.2), акцент ЗЕЛЁНЫЙ** («зелёный было круто»):
  green `#1f9e38`/`#2ad24b` = primary, тёмно-зелёный `#2e7d32`/`#56e070` = узкие
  brand-маркеры, SVG accent `#2e7d32`. Источник правды `tokens.css`, компоненты
  `extra.css`. **Синий как primary не возвращать без явной просьбы.** Полное
  правило: урок `kb-theme-green-skin` в памяти knowledge-base.
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

## 7. Картинки: папки docs/assets/images

```
docs/assets/images/
├── walls/
├── framing/
├── roof/
├── sheathing/
├── hangers/
└── trims/
```

## 7. Доступные CSS-классы (extra.css)

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

## 9. Импорт: источники и инструменты

| Источник | Что нужно | Инструмент |
| --- | --- | --- |
| **Tilda** (public) | URL | `WebFetch` (через Claude) или ручной просмотр |
| **Trello** | JSON export или API token | `tools/trello_json_to_markdown.py` |
| **Confluence** | Space export HTML/XML или API token | конвертер на запрос |
| **Obsidian** | локальный путь | прямое чтение из `C:\Users\User\Documents\0.Obsidian` |

## 9. Запуск конвертера Trello

### Запуск конвертера Trello

```powershell
.\.venv\Scripts\python.exe tools\trello_json_to_markdown.py `
  --input C:\path\to\board.json `
  --output imports\trello
```

## 10. Деплой: шаги CI

```yaml
on: push (branches: [main])
- pip install mkdocs mkdocs-material mkdocs-material-extensions
- mkdocs gh-deploy --force --clean --remote-branch gh-pages
```

## 13. Тонкости 2-5 (справка)

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

## 13. Тонкости 8-9 (справка)

8. **Клик-зум картинок** — кастомный `docs/assets/js/zoom.js`, подключён через
   `extra_javascript`. Не плагин. Если зум сломался — смотри туда, не в mkdocs.yml.
9. **`overrides/partials/source.html`** переопределяет partial Material
   (`custom_dir: overrides`). После апгрейда `mkdocs-material` сверяй его с
   апстримом — изменённый upstream-partial может разойтись.
