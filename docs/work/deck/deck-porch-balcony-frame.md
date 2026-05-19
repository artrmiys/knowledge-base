# Deck / Porch / Balcony Frame

Здесь — **структурный каркас** deck / porch / balcony: ledger, box, beams,
posts + hardware, joists, hangers, blocking, rim, sleepers, structural
subfloor, stair stringers.

!!! abstract "Frame vs Trim — где что"
    - **Frame (эта страница)** — несущее: posts, beams, ledger, box, joists,
      hangers, blocking, rim, sleepers, structural subfloor.
    - **Finish / trim** — decking finish, soffit, fascia, edge trim, flashing,
      lattice, railing finish: [Exterior Trims → Balcony build-up](../exterior-trims/balcony-buildup.md)
      и [Rails & Decking](../exterior-trims/rails-decking.md).
    - **Railing structural** (posts/blocking/bolts) — здесь; railing finish — в trim.

## Сборка каркаса снизу вверх { .kb-section-title .kb-st--green }

| # | Label | Типовой материал | Unit |
| --- | --- | --- | --- |
| 1 | `Posts` | `6x6 P.T.` (default) / `4x4 P.T.` | `pcs` + высота |
| 2 | `Post Bases` | `ABU66 Zmax` (под post size) | `pcs` |
| 3 | `Post Caps` | `BCS2-3/6 Zmax` | `pcs` |
| 4 | `Beam (…)` | `2x10 P.T.` / `2x12 P.T.`, multi-ply | `LFT` |
| 5 | `Ledger` | `2x10 P.T.` к house wall | `LFT` |
| 6 | `Box` | `2x10 P.T.` периметр | `LFT` |
| 7 | `Joists` | `2x10 P.T.` / `2x12 P.T.` @ `16" o.c.` | `LFT` / `pcs` |
| 8 | `Hangers` | `LUC26`, `LUS28` (под joist) | `pcs` |
| 9 | `Blocking` | `2x` между joists | `LFT` |
| 10 | `Rim` / `Rim Board` | `2x` P.T. по периметру | `LFT` |
| 11 | `Sleepers` | `2x4 P.T.` (часто **2 слоя**) | `LFT` |
| 12 | `Subfloor` (structural) | `3/4" CDX Ply` | `4x8` / `SQ FT` |
| 13 | `Stringers (4)` / `Treads` | `2x12` stringers, tread stock | `pcs` / `LFT` |
| 14 | `Anchor Bolts` / `Washers` / `Nuts` | per detail | `pcs` |

!!! warning "Frame не прячь в trim"
    Эти строки — отдельный structural scope. Они **не** должны раствориться
    в `Balcony Trims` / `Decking`. Trim — только finish (soffit/fascia/edge/
    flashing/decking finish).

## Beam: multi-ply P.T. { .kb-section-title .kb-st--cyan }

Deck/balcony beam обычно **многослойный** P.T.: в balcony-template это
`plate1` (default 3 ply) + `plate2` (default 2 ply), материал `2x10 P.T.`
(или `2x12 P.T.`).

- Пиши ply явно: `(3)2x10 P.T.` + `(2)2x10 P.T.`.
- `Note: Assumed Balcony Joists are 2x10 P.T. per structural; per S664 2x8
  P.T.; verify` — типичное противоречие, оставляй note видимой.
- Общая логика beam (mark top-down, длины ≥8' к 2', built-up sizes) —
  [Floor Framing → Beam](../horizontal/floor-framing/beam.md).

## Posts + hardware (всегда набором) { .kb-section-title .kb-st--magenta }

| Label | Пример | Unit |
| --- | --- | --- |
| `Posts` | `6x6 P.T.`, `4x4 P.T.` | `pcs` + высота |
| `Post Bases` | `ABU66 Zmax`, `Post base for 4x4` | `pcs` |
| `Post Caps` | `BCS2-3/6 Zmax`, `Cap for …` | `pcs` |
| `Post Anchors` | `DTT2Z` | `pcs` |
| `Post Blocking` | `2x` усиление под post | `LFT` |

- Post почти всегда тройка: **post + base + cap** (часто + anchor/blocking).
- Railing posts structural (`4x4 P.T.` + sleeve/cap) — см.
  [Railing](railing.md); finish-перила в trim ([Rails & Decking](../exterior-trims/rails-decking.md)).

