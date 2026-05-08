# Current Session Handoff

Updated: 2026-05-06 / 2026-05-07 live import session.

## User intent

The user wants this wiki to keep the current design/structure and be filled
with estimating content, tables, schemes, and useful pictures from the logged-in
E-Wood sources.

Important: do not change design, theme, nav, CSS, `mkdocs.yml`, or the hero
unless the user explicitly asks. The user was upset when the design changed.
Continue with content-only imports and page enrichment.

## Workspace

- Project root: `E:\---\Work\knowledge-base-e-wood`
- Site stack: MkDocs + Material.
- Local preview URL: `http://127.0.0.1:8000/knowledge-base-e-wood/`
- Build check: `.\.venv\Scripts\python.exe -m mkdocs build --strict`

## Live browser sources

Open these with Playwright/browser after the user is logged in:

- Confluence work overview:
  `https://ewood.atlassian.net/wiki/spaces/work/overview?homepageId=1933591`
- Trello important changes:
  `https://trello.com/b/wDztpnZg/%D0%B8%D0%B7%D0%BC%D0%B5%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F-%D0%BE%D1%87%D0%B5%D0%BD%D1%8C-%D0%B2%D0%B0%D0%B6%D0%BD%D0%BE`
- Trello int trims:
  `https://trello.com/b/TyUKA0Zw/int-trims`

Do not store passwords, cookies, tokens, email screenshots, UID, salary,
credentials, SSH/IP secrets, or private links in docs.

## Current raw import state

Raw Confluence imports are being stored here:

`imports/live-sources/confluence-work/pages/`

Full Confluence `work` space crawl completed on 2026-05-07:

- Confluence pages found in the `work` space: 63.
- Safe/usable source URLs now mapped into the wiki: 61.
- Safe missing pages imported during the full crawl pass: 11.
- Private/sensitive pages intentionally skipped: 2.
- Wiki pages with generated `Confluence Context` relationship blocks: 43.
- Confluence public image assets imported and used: 175 / 175.

The current relationship/audit pages are:

- Public map: `docs/reference/confluence-source-map.md`
- Full image archive: `docs/reference/confluence-image-archive.md`
- Internal usage audit: `imports/live-sources/confluence-work/USAGE_AUDIT.md`
- Full crawl manifest: `imports/live-sources/confluence-work/space_crawl_manifest.json`

Do not import or publish the skipped private pages:

- `salary - conditions` - private salary/conditions page.
- `Conditions 2026` - contains pay/vacation conditions mixed with estimating
  notes.

Trello was imported from the logged-in browser session:

- `imports/live-sources/trello-int-trims/` - original browser DOM dump:
  44 cards, 43 images.
- `imports/live-sources/trello-important-changes/` - original browser DOM dump:
  62 cards, 16 images.
- `imports/live-sources/trello-int-trims-full/` - full Trello API export:
  44 cards, 43 attachments, 279 actions, 0 comments.
- `imports/live-sources/trello-important-changes-full/` - full Trello API
  export: 75 cards, 20 attachments, 269 actions, 0 comments.

Full live-source audit:

- `imports/live-sources/FULL_SOURCE_AUDIT.md`
- `docs/reference/trello-source-map.md`

The old `important changes` DOM dump missed 13 cards and 4 attachment images.
The full API export fixed this; public `docs/start/important-changes.md` now
has 20 important-change images.

The public site assets now include copied images:

- `docs/assets/images/trims/int-trims-01.png` through `int-trims-43.png`
- `docs/assets/images/reference/important-change-01.png` through
  `important-change-20.png`
- `docs/assets/images/confluence/confluence-001.*` through `confluence-175.*`
  plus `docs/assets/images/confluence/manifest.json`.

Confluence image import:

- Raw originals: `imports/live-sources/confluence-work-images/`
- Public archive page: `docs/reference/confluence-image-archive.md`
- Imported public images/previews: 175
- Large GIF/PNG attachments were converted to lightweight public previews.
- The private `salary - conditions` page is intentionally excluded.

## Import helper

A local helper was added:

`tools/live_source_receiver.py`

