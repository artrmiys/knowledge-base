# Wall Bracing and Blocking for Drywall

<figure markdown>
  ![Wall bracing and drywall backing: two different rows](../../../../assets/images/framing/drywall-bracing.svg)
  <figcaption markdown="span">Two different rows. (a) Wall bracing: 2x4 by the piece, one board per 8 LFT of wall, board length by wall height. (b) Backing for the ceiling drywall at a wall parallel to the joists: a board along the top of the wall, row `Blocking for Drywall`.</figcaption>
</figure>

<!-- TODO-PHOTO: 2x4 drywall backing / ledger on top plate of a wall parallel to joists, EN query "drywall backing blocking top plate parallel joists" -->

## What it is

This page covers two different rows that are often mixed up. There is no `Bracing for Drywall` row in the DFL.

| | Wall bracing | Drywall backing |
| --- | --- | --- |
| What it is | temporary `2x4` braces that hold the wall during erection | a continuous `2x4` along the top of the wall, backing for the ceiling drywall edge |
| Where it is needed | all walls 7' and taller | walls parallel to the joists or trusses |
| Label | `Bracing Ext Walls`, `Bracing Corridor`, `Bracing Demising` | `Blocking for Drywall` |
| DFL section | floor walls (Floor Walls) | Floor Framing List |
| Unit | pieces, board length in D by the wall height | 16' boards |

Wall bracing is counted on every job, panel jobs included: it is not part of the panel. Blocking between joists: [Blocking](blocking.md); ribbon under the joists: [Ribbon Board](ribbon.md).

## Where to find it on the plans

| Sheet | What to take |
| --- | --- |
| Wall schedule, sections | wall heights by type (ext, corridor, demising): they set the wall bracing board length |
| Floor framing plan | which walls run parallel to the joists and trusses: those need drywall backing |
| Ceiling details, RCP | drywall ledger or nailer along the top of the wall, on one side or both; dropped soffit (a soffit is not bracing) |

## How to measure in OurPlanCore

- Wall bracing: no separate measurement is needed, the length comes from the floor walls (`walls/<floor> floor walls/ext ...`, `corr`, `dem`).
- Drywall backing: a Line (L) along the walls where the detail shows a 2x4 on top, in `framing/<floor> framing/details/bd` or with the detail number. One Line per run, do not cut it into 16' pieces. A detail with a 2x4 on both sides of the wall is counted twice.

## Tree name and DFL row

### Wall bracing

Three rows per floor, by wall type. `G` is the LFT of walls of that type on the floor, C = `G / 8 x 1.1`: one board for every 8 LFT of wall plus 10%. C is pieces, not LFT.

| A (Label) | B | C | D | G |
| --- | --- | --- | --- | --- |
| `Bracing Ext Walls` | `2x4` | `=G/8*1.1` | by height | LFT of ext walls on the floor |
| `Bracing Corridor` | `2x4` | `=G/8*1.1` | by height | LFT of corridor walls |
| `Bracing Demising` | `2x4` | `=G/8*1.1` | by height | LFT of demising walls |

The board length in D follows the tallest wall of that type on the floor. This is the ladder of the DFL template: in the book D is a formula ([COM](../../../../work-types/com.md) links here):

| Wall height | D (board length) |
| --- | --- |
| up to 10' inclusive | `14` |
| over 10' up to 12' | `16` |
| over 12' up to 16' | `18` |
| over 16' | `20` |

- Walls under 7' (parapet, knee wall, curb, mech screen) get no bracing.
- Gable: D `14`.

### Drywall backing

| Tree name | A (Label) | B | C | D | E |
| --- | --- | --- | --- | --- | --- |
| `details/bd` | `Blocking for Drywall` | `2x4` | `=CEILING(G/D,1)` | `16` | all details of the row |

`G` is the sum of the line lengths in LFT, `D` is the board length (16). One row per floor, with the details listed in E. There is no separate waste factor: rounding up to a whole board is the allowance.

Export: the WL button on the XL strip moves the walls to `A3`, and the wall bracing rows are filled from the same LFT. The `bd` lines are moved by the DT button; the `bd` flag gives the `Blocking for Drywall` row.

## Common mistakes

- Wall bracing written in `LFT`. It is pieces: one board per 8 LFT of wall, with the board length in D.
- Board length not by wall height: an 11' wall got 14 instead of 16.
- Drywall backing written as `Bracing for Drywall` or put into the wall bracing rows. Its row is `Blocking for Drywall`, 16' boards.
- Drywall backing counted on one side of the wall; the detail gives both.
- A dropped soffit taken for bracing: soffits are counted on [Ceiling / Soffit Framing](../../ceiling-soffit-framing.md).
- On a panel job the wall bracing was thrown out with the panels, though it is not part of the panel.
- [All wall mistakes](../../../../start/common-mistakes.md#walls)

## Example

Floor walls 11' tall: D = 16.

| A | B | C | D | E | G |
| --- | --- | --- | --- | --- | --- |
| `Bracing Ext Walls` | `2x4` | `=G/8*1.1` | 16 | | 412 |
| `Bracing Corridor` | `2x4` | `=G/8*1.1` | 16 | | 161 |
| `Bracing Demising` | `2x4` | `=G/8*1.1` | 16 | | 648 |
| `Blocking for Drywall` | `2x4` | `=CEILING(G/D,1)` | 16 | `6/S400` | 310 |

Check: 412 / 8 x 1.1 = 56.7 boards; 161 / 8 x 1.1 = 22.1; 648 / 8 x 1.1 = 89.1; 310 / 16 = 19.4, so 20 boards.

## See also

- [Blocking](blocking.md), [Ribbon Board](ribbon.md)
- [Demising Walls](../../../vertical/walls/demising.md), [Exterior Walls](../../../vertical/walls/exterior.md), [COM](../../../../work-types/com.md)
