# Screws

<figure markdown>
  ![Structural screws in a built-up member](../../../../assets/images/framing/screws.svg)
  <figcaption markdown="span">Structural screws (SDS, SDWS, SDWC) per connection details: ledger to trusses, LVL packs, tie replacement. Counted in pcs by spacing or by the number per connection.</figcaption>
</figure>

<figure markdown>
  ![Ledger screwed to the house wall with hex-head structural screws](../../../../assets/images/photos/hardware/ledger-structural-screws.jpg){ width="360" }
  <figcaption markdown="span">P.T. deck ledger on a wall: hex-head structural screws in pairs at a spacing, a joist hanger at the top. Count screws in pieces per the ledger detail (number per point per spacing), with no washers or nuts. Photo: greenbuildingadvisor.com, [source](http://www.greenbuildingadvisor.com/homes/durable-deck-ties-home-landscape), found via Pinterest.</figcaption>
</figure>

## What it is

Screws are structural screws from the details: `SDS 1/4 x 4 1/2`, `SDWS 22" ledger screw`, `SDWC` (in lieu of H2.5A). They are counted only when the detail names them; we do not count nails. Screws need no washers or nuts. Bolts: [Bolts](bolts.md).

## Where to find it on the plans

| Sheet | What to take |
| --- | --- |
| Ledger details | screw type, spacing or number per truss end (for example, 3 per end @ 16") |
| Built-up beam, multi-ply LVL details | SDS per pack, spacing and rows |
| Roof-to-wall details | `6" SDWC in lieu of H2.5A`: either clips or screws, not both |
| Stair detail | screws for the stringer bottom bearing board |

## How to measure in OurPlanCore

Length from the detail Line (`details/2x10 ledger + screws`, `details/12/S401`), number of connections from the Count. No separate takeoff for screws is needed if they go with the ledger detail.

## Tree name and DFL row

The screws row sits right under its connection, and B holds the screw exactly as the detail calls it: `SDWS22600DB Screws`, without a code `1/4" x 4 1/2" SDS Screws`.

Ledger screws are the `Screws (n) at Ledger` row:

- `n` is the screws at one point (per stud or per truss end), and the point spacing `sp` comes from the detail;
- `G` is the ledger LFT, the same lines as the `Ledger` row;
- the screw count is `x = G*12/sp*n`, with no separate allowance;
- one rounding, as on every count row: under 50 round up to even, 50 and over round up to 10: `=IF(x<50,CEILING(x,2),CEILING(x,10))`.

Older books have the old form `Screws 16" o.c. (3)`: spacing in H, a `1.05` / `1.1` allowance and `,3` rounding. Do not write new ledger rows that way.

| A (Label) | B | C | D | E |
| --- | --- | --- | --- | --- |
| `Screws (3) at Ledger` | `SDWS22600DB Screws` | `=IF(G*12/16*3<50,CEILING(G*12/16*3,2),CEILING(G*12/16*3,10))` | `pcs` | `4/S401` |
| `Screws (2)` | `1/4" x 4 1/2" SDS Screws` | connections x 2 | `pcs` | beam-to-post detail |
| `Screws` | `SDWS 1/4 x 4 1/4` | `=4*4*G` per stair | `pcs` | stair detail |
| `Screws 24" o.c.` | `SDWC 6"` | by truss spacing | `pcs` | `in lieu of H2.5A` |

## Common mistakes

- Ledger screws not per the detail: 1 per end instead of 3 (84 became 132).
- Screws taken from another floor, not from their own ledger.
- The ledger row kept the old `1.05` / `1.1` allowance and `,3` rounding: there is one rounding, to even or to 10.
- Details 1 and 3 look alike in the drawing, but the hardware is different.
- Both H2.5A clips and SDWC counted when the detail says "in lieu of".
- Nails counted in pieces.
- [All floor framing mistakes](../../../../start/common-mistakes.md#floor)

## Example

| A | B | C | D | E | G |
| --- | --- | --- | --- | --- | --- |
| `Ledger` | `2x10` | `=CEILING(G/D,1)` | 16 | `4/S401` | 44 |
| `Screws (3) at Ledger` | `SDWS22600DB Screws` | `=IF(G*12/16*3<50,CEILING(G*12/16*3,2),CEILING(G*12/16*3,10))` | pcs | `4/S401` | 44 |

Ledger: 44 / 16 = 2.75, so 3 boards of 16'. Screws: 3 per stud at 16" o.c., 44 x 12 / 16 = 33 points, x 3 = 99; that is not under 50, so up to 10 = 100 pcs.

## See also

- [Bolts](bolts.md), [Steel Beam Web Fillers](steelbeams.md), [Hardware catalog](../../../../reference/hardware-catalog.md)
- [Hangers](../../../../reference/hangers.md)
