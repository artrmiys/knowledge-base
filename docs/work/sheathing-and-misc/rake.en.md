# Rake

<figure markdown>
  ![Rake: the sloped edge on the gable, the eave is the horizontal bottom edge](../../assets/images/roof/rake.svg)
  <figcaption markdown="span">The rake is the sloped roof edge along the gable slope; the eave is the horizontal bottom edge. Two different lines, two different folders.</figcaption>
</figure>

## What it is

The rake is the sloped roof edge on the gable side, where the roof overhangs the
gable. It differs from the eave in direction (along the slope, not horizontal),
framing (lookouts/outriggers instead of truss tails) and its set of rows. The canon for
the whole eave, including units and soffit, is on the [Eve / Eave](eve.md) page.

## Where to find it on the plans

| Sheet | What to take |
| --- | --- |
| Elevations (`el`) | True length of the rake (measure here), rake fascia, barge board, trim, FRT on exposed wood |
| Roof plan (`a105 rf`) | Where the rakes are, the overhang |
| Details (`d`) | Lookouts or outlookers (size and spacing), frame for rakes, sub fascia, blocking |

## How to measure in OurPlanCore

1. Line tool along the sloped edge on the elevation, where the slope is shown at
   true length. LFT unit. Do not measure the rake on the roof plan: the plan
   line is shorter than the real edge because the pitch is lost.
2. Name `rake <overhang in inches> <zone>`: `rake 12 main`, `rake 24 main`.
   The number is the overhang from a section or detail, not the pitch and not the length.
   The `eves rakes/rakes` folder is created from the name automatically.
3. The elevation length is already sloped: no pitch factor is applied, neither in the
   takeoff nor in the formula. Only when no elevation shows that gable, multiply the plan
   length once by the common rafter factor (4:12 = 1.054, 6:12 = 1.118,
   8:12 = 1.202, 12:12 = 1.414; the table is on the
   [Hip](../horizontal/roof-framing/hip.md) page).
4. If gable areas are already traced on the elevation, run the rake along the top
   edge of those areas: faster and nothing gets missed.
5. Porch and canopy rakes are their own takeoffs (`rake 8 porch`); they are not part
   of `main`. Returns are their own takeoff too ([Returns](returns.md)).
6. A roof of `AJS Rafters` with an open overhang: count the rafters by hand as
   framing, not as a simple `rake`.

## Takeoff name and DFL row

Below, LFT is the length of the rake line and the overhang is the number from its name in inches.

| Takeoff name | DFL row | Material | Unit (D) | Formula C |
| --- | --- | --- | --- | --- |
| `eves rakes/rakes/rake 12 main` | `Soffits at Rakes` | `12" Vinyl` / `T&G beadboard` | `SQ FT` | `=EVEN(LFT*overhang/12*1.1)` |
| same line, soffit made of one board across the full width | `Soffits at Rakes` | `1x12` | `LFT` | `=EVEN(LFT*1.1)` |
| same line | `Fascia at Rakes` | `1x8`, `1x6` per detail | `LFT` | `=EVEN(LFT*1.1)` |
| same line | `Frame for Rakes 24" o.c.` | `2x6`, `2x4` or `2x8` per detail | `16` | `=CEILING(G/D,1)`, G = LFT x overhang / spacing + LFT |
| same line | `Sub Fascia` | `2x6` per detail | `16` | `=CEILING(G/D,1)`, G = LFT |
| same line, only when the detail draws blocking | `Blocking for Rakes 48" o.c.` | `2x6` | `16` | `=CEILING(G*12/H*2/D,1)`, H = spacing |

- `Frame for Rakes`, `Sub Fascia` and `Blocking for Rakes` are framing: D holds the
  16' board length, C the number of boards, and there is no 1.1 waste (rounding up to a
  whole board). G of `Frame for Rakes` holds the lookouts (LFT x overhang / spacing) and
  the ledger along the wall (LFT). Spacing is 24" by default, 16" when the detail says so.
- `Soffits at Rakes` and `Fascia at Rakes` are finish: only when trims are in scope.
  Soffit is in `LFT` only when it is one board or one strip across the full
  width; the rule and the default material: [Eve / Eave](eve.md).
- Aluminum or prefab rake by others: no framing or finish rows, a note stays.

## Common mistakes

- Rake merged with the eave into one line.
- Rake traced on the roof plan instead of the elevation: the length comes out short.
- A pitch factor applied again to a length taken from the elevation.
- The name carries the pitch or the length instead of the overhang (`rake 12` is a 12" overhang).
- Sub Fascia and Frame for Rakes written in `LFT` with 1.1 waste instead of 16' boards.
- FRT on an exposed rake not checked against the exterior wall rules.

All roof mistakes: [common-mistakes](../../start/common-mistakes.md#roof).

## Example

```text
Takeoffs/Main/eves rakes/rakes/
  rake 12 main     Line  96 LFT   (on the elevations)
Takeoffs/Grge/eves rakes/rakes/
  rake 24 main     Line  44 LFT

Main, 12" overhang:
Soffits at Rakes           12" Vinyl    106   SQ FT   96 x 12/12 x 1.1 = 105.6
Fascia at Rakes            1x8          106   LFT     96 x 1.1 = 105.6
Frame for Rakes 24" o.c.   2x6            9   16      G = 96 x 12/24 + 96 = 144; 144 / 16 = 9
Sub Fascia                 2x6            6   16      G = 96; 96 / 16 = 6
```

## See also

- [Eve / Eave](eve.md), [Returns](returns.md), [Gable Sheathing](../vertical/sheathing/gable.md)
- [Soffit and Fascia](../exterior-trims/soffit-fascia.md), [Roof Sheathing](../horizontal/roof-framing/roof-sheathing.md)
