# Casing

<figure markdown>
  ![Door and window casing: head, sides, stool, apron](../../assets/images/trims/int-casing.svg)
  <figcaption markdown="span">Window from the inside: head casing, side casing, stool, apron; door: head and two sides. Casing is counted in LFT with a formula from the opening list.</figcaption>
</figure>

## What it is

The trim around a door or window on the inside. Counted in LFT with a formula from
the opening list: the perimeter of each door (width plus two heights), both faces of
the wall and 1.1 waste. The list of doors and cased openings, size designations and
Excel entry are on the [Door and Window Trim](door-window-trim.md) page; this page has
the casing formula.

## Where to find it on the plans

| Sheet | What to take |
| --- | --- |
| Door schedule | Size, type, number of doors; usually no trim type there |
| Window schedule and interior elevations | Windows with casing, stool and apron |
| Finish schedule and notes | Casing profile (`1" x 3-1/2" Polyurethane casing`), stained or painted |

## How to measure in OurPlanCore

No separate measurement is needed: casing is calculated with a formula from the list of doors and
windows per floor. The door list comes from the plan (open door symbol) or the
door schedule, windows from `openings`. Odd-shaped casing (arched, a cased
opening across the whole wall) can be traced with a Line.

## Tree name and DFL row

| DFL row | Unit | Formula |
| --- | --- | --- |
| `Casing for Int. Doors` | LFT | `=CEILING(2*SUM(perimeters)/12*1.1,10)`: door perimeter = W + 2H in inches from the door code, `2` = both faces of the wall, `/12` = to feet, `1.1` = waste |
| `Casing for Ext. Doors&Wind` | LFT | `=CEILING(perimeter*1.1,10)`: perimeter of the exterior doors and windows of that floor from the openings table, `4-sides` in E |
| `Window Stool` | LFT | `=CEILING(sill*1.1,10)`: sill length of the windows of the floor; no stool on the detail means no row |
| `Cased Openings` | unit | an opening without a door, its own quantity row; its perimeter goes into the same `Casing for Int. Doors` sum |

- In the DFL template the door row itself computes the perimeter: column G reads
  the size code (`2680` = 30" + 2 x 96" = 222") and multiplies it by the quantity;
  pairs `(2)` are doubled. The `SUM` in the casing formula must cover every door
  and cased opening row of that floor and nothing else.
- There is no separate `Int. Door jambs` row in LFT. Interior doors are counted
  with points per unit and grouped by the size of the wall they stand in: a point
  at a `2x6` wall is a door with a jamb for `2x6`.
- Group casing by location and type when common areas differ from
  units.
- Keep the profile from the notes in column B or a note (`Note: All door trim to be 1"
  x 3-1/2" Polyurethane casing`); no profile given: `TBD Casing`. Hardware
  numbers are not part of trim.

## Common mistakes

- Casing counted on one side of the door instead of two (no `2*` in the formula).
- The 1.1 waste and the round-up to 10 are lost: the formula was replaced by a number.
- A jambs row in LFT (`casing / 2`) was added: there is no such row.
- Interior casing mixed with exterior casing and flashing.
- A made-up profile instead of `TBD Casing`.
- All Excel mistakes: [Excel DFL and notes](../../start/common-mistakes.md#excel).

## Example

```text
Int. Doors              2680      24   unit   A601
Casing for Int. Doors   1x3-1/2   980  LFT    =CEILING(2*SUM(G)/12*1.1,10)

One 2680 door: 30" + 2 x 96" = 222" (18.5')
24 doors: 222 x 24 = 5328"
Both faces: 2 x 5328 / 12 = 888 LFT, the same as (2 x 8 + 2.5) x 2 x 24
Waste: 888 x 1.1 = 976.8, rounded up to 10 = 980 LFT
```

## See also

- [Door and Window Trim](door-window-trim.md), [Base](base.md), [Room Schedule](room-schedule.md), [Interior Trims](overview.md)
- [Exterior Trims - Casing, Corner & Band](../exterior-trims/casing-corner-band.md)
