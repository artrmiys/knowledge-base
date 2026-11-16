# Other: bookmarks, calculator, sheet windows, templates, import

Here: small features that are on by default but almost never used in E-Wood measuring: Bookmarks, Quick Calculator, detached sheet windows and `Tile M2`, the Templates tab, PlanSwift and PDF Takeoffs import. Each is described briefly: what it does, where the button is, when it may come in handy.

## Bookmarks { #bookmarks }

The Bookmarks module (on). A bookmark remembers the sheet and the view position, so you can come back to a spot on a large plan.

| Action | How |
| --- | --- |
| Add a bookmark for the current view | `B`, then `K` (a sequence, up to 0.9 s between presses) |
| List | the `Bookmarks` sub-tab in the Pages panel (`Bkm`): columns `Name`, `Page`, `View` |
| Open | `Enter` or double-click the row |
| Delete | `Delete` |
| Dock under Pages | the button in the tab header; back - `Return Bookmarks to the tab list` |

Bookmarks are stored in the job (`bookmarks.json`). Crop bookmarks with a PNG are created by the AI module (`Save AI crop here`, `AI Crop +` in the AI console), and the selected bookmark goes into the AI terminal context ([console](ourplancore-ai-console.md#context)); this is full version only. In everyday work, the tabs of open sheets and `F` (fit the sheet) play the role of bookmarks.

## Quick Calculator { #calculator }

The Quick Calculator module (on). The calculator button on the right command strip (palette command `Quick Calculator`) slides out a `Calculator` panel to the left of the strip: regular operations and a `Feet + inches + fraction` line with the result in decimal feet (`= 9.09 ft`). Handy for turning `9'-1 1/8"` into `9.09` for a wall name without leaving the app. It closes with the same button or the panel X.

## Detached sheet windows and Tile M2 { #detached }

The Detached Sheets module (on). A sheet can be opened not as a tab but as a separate window and moved to a second monitor.

| Button | Where | What it does |
| --- | --- | --- |
| `Open > Open as Tabs` / `Detach to windows` | Pages header | open the selected sheets as tabs or as separate windows |
| `Tile M2` (the dot next to it - vertical layout) | Pages header | open the selected sheets as windows and tile them on the second monitor |
| close button with a menu | Pages header | `Close every other sheet tab and all detached windows...`, `Close all detached sheet windows on monitor 2` |
| `Detach`, `Tile M2` | Sheet Manager | the same from the sheet table |

All tools work in a detached window, including Beam and Openings, `Ctrl+C` / `Ctrl+V` copying between windows and `Ctrl+Z`. Clicking a detached window makes it the Pages navigation target: selecting a takeoff in the tree opens the sheet in it. Legend groups and the mask show the same in the main window, a detached window and the PDF.

## Similar across all sheets { #similar }

The `Similar` tool finds identical symbols from a sample; the checkbox `Search all sheets in this job` extends the search to the whole job (up to 80 sheets per run). Steps, thresholds and traps: [Editing and snapping](ourplancore-editing.md).

## Templates: tree and takeoff presets { #templates }

The Takeoff Templates module (on). The `Templates` tab next to `Takeoffs` and `Estimating` (it can also dock under Pages with the button `Pop Templates out into a panel docked below Takeoffs`) shows a tree of presets: folders and Line, Area, Count takeoff presets with name, type and color.

| Action | How |
| --- | --- |
| Create a takeoff from a preset | right-click the preset > `Create New Takeoff`: the takeoff is created in the selected Takeoffs folder with the preset's name and properties |
| Edit presets | expand `Edit`: `Folder`, `Line`, `Area`, `Count` add nodes; `Edit`, `Dup`, `Del`; `Reset` restores the built-in set |
| Save for the job | `Job` writes a copy of the tree into the job, `Clear` returns to the global one |
| Settings | `Settings > Takeoff Templates`: the same editor with Auto / COM / EWP modes |

In E-Wood work the tree is built by `More > Auto Tree` from the COM template, and takeoff names carry numbers from the drawing (`ext 2x6 9.09`), so presets with a fixed name are rarely needed: perhaps for repeating Count items like hardware marks.

## PlanSwift and PDF Takeoffs import { #import }

Both imports are for old jobs; a new E-Wood job starts from a PDF ([jobs](job-creation-storage.md)).

| Route | What is added | Where |
| --- | --- | --- |
| `Main > PlanSwift` | a separate converter: an old PlanSwift job folder becomes a new OurPlanCore job | new job |
| `Main > Open / Import > Import into the current job > PlanSwift project...` | sheets and takeoffs of the old job into the open job; the source folder is only read | the `01. planswift` group in Pages and Takeoffs, an import report |
| `Main > Open / Import > Import PDF Takeoffs...` or `Main > PDF Takeoffs` (`Page > ADD > PDF Takeoffs`) | a PDF with someone else's measurement annotations: the app scans the files (with subfolders), shows the lines, areas, points and rulers found, asks whether to use a new or the current job | the `from pdf` group; a report `import_reports/pdf_takeoff_import_<date>.md` inside the job |

PlanSwift Item and Note formulas are not carried over ([known limitation](ourplancore-ideas.md)); takeoff names are brought to the canon by hand after import. Any import is rolled back with `Open / Import > Undo Last Page Operation`.

## See also

- [Extra features](ourplancore-extras.md): a table of all moved-out features
- [Sheets (Pages)](ourplancore-pages.md): the panel, sub-tabs, the `Open` button
- [Editing and snapping](ourplancore-editing.md): Similar, Merge, Split, Snap
- [Jobs and saving](job-creation-storage.md): importing PDFs and OurPlanCore jobs
