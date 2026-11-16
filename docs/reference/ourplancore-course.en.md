# First steps: 10 lessons

A course on the OurPlanCore 3.0 demo job: from opening the app to PDF and Excel. Each lesson is one task from start to a visible result, 5-10 minutes. Lessons follow the estimator's order of work; details on each topic are on the pages of this section, linked at the end of each lesson. You can break the demo job: a new one is created with the `Open sample job` tile ([demo tour](ourplancore-start.md#demo)).

What you need before you start: the app is installed and launches from the desktop shortcut ([getting started](ourplancore-start.md)); for lesson 9, Excel and a copy of `TemplateCom.xlsm` from the `templates` folder of the shared Dropbox folder ([where the app is](ourplancore-start.md)).

## Lesson 1. Open the demo job and look around { #lesson-1 }

<figure markdown>
  <video class="kb-demo" loop muted playsinline preload="none" poster="../../assets/images/ourplancore/demo/d-open-sample.png"><source src="../../assets/images/ourplancore/demo/d-open-sample.mp4" type="video/mp4"></video>
  <figcaption markdown="span">Demo: `Open sample job` on the start card creates the demo job; then the W, F, S and U sheets with their legends and the 3D tab (it exists only in the full version).</figcaption>
</figure>

Goal: open the training job and learn where things are in the window.

1. Launch the app and press the **Open sample job** tile (or **Main > Open / Import > Sample job (demo to explore)**).
2. Wait for the status `Sample project created: OurPlanCore Guide Sample.`
3. In the **Pages** panel on the left, expand the `00. Guide` folder and click a floor plan: it opens as a tab in the center.
4. Find the **Takeoffs** panel with the takeoff tree on the right, the tool strip at the bottom, and the status bar at the very bottom.
5. Press `F1`: a shortcut cheat sheet over the window; close it with `Esc`.
6. Press `Ctrl+Shift+P`, type `fit`, `Enter`: the sheet fits the window. The `F` key does the same.

Check yourself: the window title shows `OurPlanCore Guide Sample`, the status bar shows `Scale:` and `Route:`, the right mouse button pans the sheet, the wheel zooms.