Purpose: receive already-extracted JSON/base64 images from the logged-in
Playwright browser and write raw dumps under `imports/live-sources/`.

Start it when continuing a live import:

```powershell
.\.venv\Scripts\python.exe tools\live_source_receiver.py --host 127.0.0.1 --port 8765
```

If a previous receiver process is still running, stop it before starting a new
one.

## Next good step

Confluence image galleries have been applied to the topic pages with generated
blocks marked by:

```markdown
<!-- confluence-gallery:start -->
...
<!-- confluence-gallery:end -->
```

Use this refresh command after a new Confluence image import:

```powershell
.\.venv\Scripts\python.exe tools\apply_confluence_galleries.py
```

The script maps 175 imported images into 33 wiki pages by Confluence source
page/topic and keeps the hidden full archive page for audit.

Refresh commands after a new live Confluence import:

```powershell
.\.venv\Scripts\python.exe tools\import_confluence_json_dump.py --space-pages imports\live-sources\confluence-work\confluence-space-pages-2026-05-07.json --safe-pages imports\live-sources\confluence-work\confluence-safe-missing-pages-2026-05-07.json
.\.venv\Scripts\python.exe tools\apply_confluence_context.py
.\.venv\Scripts\python.exe tools\apply_confluence_galleries.py
$env:PYTHONIOENCODING='utf-8'; .\.venv\Scripts\python.exe tools\audit_confluence_usage.py
.\.venv\Scripts\python.exe tools\import_confluence_full_rest.py --input imports\live-sources\confluence-work\confluence-work-full-rest-export-2026-05-07.json
.\.venv\Scripts\python.exe tools\import_trello_full_export.py --input imports\live-sources\trello-int-trims\trello-int-trims-full-with-attachments-2026-05-07.json --output imports\live-sources\trello-int-trims-full
.\.venv\Scripts\python.exe tools\import_trello_full_export.py --input imports\live-sources\trello-important-changes\trello-important-changes-full-with-attachments-2026-05-07.json --output imports\live-sources\trello-important-changes-full
.\.venv\Scripts\python.exe tools\build_trello_source_map.py
.\.venv\Scripts\python.exe tools\audit_full_source_coverage.py
.\.venv\Scripts\python.exe -m mkdocs build --strict
```

Next content step:

1. Review the generated captions and replace generic attachment names with
   human descriptions where the image itself shows a clear rule.
2. Continue turning the generated `Confluence Context` notes into shorter
   hand-written estimating rules on the topic pages.
3. Keep `docs/reference/confluence-source-map.md` in nav so every source/page
   relationship stays visible.

---

## Session handoff — 2026-05-07 (Confluence integration pass)

### Что было сделано в сессии

