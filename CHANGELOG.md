# CHANGELOG

Лог изменений wiki. Сайт деплоится вручную (Actions на паузе):
`.\tools\deploy.ps1` или `mkdocs gh-deploy --force --clean --remote-branch gh-pages`.
Прод: https://artrmiys.github.io/knowledge-base/

## 2026-05-30

### Reference — ИИ-ассистент и стратегия (новая страница)
- `reference/ai-assist-system.md` + nav. Карта системы предсказание→проверка DFL:
  полная петля (scope → SUGGEST состав → измерение → per-project с PDF → блоки →
  VALIDATE → ingest растит корпус); три операции (**SUGGEST** scope→состав,
  **VALIDATE** 3 уровня: секции/строки/количества, **PDF→spec** crop→AI);
  stable-дефолты vs per-project; roadmap (готово: suggest/validate/pdf→spec/CSI;
  дальше: авто-парсинг legend, validate по спеке, NL→Excel, масштаб 500+).

### Reference — Отраслевые стандарты (новая страница)
- `reference/industry-standards.md` + nav. Позиционирование workflow в индустрии:
  **assemblies** (RSMeans-стиль, per LFT/SQFT — наш DFL = библиотека assemblies),
  **CSI MasterFormat** (Div 06 Wood / 07 Thermal&Moisture / 08 Openings / 09 Finishes —
  Артём уже пишет CSI-коды в E-колонке: `07.04 WD-01`, `05.01`, `07.01 EIFS`),
  best-practices чеклист (waste, group-by-size, risk-flag), AI-takeoff контекст.
  Связь с output-wiki `wiki/E-Wood/` (takeoff-to-dfl, research-positioning, csi-mapping).
  Источник — ресёрч май 2026 + reconciliation формул.

### Дополнения существующих страниц
- `reference/formulas.md` — blocking factor по типу (flat 2 / diagonal 2.5 /
  vertical 1.5–2) + блок «контрольные диапазоны количеств» (sanity-check от VALIDATE).
- `start/quality-checklist.md` — секция «Авто-проверка (ИИ-дубль)»: VALIDATE как
  второй глаз к ручному чеклисту (секции/строки/количества).
- `reference/ourplanecore-guide.md` — обновления программы май 2026 (3D per-edge roof,
  3D Massing AI-черновик, vertex-grips, page takeoff layers).

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
