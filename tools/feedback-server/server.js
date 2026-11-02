'use strict';
// Receives corrections from the form on the KB site and shows them on one private page.
// Node stdlib only, no npm: the server disk is nearly full.
// Storage is one append-only file, DATA_DIR/inbox.jsonl.
const crypto = require('crypto');
const fs = require('fs');
const http = require('http');
const path = require('path');

const PORT = Number(process.env.PORT || 8080);
const DATA_DIR = process.env.DATA_DIR || './data';
const ORIGIN = process.env.ALLOWED_ORIGIN || 'https://artrmiys.github.io';
const SITE_ROOT = process.env.SITE_ROOT || 'https://artrmiys.github.io/knowledge-base/';
const LOG = path.join(DATA_DIR, 'inbox.jsonl');
const KEY = fs.readFileSync(path.join(DATA_DIR, 'inbox.key'), 'utf8').trim();
if (KEY.length < 32) throw new Error('inbox.key is too short');

const MAX_BODY = 16 * 1024;
const MAX_FILE = 5 * 1024 * 1024;
const MAX_TEXT = 2000;
const IP_LIMIT = 20;
const IP_WINDOW = 60 * 60 * 1000;
const hits = new Map(); // IP only lives here, in memory, and is never written to disk.

function limited(ip, now = Date.now()) {
  for (const [k, list] of hits) {
    const fresh = list.filter((t) => now - t < IP_WINDOW);
    if (fresh.length) hits.set(k, fresh);
    else hits.delete(k);
  }
  const list = hits.get(ip) || [];
  if (list.length >= IP_LIMIT) return true;
  list.push(now);
  hits.set(ip, list);
  return false;
}

function clean(value, max) {
  if (typeof value !== 'string') return '';
  return value.replace(/[^\P{Cc}\n\t]/gu, '').trim().slice(0, max);
}

function append(record) {
  fs.appendFileSync(LOG, JSON.stringify(record) + '\n');
}

function readInbox() {
  let text = '';
  try {
    text = fs.readFileSync(LOG, 'utf8');
  } catch (err) {
    if (err.code !== 'ENOENT') throw err;
  }
  const items = new Map();
  for (const line of text.split('\n')) {
    if (!line) continue;
    let rec;
    try {
      rec = JSON.parse(line);
    } catch {
      continue;
    }
    if (rec.toggle) {
      const item = items.get(rec.toggle);
      if (item) item.done = !item.done;
    } else if (rec.id) {
      items.set(rec.id, { ...rec, done: false });
    }
  }
  return [...items.values()].reverse();
}

function readBody(req) {
  return new Promise((resolve, reject) => {
    const parts = [];
    let size = 0;
    req.on('data', (chunk) => {
      size += chunk.length;
      // Keep draining without storing, so the client still receives the 413 answer.
      if (size > MAX_BODY) {
        parts.length = 0;
        reject(Object.assign(new Error('too large'), { status: 413 }));
        return;
      }
      parts.push(chunk);
    });
    req.on('end', () => resolve(Buffer.concat(parts).toString('utf8')));
    req.on('error', reject);
  });
}

function json(res, status, body, extra = {}) {
  res.writeHead(status, { 'Content-Type': 'application/json; charset=utf-8', ...extra });
  res.end(JSON.stringify(body));
}

function corsHeaders() {
  return {
    'Access-Control-Allow-Origin': ORIGIN,
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '86400',
    Vary: 'Origin',
  };
}

async function submit(req, res) {
  const cors = corsHeaders();
  if (req.headers.origin !== ORIGIN) return json(res, 403, { ok: false }, cors);

  let data;
  try {
    data = JSON.parse(await readBody(req));
  } catch (err) {
    return json(res, err.status || 400, { ok: false }, cors);
  }
  if (!data || typeof data !== 'object') return json(res, 400, { ok: false }, cors);
  // Hidden field: only bots fill it. They get a normal answer and nothing is stored.
  if (data.website) return json(res, 200, { ok: true }, cors);

  const what = clean(data.what, MAX_TEXT);
  if (what.length < 3) return json(res, 400, { ok: false, error: 'what' }, cors);

  const ip = String(req.headers['x-forwarded-for'] || req.socket.remoteAddress || '')
    .split(',').pop().trim();
  if (limited(ip)) return json(res, 429, { ok: false, error: 'rate' }, cors);

  let size = 0;
  try {
    size = fs.statSync(LOG).size;
  } catch {
    // no file yet
  }
  if (size > MAX_FILE) return json(res, 507, { ok: false, error: 'full' }, cors);

  const page = clean(data.page, 300);
  append({
    id: crypto.randomBytes(8).toString('hex'),
    at: new Date().toISOString(),
    page: page.startsWith(SITE_ROOT) ? page : '',
    what,
    how: clean(data.how, MAX_TEXT),
    name: clean(data.name, 80),
  });
  return json(res, 200, { ok: true }, cors);
}

