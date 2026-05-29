# Аудит wiki — 2026-05-29

Прошлись по всем 104 .md (4 параллельных Explore-агента + ручная верификация
каждой претензии). Часть жалоб была ложной (нормальный wiki-стиль с англ.
терминами в рус. тексте), они отсеяны. Ниже — только реально подтверждённые
находки.

---

## ✅ Сделано в этом проходе

### Flashing-рефакторинг (предыдущая итерация)
- Создана отдельная страница `docs/work/vertical/openings/window-flashing.md`
  с правилом «3 стороны / sill / у дверей нет sill», разделением по wood / Mtl
  / CMU / concrete и опциональным wood jamb `1x4` / `2x4 P.T.` на бетоне.
- `docs/work/sheathing-and-misc/flashing.md` сброшен до заглушки под roof /
  wall / deck flashing с указателем на window-flashing.
- Дубль таблицы flashing-по-типам-стен в
  `docs/work/vertical/sheathing/exterior-materials.md` заменён на короткий
  указатель.
- `docs/work/vertical/openings/windows-doors.md` — первые секции переписаны
  нормальным русским; добавлена секция-указатель на window-flashing.
- `mkdocs.yml` — добавлена nav-запись `Window Flashing` под Openings.

### Дубликаты — устранены
- **Client Metal Rule.** Таблица была одновременно в
  `docs/reference/boss-feedback-rules.md:99-107` и
  `docs/start/client-rules.md:8-17`. Канонично — `client-rules.md`; в
  `boss-feedback-rules.md` оставлен короткий указатель.
- **Sill Sealer / Termite Shield / Washers.** Список был в
  `docs/work/vertical/walls/exterior.md:37-45` и
  `docs/work/vertical/walls/sill-plates.md:11-16`. Канонично —
  `sill-plates.md`; в `exterior.md` оставлен короткий указатель.

### Опечатки и битые анкоры — исправлены
- `docs/reference/boss-feedback-rules.md:137` — Confluence-якорь с заголовком
  `---:` переименован в человеческий `Разное (QA feedback)`.
- `docs/work/sheathing-and-misc/eve.md:129` — опечатка `Vinel Soffits`
  → `Vinyl Soffits`.

### Мешанина RU/EN — переписано
- `docs/work/vertical/walls/corridor.md:18-19` — правило про `DHU/DGU` поверх
  fire wall сформулировано чище.
- `docs/work/vertical/walls/demising.md:14-15` — то же про `ITS`,
  добавлена кросс-ссылка на `Corridor`.
- `docs/work/horizontal/floor-framing/joist.md:156` — «top chord bearing» с
  ribbon-board нюансом + ссылка на `details/ribbon.md`.
- `docs/work/horizontal/floor-framing/details/steelbeams.md:16` —
  top-mount vs face-mount hangers сказано явно.

---

## ⚠️ Открыто — требуют решения (нельзя выбрать сторону за тебя)

Все ниже — реальные противоречия / недосказанности. Я могу пофиксить, как
только подтвердишь, какая версия правильная.

### Фактические противоречия

1. **FRT-правило для parapets vs shear-wall sheathing.**
   - `docs/work/vertical/walls/parapet.md:11` говорит: «`Parapets = FRT`, когда
     `exterior walls = FRT`» — автоматически.
   - `docs/work/vertical/sheathing/shear-wall.md:14` говорит: на demising
     shear-wall sheathing FRT **не** автомат.
   - Правило одинаково для всех sheathing когда стена FRT, или зависит от
     роли элемента (cladding / shear / draft stop)?

2. **Rim factor `1.05` vs Blocking factor `1.1`.**
   - `docs/work/horizontal/floor-framing/details/rim.md:8`: rim factor `1.05`.
   - `docs/reference/formulas.md:18`: rim factor `1.05` ✓ совпадает.
   - `docs/work/horizontal/floor-framing/details/blocking.md` и
     `details/blockingoc.md` — blocking factor `1.1`.
   - Это разные factors для разных компонентов, или ошибка? Если разные —
     явно прописать на странице rim, почему он 1.05, а не 1.1.

3. **Zip sheathing — чей note приоритетнее.**
   - `docs/reference/material-catalog.md:57-58`: «Assumed per Structural;
     verify».
   - `docs/reference/ourplanecore.md:250` и
     `docs/reference/boss-feedback-rules.md:64-65`: «Zip на exterior walls
     перекрывает structural sheathing notes».
   - Какой источник в приоритете при конфликте?

4. **`ITS` hanger — депт-граница.**
   - `docs/work/horizontal/floor-framing/joist.md:138`: «`ITS` — только для
     light floor applications до 16"».
   - Пример в `joist.md:201` использует `ITS2.37/11.88` для 16" o.c. Это
     корректно (16" o.c. ≠ 16" depth) или конфликт? Уточнить определение
     «light floor».

