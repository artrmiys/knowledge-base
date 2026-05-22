# OurCore Design System (v1)

Единый визуальный язык для трёх продуктов:

| Продукт | Стек | Тема | Статус |
| --- | --- | --- | --- |
| Knowledge Base | MkDocs Material | светлая + тёмная | ✅ переведён на токены |
| Pay-дашборд | React + Vite | тёмная (нужна светлая) | ⏳ план |
| takeoff-app | WPF (desktop) | светлая + тёмная | ⏳ план |

> Внутреннее имя системы — **OurCore**. На видимых частях UI бренд «E-Wood» не
> используется (в коде/комментариях — допустимо).

---

## Принципы

- 🟢 **green** = действие / бренд / активное состояние / success
- 🔵 **blue** = ссылки / info / выделение (selection)
- **Шрифт** — системный **Segoe UI** (как в takeoff-app), числа/код — **Consolas**
- **Форма** — единый радиус `12px` и единый набор теней
- **Светлая И тёмная** тема — обе первоклассные во всех продуктах

---

## Токены

Канонический источник — [`docs/assets/stylesheets/tokens.css`](docs/assets/stylesheets/tokens.css).
Все переменные имеют префикс `--ds-*`. Другие продукты **копируют** этот файл
(вендорят) и маппят свои локальные переменные на `--ds-*`.

### Бренд

| Токен | Значение | Роль |
| --- | --- | --- |
| `--ds-green` | `#2ad24b` | акцент действия (яркий, для тёмного фона) |
| `--ds-green-dark` | `#1f9e38` | читаемый зелёный на белом (текст/шапка) |
| `--ds-green-darker` | `#18802d` | hover/нажатие |
| `--ds-blue` | `#2563eb` | ссылки / info / выделение |
| `--ds-blue-dark` | `#1d4ed8` | blue на светлом фоне |
| `--ds-blue-light` | `#5ba8e8` | blue на тёмном фоне |

### Статусы

`--ds-success #1e7e34` · `--ds-warning #c68a00` · `--ds-danger #c62828` · `--ds-info = blue`

### Маркеры takeoff (канвас takeoff-app)

`--ds-mk-line #1a5ba8` · `--ds-mk-area #6a4fb6` · `--ds-mk-joist #1b7a60` · `--ds-mk-count #b83276`

### Форма

| Токен | Значение |
| --- | --- |
| `--ds-radius` | `12px` (контейнеры, кнопки, таблицы, инпуты) |
| `--ds-radius-sm` | `4px` (inline-код, kbd, чипы) |
| `--ds-radius-pill` | `999px` |
| `--ds-shadow-sm/md/lg` | единая шкала теней |

### Типографика

```
--ds-font-text: "Segoe UI", system-ui, -apple-system, "Roboto", Arial, sans-serif;
--ds-font-mono: "Consolas", "JetBrains Mono", ui-monospace, monospace;
```

### Нейтральная рампа

Светлая (`:root`) и тёмная (`[data-md-color-scheme="slate"]`, `.theme-dark`,
`[data-theme="dark"]`) — `--ds-bg`, `--ds-surface`, `--ds-surface-2`,
`--ds-line`, `--ds-text`, `--ds-text-2`, `--ds-text-3`, плюс контекстные
`--ds-accent`, `--ds-link` (автоматически меняются по теме).

---

## Применение по продуктам

### Knowledge Base (сделано)
- `tokens.css` подключён первым в `extra_css`, `extra.css` маппит `--md-*` на `--ds-*`.
- Шрифты: `font: false` в `mkdocs.yml` + `--md-text-font/-code-font` в CSS.

### Pay-дашборд (план)
- Скопировать `tokens.css` в `web/src/`, импортировать перед `styles.css`.
- Заменить локальные `--bg/--panel/--line/--text/--muted/--accent` на `--ds-*`.
- Добавить **светлую тему** + переключатель (класс `.theme-dark` на корне).
- Шрифт `Manrope` → системный стек `--ds-font-text`.
- Скрыть видимый бренд «E-Wood».

### takeoff-app (план)
- Вынести цвета в `ResourceDictionary` со значениями из токенов.
- Selection/активное = green; ссылки/info = blue; маркеры — `--ds-mk-*`.
- Тема уже светлая + тёмная — синхронизировать палитру.
