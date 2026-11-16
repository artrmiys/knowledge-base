# Rim Board

<figure markdown>
  ![Rim board at joist ends](../../../../assets/images/framing/rim-board.svg)
  <figcaption markdown="span">The rim board closes the joist ends around the floor perimeter and carries the wall above. It is measured as one Line along the perimeter; in the DFL the formula turns the length into 16' boards (on an EWP-only job it stays LFT x 1.05).</figcaption>
</figure>

<figure markdown>
  ![Rim joist around the floor perimeter on the sill plate](../../../../assets/images/photos/framing/rim-joist-floor-perimeter.jpg){ width="520" }
  <figcaption markdown="span">First floor framing: rim around the whole perimeter on the sill plate, the joist ends butt into it. Measure a Line along the building perimeter and along the edges of floor openings; with I-joists the rim material is engineered only. Photo: hunker.com, [source](https://www.hunker.com/13720287/what-is-a-rim-joist), found via Pinterest.</figcaption>
</figure>

## What it is

The rim is the board at the edge of the floor that the joist ends butt into: `1-1/8" OSB Rim`, `1-1/4" LSL Rim`, `1-3/4" LVL`. With I-joists, engineered rim only. A [Ribbon](ribbon.md) is let into the studs and carries the joists, [Blocking](blocking.md) sits between the joists: these are different rows. Rim around a deck or balcony is P.T. 2x in [Deck / Porch / Balcony Frame](../../../deck/deck-porch-balcony-frame.md).

## Where to find it on the plans

| Sheet | What to take |
| --- | --- |
| Joist schedule, general notes | rim product and thickness by joist depth |
| Wall sections, floor details | rim at the exterior wall, at demising on both sides, at roof TJI |
| Deck / corridor details | where the rim carries load and must be `1-3/4" LVL` |
| Floor framing plan | perimeter and interior lines where the joist direction changes |

## How to measure in OurPlanCore

Line (L) along the rim line on the framing sheet with the F point: the outside perimeter of the floor plus interior lines where the joists change direction or butt into a wall. Line length = the length where the detail applies. Takeoff `framing/<floor> framing/details/rim` or with the detail number `5/S400 rim`. Do not cut the line into 16' pieces: it is one Line for the whole run, and the formula in the DFL counts the boards.

<figure markdown>
  ![Line along a detail on the plan](../../../../assets/images/ourplancore/v3/measure-line-detail.png)
  <figcaption markdown="span">Line along where the detail applies: the line length goes to G of the DFL row, the detail name gives the M flag on export.</figcaption>
</figure>

## Tree name and DFL row

Export: the DT button puts details into J:L of the floor worksheet; a name with `rim` gets the `r` flag in M, and the `C_RimBoardBlockingHangers` macro moves the length to the `Rim Board` row.

| Tree name | A (Label) | B (material) | C | D | E |
| --- | --- | --- | --- | --- | --- |
| `details/rim` | `Rim Board` | `11-7/8" Rim` | `=CEILING(G/D,1)` | `16` | detail |
| `details/rim LSL` | `Rim Board` | `11-7/8" LSL Rim` | `=CEILING(G/D,1)` | `16` | |
| `details/rim corr LVL` | `Rim Board` | `1-3/4 x 11-7/8 LVL` | `=CEILING(G/D,1)` | `16` | corridor detail |
| `details/rim dem` | `Rim Board (2)` | | `=CEILING(G*H/D,1)`, H = 2 | `16` | demising on both sides |
| `details/rim` on an EWP-only job | `Rim Board` | `11-7/8" Rim` | `G x 1.05` | `LFT` | detail |

`G` is the rim line length in LFT from OurPlanCore, `D` is the board length (16), `H` is the number of plies.

| Product | When |
| --- | --- |
| `1-1/8" OSB Rim` | common thin rim per schedule |
| `1-1/4"` or `1-1/2" LSL Rim` | LSL is specified or a heavier rim is needed |
| `1-3/4" LVL Rim` | a deck or corridor frame attaches to the rim, or the detail calls for it directly |

- Framing book (Frame, COM, residential, reconstruction): the rim is 16' boards, C = `G / D` rounded up. There is no separate waste factor: rounding up to a whole board is the allowance.
- EWP-only job (only engineered wood is counted): the rim stays in `LFT`, C = `G x 1.05`, and is not cut into 16' pieces.
- A client on an ordinary job asks for the rim in LFT: `G x 1.1`.

Summary of the numbers: [Formulas](../../../../reference/formulas.md#rim-ribbon-blocking-ledger), same in [Tips](../../../../reference/boss-feedback-rules.md#rim-board).

## Common mistakes

- Rim called `1-3/4 LVL` though LVL is not specified. Default is `11-7/8" Rim`; product unclear - `assumed` in the note.
- The rim line in the tree cut into 16' pieces. Measure one Line; the formula `G / D` turns it into boards.
- The rim left in LFT with `1.05` in a framing book: that form is for an EWP-only job only.
- Rim at roof TJI forgotten.
- At demising one side counted, the detail gives rim on both sides.
- On a panel job the rim counted with the wall length, not along the floor line.
- [All floor framing mistakes](../../../../start/common-mistakes.md#floor)

## Example

Framing book:

| A | B | C | D | E | G | H |
| --- | --- | --- | --- | --- | --- | --- |
| `Rim Board` | `11-7/8" LSL Rim` | `=CEILING(G/D,1)` | 16 | `5/S400` | 412 | |
| `Rim Board (2)` | `11-7/8" LSL Rim` | `=CEILING(G*H/D,1)` | 16 | `9/S400 demising` | 96 | 2 |

412 / 16 = 25.75, so 26 boards; 96 x 2 / 16 = 12 boards.

The same rim on an EWP-only job:

| A | B | C | D | E | G |
| --- | --- | --- | --- | --- | --- |
| `Rim Board` | `11-7/8" LSL Rim` | `=CEILING(G*1.05,1)` | LFT | `5/S400` | 412 |

412 x 1.05 = 432.6, so 433 LFT.

## See also

- [Ribbon Board](ribbon.md), [Blocking](blocking.md), [Joist](../joist.md)
- [Tips: Rim Board](../../../../reference/boss-feedback-rules.md#rim-board), [Formulas](../../../../reference/formulas.md)
