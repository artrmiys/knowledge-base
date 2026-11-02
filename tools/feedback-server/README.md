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