function esc(value) {
  return String(value).replace(/[&<>"']/g, (c) => (
    { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]
  ));
}

function pageLabel(url) {
  const tail = url.slice(SITE_ROOT.length) || 'главная';
  try {
    return decodeURI(tail);
  } catch {
    return tail;
  }
}

function card(item) {
  const at = new Date(item.at).toLocaleString('ru-RU', {
    timeZone: 'America/Argentina/Buenos_Aires',
    dateStyle: 'short',
    timeStyle: 'short',
  });
  const page = item.page
    ? `<a href="${esc(item.page)}" target="_blank" rel="noopener noreferrer">${esc(pageLabel(item.page))}</a>`
    : 'страница не указана';
  const how = item.how ? `<p><b>Как должно быть:</b><br>${esc(item.how)}</p>` : '';
  const who = item.name ? ` - ${esc(item.name)}` : '';
  return `<article>
<div class="meta">${esc(at)}${who}<br>${page}</div>
<p>${esc(item.what)}</p>${how}
<form method="post" action="/inbox/${KEY}/toggle/${esc(item.id)}"><button>${item.done ? 'Вернуть' : 'Готово'}</button></form>
</article>`;
}

function inboxHtml() {
  const items = readInbox();
  const open = items.filter((i) => !i.done);
  const done = items.filter((i) => i.done);
  return `<!doctype html><html lang="ru"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow"><title>Поправки KB</title>
<style>
:root{color-scheme:light dark;--bg:#fff;--fg:#1c1c1c;--muted:#666;--line:#ddd}
@media (prefers-color-scheme:dark){:root{--bg:#161616;--fg:#eee;--muted:#aaa;--line:#3a3a3a}}
body{margin:0 auto;max-width:720px;padding:16px;background:var(--bg);color:var(--fg);font:16px/1.45 system-ui,sans-serif}
h1{font-size:22px;margin:8px 0 16px}
article{border:1px solid var(--line);border-radius:8px;padding:12px 14px;margin:0 0 12px}
article p{margin:8px 0;white-space:pre-wrap;overflow-wrap:anywhere}
.meta{color:var(--muted);font-size:14px;overflow-wrap:anywhere}
button{font:inherit;padding:6px 14px;cursor:pointer}
summary{cursor:pointer;margin:20px 0 12px;color:var(--muted)}
</style></head><body>
<h1>Поправки KB: новых ${open.length}</h1>
${open.map(card).join('\n') || '<p>Новых поправок нет.</p>'}
${done.length ? `<details><summary>Готовые: ${done.length}</summary>${done.map(card).join('\n')}</details>` : ''}
</body></html>`;
}

function keyMatches(given) {
  const a = Buffer.from(given);
  const b = Buffer.from(KEY);
  return a.length === b.length && crypto.timingSafeEqual(a, b);
}

const INBOX_HEADERS = {
  'Cache-Control': 'no-store',
  'Referrer-Policy': 'no-referrer',
  'X-Content-Type-Options': 'nosniff',
  'Content-Security-Policy': "default-src 'none'; style-src 'unsafe-inline'; form-action 'self'; frame-ancestors 'none'",
};

async function handle(req, res) {
  const { pathname } = new URL(req.url, 'http://localhost');

  if (pathname === '/health') return json(res, 200, { ok: true });
  if (pathname === '/submit') {
    if (req.method === 'OPTIONS') {
      res.writeHead(204, corsHeaders());
      return res.end();
    }
    if (req.method === 'POST') return submit(req, res);
    return json(res, 405, { ok: false });
  }

  const m = pathname.match(/^\/inbox\/([a-f0-9]+)(?:\/toggle\/([a-f0-9]+))?$/);
  if (m && keyMatches(m[1])) {
    if (!m[2] && req.method === 'GET') {
      res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8', ...INBOX_HEADERS });
      return res.end(inboxHtml());
    }
    if (m[2] && req.method === 'POST') {
      if (readInbox().some((i) => i.id === m[2])) append({ toggle: m[2] });
      res.writeHead(303, { Location: `/inbox/${KEY}`, ...INBOX_HEADERS });
      return res.end();
    }
  }
  res.writeHead(404, { 'Content-Type': 'text/plain; charset=utf-8' });
  return res.end('Not found');
}

const server = http.createServer((req, res) => {
  handle(req, res).catch((err) => {
    console.error(err.message);
    if (!res.headersSent) res.writeHead(500, { 'Content-Type': 'text/plain; charset=utf-8' });
    res.end('Error');
  });
});

if (require.main === module) {
  server.listen(PORT, '0.0.0.0', () => console.log(`kb-feedback on ${PORT}`));
}

module.exports = { server };
