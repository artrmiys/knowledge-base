# Balcony Trims

<figure markdown>
  ![Balcony trim, archive](../../assets/images/confluence/confluence-152.png)
  <figcaption markdown="span">Fascia and edge trim along the open sides of the balcony, soffit underneath, flashing at the wall. Counted only when trim is in scope.</figcaption>
</figure>

## What it is

The finish rows of a balcony block: fascia and edge trim around the perimeter, soffit
underneath, post wrap, flashing at the wall. The full map of layers from frame to
finish is on the canonical page
[Balcony build-up](../exterior-trims/balcony-buildup.md); the frame is on
[Deck / Porch / Balcony Frame](deck-porch-balcony-frame.md).

## Where to find it on the plans

| Sheet | What to take |
| --- | --- |
| Balcony section A4xx, details A5xx | Fascia, soffit (beadboard), flashing, post wrap: material and size |
| Elevations | Visible trims, color and profile, what is hidden by the railing |
| Job scope | Frame only: do not insert trim at all |

## How to measure in OurPlanCore

Lengths and areas come from the block size W x D and the multiplier G, as for
railing. The soffit under the balcony is an Area along the real outline only when
the outline is not a rectangle; W x D is usually enough.

## Tree name and DFL row

| DFL row | Material | Unit | Rule |
| --- | --- | --- | --- |
| `Balcony Trims` / `Fascia` | `1x10`, `5/4x8` | LFT | open sides: `=(W+2*D)*G` |
| `Soffits at Balcony` | `Beadboard` | SQ FT | `=W*D*G` |
| `Post Wrap` | `1x8` | LFT | by post height x 4 sides |
| `Flashings at Wall` | `Copper` / drip edge | LFT | along the wall, `=W*G` |

Size not specified: `TBD` in the material and the note `Note: All trims to be verified.
Scaled per elevations`.

## Common mistakes

- Balcony trims dissolved into the general `Exterior Trims` without their own row.
- Frame rows (sleepers, joists) written into the trims block.
- Trim inserted when the scope is Frame only.
- All mistakes for the section: [Deck, porch, balconies](../../start/common-mistakes.md#deck).

## See also

- [Balcony build-up](../exterior-trims/balcony-buildup.md) (canonical layers)
- [Porch / Deck / Balcony](../exterior-trims/porch-deck-balcony.md), [Rails & Decking](../exterior-trims/rails-decking.md)
- [Deck / Porch / Balcony Frame](deck-porch-balcony-frame.md), [Railing](railing.md)
