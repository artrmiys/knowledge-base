# DFL row labels (Labels) and format

Here: what a row is called in column A, what goes in the other columns, and which labels are canonical. The label comes from the template (the `Standarts` worksheet), because macros sort and sum rows by their text, and the reviewer looks for an item by a familiar name.

## Row format

| Column | Rule | Example |
| --- | --- | --- |
| A | label from the dictionary below; spacing, plies and purpose go in the label | `Studs Ext 16" o.c.`, `Plates Ext (2) dbl top`, `Beam (3) Flush` |
| B | size or model; P.T., FRT, grade after the size | `2x6 P.T.`, `2x10 FRT`, `(2) 1 3/4 x 11 7/8 LVL`, `11-7/8" TJI 210`, `LUS210 Zmax` |
| C | formula from G and H of its own block | `=EVEN(G33*H33*1.1)` |
| D | unit: `LFT` (not `FT`), `SQ FT` (not `SF`), `4x8`, `pcs`, `unit`, `tubes`, `50' rolls`. For lumber by the piece (studs, joists, beams, posts, headers, rim, ribbon, blocking in a framing list, ledger, bracing) the board length in feet; C is then the number of boards | `LFT`, `16` |
| E | sheet or detail, SW mark, stud height, purpose; inches with the `"` sign | `8/S3.0`, `SW-2`, `9' 1 1/8"`, `for Ext Walls` |
| G | the measurement from OurPlanCore with no waste: area for panels, length for lumber and linear items, number of points for piece items | `3760` |
| H | spacing in inches, plies, height; which one depends on the row: [Formulas](formulas.md#legend) | `16`, `2` |

- `(n)` at the end of a label is the number of plies in one place. C counts every board: places x n. `Beam (3)` with two beams on the plan = 6 in C; `Dbl Rafters` = places x 2. In the tree one built-up beam is one point, not n points.
- The label matches the calculation: `Plates (2)` with H = 1, and `Posts (3)` when the detail has one post, are mistakes.
- A different grade or material goes on a separate row: if six of 18 2x12 boards are MSR 1650f-1.5E, they get their own row.
- Caps, bases, hangers, ties, bolts in `pcs`. Rim, ribbon, blocking, ledger in the framing list of a regular workbook are 16' boards: C `=CEILING(G/D,1)`, D `16`. They stay in `LFT` only on an EWP-only job; blocking in walls and in `Wall Materials` is always `LFT`. In the tree the detail line is never cut into pieces.
- Floors: `1st`, `2nd`, `3rd`, `4th`; the floor above the last full floor is `Loft`. `Schedule`, not `Shedule`; models without typos (`SDWS`, `PC6Z`, `MPB66`).
- A copied block: labels, E and references in C corrected for the new floor.

## Rounding

| What | Rule |
| --- | --- |
| Piece hardware, result under 50 | up to an even number: `=CEILING(G*12/H*1.1,2)` |
| Piece hardware, 50 and more | the template's own significance (`,10` for large ties and screws, `,1` for panels) |
| Screws at trusses | 3 per point: `=CEILING(...,3)` |
| Lumber, panels, pipes | whole numbers, rounded up; `2.75` and `9.6` never appear in C |

## Label dictionary

The canon is the `Standarts` worksheet. Below are the most needed groups. Variants in parentheses are filled in as needed: `(2)`, `(3)` plies, spacing `16" o.c.`, purpose `Ext`, `Int`, `Corr`, `Demising`.

### Section headers

`Foundation Walls`, `Basement Floor Walls`, `1st ... 4th Floor Walls`, `Gable Walls`, `Parapet Walls`, `Wall Materials`, `1st ... 4th Floor Framing List`, `Loft Framing List`, `Roof Frame list`, `Roof System Misc`, `Roof Products`, `Covered Front Porch Framing List`, `#N Upper Balcony List W' x D'`, `#N Porch Framing List W' x D'`, `Canopy Framing List`, `Exterior Trims`, `Interior Doors&Trims`.

Formatting: bold, colored fill, columns B-F empty. Group subsections: `Rear Ground Deck Frame`, `Balcony Railing`, `Ground Deck Decking (rear)`, `Canopy Trims`, `Porch Trims`. [File format](dfl-overview.md#source-format).

### Walls

| Label | When |
| --- | --- |
| `Plates Ext (1) btm`, `Plates Ext (2) dbl top`, `Plates (bottom and dbl top)`, `PT Plates (single)`, `PT Sill Plates at ext. found`, `Plates Furring`, `Eve Plates (single)`, `Hip Plates (2)` | number of plies in the label and in H; P.T. only on concrete and masonry |
| `Studs Ext 16" o.c.`, `Studs Interior 16" o.c.`, `Studs Demising 16" o.c.`, `Studs for Gables`, `Blocking Studs` | stud height in E |
| `Bracing Ext Walls`, `Bracing Corridor`, `Bracing Demising`, `Bracing 48" o.c.` | by wall type |
| `Blocking`, `Blocking (2)`, `Blocking 48" o.c.`, `Blocking for Drywall`, `Blocking at Eves`, `Blocking (3) Plates`, `Blocking around all openings` | spacing or purpose in the label |
| `Ext. Headers up to 48"`, `... up to 60"`, `... up to 72"`, `Ext. Headers over 72"`, `Int. Headers (2)`, `Garage headers (3)` | plies in the label |
| `Wall Sheathing`, `Box Sheathing`, `Inside Sheathing`, `Tape`, `Vapor Barrier` (WRB per the specification), `Insulation`, `Rigid Insulation`, `Window Flashing`, `Sill Flashing` | B pulls the spec cell (`=$O$3`) |
| `Holdowns (1) btm`, `Holdowns (2) btm top`, `SW Anchor Bolts 12" o.c.`, `Anchor Bolts 48" o.c.`, `Washers`, `Nuts` | model in B, SW mark in E |
| `Tracks (1) btm`, `Deflection Tracks (1) top`, `Mtl Studs 16" o.c.` | metal walls, in this order |
| `Buildout Horizontal`, `Buildout Vertical 16" o.c.` | facade build-out, FRT per detail |
| `Draft Stop` | in `Gable Walls` after a blank row |

### Floor framing and framing

| Label | When |
| --- | --- |
| `Beam`, `Beam (2) Flush`, `Beam (3) Dropped`, `Beam Rim`, `Beam Stairs`, `Beam balcony`, `Ext Beam`, `Platform Beam (2)`, `Nailer Plates for Steel Beam` | plies and Flush/Dropped in the label, beam code in E |
| `Joists 16" o.c.`, `Joist J1`, `Dbl Joists 16" o.c.`, `Extra joists`, `End Joists`, `Ceiling Joists 16" o.c.`, `Rafters 24" o.c.`, `Dbl Rafters`, `Collar ties 16" o.c.` | I-joist series in B (`11-7/8" TJI 210`) |
| `Rim Board`, `Rim Board (2)`, `Ribbon Board`, `Ledger`, `Ledger (2)`, `Ledger and Box`, `Box`, `Bracing for Trusses` | 16' boards (D `16`); rim without `LVL` in B if the product is not named |
| `Cross Bridging`, `Cross Bridging for I Joists` | wood `1x3` in 16' boards; `TB27` for I-joists in `pcs` |
| `Hangers`, `Hangers 16" o.c.`, `Hangers on demising`, `Clips`, `Ties`, `Simpson Ties at Eves` | model in B: `LUS210 Zmax`, `H2.5A` |
| `Posts`, `Posts (2)`, `Post Bases`, `Post Caps`, `Post Blocking`, `Post Sheathing`, `Columns` | height in E, hardware model in B |
| `Stringers (4)`, `Treads`, `Risers`, `Platform`, `Platform Ledger` | `2x12 Tread`, `1x8 Riser` |
| `Subfloor`, `Panel Adheasive`, `Plywood`, `Linear Panels`, `Liner Panels` | the template label is kept as is |

### Roofing and eaves

`Ridge`, `Ridge (2)`, `Ridge Vent`, `Frame for Rakes 24" o.c.`, `Frame for Soffits 24" o.c.`, `Rafter Frame for returns`, `Sub Fascia`, `Truss Bracing`, `Blocking at Eves`, `Metal Roofs`, `Felt for Roof`, `Ice and Water (eves&valleys)`, `EPDM at flat roofs`, `Hclips` (spec `5/8 Hclip` by decking thickness).

### Deck, porch, balcony, railing

`Decking`, `Deck Fascia`, `Deck Risers`, `Sleepers`, `Posts at Rails 4x4`, `Post Sleeve`, `Post Cap`, `Rail sections 6'`, `Balustrades`, `Rails (top & bottom)`, `Cap Rail`, `Cables`, `Brackets`, `Railing`. Block makeup: [Balcony, porch and holdown blocks](dfl-blocks.md).

### Trim and other

`Ext Casing`, `Casing for Int. Doors`, `Corner Boards`, `Crowns`, `Frieze Board`, `Fascia at Eves`, `Fascia at Rakes`, `Over Fascia Trims`, `Furring`, `Baseboard`, `Head Trim Flashing`, `Flashings at Wall`, `Int. Doors` (`3070 1 unit MARK FIRE LABEL`, doors wider than 4' as double `(2)2670`), `Cased Openings`, `Drywall at Walls`, `Drywall at Ceiling`, `Insulation at 6" Ext. Walls` (drywall and insulation between studs only when they are explicitly in scope; usually by others), `Lath Horiz 4" o.c.`, `Lath Vert 16" o.c.`.

## Common mistakes

- `FT` or `SF` in D; hardware in `LFT`; a unit instead of the board length in D of a lumber row, so the formula divides by text.
- A detail line (rim, blocking) cut into 16' pieces in the tree: measure the whole length, the formula splits it into boards.
- The label does not match the calculation (`Plates (2)` when the detail shows one plate).
- `1-3/4 LVL Rim` when LVL is not named on the drawing: write `11-7/8" Rim` or `11-7/8" LSL Rim`.
- A hardware model with a typo or in a made-up format (`ABU66Z` instead of `ABU66 Zmax`): [Hangers, how to write them](hangers.md#dfl-format).
- Free-form labels instead of the dictionary: the sorting macros cannot find them.

All workbook mistakes: [Common mistakes, Excel DFL and notes](../start/common-mistakes.md#excel).

## Example

```text
A                           B                      C                        D      E            G     H
2nd Floor Framing List
Note: Floor Trusses are by others
Beam (3) Flush              1 3/4 x 11 7/8 LVL     =2*3                     14     FB2
Corridor Joists             2x10                   43                       14     86 pcs 7'
Rim Board                   1 1/8 x 24 Rim Board   =CEILING(G144/D144,1)    16     5/S401       310
Blocking for Drywall        2x4                    =CEILING(G145/D145,1)    16     6/S401       420
Bracing for Trusses         2x6                    =CEILING(G147/D147,1)    16     assumed      288
Hangers                     LUS210                 =2*86                    pcs    7/S401
```

How to read the example:

- `Beam (3) Flush`: two beams of three plies each, C = 2 x 3 = 6 boards of 14'. `(3)` in the label is the number of plies in one place; C counts every board.
- `Corridor Joists`: 86 pieces of 7' are cut two from each 14' board, so C = 43 and the piece count is noted in E.
- `Rim Board`: 310 / 16 = 19.4, so 20 boards of 16'. D holds the board length, which is why the formula divides by D. Put `LFT` in D and the formula divides by text.
- `Blocking for Drywall`: 420 / 16 = 26.3, so 27 boards. `Bracing for Trusses`: 288 / 16 = 18 boards.
- `Hangers`: two per joist piece, 2 x 86 = 172.
- Rim in `LFT` with the `1.05` factor happens only on an EWP-only job: [Formulas](formulas.md#rim-ribbon-blocking-ledger).

## See also

- [How the DFL workbook works](dfl-overview.md), [Notes in the DFL](standard-notes.md), [Balcony, porch and holdown blocks](dfl-blocks.md)
- [Material catalog](material-catalog.md), [Hardware catalog](hardware-catalog.md), [Excel macros and hotkeys](excel-hotkeys.md)
