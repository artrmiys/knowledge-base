# Canopy

<figure markdown>
  ![Canopy highlighted in red around the building](../../../assets/images/confluence/confluence-147.png)
  <figcaption markdown="span">Archive 3D view: the canopy framing along the elevations is highlighted in red and lifted out. Its own joists or rafters, an edge beam, attachment to the wall and soffit underneath: a separate block, not part of the main roof.</figcaption>
</figure>

<figure markdown>
  ![Entry canopy on timber brackets](../../../assets/images/photos/roof/entry-canopy-timber-brackets.jpg){ width="360" }
  <figcaption markdown="span">Entry canopy: a shed mini-roof on two timber brackets at the wall, soffit underneath, fascia at the edge. Count the canopy rafters or joists, the edge beam, brackets or posts, the wall attachment, soffit and fascia, all as a separate block. Photo: discoverydreamhomes.com, [source](https://www.discoverydreamhomes.com/), found via Pinterest.</figcaption>
</figure>

## What it is

A canopy is a small roof over an entry or along a facade: its own flat or sloped mini-roof, soffit underneath, attached to the wall with a ledger or a steel plate, sometimes on posts. It is a separate scope and a separate DFL worksheet, `Canopy Framing List`. A porch is bigger and usually on posts: [Deck / Porch / Balcony Frame](../../deck/deck-porch-balcony-frame.md). A canopy is not part of the main roof `eve` and `rake`.

## Where to find it on the plans

| Sheet | What to take |
| --- | --- |
| Elevations, roof plan (A) | where the canopy is, dimensions, slope or flat |
| Canopy details (A5xx, S5xx) | beams, rafters or joists, spacing, wall attachment, posts |
| RCP | canopy soffit: material, layers, soffit framing |
| Roof assembly notes | canopy deck: `3/4" T&G OSB`, tapered insulation, cover board |
| Steel details | steel plate and anchor bolts to the wall or column |

## How to measure in OurPlanCore

| Part | Tool | Branch and name |
| --- | --- | --- |
| Canopy area (deck and soffit) | Area (A) | `sqfts/canopy` or `sqfts/flat canopy` |
| Canopy joists or rafters | J Area (J) | `framing/<floor> framing/joists/flat canopy 2x6 24"` |
| Canopy beams | Beam (B) | `framing/<floor> framing/beams/FB30 12` |
| Ledger to the wall | Line (L) | `framing/<floor> framing/details/canopy ledger` |
| Posts | Count (P) | `framing/<floor> framing/posts/6x6 P.T. 9` |

The floor is the one whose floor framing the canopy attaches to. The canopy has its own slope; a flat canopy has no slope factor.

<figure markdown>
  ![J Area](../../../assets/images/ourplancore/v3/measure-joist-area.png)
  <figcaption markdown="span">J Area: outline, direction and spacing; the app figures the count and the lengths.</figcaption>
</figure>

<figure markdown>
  ![Canopy section](../../../assets/images/roof/canopy-parts.svg)
  <figcaption markdown="span">Canopy at the wall: ledger or steel plate with anchors, joists, edge beam, deck and soffit. The canopy is not part of eve/rake.</figcaption>
</figure>

## Takeoff name and DFL row

Export: the FR and JS buttons on the XL ribbon put the canopy takeoffs into `Canopy Framing List`; if the worksheet does not exist, it is created as a copy of the nearest floor. Block contents per detail:

| A (Label) | B | C | D | E |
| --- | --- | --- | --- | --- |
| `Beams (3)` | `2x10` | points | `12` | `FB30` |
| `Plates (2) with steel plate` | `2x10` | LFT / 16 | `16` | attachment detail |
| `Rafters 16" o.c.` or `Joists 24" o.c.` | `2x10`, `2x6` | from J Area | lengths | |
| `Hangers` | `LUS210`, `HUC210-2` | per connection | `pcs` | |
| `Anchor Bolts` + `Washers` + `Nuts` | `3/4" Ø x 5"` | per detail | `pcs` | steel plate to the wall |
| `Roof Sheathing at Canopy` | `3/4" T&G OSB` | SQ FT / 32 x 1.1 | `4x8` | |
| `Tapered Insulation` | per spec | SQ FT | `SQ FT` | |
| `Soffits at Canopy (2)` | `5/8" Glassmat` or `5/8" Ext Gyp` | SQ FT x layers | `SQ FT` | RCP |
| `Frame 16" o.c.` + `Plate (2)` | `2x4` | soffit framing | `LFT` | RCP |

Framing not shown: a note right under the block header: `Note: Canopy framing is not specified; all framing assumed; verify`.

## Common mistakes

- Canopy counted a second time in the main roof `eve` and `rake`.
- Canopy soffit counted as regular gypsum when it needs exterior grade (`5/8" Glassmat`, DensGlass), two layers per detail.
- Soffit area left out of the sheathing and WRB when the detail calls for it.
- Canopy deck taken from the main roof spec when the detail calls for `3/4" T&G` + tapered insulation.
- Wall attachment (steel plate, anchor bolts, washers, nuts) missed.
- Metal stud canopy joists counted as wood or not counted: follow the detail.
- [All roof mistakes](../../../start/common-mistakes.md#roof)

## Example

```text
sqfts/flat canopy                              Area, 96 SF
framing/1st floor framing/joists/flat canopy 2x6 24"    J Area
framing/1st floor framing/beams/FB30 12        3 points
framing/1st floor framing/details/canopy ledger   Line, 24 LF
```

| A | B | C | D | E |
| --- | --- | --- | --- | --- |
| `Beams (3)` | `2x10` | 3 | 12 | `FB30 per S601` |
| `Joists 24" o.c.` | `2x6` | 7 | 8 | `11/A506` |
| `Soffits at Canopy (2)` | `5/8" Glassmat` | 192 | SQ FT | `11/A506` |

## See also

- [Porch SQFT](../../sqfts/porch.md), [Deck / Porch / Balcony Frame](../../deck/deck-porch-balcony-frame.md)
- [Eve / Eave](../../sheathing-and-misc/eve.md), [Soffit & Fascia](../../exterior-trims/soffit-fascia.md), [Roof Types](../../sheathing-and-misc/rooftype.md)
