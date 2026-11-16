# Measuring siding

<figure markdown>
  ![Siding take-off by elevation area](../../assets/images/siding/measure.svg)
  <figcaption markdown="span">SQ FT by elevation: the wall field is an Area, gable and accent as separate areas, large openings deducted once.</figcaption>
</figure>

<!-- TODO-SCREEN: measure-area-siding.png (Area on an elevation in OurPlanCore with an opening deducted, item siding/6" vertical) -->

## What it is

Siding is counted by area in `SQ FT` per elevation, wall by wall. Trim,
accessories and flashing are counted separately in `LFT` and `pcs`; they are not part of the
siding area.

## Where to find it on the plans

| Sheet | What to take |
| --- | --- |
| Elevations (`el`) | Area of each elevation, material by zone, gables, bays, dormers |
| Wall sections | Wall height up to the soffit, flare, furring |
| Plans and opening layout | Large openings to deduct (overhead doors, storefronts) |
| Notes | `by others`, `TBD`, product |

## How to measure in OurPlanCore

1. Open the elevation sheet. Elevations have no sheet point, so the item is created
   in the `siding` root manually or by a name rule.
2. Area along the wall field of each elevation: one item per material and color
   (`6" vertical`, `panel grey`, `shingle gable`). One material on
   several elevations can be collected as several polygons in one item.
3. Gables, dormers, bays, return walls as separate polygons or items,
   especially with a different material.
4. Cut large openings out as holes in the Area; windows under 4' are not deducted,
   they go to waste. Do not deduct the same opening twice (siding and
   WRB each take the deduction from their own area).
5. Check the elevation scale against a known dimension (floor height, overhead door
   width): elevations are often at a different scale than the plans.
6. Move the area to the DFL with a formula with visible addends and update it after
   the takeoff is edited.

## Tree name and DFL row

| Tree name | DFL row | Unit | Formula |
| --- | --- | --- | --- |
| `siding/6" vertical` | `Siding Vertical 1x6 Cedar` | SQ FT | `=Front+Rear+Left+Right` |
| `siding/panel grey` | `Siding Fiber Cement Panel grey` | SQ FT | separately by color |
| `siding/shingle gable` | `Siding Gable front Vinyl Shingles` | SQ FT | accent separately |
| | `Siding` (correction) | SQ FT | `-140` as a visible row, if a deduction is needed |
| | `Siding Per customer TBD` | SQ FT | `0` plus a note |

Waste: lap is moderate, shingle and shake higher, diagonal and small gables
give more offcuts. Keep the factor as a visible multiplier per
[Formulas and factors](../../reference/formulas.md).

## By others and TBD

- Siding by others: a row with `0` and the note `by others` or `by customer`.
- Material not specified: `Per customer TBD` or `verify material`, do not
  substitute a product.
- EIFS, stucco, stone, brick: not counted, but check the WRB, sheathing, furring and
  trim next to them: [EIFS / Stucco / Veneer](eifs-stucco-veneer.md).

## Common mistakes

- Area from the plan (perimeter x height) without deducting gables and without the different
  wall heights per elevation.
- An opening deducted twice or not at all (garage doors).
- Elevation scale not checked.
- Area measured but not moved to Excel or not updated.
- All area and sheathing mistakes: [SQFT areas](../../start/common-mistakes.md#sqft), [Sheathing](../../start/common-mistakes.md#sheathing).

## Example

```text
Takeoffs/Main/siding/6" vertical     Area   4 polygons   3 180 SF
Takeoffs/Main/siding/shingle gable   Area   2 polygons     420 SF

Siding Vertical      1x6 Cedar              3 180  SQ FT   =1120+940+560+560   A201 A202
Siding Gable front   Cedar Shingles 5-1/2"    420  SQ FT   =210+210            A201
```

## See also

- [Siding](overview.md), [Siding types](types.md), [Underlayment](underlayment.md), [EIFS / Stucco / Veneer](eifs-stucco-veneer.md)
- [Formulas and factors](../../reference/formulas.md), [Client rules](../../start/client-rules.md), [Trim macros](../exterior-trims/macros.md)
