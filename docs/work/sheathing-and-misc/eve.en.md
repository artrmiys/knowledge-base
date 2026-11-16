# Eve / Eave

<figure markdown>
  ![Roof corner: horizontal eave and sloped rake in OSB sheathing](../../assets/images/photos/roof/rm-eave-rake-corner-osb.jpg)
  <figcaption markdown="span">Roof corner at the framing stage: on the left the sloped rake edge along the gable, on the right the horizontal eave with blocking between the truss tails. Eave and rake are different lines and different takeoffs. Photo: ssukotash, CC BY 2.0, <a href="https://www.flickr.com/photos/20775821@N03/6071724150">source</a>.</figcaption>
</figure>

## What it is

The eave (`eve` in the tree) is the lower horizontal edge of the roof along the wall, an overhang with
soffit underneath and fascia on the end. The rake is the sloped edge on the gable
([Rake](rake.md)), a return is the box at the corner where the eave turns into the rake
([Returns](returns.md)). The vertical strip at the truss heel above the wall is
[Truss Heel](../vertical/sheathing/truss-heel.md), not part of the eave. From one
eave line the export gets the soffit (SQ FT), fascia (LFT), sub fascia and the overhang
framing (16' boards).

## Where to find it on the plans

| Sheet | What to take |
| --- | --- |
| Roof plan (`a105 rf`) | Eave lines around the perimeter, overhang, main vs porch and canopy |
| Sections, soffit detail (`sec`, `d`) | Overhang width, sub fascia `2x6`/`2x8`, frame for soffit `2x4`/`2x6`, soffit material |
| Elevations (`el`) | Fascia, frieze, material changes by elevation |
| RCP | Soffit under canopy and porch (its own branch, not eave) |
| Finish schedule / specs | Vinyl vented, beadboard, fiber cement, exterior gypsum |

## How to measure in OurPlanCore

1. Line tool along the outer edge of the eave on the roof plan. LFT unit.
   All runs: every side of the building, every bump-out.
2. Name: `eve <overhang in inches> <zone>`: `eve 24 main`, `eve 12 porch`,
   `eve 18 upperporch no frame`. Take the overhang from a section or detail, not from the
   line weight on the plan. The `eves rakes/eves` folder is created from the name automatically; do not
   change `eves` to `eaves`.
3. Different overhangs and zones = different takeoffs. Mark runs with no overhang framing in
   the name (`no frame`).
4. Canopy and porch are not part of the eave: they have their own takeoffs and their own block. The main
   mistake is counting them twice.
5. Soffit SQ FT = length x width only when the width is constant. A complex porte-cochere
   or porch soffit is traced separately with an Area, without counting it a second time by
   length.

## Takeoff name and DFL row

| Takeoff name | DFL row | Material | Unit | Formula |
| --- | --- | --- | --- | --- |
| `eves rakes/eves/eve 24 main` | `Soffits at Eves` | `12" Vinyl vented` / `T&G beadboard` / `Soffit panel` | `SQ FT` | `=EVEN((eave LFT + returns LFT)*overhang/12*1.1)` |
| same line, soffit made of one board or one strip across the full width | `Soffits at Eves` | `1x12`, `1x4` | `LFT` | `=EVEN((eave LFT + returns LFT)*1.1)` |
| same line | `Fascia at Eves` | `1x8`, `1x10` or `1x6` per detail | `LFT` | `=EVEN((eave LFT + returns LFT)*1.1)` |
| same line | `Sub Fascia` | `2x6`, `2x8` per detail | `16` | `=CEILING(G/D,1)`, G = LFT of eaves and returns, no 1.1 |
| same line | `Frame for Soffits 24" o.c.` | `2x4`, `2x6` per detail | `16` | `=CEILING(G/D,1)`, G = LFT x overhang / spacing + LFT |
| same line | `Blocking at Eves` | `2x6`, `2x4` or `2x8` per detail | `16` | `=CEILING(G/D*1.1,1)`, G = eave LFT without returns |
| same line | `Simpson Ties at Eves 24" o.c.` | `H2.5`, `H2.5A` per the S notes (no Zmax) | `pcs` | `=CEILING(G*12/H,10)`, H = truss spacing; [Roof Sheathing](../horizontal/roof-framing/roof-sheathing.md) |
| `eves rakes/eves/eve 12 porch` | the same rows in the porch block | per porch detail | | separate from main |

LFT is the line length and the overhang is the number from its name in inches. Excel export:
XL strip, E/R button; the macro reads the overhang number in the name as the width in inches.

Soffit is counted in `SQ FT`: (eave LFT + returns LFT) x overhang / 12 x 1.1. It is in `LFT`
only when the soffit is closed by one board or one strip across the full width
(`1x12`, `1x4`, a single narrow vinyl strip): then the width is not in the formula.
Examples: 12" vinyl panels on a 24" overhang = `SQ FT`; a 9" overhang closed by one
`1x10` = `LFT`. Plywood soffit is written as `AC Ply` in `SQ FT`, not in sheets. Vinyl
soffit is a material row, not a framing row. Aluminum soffit and aluminum-wrapped
fascia are by others: no soffit or fascia rows, only a Note; the sub fascia and the
overhang framing behind them are still counted.

Soffit not named on the plans: default by siding. Vinyl siding = vinyl soffit
in `SQ FT`; wood or composite clapboard = `1x` Azek in `LFT` (if many overhangs
are wider than 12", soffit panel in `SQ FT` for all); cedar shingles = beadboard in
`SQ FT`; Hardie, board and batten and panels = soffit panel in `SQ FT`. If 30%
or more of the soffit is beadboard, count the whole soffit as beadboard and write a Note
that this is a local rule.

`Sub Fascia`, `Frame for Soffits` and `Blocking at Eves` are framing: D holds the 16'
board length, C the number of boards. An aluminum soffit frame, or a short overhang with only
sub fascia and blocking: no `Frame for Soffits` row.

## Common mistakes

- Canopy and porch counted again inside the eave or rake.
- Not all eave runs traced (271 LFT instead of 310).
- Rake and returns merged into the eave although the rows are different.
- Truss heel hidden in the soffit SQ FT.
- `Soffit Eve Vinyl` entered as framing instead of as material SQ FT.
- Panel soffit written in `LFT`, or returns not added to the soffit and fascia.
- `2x4` frame for soffit filled in automatically although the detail calls for `2x6`.
- For a roof of `AJS Rafters` with an open overhang, a simple rake counted instead of rafters by hand.

All roof mistakes: [common-mistakes](../../start/common-mistakes.md#roof).

## Example

```text
Takeoffs/Main/eves rakes/eves/
  eve 24 main          Line  310 LFT
  eve 12 porch         Line   38 LFT
  returns 24           Line    8 LFT
Takeoffs/Main/eves rakes/rakes/
  rake 12 main         Line   96 LFT

Main, 24" overhang (porch is in its own block):
Soffits at Eves              12" Vinyl vented    700   SQ FT   (310 + 8) x 24/12 x 1.1 = 699.6
Fascia at Eves               1x8                 350   LFT     (310 + 8) x 1.1 = 349.8
Sub Fascia                   2x8                  20   16      G = 310 + 8 = 318; 318 / 16 = 19.9
Frame for Soffits 24" o.c.   2x4                  40   16      G = 318 x 24/24 + 318 = 636; 636 / 16 = 39.8
```

<figure markdown>
  ![Eave parts in the takeoff](../../assets/images/roof/eave-parts-takeoff.svg)
  <figcaption markdown="span">One eave line gives several rows: soffit by area, fascia and sub fascia by length, overhang framing per detail.</figcaption>
</figure>

## See also

- [Rake](rake.md), [Returns](returns.md), [Truss Heel](../vertical/sheathing/truss-heel.md)
- [Soffit and Fascia](../exterior-trims/soffit-fascia.md) - materials and LFT vs SQ FT
- [Roof Sheathing](../horizontal/roof-framing/roof-sheathing.md), [Canopy](../horizontal/roof-framing/canopy.md), [Porch SQFT](../sqfts/porch.md)
