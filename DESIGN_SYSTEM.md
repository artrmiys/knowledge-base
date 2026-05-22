# OurCore Design System (v1)

Единый визуальный язык для трёх продуктов:

| Продукт | Стек | Тема | Статус |
| --- | --- | --- | --- |
| Knowledge Base | MkDocs Material | светлая + тёмная | ✅ токены + Pay-chrome + лого |
| Pay-дашборд | React + Vite | светлая + тёмная | ✅ токены + ребренд + лого |
| takeoff-app | WPF (desktop) | светлая + тёмная | ✅ иконка L4D |

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

## Лого — семейство «L4D»

Один **glass-каркас**, у каждого продукта свой глиф. Каркас = стопка из 3 матовых
стёкол (glassmorphism) над градиентом синий→тил `#0b2a4a → #0e7490` + blueprint-сетка
в верхнем листе + лаймовый `#c6ff3d` глиф с лёгким glow.

| Продукт | Глиф | Мастер-файл |
| --- | --- | --- |
| takeoff-app | трасса-замер с узлом-таргетом | `ourcore-logos-v2/l4d.svg` |
| Knowledge Base | угол плана (L стен) + пунктирный гайд + линия-замер с узлами | `ourcore-logos-v2/logo-kb-final.svg` |
| Pay | растущие столбцы + трендовая линия с узлами | `ourcore-logos-v2/logo-pay-final.svg` |

- Мастера и preview-`*.html` лежат в `C:\Users\User\Desktop\ourcore-logos-v2\`.
- KB использует свой как `docs/assets/images/logo.svg` (шапка + favicon).
- Pay — как `web/public/logo.svg` (логин/сайдбар/favicon).
- Иконки ярлыков Windows: `C:\Users\User\Desktop\updates\{wiki.ico = KB, pay.ico = Pay}`.
  `wiki.url` (десктоп + updates) и `pay.url` (десктоп) ссылаются на них; `OurPlaneCore.lnk` держит L4D.

---

## Применение по продуктам

### Knowledge Base ✅
- `tokens.css` подключён первым в `extra_css`, `extra.css` маппит `--md-*` на `--ds-*`.
- Шрифты: `font: false` в `mkdocs.yml` + `--md-text-font/-code-font` в CSS.
- **Pay-style chrome:** шапка светлая в light / тёмный titlebar (`#171a22→#0f1117`) в dark
  (не зелёная плашка); фон `.md-main` = радиальное green/blue свечение; glass-карточки
  + мягкие тени; кнопки = soft-green тон + обводка (не неон).
- Деплой: `mkdocs gh-deploy` → gh-pages, + push в main.

### Pay-дашборд ✅
- `tokens.css` вендорится в `web/src/`, импортируется перед `styles.css`.
- Локальные `--bg/--panel/--line/--text/--muted/--accent` маппятся на `--ds-*`.
- Светлая + тёмная тема + переключатель (класс `.theme-dark` на корне).
- Шрифт `Manrope` → системный стек `--ds-font-text`.
- Видимый бренд скрыт (= «My Account», без E-Wood/OurCore).
- Прод: `deploy@185.81.165.121`, `~/e-wood-pay`, `docker compose up -d --build web`.

### takeoff-app ✅ (минимально)
- Заменена только иконка `.ico` → L4D. Палитра/UI оставлены родными по решению пользователя.
- При синхронизации палитры: selection/активное = green; ссылки/info = blue; маркеры — `--ds-mk-*`.
