# Balcony build-up

<figure markdown>
  ![Balcony section: frame and finish layers with row numbers](../../assets/images/trims/balcony-buildup.svg)
  <figcaption markdown="span">Balcony section at the wall: frame, subfloor, EPDM on the subfloor turned up the wall, sleepers over the membrane, decking on the sleepers. Numbers match the table below: rows 1-6 are counted on the frame page, rows 7-12 here. Pavers and membrane are often by others.</figcaption>
</figure>

## What it is

The map of all balcony layers and the canonical page for the finish layers: post wrap, EPDM, decking
as a finish, soffit underneath, fascia and edge trim, flashing at the wall, an assembly with
pavers. The frame (posts, beam, ledger, joists, hangers, sleepers, subfloor)
is counted on [Deck / Porch / Balcony Frame](../deck/deck-porch-balcony-frame.md),
the railing on [Rails & Decking](rails-decking.md). The
[Balcony Trims](../deck/balcony-trims.md) page is a short pointer here.

## Where to find it on the plans

| Sheet | What to take |
| --- | --- |
| Balcony section A4xx | Layer order: subfloor, membrane, sleepers, decking or pavers |
| Details A5xx (balcony edge, wall flashing) | Fascia, edge trim, soffit, flashing, post wrap |
| Spec and notes | `Pavers Deck System by others`, decking product (DuxxBak, composite) |
| Job scope | Frame only: do not insert rows 7, 10 and 11 |

## How to measure in OurPlanCore

Areas and lengths come from the block size W x D and the number of instances (units)
(see [frame](../deck/deck-porch-balcony-frame.md)). The soffit underneath and the decking
equal the balcony area; trims and flashing go along the perimeter: the front and sides
are open, the wall side gives flashing.

Build order, bottom to top, the way it is built:

- Regular open balcony: posts and beam, joists, decking right on the joists.
- Terrace (over a garage or a room): joists, `Subfloor`, `EPDM` over the
  subfloor, `Sleepers` on top of the membrane, decking on the sleepers. The membrane
  is always under the sleepers: decking is never laid on the membrane.

## Tree name and DFL row

| # | DFL row | Material | Unit | Who counts it |
| --- | --- | --- | --- | --- |
| 1 | `Posts` + `Post Bases` + `Post Caps` | `6x6 P.T.`, per schedule | posts: length in D; bases and caps pcs | frame |
| 2 | `Beam (3)` front, `Beam (2)` sides | `2x12 P.T.` | boards, length in D | frame |
| 3 | `Ledger` + screws, `Box` if the beam is not flush | `2x12 P.T.` | boards, length in D; screws pcs | frame |
| 4 | `Joists` + `Hangers Zmax` + `End Joists` | `2x12 P.T.` 16" o.c. | boards, length in D; hangers pcs | frame |
| 5 | `Sleepers` (Terrace) | `2x4 P.T.` | boards, length in D | frame, pieces per balcony `=CEILING(W*12/16,1)+1` |
| 6 | `Subfloor` (Terrace) | `3/4" Ply` | 4x8 | frame |
| 7 | `Post Wrap` | `1x8` (6x6 post), `1x6` (4x4 post) | LFT | **here**, G = height x 4 sides x posts per balcony; C = G x 1.1 rounded up to 10 (under 50 to 2), x units |
| 8 | `EPDM` (Terrace) | `EPDM`, `60 EPDM` | SQ FT | **here**, `=CEILING(W*D*units*1.1,10)`, same area as the subfloor |
| 9 | `Decking` | per the detail: `2x6 DuxxBak` (balcony), `5/4x6` (Terrace) | SQ FT | **here**, `=CEILING(W*D*units*1.1,10)` |
| 10 | `Soffits at Balcony` | `Beadboard` | SQ FT | **here**, `=CEILING(W*D*1.1,10)*units` |
| 11 | `Fascia Trim at Hdr outside` | `1x12`, `1x10` for a header under 10" | LFT | **here**, G = front W of one balcony (header length); C = G x 1.1 rounded up to 2 (from 50 to 10), x units |
| 12 | `Flashings at Wall` (Terrace) | `Copper` | LFT | **here**, `=W*units`, length of the wall side, no waste |

