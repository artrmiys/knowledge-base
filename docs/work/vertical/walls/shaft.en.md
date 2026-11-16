# Shaft Walls

<figure markdown>
  ![2" H-stud and C-runner with shaftliner panels](../../../assets/images/walls/shaft-h-c-assembly.jpg)
  <figcaption markdown="span">Type 2 assembly: 1" x 24" shaftliner panels between 2" H-studs, 2" C-runner around the perimeter. Source: PABCO Gypsum, H-Stud ASW.</figcaption>
</figure>

## What it is

A shaft wall encloses a vertical shaft: elevator, vent duct, trash chute,
mechanical. It is almost always fire-rated and almost always built from metal
studs with a gypsum liner, so it is neither a regular partition nor
[Metal Tracks](metal-tracks.md). Two working types: `2-1/2" CH + J-channel`
(one liner layer) and `2" H + C-channel` (two layers). A CMU elevator gives no wood
or liner framing.

## Where to find it on the plans

| Sheet | What to take |
| --- | --- |
| Floor plans `a101` | Where the shafts actually are: elevator, chute, vent, mech |
| Wall type schedule (`wt`), type `7A` and similar | CH or H, stud size, liner layers, gypsum outside |
| Shaft details `a806` | Perimeter channels, joint with the floor framing, transition to wood |
| Sections | Shaft height by floor; where the shaft stops above the ceiling |
| S plans | Hangers over the shaft (`DHU`) when joists bear over a fire wall |

## How to measure in OurPlanCore

**Line** tool, LFT unit, around the shaft perimeter on the plan of each floor.
One takeoff per assembly type and height; branch `walls/<floor> floor walls`,
the takeoff is named `shaft`, then the wall type and height (for example `shaft 7A 10.5`).
The `SHF` button on the XL ribbon builds the Shaft walls block above the first framing sheet.

1. A typical detail is not a quantity by itself: find every shaft on the plan.
2. Always record the material: CMU elevator, metal shaftliner, wood. Do not
   throw a shaft out because of a general note `walls are panels by others`.
3. Do not multiply a wood-to-shaft transition above the ceiling by the full floor height.
4. If the wall type gives a shaft assembly but the plan shows only resilient channel,
   count the resilient channel separately, not a full shaft.

## Takeoff name and DFL row

Type 1, `2-1/2" CH + J-channel`, one liner layer:

| DFL row | Material | Unit | Formula |
| --- | --- | --- | --- |
| `Linear Panels` | `1" Shaft Panels` | 2x12 panels | `LFT x 1.1 / 24`, to 2 |
| `CH Channels Vertical` | `2-1/2" CH-channels` | 12' | `LFT x 0.5 x 1.1 / 12`, to 2 |
| `J Channels Horizontal` | `2-1/2" J-channels` | 12' | `horizontal LFT x 1.1 / 12`, to 2 |

Type 2, `2" H + C-channel`, two liner layers (`x 2` multiplier on the panels):

| DFL row | Material | Unit | Formula |
| --- | --- | --- | --- |
| `Linear Panels` | `1" Shaft Panels` | 2x12 panels | `LFT x 2 x 1.1 / 24`, to 2 |
| `Channels Vertical` | `2" H-channels` | 12' | `LFT x 0.5 x 1.1 / 12`, to 2 |
| `Channels Horizontal` | `2" H-channels` | 12' | `horizontal LFT x 2 x 1.1 / 12`, to 2 |
| `Channels Perimeter` | `2" C-channels` | 12' | `perimeter LFT x 1.1 / 12`, to 2 |

Full breakdown of the formulas: [Formulas: Shaft Walls](../../../reference/formulas.md#shaft-walls).
Without a detail, write the assembly with `assumed; verify`. Resilient channels:
`CEILING(area x 12 / spacing x 1.1, 10)` only where shown in the wall type;
metal RC under the floor framing is usually by others.

<div class="kb-gallery">
  <a class="kb-gallery__item" href="../../../../assets/images/confluence/confluence-129.png">
    <img src="../../../../assets/images/confluence/confluence-129.png" alt="C-T stud, J-track and J-L corner profiles" loading="lazy">
    <div class="kb-gallery__caption">Type 1: C-T (CH) stud 2-1/2", 4", 6", J-track and J-L corner. Size from the wall type.</div>
  </a>
  <a class="kb-gallery__item" href="../../../../assets/images/walls/shaft-h-stud.png">
    <img src="../../../../assets/images/walls/shaft-h-stud.png" alt="2 inch H-stud" loading="lazy">
    <div class="kb-gallery__caption">Type 2: 2" H-stud, the panels slide into the slots on both sides.</div>
  </a>
  <a class="kb-gallery__item" href="../../../../assets/images/walls/shaft-c-runner.png">
    <img src="../../../../assets/images/walls/shaft-c-runner.png" alt="2 inch C-runner" loading="lazy">
    <div class="kb-gallery__caption">Type 2: 2" C-runner around the perimeter: top, bottom, end cap.</div>
  </a>
  <a class="kb-gallery__item" href="../../../../assets/images/confluence/confluence-131.png">
    <img src="../../../../assets/images/confluence/confluence-131.png" alt="1 inch gypsum shaftliner" loading="lazy">
    <div class="kb-gallery__caption">1" shaftliner: one layer in Type 1, two layers in Type 2. A separate row.</div>
  </a>
</div>

## Common mistakes

- A CMU elevator written as shaftliner, or a type 7A chute wall missed altogether.
- Shafts thrown out as "panels by others".
- Two types mixed into one block: they have different channels and different formulas.
- A wood-to-shaft transition multiplied by the full floor height.
- Hangers over the shaft taken as `ITS` instead of `DHU` per detail.
- Resilient channel counted as a full shaft.

Walkthrough with examples: [all wall mistakes](../../../start/common-mistakes.md#walls).

## Example

```text
walls/2nd floor walls/
  shaft 7A 10.5        Line, 64.0 LFT     Notes: A806 det 3, 2-1/2" CH + 1" liner
  shaft elev 10.5      Line, 48.0 LFT     Notes: CMU per S201, framing by others
```

## See also

- [Formulas: Shaft Walls](../../../reference/formulas.md#shaft-walls), [Demising Walls](demising.md)
- [Metal Tracks](metal-tracks.md), [Hangers](../../../reference/hangers.md)
- [Wall Panels](wall-panels.md): a shaft is not excluded by a general note
