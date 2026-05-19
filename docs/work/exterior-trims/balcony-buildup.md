# Balcony build-up

Balcony — это не одна строка trim, а **полная сборка**: от structural framing
снизу до finish сверху. Этот порядок зашит в balcony-template макрос
(`B_Balcony_Insert_Template_FromText`) — он вставляет весь блок целиком.

!!! info "Template-макрос"
    Вставляется командой `b 12x30` (ширина × длина) или `b 1.3x1.9 u2`
    (×2 units). Defaults: beam `2x10 P.T.`, posts `6x6 P.T.`, OC `16"`.
    Подробно — [Trim macros](macros.md). Ниже — что именно он раскладывает.

## Полная сборка снизу вверх { .kb-section-title .kb-st--green }

| # | Label | Типовой материал | Unit |
| --- | --- | --- | --- |
| 1 | `Posts` | `6x6 P.T.` (default) | `pcs` + высота |
| 2 | `Post Bases` | `ABU66 Zmax` | `pcs` |
| 3 | `Post Caps` | `BCS2-3/6 Zmax` | `pcs` |
| 4 | `Post Wrap` | `1x` / `5/4x` | `LFT` |
| 5 | `Beam (…)` | `2x10 P.T.` (plate1 ×3 + plate2 ×2 ply) | `LFT` |
| 6 | `Ledger` | `2x10 P.T.` к стене | `LFT` |
| 7 | `Box` | `2x10 P.T.` периметр | `LFT` |
| 8 | `Joists` | `2x10 P.T.` / `2x12 P.T.` @ 16" o.c. | `LFT` / `pcs` |
| 9 | `Hangers` | `LUC26`, `LUS28` | `pcs` |
| 10 | `Subfloor` | `3/4" CDX Ply` `4x8` | `4x8` / `SQ FT` |
| 11 | `Sleepers` | `2x4 P.T.` (часто **two layers**) | `LFT` |
| 12 | `EPDM` | `EPDM` membrane | `SQ FT` |
| 13 | `Decking` | `5/4x6` (Composite / Azek / Wd) | `SQ FT` |
| 14 | `Treads` / `Stringers (4)` | по детали | `LFT` / `pcs` |
| 15 | `Soffits at Balcony` | `Beadboard` | `SQ FT` |
| 16 | `Balcony Trims` | fascia / edge trim `1x` / `5/4x` | `LFT` |
| 17 | `Flashings at Wall` | `Copper` / drip edge | `LFT` |

!!! warning "Не прячь framing в trim"
    Beam / Ledger / Box / Joists / Hangers / Subfloor / Sleepers — это
    **structural**, отдельные строки. Они не должны раствориться в
    `Balcony Trims`. Trim — это только soffit, fascia, edge trim, flashing.

## Beam: plate1 + plate2 { .kb-section-title .kb-st--cyan }

Balcony beam в шаблоне — это **multi-ply**: `plate1` (default 3 ply) +
`plate2` (default 2 ply), материал `2x10 P.T.` (или `2x12 P.T.`).

- Пиши ply явно: `(3)2x10 P.T.` + `(2)2x10 P.T.`.
- `Note: Assumed Balcony Joists are 2x10 P.T. per structural; per S664 2x8
  P.T.; verify` — типичное противоречие, оставляй note.

## Sleepers: часто два слоя { .kb-section-title .kb-st--magenta }

Под decking на balcony идут **sleepers** (`2x4 P.T.`), нередко **в два
слоя** (cross-sleepers для уклона/дренажа). Считай оба слоя, держи note.

- `Note: balcony framing requires 2-ply framing and two layers of sleepers`
  — держи видимым (см. [Balcony Trims](../deck/balcony-trims.md)).

## Composition (paver-вариант) { .kb-section-title .kb-st--green }

Если balcony не deck-on-sleepers, а **paver on membrane** — слои сверху вниз:

| Слой | Что это | Scope |
| --- | --- | --- |
| `Porcelain Pavers` | финиш | часто **by others** |
| `Thinset Mortar` | клей | by others с pavers |
| `Roofing Membrane` | гидроизоляция | проверь scope |
| `Tapered Rigid Insulation` | разуклонка | проверь scope |
| `Conc. Deck` | плита | structural |
| `Structural Steel` | каркас | structural — не trim |

!!! danger "Pavers / membrane часто by others"
    `Note: Pavers Deck System are by others`. Тогда из composition считаем
    только наш framing/trim, paver-систему — нет. Это то же правило
    исключений: [Exclusions](exclusions.md).

## Чек перед выводом { .kb-section-title .kb-st--cyan }

- [ ] Полная сборка: posts/bases/caps → beam → ledger/box → joists/hangers →
      subfloor → sleepers → EPDM → decking → soffit/trim/flashing?
- [ ] Beam multi-ply (plate1+plate2) посчитан с явным `(n)`?
- [ ] Sleepers — оба слоя, если two layers?
- [ ] Joists P.T. size взят из structural (2x10/2x12/2x8 — противоречия в note)?
- [ ] Hangers (`LUC26`/`LUS28`) посчитаны по joists?
- [ ] Composition: pavers/membrane — by others проверено?
- [ ] Trim (soffit/fascia/edge/flashing) отделён от structural?

## See also

- [Porch / Deck / Balcony](porch-deck-balcony.md)
- [Rails & Decking](rails-decking.md)
- [Trim macros](macros.md)
- [Balcony Trims](../deck/balcony-trims.md) · [Hangers](../../reference/hangers.md)
- [Standard notes](../../reference/standard-notes.md)
