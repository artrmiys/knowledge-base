# Loft SQFT

<figure markdown>
  ![Loft with a guard along the open edge](../../assets/images/sqfts/loft.svg)
  <figcaption markdown="span">Loft: the loft floor inside the volume of a story plus a guard along the open edge. The area is a separate Area, not part of the floor below.</figcaption>
</figure>

## What it is

A loft is a loft or mezzanine inside the volume of a story, often over part of the
plan. Its area is counted separately from the floor below it: it drives its own
subfloor, its own joists and the guard along the open edge. On the Front Page the level
is called `Loft`, not the next floor number. General measuring rules:
[Floor SQFT, rules section](1st2nd.md#rules).

## Where to find it on the plans

| Sheet | What to take |
| --- | --- |
| Loft / mezzanine plan (A) | Floor outline, open edge, stair |
| Sections (`sec`) | Height, framing type: floor framing, roof framing or by others |
| Framing plan (S) | Loft joists, beams, bearing; depth and hangers |
| Door / guard notes | Guard along the open edge |

## How to measure in OurPlanCore

1. Area along the loft floor outline on the loft plan sheet (W point). Name `loft`.
2. The open edge (over the room below) is not part of the loft area, but it is needed
   as the guard length: a Line in `trims` or `framing` per the agreed tree.
3. Confirm the framing type: floor joists, roof-type or by others; that decides
   where the joists go ([Joist](../horizontal/floor-framing/joist.md)).

!!! warning "To be confirmed"
    The `loft` token in the name auto-routing is not confirmed: check that the takeoff
    landed in `sqfts`; otherwise move it, or add a rule in
    Settings > Takeoff Name Routing.

## Tree name and DFL row

| Tree name | DFL row | Material | Unit | Formula |
| --- | --- | --- | --- | --- |
| `sqfts/loft` | Front Page, `Loft` | | `SQ FT` | as measured |
| `sqfts/loft` | `Subfloor` in `Loft Framing List` | `3/4" T&G` | `4x8` | `=CEILING(SQFT/32*1.1,1)` |
| Line along the open edge | `Railing` / guard | per detail | `LFT` | |

## Common mistakes

- Loft not found: it is on the architectural sheets, the framing is on the structural ones.
- Guard along the open perimeter forgotten.
- Loft written as `5th` instead of `Loft` on the Front Page.

All area mistakes: [common-mistakes](../../start/common-mistakes.md#sqft).

## Example

```text
Takeoffs/Main/sqfts/
  loft      Area   340 SF
Loft Framing List
Joists 16" o.c.    2x10     ...   LFT   S203
Subfloor           3/4" T&G  12   4x8
```

## See also

- [Floor SQFT](1st2nd.md), [Joist](../horizontal/floor-framing/joist.md), [Stair](../horizontal/floor-framing/stair.md)
- [Railing](../deck/railing.md)
