'use strict';
const assert = require('node:assert');
const fs = require('node:fs');
const http = require('node:http');
const os = require('node:os');
const path = require('node:path');
const { after, before, test } = require('node:test');

const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'kb-feedback-'));
const KEY = 'a'.repeat(48);
const ORIGIN = 'https://artrmiys.github.io';
const PAGE = 'https://artrmiys.github.io/knowledge-base/work/walls/';
const PNG = 'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg==';
const JPG = Buffer.from([0xff, 0xd8, 0xff, 0xe0, 0, 16, 0x4a, 0x46, 0x49, 0x46, 0, 1]).toString('base64');

// A stand-in for api.telegram.org that records what it receives.
const tgCalls = [];
const tg = http.createServer((req, res) => {
  const parts = [];
  req.on('data', (c) => parts.push(c));
  req.on('end', () => {
    tgCalls.push({ url: req.url, body: Buffer.concat(parts).toString('latin1') });
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end('{"ok":true}');
  });
});
tg.listen(0); // no host: binds synchronously, so the port is known before the server loads

fs.writeFileSync(path.join(dir, 'inbox.key'), KEY);
process.env.DATA_DIR = dir;
process.env.TG_BOT_TOKEN = 'TESTTOKEN';
process.env.TG_CHAT_ID = '42';
process.env.TG_API = `http://127.0.0.1:${tg.address().port}`;
const { server } = require('../server.js');

let base;
before(() => new Promise((resolve) => server.listen(0, '127.0.0.1', () => {
  base = `http://127.0.0.1:${server.address().port}`;
  resolve();
})));
after(() => {
  server.closeAllConnections();
  server.close();
  tg.closeAllConnections();
  tg.close();
  fs.rmSync(dir, { recursive: true, force: true });
});

async function waitCalls(n) {
  for (let i = 0; i < 100 && tgCalls.length < n; i += 1) await new Promise((r) => setTimeout(r, 20));
  return tgCalls.slice(0, n);
}

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
  assert.strictEqual((await send({ what: 'x'.repeat(10 * 1024 * 1024) })).status, 413);
});

test('a screenshot is stored, shown on the private page and served only with the key', async () => {
  const r = await send({ what: 'Со скрином', images: [`data:image/png;base64,${PNG}`] });
  assert.strictEqual(r.status, 200);
  const html = await inbox();
  const name = html.match(/file\/([a-f0-9]{16}-1\.png)/)[1];
  const img = await fetch(`${base}/inbox/${KEY}/file/${name}`);
  assert.strictEqual(img.status, 200);
  assert.strictEqual(img.headers.get('content-type'), 'image/png');
  assert.strictEqual(Buffer.from(await img.arrayBuffer()).toString('base64'), PNG);
  assert.strictEqual((await fetch(`${base}/inbox/${'b'.repeat(48)}/file/${name}`)).status, 404);
  assert.strictEqual((await fetch(`${base}/inbox/${KEY}/file/..%2Finbox.key`)).status, 404);
  assert.strictEqual((await fetch(`${base}/inbox/${KEY}/file/inbox.jsonl`)).status, 404);
});

test('bad screenshots are refused and nothing is stored', async () => {
  const fake = Buffer.from('<svg onload=alert(1)>').toString('base64');
  const four = Array(4).fill(`data:image/png;base64,${PNG}`);
  assert.strictEqual((await send({ what: 'Не картинка', images: [`data:image/png;base64,${fake}`] })).status, 400);
  assert.strictEqual((await send({ what: 'SVG', images: [`data:image/svg+xml;base64,${fake}`] })).status, 400);
  assert.strictEqual((await send({ what: 'Четыре', images: four })).status, 400);
  assert.strictEqual((await send({ what: 'Не список', images: 'x' })).status, 400);
  const html = await inbox();
  for (const t of ['Не картинка', 'SVG', 'Четыре', 'Не список']) assert.ok(!html.includes(`<p>${t}</p>`));
});

test('a new correction goes to Telegram with its screenshots', async () => {
  tgCalls.length = 0;
  await send({ page: PAGE, what: 'В телегу', name: 'Максим', images: [`data:image/png;base64,${PNG}`] });
  const [msg, photo] = await waitCalls(2);
  assert.strictEqual(msg.url, '/botTESTTOKEN/sendMessage');
  assert.ok(Buffer.from(msg.body, 'latin1').toString('utf8').includes('В телегу'));
  assert.ok(Buffer.from(msg.body, 'latin1').toString('utf8').includes('Максим'));
  assert.ok(msg.body.includes(`/inbox/${KEY}`));
  assert.strictEqual(photo.url, '/botTESTTOKEN/sendPhoto');
  assert.ok(photo.body.includes(Buffer.from(PNG, 'base64').toString('latin1')));

  tgCalls.length = 0;
  await send({ what: 'Два скрина', images: [`data:image/png;base64,${PNG}`, `data:image/jpeg;base64,${JPG}`] });
  const [, group] = await waitCalls(2);
  assert.strictEqual(group.url, '/botTESTTOKEN/sendMediaGroup');
  assert.ok(group.body.includes('attach://f1'));
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
