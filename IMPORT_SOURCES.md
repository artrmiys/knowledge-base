# Import Sources Playbook

This repo is the clean MkDocs wiki. Do not scrape blindly into `docs/`.
Collect source data first, convert it to reviewable Markdown, then move only
good rules into the wiki pages.

## Source Types

### 1. Public websites

Use normal crawling:

1. Open the homepage.
2. Collect internal links.
3. Ignore platform/help/ads links.
4. Convert page text to Markdown.
5. Merge useful rules into existing topic pages.

This worked for `https://redacted.example/source-site/`, where only `Walls` and `Gables` had
active work links.

### 2. Trello boards

Browser HTML usually only exposes the JavaScript shell. For real cards/lists use
one of these:

- Trello JSON export from the board menu.
- Logged-in `.json` URL in the browser.
- Trello REST API with `TRELLO_KEY` and `TRELLO_TOKEN`.
- A future Trello/Atlassian MCP connector if available.

Current blocked boards:

- `TyUKA0Zw` / `int-trims` -> HTTP 401 for JSON/API.
- `wDztpnZg` / `изменения очень важно` -> HTTP 401 for JSON/API.

When you have a board export JSON:

```powershell
.\.venv\Scripts\python.exe tools\trello_json_to_markdown.py `
  --input C:\path\board.json `
  --output imports\trello
```

Review the generated Markdown before moving it into `docs/`.

### 3. Confluence

Best options:

- Space export as HTML/XML from Confluence admin/export UI.
- Atlassian REST API with email + API token.
- A future Confluence/Atlassian MCP connector if available.

REST shape:

```text
GET https://<site>.atlassian.net/wiki/rest/api/content
  ?spaceKey=<SPACE>
  &type=page
  &expand=body.storage,version,ancestors
```

Convert Confluence storage HTML to Markdown, keep page titles and source URLs,
then merge rules into topic pages.

## Import Rules

- Do not publish private links, emails, UIDs, salary history, tokens, or invite
  URLs.
- Keep source dumps outside `docs/` until reviewed.
- Prefer one imported Markdown file per Trello list / Confluence section.
- Keep exact source status in a temporary import note until useful rules are
  moved into public topic pages.
- Run `.\.venv\Scripts\python.exe -m mkdocs build --strict` after moving
  reviewed pages into `docs/`.
