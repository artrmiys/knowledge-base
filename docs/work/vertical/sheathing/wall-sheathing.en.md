# Wall Sheathing

<figure markdown>
  ![Installing OSB sheathing on a framed wall](../../../assets/images/confluence/confluence-094.jpg)
  <figcaption markdown="span">Structural sheathing on an exterior wall: OSB sheets over the studs. Area = wall length x wall height, minus openings wider than 4'. Archive photo.</figcaption>
</figure>

## What it is

Wall Sheathing is the structural panel on the outside face of a framed wall: OSB,
plywood or Zip. It is not the same as Exterior Gypsum (`Type X`,
`Densglass`) and not interior drywall: exterior gypsum goes on a separate
row ([Exterior Wall Materials](exterior-materials.md)); interior gypsum,
interior insulation and sound batts are not counted in the frame scope. Narrow strips
(box, truss heel, gable, parapet) have their own pages and their own rows.

## Where to find it on the plans

| Sheet | What to take |
| --- | --- |
| Wall type schedule (`wt`) and wall sections (`sec`) | Product, thickness, number of layers by the layer arrows; wall side |
| Structural general notes, table WS-1 (for example S3.1) | Structural thickness and nailing; the wall table and the roof table (WRS-1) are different |
| Shear wall schedule | Shear wall sheathing: side, thickness, layers; see [Shear Wall](shear-wall.md) |
| Energy / envelope sheets | Zip, Zip R, WRB, continuous insulation |
| Elevations (`el`) | Densglass zones, material changes, gables |

## Source priority

| Situation | Decision |
| --- | --- |
| Arch says Zip, structural says OSB/ply | Take Zip, the main DFL Note cites both sources |
| No Zip: Arch `1/2"`, Structural `5/8"` | Take `5/8"` (the stronger one), Note with both sheets |
| `19/32"` | This is `5/8"` for plywood/OSB, not `1/2"` |
| `7/16" Zip` on the S sheet and `Zip R-3` in the wall type | One product, a factual Note, no "differ" |
| No thickness anywhere | `assumed 1/2" Ply; verify` in the main Note |

Take the product name from this plan set: `LP FlameBlock 2-sided` is not
`7/16" OSB FRT`, do not turn `5/8" EXT. SHEATHING` into Ply without a reason,
write `CDX` only if the set says so. Call the exterior barrier WRB / Weather
Barrier per the spec (fluid-applied is not Tyvek), not "Vapor Barrier".

## How to measure in OurPlanCore

There is no separate `sheathing` branch in the tree. The wall area is collected from the wall
lines: the wall name carries the height (`ext 2x6 9.09`), and the Excel export multiplies the length
by the height.

1. Walls are traced with Line in `walls/<floor> floor walls/` on the sheet with the W dot
   (`a101 1st`). A change in height, size or sheathed side = a new takeoff.
2. Before counting, build a table of surfaces: building, floor, side, product,
   thickness, layers, gross or net, deductions. Count the layers by the detail arrows.
3. Deductions: openings are subtracted on their own floor and once (from the sheathing, WRB,
   insulation, Z-girt). Windows narrower than 4' are not subtracted. Garage doors are subtracted.
4. Strips outside the walls come from their own branches: `gables`, `trussheel`, `parapets`,
   box from the floor framing depth. Each strip is counted once.
5. How many sides: on a panel job one side is already in the panel, only the required
   second side is separate. The outside face of a shear wall is already in ext walls, add
   only the inside face. `P` on the mark = perforated, not two sides.

## Takeoff name and DFL row

| Takeoff name | DFL row | Material | Unit | Formula |
| --- | --- | --- | --- | --- |
| `walls/1st floor walls/ext 2x6 9.09` | `Wall Sheathing` | `7/16" Zip` or `1/2" OSB` | `4x8` | `=CEILING(SQFT/32*1.1,1)` |
| same takeoff | `Tape` | `Zip Tape` (only with Zip) | `LFT` | `=CEILING(SQFT*0.4*1.1,10)` |
| same takeoff | `Vapor Barrier` (in the template) | WRB per spec | `SQ FT` | `=CEILING(SQFT*1.1,10)` |
| same takeoff | `Insulation` | exterior `1" Insulation` or Zip R | `SQ FT` | as WRB |
| `walls/1st floor walls/ext ...` | `Wall Sheathing` as a second row | `5/8" Type X` (exterior gypsum) | `SQ FT` | [Exterior Wall Materials](exterior-materials.md) |

The spec lives in the template cells: O3 sheathing, O4 WRB, O5 Zip, O6 Zip Tape,
and P holds a bare sheet reference (`S3.0`, `8/S3.0`, without the word "per"). It is filled in when
the job is created. The Box Sheathing and Holdowns rows sit at the end of the floor's wall section.

## Common mistakes

- Openings not subtracted (garage doors) or subtracted twice (doors on two floors).
- Thickness and product inherited from the previous building instead of read from this set.
- `Vapor Barrier` and `Tyvek` with a fluid-applied barrier in the spec.
- Arch vs structural conflict resolved silently, without a Note citing both sheets.
- Interior gypsum, interior insulation or sound batts counted.
- Area measured in the app, but the old number stayed in Excel.
- The same layer counted both in the wall and in the gable or parapet.

All sheathing mistakes: [common-mistakes](../../../start/common-mistakes.md#sheathing).

## Example

```text
1st Floor Walls
Wall Sheathing      7/16" Zip        214   4x8     8/S3.0
Tape                Zip Tape        2740   LFT
Insulation          Zip R-3         6850   SQ FT   A2-00
Note: Wall Sheathing 7/16" Zip R3 per 8/S3.0 A2-00.
Box Sheathing       7/16" Zip         21   4x8
Tape                Zip Tape         270   LFT
```

<figure markdown>
  ![House sheathed with Zip System](../../../assets/images/confluence/confluence-093.jpg)
  <figcaption markdown="span">Zip System: panel and WRB in one product, the Tape row is required. The gable triangle is in the gables branch, the wall below is in walls. Archive photo.</figcaption>
</figure>

## See also

- [Exterior Wall Materials](exterior-materials.md) - exterior gypsum, insulation, flashing, bracing
- [Shear Wall](shear-wall.md), [Box Sheathing](box-sheathing.md), [Truss Heel](truss-heel.md), [Gable Sheathing](gable.md)
- [Exterior Walls](../walls/exterior.md), [Parapet](../walls/parapet.md)
- [Tips and key rules, Sheathing](../../../reference/boss-feedback-rules.md#sheathing)
