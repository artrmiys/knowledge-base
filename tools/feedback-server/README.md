# kb-feedback

Receives corrections from the form on `docs/start/suggest-change.md` (script `docs/assets/js/suggest.js`).
Node stdlib, no npm. Tests: `node --test` from this folder.

Server: deploy@185.81.165.121, folder `~/kb-feedback`.

- `app/server.js` - the code, mounted read-only.
- `data/inbox.jsonl` - corrections, append-only. Not in git, holds what readers wrote.
- `data/inbox.key` - the key of the private page, created on the server, never in git.
- `compose.yml` - stock `node:24-bookworm-slim`, container `kb_feedback`.

Address: `https://kb-fix.185.81.165.121.sslip.io`, a site block in `~/e-wood-pay/Caddyfile`.
That file is bind-mounted as a single file and shared with Pay: back it up, validate, write it in place with
`cat >`, then `caddy reload`, and check Pay afterwards.

Private page: `/inbox/<key>`. Read the key on the server: `cat ~/kb-feedback/data/inbox.key`.

Update: copy `server.js` to `~/kb-feedback/app/`, then `docker compose restart` in `~/kb-feedback`.

Limits: 20 corrections an hour from one address, 2000 characters a field, 5 MB in the file, then new ones are refused.
The IP address is used only in memory for the limit and is not written to disk.

Screenshots (2026-11-16): up to 3 per correction, PNG or JPEG, 2 MB each after decoding; the browser shrinks
bigger pictures to JPEG with the long side at most 2400 px. Files go to `data/files/<id>-<n>.png|jpg`, the record
lists them in `files`, the private page shows them at `/inbox/<key>/file/<name>`. Over 150 MB in `data/files`
new screenshots are refused (507). The Caddy block for kb-fix has `request_body max_size 10MB` for this.

Telegram (2026-11-16): every new correction goes to the owner's private chat (824988257) through the feedback
voice bot: one message with the text, page, name and a link to the private page, then the screenshots
(as photos, or as files if Telegram refuses a photo). The token is not copied anywhere: `~/kb-feedback/.env` is a
symlink to `~/telegram-codex-voice-bot/.env`, and compose passes only `TELEGRAM_BOT_TOKEN` into the container as
`TG_BOT_TOKEN`. If that bot is moved or archived, the symlink breaks and notices stop silently: point the
symlink at another bot's `.env` and change the variable name in `compose.yml`. A failed send is logged as
`telegram: <method> <status>` in `docker logs kb_feedback`, the correction is still stored.
