# Extra features

This section collects what OurPlanCore 3.0 has but everyday E-Wood measuring almost never needs: snapping and tracing, manager tabs, 3D, bookmarks, the calculator, importing old jobs. The "Every day" and "Advanced" level pages give these features one line with a link here, so they do not distract from walls, areas and framing. If you need one of these features, everything is described on the pages of this level.

## What is here and why

Selection criteria (owner's decision, 10/17/2026):

1. **The module is off by default** in `Settings > Modules`: Sheet Manager, Takeoff Manager, Report Builder, Materials, AI, 3D, Job Tracker. Without turning the module on, there are no buttons or tabs.
2. **The feature is not in the measuring work rules.** None of the skills for walls, openings, framing, roofing, shear walls and units mentions Snap, Ortho, Box, Layer Trace, Wall Trace, bookmarks, the calculator, detached windows, tree templates or PlanSwift import. The measuring canon rests on Line, Area, Count, J Area, Beam, Openings, Record, sheet dots, the XL strip and Export PDF.
3. **A newer path replaced the feature.** Report Builder gave way to the XL strip, AI 3D Massing was replaced by the deterministic roof from edges, inserting PDF Takeoffs and PlanSwift is needed only for old jobs.

What stays on its own levels: the Line, Area, Count, J Area, Beam, Openings, Pitch, Ruler, Record tools and copying; W/F/S/U dots; the XL strip; Export PDF and Preview; editing and snapping as one set (Cut, Merge, Split, Break, Ends, Combine, Similar, P Line, Snap, Ortho, Box) on the [Editing and snapping](ourplancore-editing.md) page; Crop to Sheet, the Hide mask, Overlay, legend groups; the 3D roof; Settings; the AI console and Agent Bridge; Workspace.

## Feature table

| Feature | Module, default | When it helps | Page |
| --- | --- | --- | --- |
| Snap, PDF Snap, Ortho, Box | no module, the buttons are always on the strip | a precise outline on a vector drawing, right angles, a rectangle in two clicks | [Editing and snapping](ourplancore-editing.md) |
| PDF Layers, Layer Trace | PDF Layers, on | walls or an outline sit on a separate PDF layer | [Snap and tracing](ourplancore-snap-trace.md#layers) |
| Trace Walls Inside Area | Advanced Takeoff Tools, on | a vector plan: wall centerlines inside an area in one action | [Snap and tracing](ourplancore-snap-trace.md#wall-trace) |
| Trace wall from this point, Trace closed area, Check missed takeoffs | AI, off | requests in AI Inbox for a trace or a check | [Snap and tracing](ourplancore-snap-trace.md#ai-trace) |
| Sheet Manager | Sheet Manager, off | bulk editing of names, scale and raster in a table; `Crop Hints`, `AI Fill` | [Managers](ourplancore-managers.md#sheet-manager) |
| Takeoff Manager | Takeoff Manager, off | the Takeoffs tree as a table with prices | [Managers](ourplancore-managers.md#takeoff-manager) |
| Report Builder | Report Builder, off | the old wall path into `TemplateCom.xlsm` | [Managers](ourplancore-managers.md#report-builder) |
| Materials | Materials, off | a material list from the tree to CSV | [Managers](ourplancore-managers.md#materials) |
| AI Inbox, AI Manager, markers | AI, off | a queue of model requests, symbol samples | [Managers](ourplancore-managers.md#ai-manager) |
| Job Tracker, the `In Progress` button | Job Tracker, off | the job card in the tracker from the app | [Managers](ourplancore-managers.md#job-tracker) |
| 3D: walls and roof, Roof Qty | 3D, off | see the edges of a complex roof in 3D | [3D and Massing](ourplancore-3d.md) |
| AI 3D Massing | turned off in code | no, archive | [3D and Massing](ourplancore-3d.md#massing) |
| Bookmarks | Bookmarks, on | come back to a spot on a large sheet | [Other](ourplancore-extras-other.md#bookmarks) |
| Quick Calculator | Quick Calculator, on | add feet, inches and fractions without leaving the app | [Other](ourplancore-extras-other.md#calculator) |
| Detached Sheets, `Tile M2` | Detached Sheets, on | a second monitor, two sheets side by side | [Other](ourplancore-extras-other.md#detached) |
| Similar across all sheets | Advanced Takeoff Tools, on | one symbol on dozens of sheets | [Editing and snapping](ourplancore-editing.md) |
| Takeoff Templates | Takeoff Templates, on | repeating takeoff presets | [Other](ourplancore-extras-other.md#templates) |
| PlanSwift import, Import PDF Takeoffs | no module | an old job from PlanSwift or a PDF with someone else's annotations | [Other](ourplancore-extras-other.md#import) |

## How to turn a module on { #enable }

1. `Settings > Modules`: check the module, `Apply` (until restart) or `Save global default`; `Save as this job` turns the module on only in the open job.
2. The presets `Current default`, `All modules on`, `Takeoff Only`, `Minimal` set the whole set at once; `Reset` restores the built-in one.
3. A module that is on adds its tab to the mode bar (Sheet Manager, Takeoff Manager, Report Builder, Materials, AI Manager, 3D) or buttons to the ribbon (`Name`, `Scale`, `Name+Scale`, `In Progress`).
4. A disabled module hides its buttons and tab; a key for a hidden command does not fire.

<figure markdown>
  <video class="kb-demo" loop muted playsinline preload="none" poster="../../assets/images/ourplancore/demo/d-settings.png"><source src="../../assets/images/ourplancore/demo/d-settings.mp4" type="video/mp4"></video>
  <figcaption markdown="span">Demo: `Settings`, the routing and color sections, then `Modules`: the AI and 3D checkboxes, `Apply` and `Save global default`; the AI Manager and 3D tabs appeared in the mode bar.</figcaption>
</figure>

The full module list with groups: [Workspace and modules](ourplancore-workspace.md#modules).

## Rare items of the measurement menu on the sheet { #measurement-menu }

Right-click on a measurement on the sheet opens the edit menu; copying, Merge, Split and other common items are described on the [Editing and snapping](ourplancore-editing.md) page. Here are the items you need rarely:

| Item | What it does | When you need it |
| --- | --- | --- |
| `Takeoff Properties...` | the properties window of the whole takeoff, same as right-click on the takeoff in Takeoffs | change the name, color or Notes of the takeoff without looking for it in the tree |
| `Section Properties...` (for Count, `Count Properties...`) | name and `Notes` of one measurement (section); for a measurement with no takeoff in the tree, the item is gray and called `Measurement Properties...` | label one piece of a takeoff, for example `per S2.1` |
| `Set / Reset Joist Direction` | on an Area: the joist direction by two clicks on this measurement | turn the joist layout in one area |
| `Set Direction for All Areas` | on an Area: the direction is drawn once by two clicks on this measurement and applied to all Area measurements of this takeoff on all sheets; the takeoff becomes a joist takeoff | many floor framing areas with one direction, like [J Area](ourplancore-tools.md#jarea) |

The joist items show on an Area with the Advanced Takeoff Tools module on (on by default); the same two items are in the right-click menu of a takeoff in Takeoffs. `Notes` comments go to Excel when the dot on the `Excel` button is on ([comments in Excel](ourplancore-excel.md#notes)).

## Pages of this level

<div class="grid cards" markdown>

-   **[Snap and tracing](ourplancore-snap-trace.md)**

    ---

    The PDF Layers tab and Layer Trace; Trace Walls Inside Area; trace requests through AI Inbox. The snaps themselves (Snap, PDF Snap, Ortho, Box) together with measurement editing: [Editing and snapping](ourplancore-editing.md).

-   **[Managers](ourplancore-managers.md)**

    ---

    Sheet Manager, Takeoff Manager, Report Builder, Materials, AI Inbox and AI Manager, Job Tracker: tabs turned on in `Settings > Modules`.

-   **[3D and Massing](ourplancore-3d.md)**

    ---

    Walls and roof from measurements, Roof Qty and Roof Takeoff, what is turned off and why.

-   **[Other](ourplancore-extras-other.md)**

    ---

    Bookmarks, Quick Calculator, detached windows and `Tile M2`, Similar across all sheets, Templates, PlanSwift and PDF Takeoffs import.

</div>

## See also

- [OurPlanCore 3.0: section hub](ourplanecore.md)
- [Settings and modules](ourplancore-settings.md), [Workspace and modules](ourplancore-workspace.md#modules)
- [Ideas and plans](ourplancore-ideas.md): which extras are still in development
