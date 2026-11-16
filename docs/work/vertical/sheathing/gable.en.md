# Gable Sheathing

<figure markdown>
  ![Stick framed gable over a sheathed wall](../../../assets/images/photos/sheathing/sh-gable-stick-framing.jpg)
  <figcaption markdown="span">Gable stick: the framed triangle above the wall's top plate. Gable sheathing is counted from the top of the top plate up to the slope; the wall below is already in walls. Photo: wheezinggirl, CC BY 2.0, <a href="https://www.flickr.com/photos/13073825@N07/3962422200">source</a>.</figcaption>
</figure>

## What it is

Gable sheathing covers the gable triangle under a gable roof, from the
wall's top plate up to the slope. Two types: gable trusses (truss by others,
we count only the sheathing and WRB) and gable stick (we count the framing and the sheathing, see
[Gable Wall](../walls/gable.md)). The heel strip on the eave sides is
[Truss Heel](truss-heel.md). The attic draft stop lives in the same branch, but it is
an interior attic partition, not exterior sheathing.

## Where to find it on the plans

| Sheet | What to take |
| --- | --- |
| Roof plan notes | `Trusses` = gable trusses; `2x10`, `TJI`, `stick` = gable stick |
| Elevations (`el`) | Triangle outline, dormer gables, where the wall ends and the gable starts |
| Sections (`sec`) | Top plate height, pitch, heel |
| Draftstops plan (for example A1-00) and section A4 | Draft stop lines and the attic profile (span x rise) |
| Wall notes / fire rating | Draft stop thickness (`1/2" Ply`, `5/8" Type X`), gable material |

## How to measure in OurPlanCore

1. Area tool along the real face of the gable on the elevation (`a201 el`), including
   steps and dormers. Bottom of the polygon = top of the top plate. Several gables of one
   type can be collected as polygons in one takeoff.
2. For gable stick add a Line `btm` (bottom of the triangle) and `top` (both sloped
   edges): the export figures plates and studs from them.
3. Draft stop: location from the Draftstops Plan sheet, attic profile from the section,
   one Area triangle per line (base = span across the building, apex under
   the ridge). Place it on the architectural roof plan, not on an S sheet. Its own color,
   source sheets in Notes. At hips the triangle is smaller: mark it "check".
4. Do not collect one gable twice from two elevations, and do not put it both in
   gable and in the wall area. Existing gables go in a separate takeoff
   (`existing gable`).

## Takeoff name and DFL row

| Takeoff name | DFL row (Gable Walls block) | Material | Unit | Formula |
| --- | --- | --- | --- | --- |
| `gables/gable trusses/gable` (Area) | `Wall Sheathing` | `7/16" Zip` / `1/2" OSB` | `4x8` | `=CEILING(SQFT/32*1.1,1)` |
| same area | `Vapor Barrier` (WRB), `Tape` with Zip | per spec | `SQ FT` / `LFT` | as for the wall |
| `gables/gable stick/gable stick` (Area) + `btm`, `top` (Line) | `Studs for Gables`, `Plates Ext (3)`, `Blocking` | per [Gable Wall](../walls/gable.md) | | |
| `gables/gable trusses/draft stop` (Area) | `Draft Stop` | `1/2" Ply` or `5/8" Type X` per detail | `4x8` | `=CEILING(SQFT/32*1.1,1)` |

The GB button on the XL ribbon moves the `gables` branch into the Gable Walls block.

## Common mistakes

- Draft stop not counted or copied from the shear wall total (the most frequent miss).
- Area measured, but the old number stayed in Excel.
- Gable counted twice (two elevations, or gable plus wall).
- Truss heel included both in gable and in trussheel.
- Draft stop thickness not checked (`7/16"` vs `1/2"`).
- Plates and studs counted for gable trusses although they are already in the truss.

All mistakes: [common-mistakes](../../../start/common-mistakes.md#sheathing).

## Example

```text
Takeoffs/Main/gables/gable trusses/
  gable            Area   412 SF   (4 polygons, north and south elevations)
  draft stop       Area   318 SF   (3 lines from A1-00, profile from A4-01)
Takeoffs/Main/gables/gable stick/
  gable stick      Area   96 SF
  btm              Line   24 LFT
  top              Line   27 LFT
```

<figure markdown>
  ![Gable triangle diagram](../../../assets/images/sheathing/gable-sheathing.svg)
  <figcaption markdown="span">Gable area is counted from the top of the wall's top plate; the truss heel on the eave sides is a separate trussheel strip.</figcaption>
</figure>

## See also

- [Gable Wall](../walls/gable.md) - stick gable framing and the row table
- [Truss Heel](truss-heel.md), [Wall Sheathing](wall-sheathing.md), [Demising Walls](../walls/demising.md) (draft stop on walls)
