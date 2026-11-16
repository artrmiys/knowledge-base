# Porch SQFT

<figure markdown>
  ![Porch section: post, beam, soffit, decking](../../assets/images/sqfts/porch.svg)
  <figcaption markdown="span">Porch: a floor on its own frame and a ceiling (soffit) under the roof. The floor area is an Area `porch`; the roof over the porch is its own Area in roof.</figcaption>
</figure>

## What it is

A porch is a covered platform at an entry, on its own frame. Its area gives the floor
(decking or subfloor) and the ceiling (`5/8" Gyp` exterior, two surfaces in
one row with x2). The roof over the porch is a separate area per
[Roof SQFT](roof.md); the porch eave is a separate takeoff `eve 12 porch`.
A porch is counted on its own, separately from balconies, even if it looks similar. General
measuring rules: [Floor SQFT, rules section](1st2nd.md#rules).

## Where to find it on the plans

| Sheet | What to take |
| --- | --- |
| Floor plan (`a101 1st`) | Porch outline, posts |
| Framing plan, details (S) | Ceiling joists, ledger, hangers, beams, posts; framing not shown - Note |
| RCP (`rcp`) | Ceiling material: `5/8" Ext Gyp`, DensGlass, beadboard |
| Elevations, sections | Porch roof, pitch, columns |

## How to measure in OurPlanCore

1. Area along the porch floor outline on the plan (W point). Name `porch`. Several
   identical porches are polygons in one takeoff; different types are different takeoffs.
2. Typical porches in a multifamily building are marked as blocks: one Count
   takeoff per type, a point for every instance (see
   [Deck / Porch / Balcony Frame](../deck/deck-porch-balcony-frame.md)).
3. Trace the porch roof in `sqfts` separately (`rf 4` porch or `rf mtl 4`).

## Tree name and DFL row

| Tree name | DFL row (Porch block) | Material | Unit | Formula |
| --- | --- | --- | --- | --- |
| `sqfts/porch` | Front Page, `Porches` | | `SQ FT` | as measured |
| `sqfts/porch` | `Decking` or `Subfloor` | per detail | `SQ FT` / `4x8` | `SQFT x 1.1` or `/32` |
| `sqfts/porch` | `Ceiling` | `5/8" Gyp` exterior | `SQ FT` | `SQFT x 2 x 1.1` |
| same area | `Ceiling Joists 16" o.c.` + `Ledger` + `Hangers` | per detail | `LFT`, `pcs` | separate from rafters |
| posts | `Posts` | P.T. outdoors; under the roof no P.T. | `pcs` | |

Framing not shown: `Note: Porch framing is not specified; all framing
assumed; verify` right under the block header.

## Common mistakes

- Porch SQFT empty on the Front Page (the house total did not add up).
- Porch mirrored from the balconies instead of counted separately.
- Porch ceiling counted as regular interior gypsum, not exterior.
- Porch roof ended up in the main `rf 6` with the wrong pitch.
- Porch eave counted again inside `eve 24 main`.

All area mistakes: [common-mistakes](../../start/common-mistakes.md#sqft).

## Example

```text
Takeoffs/Main/sqfts/
  porch       Area   96 SF
  rf 4        Area  118 SF   (porch roof)
Covered Front Porch Framing List
Note: Porch framing is not specified; all framing assumed; verify.
Ceiling Joists 16" o.c.   2x8          ...   LFT
Ceiling                   5/8" Gyp     212   SQ FT   x2
```

## See also

- [Deck / Porch / Balcony Frame](../deck/deck-porch-balcony-frame.md), [Porch / Deck / Balcony trims](../exterior-trims/porch-deck-balcony.md)
- [Eve / Eave](../sheathing-and-misc/eve.md), [Soffit and Fascia](../exterior-trims/soffit-fascia.md), [Roof SQFT](roof.md)