- Decking is ours: every balcony block ends with a `Decking` row. Leave it
  out only when the drawings say by others in so many words (pavers deck
  system, prefab balcony); then a note instead of the row.
- Decking product not named anywhere: `TBD Decking`; on a panel job with no spec
  `5/4x6` and `assumed` in E.
- `Sleepers` are one run of `2x4 P.T.` strips at 16" o.c. under the terrace decking:
  per balcony `=CEILING(W*12/16,1)+1` pieces, board length in D = the next even
  length above the balcony depth D. A `2x6` size or a second layer only
  when the section shows them.
- `EPDM` and `Flashings at Wall` exist only on a terrace with a membrane; an
  open wood balcony has neither row.
- `Post Wrap` only when the elevation or the detail shows a wrapped post; a bare
  `P.T.` post gets no row.

`Post Wrap`, `Soffits at Balcony` and `Fascia Trim at Hdr outside` (rows 7, 10,
11) are inserted only when trim is in scope, in their own `Balcony Trims` section
after the block, never inside the block. Side beams get fascia trim only when the
detail shows it on them: then G = W + 2 x D. `Decking` (9) and, on a terrace,
`EPDM` (8) and `Flashings at Wall` (12) are rows of the block itself: they are written
on Frame only jobs too when the drawings show them. Size not specified:
`TBD` and the note `Note: All trims to be verified. Scaled per elevations`.

## Assembly with pavers

A balcony on a slab or over a garage instead of decking on sleepers:

| Layer, top to bottom | Scope |
| --- | --- |
| `Porcelain Pavers` + `Thinset Mortar` | usually by others, note `Note: Pavers Deck System are by others` |
| `Roofing Membrane`, `Tapered Rigid Insulation` | check the scope |
| `Conc. Deck`, `Structural Steel` | structural, not trim |

Over a garage with trusses and LW concrete the block is counted as a Terrace:
`3/4" Ply` subfloor, EPDM, `2x4 P.T.` sleepers on top of the membrane, `5/4x6`
decking.

## Common mistakes

- Frame rows duplicated in the finish block (sleepers twice).
- `5/4x6` decking on a regular balcony instead of `2x6 DuxxBak` per the detail.
- Pavers and membrane by others counted as material.
- Trim inserted when the scope is Frame only.
- Decking area without the units multiplier or without the 1.1 waste.
- Decking left out as "by others" though the drawings do not say so.
- A note or text puts decking on the membrane and sleepers under the membrane.
- All mistakes for the section: [Deck, porch, balconies](../../start/common-mistakes.md#deck).

## Example

```text
Block: balcony 12' x 8', 6 units, 2 posts per balcony = 12 posts 6x6, post height 9'

Post Wrap                    1x8          480  LFT    =CEILING(9*4*2*1.1,10)*6      assumed
Decking                      2x6 DuxxBak  640  SQ FT  =CEILING(12*8*6*1.1,10)       5/A550
Soffits at Balcony           Beadboard    660  SQ FT  =CEILING(12*8*1.1,10)*6       6/A550
Fascia Trim at Hdr outside   1x12          84  LFT    =CEILING(12*1.1,2)*6          6/A550

Post Wrap: 9' x 4 sides x 2 posts = 72, x 1.1 = 79.2, rounded up to 10 = 80, x 6 = 480
Decking: 12 x 8 x 6 = 576, x 1.1 = 633.6, rounded up to 10 = 640
Soffit: 96 x 1.1 = 105.6, rounded up to 10 = 110, x 6 = 660
Fascia: front 12 x 1.1 = 13.2, rounded up to 2 = 14, x 6 = 84
```

## See also

- [Deck / Porch / Balcony Frame](../deck/deck-porch-balcony-frame.md), [Rails & Decking](rails-decking.md), [Balcony Trims](../deck/balcony-trims.md)
- [Porch / Deck / Balcony](porch-deck-balcony.md), [Exclusions and J-Channel](exclusions.md)
- [DFL blocks](../../reference/dfl-blocks.md), [Standard notes](../../reference/standard-notes.md)
