# CLAUDE.md — Operating Manual for Estimating Knowledge Base

Этот файл — инструкция для любого агента (Claude Code или другого), который
будет дорабатывать или поддерживать этот проект. Прочитай его в начале каждой
сессии до того, как трогать `docs/`, `mkdocs.yml` или CSS.

---

## 1. Что это за проект

**Estimating Knowledge Base** — рабочая wiki по estimating (takeoff, COM/EWP,
walls/framing/sheathing). Это **шпаргалка для конструктора**: краткие правила,
таблицы, и много схем/картинок.

- **Стек:** [MkDocs](https://www.mkdocs.org/) + [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).
- **Деплой:** GitHub Pages (workflow в [.github/workflows/deploy.yml](.github/workflows/deploy.yml)) при каждом push в `main`.
- **Прод-URL:** https://artrmiys.github.io/knowledge-base/
- **Репо:** https://github.com/artrmiys/knowledge-base
- **Источник контента:** Obsidian-vault `C:\Users\User\Documents\0.Obsidian` + Tilda + Trello + локальные правки.

---

## 2. Команды

Все команды запускать **из корня проекта** (текущий checkout).
Используется локальный venv `.venv`.

```powershell
# Чистый билд (используй для проверки перед коммитом)
.\.venv\Scripts\python.exe -m mkdocs build --strict

# Локальный preview (живой reload)
.\.venv\Scripts\python.exe -m mkdocs serve -a 127.0.0.1:8000
```

⚠️ Локальный URL — **`http://127.0.0.1:8000/`**.
`site_url` в `mkdocs.yml` не задан, поэтому preview открывается без project-page
префикса.

Зависимости (если venv удалён):

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -U mkdocs mkdocs-material mkdocs-material-extensions
```

---

## 3. Структура файлов

```
knowledge-base/
├── CLAUDE.md                  ← этот файл
├── README.md                  ← короткое описание для людей
├── IMPORT_SOURCES.md          ← playbook по импорту из Trello/Confluence/Tilda
├── mkdocs.yml                 ← КОНФИГ САЙТА (тема, плагины, навигация)
├── .github/workflows/deploy.yml
├── tools/
│   └── trello_json_to_markdown.py   ← конвертер Trello JSON → MD
├── docs/                      ← КОНТЕНТ САЙТА
│   ├── index.md               ← главная (hero + grid cards + galery)
│   ├── assets/
│   │   ├── images/            ← все картинки и схемы (см. раздел 7)
│   │   └── stylesheets/extra.css
│   ├── start/                 ← Workflow, QA, takeoff tool, Client Rules, ...
│   ├── work/                  ← Walls, Framing, Sheathing, SQFTs, Trims
│   ├── work-types/            ← COM, EWP/Capital, Residential
│   └── reference/             ← Советы, Hangers, Formulas, Source Map
├── site/                      ← БИЛД (в .gitignore)
└── .venv/                     ← venv (в .gitignore)
```

**Никогда не коммить:** `site/`, `.venv/`, `mkdocs-serve*.log`, личные `.env`.

---

## 4. Навигация

Навигация задаётся **строго в [mkdocs.yml](mkdocs.yml) → `nav:`**. Обычные «авто-навигации» не используются — порядок и группировка важны.

### Топ-уровень (табы)

1. **Главная** — `index.md`
2. **Старт** — процесс, чек-листы, как пользоваться
3. **Работа** — основное: типы работ, walls, framing, sheathing, SQFTs, trims
4. **Справочник** — советы, hangers, formulas, sources

### Правила нейминга в `nav`

- Подписи в меню — преимущественно **русские** для ориентиров (Старт, Работа,
  Справочник, Советы и важные вещи).
- Названия предметных страниц — **английские**, потому что термины приходят
  из чертежей: `Sill Plates`, `Joist`, `Beam`, `Hangers`, `Wall Sheathing`.
- Никаких эмодзи в названиях `nav` (вроде `◼️ Sill Plates`) — иконки только
  внутри страниц через `:material-*:`.

### Скрытые страницы (`not_in_nav`)

Файлы существуют на диске, но не показываются в меню:

```yaml
not_in_nav: |
  /work/vertical/sheathing/duplicate-of-gable.md
  /work/interior-trims/trello-import-pending.md
  /start/important-changes.md
```

Используй это для pending-импортов и техдолга, чтобы они не позорили публичный сайт.

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

- **Light + Dark** с авто-переключением и тоггл-кнопкой в шапке.
- Зелёная палитра (primary `green`, accent `lime`).
- Шрифты `Inter` (текст) + `JetBrains Mono` (код).
- Иконка GitHub в шапке + edit-кнопка на каждой странице (`edit_uri`).

### Навигация

- `navigation.tabs` + `navigation.tabs.sticky` — табы сверху.
- `navigation.sections` — заголовки разделов в сайдбаре.
- `navigation.indexes` — поддерживается section-index page.
- `navigation.top` — кнопка «вверх».
- `navigation.footer` — стрелки prev/next в подвале.

### Поиск

- `search.suggest` + `search.highlight` + `search.share`.
- Языки индекса: `en` + `ru`.

### Markdown extensions

| Расширение | Использование |
| --- | --- |
| `admonition` | `!!! note "Заголовок"` блоки |
| `pymdownx.details` | `??? tip` сворачиваемые блоки |
| `pymdownx.superfences` | вложенные code/admonition |
| `pymdownx.tabbed` | `=== "Tab 1"` табы |
| `pymdownx.tasklist` | `- [x]` чеклисты |
| `pymdownx.highlight` + `inlinehilite` | подсветка кода |
| `pymdownx.keys` | `++ctrl+s++` → клавиши |
| `pymdownx.caret/mark/tilde` | `^^ins^^`, `==mark==`, `~~strike~~` |
| `pymdownx.emoji` (material) | `:material-wall:`, `:octicons-arrow-right-24:`, `:fontawesome-brands-github:` |
| `attr_list` + `md_in_html` | классы и HTML-блоки внутри markdown |
| `tables`, `def_list`, `footnotes`, `abbr` | базовые штуки |

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

### Шаблоны (полный гайд — [docs/start/images-and-schemas.md](docs/start/images-and-schemas.md))

**Одна картинка с подписью:**

```markdown
<figure markdown>
  ![Wall section](../assets/images/walls/exterior-2x6.png)
  <figcaption>Exterior 2×6 wall — typical section</figcaption>
</figure>
```

**Две колонки «текст + схема»:**

```html
<div class="kb-split" markdown>

Текст / правила слева.

<figure markdown>
  ![alt](../assets/images/...)
  <figcaption>Подпись.</figcaption>
</figure>

</div>
```

**Галерея:**

```html
<div class="kb-gallery">
  <a class="kb-gallery__item" href="../assets/images/walls/exterior.png">
    <img src="../assets/images/walls/exterior.png" alt="Exterior">
    <div class="kb-gallery__caption">Exterior wall</div>
  </a>
</div>
```

**Большая схема на всю ширину:**

```html
<div class="kb-schema-full">
  ![alt](../assets/images/...)
</div>
```

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
  Twist/ChatGPT private links, SSH/IP/credentials. Полный список — в `IMPORT_SOURCES.md` и `docs/reference/source-map.md`.
- Эмодзи в навигации.
- Дубли страниц по одной теме (см. историю с `gable` walls / sheathing /
  `duplicate-of-gable`).

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
если данных нет, фиксируй это в `docs/reference/source-map.md` и добавь
страницу в `not_in_nav` пока она пустая.

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
- [ ] `docs/reference/source-map.md` обновлён, если добавлен новый источник.
- [ ] `mkdocs.yml`'s `nav:` — новая страница добавлена в меню или в `not_in_nav`.

---

## 12. История важных решений

- **Дизайн откатывался дважды.** Прежний агент сделал тяжёлый синий overlay
  с blur'ом, контент был нечитаем. Текущий стиль — чистый Material с
  light/dark и аккуратным hero на главной. Не возвращай overlay-фон body
  без явной просьбы.
- **«Boss Feedback Rules» переименован в «Советы и важные вещи».** Файл
  оставлен как `reference/boss-feedback-rules.md` для стабильности URL.
  Всегда используй новое русское имя в навигации и текстах.
- **Sheathing раньше был размазан по 4 папкам.** Сейчас собран в одну
  секцию `Работа → Sheathing` в `mkdocs.yml`, но физические файлы остались
  в исторических папках (`work/vertical/sheathing/`, `work/horizontal/...`).
  При перемещении файлов будь осторожен — обновляй ссылки.
- **`Duplicate of Gable`** оставлен на диске, но скрыт через `not_in_nav` —
  это артефакт старого takeoff-дерева, выбрасывать пока не стали.
- **Главная — карточная**, с галереей-заглушками под будущие схемы. Картинки
  ожидаются на каждой предметной странице.

---

## 13. Тонкости / known issues

1. **`site_url` сейчас не задан.** Локальный preview живёт на
   `http://127.0.0.1:8000/`, а прод — на GitHub Pages project URL.
2. **Material's marketing warning.** При каждом билде печатается длинный блок
   про MkDocs 2.0 — это маркетинг от squidfunk, к проекту отношения не имеет.
   Игнорируй.
3. **Большой `animation.gif` (18 МБ)** уже в git history. Не добавляй больше
   тяжёлых медиа без LFS или сжатия. Однажды нужно будет почистить историю
   или перейти на Git LFS.
4. **Поиск на русском работает за счёт `plugins.search.lang: [en, ru]`.**
   Если нужно сербский/немецкий — добавлять туда же.
5. **Иконки `:material-*:` требуют `pymdownx.emoji` с Material extension.**
   Уже подключено. Если случайно удалить из `mkdocs.yml`, иконки превратятся
   в текст.

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
