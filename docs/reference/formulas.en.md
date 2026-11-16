# Formulas and factors

Here: the multipliers and column C formulas used in the workbook, and how studs differ from joists. Formulas are given in the English locale (`CEILING`, `EVEN`); in other locales Excel shows localized function names with `;` between arguments, the meaning is the same.

!!! warning "Studs and joists use different tables"
    Studs and joists share the same `o.c.`, but the multipliers differ: studs follow the owner's rule (a stud per foot plus waste), joists follow geometry (`12 / spacing`). Do not mix up the tables.

## Stud spacing factors { #stud-spacing-factors }

The canon for studs. At `16" o.c.` count one stud per foot of wall plus 10 percent waste, not the geometric `0.75`: this covers corners, T-intersections, jack, king and cripple studs at openings, and cutoffs.

| Spacing | Factor (pcs / LFT) | Where it comes from |
| --- | ---: | --- |
| 12" o.c. | **1.4667** | 1:1 scaled 16 to 12 (x1.333) plus 10% waste |
| 16" o.c. | **1.1** | 1:1 plus 10% waste |
| 24" o.c. | **0.625** | 0.5 plus 25% waste |

- `pcs = wall LFT x factor`; stud height in column E of the row, to 1/8" (floor-to-floor minus subfloor, minus floor framing, minus plates).
- Bearing walls as Extra: the main line with the regular factor, extra plies on a separate `double extra` row, subtract the base from the regular studs. Extra factors: `16" o.c.` 0.75, `24" o.c.` 0.5 (without the base row's waste).
- A double wall = two frames only if the plan shows two frames; staggered corridor 2x4 = two rows at 16" o.c., 2x6 plates.

## Joist spacing factors

Joists, rafters and floor trusses follow the true center-to-center geometry, with no stud waste.

| Spacing | Factor (pcs / LFT of width) |
| --- | ---: |
| 12" o.c. | **1.0** |
| 16" o.c. | **0.75** |
| 19.2" o.c. | **0.625** |
| 24" o.c. | **0.5** |

- `pcs = span width LFT x 12 / spacing + 1` (an end joist for each run).
- From OurPlanCore, joists come as "count / length" pairs from J Area: identical lengths are added together, a length over 8' that is odd gets +1 (the `C_JoistsSort` rule); short ones up to 7' go onto a double-length board (`90 x 6'` = `45 x 12'`, E shows `90 pcs 6'`). Extra joists of the same length are added to the main row.
- Hangers for joists: at both ends of each joist, by assembly; piece hardware under 50 rounds to an even number.

## Rim, ribbon, blocking, ledger

| Item | Unit | Factor |
| --- | --- | --- |
| Rim Board, EWP jobs | LFT | `1.05` |
| Rim Board, other jobs (residential, COM) | LFT | `1.1` |
| Blocking, Ribbon, Ledger, Blocking for Drywall, bracing along walls | LFT | `1.1` once in the formula |

- Rim and blocking stay in LFT and are not divided into 16' pieces, unless the output explicitly requires pcs.
- Top chord bearing trusses: instead of a ribbon board, blocking between trusses, often `(2) 2x6`.
- Blocking at spacing is counted in pieces: formulas below.

## Blocking formulas { #blocking-formulas }

```excel
Flat 48" o.c.          = CEILING(LFT * 12 / 48 * 2 * 1.1 / Stock LF, 1)
Diagonal 48" o.c.      = CEILING(LFT * 12 / 48 * 2.5 * 1.1 / Stock LF, 1)
Blocking btw trusses   = CEILING(G * 12 / 48 * 2 / D * 1.1, 1)
T blocking at gables   = EVEN(G / D)
```

### Blocking factor by type { #blocking-factor }

| Type | Pieces per bay factor |
| --- | ---: |
| Flat | `2` |
| Diagonal | `2.5` |
| Vertical | `1.5` ... `2` |

Walls 10' and taller get two rows of blocking. Kitchen: `2x6`, 4 pieces at 14' per kitchen; bath: 1 piece at 14' per bathroom. Kickers only where the detail shows them.

## Column C formulas by row type

| Row type | C | D |
| --- | --- | --- |
| 4x8 panels (sheathing, subfloor) | `=CEILING(G/32*1.1,1)` | `4x8` |
| Linear stock by stock length | `=CEILING(G/D,1)` (D = 14 or 16) | `LFT` |
| Plates | `=EVEN(G*H*1.1)` (H = number of plates) | `LFT` |
| Studs | `=CEILING(G*1.1,1)` at 16" o.c. | `pcs` |
| Hardware at spacing (anchors, ties, hangers) | `=CEILING(G*12/H*1.1,2)`; at 50 and more the template's own significance `,10` or `,1` | `pcs` |
| Screws at trusses | `=CEILING(...,3)` | `pcs` |
| Washers | `=C<anchor row>` or `=SUM(...)` as one row per group | `pcs` |
| H-clips | by decking thickness and support spacing: `PSCL at 16"` = 6 per sheet, not "4 per sheet"; not needed with T&G or with decking thicker than the spec threshold | `pcs` |
| Truss bracing | `2x6` by default, a row every 10'; `=CEILING(G/4/D,1)` over the whole area under the roof, including the garage | `pcs` |
| Panel adhesive | `=C<subfloor>/3` | `tubes` |
| Resilient channels | `=CEILING(area*12/spacing*1.1,10)`, only where the wall type shows them | `LFT` |
| Holdowns | `=G` to concrete, `=G*2` through a wood floor | `pcs` |
| Double-sided shear wall | G = sum of the two faces, no extra x2 | `SQ FT` |

Formulas look at their own block: their own header, their own unit multiplier, their own floor. A copied floor with references into another block is the most common workbook mistake.

## Roofing

The pitch is applied once: plan area x `sqrt(1 + (rise/12)^2)`.

| Pitch | Factor |
| --- | ---: |
| 4/12 | 1.054 |
| 6/12 | 1.118 |
| 8/12 | 1.202 |
| 12/12 | 1.414 |

Pitch from the sheet, each building has its own (garage 4/12 with the house at 6/12). The number in the name `rf 6` is the rise per 12.

## Rounding

| What | Rule |
| --- | --- |
| Piece hardware under 50 | up to an even number (significance 2) |
| 50 and more | template significance: `,10` for large ties and screws, `,1` for panels and strips |
| Lumber, panels, pipes | whole numbers, rounded up; `2.75` and `9.6` never appear in C |
| Waste | once: if G already includes 1.1, C has no second 1.1 |

## Shaft Walls { #shaft-walls }

Shaft walls go in a separate block, even when the building walls are panels by others. Material from the wall type and the detail: it can be `2-1/2"` CH + J-channel or `2"` H + C-channel. `Stock LF` is usually 12; panels in the worksheet as `2x12 Panels`.

```excel
2-1/2" CH + J:
1" Shaft Panels        = CEILING(LFT * 1.1 / 24, 2)
CH-channels vertical   = CEILING(LFT * 0.5 * 1.1 / Stock LF, 2)
J-channels horizontal  = CEILING(Horizontal LFT * 1.1 / Stock LF, 2)

2" H + C:
1" Shaft Panels, 2 layers = CEILING(LFT * 2 * 1.1 / 24, 2)
H-channels vertical       = CEILING(LFT * 0.5 * 1.1 / Stock LF, 2)
H-channels horizontal     = CEILING(Horizontal LFT * 2 * 1.1 / Stock LF, 2)
C-channels perimeter      = CEILING(Perimeter LFT * 1.1 / Stock LF, 2)
```

Dropped ceiling metal joists: `12" C-type = Area * 0.75 * 1.1 LF`.

## Order-of-magnitude check

If a number looks odd, compare it with what is typical for a similar building: [Quantity benchmarks](quantity-benchmarks.md). This is a sanity check, not a norm; a discrepancy means "open the detail and the units", not "fix it to the average".

## See also

- [How the DFL workbook works](dfl-overview.md), [DFL row labels](takeoff-items.md), [Tips and key rules](boss-feedback-rules.md)
- [Joist](../work/horizontal/floor-framing/joist.md), [Rim Board](../work/horizontal/floor-framing/details/rim.md), [Blocking](../work/horizontal/floor-framing/details/blocking.md), [Shaft](../work/vertical/walls/shaft.md)
