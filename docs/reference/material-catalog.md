# Material catalog

Сводная номенклатура материалов из takeoff-воркбука (лист `Mat List`),
сгруппированная по семействам. Здесь **только размеры и сорта** — без
SKU/кодов поставщика (это внутренние данные, в публичную базу не идут).

!!! note "Зачем эта страница"
    Чтобы writing/output совпадал с тем, как материал называется в workbook
    и в заказе. Размер всегда видим: `2x10x16' PT SYP`, `1 3/4 x 11 7/8 LVL`,
    `4x8x3/4 CDX`. Никогда не сворачивай к generic `lumber` / `trim`.

## Dimensional lumber { .kb-section-title .kb-st--green }

| Семейство | Размеры (nominal) | Длины | Где |
| --- | --- | --- | --- |
| **PT SYP** (pressure-treated southern yellow pine, ACQ .25) | `2x4` `2x6` `2x8` `2x10` `2x12`, `4x4` `4x6` `6x6` | `8'`–`24'` | низ/влажно: sills, deck, balcony, ledger, furring P.T. |
| `2x2 PT Clear` (ACQ) | `2x2` | `8'` | ballusters, мелкое P.T. |
| **D Fir** (Douglas fir #2 & Btr) | `2x4` `2x6` `2x8` `2x10` `2x12` | `8'`–`20'` | основное framing |
| `4x4 D Fir S4S` | `4x4` | `8'` | posts |
| **D Fir studs** (precut) | `2x4` / `2x6` × `92-5/8` `104-5/8` `116-5/8` | precut | walls 8'/9'/10' |
| **KD D Fir studs** (kiln-dried #2) | `2x4` / `2x6` × `92-5/8` `116-5/8` | precut | где требуется KD |

- `ACQ .25` / `.40` — класс пропитки P.T.; `.40` обычно для `4x4` posts.
- Precut studs `92-5/8` ≈ 8' wall, `104-5/8` ≈ 9', `116-5/8` ≈ 10'.

## Engineered lumber (EWP) { .kb-section-title .kb-st--cyan }

!!! warning "EWP часто by others"
    `Note: All EWP products are by others` / `EWP Floor system are by others`
    — встречается постоянно. Если так — EWP **не считаем**, но фиксируем
    видимой note. См. [Standard notes](standard-notes.md).

| Семейство | Сечения | Длины | Назначение |
| --- | --- | --- | --- |
| **Timberstrand (TS) LSL stud** | `1½×3½`, `1½×5½` | `116-5/8`, `12'`, `16'` | прямые studs/posts |
| **LSL** (1.55E) | `1½×` `3½`/`5½`/`7¼`/`9¼`/`10½`/`11¼`/`11½`, `1¾×` `11⅞`/`14` | `16'`–`24'`, RL | studs, beams |
| **LSL Rim Board (RB)** 1.3 | `1¼×` `9½`/`11⅞`/`14`/`16`/`18`/`20`, `1¼×11⅞ TS RB` | `16'` | rim board |
| **LVL ML** (1¾ thick) | depth `5½`,`7¼`,`9¼`,`9½`,`11¼`,`11⅞`,`14`,`16`,`18`,`20`,`22`,`24` | `10'`–`48'`, RL | beams, headers, posts (built-up) |
| **I-joists** | `BCI`, `TJI`, `LPI`, `RED-I`, `TriForce OJ` — `9½`,`11⅞`,`14`,`16`,`18` | per page | floor/roof joists |
| **PSL** | напр. `5½ x 11⅞ PSL` (typ interior beam) | per spec | тяжёлые beams |

- `RL` = random length. Multi-ply LVL/LSL пиши как `(2)`/`(3)` ply.
- I-joist серия (`TJI 230`, `BCI 6000`, `LPI 20 PLUS`, `RED-I45`) — это
  product line; держи серию в Label, не сводить к «I-joist».

## Sheathing & subfloor { .kb-section-title .kb-st--magenta }

| Материал | Толщины | Формат |
| --- | --- | --- |
| **CDX FIR** sheathing | `1/2`, `5/8`, `3/4` | `4x8` |
| **Advantech** T&G / SE underlayment | `3/4` T&G, `5/8` SE | `4x8` |
| **Zip** wall/roof + Zip Tape | `7/16`, `1/2`, `5/8`, R-6 | `4x8` / rolls |
| **OSB** | `7/16`, `15/32`, `1/2`, `5/8` | `4x8` |
| **Plywood / Ply** | `1/2`, `5/8`, `3/4` | `4x8` |
| Specialty gypsum/board | `1/2` Durock, `1/2` FRT, `1/2` MR, `5/8` Densglass, Shaft/Liner panels | sheet |

- На плане Arch и Structural часто **противоречат** по sheathing — оставляй
  note `Assumed per Structural; verify` (см. [Standard notes](standard-notes.md)).

## Accessories { .kb-section-title .kb-st--green }

| Материал | Размеры |
| --- | --- |
| **Sillsealer** | `1/2 x 4` / `x6` / `x8` / `x10` (рулоны 50') |
| **Sill** trim | `1"`, `1-1/2"`, `2"` |
| Insulation (rigid / R-value) | `1"` R3.5/R6.0/R6.6, `1-1/2"`, `2"` rigid; tapered |
| Membrane | `EPDM`, Tyvek, Ice & Water, Felt 15# |

## Trim / decking / rail families { .kb-section-title .kb-st--cyan }

Детально — в разделе Exterior Trims; здесь свод размеров:

| Группа | Типовые размеры |
| --- | --- |
| Casing / band / corner / watertable | `5/4x3` `5/4x4` `5/4x6` `5/4x8` `5/4x10` `5/4x12`; vinyl `3-1/2"` / `4"` |
| Fascia / soffit / frieze | fascia `1x6`–`1x12`/`2x8`; soffit `1x` / vinyl vented / beadboard / panel; frieze `5/4x6`–`5/4x10` |
| Crown / moulding | `2"`, `3"`, `3-1/2"`, `4"`, `5"`, `5-1/2"` crown; `1x4` crown cap |
| Decking | `5/4x6` (Wd/Azek/Trex/Composite), `5/4x4 T&G Mahogany`, `1x6 T&G Red Cedar` |
| Rail | `2x2` ballusters, `1x3`/`2x4` rails, `2x4`/`2x6`/`5/4x6` cap rail, cable SS, metal subrail |
| Columns / posts | `4x4` PT post, Fbg/synthetic `Dia`/`SQ` taper/non-taper `w/c&b` |
| IPE (open structure) | `1x4`/`1x6` slats, `5/4 IPE Cap`, `5/4 IPE Jambs`, `4x4 IPE` posts |

## See also

- [Standard notes](standard-notes.md)
- [Takeoff item labels](takeoff-items.md)
- [Exterior Trims → Overview](../work/exterior-trims/overview.md)
- [Hangers](hangers.md) · [Formulas and factors](formulas.md)
