# Returns

<figure markdown>
  ![Return: the box at the corner where the eave turns into the rake](../../assets/images/roof/returns.svg)
  <figcaption markdown="span">A return is the short piece of eave that turns onto the gable and dies into the rake. A separate takeoff, a separate set of trim.</figcaption>
</figure>

## What it is

A return (eave return, cornice return) is the box at the gable corner where the
horizontal eave turns into the sloped rake. Two kinds: a proper
cornice return (soffit + fascia + crown) and a pork-chop (a simple triangular
stub, but it still has fascia and a small soffit). A return is part of neither
the eave nor the rake: different framing and a different set of rows.

<div class="kb-gallery">
  <a class="kb-gallery__item" href="../../../assets/images/trims/ext-pork-chop.png">
    <img src="../../../assets/images/trims/ext-pork-chop.png" alt="Pork-chop return">
    <div class="kb-gallery__caption">Pork-chop return: a triangle, we count fascia and soffit</div>
  </a>
  <a class="kb-gallery__item" href="../../../assets/images/trims/ext-eave-return.png">
    <img src="../../../assets/images/trims/ext-eave-return.png" alt="Cornice return">
    <div class="kb-gallery__caption">Cornice return: soffit, fascia, crown as a separate set</div>
  </a>
</div>

## Where to find it on the plans

| Sheet | What to take |
| --- | --- |
| Elevations (`el`) | Whether there are returns, how many corners, type |
| Architectural details (`d`) | Pork-chop or cornice; return length, trim |
| Roof plan (`a105 rf`) | Where the eave meets the rake |

Returns are not shown on the structural sheets: open the elevations and details.

## How to measure in OurPlanCore

1. Line tool along the short return piece along the gable wall, on the
   roof plan or elevation. LFT unit.
2. Name `returns <overhang in inches>`: `returns 12`. Folder `eves rakes/rakes`
   or `eves` per the job's agreed tree; a name with `returns` is routed
   like a rake.
3. One return = one segment; the number of corners shows in the number of takeoffs.

## Takeoff name and DFL row

| Takeoff name | DFL row | Material | Unit |
| --- | --- | --- | --- |
| `eves rakes/rakes/returns 12` | `Rafter Frame for returns` | `2x4` per detail | `LFT` |
| same line | `Soffits at Eves` (part) / `Fascia` | per detail | `SQ FT` / `LFT` |
| cornice | `Crown` at returns | per detail | `LFT` |

## Common mistakes

- Returns dissolved into the overall eave line.
- Type not determined (pork-chop vs cornice): different trim and SQ FT.
- FRT for exposed wood not checked.

All roof mistakes: [common-mistakes](../../start/common-mistakes.md#roof).

## Example

```text
Takeoffs/Main/eves rakes/rakes/
  returns 12      Line  8 LFT   (4 corners at 2')
```

## See also

- [Eve / Eave](eve.md), [Rake](rake.md)
- [Soffit and Fascia, Returns section](../exterior-trims/soffit-fascia.md)
