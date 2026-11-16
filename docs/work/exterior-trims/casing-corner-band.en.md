# Casing, Corner & Band

<figure markdown>
  ![Exterior PVC window casing with a head crown on lap siding](../../assets/images/photos/trims/ext-window-casing-head-crown.jpg)
  <figcaption markdown="span">Top corner of a window: flat PVC casing on the sides and head, a head crown with a cap above it. Casing sides and head are counted in LFT from the opening size; crown and cap are separate rows by the head width. Photo: elitetrimworks.com, [source](https://elitetrimworks.com/products/pvc-rams-crown-2), found via Pinterest.</figcaption>
</figure>

<figure markdown>
  ![Corner board over siding](../../assets/images/trims/ext-cornerboard-vinyl.png)
  <figcaption markdown="span">A corner board covers the cut edge of the siding at the corner. Counted in LFT by the corner height times the number of corners of that type.</figcaption>
</figure>

## What it is

Trim around openings and across the face of the elevation: ext. casing (sides, heads, apron,
mulls), corner boards, band and watertable, head crowns with cap and flashing,
window sills, shutters, louvers, brackets. All of it is wood, PVC or composite
linear stock; siding and cladding are not part of it.

## Where to find it on the plans

| Sheet | What to take |
| --- | --- |
| Elevations | Where there is casing, corner, band; how many corners; shutters and louvers by window |
| Window and door details (A5xx, A6xx) | Casing profile (`5/4x4`), head crown, cap, drip cap, sill, 3-sides or 4-sides |
| Wall sections | Band and watertable, flashing above them, build-up under the corner |
| Spec and notes | Material (PVC, Azek, Hardi trim, vinyl), `All trims to be verified` |

## How to measure in OurPlanCore

Casing, corner and band are Lines in the `trims` root, one item per profile:
`2" casing`, `8" horizontal trim`, `corner 5/4x6`. Elevations have no sheet dot,
so check that the item landed in `trims`. Casing is easier to count
with a formula from the opening list (perimeter of one window x quantity); use a Line
only where the profile follows a complex outline. Shutters, louvers and
brackets are Count points, with their own color and symbol for each takeoff.

## Tree name and DFL row

| Tree name | DFL row | Size | Unit | Rule |
| --- | --- | --- | --- | --- |
| `trims/casing sides` | `Ext. Casing sides` | `5/4x4` | LFT | vertical sides of openings |
| `trims/casing heads` | `Ext. Casing heads` | `5/4x4` / `5/4x6` | LFT | head, often wider; `(at crowns)` as a separate row |
| | `Ext. Casing (apron & sides)` | `5/4x3` | LFT | sides plus apron under the window |
| | `Mull trims` | `5/4x6` | LFT | between ganged windows |
| | `Casing garage doors (sides)`, `Head casing garage dr` | `5/4x8`, `5/4x12` | LFT | overhead doors separately |
| | `Ext. Casing` | `Vinyl J-channel` / `3-1/2" Vinyl casing` | LFT | with vinyl siding, do not duplicate with `5/4` |
| | `Head crowns`, `Crown cap`, `Head flashing` | `3-1/2" crown`, `1x4`, `Drip edge` | LFT | stack over the head: crown, cap, flashing |
| | `Window Sills` | `1" Sill` / `2" Sill` | LFT | when a sill is shown |
| `trims/corner 5/4x6` | `CornerBoards` | `5/4x6` / `5/4x8` | LFT | corner height x number of corners; bays as a separate row |
| `trims/band 5/4x10` | `Band Trims`, `Watertable Trim` | `5/4x10` / `5/4x12` | LFT | plus `Flashing at band` drip edge on top |
| `trims/shutters` | `Shutters - paneled` | `20"x60"` | pairs | a pair per window, size in the row |
| | `Louver vent`, `Brackets` | `24" Dia`, `5-1/2"x7"x?` | pcs | the `?` in the size stays as verify |

- `4-sides` casing runs around the whole perimeter, `3-sides` has no bottom (sill or
  siding). Write this in the row; it changes the LFT.
- Vinyl corner (`4" Vinyl corner`) is a different product, not `5/4`.
- Size not specified: `TBD` in size, `scaled` or `assumed` in E, the note
  `Note: All trims to be verified. Scaled per elevations`.

## Common mistakes

- Casing in one row without splitting sides, heads, mulls, garage.
- With vinyl siding both J-channel and wood casing counted.
- Head crown without cap and drip edge, though the detail shows them.
- Band and watertable without flashing on top.
- Shutters in pcs instead of pairs; shutter size lost.
- Trim around stone or EIFS missed (see [Exclusions](exclusions.md)).
- All Excel and row mistakes: [Excel DFL and notes](../../start/common-mistakes.md#excel).

## Example

```text
Takeoffs/Main/trims/2" casing          Line   412 LFT
Takeoffs/Main/trims/corner 5/4x6       Line   8 x 28' = 224 LFT

Ext. Casing sides    5/4x4   380  LFT   =2*5.5*34 windows     A601
Ext. Casing heads    5/4x6   112  LFT   =3.3*34               A601
Head flashing        Drip edge 112 LFT  =C<heads>
CornerBoards         5/4x6   224  LFT   8 corners x 28'       A201
Shutters - paneled   20"x60" 12   pairs                       A201
```

## See also

- [Overview](overview.md), [Exclusions and J-Channel](exclusions.md), [Furring & Window Jambs](furring-and-jambs.md), [Soffit & Fascia](soffit-fascia.md)
- [Windows and Doors](../vertical/openings/windows-doors.md), [Window flashing](../vertical/openings/window-flashing.md)
- [Trim macros](macros.md), [Standard notes](../../reference/standard-notes.md)
