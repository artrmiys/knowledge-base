# Client and job type rules

What we count and what we do not depends on the job type and the client. Scope is read from
the tags on the project folder at intake; if the project contradicts a rule below,
the drawings and the client's email win, and the discrepancy goes into a note in the DFL header.

## Job types

| Folder tag / type | What we count | What we do not count | Note in the DFL header | Page |
| --- | --- | --- | --- | --- |
| `Frame` (full framing) | Walls, openings, sheathing, areas, floor framing, roof, hardware | Trim, trims, interior doors | `Roof and Floor Trusses are by others` (check against the set) | [COM](../work-types/com.md), [Residential](../work-types/residential.md) |
| `Frame. Wall panels` (COM w/panel) | Loose scope: bracing, floor-height and box sheathing, truss heel, parapets, gables, shear plywood, holdowns, beams, posts; stick exceptions (under concrete, in an existing frame, short, sloped) | Studs, plates, in-panel blocking and sheathing, typical headers in the panels | `Walls are panels by others` | [Wall Panels](../work/vertical/walls/wall-panels.md) |
| `Frame. EWP by others` | All framing except EWP: posts, sheathing, 2x, hardware | I-joists, LVL/PSL/LSL, engineered rim | `All EWP products are by others`; `Walls are panels by others` is deleted if there is no panel scope | [EWP / Capital](../work-types/ewp-capital.md#ewp-by-others) |
| EWP only (Capital-type) | EWP only: I-joists, LVL/PSL/GL, rim, hangers for them | Regular 2x, trusses, ties, nails | a note on what the scope includes | [EWP / Capital](../work-types/ewp-capital.md) |
| `Revision` / `rev` / `review` | Only the changes between sets; the base is the previous delivery | Do not add old and new takeoffs together | a note about the revision | [Workflow](workflow.md) |
| Reconstruction, `NO metal` | New and replaced stick walls, new-to-existing connections, new subfloor per detail | Existing to remain, demo, steel partitions | `Metal Studs by others`, `Existing framing to remain - not counted` | [Reconstruction](../work-types/reconstruction.md) |
| `EXT` (exterior trim only) | Siding, soffit, fascia, exterior trims, furring, flashing | Framing, floor framing, areas | a note on scope | [Siding](../work/siding/overview.md), [Exterior Trims](../work/exterior-trims/overview.md) |
| Interior trim and interior doors | Base (wood only), casing, crown, doors with material and fire label, shaft CH + liner | Tile base, gypsum (except shafts and exterior soffits), hardware numbers | a note on what the scope includes | [Interior Trims](../work/interior-trims/overview.md) |
| Progress set (a set without structural) | Everything that is visible: walls, openings as drawn, areas; the rest by assumption | Exact beams, posts, shear, heights - only as assumed | A detailed note: `beams, posts, balcony framing, shear walls and wall heights are assumed; verify`; walls under concrete as optional stick with a "verify if metal" note | [Standard notes](../reference/standard-notes.md) |

## Building types that come in

| Type | What to look at |
| --- | --- |
| Hotel | Porte cochere, storage and other buildings as separate branches and workbooks; PTAC openings; a multi-layer facade (ZIP-R by facade type): read through all layers |
| Podium, Type III | Everything in the plane of the exterior wall is FRT: studs, plates, headers, blocking, sheathing; wood walls below the podium are FRT too. No LVL/PSL/LSL in the plane of the exterior wall, do not write "LVL FRT". Walls under the podium are stick, not panels |
| Residential over parking | Parking: exterior-type gypsum and insulation per the assembly; above it, regular COM |
| Condominiums, villas, several buildings | Each building gets its own folder in Takeoffs and its own workbook; identical structure in twin buildings is not a mistake, but each workbook is complete |
| Residential (single house, garage) | Garage, porch, porte cochere have their own outlines and roof pitches; EWP per the specification, not out of habit |

The construction type (Type III, Type V-A, V-B) comes from the Code Compliance Summary on
the cover sheet; it is not a conditional note. Type V has no general FRT. FRT and FRTW are different
designations, write them as in the project. More about FRT:
[Tips: FRT](../reference/boss-feedback-rules.md#frt).

## Metal studs by client {#metal-studs}

| Client | Metal studs |
| --- | --- |
| WM | Count and show |
| Timberline | Count and show |
| Littleton | Count and show |
| EBS | By others |
| Probuild | By others |
| Triangle | By others |
| Interstate | By others |
| Bliffert | By others |

Even when metal is excluded, mark where the metal studs and floors are, and write
`Metal Studs by others`. When we count them: gauge in the name (`6" 18ga mtl`), deflection
track only on full-height walls up to the floor framing, dropped soffits on regular top
tracks. Details: [Metal Tracks / CFMF](../work/vertical/walls/metal-tracks.md).

## What the client's reviewer asked for (October 2026)

Comments on delivered jobs, adopted as rules:

- **Wall panels.** The only walls that are not panels: walls under a concrete slab, in an existing frame,
  short and irregular sloped walls, possibly exterior build-up. A wall next to CMU
  can easily be a panel; do not add optional stick because it is next to CMU.
  Do not automatically exclude exterior build-ups from panels: check the assembly.
- **Optional.** "Be careful calling anything option, unless it totally assumed."
  Option rows get their own color ([Options and color](../reference/dfl-overview.md#options)).
  An optional block must have a note with the reason: what is not specified, what was assumed,
  what to verify. Example: `Optional framing for unspecified roof corridor frame (assumed 2x10 - verify if truss)`.
- **H-clips** only for square edge, not for T&G.
- **New subfloor over an existing floor** per detail: include it in full:
  old building, old floor, the whole floor gets covered.

## Client instructions on hardware

- A holdown over a beam does not need a transfer holdown below (client instruction;
  recorded as a rule).
- Do not delete hardware the engineer shows explicitly, even if it looks unnecessary.
- Hangers: model per detail, Zmax outside and on P.T. How to write them:
  [Hangers](../reference/hangers.md).

## Where this applies

| Rule | Page |
| --- | --- |
| What the panel package includes, stick exceptions | [Wall Panels](../work/vertical/walls/wall-panels.md) |
| FRT by construction type | [COM Commercial](../work-types/com.md), [Tips: FRT](../reference/boss-feedback-rules.md#frt) |
| Doors: labels, fire rating, double doors | [Windows and Doors](../work/vertical/openings/windows-doors.md) |
| Interior: base, tile, common areas | [Interior Trims](../work/interior-trims/overview.md) |
| Notes for by others and assumed | [Standard notes](../reference/standard-notes.md) |

## See also

- [Job types: COM](../work-types/com.md), [EWP / Capital](../work-types/ewp-capital.md), [Reconstruction](../work-types/reconstruction.md), [Residential](../work-types/residential.md)
- [Tips and key rules](../reference/boss-feedback-rules.md)
- [Common mistakes](common-mistakes.md)
