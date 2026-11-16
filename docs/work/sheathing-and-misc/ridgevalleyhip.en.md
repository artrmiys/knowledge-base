# Ridge / Valley / Hip

<figure markdown>
  ![Ridge, hip and valley on a roof plan](../../assets/images/roof/ridge-valley-hip.svg)
  <figcaption markdown="span">Ridge is the top line, hip is the outside sloped edge, valley is the inside one. On the roof plan these are three different line types.</figcaption>
</figure>

## What it is

- **Ridge**: the horizontal line where two slopes meet at the top.
- **Hip**: the sloped outside edge, the slopes meet at a convex corner.
- **Valley**: the sloped inside edge, the slopes meet at a concave corner.

On a truss roof all three lines are part of the trusses by others; we count only
what is shown loose: ridge board between gable trusses, overframe valley sleepers,
flashing. On a stick roof the ridge beam, hip and valley rafters are
our framing. Details for each element: [Ridge](../horizontal/roof-framing/ridge.md),
[Hip](../horizontal/roof-framing/hip.md), [Valley](../horizontal/roof-framing/valley.md).

## Where to find it on the plans

| Sheet | What to take |
| --- | --- |
| Roof framing plan (S) | Trusses or rafters; size of the ridge beam, hip and valley rafters, LVL/PSL |
| Arch roof plan (`a105 rf`) | Ridge, hip, valley lines; lengths; overframes |
| Details (`d`) | Ridge beam bearing, posts under the ridge, valley sleepers, metal valley |

## How to measure in OurPlanCore

1. Ridge beam: Beam tool along the span between supports, takeoff in
   `framing/roof framing/beams/<size> <length>` (for example `(2) 1 3/4 x 11 7/8 LVL 22`);
   the tool rounds the length itself.
2. Hip and valley rafters: Line along the edge line on the plan, in
   `framing/roof framing/details/<size> hip` or the job's agreed branch;
   plan length, pitch applied once in the formula.
3. Ridge board between trusses and overframe sleepers: Line in `details`.
4. Metal valley flashing: [Flashing](flashing.md), if in scope.

!!! warning "To be confirmed"
    There is no fixed single branch for hip and valley rafters in the tree; on
    each job keep them in one roof framing folder, not in `sqfts`.

## Takeoff name and DFL row

| Takeoff name | DFL row | Material | Unit |
| --- | --- | --- | --- |
| `framing/roof framing/beams/(2) 1 3/4 x 11 7/8 LVL 22` | `Ridge (2)` | LVL | `pcs` + length |
| `framing/roof framing/details/2x12 hip` | `Hip plates` / rafter per template | `2x12` | `LFT` |
| `framing/roof framing/details/2x12 valley` | `Ridge / Valley / Hip` | `2x12` | `LFT` |

## Common mistakes

- Hip and valley rafters taken as common rafters: they are longer and bigger.
- Ridge beam on a truss roof counted as ours although the trusses are by others.
- Pitch applied twice (in the takeoff and in the formula).
- Framing and roof trim along the same lines merged into one row.

All roof mistakes: [common-mistakes](../../start/common-mistakes.md#roof).

## See also

- [Ridge](../horizontal/roof-framing/ridge.md), [Hip](../horizontal/roof-framing/hip.md), [Valley](../horizontal/roof-framing/valley.md)
- [Overframes](../horizontal/roof-framing/overframes.md), [Flashing](flashing.md)