Details: [Getting started](ourplancore-start.md), [window map](ourplanecore.md#window-map).

## Lesson 2. Sheets: name, scale, sheet dot { #lesson-2 }

<figure markdown>
  <video class="kb-demo" loop muted playsinline preload="none" poster="../../assets/images/ourplancore/demo/d-sheet-rename-dot.png"><source src="../../assets/images/ourplancore/demo/d-sheet-rename-dot.mp4" type="video/mp4"></video>
  <figcaption markdown="span">Demo: ++ctrl+d++ makes a copy of the sheet, ++f2++ names it `a101 1st sw`, a click on the S/1 dot under `Scale` sets the route `S 1st floor`.</figcaption>
</figure>

Goal: understand that a sheet has a canonical name, a scale and a W/F/S/U dot, and learn to set them by hand.

1. Select a floor plan in Pages and read `Scale: 1/8" = 1'0"` (or `1:96`) and `Route: W 1st` in the status bar.
2. Press `R` (Ruler) and click both ends of a dimension string on the sheet: the tape length matches the labeled dimension, so the scale is right.
3. Press `F2` on the sheet, type the same name (`a101 1st`), `Enter`: the name in lowercase, the floor tag last; the W dot under the Scale header stays.
4. Press `Ctrl+D`: a copy of the sheet with the same name appears next to it.
5. Press `F2` on the copy, type `a101 1st sw`, `Enter`, then right-click the copy and **Move to Folder...** if you want to put it in a separate folder.
6. Open the copy and click the dot in row `S`, column `1`, under the Scale header.

<figure markdown>
  <video class="kb-demo" loop muted playsinline preload="none" poster="../../assets/images/ourplancore/demo/d-scale.png"><source src="../../assets/images/ourplancore/demo/d-scale.mp4" type="video/mp4"></video>
  <figcaption markdown="span">Demo: on a sheet with the wrong scale, ++f4++ and entering `1/8" = 1'0"`; the length in the legend is recalculated right away.</figcaption>
</figure>

If the sheet has no scale: press `S`, click both ends of a known dimension, type the length (`20'` or `1/8" = 1'0"`), `Enter`; for several sheets, select them in Pages and press `F4`.

Check yourself: on the copy the status shows `Route: S 1st`, on the original `Route: W 1st`; both sheets have a scale.

Details: [Sheets (Pages)](ourplancore-pages.md), [split by sheets](ourplancore-split-by-sheets.md), [sheet names](../start/takeoff-structure.md).

## Lesson 3. Routing: where a measurement goes { #lesson-3 }

<figure markdown>
  <video class="kb-demo" loop muted playsinline preload="none" poster="../../assets/images/ourplancore/demo/d-routing.png"><source src="../../assets/images/ourplancore/demo/d-routing.mp4" type="video/mp4"></video>
  <figcaption markdown="span">Demo on a real job: a wall on a W sheet goes to `walls/3rd floor walls`, a beam on an F sheet to `framing/3rd floor framing/beams`, a shear wall on a sheet copy with the S dot to `shear walls`.</figcaption>
</figure>

Goal: see how the sheet dot and the takeoff name pick the folder in the tree by themselves.

1. Open a plan with the W dot (`a101 1st`) and press `L`.
2. In the **New Takeoff Item** dialog type the name `ext 2x6 9.09` and read the destination line at the bottom of the dialog: `walls/1st floor walls`.
3. Press **OK**, click two corners on the sheet and press `C`.
4. Find the takeoff in Takeoffs: it is in `walls/1st floor walls`; the status shows `Takeoff: ext 2x6 9.09 (Route: W 1st)`.
5. Press `L` again and type `eve 24 main`: the destination line shows `eves rakes/eves`, even though the sheet is the same. The word `eve` in the name beats the sheet dot. Press **Cancel**.
6. Open the copy with the S dot, press `L`, type `SW1-1`: destination `shear walls/1st floor/shear`. Press **Cancel**.

Check yourself: you can tell which folder a takeoff will go into before pressing OK, and you see it in the `Route:` field of the status bar.

Details: [Names and auto-routing](takeoff-naming.md), [Split by sheets and routing](ourplancore-split-by-sheets.md).

## Lesson 4. Walls: Line { #lesson-4 }

<figure markdown>
  <video class="kb-demo" loop muted playsinline preload="none" poster="../../assets/images/ourplancore/demo/d-line-walls.png"><source src="../../assets/images/ourplancore/demo/d-line-walls.mp4" type="video/mp4"></video>
  <figcaption markdown="span">Demo: ++l++, name `ext 2x6 9.09`, route line `walls/1st floor walls`, clicks along the exterior wall centerline and ++c++.</figcaption>
</figure>

Goal: draw the exterior walls of a floor as one takeoff and continue it with Record.

1. On a plan with the W dot press `L`, name `ext 2x6 9.09` (purpose, size, height in feet), **OK**.
2. Click along the exterior wall centerline corner by corner; `Backspace` removes the last point.
3. Press `C`: the run is closed, the status shows `Mode: Record ext 2x6 9.09`.
4. Draw the next disconnected run of the same wall: it goes into the same takeoff.
5. Press `Space` to stop Record. Select the takeoff in the tree and press `Space` again: Record continues it when you come back to the walls later.
6. For partitions of a different height press `L` and create a new takeoff `2x4 9.09`: a new height or size means a new takeoff.

Check yourself: `walls/1st floor walls` has two takeoffs, `ext 2x6 9.09` has sections by run under it, `Total` shows linear feet.

Details: [Measuring tools, Line](ourplancore-tools.md), [Exterior](../work/vertical/walls/exterior.md).

## Lesson 5. Openings: Openings { #lesson-5 }

<figure markdown>
  <video class="kb-demo" loop muted playsinline preload="none" poster="../../assets/images/ourplancore/demo/d-openings.png"><source src="../../assets/images/ourplancore/demo/d-openings.mp4" type="video/mp4"></video>
  <figcaption markdown="span">Demo: ++o++, a box around a window, name `4.0x4.0`, the other windows with one click each; total 4 ea.</figcaption>
</figure>

Goal: count windows and doors as size-named takeoffs, one point per opening.

1. Press `O` on a plan or an elevation.
2. Click two opposite corners of a box around the opening.
3. In the dialog type the name `3.0x6.8 d`: width by height in feet with one decimal place, suffix ` d` for a door (` gd` garage door, ` lv` louver); a window has no suffix, `4.0x4.0`.
4. Press **OK**: a point appears in the center of the opening, the takeoff goes into `openings` from any sheet.
5. Repeat for the next opening of the same size: select the takeoff and `Space`, then the box; different marks of the same size = one takeoff.
6. In Takeoffs create a folder `1` under `openings` (**New Folder**) and drag the floor's takeoffs into it.

Check yourself: `openings/1` has the takeoffs `3.0x6.8 d` and `4.0x4.0`, `Total` equals the number of openings, the plan has one point per opening.

Details: [Tools, Openings](ourplancore-tools.md), [Windows and Doors](../work/vertical/openings/windows-doors.md).

## Lesson 6. Areas: Area and Cut { #lesson-6 }

<figure markdown>
  <video class="kb-demo" loop muted playsinline preload="none" poster="../../assets/images/ourplancore/demo/d-area.png"><source src="../../assets/images/ourplancore/demo/d-area.mp4" type="video/mp4"></video>
  <figcaption markdown="span">Demo: ++a++, the `1st` floor outline and ++c++; then ++x++ (`Cut`) with ++f9++ (`Box`) cuts a bathroom out of the area.</figcaption>
</figure>

Goal: take off the floor area and cut a shaft out of it.

1. On a plan with the W dot press `A`, name `1st`, **OK**.
2. Trace the floor outline corner by corner, `C` closes it: the takeoff goes into `sqfts`.
3. Press `X` (Cut), trace the outline of a shaft or stair opening inside the area, `C`.
4. Read the takeoff's `Total`: the area went down by exactly the cutout.
5. For a rectangular room press `A`, then `F9` (Box) and click two corners.

Check yourself: `sqfts` has the takeoff `1st`, the sheet shows an outline with a hole, `Total` in SF.

Details: [Tools, Area](ourplancore-tools.md), [SQFT](../work/sqfts/1st2nd.md), [Editing and snaps](ourplancore-editing.md).

## Lesson 7. Framing on an F sheet: J Area and Beam { #lesson-7 }

<figure markdown>
  <video class="kb-demo" loop muted playsinline preload="none" poster="../../assets/images/ourplancore/demo/d-jarea.png"><source src="../../assets/images/ourplancore/demo/d-jarea.mp4" type="video/mp4"></video>
  <figcaption markdown="span">Demo: ++j++, name `2x10 16"`, floor framing outline and the joist direction line; the app counts pieces and linear feet.</figcaption>
</figure>

Goal: count joists by area and a beam with an order length on a structural plan.

1. Open a structural plan with the F dot (`s101 1st`); status `Route: F 1st`.
2. Press `J`, name `2x10 16"` (size and spacing), **OK**, trace the joist area, `C`.
3. Draw the direction line along the joists when the app asks; `Shift` keeps the direction on the axes.
4. Read `Total`: pieces and linear feet, the takeoff is in `framing/1st floor framing/joists`.

<figure markdown>
  <video class="kb-demo" loop muted playsinline preload="none" poster="../../assets/images/ourplancore/demo/d-beam.png"><source src="../../assets/images/ourplancore/demo/d-beam.mp4" type="video/mp4"></video>
  <figcaption markdown="span">Demo: ++b++, two beam ends, name `FB1`; the app adds the length to the name: `FB1 52`.</figcaption>
</figure>

5. Press `B`, draw from support to support of the beam, type the mark `FB1` in the dialog, **OK**: the app added the length in feet, rounded up (`FB1 14`), the takeoff is in `.../beams`.
6. Press `P`, name `C4 20`, click the post symbol: the takeoff is in the root of `framing/1st floor framing`; drag it into the `posts` folder.

Check yourself: `framing/1st floor framing` has the folders `joists`, `beams`, `posts` with takeoffs; the beam has its length in the name, the joists have pieces in `Total`.

Details: [Tools, J Area and Beam](ourplancore-tools.md), [Joist](../work/horizontal/floor-framing/joist.md), [Beam](../work/horizontal/floor-framing/beam.md).

## Lesson 8. Check: legend, Hide, Total { #lesson-8 }

<figure markdown>
  <video class="kb-demo" loop muted playsinline preload="none" poster="../../assets/images/ourplancore/demo/d-legend-groups.png"><source src="../../assets/images/ourplancore/demo/d-legend-groups.mp4" type="video/mp4"></video>
  <figcaption markdown="span">Demo: two takeoffs under a sheet in Pages, right-click `Legend Group > New Group`; the legend on the sheet splits into walls and openings blocks.</figcaption>
</figure>

Goal: make sure everything is in place on the sheet and in the tree before exporting.

1. Turn on **Display > Legend Show**: a legend with this sheet's takeoffs appears on the sheet.
2. Right-click the sheet in Pages, **Organize > Sort Sheet Legend by Key (before space)**: takeoffs are sorted by the first word of the name.
3. Expand the sheet in Pages: under it are the same takeoffs as in the legend.

<figure markdown>
  <video class="kb-demo" loop muted playsinline preload="none" poster="../../assets/images/ourplancore/demo/d-hide.png"><source src="../../assets/images/ourplancore/demo/d-hide.mp4" type="video/mp4"></video>
  <figcaption markdown="span">Demo: ++h++ hides the selected takeoff on the sheet, the visibility dot under the sheet in Pages brings it back.</figcaption>
</figure>

4. Select the `1st` takeoff in Takeoffs and press `H`: the area disappears from the sheet, status `Hidden 1 whole takeoff(s)`.
5. Click the visibility dot next to the takeoff under the sheet in Pages: the area is back.
6. Open the **Estimating** tab on the right: all takeoffs in one table with totals. Press **Delete Empty** in Takeoffs to remove takeoffs with no measurements.

Check yourself: the legend is readable, each takeoff has its own color, Estimating has no empty rows or zero totals.

Details: [Takeoffs tree](ourplancore-takeoffs.md#hide), [PDF and delivery, legend](ourplancore-pdf.md#legend).

## Lesson 9. Excel: the Excel, Value and Link to Excel buttons { #lesson-9 }

Goal: send takeoff numbers into the DFL workbook and link one number to a measurement.

1. Copy `TemplateCom.xlsm` from the `templates` folder of the shared Dropbox folder into the job folder under the building's name, open the copy in Excel, enable macros, activate the `Detailed Frame List` worksheet.
2. In Excel, click the first free cell of the `J:L` list (from row 10).
3. In OurPlanCore, select the `walls/1st floor walls` folder in Takeoffs and press `Excel` at the bottom left: the rows (name, number, unit) land starting from that cell. `Value` writes only the numbers of the same selection into one column.
4. Click another cell in Excel, select the floor area takeoff in `sqfts` (for example `1st`) and press **Link to Excel** at the bottom. Status: `Linked <takeoff> to <workbook> <sheet!cell>: <number>`, the takeoff row shows a chain icon.
5. Select that takeoff, press `Space` and trace one more room: after a short pause the number in the linked cell goes up.
6. Save the workbook in Excel yourself: the app does not save it.

Check yourself: `J:L` has wall rows with numbers in LF, the linked cell shows the same number as the takeoff's `Total` in the tree.

In Lite, the calculation from the `J:L` list (wall matrix, areas, openings) is run with the E-Wood tab buttons in Excel ([Calculation from takeoffs](ewood-tab.md#calculate)). The XL strip does it too: `LG`, then `ALL` exports the whole building and runs the workbook macros itself ([XL strip](ourplancore-excel.md#steps)). In the full version it is on from the start; in Lite turn it on with the `Excel Strip (XL)` checkbox in `Settings > Modules`.

Details: [Export to Excel](ourplancore-excel.md#lite), [How the DFL workbook works](dfl-overview.md).

## Lesson 10. PDF and delivery { #lesson-10 }

<figure markdown>
  <video class="kb-demo" loop muted playsinline preload="none" poster="../../assets/images/ourplancore/demo/d-preview.png"><source src="../../assets/images/ourplancore/demo/d-preview.mp4" type="video/mp4"></video>
  <figcaption markdown="span">Demo: `PDF Output > Preview`; the sheet preview redraws when the opacity and legend size change on the ribbon.</figcaption>
</figure>

Goal: get a PDF with only the sheets that have measurements, and check it before export.

1. Press `Ctrl+S` and wait for `Save: Saved hh:mm:ss` in the status bar.
2. Open the **PDF Output** ribbon and press **Preview**: the window shows the current sheet as it will print.
3. Change **Opac** to 70 and the **Legend** size: the preview redraws.

<figure markdown>
  <video class="kb-demo" loop muted playsinline preload="none" poster="../../assets/images/ourplancore/demo/d-export-pdf.png"><source src="../../assets/images/ourplancore/demo/d-export-pdf.mp4" type="video/mp4"></video>
  <figcaption markdown="span">Demo: `Main > Export`, check the sheets you need, `Export`; status `Exported PDF (2 sheet(s))`.</figcaption>
</figure>

4. Press **Main > PDF > Export**, check only the sheets with measurements in the dialog, leave **Measurements** and **Legend** checked.
5. Press **Export**, name the file `<job> Bldg A.pdf`, save.
6. Open the PDF and page through it: measurements and legend in place, no extra sheets.

Check yourself: a PDF with one or two sheets, wall lines do not cover the dimensions, the legend is readable.

Details: [PDF and delivery](ourplancore-pdf.md), [Workflow, delivery](../start/workflow.md).

## Next

- Several buildings in a job: [Multiple buildings](ourplancore-buildings.md).
- Editing finished measurements, Merge and Split, snaps: [Editing and snaps](ourplancore-editing.md).
- Details on a separate sheet and the mask: [Sheets: crops, mask, overlays, legend](ourplancore-sheets-advanced.md).
- AI models and the terminal, full version only: [AI in the app](ourplancore-ai.md), [AI console](ourplancore-ai-console.md); how Lite differs: [Lite vs full version](ourplancore-lite.md).
- Takeoff order on a real project: [Workflow](../start/workflow.md), [Common mistakes](../start/common-mistakes.md).