**Push 1 (commit `4cad4d7`)** — выкачено всё накопленное содержимое в гит:
- 175/175 публичных Confluence-картинок в `docs/assets/images/confluence/`
- 43 Trello int-trims + 20 important-changes картинки
- Полный source-map (Confluence + Trello + Tilda)
- Все docs/work/* страницы с auto-generated `<!-- confluence-context -->` и `<!-- confluence-gallery -->` блоками
- Конфиг (mkdocs.yml, overrides/, tools/), мета-доки (CLAUDE.md, AGENTS.md, IMPORT_SOURCES.md)
- `.gitignore` пополнен: `twist-*.md`, `twist-*.json`, `probe-twist-*.json` (приватные снапшоты)

**Confluence integration pass (в процессе)** — встраивание контента из raw Confluence в hand-written секции docs/-страниц + удаление дублирующих `<!-- confluence-context -->` блоков (галереи `<!-- confluence-gallery -->` НЕ трогать).

Pilot и завершённые batch'и:

- **Pilot** (`docs/work/vertical/walls/exterior.md`) — добавлены секции `## Wall Sizing & Height` и `## Под Bottom Plate (на бетоне)`. Используй как style reference для остальных страниц.
- **Walls batch (8 страниц)** — completed: corners, corridor, demising, parapet, shaft, furring, gable, sill-plates, unit. Конкретика: PlanSwift `dem (2) 2x6 10.5` запись, parapet vs truss decision tree, gable stick-vs-truss, sill plate vs btm plate, unit `A 2x4`/`A 2x6` с letter prefixes.
- **Openings + Sheathing batch (8 страниц)** — completed: windows-doors (macro `F_Openings`, mark `d`/`gd`), wall-sheathing (Sheathing Material Variants table — CDX/OSB/Zip/APA), truss-heel (heel height 1'-7"), headers/floor/gable/shear-wall/dup-of-gable (Confluence stubs — только удалён context block).

В фоне на момент паузы работали 2 агента — их writes идут напрямую на диск, должны были закончиться:

- **Floor + Roof + Deck batch (13 страниц)**: `docs/work/horizontal/floor-framing/{beam,joist,post}.md` + `docs/work/horizontal/roof-framing/{ridge,header,dbl-trpl-rafters,hip,valley,overframes,canopy,dormer,roof-sheathing}.md` + `docs/work/deck/{anchor-bolts,balcony-trims,railing}.md`
- **Reference + Job-types + Start batch (~10 страниц)**: `docs/work-types/{com,ewp-capital,residential}.md`, `docs/start/{takeoff-structure,quality-checklist,maintenance,how-to-use}.md`, `docs/reference/hangers.md`

### Что нужно сделать после возобновления

1. **Проверить, что 2 фоновых агента закончили работу:**
   ```powershell
   git status --short
   ```
   Если изменены файлы из batch'ей выше — агенты закончили. Если нет — перезапустить их (см. раздел "Если агенты не закончили" ниже).

2. **Build + проверить:**
   ```powershell
   .\.venv\Scripts\python.exe -m mkdocs build --strict
   ```
   Должно быть 0 warnings/errors (Material marketing notice — ignore, см. CLAUDE.md §13.2).

3. **Commit + push:**
   ```powershell
   git add docs/
   git commit -m "content: интегрировать конкретику из Confluence raw в docs/-страницы"
   git push origin main
   ```
   GitHub Actions автоматически передеплоит сайт.

4. **Если нужно — handle box-sheathing.md:** у него нет Confluence-источника, проверь что `<!-- confluence-context -->` блок там либо отсутствует, либо тоже удалён.

### Если агенты не закончили

Возможно при паузе сессии 2 фоновых агента (`floor+roof+deck` и `reference+job-types`) были прерваны до завершения. Проверка:

```powershell
git diff --stat docs/ | grep -E "(beam|joist|post|ridge|header|dbl-trpl|hip|valley|overframes|canopy|dormer|roof-sheathing|anchor-bolts|balcony-trims|railing|com\.md|ewp-capital|residential|takeoff-structure|quality-checklist|maintenance|how-to-use|hangers)"
```

Если этих файлов в diff нет — нужно перезапустить недостающие batch'и. Инструкции были такие (одинаковые для всех):

> Для каждой docs/-страницы: прочитать raw Confluence MD из `imports/live-sources/confluence-work-full/pages-public/`, извлечь конкретные правила/числа/PlanSwift записи которые ЕСТЬ в Confluence но НЕТ в hand-written секциях текущей docs/-страницы, добавить в существующие `## Critical Rules`/`## Count` или новые H2-секции (между шапкой и `<!-- confluence-context -->`). После — УДАЛИТЬ блок `<!-- confluence-context:start -->` ... `<!-- confluence-context:end -->`. Блок `<!-- confluence-gallery -->` — НЕ трогать. Пилот: `docs/work/vertical/walls/exterior.md`. НЕ цитировать salary/email/UID/private. Финальный build `--strict`.

Полные таблицы (docs ↔ raw Confluence MD) для каждого batch — см. начало сессии (используй `imports/live-sources/confluence-work-full/pages-public/` + `docs/reference/confluence-source-map.md` для маппинга).

### Что НЕ сделано в этой сессии (next sessions)

1. **Captions у gallery картинок** — все ещё generic ("exterior wall detail/reference 01"). Можно улучшить вытянув `<ac:caption>` из Confluence storage HTML.
2. **Twist `WORK_EXTRACT_DRAFT.md`** — `imports/live-sources/twist-1337560-private/WORK_EXTRACT_DRAFT.md` ещё не разобран. Содержит и приватное (нельзя в публичный docs), и полезные правила (можно).
3. **Trello-карточки** (44 int-trims + 75 important-changes) — raw в `imports/live-sources/trello-*-full/`. Картинки уже в публичном docs, текстовые правила из карточек ещё не извлечены.
4. **Confluence Context дублирование на reference/source-map.md** — resolved in the resume pass below.

---

## Resume pass — 2026-05-08

Completed the Confluence integration cleanup after the interrupted session:

- Confirmed the two late batches wrote to disk:
  - Floor + Roof + Deck pages.
  - Reference + Job Types + Start pages.
- Removed every remaining `<!-- confluence-context:start -->` / `<!-- confluence-context:end -->`
  block from `docs/`; galleries were left in place.
- Fixed the stale `maintenance.md` anchor link to `quality-checklist.md`.
- Verified there are no remaining `confluence-context` blocks in `docs/`.
- Verified `.\.venv\Scripts\python.exe -m mkdocs build --strict` passes.
- Committed the integration to `main` as `67424e5`.
- Pushed `main` to GitHub. The GitHub Actions API did not show a fresh run
  after the push, so a one-off manual deploy was run with:
  `.\.venv\Scripts\python.exe -m mkdocs gh-deploy --force --clean --remote-branch gh-pages`.
- Verified the live exterior page returned HTTP 200, contained `Wall Sizing`,
  and did not contain a `confluence-context` marker.

Next content still worth doing later:

1. Improve generic gallery captions.

---

## Resume pass 2 — 2026-05-08

Continued the remaining import cleanup:

- Extracted text rules from `imports/live-sources/trello-int-trims-full/pages/`
  into interior-trim topic pages:
  - `docs/work/interior-trims/base.md`
  - `docs/work/interior-trims/crown.md`
  - `docs/work/interior-trims/door-window-trim.md`
  - `docs/work/interior-trims/overview.md`
- Extracted high-signal text-only cards from
  `imports/live-sources/trello-important-changes-full/pages/` into
  `docs/start/important-changes.md`.
- Copied the same Trello rules into closest topic pages where useful:
  joist, post, beam, blocking, rim, roof sheathing, box sheathing, headers,
  anchor bolts, balcony trims, eve/soffit, cantilevered SQFT, hangers, and
  boss-feedback QA.
- Reviewed `imports/live-sources/twist-1337560-private/WORK_EXTRACT_DRAFT.md`
  and copied only non-private estimating rules into topic pages:
  - draft stop vs shear wall sheathing;
  - shaft detail/resilient-channel checks;
  - metal-stud unit wall spacing/jamb checks;
  - demising rim counted on both sides.
- Did not copy project names, due dates, people names, screenshots, or raw Twist
  chat text into public docs.
- Checked Confluence image metadata for better gallery captions. The manifest
  and raw image pages only carried generic attachment filenames/page titles, not
  useful `<ac:caption>` text, so no safe bulk caption rewrite was made.

---

## Resume pass 3 — 2026-05-08

Improved the Interior Trims section after user feedback that rules were not
connected clearly enough to pictures:

- Added a `Picture Map` and `Workflow Pictures` table to
  `docs/work/interior-trims/overview.md`.
- Added `Picture Guide` tables to:
  - `docs/work/interior-trims/base.md`
  - `docs/work/interior-trims/crown.md`
  - `docs/work/interior-trims/door-window-trim.md`
- Expanded the visual galleries on Base, Crown, and Door/Window Trim so the
  topic pages show the relevant Trello images directly instead of relying only
  on the full visual archive.
- Added a door-notation table explaining `2680`, `(2)2680`, `2680 Pocket`,
  `(2)3080 Slider`, `2680 Metal F.R. S.C.`, and `4080 C.O.`.
- Clarified that door `F.R.` means fire-rated and should not be confused with
  `FRT` lumber.

---

## Resume pass 4 -- 2026-05-08

Added a small internet sanity-check pass for Interior Trims, with restrained
scope so external references do not override E-Wood takeoff rules:

- Added two original SVG diagrams:
  - `docs/assets/images/trims/finish-schedule-trim-check.svg`
  - `docs/assets/images/trims/door-fr-sc-notation.svg`
- Added `External Cross-Check` sections to:
  - `docs/work/interior-trims/overview.md`
  - `docs/work/interior-trims/base.md`
  - `docs/work/interior-trims/crown.md`
  - `docs/work/interior-trims/door-window-trim.md`
- Added web-reference links to `docs/reference/source-map.md`.
- Sources used only as terminology/sanity checks:
  UL fire-rated doors guide, NAAMM/HMMA hollow metal fire-door checklist,
  Steel Door Institute fire-door assembly notes, AWC FRTW FAQ, Helonic finish
  schedule guide, and Metrie measuring guide.
- Confirmed all external URLs returned HTTP 200 before committing the links.

Follow-up content note:

- Made the garage trim rule explicit on Interior Trims overview, Base, and Crown:
  garage has no `Baseboard` and no `Crowns`; do not carry those perimeters
  through garage walls.

---

## Resume pass 5 -- 2026-05-08

Improved the Joist page after user feedback that `joist type` pictures were
hard to find:

- Added `docs/assets/images/framing/joist-types-overview.svg`.
- Added a `Joist Type Pictures` section near the top of
  `docs/work/horizontal/floor-framing/joist.md`.
- Pulled the existing Confluence joist-series images up into a visible gallery:
  `TJI`, `RED`, `LP/LPI`, `RFPI`, `BCI`, `Nordic Joist`, and spacing.
- Re-captioned the old Confluence gallery entries so they no longer say generic
  `joist series/reference 01`.
- Clarified the EWP material rule: count engineered joists only; do not convert
  every regular `2x` joist into an EWP line unless the scope says so.

Follow-up cleanup after user feedback that the page still looked disconnected:

- Removed unclear generated SVG diagrams from visible docs and deleted the
  unused generated SVG assets.
- Removed the remaining generated `joist-run-rim-blocking.svg` from the Joist
  page so the page starts with real source pictures.
- Added CSS rule-card layout (`.kb-rule-gallery`, `.kb-rule-card`) so each
  screenshot sits directly with its estimating rule and action note.
- Rebuilt Joist, Interior Trims Overview, Base, Crown, and Door/Window Trim
  around real imported screenshots instead of separate image tables plus
  detached galleries.
- Removed the duplicate raw Confluence gallery from Joist after all useful
  Joist Series images were integrated into rule cards.

---

## Resume pass 6 -- 2026-05-08

Large Russian-language upgrade after user feedback that the site should be in
Russian except for estimating/construction terms:

- Updated `mkdocs.yml` navigation labels and theme toggle labels to Russian
  where they were workflow/UI text, while keeping trade terms such as `Joist`,
  `Sheathing`, `Hangers`, `Interior Trims`, `COM`, `EWP`, and `PlanSwift`.
- Converted common H2 headings and table columns across docs to Russian:
  `Что считать`, `Проверить`, `Правила`, `Критические правила`,
  `Визуальные правила`, `Внешняя проверка`, `Где смотреть`, etc.
- Rewrote the most visible English prose on:
  - `docs/index.md`
  - `docs/start/how-to-use.md`
  - `docs/start/client-rules.md`
  - `docs/start/quality-checklist.md`
  - `docs/start/maintenance.md`
  - `docs/start/takeoff-structure.md`
  - `docs/start/important-changes.md`
  - `docs/reference/boss-feedback-rules.md`
  - `docs/reference/formulas.md`
  - `docs/reference/hangers.md`
  - `docs/work-types/*.md`
  - all visible `docs/work/**` topic pages
  - `docs/work/interior-trims/*`
- Rewrote Joist and Interior Trims rule cards into RU explanations while
  preserving technical terms/code labels in English.
- Removed noisy gallery suffixes like `(image, 222 KB raw)` / `(preview, ... KB raw)`
  from captions so image captions are cleaner on the public site.

Need after this note:

1. Run `.\.venv\Scripts\python.exe -m mkdocs build --strict`.
2. Review any broken anchors caused by heading translation.
3. Commit and deploy to `main` / `gh-pages`.
