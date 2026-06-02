# CHANGELOG

Лог изменений wiki. Сайт деплоится вручную (Actions на паузе):
`.\tools\deploy.ps1` или `mkdocs gh-deploy --force --clean --remote-branch gh-pages`.
Прод: https://artrmiys.github.io/knowledge-base/

## 2026-06-02

### Контент — новая страница Metal Tracks / CFMF
- Добавлена обучающая страница `work/vertical/walls/metal-tracks.md` (Работа →
  Вертикальные работы → Walls, рядом с Exterior). Покрывает: что такое CFMF
  (plates→tracks, studs→mtl studs), три типа треков, **deflection track** (зачем и
  когда обязателен), **GA (gauge)** — толщина стали, деревянные / double jambs у
  проёмов, **пакет обшивки = как у деревянной стены** (sheathing / vapor / insulation
  / gypsum / bracing / blocking), концепт takeoff (tracks по LFT, studs по spacing),
  **by others** (проверять scope), и где искать детали — **WT-листы**.
- Две реальные детали в `assets/images/walls/`: `metal-deflection-head.png`
  (DEFLECTION HEAD + стальная балка) и `metal-wt-section.png` (слои стены на floor
  line). Источник: 112 Queensberry, A402 Section Details.

### Бренд — починен логотип (чёрные артефакты)
- `assets/images/brand/icon-kb-128.png`: PNG имел непрозрачный почти-чёрный фон
  вокруг плитки → на светлой шапке читался как чёрный квадрат, плюс был смещён.
  Пересобрал из оригинала: альфа по яркости + **un-matting** (деление цвета на
  альфу против чёрного) — кромка стала чистый navy без тёмного ореола (0 fringe-
  пикселей), обрезан по содержимому и отцентрован (130×130 → 116×116).

