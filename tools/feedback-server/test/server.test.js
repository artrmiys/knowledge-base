'use strict';
const assert = require('node:assert');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const { after, before, test } = require('node:test');

const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'kb-feedback-'));
const KEY = 'a'.repeat(48);
const ORIGIN = 'https://artrmiys.github.io';
const PAGE = 'https://artrmiys.github.io/knowledge-base/work/walls/';
fs.writeFileSync(path.join(dir, 'inbox.key'), KEY);
process.env.DATA_DIR = dir;
const { server } = require('../server.js');

let base;
before(() => new Promise((resolve) => server.listen(0, '127.0.0.1', () => {
  base = `http://127.0.0.1:${server.address().port}`;
  resolve();
})));
after(() => {
  server.closeAllConnections();
  server.close();
  fs.rmSync(dir, { recursive: true, force: true });
});

const send = (body, headers = { Origin: ORIGIN }) => fetch(`${base}/submit`, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json', 'X-Forwarded-For': '10.0.0.1', ...headers },
  body: typeof body === 'string' ? body : JSON.stringify(body),
});
const inbox = () => fetch(`${base}/inbox/${KEY}`).then((r) => r.text());

test('a correction is stored and shown on the private page', async () => {
  const r = await send({ page: PAGE, what: 'Неверный шаг', how: 'Должно быть 16', name: 'Катя' });
  assert.strictEqual(r.status, 200);
  assert.strictEqual(r.headers.get('access-control-allow-origin'), ORIGIN);
  const html = await inbox();
  assert.match(html, /новых 1/);
  assert.match(html, /Неверный шаг/);
  assert.match(html, /Должно быть 16/);
  assert.match(html, /Катя/);
  assert.match(html, /work\/walls/);
});

test('the stored record holds no IP address', () => {
  assert.doesNotMatch(fs.readFileSync(path.join(dir, 'inbox.jsonl'), 'utf8'), /10\.0\.0\.1/);
});

test('html in a correction is escaped', async () => {
  await send({ what: '<script>alert(1)</script>', name: '"><img src=x>' });
  const html = await inbox();
  assert.ok(!html.includes('<script>alert'));
  assert.ok(!html.includes('<img src=x'));
  assert.ok(html.includes('&lt;script&gt;'));
});

test('a page outside the site is dropped, so no foreign links appear', async () => {
  await send({ what: 'Ссылка чужая', page: 'javascript:alert(1)' });
  await send({ what: 'Ссылка чужая 2', page: 'https://evil.example/' });
  const html = await inbox();
  assert.ok(!html.includes('javascript:alert'));
  assert.ok(!html.includes('evil.example'));
});

test('bad requests are refused', async () => {
  assert.strictEqual((await send({ what: '' })).status, 400);
  assert.strictEqual((await send('not json')).status, 400);
  assert.strictEqual((await send({ what: 'С чужого сайта' }, { Origin: 'https://evil.example' })).status, 403);
  assert.strictEqual((await send({ what: 'x'.repeat(20000) })).status, 413);
});

test('the hidden field gets ok and stores nothing', async () => {
  const r = await send({ what: 'Бот пишет', website: 'spam' });
  assert.strictEqual(r.status, 200);
  assert.ok(!(await inbox()).includes('Бот пишет'));
});

test('the private page needs the exact key', async () => {
  assert.strictEqual((await fetch(`${base}/inbox/${'b'.repeat(48)}`)).status, 404);
  assert.strictEqual((await fetch(`${base}/inbox/aaaa`)).status, 404);
  assert.strictEqual((await fetch(`${base}/inbox`)).status, 404);
  assert.strictEqual((await fetch(`${base}/inbox.jsonl`)).status, 404);
});

test('Done moves a correction to the done list and back', async () => {
  const before_ = await inbox();
  const open = Number(before_.match(/новых (\d+)/)[1]);
  const id = before_.match(/toggle\/([a-f0-9]+)/)[1];
  const url = `${base}/inbox/${KEY}/toggle/${id}`;
  const r = await fetch(url, { method: 'POST', redirect: 'manual' });
  assert.strictEqual(r.status, 303);
  const after_ = await inbox();
  assert.match(after_, new RegExp(`новых ${open - 1}`));
  assert.match(after_, /Готовые: 1/);
  await fetch(url, { method: 'POST', redirect: 'manual' });
  assert.match(await inbox(), new RegExp(`новых ${open}`));
});

test('one address is limited to 20 corrections an hour', async () => {
  const headers = { Origin: ORIGIN, 'X-Forwarded-For': '10.0.0.9' };
  for (let i = 0; i < 20; i += 1) {
    assert.strictEqual((await send({ what: `Поправка ${i}` }, headers)).status, 200);
  }
  assert.strictEqual((await send({ what: 'Лишняя' }, headers)).status, 429);
});
