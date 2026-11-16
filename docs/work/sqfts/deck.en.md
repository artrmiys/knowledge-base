# Deck SQFT

<figure markdown>
  ![Deck section: ledger, joists, beam on posts, decking, railing](../../assets/images/sqfts/deck.svg)
  <figcaption markdown="span">Deck: ledger to the house, joists on hangers, beam on posts, decking, railing. The decking area is an Area `deck`; frame and railing are on their own pages.</figcaption>
</figure>

## What it is

A deck is an open exterior platform with no roof, on its own frame. The decking
area gives the decking, sleepers and underlayment per the detail; the frame (ledger,
joists, beams, posts) is counted on the
[Deck / Porch / Balcony Frame](../deck/deck-porch-balcony-frame.md) page.
On many COM jobs the deck is not in scope: check, do not assume. General
measuring rules: [Floor SQFT, rules section](1st2nd.md#rules).

## Where to find it on the plans

| Sheet | What to take |
| --- | --- |
| Floor plan / site plan (A) | Deck outline, stairs |
| Deck framing plan, details (S) | Ledger, joists, beams, posts, attachment (bolts, screws) |
| Details (`d`) | Decking material, sleepers, underlayment, railing |
| Scope | Whether the deck is in the job |

## How to measure in OurPlanCore

1. Area along the decking outline on the plan (W point). Name `deck`; several decks
   of one type are polygons in one takeoff, different types are different takeoffs.
2. Deck stairs are not part of the area: stringers and steps separately.
3. Railing is a Line along the open perimeter, in `trims` or `framing` per the
   agreed tree.

## Tree name and DFL row

| Tree name | DFL row | Material | Unit | Formula |
| --- | --- | --- | --- | --- |
| `sqfts/deck` | Front Page, `Deck` | | `SQ FT` | as measured |
| `sqfts/deck` | `Decking` | composite / `5/4x6 P.T.` per spec | `SQ FT` | `=CEILING(W*D*units*1.1,10)`: area of one deck x units x 1.1; under 50 round up to 2 |
| `sqfts/deck` | `Underlayment` | `1/2"` per detail | `4x8` | `=CEILING(SQFT/32*1.1,1)` |
| Line along the edge | `Posts at Rails` | `4x4 P.T.`, 4' posts | `4` (post length) | long rails: `=CEILING(LFT/6,1)+1` |
| same line | railing rows by type | per detail | `LFT`, `pcs`, `unit` | [Railing](../deck/railing.md) |

## Common mistakes

- Deck counted though it is not in scope (or the other way around).
- LVL rim used by default: only when a deck attaches to it.
- Railing and stairs forgotten; guards as a separate row.
- Deck area assigned to a house floor.
- Decking without the 1.1 waste or in `LFT` instead of `SQ FT`.

All area mistakes: [common-mistakes](../../start/common-mistakes.md#sqft).

## Example

```text
Takeoffs/Main/sqfts/
  deck       Area   240 SF   (20' x 12', railing on three sides 44 LFT)
Ground Decks Framing List
Decking         5/4x6 P.T.      270   SQ FT   240 x 1.1 = 264, round up to 10
Posts at Rails  4x4 P.T.          9   4       44 / 6 = 7.3, up to 8, plus 1
```

## See also

- [Deck / Porch / Balcony Frame](../deck/deck-porch-balcony-frame.md), [Railing](../deck/railing.md), [Anchor Bolts](../deck/anchor-bolts.md)
- [Rails and Decking](../exterior-trims/rails-decking.md), [Porch](porch.md), [Balcony](balcony.md)