### Контент — Workflow развёрнут
- `start/workflow.md`: переписан из списка в методичку. Новый раздел «сканируй
  лист целиком» (слева→направо, сверху→вниз, один scope за проход) со схемой
  `framing/scan-order.svg`. Раздел **Beams — длина и округление** (support to
  support; ≥8' → до 2', <8' как есть) со схемой `framing/beam-marking-direction.svg`.
  Раздел Joists, callout'ы про scale и двойной waste, ссылки на все предметные
  страницы и QA.

### Контент — Basement wall вынесен из SQFT
- Описание каркаса цокольной стены перенесено из `work/sqfts/basement.md` в новую
  страницу `work/vertical/walls/basement.md` (Walls, после Sill Plates; добавлена
  в nav). В SQFT остался только расчёт площади + кросс-ссылка.

### Контент — naming (takeoff-structure)
- `start/takeoff-structure.md`: добавлен `prpt` / `p` = parapet; починена опечатка
  `blocking ×2` (`bи` → `bb`); Details-коды развёрнуты по макросу `struct_rimblock`
  (правила ×2 / o.c. / группа); добавлена таблица **Connectors/fasteners**
  (hangers / screws / ties + `blt` = Anchor Bolts + Washers + Nuts, 3 строки,
  default 24" o.c.) со ссылками на Bolts / Screws / Hangers.

### Фиксы — битые кириллические якоря
- ASCII-id для русских заголовков: `corridor.md#rules`, `sill-plates.md#with-sill-plate`,
  `ourplanecore.md#tab-6-ai-manager`, `ourplanecore.md#hotkeys`. Ссылки обновлены
  в demising/exterior/basement/site-preview/ourplanecore.

## 2026-05-31

### Дизайн — применён OurCore Design Code v0.2 (источник: `my design core system.zip`)
- **Закон цвета:** зелёный полностью убран. **blue `#2f7fd6`(light)/`#4ea1ff`(dark)
  = «выбрано»** (active tab, ссылка, selected, primary CTA, info-leader);
  **sage `#6fa37c`/`#8fb89a` = бренд** — узко: 1.5-px полоска под active tab,
  left-border активного пункта nav/TOC, маркеры списков, tip-callout, логотип.
  Статусы ok/warn/err. Никакого неона/gradient-mesh.
- `tokens.css` переписан под v0.2: ink-поверхности light+dark, токены `--ds-*` +
  маппинг Material `--md-*` для обеих схем. Шрифты **Inter + JetBrains Mono**
  (`@import`), цифры моно/tabular. Радиусы 6/8/12/16.
- `extra.css` перешит: нейтральная шапка (white/ink, тонкая граница),
  active=blue+sage, admonitions→callouts (note/info blue · tip sage · warning warn
  · danger err), rounded-таблицы с uppercase-шапкой, карточки/hero/секции.
  Декоративные `kb-st--*`/`kb-mk--*` сведены к blue/sage/warn.
- Лого/favicon = KB-глиф `assets/images/brand/icon-kb-128.png`; палитра `blue`.
- 51 SVG-схема перекрашены: accent `#2e7d32` → blue `#2f7fd6`.
- Проверено рендером (headless Chrome) в светлой и тёмной теме. Зафиксировано в
  CLAUDE.md §6 — green/lime не возвращать.

### Контент — спейсинг, факторы, перелинковка
- **Joist vs Stud spacing разведены.** `formulas.md`: две таблицы — Stud
  (`12/16/24 = 1.4667/1.1/0.625`, boss-rule «1 стойка/фут + waste») и **Joist**
  (геометрия `12/spacing` → `1.0/0.75/0.625/0.5`). `joist.md` исправлен (был
  stud-фактор). Stud-таблица добавлена в `Exterior Walls`. Rim `1.05` — EWP-only
  (подтверждено везде). `industry-standards`, `boss-feedback`, `quantity-benchmarks`
  согласованы.
- **See-also перелинковка** по work/work-types/reference; определения терминов на
  тонких страницах; чистка мёртвых `Source: redacted` строк.
- `site-preview` — починены пути картинок (raw-HTML `../assets`→`../../assets`).
- `bracingdrywall` — bracing-length явно как свойство стены (+ ссылки на walls/COM).

### Схемы и картинки
- **49 новых SVG-схем** в едином чертёжном стиле на всех страницах, где не было
  изображений (rim/blocking/ribbon/bolts/screws/steel-beam/bracing, stair/subfloor,
  header, gable/shear/box sheathing, corners/furring, rake/returns/ridge-valley-hip/
  rooftype/flashing, 8× sqfts, casing/room-schedule, siding eifs/measure,
  exterior-trims ×5, deck-frame, ceiling-soffit, 3× work-types, stud-spacing-extra,
  sill-plate-assembly). Новые папки `framing/`, `openings/`, `sqfts/`, `siding/`,
  `work-types/`, `brand/`.
- **6 «гпт-шных» SVG перерисованы** в архитектурном стиле (wall sections, eave map,
  hanger flow) — настоящие штриховки/leader-линии.
- **Реальные reference-картинки интегрированы в текст** (вместо дампов-галерей):
  sill-plates (узел + termite shield), parapet (truss-bearing detail), unit
  (A2x4/A2x6 PlanSwift), corridor/demising (takeoff-строки), shaft (CH-stud/J-track
  + shaftliner), com (field/extra/dbl studs), ewp-capital (материалы).

### Reference — OurPlaneCore: две страницы → одна
- `ourplanecore.md` и `ourplanecore-guide.md` объединены в одну (актуальное
  состояние май 2026: per-edge 3D roof, 3D Massing, vertex-edit). `-guide` удалён,
  nav и ссылки (`ai-assist-system`, `ceiling-soffit-framing`) поправлены.

## 2026-05-30

### Чистка — убраны corpus-частоты (`%`/freq) из обучалки
- Со всех work/reference-страниц убраны частотные проценты и `freq`-колонки
  (`94%`, `81%`, `58%`, «по корпусу N файлов» и т.п.) — для рабочей wiki это шум.
  Оставлено только полезное: что за позиции, типовые спеки и размеры.
  Затронуто: hardware-catalog, parapet, sill-plates, gable, beam, stair, subfloor,
  basement, roof-sheathing, truss-heel, wall-sheathing, siding/types, exterior,
  railing, ceiling-soffit-framing, quality-checklist.

### Work — Ceiling / Soffit Framing (новая страница)
- `work/horizontal/ceiling-soffit-framing.md` + nav. Внутренний каркас потолков/софитов:
  Interior Soffit Framing (dropped soffit `2x4`), Kitchen Ceiling (per unit), Ceiling Mech
  (`2x6` Plate + Frame `24"oc` + Screws, MC/1-storey), Interior Materials/Gable Walls.
  Чётко отделено от finish-trim, roof eave soffit и truss soffit plywood. Источник — RCP.

### Reference — corpus-данные (новые страницы)
- `reference/hardware-catalog.md` + nav. Словарь крепежа Simpson по корпусу 180+
  takeoff'ов с частотами: hangers / ties-clips / straps / post bases-caps /
  holdowns (HDU-серия) / screws. Дополняет прескриптивный `hangers.md`.
- `reference/quantity-benchmarks.md` + nav. Типовые количества/длины (median[q1–q3])
  для sanity-check + сверка факторов с индустрией + метод Tukey.

### Распределение corpus-фактов по профильным страницам (полный проход)
- `floor-framing/stair.md` — спеки stringers `2x12`/LVL, treads/risers `12'`, `1x8` riser.
- `floor-framing/subfloor.md` — дефолт `3/4" T&G` (88%) + Panel Adhesive `29OZ` companion.
- `sqfts/basement.md` — состав цокольной стены: btm-plate всегда P.T., studs by-height, corridor.
- `roof-framing/roof-sheathing.md` — companion overhang-каркас (sub fascia/blocking/clips/H2.5)
  + flat-roof опоры (timber posts/LVL beams/CBH caps).
- `vertical/sheathing/truss-heel.md` — Vapor Barrier companion (81%) + blocking-for-drywall.
- `vertical/sheathing/wall-sheathing.md` — OSB чаще Zip (~3:1) как sanity-default.
- `siding/types.md` — ориентация Horizontal/Vertical + companion Post Wrap/Fascia.
- `vertical/walls/exterior.md` — полнота 1st-floor стены (studs/bracing/holdowns 58%/headers).
- `deck/railing.md` — metal vs wood railing (corpus): mtl post/cap/balusters vs `4x4 P.T.`.
- `vertical/walls/parapet.md` — типовой состав (corpus): 3 плоскости обшивки
  (inside 94% + wall 89% + top 82%) + drip edge 100% + studs/plates.
- `vertical/walls/sill-plates.md` — corpus-спеки: Sill Sealer `6"` (100%),
  Termite Shield `Copper` (100%), Washer `3x3 Square`; anchor ~71%.
- `vertical/walls/gable.md` — Draft Stop (`1/2" Ply`/`5/8" Type X`, ~36%, частый пропуск).
- `horizontal/floor-framing/beam.md` — частые сечения (`1¾x11⅞ LVL`/`2x10`/`1¾x14 LVL`),
  длина med `12'`, кол-во `2–4`.

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
