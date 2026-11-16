# Corners

<figure markdown>
  ![Three corner options in plan: 2-stud, 3-stud, California corner](../../../assets/images/framing/corners.svg)
  <figcaption markdown="span">Wall corner in plan: 2-stud L, 3-stud, California corner with backing for gypsum. Stick: `corners` points per floor, the template adds the corner studs to `Studs Ext`. Panels: not counted.</figcaption>
</figure>

<!-- TODO-PHOTO: three stud corner wood framing photo, EN query "three stud corner framing" -->

## What it is

A corner is the stud pack where two walls meet: 2 or 3 studs, or a California corner.
The stud factor `1.1` (one stud per foot plus waste) covers cutoffs and studs
at openings, and corners and T-intersections on stick framing are counted as `corners`
points: the DFL template itself adds 2 LFT of studs per point to the first `Studs Ext`
row of the floor. There is no separate `Corners` row in the DFL. On a panel job the
corners are already inside the panel.

## Where to find it on the plans

| Sheet | What to take |
| --- | --- |
| Floor plans | Number of exterior corners and T-intersections per floor |
| Typical wall details, corner detail | How many studs per corner, backing for gypsum |
| Structural details | Corner holdowns, extra studs, where called out |
| Scope | Stick or panels: on a panel job corners are not counted |

## How to measure in OurPlanCore

**Count** tool (points), one in each exterior corner and each
T-intersection on the floor plan. Takeoff `corners` in
`walls/<floor> floor walls` (the W dot puts the Count into walls; the word `corners`
itself counts as a wall token). Give it its own CountSymbol so the points look different from holdowns.

## Takeoff name and DFL row

| Takeoff name | DFL row | Unit | Formula / factor |
| --- | --- | --- | --- |
| `corners` (Count, 1st floor) | no row of its own: the points go into G of the first `Studs Ext` row of the 1st floor | G in LFT | G = exterior wall LFT + 2 x number of points (template formula `=P40+Q38*2`, do not change it by hand) |
| `corners` (Count, 2nd floor) | the same, in `Studs Ext` of the 2nd floor | G in LFT | per floor, each floor in its own folder |

A `Corners` row of its own counts the corners a second time: they already sit in G
of the `Studs Ext` row, and C of that row (`G x 1.1`) turns them into studs.

## Common mistakes

- Corners counted on a panel job: they are already in the panel.
- `corners` points of different floors in one takeoff: the corners land on the wrong floor.
- T-intersections and backing forgotten although the detail shows them.
- A `Corners` row of its own added: the corners are counted twice.

Walkthrough with examples: [all wall mistakes](../../../start/common-mistakes.md#walls).

## Example

```text
walls/1st floor walls/
  corners      Count, 14 ea     Notes: 3-stud per 5/A701
walls/2nd floor walls/
  corners      Count, 14 ea
```

## See also

- [Exterior Walls](exterior.md), [Sill Plates](sill-plates.md)
- [COM Commercial: studs, extra, dbl](../../../work-types/com.md)
- [Hardware catalog](../../../reference/hardware-catalog.md)
