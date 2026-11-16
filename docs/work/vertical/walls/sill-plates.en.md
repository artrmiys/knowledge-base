# Sill Plates

<figure markdown>
  ![Sill plate assembly on the foundation in section](../../../assets/images/framing/sill-plate-assembly.svg)
  <figcaption markdown="span">The stack on concrete from bottom to top: foundation, sill sealer, termite shield, P.T. sill plate with anchor bolt and washer, wall btm plate, stud. Each layer gets its own DFL row.</figcaption>
</figure>

## What it is

The sill plate is the lowest wood member. It sits on the foundation or stem wall
concrete, so it is always P.T. **A sill plate is not a btm plate**: the wall btm plate
sits on the floor framing above, the sill plate sits under the floor framing on concrete.
Each goes on its own row. It can be single, double or triple,
typically `2x6 P.T.`, but take the size only from the detail.

<figure markdown>
  ![Labeled detail: bottom plate, sill plate, anchor bolt, foundation wall](../../../assets/images/confluence/confluence-155.png)
  <figcaption markdown="span">A connection without a floor (the wall straight on the foundation, as at a garage): wall bottom plate on top, sill plate (red) on concrete, anchor bolt through it, foundation wall. With a floor, the rim and joists sit between them, see the text above.</figcaption>
</figure>

## Where to find it on the plans

| Sheet | What to take |
| --- | --- |
| Foundation plan `s101 f` | Length of walls on the foundation and slab; garage separately |
| Typical sill detail, wall section at foundation | Size and number of plies, P.T., sill sealer, termite shield |
| Anchor bolt schedule, SW schedule, general notes | Anchor diameter, embed and spacing, washer size |
| 1st floor plans | Openings (garage doors, doors) subtracted from the sill line once |
| Specs (COM) | Sill plate species (DF, SYP); plate rules are often hidden here |

## How to measure in OurPlanCore

**Line** tool, LFT unit, along the walls on concrete on the foundation plan
or the 1st floor plan. The F dot on `s101 f` puts the Line into
`framing/<floor> framing/details`; the name follows the detail material:
`2x6 P.T. sill`, `4x10 P.T. Sill grge`.

1. Separate lines for the house and the garage, for single and double sill, for
   different sizes.
2. Line length = the length the detail applies to, not the length of the leader on the detail.
3. Sill sealer, termite shield, anchor bolts and washers are figured from the same length:
   these three items are **not shown** on the plan and are easy to forget.
4. Subtract openings (garage doors) once, on their own floor.

<div class="kb-gallery">
  <a class="kb-gallery__item" href="../../../../assets/images/confluence/confluence-160.jpg">
    <img src="../../../../assets/images/confluence/confluence-160.jpg" alt="Sill plate on sill sealer with an anchor bolt" loading="lazy">
    <div class="kb-gallery__caption">P.T. sill plate on pink sill sealer, the anchor bolt comes up out of the slab. This is how it looks on site.</div>
  </a>
  <a class="kb-gallery__item" href="../../../../assets/images/confluence/confluence-156.jpg">
    <img src="../../../../assets/images/confluence/confluence-156.jpg" alt="Termite shield with lap and anchor" loading="lazy">
    <div class="kb-gallery__caption">Termite shield: 1 ft lap at joints, bead of caulk along the edge, anchor through the sheet.</div>
  </a>
  <a class="kb-gallery__item" href="../../../../assets/images/confluence/confluence-170.jpg">
    <img src="../../../../assets/images/confluence/confluence-170.jpg" alt="Sill plate gasket under the sill plate" loading="lazy">
    <div class="kb-gallery__caption">Sill sealer (gasket) between the concrete and the sill plate, anchor bolts, joists and subfloor on top.</div>
  </a>
</div>

## Takeoff name and DFL row

| Takeoff name | DFL row | Material | Unit | Formula / factor |
| --- | --- | --- | --- | --- |
| `2x6 P.T. sill` | `PT Sill Plates at ext. found` | `2x6 P.T.` | LFT | `LFT x 1.1`; double `x 2` |
| same | `Sill Sealer` | `6"` (less often 4", 8") | LFT | `LFT` |
| same | `Termite Shield` | `Copper` | LFT | `LFT x 1.1` (1 ft lap) |
| same | `Anchor Bolts 48" o.c.` | per detail / SW schedule | pcs | `LFT / spacing`, to an even number |
| same | `Washers`, `Nuts` | size per detail | pcs | one per bolt |
| `4x10 P.T. Sill grge` | `PT Sill Plates` garage | `4x10 P.T.` | LFT | on a separate row |

Anchor size, embed and washers come from your detail, not from the template:
[Anchor Bolts](../../deck/anchor-bolts.md). Anchor spacing is split by
run (1st floor SW to concrete have their own spacing), not one spacing for the whole
building. Sill plate species unclear: a visible note, not a silent choice of SPF.

## Common mistakes

- Sill sealer and termite shield missing from the DFL: they are not visible on the plan, but on concrete they are almost always there.
- P.T. plate on wood floor framing: P.T. only on concrete and masonry.
- Double sill or double btm plate everywhere although the detail shows it only on some floors.
- One anchor spacing for the whole building; wedge anchor swapped for Titen HD with no reason.
- Garage doors not subtracted from the sill, sill sealer and anchors, or subtracted twice.
- Washers written as generic 3x3 without checking the table.

Walkthrough with examples: [all wall mistakes](../../../start/common-mistakes.md#walls).

## Example

```text
framing/1st floor framing/details/
  2x6 P.T. sill          Line, 318.0 LFT    Notes: 2/S501, dbl sill at stair
  4x10 P.T. Sill grge    Line, 64.5 LFT     Notes: 5/S501
```

## See also

- [Anchor Bolts](../../deck/anchor-bolts.md), [Exterior Walls](exterior.md), [Basement Walls](basement.md)
- [Corners](corners.md), [Basement SQFT](../../sqfts/basement.md)
- [DFL notes](../../../reference/standard-notes.md)
