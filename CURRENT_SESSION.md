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