5. **`TJI 9 1/2` — какие series.**
   - `docs/work/horizontal/floor-framing/joist.md:162`: «`TJI 9 1/2` does not
     use 360 / 560 series».
   - Какие series тогда применяются для `TJI 9 1/2`? Сейчас просто отрицание
     без позитивного ответа.

### Недосказано / нужны дефолты

6. **SQFT и overhangs.** Все 8 страниц в `docs/work/sqfts/*` не говорят:
   считать ли eave / soffit overhang в SQFT этажа? Только в `roof.md`
   упомянуты cantilevers. Нужно одно общее правило.

7. **Soffit: где порог «узкий» vs «широкий».**
   `docs/work/exterior-trims/soffit-fascia.md:15-16`: «узкий — `LFT`,
   широкий — `SQ FT`». Какая ширина — порог? `12"` / `24"` / другая?

8. **Furring — `LFT` или `SQ FT`.**
   `docs/work/exterior-trims/furring-and-jambs.md:26-29` говорит обоими
   способами, но не задаёт правило выбора (когда sparse → `LFT`, когда
   сплошной → `SQ FT`?). Стоит зафиксировать критерий.

9. **Sleepers — дефолтная толщина в слоях.**
   `docs/work/deck/deck-porch-balcony-frame.md:77` говорит «sleepers часто в
   2 слоя». `docs/work/deck/anchor-bolts.md` и
   `docs/work/exterior-trims/balcony-buildup.md` упоминают `2x4 P.T.`
   без указания слоёв. Какой дефолт — 1 или 2?

10. **`5/4x4 P.T.` blocking-jamb vs `2x4/2x8/2x10` structural jamb.**
    `docs/work/exterior-trims/macros.md:94` ставит `5/4x4 P.T.` jamb-блок,
    `docs/work/exterior-trims/furring-and-jambs.md:47-49` — `2x4/2x8/2x10`.
    Это разные элементы (blocking vs structural jamb) — стоит явно сказать,
    что это два разных скоупа.

### Незаконченный контент

11. **`docs/work-types/reconstruction.md`.** Страница помечена как
    «черновик без source». Сейчас контент шпаргалки есть, но без привязки к
    реальным project notes / feedback. Когда будет первый
    reconstruction-проект, перенести оттуда правила.

12. **`docs/work/horizontal/floor-framing/details/blockingoc.md`.** Формулы
    используют переменные `G` и `D` без определения. Нужно либо подписать,
    либо линковать на `docs/reference/formulas.md` где это определено.

---

## 🚫 Отвергнуто (ложные срабатывания агентов)

- `window-flashing.md:33` — претензия про несовместимость `flange` с
  `head/jambs`. Терминология верна: у виниловых/алюминиевых окон есть
  nailing flange, его и закрывают flashing'ом по head/jambs.
- `ourplanecore.md:24`, `excel-hotkeys.md:43-45` — агент перепутал файлы,
  цитируемый фрагмент про `Workbook_Open` находится в `excel-hotkeys.md:121`
  и читается нормально.
- `start/workflow.md:38-41` — «`waste`» как технический термин в норме
  для этой wiki.
- `vertical/walls/shaft.md:38-39`, `vertical/sheathing/box-sheathing.md:23` —
  предложения целые, не обрывы. Агент ошибся.
- `vertical/walls/corners.md` — есть контент (lines 7-22), `Source: redacted`
  на line 3 — обычное placeholder соглашение проекта.
- Массовые `redacted.atlassian.net` ссылки в `interior-trims/*`, `deck/*` и
  др. — это **проектное соглашение** (placeholder, не битость). Отдельная
  задача, если решишь переименовать или удалить.
- Дубль interior-trim rules в `boss-feedback-rules.md:91-97` ↔
  `quality-checklist.md:49-52` — текстуально это **разные** короткие списки
  (boss-feedback — правила, QA — чек-лист). Логически одна тема,
  но дублирования контента нет.
- Дубль stud-spacing factor в `formulas.md` и `boss-feedback-rules.md` —
  это **две формы одного факта** (`1.1` combined factor vs `1:1 + 10% waste`
  split), и `formulas.md:11-12` явно объясняет связь. Не дубль.

---

## TL;DR — что осталось решить

- 5 фактических противоречий (FRT, factors, Zip-приоритет, ITS depth,
  TJI 9 1/2 series) — нужно слово от тебя.
- 5 недосказанных правил (SQFT overhangs, soffit width threshold, furring
  unit, sleepers default ply, jamb 5/4x4 vs 2x) — нужны дефолты.
- 2 незаконченных страницы (`reconstruction.md` черновик,
  `blockingoc.md` переменные без определения) — нужен контент.

Скажи по каждому пункту, как должно быть — допишу пачкой.
