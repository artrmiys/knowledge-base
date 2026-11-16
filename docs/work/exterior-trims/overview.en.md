# Exterior Trims

Exterior Trims are wood, PVC or composite linear stock and products on the outside of the
building: casing around openings, corner boards, band and watertable, head
crowns, soffit and fascia, frieze, columns, porch, deck and balcony trim.
It is a separate scope: not siding, not EIFS, stucco or veneer, and not framing.
We count only the trim material and only when trim is in the job.

!!! danger "What we do not count"
    EIFS, stucco, stone and brick veneer are finish systems by others.
    Canonical page: [EIFS / Stucco / Veneer](../siding/eifs-stucco-veneer.md); the rule
    for the trim scope and J-channel: [Exclusions and J-Channel](exclusions.md).

## What is included and in what order

<div class="grid cards" markdown>

-   :material-window-closed-variant:{ .lg .middle } **Casing, Corner & Band**

    ---

    Ext. casing (sides, heads, apron, mulls), corner boards, band and
    watertable, head crowns with cap and flashing, shutters, louvers, brackets.

    [Casing, Corner & Band](casing-corner-band.md)

-   :material-format-line-spacing:{ .lg .middle } **Furring & Window Jambs**

    ---

    Furring `1x4` / `2x4` under siding and jamb `2x4` / `2x8` / `2x10` in openings.
    They live in the sections, not on the elevations.

    [Furring & Jambs](furring-and-jambs.md)

-   :material-home-roof:{ .lg .middle } **Soffit & Fascia**

    ---

    Soffit and fascia along eaves and rakes, frieze, rake moulding, returns,
    columns.

    [Soffit & Fascia](soffit-fascia.md)

-   :material-balcony:{ .lg .middle } **Porch / Deck / Balcony**

    ---

    Porch trims, flare; hub for railing, balcony layers, pergola.

    [Porch / Deck / Balcony](porch-deck-balcony.md)

-   :material-fence:{ .lg .middle } **Rails & Decking**

    ---

    Canonical page for railing: composite as a system, wood by components, metal by others;
    decking, post hardware, lattice.

    [Rails & Decking](rails-decking.md)

-   :material-layers-triple:{ .lg .middle } **Balcony build-up**

    ---

    All balcony layers: what the frame counts, what the trim counts; assembly with pavers.

    [Balcony build-up](balcony-buildup.md)

-   :material-shower:{ .lg .middle } **Outdoor Shower & Pergola**

    ---

    IPE privacy screen, pergola, trellis, canopy.

    [Shower & Pergola](shower-pergola.md)

-   :material-microsoft-excel:{ .lg .middle } **Trim macros**

    ---

    `C_TrimsCalc`, collapsing duplicates, inserting jambs, pavers,
    balcony, bolts blocks.

    [Trim macros](macros.md)

-   :material-cancel:{ .lg .middle .kb-mk--amber } **Exclusions and J-Channel**

    ---

    What we do not count in the trim scope and where J-channel goes.

    [Exclusions](exclusions.md)

</div>

## Workflow

1. Read the siding material note on the elevations: Hardi, vinyl, cedar, EIFS,
   stone. It decides which trim is possible at all (vinyl often means
   J-channel instead of casing).
2. Open the window and door details, wall sections, eave details: profiles,
   furring, jambs, head crown with cap and flashing.
3. Count by groups: openings (casing), corners and bands, overhangs, porch and
   balcony, products (shutters, louvers, columns).
4. Size not specified: `TBD` and the note `Note: All trims to be verified. Scaled
   per elevations`. Do not make up a product.

## How to measure in OurPlanCore

The `trims` root in the building tree. The physical object sets the takeoff type:
casing, band, corner and fascia are Lines, one item per profile (`2" casing`,
`8" horizontal trim`); soffit and the porch ceiling are Areas along the real
outline; shutters, columns, brackets are Counts. Each takeoff has its own color
and its own point symbol. Elevations and RCPs have no sheet point, so check
where the item landed. Eave and rake lengths come from `eves rakes`, the siding area
from `siding`.

## DFL row

| A Description | B Size | C Qty | D Unit | E |
| --- | --- | --- | --- | --- |
| `Ext. Casing sides` | `5/4x4` | `=2*5.5*34` | LFT | `A601` |
| `Head crowns` | `3-1/2" crown` | `=3.3*34` | LFT | `scaled` |
| `CornerBoards` | `5/4x6` | `=8*28` | LFT | `A201` |
| `Soffits at Porch` | `Beadboard` | `=12*8*G` | SQ FT | `6/A550` |
| `Columns` | `12" Dia Fbg Non-taper w/c&b` | `4` | pcs | `8'` |
| `Shutters - paneled` | `20"x60"` | `12` | pairs | `A201` |

- `LFT` for linear stock, `SQ FT` for panels and beadboard, `pcs` and `pairs`
  for products. Column and post height separately, not inside the description.
- Size and profile always visible (`5/4x4`, `3-1/2" crown`, `4" Vinyl
  corner`); never write a generic `trim`.
- In the trims workbook for macros a row is three columns: Label, Value,
  Unit, see [Trim macros](macros.md).

## Common mistakes

- Trim counted when the scope is Frame only.
- Vinyl siding: J-channel and wood casing on the same openings.
- Canopy and porch counted again in eave and rake; porch SQFT empty on the Front Page.
- A product guessed instead of `TBD` and a note.
- All mistakes: [Excel DFL and notes](../../start/common-mistakes.md#excel), [Deck, porch, balconies](../../start/common-mistakes.md#deck).

## See also

- [Interior Trims](../interior-trims/overview.md), [Siding](../siding/overview.md), [Eve](../sheathing-and-misc/eve.md)
- [Material catalog](../../reference/material-catalog.md), [Standard notes](../../reference/standard-notes.md), [Takeoff item labels](../../reference/takeoff-items.md), [Excel macro hotkeys](../../reference/excel-hotkeys.md)
