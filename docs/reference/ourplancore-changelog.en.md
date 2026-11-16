# OurPlanCore - what's new

This page lists what went into OurPlanCore 3.0: the new 3.0 releases first, below them what accumulated in builds 2.2.6-2.2.42. You need it to see which feature was missing in an older version and where to read about it. Releases 3.0.4-3.0.26 are not written up here yet.

## 3.0.30 (11/05/2026)

- **`TemplateCom.xlsm` template:** the formula for the balcony and porch block size now reads the same on a Russian and an English computer ([Two languages](ewood-tab.md#languages)). The numbers in the template did not change.
- **Writing to a closed workbook:** a timeout is now reported as usual; before, it could end in a thread error.

## 3.0.29 (11/04/2026)

- **Auto Link**: a button next to `Link to Excel`, DFL only. One click links `Sure` takeoffs (the label in J equals the name, the number matches) and `Probable` ones (the number matches one to one in column K, with no name) right away. Cell values do not change, the workbook is not saved. Windows, doors and other openings, joists, unnamed points, small unnamed whole numbers are skipped. `Ambiguous` ones are linked in the result window, where **Undo This Auto Link** also is. Look at the result window right away: a `Probable` can land on someone else's row with the same number. Also in Lite. [Auto Link](ourplancore-excel.md#auto-link)
- **Reset All Links**: removes all links of the job after a prompt, cannot be undone, the values in the cells stay. Names leave open workbooks right away, closed ones at the next opening or right away with a second button. [Reset All Links](ourplancore-excel.md#reset-links)
- `Unlink` for a closed workbook: the hidden name now goes away when the workbook is opened while this job is open, instead of staying until `Remove All Links`.

## 3.0.28 (11/04/2026)

- **Link to Excel**: a button next to `Value` and `Excel` writes the number of one takeoff into the active cell of the open workbook and keeps it there. The link goes only from OurPlanCore to Excel; inserting rows does not break it. A closed workbook is updated on ++ctrl+s++ or with `Update Links`. States `Linked`, `Pending`, `Conflict`, `Broken`, the `All Excel Links...` list, settings `Settings > Excel Links`. Before the workbook goes to the client the links are removed: `Remove All Links from This Workbook...`. Also in Lite. [Link to Excel](ourplancore-excel.md#link)

## 3.0.27 (11/04/2026)

- PDF export by default puts measurements in as separate objects that can be edited in Adobe Acrobat; the look stays as in OurPlanCore. In Acrobat lines, areas and labels move; `Count` points and joist areas do not, and the legend is the same type as the points and should not move (it was not tested separately). Adobe does not recalculate labels and the legend. To turn it off: `PDF Output > ADOBE > Editable`, settings `Settings > PDF Editable Export`. Also in Lite. [Editing the PDF in Adobe](ourplancore-pdf.md#adobe)

## 3.0.3 (10/18/2026)

- The sheet legend is split by default into blocks by the current Takeoffs folders. On framing `Posts`, `Beams`, `Details` come first; `SQFTs` after the other measurements. The order and names are edited in `Settings > Sheet Legend` globally or per job. The button next to the crop lock turns off the automatic blocks on one sheet; manual groups stay available. [Sheet legend](ourplancore-sheets-advanced.md#legend)
- On an F sheet, a Count/Points ending in ` Post` goes to `framing/<floor>/posts`, a name ending in ` Stair` with any tool goes to `framing/<floor>/stairs`. [Names and auto-routing](takeoff-naming.md)
- `Crop to Sheet` places crops from the top left corner to the right, then below, with margins and without overlap. If a whole crop does not fit, it is not added; the status suggests a larger or a new sheet. [Crops](ourplancore-sheets-advanced.md#crop)
- On an error, autosave retries after 30, 60 and 120 seconds, then every 5 minutes until it succeeds; the intervals are edited in `Settings > Autosave Recovery`. A temporarily unreadable file is checked every 30 seconds; the protection is lifted only after the data loads successfully. A corrupted file stays protected for manual recovery. [Saving](job-creation-storage.md#autosave)

## 3.0.2 (10/17/2026)

Fixes found while recording the clips for this section. Rollback: the `ourplancore.exe.3.0.1-*.bak` file next to the EXE.

- `Fit` (++f++) puts the sheet in the middle of the work area, not in the top left corner.
- Autosave: if the job file changed while the app was writing the `.ourplan`, it retries by itself. Before, such a race stopped autosave until a manual ++ctrl+s++ (`Save: Failed`). [Saving](job-creation-storage.md#autosave)
- A sheet file that is briefly busy with another write is reread by the app instead of being declared `Save: Protected data` right away.
- 3D: the `rf 6`, `rf 4` roof area sits on top of the walls; before, the pitch digit was read as a floor number, and the slab hung several floors higher. Already saved models are fixed on opening.
- 3D roof: any sheet tool turns off edge selection; ++ctrl++ or ++shift++ with a right-click add an edge without the sheet menu; `Auto` and `Wall` no longer break `Roof Base` groups. [3D roof](ourplancore-3d-roof.md)
- A large sheet no longer stays white after the 3D tab, and undo (++ctrl+z++) survives switching to the 3D tab and back.

## 3.0.1 (10/17/2026)

Fixes found while shooting the screenshots and clips for this section on the sample job. Rollback: the `ourplancore.exe.3.0.0-*.bak` file next to the EXE.

- `Open sample job` works again. The sample is laid out as in real work: sheet copies with the W, F, S and U dots, a tree per the canon, each takeoff on its own sheet, a gable roof from `sqfts/rf 6`, the saved 3D model visible right away. [Sample job](ourplancore-start.md#demo)
- The default tree folder is `basement floor walls` (was `basement foor walls`).
- `New Takeoff Item`: the measurement type shows `Line`, not the record text.
- A new blank sheet gets a W/F/S/U dot from its name; `Duplicate Page` gives the copy a unique name and does not carry over the dot.
- `PDF Output > Preview` keeps the sheet's legend groups.
- `Batch Overlay`: column headers in English, with tooltips.
- ++ctrl+z++ from the ribbon also undoes a `Hide` mask that was just drawn.
- The XL strip and the command strip scroll with the wheel in a short window.
- The tiles of the start card respond to a normal click.

## 3.0.0 (10/17/2026)

Release 3.0.0 is build 2.2.42 plus one fix: the Workspace sync no longer gets stuck on a dialog transcript that is too large (a file over 256 MB is skipped with a warning, the other dialogs sync). Window title: `OurPlanCore 3.0.0 - <job>`. One install in the updates folder `Desktop\updates\OurPlanCore`, the rollback is the `.bak` file next to the EXE. Below is everything that accumulated since 2.2.7 and went into 3.0.0; what 2.2.6 and 2.2.7 themselves brought (a single `.ourplan` file, autosave, Project Data Recovery, live Preview, key editor) is in the [08/15-09/06](#aug-sep) section.

### Where a new takeoff goes

- **W/F/S/U** dots under the Scale label: one dot per sheet decides the folder and floor for any tool; status `Route: W 2nd`. The dot is set automatically from the sheet name (`a` is W, `s` is F, a final `u` is U), and there is a `Route sheets without a dot now` pass.
- **Takeoff Name Routing**: rules by name and tool (`eve`, `rake`, `gable`, `prpt`, `trussheel`, Openings) beat the sheet dot.
- **Green and red dots** in the Takeoffs header: the building for new takeoffs; New takeoffs paste goes into it, copies keep their subfolders (`D3/sqfts` to `D4/sqfts`).
- **Takeoff Colors**: `bft` is always light gray; random colors avoid gray, black and white.
- Details: [Takeoff routing](ourplancore-routing.md).

### Editing measurements

- **Merge and Split of whole takeoffs** from the tree (++ctrl+m++, ++ctrl+shift+m++): by section or by sheet, undo with ++ctrl+z++ in Takeoffs.
- **Break** (++ctrl+shift+b++) and **Break H/V** (++ctrl+shift+v++): lines into segments, horizontal and vertical ones into separate takeoffs. **Ends**: Count marks at the segment ends.
- ++h++ hides the takeoff of the selected segment, the highlighter moved to ++shift+h++. Keys work in the Russian layout.
- Details: [Editing takeoffs](ourplancore-edit-takeoffs.md), [Hotkeys](ourplancore-shortcuts.md).

### Sheets

- **Crop to Sheet**: details from several sheets onto one clean sheet at 100 % scale; rotate, mirror, opacity, order, lock, the `not true scale` badge.
- **Blank Sheet** with size, units and presets; `Change Sheet Size...`; fast zoom on large blank sheets.
- **Hide**: a white mask over the sheet, prints in the PDF. Area markup by box. `PDF Output > Opac` is the line opacity in the PDF.
- **Legend groups** and `Sort Sheet Legend by Key (before space)`. **Batch Overlay** for all floors at once.
- Sheet names across the whole set: tags `rcp`, `demo`, `u`, `base`, `sch`, `in el`, `fin`; OCR for scans; AI from the title block image; learning (the Kept column); sorting by the last word, `rcp` and `demolition` folders.
- Details: [Sheets: Crop to Sheet, Overlay, legend, Hide](ourplancore-sheets-advanced.md), [Pages sheets](ourplancore-pages.md).

### Excel and PDF

- The **XL** strip: new buttons SH, SW, SHF, UN, BL and the framing buttons FR, PS, BM, HD, JS, DT, ST; Framing no longer wipes the template, a repeat run works; details get M flags.
- The "comments" dot on the Excel button: takeoff and measurement notes go into the export.
- PDF: crops and masks print even without Markups, legend groups in the PDF, export by building through the pipeline.
- Details: [Excel export](ourplancore-excel.md), [PDF export](ourplancore-pdf.md).

### AI, workspace, pipeline

- **Claude and Codex** terminals in the window (`>_`) with live sheet context and Quick / Balanced / Deep effort.
- **Agent Bridge**: an agent edits the open job through the app, with undo.
- **Workspace**: a shared server for rules, skills, jobs and dialogs for a second computer.
- **AI Crop Notes**: notes from a schedule in compact rows.
- The **In Progress** button (Job Tracker module), importing an OurPlanCore job into the open one, the `OurPlanCoreCli` pipeline console.
- Details: [AI console](ourplancore-ai-console.md), [AI in the app](ourplancore-ai.md), [Workspace and modules](ourplancore-workspace.md), [Managers](ourplancore-managers.md).

### Settings

Settings grew from 12 to **20 categories** (Blank Sheets, Sheet Takeoff Routing, Takeoff Name Routing, Takeoff Colors, AI Crop Notes, Agent Bridge, Terminals, Workspace); 19 modules (plus Job Tracker). One principle everywhere: Reset, Save global default, Save as this job. Details: [Settings: all categories](ourplancore-settings.md).

## Build history 2.2.8-2.2.42

| Version | Date | What went in |
| --- | --- | --- |
| 2.2.8-2.2.9 | 09/07 | internal: sort Undo only for changed nodes, waiting for autosave before tree edits |
| 2.2.10 | 09/09 | W/F/S dots, gray `bft`, Shift for joist direction, AI Crop Notes, ++h++ = hide, EN/RU keys |
| 2.2.11-2.2.12 | 09/09 | ++h++ turns off the whole takeoff of the selected segment |
| 2.2.13-2.2.14 | 09/11, 09/14 | importing an OurPlanCore job into the open one; UTF-8 BOM fix on import |
| 2.2.15 | 09/15 | Takeoff Name Routing; `units` with 1st-5th subfolders in the COM template |
| 2.2.16 | 09/15 | Save after moving a sheet between folders |
| 2.2.17 | 09/15 | green and red root dots; a renamed `.ourplan` shows the file name |
| 2.2.18-2.2.19 | 09/18 | New takeoffs paste into the selected root; copies keep subfolders, the `Copies keep their source folders` checkbox |
| 2.2.20 | 09/26 | sheet names, scale and sorting across 3534 sheets; Break and Ends |
| 2.2.21 | 09/27 | reading the number across the whole set, OCR, AI from the title block, Kept learning, dot from the sheet name |
| 2.2.22-2.2.23 | 09/27 | `OurPlanCoreCli`; the In Progress button; the rule `a` is W, `s` is F; dot on F2, Batch Rename, Page Setup |
| 2.2.24-2.2.25 | 09/27 | Framing export fixes; SH, SW, SHF, UN, BL buttons; detail M flags |
| 2.2.26 | 10/02 | the "comments" dot on Excel; the H/V dot on Break; PDF export by building (pipeline) |
| 2.2.27 | 10/06 | Agent Bridge |
| 2.2.28-2.2.29 | 10/07 | Merge and Split of whole takeoffs |
| 2.2.30 | 10/09 | Blank Sheet with size and presets; Batch Overlay |
| 2.2.31-2.2.32 | 10/12 | Claude and Codex terminals; Quick / Balanced / Deep; Workspace |
| 2.2.33 | 10/15 | the U row; Sort Sheet Legend by Key; ++ctrl+shift+b++ / ++ctrl+shift+v++; a new color on Split |
| 2.2.34 | 10/16 | Hide (white mask); Area by box; Opac in PDF Output |
| 2.2.35 | 10/16 | Crop to Sheet |
| 2.2.36-2.2.37 | 10/16 | terminal context on sheets with crops; Change Sheet Size; crop mirroring |
| 2.2.38 | 10/16 | legend groups; crop lock, opacity and order; faster crops |
| 2.2.39-2.2.42 | 10/16-10/17 | zoom speed on large blank sheets, timing log |
| 3.0.0 | 10/17 | release: build 2.2.42 plus a Workspace sync fix (a dialog transcript that is too large is skipped, the others sync); file version and window title 3.0.0 |

## 08/15-09/06: builds 2.2.6 and 2.2.7 Preview { #aug-sep }

Until 2.2.8 the app ran on the stable 2.2.5 (07/22), and new work was built into a separate Preview with its own profile and shortcut. Since 2.2.10 there is no Preview: everything is installed into the main updates folder. What went in over those three weeks:

### Jobs and saving

- **A single `.ourplan` file** (08/17): the job became a portable package; on opening it is unpacked into a working copy, and `Save` packs it back. Old folder jobs open with the same `Open project...`. [Jobs and saving](job-creation-storage.md#file)
- **`Save As` with a format choice** (08/20): a new portable file or a compatible folder copy; since 09/01 it is a single `Save As...` item (`Ctrl+Shift+S`) that keeps the format of the open job. [Jobs](job-creation-storage.md#file)
- **Unified job storage** (09/01): one `Open project...` dialog with source folders, a filter and `Open project file...` for an `.ourplan` outside those folders; the `Settings > Project Storage` category with size analysis and `Compact snap.json`. [Jobs](job-creation-storage.md#create), [Settings](ourplancore-settings.md)
- **Package autosave** (09/02): the `.ourplan` file is repacked by itself after a few seconds of quiet and on `Ctrl+S`; status `Save: Saved / Pending / Saving... / Failed`; a retry when the file is temporarily locked. [Autosave](job-creation-storage.md#autosave)
- **Data protection** (2.2.6 Preview, 09/06): a corrupted or locked metadata file is not overwritten with an empty one, `Open / Import > Project Data Recovery...` with `Retry reading` and `Restore from copy...`; a log of sheet operations and `Undo Last Page Sort` / `Undo Last Page Operation`; raster caches are read on long paths too. [If the job did not save](job-creation-storage.md#lost)

### Sheets

- **`Ctrl+Z` brings back deleted sheets and folders** in Pages (08/17). [Sheets](ourplancore-pages.md)
- **Guided PDF metadata analysis** (08/20): `Metadata > Analyze PDF Metadata` goes through one typical sheet of the set and asks you to show the title block areas; the `Crop Hints` button draws three areas, `Sheet #`, `Sheet Title`, `Scale`, which the app uses to find names and scales on the other sheets. [Managers, Sheet Manager](ourplancore-managers.md#sheet-manager)

### Measurements and output

- **Live `PDF Output > Preview`** (09/05): a modeless window of the current sheet that redraws when the ribbon settings change; `Fit`, `-`, `+`, `100%`, wheel zoom, right-button pan, `Save PDF...`. [PDF and delivery](ourplancore-pdf.md#preview)
- **Tools in detached sheet windows** (09/05): Beam and Openings work there too, paste and `Ctrl+Z` are shared between the main and the detached window. [Other, detached windows](ourplancore-extras-other.md#detached)
- **`Repeat Line` and `Repeat Beam`** (09/05): the arrow next to the Line and Beam buttons, a series of segments or beams until `Esc`. [Tools](ourplancore-tools.md)
- **Beam dimension offset** and a line along the beam: `Settings > Defaults > Beam`. [Settings](ourplancore-settings.md)
- **`Move joist note`** (09/05): a checkbox in the Joist Area properties, the zone table can be dragged; the position is saved and printed. [Tools, J Area](ourplancore-tools.md)
- **Paste between sheets with a choice** of `Same takeoffs` / `New takeoffs` / `Cancel` (2.2.7, 09/06). [Copying](ourplancore-takeoffs.md#copy)

### Keys and settings

- **Customizable keys** (2.2.7 Preview, 09/06): a separate `Settings > Keyboard Shortcuts` editor with search, sequences, conflicts, JSON presets, a global and a per-job set, `Recover settings...`. [Hotkeys](ourplancore-shortcuts.md#remap)
- Faster `Save` and closing of large jobs, stable raster after zoom (2.2.7).

| Version | Date | What went in |
| --- | --- | --- |
| after 2.2.5 | 08/17 | a single `.ourplan` file; `Ctrl+Z` for deleted sheets |
| | 08/20 | guided PDF metadata analysis, `Crop Hints`; `Save As` with a format choice |
| | 09/01-09/02 | unified job storage, `Open project...`, Project Storage; package autosave |
| | 09/05 | live PDF Preview with navigation; Beam and Openings in detached windows; Repeat Line and Beam; Beam dimension offset; `Move joist note` |
| 2.2.6 Preview | 09/06 | data protection: Project Data Recovery, operations log, Undo Last Page Sort / Operation; long raster paths |
| 2.2.7 Preview | 09/06 | key editor; paste Same / New takeoffs / Cancel; faster Save and Close; stable raster |
| 2.2.8 | 09/07 | internal: sort Undo only for changed nodes |

## See also

- [Getting started](ourplancore-start.md)
- [Ideas and plans](ourplancore-ideas.md) - what is still ahead
- [Troubleshooting](ourplancore-troubleshooting.md)
