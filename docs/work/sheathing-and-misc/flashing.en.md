# Flashing (roof, walls, deck)

<figure markdown>
  ![Roof-to-wall intersection: step flashing and kick-out](../../assets/images/roof/flashing.svg)
  <figcaption markdown="span">Roof-to-wall intersection: step flashing stepped under the siding, kick-out at the bottom. Step flashing is counted in LFT along the intersection, kick-outs by the piece.</figcaption>
</figure>

<figure markdown>
  ![Kick-out flashing at the bottom of a roof-to-wall intersection](../../assets/images/photos/roof/kickout-step-flashing-siding.jpg)
  <figcaption markdown="span">Bottom of a roof-to-wall intersection: the last step of the step flashing turns into a kick-out that sends the water over the siding into the gutter. Step flashing is counted in LFT along the intersection line, one kick-out for each lower end of such a line. Photo: finehomebuilding.com, [source](https://www.finehomebuilding.com/2022/12/12/kickout-flashing-for-seamless-siding-and-trim), found via Pinterest.</figcaption>
</figure>

## What it is

Flashing is metal or tape at joints where water can get under the material:
roof-to-wall intersections (step, kick-out), parapets (cap, coping, drip edge),
horizontal wall joints (band, water table), deck or balcony-to-wall
connections. Flashing around windows and doors is a separate page,
[Window Flashing](../vertical/openings/window-flashing.md): it has different rows
and is split by wall type.

## Where to find it on the plans

| Sheet | What to take |
| --- | --- |
| Architectural sections and details (`sec`, `d`) | Rake, eave, parapet, cap flashing, step and kick-out; they are not on the structural sheets |
| Wall sections | Band flashing, water table, flashing over a build-out |
| Roof plan (`a105 rf`) | Roof-to-wall intersections, chimneys, valleys under metal |
| Deck / balcony details | Flashing along the ledger and under the decking |
| Parapet details | Coping or drip edge on top |

## How to measure in OurPlanCore

1. Line tool along the joint: roof-to-wall intersection, top of the parapet,
   balcony ledger. LFT unit. Kick-outs are a Count of points.
2. Name = product and location: `step flashing`, `drip edge prpt`, `ledger flashing
   blcny`. Folder per the job's agreed tree (`roof misc` or `trims`).
3. Parapet: the parapet top length from `parapets/prpt ...`; coping on a separate
   row or in Drip Edge per detail.
4. Roof, wall and deck flashing are counted independently of opening flashing: they are
   different rows.

!!! warning "To be confirmed"
    There is no single branch for flashing in the tree; confirmed takeoff names
    exist only for windows (Window Flashing). Keep flashing in one folder per job.

## Takeoff name and DFL row

| Takeoff name | DFL row | Material | Unit |
| --- | --- | --- | --- |
| `roof misc/step flashing` | `Flashings at Wall` | step flashing, kick-out `pcs` | `LFT`, `pcs` |
| `parapets/prpt 3.4 3 2 par` | `Flashing` | `Drip Edge` / coping | `LFT` |
| `sqfts/rf mtl 4` (valleys) | `Ice and Water (eves&valleys)` | per spec | `SQ FT` / `LFT` |
| `framing/blcny/details/ledger flashing` | `Head Trim Flashing` / `Flashing(s)` | per detail | `LFT` |

## Common mistakes

- Kick-outs and step flashing at roof-to-wall intersections forgotten.
- Parapet flashing and coping counted twice (Flashing row and Drip Edge).
- Flashing looked for only on the structural sheets.
- Roof flashing mixed into the Window Flashing rows.

All roof mistakes: [common-mistakes](../../start/common-mistakes.md#roof).

## Example

```text
Flashing             Drip Edge            186   LFT   parapet top, 5/A501
Flashings at Wall    Step flashing         64   LFT   roof to wall, 7/A502
Kick-out             pcs                    4   pcs
```

## See also

- [Window Flashing](../vertical/openings/window-flashing.md), [Exterior Wall Materials](../vertical/sheathing/exterior-materials.md)
- [Parapet](../vertical/walls/parapet.md), [Eve / Eave](eve.md), [Rake](rake.md)
