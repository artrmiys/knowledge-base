# Cantilevered SQFT

<figure markdown>
  ![Section through a cantilevered floor](../../assets/images/sqfts/cantilevered.svg)
  <figcaption markdown="span">The joists run past the bearing to the outside. On the cantilever the rim, blocking and often holdowns change, and a soffit appears underneath. The cantilever area is a separate Area `cant`.</figcaption>
</figure>

## What it is

A cantilever is part of a floor, roof or deck that extends past the bearing with no
post underneath. The cantilever area is counted separately because it has a different
rim, extra blocking, FRT per the exterior wall rules, and a soffit underneath. In the
deliverable keep a visible `Cantilevered` label so it is clear why the
area is separated. General measuring rules: [Floor SQFT, rules section](1st2nd.md#rules).

## Where to find it on the plans

| Sheet | What to take |
| --- | --- |
| Framing plan (S) | Where the joists run past the wall; direction, cantilever length |
| Details (`d`) | Rim on the cantilever, blocking over the bearing, straps or holdowns, soffit |
| Sections (`sec`) | Height and layers underneath (soffit, insulation) |
| Floor plan (A) | Cantilever outline (bay, bump-out) |

## How to measure in OurPlanCore

1. Area along the cantilever outline on the floor framing plan (W point). Name `cant`.
2. The cantilever joists are drawn with the J Area as part of the joist zone; the `cant` area
   is needed for the soffit, rim and blocking, not for counting the joists a second time.
3. The soffit under the cantilever is `Soffits at Floor Overhangs` by length or area
   ([Soffit and Fascia](../exterior-trims/soffit-fascia.md)).

## Tree name and DFL row

| Tree name | DFL row | Material | Unit | Formula |
| --- | --- | --- | --- | --- |
| `sqfts/cant` | `Cantilevered` label in the floor block | | `SQ FT` | as measured |
| cantilever perimeter | `Rim Board` | per detail, FRT if the exterior wall is FRT | `LFT` | `x 1.1` |
| bearing line | `Blocking` | `2x` between joists over the wall | `LFT` | per detail |
| underneath | `Soffits at Floor Overhangs` | `1x12` / Vinyl / `5/8" Ext Gyp` | `LFT` / `SQ FT` | |
| details | `Holdowns` / straps | only if shown | `pcs` | |

## Common mistakes

- The cantilever dissolved into the floor area, the rim and blocking on it not changed.
- The soffit underneath forgotten.
- Holdowns or straps added without a detail (or missed when there is one).
- Cantilever joists counted a second time through the area.

All area mistakes: [common-mistakes](../../start/common-mistakes.md#sqft).

## Example

```text
Takeoffs/Main/sqfts/
  cant       Area   48 SF   (bay 2nd floor, 2' cantilever)
2nd Floor Framing List
Rim Board (Cantilevered)   11-7/8" LSL Rim   26   LFT   3/S401
Blocking                   2x12              22   LFT   over wall
```

## See also

- [Rim Board](../horizontal/floor-framing/details/rim.md), [Blocking](../horizontal/floor-framing/details/blocking.md), [Joist](../horizontal/floor-framing/joist.md)
- [Balcony](balcony.md), [Soffit and Fascia](../exterior-trims/soffit-fascia.md)
