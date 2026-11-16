# Quantity benchmarks

Here: typical values from delivered jobs, so you notice a number of the wrong order of magnitude. This is a sanity check, not a standard: a deviation means "open the detail, units and scope", not "adjust to the average".

## How to use it

1. Counted an item - compare it with what is typical for a similar building and scope.
2. Out of range - check the units (LFT or pcs), spacing, unit multiplier, floor, double waste.
3. Found the reason and it is a feature of the project - keep it, with a note if needed.

## Multipliers (canon in Formulas)

| Factor | Value | Where |
| --- | --- | --- |
| Studs 16" o.c. | x1.1 | a stud per foot plus 10% waste |
| Studs 24" o.c. | x0.625 | 0.5 plus 25% waste |
| Joists | 12 / spacing + 1 | no stud waste |
| General waste | x1.1 | once in the formula |
| Rim EWP | x1.05 | EWP-only jobs only, where rim stays in LFT; in a regular workbook rim goes in 16' boards with no factor |
| Wall bracing | 1 board per 8 LFT of wall, x1.1 | `=G/8*1.1`, in pieces; board length by wall height |

Source of the multipliers: [Formulas and factors](formulas.md).

## Typical stock lengths

| Item | Usually | Note |
| --- | --- | --- |
| Beam | 12' (8 ... 16) | sawn 8 / 10 / 12 / 14 / 16; length from the name in the app |
| Joist | 12' (10 ... 16) | short ones up to 7' go on a double board |
| Stringers | 10' (10 ... 14) | slope length plus bearing: 10.0' = 12' |
| Treads, risers | 12' | |
| Sub fascia, truss bracing | 16' | |
| Posts deck, porch | 10' (8 ... 10) | 6x6 P.T. |
| Blocking | 16' / 8' | stick |

## Typical quantities

| Item | Typical | How to read it |
| --- | --- | --- |
| Foundation anchor bolts | about 66 (34 ... 180) | spacing from the anchorage schedule; SW separately |
| Foundation washers | about 120 (50 ... 224) | one per bolt; two when there is wood on both sides |
| Termite shield | 350 LFT (200 ... 600) | foundation perimeter |
| Beams per floor (Wall Materials) | 3 (2 ... 4) | marks, not pieces |
| Hangers in Wall Materials | 16 (5 ... 62) | only per-row hangers, joist hangers separately |
| Decking posts | 4 (2 ... 8) | 2 per balcony, corner 1 |
| Sub fascia on a flat roof | 27 (18 ... 38) | 16' pieces |

## Ratios between similar buildings

For buildings of the same type, quantities per 1000 SF of floor stay constant: an outlier in one building is a flag. Check sheathing, window and sill flashing, WRB, insulation, draft stop, clips, anchors; area per unit and balconies per unit; porch = balcony when the porch is under a balcony. Loft and attic: subfloor over the full footprint, not just the walkable area.

## Examples where a number was off and was a mistake

| What we saw | Cause |
| --- | --- |
| Clips 1.5 times more than sheets x 4 | counted 4 per sheet instead of by support spacing; or clips with T&G |
| Garage roof sheathing 3 sheets too many | 6/12 pitch instead of 4/12 from the sheet |
| Ties 180 with 390 LFT of bearing | not all bearing lines |
| Balcony decking 900 SF for a 60 SF block | unit multiplier from another block |
| Hangers 154 for 106 joists | by purchase boards, not by assemblies |

## See also

- [Formulas and factors](formulas.md), [Hardware catalog](hardware-catalog.md), [Common mistakes](../start/common-mistakes.md), [QA checklist](../start/quality-checklist.md)
