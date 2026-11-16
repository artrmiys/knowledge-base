# Reconstruction

Part of the building already exists, part is demolished, part is added. The main
difficulty: do not count the whole building as new, and do not lose the places where new
framing connects to existing.

<figure markdown>
  ![Reconstruction plan: existing, demo, new and connections](../assets/images/work-types/reconstruction.svg)
  <figcaption markdown="span">Mini plan: existing in grey is not counted, demo dashed only if in scope, new in green is counted. Separately the new-to-existing connections: ledger and hangers on the existing wall, header at the enlarged opening.</figcaption>
</figure>

## What it is

A job on an existing building: an addition on top, a re-layout, floor framing replacement,
new openings, roof or porch repair. Scope comes with a tag like
`Frame. Interior trim and Int doors. NO metal` or `Revision`. Panel rules
do not apply here to new walls inside an existing frame:
[Wall Panels](../work/vertical/walls/wall-panels.md#reconstruction-existing).

## How it differs

| | New construction | Reconstruction |
| --- | --- | --- |
| Floor plan | The whole plan is a takeoff plan | The existing floor plan is often just context; measure from the new work plan |
| Walls | Per the wall schedule | Only `New`, `Replace`, `Patch`; do not count `Existing to remain` |
| Panels | Possible | New walls inside an existing frame are always stick |
| Main focus | Completeness | New-to-existing connections: ledgers, straps, anchors, hangers |

## What to count and what not

**Count:** new walls, openings, floor framing and roofing shown as new;
repair and rebuild areas (rotten framing, replaced subfloor, patched roof, rebuilt
porch, new beams and posts); new connections (hangers, straps, anchors, bolts,
blocking, ledgers); bracing, if in the structural notes; envelope: WRB, sheathing
patches, siding backing, insulation, flashing; a new subfloor over the whole
existing floor, if the detail requires it (the old floor is covered entirely).

**Do not count:** existing framing with no changes; demo-only items without demo scope;
existing walls and openings shown for context; old joists and rafters with the note
`existing to remain`; trim with a structural scope; steel partitions with
`NO metal` (note `Metal Studs by others`).

## How to read the marks

| Mark on the drawings | How to read it | What to do |
| --- | --- | --- |
| `Existing` / `E` | Already built | Do not count unless a repair or replacement is shown |
| `Existing to remain` | Stays | Do not add material; check only the connection to new work |
| `Demo` / dashed line | Removed | Count only with demo scope |
| `New` / heavy line / keyed note | New work | Count as regular material scope |
| `Replace in kind` | Replace with the same | Count the replacement area or length, not the whole existing run |
| `Patch` / `Repair` | Local repair | Only the indicated area, plus a note |

## What to look at

| Where on the drawings | What to check |
| --- | --- |
| Cover, code, general notes | What the remodel scope includes; construction type |
| Demo plans | What is removed and what stays |
| New work plans | Where new framing actually appears |
| Structural details | Connections to existing: ledgers, straps, anchors, sistering |
| Elevations, sections | Height changes, roof tie-ins, wall rebuild areas |
| Keynotes | Patch, repair, replace items that are not visible on the plan |
| Photos, field notes | Existing condition, if the drawings are incomplete |

- Legend first: line weights, dashed lines, hatch, keynote symbols.
- An opening is moved or widened: header, king/jack studs, sill, sheathing patch.
- An existing roof or floor is opened up: temporary support, sistering, scab, reinforcement.
- Old member sizes are not the same as new ones: do not assume `2x10` if the detail shows the actual existing member.
- If the drawings show only the repair area, do not multiply it over the whole floor.

## Common items

| Item | When it appears | Check |
| --- | --- | --- |
| Ledgers | New floor, deck or roof to an existing wall | Size, fasteners, P.T. or FRT, spacing |
| Hangers | New joists to an existing beam, wall, ledger | Top mount or face mount, skew, width |
| Blocking | Edge support, drywall backing, roof or floor patch | New or existing? |
| Sistered joists, rafters | Reinforcing an existing member | Length, count, side, fasteners |
| New headers | New and widened openings | Plies, LVL or 2x, bearing |
| Anchor bolts, straps | New wall or ledger to existing concrete or framing | Material, spacing, embed per detail |
| Sheathing patch | Wall, roof, floor repair | Thickness, FRT, Zip, OSB; one side or two |
| New subfloor | Detail "new subfloor over existing" | The whole area of the new layer |

## Common mistakes

- A demo plan taken as a material takeoff.
- A patch area stretched over the whole floor.
- A new subfloor over the old floor missed ("it is already there").
- Steel partitions counted with `NO metal`, or not marked with a note.
- All wall mistakes: [Common mistakes](../start/common-mistakes.md#walls).

## Notes in the DFL

- `Existing framing to remain - not counted.`
- `Counted new work only per shaded/keyed repair area.`
- `Header counted only at enlarged opening.`
- `Ledger and hangers counted at new-to-existing connection per <detail>.`
- `Demo shown for context only - no demo material counted.`
- `Metal Studs by others.`

## See also

- [Wall Panels](../work/vertical/walls/wall-panels.md), [Exterior Walls](../work/vertical/walls/exterior.md)
- [Headers](../work/vertical/openings/headers.md), [Hangers](../reference/hangers.md)
- [Client and job type rules](../start/client-rules.md)
