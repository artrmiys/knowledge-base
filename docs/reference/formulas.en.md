# Formulas and factors

Here: the multipliers and column C formulas used in the workbook, and how studs differ from joists. Formulas are given in the English locale (`CEILING`, `EVEN`); in other locales Excel shows localized function names with `;` between arguments, the meaning is the same.

## Legend { #legend }

The letters in the formulas are the columns of one DFL row. One row = one material item.

| Letter | What it is | Example |
| --- | --- | --- |
| `G` | The measurement from OurPlanCore: a line length in feet, an area in square feet, or a number of points. A grey column to the right of the table; it does not go into the order. `G` carries no waste: it is the bare measurement. | `G` = 186 (length of the exterior walls) |
| `H` | The second number of the row, also grey. Its meaning depends on the row: spacing in inches (hardware and blocking at a spacing), the number of plies for a label with `(n)` (plates, headers, rim), the wall height in feet (studs, shear walls). Each formula below says what `H` holds. | `H` = 48 (anchors at 48" o.c.) |
| `C` | The quantity to order. A formula of `G` (and `H`, `D`); the number is never typed by hand. | `=CEILING(G/D,1)` |
| `D` | The unit: `LFT`, `SQ FT`, `4x8`, `pcs`, `unit`, `tubes`. For lumber ordered by the piece (studs, joists, beams, posts, headers, rim, ribbon, blocking, ledger, bracing) `D` holds the board length in feet: 8, 10, 12, 14, 16. Then `C` is the number of boards and the formula divides by `D`. | `D` = 16 |
| `Stock LF` | The length of one ordered piece in feet, the same number as in `D`. Shaft channels usually come in 12. | 12 |
| `LFT`, `SQ FT` | Linear and square feet. Written exactly this way in `D`; `LF`, `SF`, `SQFT` are not used in `D`. | |

How a row is built and what the other columns hold: [How the DFL workbook works](dfl-overview.md).

!!! warning "Studs and joists use different tables"
    Studs and joists share the same `o.c.`, but the multipliers differ: studs follow the owner's rule (a stud per foot plus waste), joists follow geometry (`12 / spacing`). Do not mix up the tables.

## Stud spacing factors { #stud-spacing-factors }

The canon for studs. At `16" o.c.` count one stud per foot of wall plus 10 percent waste, not the geometric `0.75`: this covers corners, T-intersections, jack, king and cripple studs at openings, and cutoffs.

| Spacing | Factor (pcs / LFT) | Where it comes from |
| --- | ---: | --- |
| 12" o.c. | **1.4667** | 1:1 scaled 16 to 12 (x1.333) plus 10% waste |
| 16" o.c. | **1.1** | 1:1 plus 10% waste |
| 24" o.c. | **0.625** | 0.5 plus 25% waste |

- `pcs = wall LFT x factor`, in the workbook `=G*factor`.
- The height in the stud row (E, to 1/8") and in the wall name is the height of the assembled wall, plates included: floor-to-floor minus the `3/4"` subfloor, minus the floor depth. The one bottom and two top plates are **not deducted**: the template picks the stud, precut or full height, from this height. Deduct only extra boards beyond those three when the section shows them (a second bottom plate, blocking under trusses). The bare stud is `4 1/2"` shorter than the wall height. Stud selection table: [Exterior Walls](../work/vertical/walls/exterior.md#precut).
- Bearing walls as Extra: the main line with the regular factor, extra plies on a separate `double extra` row, subtract the base from the regular studs. Extra factors: `12" o.c.` 1, `16" o.c.` 0.75, `24" o.c.` 0.5 (without the base row's waste).
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

In the tree each of these details is one Line along the place where it applies; its length in feet goes to `G`. How the length becomes an order depends on the row and the job type.

| Row | Where | C | D |
| --- | --- | --- | --- |
| `Rim Board`, `Ribbon Board`, `Blocking`, `Blocking for Drywall`, `Ledger` | Floor and Roof Framing List of a regular workbook (Frame, COM, residential) | `=CEILING(G/D,1)` | `16` |
| `Rim Board (2)` | same, double rim | `=CEILING(G*H/D,1)`, H = 2 | `16` |
| `Rim Board` | EWP-only job (only engineered wood is counted) | `=CEILING(G*1.05,1)` | `LFT` |
| Continuous `Blocking` | EWP-only job | `G` with no factor | `LFT` |
| `Blocking` in walls | Floor Walls | `=EVEN(G)` | `LFT` |
| `Bracing Ext Walls`, `Bracing Corridor`, `Bracing Demising` | Floor Walls | `=G/8*1.1`: one board per 8 LFT of wall | board length by wall height |

- In a regular workbook the rim, ribbon, blocking and ledger rows are written by the `C_RimBoardBlockingHangers` macro: the quantity is in 16' boards. There is no separate factor; rounding up to a whole board is the waste.
- `1.05` is the rim factor on EWP-only jobs only: there rim stays in LFT and is not cut into pieces. If a client asks for rim in LFT on a regular job, the factor is `1.1`.
- Do not cut the line in the tree into 16' pieces: measure the whole length of the detail, the formula splits it into boards.
- Board length for wall bracing: wall up to 10' - `14`, up to 12' - `16`, up to 16' - `18`, taller - `20`. The formula in `D` of the template sets it from the tallest wall of the group. Walls under 7' get no bracing.
- Top chord bearing trusses: instead of a ribbon board, blocking between trusses, often `(2) 2x6`.
- Blocking at a spacing is counted in pieces: formulas below.

## Blocking formulas { #blocking-formulas }

Blocking at a spacing means short pieces between joists or trusses set at equal intervals along a line. `G` is the length of that line in feet, `H` the spacing in inches, `D` the board length (16).

```excel
Blocking 48" o.c., flat       = CEILING(G * 12 / H * 2 / D, 1)
Blocking 48" o.c., diagonal   = CEILING(G * 12 / H * 2.5 / D, 1)
Blocking btw trusses (n)      = CEILING(G / D, 1)        G = line length x number of rows n
T blocking at gables          = EVEN(G / D)
```

How to read the first formula: `G * 12 / H` is how many blocking points fit on the line; `2` is how many feet of board one point takes; that gives linear feet; `/ D` turns them into 16' boards. Example: a 96' line at 48": 96 x 12 / 48 = 24 points, 24 x 2' = 48 LFT, 48 / 16 = 3 boards.

### Blocking factor by type { #blocking-factor }

Feet of board per point:

| Type | Feet per point |
| --- | ---: |
| Flat | `2` |
| Diagonal | `2.5` |
| Vertical | `1.5` ... `2` |

The detail governs: if it shows a different number of pieces at a point, take the multiplier from the detail.

Walls 10' and taller get two rows of blocking. Kitchen: `2x6`, 4 pieces at 14' per kitchen; bath: 1 piece at 14' per bathroom. Kickers only where the detail shows them.

## Column C formulas by row type

| Row type | C | D |
| --- | --- | --- |
| 4x8 panels (sheathing, subfloor) | `=CEILING(G/32*1.1,1)` | `4x8` |
| Lumber by the piece at a board length (rim, ribbon, blocking, ledger, sub fascia) | `=CEILING(G/D,1)`: the length in feet divided by the board length | board length, usually `16` |
| Linear items not split into boards (flashing, tape, jambs, blocking in Wall Materials) | `=CEILING(G*1.1,10)`; under 50 - `=CEILING(G*1.1,2)` | `LFT` |
| Plates | `=EVEN(G*H*1.1)` (H = number of plates from the label: `(1) btm`, `(2) dbl top`) | `LFT` |
| Studs | `=G*1.1` at 16" o.c. (factor from the table above) | stud length: `8`, `9`, `10`, `12` |
| Hardware at a spacing (anchors, ties, hangers) | `=CEILING(G*12/H*1.1,2)` (H = spacing in inches); at 50 and more the template's own significance `,10` or `,1` | `pcs` |
| Screws at trusses | `=CEILING(...,3)` | `pcs` |
| Washers | `=C<anchor row>` or `=SUM(...)` as one row per group | `pcs` |
| H-clips | by decking thickness and support spacing: `PSCL at 16"` = 6 per sheet, not "4 per sheet"; not needed with T&G or with decking thicker than the spec threshold | `pcs` |
| `Bracing for Trusses` (floor trusses) | `2x6`; `=CEILING(G/D,1)`, `G` = length of the bracing lines in feet: one line across the trusses about every 10'; not over bearing walls and not where joists or rafters are stick or TJI (trusses only) | `16` |
| `Truss Bracing` (roof trusses) | `2x4`; `=CEILING(G/4/D,1)`, `G` = plan area under the roof trusses, garage included; a stick roof gets no row | `16` |
| Panel adhesive | `=CEILING(C<subfloor>/3,1)`: one tube per 3 subfloor sheets | `tubes` |
| Resilient channels | `=CEILING(area*12/spacing*1.1,10)`, only where the wall type shows them | `LFT` |
| Holdowns | `=G` to concrete, `=G*2` through a wood floor | `pcs` |
| Double-sided shear wall | G = sum of the two faces, no extra x2 | `4x8` |

### Truss bracing: where the numbers come from { #truss-bracing }

These are two different rows, counted in different ways.

- **Floor, `Bracing for Trusses`.** In the tree you draw the bracing lines themselves (strongbacks): `framing/<floor> framing/details/bft`, one line across the trusses about every 10' of span. Do not run a line over bearing walls. Where the floor is stick joists or TJI there is no bracing at all: only trusses need it. Example: truss span 28', two lines of 48' = 96 LFT; `=CEILING(96/16,1)` = 6 boards of `2x6` at 16'.
- **Roof, `Truss Bracing`.** No lines are drawn; take the plan area under the trusses: the 1st floor plus the garage and lower roofs when trusses sit over them too. `G/4` is the linear feet of bracing: one run for every 4' of truss length, so each square foot of plan takes 1/4 foot of board. `/D` turns it into 16' boards. Example: house 1,800 SQ FT and garage 440 SQ FT: 2,240 / 4 = 560 LFT, 560 / 16 = 35 boards of `2x4`.
- If bracing lines of the trusses under a flat roof are drawn and measured (`framing/roof framing/details/bft`), they go as a `Bracing for Trusses` row in the Roof Frame list, and the area row is not needed for those trusses. Never count the same thing twice.

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
| Rows in `LFT` and `SQ FT` | `G*1.1` rounded up: under 50 to an even number, 50 and more to 10 |
| Lumber, panels, pipes | whole numbers, rounded up; `2.75` and `9.6` never appear in C |
| Waste | once, in the `C` formula. `G` carries no waste |

## Shaft Walls { #shaft-walls }

Shaft walls go in a separate block, even when the building walls are panels by others. Material from the wall type and the detail: it can be `2-1/2"` CH + J-channel or `2"` H + C-channel. The two systems are never mixed in one wall.

Panels and vertical channels are counted from the wall **area**, horizontal channels from the length:

- `Area` (the `G` of the panel and vertical channel rows) = length of the shaft walls x height, summed over the floors, in SQ FT;
- `24` = the area of one `2' x 12'` panel; E of the row says `2x12 Panels`;
- `0.5` = a vertical channel every 24": one per 2' of wall, as tall as the wall;
- `Run LFT` = length of the shaft walls; `x 2` is the channel at the top and the bottom on every floor;
- `Stock LF` = length of one piece, usually 12 (it sits in `D`).

```excel
2-1/2" CH + J (shaft, panels on one side):
Linear Panels, 1" Shaft Panels   = CEILING(Area * 1.1 / 24, 2)
CH Channels Vertical             = CEILING(Area * 0.5 * 1.1 / Stock LF, 2)
J Channels Horizontal            = CEILING(Run LFT * 2 * 1.1 / Stock LF, 2)

2" H + C (area separation wall, panels on both sides):
Linear Panels, 2 layers          = CEILING(Area * 2 * 1.1 / 24, 2)
Channels Vertical (H)            = CEILING(Area * 0.5 * 1.1 / Stock LF, 2)
Channels Horizontal (H)          = CEILING(Run LFT * 2 * 1.1 / Stock LF, 2)
Channels Perimeter (C)           = CEILING(Perimeter LFT * 1.1 / Stock LF, 2)
```

Example: a 64 LFT shaft, 10.5' high. Area 64 x 10.5 = 672 SQ FT. Panels: 672 x 1.1 / 24 = 30.8, so 32 panels. CH: 672 x 0.5 x 1.1 / 12 = 30.8, so 32 pieces of 12'. J: 64 x 2 x 1.1 / 12 = 11.7, so 12 pieces.

!!! danger "Do not divide the wall length by 24"
    If you put the length (64 LFT) into the panel formula instead of the area, you get 4 panels instead of 32: the shortfall equals the wall height in feet.

Dropped ceiling metal joists: `12" C-type = Area * 0.75 * 1.1`, in LFT.

## Order-of-magnitude check

If a number looks odd, compare it with what is typical for a similar building: [Quantity benchmarks](quantity-benchmarks.md). This is a sanity check, not a norm; a discrepancy means "open the detail and the units", not "fix it to the average".

## See also

- [How the DFL workbook works](dfl-overview.md), [DFL row labels](takeoff-items.md), [Tips and key rules](boss-feedback-rules.md)
- [Joist](../work/horizontal/floor-framing/joist.md), [Rim Board](../work/horizontal/floor-framing/details/rim.md), [Blocking](../work/horizontal/floor-framing/details/blocking.md), [Shaft](../work/vertical/walls/shaft.md)
