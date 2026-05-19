# CHANGELOG

Лог изменений wiki. Сайт деплоится вручную (Actions на паузе):
`.\tools\deploy.ps1` или `mkdocs gh-deploy --force --clean --remote-branch gh-pages`.
Прод: https://artrmiys.github.io/knowledge-base/

## 2026-05-19

### Interior Trims
- `584e888` — Bi-Fold door: добавлена нотация `(2)2680 Bi-Fold` / `9068 Bi-Fold`
  + правила в `work/interior-trims/door-window-trim.md`.

### Exterior Trims — новый раздел (`584e888`)
- `work/exterior-trims/`: overview, exclusions-и-J-Channel,
  casing-corner-band, furring-and-jambs, soffit-fascia,
  porch-deck-balcony, rails-decking, balcony-buildup, shower-pergola,
  macros. EIFS/Stucco/Stone/Brick — by others; furring под siding;
  window jamb 2x4/2x8/2x10 P.T.
- Reference: `material-catalog.md`, `standard-notes.md` (~700 notes),
  `takeoff-items.md` (словарь Label'ов). Источник — макро-воркбуки.

### Siding — новый раздел (`f2fedb0`)
- `work/siding/`: overview, types, underlayment, eifs-stucco-veneer,
  measure. Отдельно от Exterior Trims; полный EIFS/Stucco/Veneer + J-Channel.

### Чистка репо (`7755f71`)
- Удалены import-era страницы (source-map/confluence/trello/tilda/pending),
  ~19 одноразовых import/audit-скриптов, `CURRENT_SESSION.md`.
- Обновлены CLAUDE.md / AGENTS.md / IMPORT_SOURCES.md; добавлены
  preview-хелперы. Публичная вики без import-мусора.

### Deck/Porch/Balcony Frame (`975117c`)
- Структурный каркас вынесен в `work/deck/deck-porch-balcony-frame.md`;
  `balcony-buildup.md` теперь finish/trim-only. Кросс-линки с Floor Framing.
- `excel-hotkeys.md`: A-series calc pipeline, новые insert-хелперы,
  section-navigation (Ctrl/Alt/Alt+Shift + F).
- `ourplanecore.md` расширен: архитектура, 8 Settings, disk-модель, сборка.

### OurPlaneCore — полный гайд (`819cf66` … `f66a595`)
- Новый `reference/ourplanecore-guide.md`: каждый таб/кнопка/ползунок +
  процесс от и до + горячие клавиши.
- Скриншоты сняты на job 76 (через UI Automation), нарезаны на фрагменты
  и встроены **инлайн** у соответствующих разделов.
- Зафиксирован баг рендера: markdown-картинки внутри `<details>` без
  `markdown`-атрибута не парсятся md_in_html → использовать top-level
  `<figure markdown>` или raw-HTML `kb-figure-grid`.

### Известные хвосты
- Прод-скриншоты OurPlaneCore сняты с реального job (видны имена
  клиента/листов) — опубликовано по явному запросу пользователя.
- OurPlaneCore-приложение: `LastJobPath` в `%APPDATA%\OurPlaneCore\
  settings.json` переключён на job 76; вернуть на 81 при необходимости.