## Joists / hangers / blocking / rim { .kb-section-title .kb-st--green }

- `Joists` `2x10`/`2x12 P.T.` @ `12"/16"/19.2"/24" o.c.` — держи o.c. в Label.
- `Hangers` (`LUC26`, `LUS28`, `LU…`) подбираются под joist; см.
  [Hangers](../../reference/hangers.md).
- `Blocking` между joists; `Rim` / `Rim Board` по периметру (P.T. для
  deck/balcony). Общие правила — [Floor Framing → Joist](../horizontal/floor-framing/joist.md),
  [Rim Board](../horizontal/floor-framing/details/rim.md),
  [Blocking](../horizontal/floor-framing/details/blocking.md).

## Sleepers — часто 2 слоя { .kb-section-title .kb-st--cyan }

Под decking на balcony — **sleepers** (`2x4 P.T.`), нередко **в два слоя**
(cross-sleepers для уклона/дренажа). Считай оба слоя, держи note
`two layers of sleepers`.

## Anchor bolts / attachment { .kb-section-title .kb-st--magenta }

Ledger-to-wall и post-to-foundation крепёж — отдельный scope:

- Стандартный bolt (если не указан другой) — `5/8" Dia Titen HD x 5 1/2"`,
  `3 1/2" Emb`. Шаг — по детали; держи `Washers`/`Nuts` синхронно.
- Полные правила — [Anchor Bolts](anchor-bolts.md) (не copy/paste spacing).
- Вставка блока Blocking+Bolts+Washers+Nuts — макрос `B_BoltsAdd`
  ([Excel macro hotkeys](../../reference/excel-hotkeys.md)).

## Макросы для frame { .kb-section-title .kb-st--green }

| Макрос | Что вставляет/делает |
| --- | --- |
| `B_Balcony_Insert_Template_FromText` | полный balcony-каркас по `b 12x30` / `b 1.3x1.9 u2` (defaults beam `2x10 P.T.`, posts `6x6 P.T.`, OC `16"`) |
| `B_FrameOC_InsertOneRow` | вставляет одну frame-OC строку под выделенной |
| `B_Plate2_InsertOneRow` | вставляет одну Plate2-строку |
| `B_BoltsAdd` | Blocking + Anchor Bolts + Washers + Nuts |
| `C_JoistsSort` / `C_BeamsSort` / `C_RimBoardBlockingHangers` | сорт/раскладка joists/beams/rim+blocking+hangers |
| `Fame_only` | удаляет finish/trim-блоки, оставляет только frame |

Подробно — [Excel macro hotkeys](../../reference/excel-hotkeys.md) и
[Trim macros](../exterior-trims/macros.md).

## Чек перед выводом { .kb-section-title .kb-st--cyan }

- [ ] Полный каркас: posts/bases/caps → beam(multi-ply) → ledger/box →
      joists @ o.c. / hangers → blocking → rim → sleepers → structural subfloor → stringers?
- [ ] Beam ply явно `(n)`; P.T. size из structural (противоречия в note)?
- [ ] Posts = post + base + cap (+ anchor/blocking)?
- [ ] Hangers подобраны под joist size?
- [ ] Sleepers — оба слоя, если two layers?
- [ ] Anchor bolts/washers/nuts по детали, spacing не copy/paste?
- [ ] Frame отделён от finish/trim (не в `Decking`/`Balcony Trims`)?

## See also

- [Exterior Trims → Balcony build-up](../exterior-trims/balcony-buildup.md) (finish/trim слои)
- [Rails & Decking](../exterior-trims/rails-decking.md) · [Railing](railing.md) · [Anchor Bolts](anchor-bolts.md) · [Balcony Trims](balcony-trims.md)
- Floor Framing: [Beam](../horizontal/floor-framing/beam.md) · [Joist](../horizontal/floor-framing/joist.md) · [Post](../horizontal/floor-framing/post.md) · [Rim Board](../horizontal/floor-framing/details/rim.md) · [Blocking](../horizontal/floor-framing/details/blocking.md)
- [SQFT: Deck](../sqfts/deck.md) · [Porch](../sqfts/porch.md) · [Balcony](../sqfts/balcony.md)
- [Hangers](../../reference/hangers.md) · [Standard notes](../../reference/standard-notes.md)
