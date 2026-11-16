# Blocking o.c.

<figure markdown>
  ![Blocking at 48 inch on center](../../../../assets/images/framing/blocking-oc.svg)
  <figcaption markdown="span">Blocking at 48" o.c.: a Line along the zone, one piece at every point of the line; the count comes from the line length and the spacing, not as a solid row.</figcaption>
</figure>

## What it is

Blocking o.c. is separate blocking pieces that do not form a solid row but sit at a spacing along one line: on top of a partition under the trusses (a piece between the trusses every `48" o.c.`), along a bearing line, between the studs of a wall. Types: flat (laid flat between two joists or trusses), diagonal, vertical (between studs). It is counted from the line length and the spacing, not as a solid row. Solid blocking and all its kinds: [Blocking](blocking.md).

## Where to find it on the plans

| Sheet | What to take |
| --- | --- |
| Framing notes, typical details | spacing (`48" o.c.`), type (flat, diagonal, vertical), size, piece length |
| Framing plan | the line the pieces follow: a partition under the trusses, a bearing line |
| Wall details (shear, fire) | vertical blocking between studs at a spacing |

## How to measure in OurPlanCore

Line (L) along the line the blocking pieces follow, on the framing sheet with the F point: along the partition, the bearing line, the row. Rules:

1. One Line for every row of blocking. Two parallel rows are two lines.
2. The line runs along the row, not across it and not through the whole zone: the formula counts points along the line.
3. Takeoff `framing/<floor> framing/details/blocking 48` or with the detail number; the spacing goes in the name. The line length in LFT goes to G of the row, with no waste in it.

## Tree name and DFL row

The spacing sits in column H and prints in the Label.

| A (Label) | B | C (formula, English Excel names) | D | H |
| --- | --- | --- | --- | --- |
| `Blocking 48" o.c.` | per detail: `2x4` flat or the joist size | `=CEILING(G*12/H*2/D,1)` | `16` | `48` |
| `Diagonal Blocking 48" o.c.` | `2x4` | `=CEILING(G*12/H*3/D,1)` | `16` | `48` |
| `Vertical Blocking 48" o.c.` | `2x4` | `=CEILING(G*12/H*2/D,1)` | `16` | `48` |

What the letters mean:

- `G` - the line length in feet (LFT from OurPlanCore). There is no waste in it.
- `H` - the spacing in inches.
- `G*12/H` - the number of blocking points along the line.
- the multiplier (`2`, `3`) - feet of board used per point.
- `D` - the board length in feet (16).

Points x feet per point = LFT of board; LFT / 16 = boards. There is no separate waste factor in the formula: rounding up to a whole board is the allowance.

| Type | Feet of board per point |
| --- | --- |
| Flat (a piece laid flat between two members) | `2` |
| Diagonal | `3` |
| Vertical (between studs) | `2` |

If the detail gives another piece length or several pieces at one point, take the multiplier from the detail: feet of board per point. Formula summary: [Formulas, Blocking formulas](../../../../reference/formulas.md#blocking-formulas).

## Common mistakes

- The line drawn across the rows or through the whole zone. `G` must be the length of the line the pieces follow.
- `1.1` added to the formula. `G` is a line length with no waste in it, and the template formula has none either.
- Blocking at a spacing counted as a solid row: at 48" that is twice the boards.
- Spacing taken from the template, not from the job note.
- The formula applied to in-panel blocking on a panel job.
- Plates and wall blocking converted to pcs though the template expects LFT.
- [All floor framing mistakes](../../../../start/common-mistakes.md#floor)

## Example

| A | B | C | D | E | G | H |
| --- | --- | --- | --- | --- | --- | --- |
| `Blocking 48" o.c.` | `2x4` | `=CEILING(G*12/H*2/D,1)` | 16 | `note 7 per S001` | 240 | 48 |

A line of 240 LFT along the partition at 48" o.c.: 240 x 12 / 48 = 60 points; 60 x 2' = 120 LFT of board; 120 / 16 = 7.5, so 8 boards of 16'.

## See also

- [Blocking](blocking.md), [Ribbon Board](ribbon.md), [Formulas](../../../../reference/formulas.md)
