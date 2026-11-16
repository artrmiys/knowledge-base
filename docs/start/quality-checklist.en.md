# Pre-delivery check

Checklists by section, in the order of the "Work" menu. Go through all of them before every
delivery; plan 30-60 minutes for a full check, especially for items that come in large
numbers. What exactly has been found in reviews and what it looks like:
[Common mistakes](common-mistakes.md).

## General

- [ ] Scale checked against a dimension on every takeoff sheet, not against the label.
- [ ] Arch, Structural, specs, schedules, wall types, RCP read before the bulk of the takeoff.
- [ ] Project scope (`Frame`, `Wall panels`, `EWP by others`, `NO metal`, `EXT`) understood and reflected in the DFL header.
- [ ] Each floor recorded separately; identical floors marked with a note, but materials still listed.
- [ ] Each takeoff in the tree has its own color; names follow the [tree](takeoff-structure.md) canon.
- [ ] Nothing doubled: no item ended up in two branches (a wall in both `units` and `walls`, a canopy in both `eve` and `canopy`).

## Walls {#walls}

- [ ] The type of each wall run (ext, corridor, demising, unit, furring) taken from the wall schedule, not assigned as a group.
- [ ] Wall height calculated from the section: floor-to-floor minus subfloor and floor depth; plates are not deducted (this is the height of the assembled wall, the stud is picked from it). Exact heights recorded (`9'-1 1/8"`). [Wall height](../work/vertical/walls/exterior.md#stud-height).
- [ ] P.T. plate only on concrete and masonry; double bottom plate only where a detail shows it.
- [ ] Bearing walls: plies and spacing from the stud schedule of their own floor; extra plies on a separate Extra row.
- [ ] Corridor 2x4 staggered = two rows at 16", 2x6 plates.
- [ ] Shaft walls recorded, material determined (CMU, shaftliner, wood); trash chute not missed.
- [ ] Metal studs: counted with gauge, or a `by others` note per the client rule.
- [ ] Wall panels: walls under concrete, inside an existing frame, short and sloped walls counted as stick; exterior build-up walls checked against the assembly and scope, not automatically excluded from panels; being next to CMU is no reason for optional stick.
- [ ] FRT by construction type: Type III - everything in the plane of the exterior wall is FRT, no LVL/PSL there; if the exterior wall is FRT, then blocking and parapets are too.

## Openings {#openings}

- [ ] One point per physical opening, size = the product from the schedule (not the head elevation).
- [ ] Storefront once; a window and a door under one header = one opening.
- [ ] Openings deducted from sheathing, WRB, insulation and the anchor line once, on their own floor; windows under 4' are not deducted.
- [ ] Doors wider than 3'-6" recorded as double; material and fire label stated.
- [ ] Jamb blocking at windows and interior doors; blocking around windows with Zip R or insulation.

## Sheathing {#sheathing}

- [ ] Every assembly read through all layers (ZIP-R by facade type, second gypsum layer, cover board, Z-girt).
- [ ] The exterior sheathing and barrier product taken from the wall types on Arch and the energy notes; thickness, panel grade and which walls and sides are sheathed checked against Structural (general notes, SW schedule); a discrepancy recorded with a note citing both sheets.
- [ ] Product name as in the project; the exterior barrier is called WRB, product from the specification.
- [ ] Shear walls: number of sides per schedule; on a panel job one side is in the panel; `P` = perforated.
- [ ] The FRT subfloor strip, 2' or 4' along the exterior walls of its own floor, when a note requires it ([Subfloor](../work/horizontal/floor-framing/subfloor.md)); box sheathing, truss heel, gables, parapet (inside = outside minus insulation board) counted.
- [ ] Underlayment, sound membrane, 3/4 ply under bathrooms, new subfloor over existing (if the detail requires it).
- [ ] Roof sheathing by pitch from the sheet, correction applied once; H-clips only for square edge, by support spacing and clip model.
- [ ] The measured area made it to Excel and was updated after edits.

## Floor framing and roof {#floor}

- [ ] Every beam mark on every floor; posts and PSL under beams per schedule; a post counted once, on the top floor it supports.
- [ ] Joists only with J Area: direction, spacing, end joists, openings; lengths split in N / L pairs.
- [ ] Rim: product per specification (`11-7/8" Rim`, `LSL Rim`); in a regular workbook in 16' boards (`=CEILING(G/D,1)`), in LFT with `1.05` only on an EWP-only job; rim at roof TJI too.
- [ ] Hangers at both ends, by assembly, model per detail; Zmax outside and on P.T.; DHU only over stair, elevator and shaft walls.
- [ ] Ties along all bearing lines, spacing = truss spacing; `Truss Bracing` for roof trusses over the whole area under them, garage included; `Bracing for Trusses` for floor trusses by lines, not over bearing walls ([formulas](../reference/formulas.md#truss-bracing)).
- [ ] Ledger and fasteners on their own floor as separate rows; bolts, washers, nuts separately.
- [ ] Blocking: two rows for walls 10' and taller; `Blocking for Drywall` at walls parallel to the joists; cabinet blocking: 4 pieces of `2x6` at 14' for each kitchen and 1 piece at 14' for each bathroom.
- [ ] Stairs multiplied by the number of stairs; stringers per detail.
- [ ] Attic draft stop as a separate row in `Gable Walls`, in SQ FT; at piggyback trusses (a truss built in two parts by height) `2x6` sleepers between the parts; flat roof curb blocking `(2) 2x6 P.T.` if nothing is specified; densdeck or cover board on a flat roof.
- [ ] Eaves: all runs; canopy and porch not in eve/rake; dropped soffits per RCP.

## Areas, deck and porch {#sqft}

- [ ] Areas follow the real outline; balconies and porch as separate Front Page rows.
- [ ] Each balcony and porch block has its own multiplier, formulas from its own header; porch counted independently of balconies.
- [ ] Railing: as a system (composite) or by component (wood painted), not mixed; all outdoor lumber P.T., roofed or not.
- [ ] Porch: ceiling joists, ledger, hangers; framing not shown - note `assumed; verify`.

## Shear walls and holdowns {#holdowns}

- [ ] Holdown model per the SW schedule of its own building and floor; one to concrete, two through a wood floor.
- [ ] Anchors by spacing and by SW, type from the detail; washers by the model in the schedule, `3x3 Square` only when no model is named; double-sided SW = double anchorage.
- [ ] A35 and other SW hardware only where notes or details require it.

## Excel DFL and notes {#excel}

- [ ] Formulas from the block's own inputs; the first row of every new formula checked; 1.1 not applied twice.
- [ ] Copied blocks: references point to their own floor, detail labels corrected.
- [ ] Units in D: `LFT` for linear items, `pcs` for hardware, `4x8` for panels, `SQ FT` for areas; lumber by the piece has the board length in D and the formula divides by D; the label matches the calculation.
- [ ] File formatting per the [format checklist](../reference/dfl-overview.md#checklist): headers, prefixes and yellow fill of notes, color-coded options, groups, types in F.
- [ ] Notes: main ones in the header, local ones in their block; natural phrase, up to 80 characters, `per <sheet>`; every optional has a reason; a note does not contradict its row.
- [ ] Template notes checked against scope (`Walls are panels by others` only with panel scope); zero and unused rows deleted.
- [ ] Front Page: Customer, Date, Total pages, areas by floor, porch and balcony.
- [ ] A different grade or material on a separate row (MSR, P.T., FRT).

## Delivery {#delivery}

- [ ] OurPlanCore job saved; PDF only of sheets with takeoffs, one per building.
- [ ] Processed xlsx made after the last edit, notes and rows in place.
- [ ] If [Auto Link](../reference/ourplancore-excel.md#auto-link) was used: `Probable` rows reviewed right away, wrong ones removed.
- [ ] If the workbook has [Link to Excel](../reference/ourplancore-excel.md#link-list): no links in `Pending`, `Conflict` or `Broken`; before delivery to the client, links removed with `Remove All Links from This Workbook...`.
- [ ] Revision: `Changes.txt` filled in (`Changes` and `Open items`), every item confirmed by a sheet of the new set; nothing open presented as fixed.
- [ ] Revision: "before / after" comparison with the previous delivery in Excel and PDF: what was added, what was removed, note wording.
- [ ] The delivery folder is named like the client folder at intake; source drawing PDFs not sent.

## AI-assisted check

A finished DFL can be given to an assistant for an extra cross-check: sections by scope,
missing rows, quantities with questionable units. Accept only a
specific report with sheet references and check it by hand; the manual checklist
is still required.

## See also

- [Common mistakes and how to avoid them](common-mistakes.md)
- [Tips and key rules](../reference/boss-feedback-rules.md)
- [Workflow](workflow.md)
