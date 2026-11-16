# Corridor Walls

<figure markdown>
  ![Staggered stud wall: two rows of 2x4 studs on 2x6 plates](../../../assets/images/confluence/confluence-062.png)
  <figcaption markdown="span">Staggered stud wall: 2x4 studs in two staggered rows on one 2x6 plate, insulation woven between them. In the DFL these are 2x6 plates and two rows of 2x4 studs.</figcaption>
</figure>

<!-- TODO-PHOTO: staggered stud wall framing photo, EN query "staggered stud wall framing" -->

## What it is

A corridor wall separates a unit from a common area: corridor, stair,
garage, lobby. It is fire-rated, often on 2x6 plates with staggered 2x4
studs, and it carries a ledger or drywall bracing on top where the floor framing runs
parallel. A wall between two units is a [Demising](demising.md) wall,
and a shaft wall is a [Shaft](shaft.md) wall.

## Where to find it on the plans

| Sheet | What to take |
| --- | --- |
| Floor plans `a101 1st` | Wall type marks along corridors, stairs, garage |
| Wall type schedule (`wt`), UL assembly | Plate and stud size, staggered or not, gypsum layers, rating |
| Section at the corridor, S details | Ledger, `2x10` corridor joists on a ledger, blocking, hangers |
| Door schedule | Fire-rated unit entry doors (`3070 ... C-lbl`) |
| Stud schedule | If the corridor wall is also bearing: mark in [BW](bearing-walls.md) |

## How to measure in OurPlanCore

**Line** tool, LFT unit, on the floor plan (W dot).

1. Category by run: a wall segment at a stair or at the garage is also `corr`,
   even if it continues a demising wall.
2. Name `corr 2x6 11.7`: category, plate size, height. A double corridor wall
   (two frames on the plan) is `corr (2) 2x6 11.7`.
3. A staggered wall is one line: plates by the name `2x6`, the two stud rows
   are handled in the DFL.
4. Start a new takeoff when the height or size changes. Height comes from the section of your
   building, not floor-to-floor ([Exterior: stud height](exterior.md#stud-height)).
5. If the wall type is bearing, trace the same wall again in `BW/<floor>`.

## Takeoff name and DFL row

| Takeoff name | DFL row | Unit | Formula / factor |
| --- | --- | --- | --- |
| `corr 2x6 11.7` | `Plates Corr (1) btm` 2x6 (P.T. only on concrete) | LFT | `LFT x 1.1` |
| same | `Plates Corr (2) dbl top` 2x6 | LFT | `LFT x 2 x 1.1` |
| same | `Studs Corr` 2x4 staggered | pcs | `LFT x 1.1 x 2` (two rows at 16") |
| same | `Bracing Corridor` 2x4 | LFT | by wall height |
| same | `Blocking` | LFT | by wall type |
| same | `Bracing for Drywall` 2x4 | LFT | where the floor framing runs parallel to the wall |
| `corr (2) 2x6 11.7` | the same rows for two frames | | `x 2` |

Hangers over a corridor wall are regular `ITS` when the gypsum stops
below the floor framing. `DHU` / `DGU` only where the joists bear over a true
fire wall per detail (stair, elevator, shaft): [Hangers](../../../reference/hangers.md).
Corridor joists at the roof without a detail get a note with the reason, not `Optional` with no
explanation ([Standard notes](../../../reference/standard-notes.md)).

## Common mistakes

- Corridor and demising mixed up as a group: on one check 241 LF of corridor became 161, and demising grew from 577 to 648.
- A piece of corridor wall at a stair written as `ext`.
- `DHU` used only because the wall is a corridor wall.
- A staggered wall counted with one row of studs.
- 2x6 plates forgotten: studs are 2x4, and the plates were written as 2x4.
- Ledger and corridor joist hardware not listed on separate rows per detail.

Walkthrough with examples: [all wall mistakes](../../../start/common-mistakes.md#walls).

## Example

```text
walls/
  2nd floor walls/
    corr 2x6 9.09        Line, 161.0 LFT
    corr (2) 2x6 9.09    Line, 24.5 LFT   (two walls at the stair)
    dem 2x6 9.09         Line, 648.2 LFT
```

## See also

- [Demising Walls](demising.md), [Unit Walls](unit.md), [Shaft Walls](shaft.md)
- [Bracing for Drywall](../../horizontal/floor-framing/details/bracingdrywall.md)
- [Hangers](../../../reference/hangers.md): ITS vs DHU
- [Tips and key rules](../../../reference/boss-feedback-rules.md#dhu-dgu-vs-its)
