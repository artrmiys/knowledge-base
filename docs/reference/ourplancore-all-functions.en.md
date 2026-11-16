# All app functions

This page is generated from the app source code by tools/opc_inventory.py; do not edit it by hand.

It lists every button, menu item, key, Settings category and window of OurPlanCore 3.0, by where it sits in the interface. The "Details" column links to the section page that describes the function; an empty cell means the KB has no detailed description yet (check: `python tools/opc_coverage.py`). The same function is often available from several places (ribbon, menu, palette, key), so repeats here are normal.

Total entries: 1136. With a detail page: 997. No page yet: 24. Internal entries and repeats excluded from the check: 115.

## Bottom tool strip (42)

??? note "bottom tool strip, row 1 (33)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Link to Excel` |  | bottom tool strip: bottom tool strip, row 1 | Writes the selected takeoff's number into the active cell of the open workbook and keeps it there. | [Export to Excel](ourplancore-excel.md) |
    | `Auto Link` |  | bottom tool strip: bottom tool strip, row 1 | DFL only: links right away the takeoffs whose numbers already sit in the `J:L` list. Cells do not change, a window shows the result. | [Measuring tools](ourplancore-tools.md) |
    | `Value` |  | bottom tool strip: bottom tool strip, row 1 | Writes only the `Value` column for the same selection into the open Excel workbook. | [Measuring tools](ourplancore-tools.md) |
    | `Excel` |  | bottom tool strip: bottom tool strip, row 1 | Writes the selected folder or takeoff into the active cell of the open Excel workbook. | [Export to Excel](ourplancore-excel.md) |
    | `Include takeoff comments in Excel export` |  | bottom tool strip: bottom tool strip, row 1 | Adds takeoff and measurement comments to the Excel export; off by default. | [Export to Excel](ourplancore-excel.md) |
    | `Pan` | `V` | bottom tool strip: bottom tool strip, row 1 | Turns on the tool for moving the sheet with the left mouse button. | [Measuring tools](ourplancore-tools.md) |
    | `Select` | `E` | bottom tool strip: bottom tool strip, row 1 | Selects measurements with a box; `Ctrl+C` copies, `Ctrl+V` pastes. | [Measuring tools](ourplancore-tools.md) |
    | `Scale` | `S` | bottom tool strip: bottom tool strip, row 1 | Turns on the tool for setting the sheet scale from a known length. | [Measuring tools](ourplancore-tools.md) |
    | `Ruler` | `R` | bottom tool strip: bottom tool strip, row 1 | Places a ruler dimension mark on the sheet that is not part of the measurements. | [Measuring tools](ourplancore-tools.md) |
    | `Ruler Sheet Visibility` |  | bottom tool strip: bottom tool strip, row 1 | Hides or shows all ruler marks on this sheet. | [Measuring tools](ourplancore-tools.md) |
    | `Pitch` |  | bottom tool strip: bottom tool strip, row 1 | Draws a line by two points and shows the roof pitch per 12. | [Measuring tools](ourplancore-tools.md) |
    | `Count` | `P` | bottom tool strip: bottom tool strip, row 1 | Creates a new Count takeoff and starts recording; for an existing takeoff press `Record`. | [Measuring tools](ourplancore-tools.md) |
    | `Similar` |  | bottom tool strip: bottom tool strip, row 1 | Finds similar symbols on the sheet and adds the verified points to a Count takeoff. | [Measuring tools](ourplancore-tools.md) |
    | `P Line` |  | bottom tool strip: bottom tool strip, row 1 | Places Count points along the selected lines at a set spacing. | [Measuring tools](ourplancore-tools.md) |
    | `Break` |  | bottom tool strip: bottom tool strip, row 1 | Breaks the selected lines into separate segments; the total length does not change, `Ctrl+Z` brings them back. | [Editing and snaps](ourplancore-editing.md) |
    | `Break H/V` |  | bottom tool strip: bottom tool strip, row 1 | Sorts the horizontal and vertical line segments into two new takeoffs. | [Editing and snaps](ourplancore-editing.md) |
    | `Ends` |  | bottom tool strip: bottom tool strip, row 1 | Places Count points at both ends of each segment of the selected lines. | [Editing and snaps](ourplancore-editing.md) |
    | `Default Count display for newly created Count takeoffs` |  | bottom tool strip: bottom tool strip, row 1 | Picks how the points of new Count takeoffs are shown by default. |  |
    | `Line` | `L` | bottom tool strip: bottom tool strip, row 1 | Creates a new Line takeoff and starts recording; for an existing takeoff press `Record`. | [Measuring tools](ourplancore-tools.md) |
    | `Repeat Line` |  | bottom tool strip: bottom tool strip, row 1 | Creates a Line takeoff and draws separate two-point segments one after another; `Esc` stops. | [Editing and snaps](ourplancore-editing.md) |
    | `Area` | `A` | bottom tool strip: bottom tool strip, row 1 | Creates a new Area takeoff and starts recording; for an existing takeoff press `Record`. | [Measuring tools](ourplancore-tools.md) |
    | `J Area` | `J` | bottom tool strip: bottom tool strip, row 1 | Creates a new `Joist Area` takeoff and starts recording the area. | [Measuring tools](ourplancore-tools.md) |
    | `Beam` | `B` | bottom tool strip: bottom tool strip, row 1 | Measures the beam length, creates a Count takeoff and places the first point. | [Measuring tools](ourplancore-tools.md) |
    | `Repeat Beam` |  | bottom tool strip: bottom tool strip, row 1 | Measures beams one after another, each gets its own takeoff; `Esc` stops. | [Editing and snaps](ourplancore-editing.md) |
    | `Open` | `O` | bottom tool strip: bottom tool strip, row 1 | Measures the opening box, creates a Count takeoff and places a point in the center. | [Measuring tools](ourplancore-tools.md) |
    | `Cut` | `X` | bottom tool strip: bottom tool strip, row 1 | Cuts holes in areas or erases pieces of lines; `F9` turns on the box. | [Editing and snaps](ourplancore-editing.md) |
    | `Merge` | `Ctrl+M` | bottom tool strip: bottom tool strip, row 1 | Merges the selected takeoffs from all sheets or the selected measurement segments. | [Editing and snaps](ourplancore-editing.md) |
    | `Split` | `Ctrl+Shift+M` | bottom tool strip: bottom tool strip, row 1 | Splits takeoffs across all sheets or moves the selected measurements and points out separately. | [Editing and snaps](ourplancore-editing.md) |
    | `Combine` |  | bottom tool strip: bottom tool strip, row 1 | Combines two or more areas: union, subtraction, intersection, overlap removal, division. | [Editing and snaps](ourplancore-editing.md) |
    | `Snap` | `F3` | bottom tool strip: bottom tool strip, row 1 | Turns on snapping to points of existing measurements. | [Snap and tracing](ourplancore-snap-trace.md) |
    | `PDF` | `Ctrl+F3` | bottom tool strip: bottom tool strip, row 1 | Turns on snapping to PDF vector corners and points. | [Measuring tools](ourplancore-tools.md) |
    | `Ortho` | `F8` | bottom tool strip: bottom tool strip, row 1 | Limits drawing and editing to horizontal and vertical; `Shift` turns it on temporarily. | [Snap and tracing](ourplancore-snap-trace.md) |
    | `Box` | `F9` | bottom tool strip: bottom tool strip, row 1 | Draws lines and areas as a rectangle by two opposite corners. | [Measuring tools](ourplancore-tools.md) |

??? note "bottom tool strip, row 2 (9)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Flip H` |  | bottom tool strip: bottom tool strip, row 2 | Mirrors the selected measurements and marks horizontally. | [Editing and snaps](ourplancore-editing.md) |
    | `Flip V` |  | bottom tool strip: bottom tool strip, row 2 | Mirrors the selected measurements and marks vertically. | [Editing and snaps](ourplancore-editing.md) |
    | `Reset Rotate Selection` |  | bottom tool strip: bottom tool strip, row 2 | Returns the selection rotate slider to the center for the next adjustment. | [Measuring tools](ourplancore-tools.md) |
    | `Set` |  | bottom tool strip: bottom tool strip, row 2 | Applies the scale typed in the field to the active sheet. | [Measuring tools](ourplancore-tools.md) |
    | `Presets` |  | bottom tool strip: bottom tool strip, row 2 | Opens the list of common drawing scales for a quick pick. | [Measuring tools](ourplancore-tools.md) |
    | `AI Settings` |  | bottom tool strip: bottom tool strip, row 2 | Shows the OpenAI key status and the AI model settings. | [AI and terminals](ourplancore-ai.md) |
    | `Fit page` | `F` | bottom tool strip: bottom tool strip, row 2 | Fits the whole active sheet into the viewer window. | [Measuring tools](ourplancore-tools.md) |
    | `Zoom in` | `Ctrl++` | bottom tool strip: bottom tool strip, row 2 | Zooms the active sheet in by one zoom step. | [Keyboard shortcuts](ourplancore-shortcuts.md) |
    | `Zoom out` | `Ctrl+-` | bottom tool strip: bottom tool strip, row 2 | Zooms the active sheet out by one zoom step. | [Keyboard shortcuts](ourplancore-shortcuts.md) |

## Ribbon: top tabs Main, Page, Annotation, Viewport, Display (72)

??? note "Main ribbon, JOB (5)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Open / Import` |  | ribbon: Main ribbon, JOB | Opens jobs, changes the jobs folder, creates a job or imports PDF and PlanSwift. | [Jobs and saving](job-creation-storage.md) |
    | `PlanSwift` |  | ribbon: Main ribbon, JOB | Converts a PlanSwift job into a new OurPlanCore job, the source stays unchanged. | [Other](ourplancore-extras-other.md) |
    | `PDF Takeoffs` |  | ribbon: Main ribbon, JOB | Brings PDF sheets over together with the PDF measurements and rulers into takeoffs. | [Other](ourplancore-extras-other.md) |
    | `Save As` |  | ribbon: Main ribbon, JOB | Saves the current job to a new location on disk. | [Jobs and saving](job-creation-storage.md) |
    | `In Progress` |  | ribbon: Main ribbon, JOB | Moves the job card in Job Tracker to the `In Progress` status with an external command. | [Jobs and saving](job-creation-storage.md) |

??? note "Main ribbon, PDF (6)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Export` |  | ribbon: Main ribbon, PDF | Exports the selected or all sheets to one PDF. | [Extras](ourplancore-extras.md) |
    | `Name` |  | ribbon: Main ribbon, PDF | Shows and applies automatic sheet names from the PDF. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Scale` |  | ribbon: Main ribbon, PDF | Shows and applies automatic sheet scales from the PDF. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Name+Scale` |  | ribbon: Main ribbon, PDF | Shows and applies automatic sheet names and scales from the PDF. | [Sheets (Pages)](ourplancore-pages.md) |
    | `AI Fill` |  | ribbon: Main ribbon, PDF | Queues GPT for the sheets whose metadata was not found. | [AI and terminals](ourplancore-ai.md) |
    | `Crop Hints` |  | ribbon: Main ribbon, PDF | Draws the sheet number, title and scale areas for auto-naming and `AI Fill`. | [AI and terminals](ourplancore-ai.md) |

??? note "Page ribbon, ADD (3)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Add Pages` |  | ribbon: Page ribbon, ADD | Imports PDF pages into the current job. | [Jobs and saving](job-creation-storage.md) |
    | `Blank Sheet` |  | ribbon: Page ribbon, ADD | Creates a blank sheet in the current job without a PDF. | [Sheets (Pages)](ourplancore-pages.md) |
    | `PDF Takeoffs` |  | ribbon: Page ribbon, ADD | Brings PDF sheets over together with the PDF measurements and rulers into takeoffs. | [Other](ourplancore-extras-other.md) |

??? note "Page ribbon, ROTATE (5)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Left` |  | ribbon: Page ribbon, ROTATE | Rotates the active sheet 90 degrees to the left. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Right` |  | ribbon: Page ribbon, ROTATE | Rotates the active sheet 90 degrees to the right. | [Sheets (Pages)](ourplancore-pages.md) |
    | `180` |  | ribbon: Page ribbon, ROTATE | Rotates the active sheet 180 degrees. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Level` |  | ribbon: Page ribbon, ROTATE | Fits the sheet into the window and drops any half-drawn input. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Batch Rotate` |  | ribbon: Page ribbon, ROTATE | Rotates all selected sheets at once by a set angle. | [Sheets (Pages)](ourplancore-pages.md) |

??? note "Page ribbon, FLIP (2)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Vertical` |  | ribbon: Page ribbon, FLIP | Mirrors the active sheet vertically, top to bottom. | [Editing and snaps](ourplancore-editing.md) |
    | `Horizontal` |  | ribbon: Page ribbon, FLIP | Mirrors the active sheet horizontally, left to right. | [Editing and snaps](ourplancore-editing.md) |

??? note "Page ribbon, IMAGE (4)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Invert` |  | ribbon: Page ribbon, IMAGE | Inverts the active sheet's colors, white becomes black. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Copy` |  | ribbon: Page ribbon, IMAGE | Copies a PNG image of the active sheet to the clipboard. | [Editing and snaps](ourplancore-editing.md) |
    | `Crop New Page` |  | ribbon: Page ribbon, IMAGE | Creates a new sheet from the part of the sheet visible right now. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Crop to Sheet` |  | ribbon: Page ribbon, IMAGE | Copies framed details from different sheets onto one sheet at true scale. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |

??? note "Page ribbon, PAGE (5)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Batch Rename` |  | ribbon: Page ribbon, PAGE | Renames the selected sheets in sequence in one action. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Batch Overlay` |  | ribbon: Page ribbon, PAGE | Matches sheet pairs and applies overlays to many sheets of the job at once. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Set Origin` |  | ribbon: Page ribbon, PAGE | Sets the center of the visible part of the sheet as the sheet origin. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Offset Origin` |  | ribbon: Page ribbon, PAGE | Shifts the previously saved sheet origin by a set offset. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Close Page` |  | ribbon: Page ribbon, PAGE | Closes the active sheet's tab in the viewer window. | [Sheets (Pages)](ourplancore-pages.md) |

??? note "Annotation ribbon, MARKUP TOOLS (9)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Highlighter` | `Shift+H` | ribbon: Annotation ribbon, MARKUP TOOLS | Draws a semi-transparent highlighter mark on the sheet that is not part of the measurements. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Draw line` | `D` | ribbon: Annotation ribbon, MARKUP TOOLS | Draws a simple line mark on the sheet that is not part of the measurements. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Arrow` |  | ribbon: Annotation ribbon, MARKUP TOOLS | Draws a simple arrow mark on the sheet that is not part of the measurements. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Box` |  | ribbon: Annotation ribbon, MARKUP TOOLS | Draws a simple rectangle mark that is not part of the measurements. | [Snap and tracing](ourplancore-snap-trace.md) |
    | `Cloud` |  | ribbon: Annotation ribbon, MARKUP TOOLS | Draws a cloud mark on the sheet to flag changes. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Area fill` |  | ribbon: Annotation ribbon, MARKUP TOOLS | Draws a color-filled area mark on the sheet, not a measurement. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Hide area (white)` |  | ribbon: Annotation ribbon, MARKUP TOOLS | Covers part of the sheet with solid white on screen and in the PDF export. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Note` | `N` | ribbon: Annotation ribbon, MARKUP TOOLS | Writes a text note at the chosen spot on the sheet. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Style` |  | ribbon: Annotation ribbon, MARKUP TOOLS | Opens the markup tools with color and width choice. |  |

??? note "Annotation ribbon, TAKEOFF ANNOTATIONS (3)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Annotation area` |  | ribbon: Annotation ribbon, TAKEOFF ANNOTATIONS | Annotation area: drawn into an annotation takeoff (tree and legend 'annotation', no quantity) | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Annotation line` |  | ribbon: Annotation ribbon, TAKEOFF ANNOTATIONS | Annotation line: drawn into an annotation takeoff (tree and legend 'annotation', no quantity) | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Annotation point` |  | ribbon: Annotation ribbon, TAKEOFF ANNOTATIONS | Annotation point: drawn into an annotation takeoff (tree and legend 'annotation', no quantity) |  |

??? note "Annotation ribbon, STYLE (1)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Annotation line thickness` |  | ribbon: Annotation ribbon, STYLE | Sets the line width of marks on the sheet. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |

??? note "Viewport ribbon, LINES & AREA (4)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Line measurement thickness` |  | ribbon: Viewport ribbon, LINES & AREA | Sets the line width of linear measurements, from 0.25 to 4.0. | [Settings and modules](ourplancore-settings.md) |
    | `Count marker size` |  | ribbon: Viewport ribbon, LINES & AREA | Sets the size of the Count symbols, from 0.25 to 4.0. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Area boundary thickness` |  | ribbon: Viewport ribbon, LINES & AREA | Sets the outline width of area measurements, from 0.25 to 4.0. | [Settings and modules](ourplancore-settings.md) |
    | `Area fill opacity` |  | ribbon: Viewport ribbon, LINES & AREA | Sets the area fill opacity, from 0 to 100 percent. | [Settings and modules](ourplancore-settings.md) |

??? note "Viewport ribbon, RULER / EXTRA (1)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Ruler screen thickness` |  | ribbon: Viewport ribbon, RULER / EXTRA | Sets the on-screen ruler line width, from 0.5 to 6 pixels. | [Measuring tools](ourplancore-tools.md) |

??? note "Viewport ribbon, PDF SNAP (1)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `PDF Snap Tab continuation radius` |  | ribbon: Viewport ribbon, PDF SNAP | Sets the PDF snap continuation radius for the `Tab` key, from 4 to 96 pixels. | [Snap and tracing](ourplancore-snap-trace.md) |

??? note "Display ribbon, LABELS (7)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `All` |  | ribbon: Display ribbon, LABELS | Shows the labels of all measurement types on the sheet. | [Export to Excel](ourplancore-excel.md) |
    | `Line` |  | ribbon: Display ribbon, LABELS | Shows a length label on each linear measurement. | [Editing and snaps](ourplancore-editing.md) |
    | `Area` |  | ribbon: Display ribbon, LABELS | Shows an area label on each area measurement. | [Measuring tools](ourplancore-tools.md) |
    | `Joist` |  | ribbon: Display ribbon, LABELS | Shows the total and segment labels of the joist layouts in `Joist Area`. | [Measuring tools](ourplancore-tools.md) |
    | `Count` |  | ribbon: Display ribbon, LABELS | Shows a quantity label on each Count measurement. | [Measuring tools](ourplancore-tools.md) |
    | `Value label size` |  | ribbon: Display ribbon, LABELS | Sets the size of value labels on the sheet, from 0.25 to 3.0. | [Settings and modules](ourplancore-settings.md) |
    | `w/ page` |  | ribbon: Display ribbon, LABELS | Makes the labels grow and shrink with the sheet zoom; when off, the size is fixed. | [Settings and modules](ourplancore-settings.md) |

??? note "Display ribbon, OVERLAYS / RENDER (10)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Show` |  | ribbon: Display ribbon, OVERLAYS / RENDER | Shows or hides the legend on the active sheet. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Legend: Size` |  | ribbon: Display ribbon, OVERLAYS / RENDER | Picks a preset size for the legend on the sheet. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Pos` |  | ribbon: Display ribbon, OVERLAYS / RENDER | Picks the sheet corner or edge the legend is anchored to. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Legend: w/page` |  | ribbon: Display ribbon, OVERLAYS / RENDER | Makes the legend grow and shrink with the sheet zoom; when off, the size is fixed. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Header: Size` |  | ribbon: Display ribbon, OVERLAYS / RENDER | Picks a preset size for the header on the sheet. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Header: w/page` |  | ribbon: Display ribbon, OVERLAYS / RENDER | Makes the header grow and shrink with the sheet zoom; when off, the size is fixed. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Fast pan/zoom` |  | ribbon: Display ribbon, OVERLAYS / RENDER | Simplifies overlays while panning and zooming, so heavy sheets move faster. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `PDF layers` |  | ribbon: Display ribbon, OVERLAYS / RENDER | Turns on the `PDF Layers` panel and layer detection on sheets; without it sheets load faster. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Static image` |  | ribbon: Display ribbon, OVERLAYS / RENDER | Shows the sheet as a single 150 DPI image with no redraw on pan and zoom. | [Snap and tracing](ourplancore-snap-trace.md) |
    | `Black vector` |  | ribbon: Display ribbon, OVERLAYS / RENDER | Draws crisp black vector lines over the sheet image at any zoom. | [Sheets (Pages)](ourplancore-pages.md) |

??? note "Display ribbon, UNITS & VIEW (6)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `ft / sf` |  | ribbon: Display ribbon, UNITS & VIEW | Turns on imperial units ft, sf, ea; when off, metric. | [Settings and modules](ourplancore-settings.md) |
    | `Viewport PDF render RAM/quality profile` |  | ribbon: Display ribbon, UNITS & VIEW | Picks the PDF rendering memory and quality profile: `Balanced`, `High` or `Max`. | [Settings and modules](ourplancore-settings.md) |
    | `Choose the background around the sheet` |  | ribbon: Display ribbon, UNITS & VIEW | Picks the background color around the sheet: white, gray or dark. | [Settings and modules](ourplancore-settings.md) |
    | `Choose a softer page background tint` |  | ribbon: Display ribbon, UNITS & VIEW | Picks a soft tint for the sheet background itself, from white to black. | [Settings and modules](ourplancore-settings.md) |
    | `Dark` |  | ribbon: Display ribbon, UNITS & VIEW | Switches between the dark and light interface theme. | [Settings and modules](ourplancore-settings.md) |
    | `Mouse-wheel zoom step per notch` |  | ribbon: Display ribbon, UNITS & VIEW | Sets the zoom step per mouse wheel notch, from 1.05 to 2.5. | [Settings and modules](ourplancore-settings.md) |

## XL (Excel) strip right of the sheet (22)

??? note "XL strip (22)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `XL` |  | XL strip: XL strip | Show / hide ALL selection dots; the export selection is preserved | [Settings and modules](ourplancore-settings.md) |
    | `ALL` |  | XL strip: XL strip | Runs the whole configured chain of Excel macros for one selected building. | [Export to Excel](ourplancore-excel.md) |
    | `Legend (LG)` |  | XL strip: XL strip | Opens the job legend used to export Beams, Posts and Headers. | [Export to Excel](ourplancore-excel.md) |
    | `SQFT (SF)` |  | XL strip: XL strip | Adds the selected SQFT rows to the template and runs the `A2_SQFT_calc` macro. | [Export to Excel](ourplancore-excel.md) |
    | `Walls (WL)` |  | XL strip: XL strip | Adds the wall rows with floor groups and runs the `A3_Walls_Calc_AllGroup` macro. | [Export to Excel](ourplancore-excel.md) |
    | `Gables (GB)` |  | XL strip: XL strip | Adds the selected Gables rows and runs the `A2_SQFT_calc` macro. | [Export to Excel](ourplancore-excel.md) |
    | `Truss Heel (TH)` |  | XL strip: XL strip | Adds the selected Truss Heel rows and runs the `A2_SQFT_calc` macro. | [Export to Excel](ourplancore-excel.md) |
    | `Parapet (PP)` |  | XL strip: XL strip | Adds the selected Parapet rows and runs the `A4_Parapet` macro. | [Export to Excel](ourplancore-excel.md) |
    | `Eve/Rakes (E/R)` |  | XL strip: XL strip | Adds the Eves and Rakes rows in descending length order and runs `A6_Eve_Rakes`. | [Export to Excel](ourplancore-excel.md) |
    | `Openings (OP)` |  | XL strip: XL strip | Adds openings from `Z158`, groups close windows by floor and runs `A5_Openings`. | [Export to Excel](ourplancore-excel.md) |
    | `Sheathing (SH)` |  | XL strip: XL strip | Runs the `A7_walls_sheathing` macro and keeps one sheathing system based on column J or the legend. | [Export to Excel](ourplancore-excel.md) |
    | `Shear walls (SW)` |  | XL strip: XL strip | Fills the Shear Walls and Holdowns rows in the wall block of each floor. | [Export to Excel](ourplancore-excel.md) |
    | `Shaft walls (SHF)` |  | XL strip: XL strip | Adds or updates the Shaft walls block with panels and CH and J profiles. | [Export to Excel](ourplancore-excel.md) |
    | `Units (UN)` |  | XL strip: XL strip | Builds the typical unit table with counts by floor and `SUMPRODUCT` totals. | [Export to Excel](ourplancore-excel.md) |
    | `Balconies (BL)` |  | XL strip: XL strip | Creates a list block for each balcony, deck and porch size from the SQFT areas. | [Export to Excel](ourplancore-excel.md) |
    | `Framing (FR)` |  | XL strip: XL strip | Exports the posts, beams, joists, headers and details of the selected building into the framing lists. | [Export to Excel](ourplancore-excel.md) |
    | `Posts (PS)` |  | XL strip: XL strip | Replaces the Posts rows in each framing list of the selected building from the legend. | [Export to Excel](ourplancore-excel.md) |
    | `Beams (BM)` |  | XL strip: XL strip | Replaces the Beam rows in each framing list of the selected building from the legend. | [Export to Excel](ourplancore-excel.md) |
    | `Headers (HD)` |  | XL strip: XL strip | Rebuilds the header rows in the wall block one floor below each framing floor. | [Export to Excel](ourplancore-excel.md) |
    | `Joists (JS)` |  | XL strip: XL strip | Replaces the Joist rows in each framing list; Extra joists of the same length are added to the row. | [Export to Excel](ourplancore-excel.md) |
    | `Details (DT)` |  | XL strip: XL strip | Puts each floor's detail lines into columns J, K, L once. | [Export to Excel](ourplancore-excel.md) |
    | `Stairs (ST)` |  | XL strip: XL strip | Adds the stair measurements before the Subfloor row of each framing list. | [Export to Excel](ourplancore-excel.md) |

## Icon strips left and right of the sheet (default set) (32)

??? note "left icon strip (14)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Open Selected in Tabs` |  | icon strip: left icon strip | Opens the sheets selected in the Pages tree in tabs. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Detach to Windows` |  | icon strip: left icon strip | Opens the sheets selected in the Pages tree in separate windows. | [Other](ourplancore-extras-other.md) |
    | `Tile on Monitor 2` |  | icon strip: left icon strip | Opens the selected sheets in separate windows and tiles them on the second monitor. | [Other](ourplancore-extras-other.md) |
    | `Overlay` |  | icon strip: left icon strip | Picks a suitable sheet to overlay on the active one. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Move Overlay by Points` |  | icon strip: left icon strip | Aligns the active sheet's overlay by pairs of points. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Name / Scale Setup` | `F5` | icon strip: left icon strip | Opens the window for setting the active sheet's name and scale by hand. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Sort Pages A-Z` |  | icon strip: left icon strip | Sorts the contents of the selected Pages folder or the root alphabetically. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Sort Pages Z-A` |  | icon strip: left icon strip | Sorts the contents of the selected Pages folder or the root in reverse alphabetical order. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Sort Pages A/S` |  | icon strip: left icon strip | Sorts A sheets into `Arch`, S sheets into `Struct`, the rest into others. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Sort Pages D/Sec/WT` |  | icon strip: left icon strip | Sorts sheets with suffixes into the details, sections, units folders and orders the Pages root. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Auto Page Folders` |  | icon strip: left icon strip | Creates the standard sheet folder tree in the selected Pages folder. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Collapse Pages Tree` |  | icon strip: left icon strip | Collapses all folders in the Pages tree. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Expand Pages Tree` |  | icon strip: left icon strip | Expands all folders in the Pages tree. | [Measuring tools](ourplancore-tools.md) |
    | `Configure the command strip (gear)` |  | icon strip: left icon strip | Opens the icon strip setup: which commands to show on it. |  |

??? note "right icon strip (18)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Quick Calculator` |  | icon strip: right icon strip | Shows or hides the slide-out calculator that works in feet and inches. | [Other](ourplancore-extras-other.md) |
    | `New Takeoff Item` | `T` | icon strip: right icon strip | Creates a takeoff in the selected folder or in the root. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `New Takeoff Folder` |  | icon strip: right icon strip | Creates a takeoff folder in the selected folder or in the root. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Record Active Takeoff` | `Space` | icon strip: right icon strip | Starts or stops recording into the active takeoff. | [Measuring tools](ourplancore-tools.md) |
    | `Show Active Takeoff` |  | icon strip: right icon strip | Scrolls the Takeoffs tree to the active takeoff. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Active Takeoff Properties` |  | icon strip: right icon strip | Opens the properties of the active takeoff for editing. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Merge Selected Takeoffs / Measurements` | `Ctrl+M` | icon strip: right icon strip | Merges the selected takeoffs from all sheets or moves the selected measurements into another takeoff. | [Editing and snaps](ourplancore-editing.md) |
    | `Split Selected Takeoffs / Measurements` | `Ctrl+Shift+M` | icon strip: right icon strip | Splits takeoffs across all sheets or moves the selected measurements and points into a new takeoff. | [Editing and snaps](ourplancore-editing.md) |
    | `Sort Takeoffs A-Z` |  | icon strip: right icon strip | Sorts the contents of the selected Takeoffs folder or the root alphabetically. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Sort Takeoffs Z-A` |  | icon strip: right icon strip | Sorts the contents of the selected Takeoffs folder or the root in reverse alphabetical order. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Sort Takeoffs: Walls` |  | icon strip: right icon strip | Sorts the walls in the folder and subfolders: ext, corr, dem, then 2x6 and 2x4 sizes. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Sort Takeoffs: Details by Sheet` |  | icon strip: right icon strip | Groups `1/A501` style nodes by the sheet after the slash, in the Pages tree order. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Auto Takeoff Tree` |  | icon strip: right icon strip | Creates the standard takeoff folder tree for a new job. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Create Takeoffs From Pages` |  | icon strip: right icon strip | Creates top takeoff folders from the names of Pages sheets and folders typed in capitals. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Export to Current Excel` |  | icon strip: right icon strip | Writes the selected folder or takeoff into the active cell of the open Excel workbook. | [Export to Excel](ourplancore-excel.md) |
    | `Collapse Takeoffs Tree` |  | icon strip: right icon strip | Collapses all folders in the Takeoffs tree. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Expand Takeoffs Tree` |  | icon strip: right icon strip | Expands all folders in the Takeoffs tree. | [Measuring tools](ourplancore-tools.md) |
    | `Configure the command strip (gear)` |  | icon strip: right icon strip | Opens the icon strip setup: which commands to show on it. |  |

## Workspace panels and tabs (178)

??? note "Main View, Pages panel (12)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Close other sheets and keep the main viewport sheet` |  | panel: Main View, Pages panel | Closes all other tabs and separate sheet windows, keeps the sheet in the main window. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Close detached sheets on monitor 2` |  | panel: Main View, Pages panel | Closes all separate sheet windows on the second monitor. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Tile M2` |  | panel: Main View, Pages panel | Opens the selected sheets in separate windows and tiles them on the second monitor. | [Other](ourplancore-extras-other.md) |
    | `Toggle vertical Tile M2 layout` |  | panel: Main View, Pages panel | Switches the tile layout on the second monitor to vertical and back. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Open` |  | panel: Main View, Pages panel | Opens the sheets selected in the Pages tree. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Refresh Pages tree` |  | panel: Main View, Pages panel | Rereads the Pages tree from the current job folder. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Collapse all Pages nodes` |  | panel: Main View, Pages panel | Collapses all folders in the Pages tree. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Expand all Pages nodes` |  | panel: Main View, Pages panel | Expands all folders in the Pages tree. | [Measuring tools](ourplancore-tools.md) |
    | `New Folder` |  | panel: Main View, Pages panel | Creates a new folder inside the selected Pages folder. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Name` |  | panel: Main View, Pages panel | Shows and applies automatic sheet names from the PDF. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Scale` |  | panel: Main View, Pages panel | Shows and applies automatic sheet scales from the PDF. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Name+Scale` |  | panel: Main View, Pages panel | Shows and applies automatic sheet names and scales from the PDF. | [Sheets (Pages)](ourplancore-pages.md) |

??? note "Main View, Pages panel, quick row (3)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Folder Template Mode` |  | panel: Main View, Pages panel, quick row | Picks the folder template for Pages and Takeoffs: `Auto`, `COM` or `EWP`. | [Sheets (Pages)](ourplancore-pages.md) |
    | `+ New` |  | panel: Main View, Pages panel, quick row | Opens the menu for creating sheets and folders in the Pages tree. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Setup` |  | panel: Main View, Pages panel, quick row | Opens the menu for setting up and sorting sheets in the Pages tree. | [Sheets (Pages)](ourplancore-pages.md) |

??? note "Main View > Pages, Pages panel (1)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Match page folder case exactly` |  | panel: Main View > Pages, Pages panel | Matches Pages folders with exact upper and lower case. | [Sheets (Pages)](ourplancore-pages.md) |

??? note "Main View > PDF Layers, Pages panel (7)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Load` |  | panel: Main View > PDF Layers, Pages panel | Looks for PDF layers on the active sheet on demand. | [Snap and tracing](ourplancore-snap-trace.md) |
    | `All On` |  | panel: Main View > PDF Layers, Pages panel | Turns on all PDF layers on the active sheet. | [Snap and tracing](ourplancore-snap-trace.md) |
    | `All Off` |  | panel: Main View > PDF Layers, Pages panel | Turns off all PDF layers on the active sheet. | [Snap and tracing](ourplancore-snap-trace.md) |
    | `Clear Hi` |  | panel: Main View > PDF Layers, Pages panel | Removes the highlight from the highlighted PDF layers on the sheet. | [Snap and tracing](ourplancore-snap-trace.md) |
    | `Layer Trace` |  | panel: Main View > PDF Layers, Pages panel | Highlights the selected PDF layer and traces its lines into a measurement. | [Snap and tracing](ourplancore-snap-trace.md) |
    | `Full` |  | panel: Main View > PDF Layers, Pages panel | Switches the dimming in `Layer Trace`: full, muted or off; `Tab` does the same. | [Snap and tracing](ourplancore-snap-trace.md) |
    | `Apply` |  | panel: Main View > PDF Layers, Pages panel | Applies tracing of the active PDF layer at the point under the pointer. | [Snap and tracing](ourplancore-snap-trace.md) |

??? note "Main View, Bookmarks panel (1)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Return Bookmarks to the tab list` |  | panel: Main View, Bookmarks panel | Returns the bookmarks panel to the tab list. | [Other](ourplancore-extras-other.md) |

??? note "Main View, Templates panel (1)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Return Templates to the tab list` |  | panel: Main View, Templates panel | Returns the templates panel to the tab list. |  |

??? note "Main View, start card (no job open) (4)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Open a recent job - Recently used` |  | panel: Main View, start card (no job open) | Opens a job from the recently used list. | [Jobs and saving](job-creation-storage.md) |
    | `New blank job - Start empty` |  | panel: Main View, start card (no job open) | Creates an empty job, sheets can be added later. | [Jobs and saving](job-creation-storage.md) |
    | `New job from PDFs - Import a folder of drawings` |  | panel: Main View, start card (no job open) | Creates a job from a folder of PDF drawings. | [Jobs and saving](job-creation-storage.md) |
    | `Open sample job - Explore a demo` |  | panel: Main View, start card (no job open) | Opens the built-in sample job to get to know the app. | [Jobs and saving](job-creation-storage.md) |

??? note "Main View, Layer Trace row (2)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Manual` |  | panel: Main View, Layer Trace row | Switches between manual tracing and tracing by PDF layer on the sheet. | [Snap and tracing](ourplancore-snap-trace.md) |
    | `Full` |  | panel: Main View, Layer Trace row | Switches the dimming in `Layer Trace`: full, muted or off; `Tab` does the same. | [Snap and tracing](ourplancore-snap-trace.md) |

??? note "Main View, Takeoffs panel (8)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Refresh Takeoffs tree` |  | panel: Main View, Takeoffs panel | Rereads the Takeoffs tree from the current job folder. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Collapse all Takeoffs nodes` |  | panel: Main View, Takeoffs panel | Collapses all folders in the Takeoffs tree. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Expand all Takeoffs nodes` |  | panel: Main View, Takeoffs panel | Expands all folders in the Takeoffs tree. | [Measuring tools](ourplancore-tools.md) |
    | `New Folder` |  | panel: Main View, Takeoffs panel | Creates a takeoff folder in the selected folder or in the root. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `New Item` | `T` | panel: Main View, Takeoffs panel | Creates a takeoff in the selected folder or in the root. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Delete Empty` |  | panel: Main View, Takeoffs panel | Deletes all takeoffs with no measurements; `Ctrl+Z` brings back the whole batch. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `More` |  | panel: Main View, Takeoffs panel | Opens the menu of extra actions for the Takeoffs panel, the active takeoff or `AI Inbox`. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Export` |  | panel: Main View, Takeoffs panel | Opens the menu for saving and exporting quantities. | [Takeoffs tree](ourplancore-takeoffs.md) |

??? note "Main View, Takeoffs panel, active takeoff row (7)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Record` | `Space` | panel: Main View, Takeoffs panel, active takeoff row | Starts or stops recording into the active takeoff. | [Measuring tools](ourplancore-tools.md) |
    | `More` |  | panel: Main View, Takeoffs panel, active takeoff row | Opens the menu of extra actions for the Takeoffs panel, the active takeoff or `AI Inbox`. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Props` |  | panel: Main View, Takeoffs panel, active takeoff row | Opens the properties of the active takeoff for editing. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Find` |  | panel: Main View, Takeoffs panel, active takeoff row | Scrolls the Takeoffs tree to the active takeoff. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Sheet` |  | panel: Main View, Takeoffs panel, active takeoff row | Picks a takeoff from those already measured on this sheet. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Switch to next takeoff item` |  | panel: Main View, Takeoffs panel, active takeoff row | Makes the next takeoff in the target list active. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Switch to previous takeoff item` |  | panel: Main View, Takeoffs panel, active takeoff row | Makes the previous takeoff in the target list active. | [Takeoffs tree](ourplancore-takeoffs.md) |

??? note "Main View, Takeoffs panel, tree (1)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Match takeoff folder case exactly` |  | panel: Main View, Takeoffs panel, tree | Matches Takeoffs folders with exact upper and lower case. | [Takeoffs tree](ourplancore-takeoffs.md) |

??? note "Main View, AI Inbox (6)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Toggle AI Inbox` |  | panel: Main View, AI Inbox | Collapses or expands the `AI Inbox` panel. | [AI and terminals](ourplancore-ai.md) |
    | `+ Add` |  | panel: Main View, AI Inbox | Saves a manual AI observation or marker note for the job and sheet. | [AI and terminals](ourplancore-ai.md) |
    | `Run AI` |  | panel: Main View, AI Inbox | Runs the selected request from `AI Inbox`. | [AI and terminals](ourplancore-ai.md) |
    | `More` |  | panel: Main View, AI Inbox | Opens the menu of extra actions for the Takeoffs panel, the active takeoff or `AI Inbox`. | [AI and terminals](ourplancore-ai.md) |
    | `Filter AI markers by type` |  | panel: Main View, AI Inbox | Filters AI markers in `AI Inbox` by type. | [AI and terminals](ourplancore-ai.md) |
    | `Filter AI markers by sample kind` |  | panel: Main View, AI Inbox | Filters AI markers in `AI Inbox` by sample kind. | [AI and terminals](ourplancore-ai.md) |

??? note "Sheet Manager, PDF group (3)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Import PDF(s)` |  | panel: Sheet Manager, PDF group | Adds one or more PDFs to the current job. | [Managers](ourplancore-managers.md) |
    | `PDF Takeoffs` |  | panel: Sheet Manager, PDF group | Brings PDF sheets over together with the PDF measurements and rulers into takeoffs. | [Other](ourplancore-extras-other.md) |
    | `Export PDF` |  | panel: Sheet Manager, PDF group | Exports the selected or all sheets to one PDF. | [PDF and delivery](ourplancore-pdf.md) |

??? note "Sheet Manager, Raster group (3)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `PDF` |  | panel: Sheet Manager, Raster group | Turns off raster rendering for the selected sheets, they are drawn from the PDF. | [Snap and tracing](ourplancore-snap-trace.md) |
    | `Auto` |  | panel: Sheet Manager, Raster group | Restores adaptive sheet DPI in Sheet Manager; in 3D builds walls, slabs and roofs by itself. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Options...` |  | panel: Sheet Manager, Raster group | Opens the raster settings: format, preparation, first frame, cleanup and cancel. | [Jobs and saving](job-creation-storage.md) |

??? note "Sheet Manager, Format group (6)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Sheet Manager Raster Format Box` |  | panel: Sheet Manager, Format group | Picks the raster cache format: `Auto` with WebP, `WebP` or `PNG` for difficult PDFs. |  |
    | `Prepare` |  | panel: Sheet Manager, Format group | Prepares the raster cache at the last selected DPI without changing the sheet mode. | [Managers](ourplancore-managers.md) |
    | `First On` |  | panel: Sheet Manager, Format group | Opens the selected raster sheets right away from the prepared image as the first frame. | [Managers](ourplancore-managers.md) |
    | `First Off` |  | panel: Sheet Manager, Format group | Opens the selected raster sheets the regular way, through the PDF and preview. | [Managers](ourplancore-managers.md) |
    | `Clean` |  | panel: Sheet Manager, Format group | Deletes unused raster versions of the selected sheets, the active raster stays. | [Jobs and saving](job-creation-storage.md) |
    | `Cancel` |  | panel: Sheet Manager, Format group | Cancels the background raster work after the current sheet. | [Snap and tracing](ourplancore-snap-trace.md) |

??? note "Sheet Manager, Metadata group (8)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Refresh` |  | panel: Sheet Manager, Metadata group | Rereads the table of the current manager: sheets, takeoffs, report, materials or AI. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Analyze` |  | panel: Sheet Manager, Metadata group | Reads the PDF text and layers and shows the sheet metadata found. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Auto Name` |  | panel: Sheet Manager, Metadata group | Shows the proposed automatic sheet names before applying. | [Settings and modules](ourplancore-settings.md) |
    | `Auto Scale` |  | panel: Sheet Manager, Metadata group | Shows the proposed automatic sheet scales before applying. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Name+Scale` |  | panel: Sheet Manager, Metadata group | Shows the proposed sheet names and scales together. | [Sheets (Pages)](ourplancore-pages.md) |
    | `AI Fill` |  | panel: Sheet Manager, Metadata group | Queues GPT for the sheets whose metadata was not found. | [AI and terminals](ourplancore-ai.md) |
    | `Crop Hints` |  | panel: Sheet Manager, Metadata group | Draws the sheet number, title and scale areas for auto-naming and `AI Fill`. | [AI and terminals](ourplancore-ai.md) |
    | `Apply Checked` |  | panel: Sheet Manager, Metadata group | Applies the checked rename and scale rows to the job. | [Managers](ourplancore-managers.md) |

??? note "Sheet Manager, Open group (5)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Open Sheet` |  | panel: Sheet Manager, Open group | Opens the selected sheet in the main workspace. | [Managers](ourplancore-managers.md) |
    | `Open Tabs` |  | panel: Sheet Manager, Open group | Opens the selected sheets in tabs of the viewer window. | [Managers](ourplancore-managers.md) |
    | `Detach` |  | panel: Sheet Manager, Open group | Opens the selected sheets in separate windows. | [Other](ourplancore-extras-other.md) |
    | `Tile M2` |  | panel: Sheet Manager, Open group | Opens the selected sheets in separate tiled windows on the second monitor. | [Other](ourplancore-extras-other.md) |
    | `Open JSON` |  | panel: Sheet Manager, Open group | Opens the JSON file with the PDF metadata for checking. | [AI and terminals](ourplancore-ai.md) |

??? note "Sheet Manager, Organize group (4)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Sort A/S` |  | panel: Sheet Manager, Organize group | Sorts A sheets into `Arch`, S sheets into `Struct`, the rest into others. | [Sheets (Pages)](ourplancore-pages.md) |
    | `D/Sec/WT` |  | panel: Sheet Manager, Organize group | Sorts sheets with suffixes into the details, sections, units folders and orders the Pages root. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Repair Links` |  | panel: Sheet Manager, Organize group | Reattaches measurements to sheets after pages are renamed or imported. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Auto Folders` |  | panel: Sheet Manager, Organize group | Creates the standard sheet folder tree in the selected Pages folder. | [Sheets (Pages)](ourplancore-pages.md) |

??? note "Takeoff Manager, File group (1)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Save` |  | panel: Takeoff Manager, File group | Saves the current job with all its measurements. | [Takeoffs tree](ourplancore-takeoffs.md) |

??? note "Takeoff Manager, Item group (6)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Refresh` |  | panel: Takeoff Manager, Item group | Rereads the table of the current manager: sheets, takeoffs, report, materials or AI. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Set Active` |  | panel: Takeoff Manager, Item group | Makes the selected takeoff the active drawing target. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Properties` |  | panel: Takeoff Manager, Item group | Opens the properties of the selected takeoff for editing. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Open Estimating` |  | panel: Takeoff Manager, Item group | Opens a separate window with the full `Estimating` table of all measurements. | [Managers](ourplancore-managers.md) |
    | `New Folder` |  | panel: Takeoff Manager, Item group | Creates a takeoff folder in the selected folder or in the root. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `New Item` |  | panel: Takeoff Manager, Item group | Creates a takeoff in the selected folder or in the root. | [Takeoffs tree](ourplancore-takeoffs.md) |

??? note "Takeoff Manager, Tree group (2)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Auto Tree` |  | panel: Takeoff Manager, Tree group | Creates the standard takeoff folder tree for a new job. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `From Pages` |  | panel: Takeoff Manager, Tree group | Creates top takeoff folders from the names of Pages sheets and folders typed in capitals. | [Takeoffs tree](ourplancore-takeoffs.md) |

??? note "Takeoff Manager, Export group (4)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Export CSV` |  | panel: Takeoff Manager, Export group | Exports the measurement rows to a CSV file. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `TXT` |  | panel: Takeoff Manager, Export group | Exports the selected or all measurements to the PlanSwift text format. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Excel` |  | panel: Takeoff Manager, Export group | Exports the selected or all measurements to `.xlsx`, columns J, K, L starting at J10. | [Export to Excel](ourplancore-excel.md) |
    | `Current Excel` |  | panel: Takeoff Manager, Export group | Writes the selected folder or takeoff into the active cell of the open Excel workbook. | [Export to Excel](ourplancore-excel.md) |

??? note "Report Builder, Template group (1)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Reload` |  | panel: Report Builder, Template group | Reloads `TemplateCom.xlsm` into the report builder table. | [AI and terminals](ourplancore-ai.md) |

??? note "Report Builder, Table group (1)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Refresh` |  | panel: Report Builder, Table group | Rereads the table of the current manager: sheets, takeoffs, report, materials or AI. | [Managers](ourplancore-managers.md) |

??? note "Report Builder, Walls group (1)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Apply Walls` |  | panel: Report Builder, Walls group | Applies the A3 wall block rule to the selected rows in columns J and K. | [Managers](ourplancore-managers.md) |

??? note "Materials, Extract group (3)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Extract` |  | panel: Materials, Extract group | Extracts material details from the current job's source PDFs. | [Managers](ourplancore-managers.md) |
    | `Report Sheet` |  | panel: Materials, Extract group | Creates a `Materials Report` sheet for copying from the job's existing sheets. | [Managers](ourplancore-managers.md) |
    | `Refresh` |  | panel: Materials, Extract group | Rereads the table of the current manager: sheets, takeoffs, report, materials or AI. | [Managers](ourplancore-managers.md) |

??? note "Materials, Open group (4)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `JSON` |  | panel: Materials, Open group | Opens the full JSON of the material extraction result. | [Managers](ourplancore-managers.md) |
    | `Rows CSV` |  | panel: Materials, Open group | Opens the rows of the materials found as CSV. | [Managers](ourplancore-managers.md) |
    | `Summary CSV` |  | panel: Materials, Open group | Opens the summary of materials by group as CSV. | [Managers](ourplancore-managers.md) |
    | `Folder` |  | panel: Materials, Open group | Opens the job folder with the material extraction results. | [Takeoffs tree](ourplancore-takeoffs.md) |

??? note "AI Manager, Setup group (2)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `AI Settings` |  | panel: AI Manager, Setup group | Shows the OpenAI key status and the AI model settings. | [AI and terminals](ourplancore-ai.md) |
    | `+ Add` |  | panel: AI Manager, Setup group | Saves a manual AI observation or marker note for the job and sheet. | [AI and terminals](ourplancore-ai.md) |

??? note "AI Manager, Review group (4)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Refresh` |  | panel: AI Manager, Review group | Rereads the table of the current manager: sheets, takeoffs, report, materials or AI. | [AI and terminals](ourplancore-ai.md) |
    | `Open Details` |  | panel: AI Manager, Review group | Opens the details window of the selected AI entry. | [AI and terminals](ourplancore-ai.md) |
    | `Go to Page` |  | panel: AI Manager, Review group | Opens the sheet the selected entry, observation or measurement belongs to. | [AI and terminals](ourplancore-ai.md) |
    | `Run AI` |  | panel: AI Manager, Review group | Sends the request of the selected entry or observation to the AI. | [AI and terminals](ourplancore-ai.md) |

??? note "AI Manager, Batch group (2)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Run New` |  | panel: AI Manager, Batch group | Sends only the new crop bookmarks to OpenAI. | [AI and terminals](ourplancore-ai.md) |
    | `Retry Failed` |  | panel: AI Manager, Batch group | Retries only the crop bookmarks whose request failed. | [AI and terminals](ourplancore-ai.md) |

??? note "AI Manager, Markers group (3)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Create Set` |  | panel: AI Manager, Markers group | Saves the current filters of reviewed markers as a named set. | [AI and terminals](ourplancore-ai.md) |
    | `Marker Sets` |  | panel: AI Manager, Markers group | Opens the window for managing saved AI marker sets. | [AI and terminals](ourplancore-ai.md) |
    | `Export Markers` |  | panel: AI Manager, Markers group | Exports the context of the visible reviewed markers to JSON. | [AI and terminals](ourplancore-ai.md) |

??? note "3D, Build group (5)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Auto` |  | panel: 3D, Build group | Restores adaptive sheet DPI in Sheet Manager; in 3D builds walls, slabs and roofs by itself. | [3D and managers](ourplancore-3d.md) |
    | `Wall` |  | panel: 3D, Build group | Builds 3D walls from the selected linear takeoffs and measurements. | [3D and managers](ourplancore-3d.md) |
    | `Roof Base` |  | panel: 3D, Build group | Creates a 3D roof base from the selected area measurements. | [3D roof](ourplancore-3d-roof.md) |
    | `Select Edge` |  | panel: 3D, Build group | Selects the lower roof edges on the sheet; the pitch of each edge is saved in the side panel. | [3D roof](ourplancore-3d-roof.md) |
    | `Generate Roof` |  | panel: 3D, Build group | Builds ridges, hips and valleys from the saved roof edge pitches. | [3D roof](ourplancore-3d-roof.md) |

??? note "3D, Rafters group (5)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Pick Faces` |  | panel: 3D, Rafters group | Turns rafters on or off on a roof plane with a click on it in 3D. | [3D roof](ourplancore-3d-roof.md) |
    | `Whole Roof` |  | panel: 3D, Rafters group | Lays out rafters on all planes of all built roofs. | [3D roof](ourplancore-3d-roof.md) |
    | `Rafter spacing o.c` |  | panel: 3D, Rafters group | Sets the rafter spacing on center, measured horizontally along the eave. | [3D roof](ourplancore-3d-roof.md) |
    | `Rafter member size` |  | panel: 3D, Rafters group | Sets the rafter size; the depth goes under the roof plane, the walls are trimmed. | [3D roof](ourplancore-3d-roof.md) |
    | `Clear` |  | panel: 3D, Rafters group | Removes rafters from all roofs in 3D; in the XL legend clears and saves the text. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |

??? note "3D, Viewer group (5)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Fit` |  | panel: 3D, Viewer group | Fits the whole 3D scene into the viewer window. | [3D and managers](ourplancore-3d.md) |
    | `Iso` |  | panel: 3D, Viewer group | Turns the 3D model to an isometric view from the side and above. | [3D and managers](ourplancore-3d.md) |
    | `Top` |  | panel: 3D, Viewer group | Shows the 3D model from above, like a building plan. | [3D and managers](ourplancore-3d.md) |
    | `Front` |  | panel: 3D, Viewer group | Shows the 3D model from the front, like a building elevation. | [3D and managers](ourplancore-3d.md) |
    | `Reset` |  | panel: 3D, Viewer group | Resets the 3D camera view or the shift, scale and rotation of the overlaid sheet. | [3D and managers](ourplancore-3d.md) |

??? note "XL legend (LG button) (4)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Hide the Excel legend panel` |  | panel: XL legend (LG button) | Hides the Excel legend panel opened with the `LG` button. | [Export to Excel](ourplancore-excel.md) |
    | `Add missing codes` |  | panel: XL legend (LG button) | Adds a legend row for each post, beam and header code that is missing from it. | [Export to Excel](ourplancore-excel.md) |
    | `Save for job` |  | panel: XL legend (LG button) | Saves the legend text for the current job. | [Export to Excel](ourplancore-excel.md) |
    | `Clear` |  | panel: XL legend (LG button) | Removes rafters from all roofs in 3D; in the XL legend clears and saves the text. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |

??? note "Quick Calculator (1)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Hide the calculator panel` |  | panel: Quick Calculator | Hides the slide-out `Quick Calculator` panel. |  |

??? note "Pages panel, Overlay tab (19)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Show overlay` |  | panel: Pages panel, Overlay tab | Shows or hides the overlaid sheet or overlay layer. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Add...` |  | panel: Pages panel, Overlay tab | Adds one more overlay layer to the active sheet. | [Editing and snaps](ourplancore-editing.md) |
    | `Open Source` |  | panel: Pages panel, Overlay tab | Opens the source sheet that is overlaid on the active one. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Choose / Replace...` |  | panel: Pages panel, Overlay tab | Picks or replaces the sheet that is overlaid on the active one. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Next Match` |  | panel: Pages panel, Overlay tab | Puts in the next suitable candidate sheet for the overlay. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Remove` |  | panel: Pages panel, Overlay tab | Removes the active overlay from the current sheet. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Move active layer down` |  | panel: Pages panel, Overlay tab | Moves the active overlay layer one position down. |  |
    | `Move active layer up` |  | panel: Pages panel, Overlay tab | Moves the active overlay layer one position up. |  |
    | `Auto Fit` |  | panel: Pages panel, Overlay tab | Automatically aligns the overlaid sheet with the active one. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Find Best` |  | panel: Pages panel, Overlay tab | Finds the best sheet in the job to overlay on the active one. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Edit by Points` |  | panel: Pages panel, Overlay tab | Aligns the overlay by pairs of points on the two sheets. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Reset` |  | panel: Pages panel, Overlay tab | Resets the 3D camera view or the shift, scale and rotation of the overlaid sheet. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Red` |  | panel: Pages panel, Overlay tab | Makes the overlaid sheet red to tell it apart from the base sheet. |  |
    | `Blue` |  | panel: Pages panel, Overlay tab | Makes the overlaid sheet blue to tell it apart from the base sheet. |  |
    | `Green` |  | panel: Pages panel, Overlay tab | Makes the overlaid sheet green to tell it apart from the base sheet. | [Settings and modules](ourplancore-settings.md) |
    | `Orange` |  | panel: Pages panel, Overlay tab | Makes the overlaid sheet orange to tell it apart from the base sheet. |  |
    | `Magenta` |  | panel: Pages panel, Overlay tab | Makes the overlaid sheet magenta to tell it apart from the base sheet. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Gray` |  | panel: Pages panel, Overlay tab | Makes the overlaid sheet gray to tell it apart from the base sheet. | [Settings and modules](ourplancore-settings.md) |
    | `Choose custom color` |  | panel: Pages panel, Overlay tab | Opens a custom color picker for the overlaid sheet. |  |

??? note "Codex / Claude terminal panel (23)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Detach terminal to its own window` |  | panel: Codex / Claude terminal panel | Moves the terminal into a separate window, the conversation continues. | [AI console](ourplancore-ai-console.md) |
    | `Settings -> Terminals` |  | panel: Codex / Claude terminal panel | Opens the `Terminals` settings section with the Claude and Codex profiles. | [AI console](ourplancore-ai-console.md) |
    | `Terminal actions` |  | panel: Codex / Claude terminal panel | Opens the terminal menu in a narrow panel: move it to a window or open the settings. | [AI console](ourplancore-ai-console.md) |
    | `Hide panel` |  | panel: Codex / Claude terminal panel | Hides the terminal panel, the conversations continue. | [AI console](ourplancore-ai-console.md) |
    | `Codex` |  | panel: Codex / Claude terminal panel | Switches the terminal panel to the conversation with Codex. | [AI console](ourplancore-ai-console.md) |
    | `Claude` |  | panel: Codex / Claude terminal panel | Switches the terminal panel to the conversation with Claude. | [AI console](ourplancore-ai-console.md) |
    | `DeepSeek` |  | panel: Codex / Claude terminal panel | Switches the terminal panel to DeepSeek through the local Codex CLI. | [AI console](ourplancore-ai-console.md) |
    | `Run` |  | panel: Codex / Claude terminal panel | Starts or continues the assistant with the selected E-Wood shortcut. |  |
    | `Attach` |  | panel: Codex / Claude terminal panel | Attaches an already open Git Bash or mintty window to the panel. | [AI console](ourplancore-ai-console.md) |
    | `Reasoning effort for the next launch` |  | panel: Codex / Claude terminal panel | Picks the reasoning effort for the next launch: Quick, Balanced or Deep. | [AI console](ourplancore-ai-console.md) |
    | `Context` |  | panel: Codex / Claude terminal panel | Opens the live sheet context file for the assistant. | [AI console](ourplancore-ai-console.md) |
    | `Paste context` |  | panel: Codex / Claude terminal panel | Pastes the context message into the terminal without `Enter`, you send it yourself. | [AI console](ourplancore-ai-console.md) |
    | `AI Inbox` |  | panel: Codex / Claude terminal panel | Opens `AI Inbox` and the AI manager. | [AI console](ourplancore-ai-console.md) |
    | `AI Crop +` |  | panel: Codex / Claude terminal panel | Draws a crop for the AI and passes its PNG into the terminal context. | [AI console](ourplancore-ai-console.md) |
    | `Explain` |  | panel: Codex / Claude terminal panel | Crop one or more areas around a detail (Esc when done), then Send: the assistant explains it and draws a step-by-step isometric assembly diagram (HTML) | [AI and terminals](ourplancore-ai.md) |
    | `Explain + image` |  | panel: Codex / Claude terminal panel | Same as Explain, plus a generated illustration image (needs an assistant that can generate images, e.g. Codex) |  |
    | `F7` | `F7` | panel: Codex / Claude terminal panel | Record speech locally (F7). Press again to stop and insert text without Enter. |  |
    | `Cancel` |  | panel: Codex / Claude terminal panel | Cancels the background raster work after the current sheet. | [AI console](ourplancore-ai-console.md) |
    | `Insert text` |  | panel: Codex / Claude terminal panel | Insert this draft into the selected terminal without Enter |  |
    | `Copy` |  | panel: Codex / Claude terminal panel |  | [Editing and snaps](ourplancore-editing.md) |
    | `Close` |  | panel: Codex / Claude terminal panel |  | [AI console](ourplancore-ai-console.md) |
    | `Send ↵` |  | panel: Codex / Claude terminal panel |  |  |
    | `Reference Close Button` |  | panel: Codex / Claude terminal panel | Keep the draft and return to the terminal |  |

## Context menus and button menus (386)

??? note "Combine button menu, bottom tool strip, row 1 (5)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Union` |  | menu: Combine button menu, bottom tool strip, row 1 | Merges the selected areas into one combined area. | [Editing and snaps](ourplancore-editing.md) |
    | `Subtract` |  | menu: Combine button menu, bottom tool strip, row 1 | Subtracts all other selected areas from the first selected one. | [Editing and snaps](ourplancore-editing.md) |
    | `Intersect` |  | menu: Combine button menu, bottom tool strip, row 1 | Keeps only the common part of all selected areas. | [Editing and snaps](ourplancore-editing.md) |
    | `Remove Overlap` |  | menu: Combine button menu, bottom tool strip, row 1 | Trims the overlaps of the selected areas so nothing is counted twice. | [Editing and snaps](ourplancore-editing.md) |
    | `Divide` |  | menu: Combine button menu, bottom tool strip, row 1 | Divides the selected areas into separate parts and a shared overlap piece. | [Editing and snaps](ourplancore-editing.md) |

??? note "Open button menu, Main View, Pages panel (2)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Open as Tabs` |  | menu: Open button menu, Main View, Pages panel | Opens the sheets selected in the Pages tree in tabs. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Detach to windows` |  | menu: Open button menu, Main View, Pages panel | Opens the sheets selected in the Pages tree in separate windows. | [Other](ourplancore-extras-other.md) |

??? note "+ New button menu, Main View, Pages panel, quick row (3)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `New Folder` |  | menu: + New button menu, Main View, Pages panel, quick row | Creates a new folder inside the selected Pages folder. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Blank Sheet` |  | menu: + New button menu, Main View, Pages panel, quick row | Creates a blank sheet in the current job without a PDF. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Auto Folders` |  | menu: + New button menu, Main View, Pages panel, quick row | Creates the standard sheet folder tree in the selected Pages folder. | [Sheets (Pages)](ourplancore-pages.md) |

??? note "Setup button menu, Main View, Pages panel, quick row (4)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Name / Scale...` |  | menu: Setup button menu, Main View, Pages panel, quick row | Opens the window for setting the active sheet's name and scale by hand. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Sort: A -> Arch / S -> Struct` |  | menu: Setup button menu, Main View, Pages panel, quick row | Sorts A sheets into `Arch`, S sheets into `Struct`, the rest into others. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Sort: D / Sec / WT suffix` |  | menu: Setup button menu, Main View, Pages panel, quick row | Sorts sheets with suffixes into the details, sections, units folders and orders the Pages root. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Repair page links` |  | menu: Setup button menu, Main View, Pages panel, quick row | Reattaches measurements to sheets after pages are renamed or imported. | [Sheets (Pages)](ourplancore-pages.md) |

??? note "More button menu, Main View, Takeoffs panel (3)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Roof Base from area` |  | menu: More button menu, Main View, Takeoffs panel | Creates a 3D roof base from the selected area measurements. | [3D roof](ourplancore-3d-roof.md) |
    | `Auto Tree` |  | menu: More button menu, Main View, Takeoffs panel | Creates the standard takeoff folder tree for a new job. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `From Pages` |  | menu: More button menu, Main View, Takeoffs panel | Creates top takeoff folders from the names of Pages sheets and folders typed in capitals. | [Takeoffs tree](ourplancore-takeoffs.md) |

??? note "More button menu (AI Inbox) (5)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Run New Bookmarks` |  | menu: More button menu (AI Inbox) | Sends only the new crop bookmarks to OpenAI. | [AI and terminals](ourplancore-ai.md) |
    | `Retry Failed Bookmarks` |  | menu: More button menu (AI Inbox) | Retries only the crop bookmarks whose request failed. | [AI and terminals](ourplancore-ai.md) |
    | `Create Marker Set` |  | menu: More button menu (AI Inbox) | Saves the current filters of reviewed markers as a named set. | [AI and terminals](ourplancore-ai.md) |
    | `Manage Marker Sets...` |  | menu: More button menu (AI Inbox) | Opens the window for managing saved AI marker sets. | [AI and terminals](ourplancore-ai.md) |
    | `Export Marker Context` |  | menu: More button menu (AI Inbox) | Exports the context of the visible reviewed markers to JSON. | [AI and terminals](ourplancore-ai.md) |

??? note "AI Inbox entry menu (7)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Refresh Inbox` |  | menu: AI Inbox entry menu | Rereads the list of `AI Inbox` entries from the job folder. | [AI and terminals](ourplancore-ai.md) |
    | `Open Details` |  | menu: AI Inbox entry menu | Opens the details window of the selected AI entry. | [AI and terminals](ourplancore-ai.md) |
    | `Go to Page` |  | menu: AI Inbox entry menu | Opens the sheet the selected entry, observation or measurement belongs to. | [AI and terminals](ourplancore-ai.md) |
    | `Run AI Request` |  | menu: AI Inbox entry menu | Sends the selected entry's request to the AI. | [AI and terminals](ourplancore-ai.md) |
    | `Open Project Context` |  | menu: AI Inbox entry menu | Opens the job context file for the AI in Markdown format. | [AI and terminals](ourplancore-ai.md) |
    | `Use in Codex / Claude / DeepSeek terminal` |  | menu: AI Inbox entry menu | Picks an AI Inbox entry for the live context of the Codex, Claude or DeepSeek terminal. | [AI console](ourplancore-ai-console.md) |
    | `Refresh Inbox` |  | menu: AI Inbox entry menu | Rereads the list of `AI Inbox` entries from the job folder. | [AI and terminals](ourplancore-ai.md) |

??? note "AI Inbox entry menu > Crop (4)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Open Crop` |  | menu: AI Inbox entry menu > Crop | Opens the crop image that an AI entry or observation was made from. | [AI and terminals](ourplancore-ai.md) |
    | `Open Crop Folder` |  | menu: AI Inbox entry menu > Crop | Opens the folder with the selected entry's crop image in File Explorer. | [AI and terminals](ourplancore-ai.md) |
    | `Bookmark Crop For Batch AI` |  | menu: AI Inbox entry menu > Crop | Bookmarks the entry's crop for a batch AI send. | [AI and terminals](ourplancore-ai.md) |
    | `Open Bookmark JSON` |  | menu: AI Inbox entry menu > Crop | Opens the JSON file of the selected entry's crop bookmark. |  |

??? note "AI Inbox entry menu > Marker (8)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Edit Marker` |  | menu: AI Inbox entry menu > Marker | Opens the type, label and location of the selected AI marker for editing. | [AI and terminals](ourplancore-ai.md) |
    | `Delete Marker` |  | menu: AI Inbox entry menu > Marker | Deletes the selected AI marker from the job. | [AI and terminals](ourplancore-ai.md) |
    | `Find Similar From Marker` |  | menu: AI Inbox entry menu > Marker | Queues a search for similar symbols based on the selected marker. | [AI and terminals](ourplancore-ai.md) |
    | `Create Marker Set From Filter` |  | menu: AI Inbox entry menu > Marker | Creates a marker set from the entries visible under the current filter. | [AI and terminals](ourplancore-ai.md) |
    | `Manage Marker Sets...` |  | menu: AI Inbox entry menu > Marker | Opens the window for managing saved marker sets. | [AI and terminals](ourplancore-ai.md) |
    | `Export Marker Context` |  | menu: AI Inbox entry menu > Marker | Exports the marker context to JSON and opens the file right away. | [AI and terminals](ourplancore-ai.md) |
    | `Hide This Marker Type` |  | menu: AI Inbox entry menu > Marker | Hides all markers of the same type in `AI Inbox`. | [AI and terminals](ourplancore-ai.md) |
    | `Show All Marker Types` |  | menu: AI Inbox entry menu > Marker | Shows all hidden marker types in `AI Inbox` again. | [AI and terminals](ourplancore-ai.md) |

??? note "AI Inbox entry menu > AI Response (5)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Add Manual AI Response` |  | menu: AI Inbox entry menu > AI Response | Adds an AI response to the entry by hand, for example one copied from a chat. | [AI and terminals](ourplancore-ai.md) |
    | `Preview Action Draft` |  | menu: AI Inbox entry menu > AI Response | Shows on the sheet the draft of actions proposed by the AI response. | [AI and terminals](ourplancore-ai.md) |
    | `Review Action Draft` |  | menu: AI Inbox entry menu > AI Response | Opens a review of the AI action draft before it is applied. | [AI and terminals](ourplancore-ai.md) |
    | `Apply Sheet Metadata Response` |  | menu: AI Inbox entry menu > AI Response | Applies the sheet name and scale from the AI response. | [AI and terminals](ourplancore-ai.md) |
    | `Clear Action Preview` |  | menu: AI Inbox entry menu > AI Response | Removes the preview of the AI action draft from the sheet. | [AI and terminals](ourplancore-ai.md) |

??? note "AI Inbox entry menu > Files (5)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Open Request JSON` |  | menu: AI Inbox entry menu > Files | Opens the JSON file of the selected entry's AI request. | [AI and terminals](ourplancore-ai.md) |
    | `Open Layer JSON` |  | menu: AI Inbox entry menu > Files | Opens the JSON file describing the entry's PDF layers. |  |
    | `Open Response JSON` |  | menu: AI Inbox entry menu > Files | Opens the JSON file of the selected entry's AI response. |  |
    | `Open Action Draft JSON` |  | menu: AI Inbox entry menu > Files | Opens the JSON file of the AI action draft. |  |
    | `Open Marker JSON` |  | menu: AI Inbox entry menu > Files | Opens the JSON file of the selected AI marker. |  |

??? note "Count Display menu (Count marker symbol) (1)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Symbol: Cross, Square, Star, Triangle, Diamond, Ring, Circle` |  | menu: Count Display menu (Count marker symbol) | Picks the Count point symbol: cross, square, star, triangle, diamond, ring or circle. | [Measuring tools](ourplancore-tools.md) |

??? note "default Count symbol button menu (bottom tool strip) (1)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Symbol: Cross, Square, Star, Triangle, Diamond, Ring, Circle` |  | menu: default Count symbol button menu (bottom tool strip) | Picks the Count point symbol: cross, square, star, triangle, diamond, ring or circle. | [Measuring tools](ourplancore-tools.md) |

??? note "viewport menu in a separate sheet window (11)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Enable Automatic Legend Blocks on This Sheet` |  | menu: viewport menu in a separate sheet window | Turns on automatic legend blocks on this sheet; the same item again turns them off, manual groups stay. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Copy Measurement` |  | menu: viewport menu in a separate sheet window | Copies the selected measurements and marks to the app clipboard. | [Editing and snaps](ourplancore-editing.md) |
    | `Show on This Sheet` |  | menu: viewport menu in a separate sheet window | Shows or hides this takeoff on this sheet only. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Paste Measurements to This Sheet` |  | menu: viewport menu in a separate sheet window | Pastes the copied measurements onto this sheet. | [Editing and snaps](ourplancore-editing.md) |
    | `Takeoff Properties...` |  | menu: viewport menu in a separate sheet window | Opens the properties of the takeoff the selected measurement belongs to. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Measurement Properties...` |  | menu: viewport menu in a separate sheet window | Opens the properties of the selected measurement for editing. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Rename Measurement` |  | menu: viewport menu in a separate sheet window | Renames the selected measurement or its takeoff. | [Editing and snaps](ourplancore-editing.md) |
    | `Use Area As Joists...` |  | menu: viewport menu in a separate sheet window | Turns the selected area into a `Joist Area` joist layout. | [Measuring tools](ourplancore-tools.md) |
    | `Refresh Regular Joists in All Area Segments` |  | menu: viewport menu in a separate sheet window | Recalculates the regular joists in all areas of the `Joist Area` takeoff. | [Measuring tools](ourplancore-tools.md) |
    | `Set / Reset Joist Direction` |  | menu: viewport menu in a separate sheet window | Sets or resets the joist direction in the selected area. | [Measuring tools](ourplancore-tools.md) |
    | `Delete Nearest Extra Joist` |  | menu: viewport menu in a separate sheet window | Deletes the Extra Joist nearest to the pointer. | [Editing and snaps](ourplancore-editing.md) |

??? note "line weight presets menu (Viewport ribbon) (1)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Custom...` |  | menu: line weight presets menu (Viewport ribbon) | Sets your own size or thickness as a number instead of a preset. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |

??? note "point size presets menu (Viewport ribbon) (1)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Custom...` |  | menu: point size presets menu (Viewport ribbon) | Sets your own size or thickness as a number instead of a preset. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |

??? note "viewport menu: legend and labels (5)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Enable Automatic Legend Blocks on This Sheet` |  | menu: viewport menu: legend and labels | Turns on automatic legend blocks on this sheet; the same item again turns them off, manual groups stay. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Scale Legend With Sheet` |  | menu: viewport menu: legend and labels | Resizes the legend together with the sheet zoom. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Scale Measurement Labels With Sheet` |  | menu: viewport menu: legend and labels | Resizes the measurement labels together with the sheet zoom. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Scale Sheet Header With Sheet` |  | menu: viewport menu: legend and labels | Resizes the sheet header together with the sheet zoom. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Legend` |  | menu: viewport menu: legend and labels | Shows or hides the legend on the active sheet. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |

??? note "viewport menu > legend / header size (1)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Custom...` |  | menu: viewport menu > legend / header size | Sets your own size or thickness as a number instead of a preset. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |

??? note "Size button menu (Display ribbon) (1)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Custom...` |  | menu: Size button menu (Display ribbon) | Sets your own size or thickness as a number instead of a preset. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |

??? note "Estimating row menu (5)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Go to Page` |  | menu: Estimating row menu | Opens the sheet the selected entry, observation or measurement belongs to. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Select on Canvas` |  | menu: Estimating row menu | Selects on the sheet the measurements of the selected rows or sections. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Measurement Properties...` |  | menu: Estimating row menu | Opens the properties of the selected measurement for editing. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Rename Measurement` |  | menu: Estimating row menu | Renames the selected measurement or its takeoff. | [Editing and snaps](ourplancore-editing.md) |
    | `Delete Measurement` |  | menu: Estimating row menu | Deletes the selected measurement from the sheet and from the takeoff. | [Editing and snaps](ourplancore-editing.md) |

??? note "takeoff menu in Takeoffs > Excel Link (9)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Link to Excel` |  | menu: takeoff menu in Takeoffs > Excel Link | Links this takeoff to the active cell of the open workbook. | [Export to Excel](ourplancore-excel.md) |
    | `Go to Cell` |  | menu: takeoff menu in Takeoffs > Excel Link | Shows the linked cell in Excel, opening a closed workbook first. | [Export to Excel](ourplancore-excel.md) |
    | `Overwrite the Cell` |  | menu: takeoff menu in Takeoffs > Excel Link | Writes the app's number over a cell that was edited by hand. | [Export to Excel](ourplancore-excel.md) |
    | `Keep the Cell and Unlink` |  | menu: takeoff menu in Takeoffs > Excel Link | Keeps the cell as it is and breaks the link. | [Export to Excel](ourplancore-excel.md) |
    | `Unlink` |  | menu: takeoff menu in Takeoffs > Excel Link | Breaks the link, the number stays in the cell. | [Export to Excel](ourplancore-excel.md) |
    | `Auto Link (DFL)` |  | menu: takeoff menu in Takeoffs > Excel Link | DFL only: links right away the takeoffs whose numbers already sit in the `J:L` list. | [Export to Excel](ourplancore-excel.md) |
    | `Update Links` |  | menu: takeoff menu in Takeoffs > Excel Link | Writes all pending link numbers, including into closed workbooks. | [Export to Excel](ourplancore-excel.md) |
    | `Reset All Links...` |  | menu: takeoff menu in Takeoffs > Excel Link | Removes all the job's links to Excel after a prompt. The values in the cells stay. | [Export to Excel](ourplancore-excel.md) |
    | `All Excel Links...` |  | menu: takeoff menu in Takeoffs > Excel Link | Opens the list of all the job's links to Excel. | [Export to Excel](ourplancore-excel.md) |

??? note "Export button menu (Takeoffs panel) (6)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Save` |  | menu: Export button menu (Takeoffs panel) | Saves the current job with all its measurements. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Save As...` |  | menu: Export button menu (Takeoffs panel) | Saves the current job to a new location on disk. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Export CSV` |  | menu: Export button menu (Takeoffs panel) | Exports the measurement rows to a CSV file. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Export TXT` |  | menu: Export button menu (Takeoffs panel) | Exports the selected or all measurements to the PlanSwift text format. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Export Excel` |  | menu: Export button menu (Takeoffs panel) | Exports the selected or all measurements to `.xlsx`, columns J, K, L starting at J10. | [Export to Excel](ourplancore-excel.md) |
    | `Export to Current Excel` |  | menu: Export button menu (Takeoffs panel) | Writes the selected folder or takeoff into the active cell of the open Excel workbook. | [Export to Excel](ourplancore-excel.md) |

??? note "Open / Import button menu > Open A Project (1)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Open project...` |  | menu: Open / Import button menu > Open A Project | Opens the job picker window with the recent list. | [Jobs and saving](job-creation-storage.md) |

??? note "Open / Import button menu > Create A New Job (9)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Blank project - start empty` |  | menu: Open / Import button menu > Create A New Job | Creates an empty job, sheets are added later. | [Jobs and saving](job-creation-storage.md) |
    | `New project from a folder of PDFs...` |  | menu: Open / Import button menu > Create A New Job | Creates a new job from a folder of PDF drawings. | [Jobs and saving](job-creation-storage.md) |
    | `Import PDF Takeoffs...` |  | menu: Open / Import button menu > Create A New Job | Brings PDF sheets over together with the PDF measurements and rulers into takeoffs. | [Other](ourplancore-extras-other.md) |
    | `Sample job (demo to explore)` |  | menu: Open / Import button menu > Create A New Job | Creates and opens a sample tutorial job with hints. | [Jobs and saving](job-creation-storage.md) |
    | `Create Excel workbook for this project...` |  | menu: Open / Import button menu > Create A New Job |  |  |
    | `Undo Last Page Sort` |  | menu: Open / Import button menu > Create A New Job | Undoes the last sheet sort in the Pages tree. | [Editing and snaps](ourplancore-editing.md) |
    | `Undo Last Page Operation` |  | menu: Open / Import button menu > Create A New Job | Undoes the last sheet operation: sort, move or rename. | [Editing and snaps](ourplancore-editing.md) |
    | `Project Data Recovery...` |  | menu: Open / Import button menu > Create A New Job | Restores damaged job files from a verified copy. | [Jobs and saving](job-creation-storage.md) |
    | `Manage job folders...` |  | menu: Open / Import button menu > Create A New Job | Opens the management of the folders where jobs are kept. | [Jobs and saving](job-creation-storage.md) |

??? note "Open / Import button menu > Import into the current job > Create A New Job (4)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `PDF file(s)...` |  | menu: Open / Import button menu > Import into the current job > Create A New Job | Adds one or more PDFs to the current job. | [Jobs and saving](job-creation-storage.md) |
    | `Folder of PDFs...` |  | menu: Open / Import button menu > Import into the current job > Create A New Job | Imports all PDFs from the selected folder and its subfolders into the current job. | [Jobs and saving](job-creation-storage.md) |
    | `OurPlanCore project...` |  | menu: Open / Import button menu > Import into the current job > Create A New Job | Imports another OurPlanCore job into the current job. | [Jobs and saving](job-creation-storage.md) |
    | `PlanSwift project...` |  | menu: Open / Import button menu > Import into the current job > Create A New Job | Imports a PlanSwift job into the current job, into the `01. planswift` folder. | [Other](ourplancore-extras-other.md) |

??? note "Batch Rotate button menu (Page ribbon) (3)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Rotate Selected Left` |  | menu: Batch Rotate button menu (Page ribbon) | Rotates all selected sheets 90 degrees to the left. | [Editing and snaps](ourplancore-editing.md) |
    | `Rotate Selected Right` |  | menu: Batch Rotate button menu (Page ribbon) | Rotates all selected sheets 90 degrees to the right. | [Editing and snaps](ourplancore-editing.md) |
    | `Rotate Selected 180` |  | menu: Batch Rotate button menu (Page ribbon) | Rotates all selected sheets 180 degrees. | [Editing and snaps](ourplancore-editing.md) |

??? note "sheet legend menu > Legend Group (2)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `New Group...` |  | menu: sheet legend menu > Legend Group | Creates a new legend group from the selected rows. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Main Legend` |  | menu: sheet legend menu > Legend Group | Returns the selected rows from a group to the sheet's main legend. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |

??? note "folder menu in Pages (7)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Undo Last Page Delete` |  | menu: folder menu in Pages | Brings the last deleted sheet or folder back into the Pages tree. | [Editing and snaps](ourplancore-editing.md) |
    | `New Blank Sheet` |  | menu: folder menu in Pages | Creates a blank sheet in the selected Pages folder. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Batch Overlay...` |  | menu: folder menu in Pages | Matches sheet pairs and applies overlays to many sheets of the job at once. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `New Folder` |  | menu: folder menu in Pages | Creates a new folder inside the selected folder. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Rename Folder` |  | menu: folder menu in Pages | Renames the selected folder in the Pages or Takeoffs tree. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Delete Folder` |  | menu: folder menu in Pages | Deletes the selected folder or all selected rows of the Pages tree. | [Editing and snaps](ourplancore-editing.md) |
    | `Open in Explorer` |  | menu: folder menu in Pages | Opens the folder on disk in Windows File Explorer. | [Sheets (Pages)](ourplancore-pages.md) |

??? note "folder menu in Pages > Clipboard (3)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Copy Folder` |  | menu: folder menu in Pages > Clipboard | Copies the selected folder or rows to the tree clipboard. | [Editing and snaps](ourplancore-editing.md) |
    | `Cut Folder` |  | menu: folder menu in Pages > Clipboard | Cuts the selected folder or rows to move them elsewhere in the tree. | [Editing and snaps](ourplancore-editing.md) |
    | `Paste Into Folder` |  | menu: folder menu in Pages > Clipboard | Pastes the copied or cut rows into this folder. | [Editing and snaps](ourplancore-editing.md) |

??? note "folder menu in Pages > Organize (13)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Auto Create Folders` |  | menu: folder menu in Pages > Organize | Creates the standard sheet folders from the template in this folder. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Move Up` |  | menu: folder menu in Pages > Organize | Moves the selected rows one position up in the tree. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Move Down` |  | menu: folder menu in Pages > Organize | Moves the selected rows one position down in the tree. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Sort Children A-Z` |  | menu: folder menu in Pages > Organize | Sorts all contents of this folder alphabetically. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Sort Children Z-A` |  | menu: folder menu in Pages > Organize | Sorts the folder contents in reverse alphabetical order. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Sort Sheet Legends Auto in Folder` |  | menu: folder menu in Pages > Organize | Restores the automatic legend order on all sheets in the folder. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Sort Sheet Legends A-Z in Folder` |  | menu: folder menu in Pages > Organize | Sorts the legend rows of all sheets in the folder alphabetically. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Sort Sheet Legends by Key (before space) in Folder` |  | menu: folder menu in Pages > Organize | Sorts the legends of the folder's sheets by the start of the name up to the first space. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Reset Sheet Legend Orders in Folder` |  | menu: folder menu in Pages > Organize | Resets the manual legend order of all sheets in the folder. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Sort A/S in This Folder` |  | menu: folder menu in Pages > Organize | Sorts this folder's sheets into `Arch` and `Struct` by the A and S prefixes. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Sort D/Sec/WT in This Folder` |  | menu: folder menu in Pages > Organize | Sorts this folder's sheets into suffix folders: details, sections, units. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Undo Last Page Sort` |  | menu: folder menu in Pages > Organize | Undoes the last sheet sort in the Pages tree. | [Editing and snaps](ourplancore-editing.md) |
    | `Repair Measurement Links` |  | menu: folder menu in Pages > Organize | Reattaches the saved measurements to the current sheet folders. | [Sheets (Pages)](ourplancore-pages.md) |

??? note "folder menu in Pages > PDF Metadata (5)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Analyze PDF Metadata` |  | menu: folder menu in Pages > PDF Metadata | Reads the PDF text and title block and shows the names and scales found. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Auto Rename from PDF...` |  | menu: folder menu in Pages > PDF Metadata | Shows and applies the sheet names found in the PDF. | [Editing and snaps](ourplancore-editing.md) |
    | `Auto Scale from PDF...` |  | menu: folder menu in Pages > PDF Metadata | Shows and applies the sheet scales found in the PDF. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Auto Rename + Scale from PDF...` |  | menu: folder menu in Pages > PDF Metadata | Shows and applies the sheet names and scales found in the PDF. | [Editing and snaps](ourplancore-editing.md) |
    | `Queue GPT Metadata Fallback` |  | menu: folder menu in Pages > PDF Metadata | Queues GPT for the sheets where the name or scale was not found. | [AI and terminals](ourplancore-ai.md) |

??? note "folder menu in Pages > Learning (3)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Capture Final Learning Snapshot` |  | menu: folder menu in Pages > Learning | Records the final sheet names and scales to train auto-naming. |  |
    | `Review Project Learned Rules...` |  | menu: folder menu in Pages > Learning | Opens the learned sheet naming rules of this job. |  |
    | `Review Global Learned Rules...` |  | menu: folder menu in Pages > Learning | Opens the learned sheet naming rules for all jobs. |  |

??? note "sheet menu in Pages (13)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Open in New Tab` |  | menu: sheet menu in Pages | Opens the sheet in a new tab of the viewer window. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Open Selected in New Tabs` |  | menu: sheet menu in Pages | Opens all selected sheets in new tabs. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Detach Sheet to Window` |  | menu: sheet menu in Pages | Opens the selected sheet in a separate floating window. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Tile Sheet on Monitor 2` |  | menu: sheet menu in Pages | Opens the sheet in a separate tiled window on the second monitor. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Set Scale...` |  | menu: sheet menu in Pages | Sets one scale on the selected sheets. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Apply Current Sheet Scale` |  | menu: sheet menu in Pages | Applies the active sheet's scale to the selected sheets. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Export Sheet to PDF...` |  | menu: sheet menu in Pages | Exports the selected sheet or sheets to a PDF file. | [PDF and delivery](ourplancore-pdf.md) |
    | `Rename Page` |  | menu: sheet menu in Pages | Renames the selected sheet in the Pages tree. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Delete Page` |  | menu: sheet menu in Pages | Deletes the selected sheet or all selected sheets. | [Editing and snaps](ourplancore-editing.md) |
    | `Duplicate Page` |  | menu: sheet menu in Pages | Makes a copy of the selected sheet next to it. | [Sheets (Pages)](ourplancore-pages.md) |
    | `New Blank Sheet in Parent` |  | menu: sheet menu in Pages | Creates a blank sheet in the same folder as the selected one. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Change Sheet Size...` |  | menu: sheet menu in Pages | Changes the paper size of a blank sheet. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Open Page Folder in Explorer` |  | menu: sheet menu in Pages | Opens the sheet's folder on disk in Windows File Explorer. |  |

??? note "sheet menu in Pages > Clipboard (3)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Copy Page` |  | menu: sheet menu in Pages > Clipboard | Copies the selected sheet or sheets to the tree clipboard. | [Editing and snaps](ourplancore-editing.md) |
    | `Cut Page` |  | menu: sheet menu in Pages > Clipboard | Cuts the selected sheet or sheets to move them into another folder. | [Editing and snaps](ourplancore-editing.md) |
    | `Paste Into Parent Folder` |  | menu: sheet menu in Pages > Clipboard | Pastes the copied rows into the folder that holds the selected row. | [Editing and snaps](ourplancore-editing.md) |

??? note "sheet menu in Pages > Organize (12)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Move Up` |  | menu: sheet menu in Pages > Organize | Moves the selected rows one position up in the tree. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Move Down` |  | menu: sheet menu in Pages > Organize | Moves the selected rows one position down in the tree. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Move to Folder...` |  | menu: sheet menu in Pages > Organize | Moves the selected sheet into another folder of your choice. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Sort Sheet Legend Auto` |  | menu: sheet menu in Pages > Organize | Restores the automatic legend row order on this sheet. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Sort Sheet Legend A-Z` |  | menu: sheet menu in Pages > Organize | Sorts this sheet's legend rows alphabetically. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Sort Sheet Legend by Key (before space)` |  | menu: sheet menu in Pages > Organize | Sorts the sheet legend by the start of the name up to the first space. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Reset Sheet Legend Order` |  | menu: sheet menu in Pages > Organize | Resets the manual row order of this sheet's legend. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Legend Groups...` |  | menu: sheet menu in Pages > Organize | Opens the legend groups window for the selected sheets. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Copy Legend Groups to Selected Sheets` |  | menu: sheet menu in Pages > Organize | Copies this sheet's legend groups to the other selected sheets. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Sort A/S into Arch/Struct` |  | menu: sheet menu in Pages > Organize | Sorts the selected sheets into `Arch` and `Struct` folders by prefix. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Sort D/Sec/WT by Suffix` |  | menu: sheet menu in Pages > Organize | Sorts the selected sheets into folders by name suffix. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Repair Measurement Links` |  | menu: sheet menu in Pages > Organize | Reattaches the saved measurements to the current sheet folders. | [Sheets (Pages)](ourplancore-pages.md) |

??? note "sheet menu in Pages > PDF Metadata (6)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Analyze PDF Metadata` |  | menu: sheet menu in Pages > PDF Metadata | Reads the PDF text and title block and shows the names and scales found. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Auto Rename from PDF...` |  | menu: sheet menu in Pages > PDF Metadata | Shows and applies the sheet names found in the PDF. | [Editing and snaps](ourplancore-editing.md) |
    | `Auto Scale from PDF...` |  | menu: sheet menu in Pages > PDF Metadata | Shows and applies the sheet scales found in the PDF. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Auto Rename + Scale from PDF...` |  | menu: sheet menu in Pages > PDF Metadata | Shows and applies the sheet names and scales found in the PDF. | [Editing and snaps](ourplancore-editing.md) |
    | `Queue GPT Metadata Fallback` |  | menu: sheet menu in Pages > PDF Metadata | Queues GPT for the sheets where the name or scale was not found. | [AI and terminals](ourplancore-ai.md) |
    | `Open source_pdf.json` |  | menu: sheet menu in Pages > PDF Metadata | Opens the `source_pdf.json` file with this sheet's PDF metadata. |  |

??? note "sheet menu in Pages > Learning (3)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Capture Final Learning Snapshot` |  | menu: sheet menu in Pages > Learning | Records the final sheet names and scales to train auto-naming. |  |
    | `Review Project Learned Rules...` |  | menu: sheet menu in Pages > Learning | Opens the learned sheet naming rules of this job. |  |
    | `Review Global Learned Rules...` |  | menu: sheet menu in Pages > Learning | Opens the learned sheet naming rules for all jobs. |  |

??? note "sheet tab menu (5)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Detach Tab to Window` |  | menu: sheet tab menu | Moves this sheet tab into a separate window. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Tile Tab on Monitor 2` |  | menu: sheet tab menu | Moves this tab into a separate tiled window on the second monitor. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Detach All ... Tabs to Windows` |  | menu: sheet tab menu | Moves all open sheet tabs into separate windows. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Tile All ... Tabs on Monitor 2` |  | menu: sheet tab menu | Moves all open tabs into tiled windows on the second monitor. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Close Tab` |  | menu: sheet tab menu | Closes this sheet tab in the viewer window. | [Sheets (Pages)](ourplancore-pages.md) |

??? note "sheet legend menu (item under the sheet in Pages) (13)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Select Linked Takeoff` |  | menu: sheet legend menu (item under the sheet in Pages) | Selects in the Takeoffs tree the takeoff linked to this legend row. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Rename Linked Takeoff...` |  | menu: sheet legend menu (item under the sheet in Pages) | Renames the takeoff linked to this legend row. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Show on This Sheet` |  | menu: sheet legend menu (item under the sheet in Pages) | Shows or hides this takeoff on this sheet only. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Hide Selected on This Sheet` |  | menu: sheet legend menu (item under the sheet in Pages) | Hides the selected takeoffs on this sheet only. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Show Selected on This Sheet` |  | menu: sheet legend menu (item under the sheet in Pages) | Shows the selected takeoffs on this sheet. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Move Backward` |  | menu: sheet legend menu (item under the sheet in Pages) | Moves the selected takeoffs back, their measurements are drawn under the others. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Move Forward` |  | menu: sheet legend menu (item under the sheet in Pages) | Moves the selected takeoffs forward, their measurements are drawn over the others. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Move Up in Legend` |  | menu: sheet legend menu (item under the sheet in Pages) | Moves the selected rows higher in the sheet legend. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Move Down in Legend` |  | menu: sheet legend menu (item under the sheet in Pages) | Moves the selected rows lower in the sheet legend. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Sort Sheet Legend Auto` |  | menu: sheet legend menu (item under the sheet in Pages) | Restores the automatic legend row order on this sheet. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Sort Sheet Legend A-Z` |  | menu: sheet legend menu (item under the sheet in Pages) | Sorts this sheet's legend rows alphabetically. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Sort Sheet Legend by Key (before space)` |  | menu: sheet legend menu (item under the sheet in Pages) | Sorts the sheet legend by the start of the name up to the first space. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Reset Sheet Legend Order` |  | menu: sheet legend menu (item under the sheet in Pages) | Resets the manual row order of this sheet's legend. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |

??? note "PDF layer menu (Pages > PDF Layers) (9)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Save Layer Info for AI` |  | menu: PDF layer menu (Pages > PDF Layers) | Saves the PDF layer details into the AI context. | [Snap and tracing](ourplancore-snap-trace.md) |
    | `Queue AI Request for This Layer` |  | menu: PDF layer menu (Pages > PDF Layers) | Queues an AI request for this PDF layer. | [Snap and tracing](ourplancore-snap-trace.md) |
    | `Use for Layer Trace` |  | menu: PDF layer menu (Pages > PDF Layers) | Picks this PDF layer for `Layer Trace` tracing. | [Snap and tracing](ourplancore-snap-trace.md) |
    | `Trace Full Layer to Takeoff` |  | menu: PDF layer menu (Pages > PDF Layers) | Traces all lines of the PDF layer into one measurement. | [Snap and tracing](ourplancore-snap-trace.md) |
    | `Trace Nearest Edge to Takeoff` |  | menu: PDF layer menu (Pages > PDF Layers) | Traces the PDF layer edge nearest to the pointer into a measurement. | [Snap and tracing](ourplancore-snap-trace.md) |
    | `Trace Point to Takeoff` |  | menu: PDF layer menu (Pages > PDF Layers) | Places a point measurement at the PDF layer point under the pointer. | [Snap and tracing](ourplancore-snap-trace.md) |
    | `Trace All Edges to Takeoff` |  | menu: PDF layer menu (Pages > PDF Layers) | Traces all edges of the PDF layer as separate segments into a measurement. | [Snap and tracing](ourplancore-snap-trace.md) |
    | `Show Layer` |  | menu: PDF layer menu (Pages > PDF Layers) | Shows or hides this PDF layer on the sheet. | [Snap and tracing](ourplancore-snap-trace.md) |
    | `Highlight Layer` |  | menu: PDF layer menu (Pages > PDF Layers) | Highlights this PDF layer on the sheet or removes the highlight. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |

??? note "viewport menu: crop (Crop to Sheet) (12)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Open Source Sheet (...)` |  | menu: viewport menu: crop (Crop to Sheet) | Opens the sheet this crop was cut from. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Open Source Sheet (...)` |  | menu: viewport menu: crop (Crop to Sheet) | Opens the sheet this crop was cut from. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Rotate Crop 90° Clockwise` |  | menu: viewport menu: crop (Crop to Sheet) | Rotates the selected crop 90 degrees clockwise. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Rotate Crop 90° Counterclockwise` |  | menu: viewport menu: crop (Crop to Sheet) | Rotates the selected crop 90 degrees counterclockwise. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Mirror Crop Horizontal` |  | menu: viewport menu: crop (Crop to Sheet) | Mirrors the selected crop horizontally. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Mirror Crop Vertical` |  | menu: viewport menu: crop (Crop to Sheet) | Mirrors the selected crop vertically. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Reset Crop to 100% (true scale)` |  | menu: viewport menu: crop (Crop to Sheet) | Brings the crop back to 100 percent true scale. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Opacity...` |  | menu: viewport menu: crop (Crop to Sheet) | Sets the opacity of the selected crop on the sheet. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Bring to Front` |  | menu: viewport menu: crop (Crop to Sheet) | Brings the selected crop on top of all other crops. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Send to Back` |  | menu: viewport menu: crop (Crop to Sheet) | Sends the selected crop under all other crops. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Bring Forward` |  | menu: viewport menu: crop (Crop to Sheet) | Moves the selected crop one layer up. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Send Backward` |  | menu: viewport menu: crop (Crop to Sheet) | Moves the selected crop one layer down. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |

??? note "sheet menu in Pages > Sheet Overlay (5)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Overlay Properties...` |  | menu: sheet menu in Pages > Sheet Overlay | Opens the overlay properties: visibility, color, alignment. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Use This Sheet as Current Overlay` |  | menu: sheet menu in Pages > Sheet Overlay | Makes this sheet the current overlay on the active sheet. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Add This Sheet as New Overlay` |  | menu: sheet menu in Pages > Sheet Overlay | Adds this sheet as a new overlay layer on the active sheet. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Overlay Properties...` |  | menu: sheet menu in Pages > Sheet Overlay | Opens the overlay properties: visibility, color, alignment. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Clear Current Sheet Overlay` |  | menu: sheet menu in Pages > Sheet Overlay | Removes the current overlay from the active sheet. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |

??? note "overlay layer menu (under the sheet in Pages) (7)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Overlay Properties...` |  | menu: overlay layer menu (under the sheet in Pages) | Opens the overlay properties: visibility, color, alignment. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Open Overlay Sheet` |  | menu: overlay layer menu (under the sheet in Pages) | Opens the sheet that this layer overlays. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Show Overlay` |  | menu: overlay layer menu (under the sheet in Pages) | Shows or hides the overlaid sheet or overlay layer. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Open Overlay Sheet` |  | menu: overlay layer menu (under the sheet in Pages) | Opens the sheet that this layer overlays. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Move Layer Up` |  | menu: overlay layer menu (under the sheet in Pages) | Moves the overlay layer one position up. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Move Layer Down` |  | menu: overlay layer menu (under the sheet in Pages) | Moves the overlay layer one position down. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Remove Overlay Layer` |  | menu: overlay layer menu (under the sheet in Pages) | Removes this overlay layer from the sheet. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |

??? note "viewport menu: sheet overlay (3)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Overlay Properties...` |  | menu: viewport menu: sheet overlay | Opens the overlay properties: visibility, color, alignment. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Auto Fit Overlay` |  | menu: viewport menu: sheet overlay | Automatically aligns the overlaid sheet with the active one. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Fit by 2 Points` |  | menu: viewport menu: sheet overlay | Aligns the overlaid sheet by two pairs of points. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |

??? note "active takeoff More menu (Takeoffs panel) (5)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Properties...` |  | menu: active takeoff More menu (Takeoffs panel) | Opens the properties of the active takeoff for editing. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Find in Tree` |  | menu: active takeoff More menu (Takeoffs panel) | Scrolls the Takeoffs tree to the active takeoff. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Sheet Targets...` |  | menu: active takeoff More menu (Takeoffs panel) | Shows the takeoffs measured on this sheet so you can pick a target. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Previous Target` |  | menu: active takeoff More menu (Takeoffs panel) | Makes the previous takeoff in the target list active. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Next Target` |  | menu: active takeoff More menu (Takeoffs panel) | Makes the next takeoff in the target list active. | [Takeoffs tree](ourplancore-takeoffs.md) |

??? note "active takeoff Sheet menu (Takeoffs panel) (1)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Next Sheet Target` |  | menu: active takeoff Sheet menu (Takeoffs panel) | Makes active the next takeoff that has measurements on the active sheet. | [Sheets (Pages)](ourplancore-pages.md) |

??? note "MainWindow.TakeoffsAnnotation.cs:BuildTakeoffAnnotationMenuItem (1)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Make Quantity Takeoff` |  | menu: MainWindow.TakeoffsAnnotation.cs:BuildTakeoffAnnotationMenuItem |  |  |

??? note "section (measurement) menu in Takeoffs (18)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Section Properties...` |  | menu: section (measurement) menu in Takeoffs | Opens the properties of the selected measurement section in the Takeoffs tree. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Set Notes...` |  | menu: section (measurement) menu in Takeoffs | Writes notes for the selected measurement sections. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Rename Section` |  | menu: section (measurement) menu in Takeoffs | Renames the selected measurement section in the Takeoffs tree. | [Editing and snaps](ourplancore-editing.md) |
    | `Go to Page` |  | menu: section (measurement) menu in Takeoffs | Opens the sheet the selected entry, observation or measurement belongs to. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Select on Canvas` |  | menu: section (measurement) menu in Takeoffs | Selects on the sheet the measurements of the selected rows or sections. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Merge Segment...` |  | menu: section (measurement) menu in Takeoffs | Merges the selected takeoffs from all sheets or moves the selected measurements into another takeoff. | [Editing and snaps](ourplancore-editing.md) |
    | `Split Segment...` |  | menu: section (measurement) menu in Takeoffs | Splits takeoffs across all sheets or moves the selected measurements and points into a new takeoff. | [Editing and snaps](ourplancore-editing.md) |
    | `Create Count Points Along ... Lines...` |  | menu: section (measurement) menu in Takeoffs | Places Count points along the selected lines at a set spacing. | [Editing and snaps](ourplancore-editing.md) |
    | `Break ... Lines Into Segments` |  | menu: section (measurement) menu in Takeoffs | Breaks the selected polylines into separate segments. | [Editing and snaps](ourplancore-editing.md) |
    | `Count Points At ... Line Ends...` |  | menu: section (measurement) menu in Takeoffs | Places Count points at the ends of the selected lines. | [Editing and snaps](ourplancore-editing.md) |
    | `Create Line Grid...` |  | menu: section (measurement) menu in Takeoffs | Builds a grid of lines inside an area at a set horizontal and vertical spacing. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Refresh Regular Joists in All Area Segments` |  | menu: section (measurement) menu in Takeoffs | Recalculates the regular joists in all areas of the `Joist Area` takeoff. | [Measuring tools](ourplancore-tools.md) |
    | `Start Extra Joists Mode (D)` | `D` | menu: section (measurement) menu in Takeoffs | Turns on the mode for drawing additional Extra Joists. | [Measuring tools](ourplancore-tools.md) |
    | `Set / Reset Joist Direction` |  | menu: section (measurement) menu in Takeoffs | Sets or resets the joist direction in the selected area. | [Measuring tools](ourplancore-tools.md) |
    | `Set Direction for All Areas` |  | menu: section (measurement) menu in Takeoffs | Sets one joist direction for all areas of the takeoff. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Move Up` |  | menu: section (measurement) menu in Takeoffs | Moves the selected rows one position up in the tree. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Move Down` |  | menu: section (measurement) menu in Takeoffs | Moves the selected rows one position down in the tree. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Delete Section` |  | menu: section (measurement) menu in Takeoffs | Deletes the selected measurement section together with its geometry on the sheet. | [Editing and snaps](ourplancore-editing.md) |

??? note "takeoff menu in Takeoffs (17)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Set Active Target` |  | menu: takeoff menu in Takeoffs | Makes this takeoff the active drawing target. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `New Section` |  | menu: takeoff menu in Takeoffs | Adds a new measurement section to this takeoff. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Create Line Grid...` |  | menu: takeoff menu in Takeoffs | Builds a grid of lines inside an area at a set horizontal and vertical spacing. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Trace Walls Inside Area...` |  | menu: takeoff menu in Takeoffs | Traces the walls inside the selected area as linear measurements by thickness and minimum length. | [Snap and tracing](ourplancore-snap-trace.md) |
    | `Create Count Points Along Lines...` |  | menu: takeoff menu in Takeoffs | Places Count points along the takeoff's lines at a set spacing. | [Editing and snaps](ourplancore-editing.md) |
    | `Break Lines Into Segments` |  | menu: takeoff menu in Takeoffs | Breaks the takeoff's polylines into separate segments. | [Editing and snaps](ourplancore-editing.md) |
    | `Count Points At Line Ends...` |  | menu: takeoff menu in Takeoffs | Places Count points at the ends of the selected lines, a separate Count for each takeoff. | [Editing and snaps](ourplancore-editing.md) |
    | `Find Similar...` |  | menu: takeoff menu in Takeoffs | Finds similar symbols or measurements using this takeoff or measurement as a sample. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Merge Selected Takeoffs...` |  | menu: takeoff menu in Takeoffs | Merges the selected takeoffs from all sheets or moves the selected measurements into another takeoff. | [Editing and snaps](ourplancore-editing.md) |
    | `Split Selected Takeoffs...` |  | menu: takeoff menu in Takeoffs | Splits takeoffs across all sheets or moves the selected measurements and points into a new takeoff. | [Editing and snaps](ourplancore-editing.md) |
    | `Undo Takeoff Merge / Split` |  | menu: takeoff menu in Takeoffs | Undoes the last merge or split of takeoffs. | [Editing and snaps](ourplancore-editing.md) |
    | `Rename...` |  | menu: takeoff menu in Takeoffs | Renames the selected takeoff in the tree. | [Editing and snaps](ourplancore-editing.md) |
    | `Delete item + measurements` |  | menu: takeoff menu in Takeoffs | Deletes the selected takeoff together with all its measurements on all sheets. | [Editing and snaps](ourplancore-editing.md) |
    | `Duplicate Item` |  | menu: takeoff menu in Takeoffs | Makes a copy of the selected takeoff next to it in the tree. | [Editing and snaps](ourplancore-editing.md) |
    | `Properties...` |  | menu: takeoff menu in Takeoffs | Opens the properties of the selected takeoff for editing. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Bulk Properties...` |  | menu: takeoff menu in Takeoffs | Changes the properties of all selected takeoffs at once. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Set Unit Price` |  | menu: takeoff menu in Takeoffs | Sets the unit price for the selected takeoff. | [Takeoffs tree](ourplancore-takeoffs.md) |

??? note "takeoff menu in Takeoffs > Joist (5)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Use Area As Joists...` |  | menu: takeoff menu in Takeoffs > Joist | Turns the selected area into a `Joist Area` joist layout. | [Measuring tools](ourplancore-tools.md) |
    | `Refresh Regular Joists in All Area Segments` |  | menu: takeoff menu in Takeoffs > Joist | Recalculates the regular joists in all areas of the `Joist Area` takeoff. | [Measuring tools](ourplancore-tools.md) |
    | `Start Extra Joists Mode (D)` | `D` | menu: takeoff menu in Takeoffs > Joist | Turns on the mode for drawing additional Extra Joists. | [Measuring tools](ourplancore-tools.md) |
    | `Set / Reset Joist Direction` |  | menu: takeoff menu in Takeoffs > Joist | Sets or resets the joist direction in the selected area. | [Measuring tools](ourplancore-tools.md) |
    | `Set Direction for All Areas` |  | menu: takeoff menu in Takeoffs > Joist | Sets one joist direction for all areas of the takeoff. | [Measuring tools](ourplancore-tools.md) |

??? note "takeoff menu in Takeoffs > Clipboard (3)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Copy Item` |  | menu: takeoff menu in Takeoffs > Clipboard | Copies the selected takeoff or takeoffs to the tree clipboard. | [Editing and snaps](ourplancore-editing.md) |
    | `Cut Item` |  | menu: takeoff menu in Takeoffs > Clipboard | Cuts the selected takeoff or takeoffs to move them into another folder. | [Editing and snaps](ourplancore-editing.md) |
    | `Paste Into Parent Folder` |  | menu: takeoff menu in Takeoffs > Clipboard | Pastes the copied rows into the folder that holds the selected row. | [Editing and snaps](ourplancore-editing.md) |

??? note "takeoff menu in Takeoffs > Organize (2)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Move Up` |  | menu: takeoff menu in Takeoffs > Organize | Moves the selected rows one position up in the tree. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Move Down` |  | menu: takeoff menu in Takeoffs > Organize | Moves the selected rows one position down in the tree. | [Takeoffs tree](ourplancore-takeoffs.md) |

??? note "folder menu in Takeoffs (8)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `New Folder` |  | menu: folder menu in Takeoffs | Creates a takeoff folder in the selected folder or in the root. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `New Item` |  | menu: folder menu in Takeoffs | Creates a takeoff in the selected folder or in the root. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Rename Folder...` |  | menu: folder menu in Takeoffs | Renames the selected folder in the Pages or Takeoffs tree. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Delete folder + children` |  | menu: folder menu in Takeoffs | Deletes the folder together with all nested takeoffs and their measurements. | [Editing and snaps](ourplancore-editing.md) |
    | `Folder Properties...` |  | menu: folder menu in Takeoffs | Opens the folder properties: default color, price and notes. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Bulk Item Properties...` |  | menu: folder menu in Takeoffs | Changes the properties of all takeoffs inside the folder at once. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Random Colors for Items` |  | menu: folder menu in Takeoffs | Gives all takeoffs inside the folder random, different colors. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Open in Explorer` |  | menu: folder menu in Takeoffs | Opens the folder on disk in Windows File Explorer. | [Takeoffs tree](ourplancore-takeoffs.md) |

??? note "folder menu in Takeoffs > Clipboard (4)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Copy Folder` |  | menu: folder menu in Takeoffs > Clipboard | Copies the selected folder or rows to the tree clipboard. | [Editing and snaps](ourplancore-editing.md) |
    | `Cut Folder` |  | menu: folder menu in Takeoffs > Clipboard | Cuts the selected folder or rows to move them elsewhere in the tree. | [Editing and snaps](ourplancore-editing.md) |
    | `Paste Into Folder` |  | menu: folder menu in Takeoffs > Clipboard | Pastes the copied or cut rows into this folder. | [Editing and snaps](ourplancore-editing.md) |
    | `Duplicate Folder` |  | menu: folder menu in Takeoffs > Clipboard | Makes a copy of the selected folder with all its contents. | [Editing and snaps](ourplancore-editing.md) |

??? note "folder menu in Takeoffs > Organize (6)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Auto Create Tree` |  | menu: folder menu in Takeoffs > Organize | Creates the standard tree of folders and takeoffs in this folder. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Create Folders From Pages` |  | menu: folder menu in Takeoffs > Organize | Creates takeoff folders following the sheet structure in the Pages tree. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Move Up` |  | menu: folder menu in Takeoffs > Organize | Moves the selected rows one position up in the tree. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Move Down` |  | menu: folder menu in Takeoffs > Organize | Moves the selected rows one position down in the tree. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Sort Children A-Z` |  | menu: folder menu in Takeoffs > Organize | Sorts all contents of this folder alphabetically. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Sort Children Z-A` |  | menu: folder menu in Takeoffs > Organize | Sorts the folder contents in reverse alphabetical order. | [Sheets (Pages)](ourplancore-pages.md) |

??? note "Takeoffs root menu (6)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Auto Create Tree` |  | menu: Takeoffs root menu | Creates the standard tree of folders and takeoffs in this folder. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Create Folders From Pages` |  | menu: Takeoffs root menu | Creates takeoff folders following the sheet structure in the Pages tree. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Paste Into Root` |  | menu: Takeoffs root menu | Pastes the copied or cut rows into the root of the Takeoffs tree. | [Editing and snaps](ourplancore-editing.md) |
    | `Sort Root A-Z` |  | menu: Takeoffs root menu | Sorts the top level of the Takeoffs tree alphabetically. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Sort Root Z-A` |  | menu: Takeoffs root menu | Sorts the top level of the Takeoffs tree in reverse alphabetical order. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Open Takeoffs in Explorer` |  | menu: Takeoffs root menu | Opens the job's Takeoffs folder in Windows File Explorer. | [Takeoffs tree](ourplancore-takeoffs.md) |

??? note "takeoff menu in Takeoffs > 3D (2)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Wall` |  | menu: takeoff menu in Takeoffs > 3D | Builds 3D walls from the selected linear takeoffs and measurements. | [3D and managers](ourplancore-3d.md) |
    | `Roof Base from Area` |  | menu: takeoff menu in Takeoffs > 3D | Builds a 3D roof base from the selected areas. | [3D roof](ourplancore-3d-roof.md) |

??? note "Templates panel menu (8)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Create New Takeoff` |  | menu: Templates panel menu | Creates a takeoff in the job from the selected template. | [Other](ourplancore-extras-other.md) |
    | `Add Folder` |  | menu: Templates panel menu | Adds a new folder to the template tree of the Templates panel. | [Jobs and saving](job-creation-storage.md) |
    | `Add Line` |  | menu: Templates panel menu | Adds a new Line takeoff to the template. |  |
    | `Add Area` |  | menu: Templates panel menu | Adds a new Area takeoff to the template. |  |
    | `Add Count` |  | menu: Templates panel menu | Adds a new Count takeoff to the template. | [Measuring tools](ourplancore-tools.md) |
    | `Edit` |  | menu: Templates panel menu | Opens the selected template item for editing in the Templates panel. | [Other](ourplancore-extras-other.md) |
    | `Duplicate` |  | menu: Templates panel menu | Makes a copy of the selected template item next to it. | [Editing and snaps](ourplancore-editing.md) |
    | `Delete` |  | menu: Templates panel menu | Deletes the selected item from the template tree. | [Other](ourplancore-extras-other.md) |

??? note "viewport menu > 3D (3)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Create Roof Base from Areas` |  | menu: viewport menu > 3D | Builds the roof base from the RF areas and opens the 3D tab. | [3D roof](ourplancore-3d-roof.md) |
    | `Roof Edge Select` |  | menu: viewport menu > 3D | Turns roof edge selection on the sheet on or off for setting the pitch. | [3D roof](ourplancore-3d-roof.md) |
    | `Clear Roof Base` |  | menu: viewport menu > 3D | Deletes the roof base, the guides and the built roof planes. | [3D roof](ourplancore-3d-roof.md) |

??? note "viewport menu > 3D (roof edge) (4)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Add Edge to Selection` |  | menu: viewport menu > 3D (roof edge) | Adds a roof edge to the selection or removes it from the selection. | [3D roof](ourplancore-3d-roof.md) |
    | `Clear Edge Selection` |  | menu: viewport menu > 3D (roof edge) | Clears the selection of all roof edges. | [3D roof](ourplancore-3d-roof.md) |
    | `Set Edge as Eave + Pitch ...` |  | menu: viewport menu > 3D (roof edge) | Makes the selected edges an eave with the current roof pitch. | [3D roof](ourplancore-3d-roof.md) |
    | `Set Edge as Rake` |  | menu: viewport menu > 3D (roof edge) | Makes the selected edges a `Rake` with no roof plane. | [3D roof](ourplancore-3d-roof.md) |

??? note "Style menu > Color (1)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `More colors...` |  | menu: Style menu > Color |  |  |

??? note "viewport menu (right-click on the sheet) (1)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Open Project Context` |  | menu: viewport menu (right-click on the sheet) | Opens the job context file for the AI in Markdown format. | [Jobs and saving](job-creation-storage.md) |

??? note "viewport menu: measurement clipboard (4)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Copy Measurement` |  | menu: viewport menu: measurement clipboard | Copies the selected measurements to the app clipboard. | [Editing and snaps](ourplancore-editing.md) |
    | `Paste Measurements to This Sheet` |  | menu: viewport menu: measurement clipboard | Pastes the copied measurements onto this sheet. | [Editing and snaps](ourplancore-editing.md) |
    | `Merge Segment...` |  | menu: viewport menu: measurement clipboard | Merges the selected takeoffs from all sheets or moves the selected measurements into another takeoff. | [Editing and snaps](ourplancore-editing.md) |
    | `Split Segment...` |  | menu: viewport menu: measurement clipboard | Splits takeoffs across all sheets or moves the selected measurements and points into a new takeoff. | [Editing and snaps](ourplancore-editing.md) |

??? note "viewport menu > AI Assist (sheet point) (14)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `AI crop here -> note` |  | menu: viewport menu > AI Assist (sheet point) | Draws a crop at this spot, the AI reads it and writes a note on the sheet. | [AI and terminals](ourplancore-ai.md) |
    | `AI quick box here -> note` |  | menu: viewport menu > AI Assist (sheet point) | Takes a quick crop around the point, the AI reads it and writes a note. | [AI and terminals](ourplancore-ai.md) |
    | `Save AI crop here` |  | menu: viewport menu > AI Assist (sheet point) | Saves a crop of this spot of the sheet as an AI entry. | [AI and terminals](ourplancore-ai.md) |
    | `Save AI marker here` |  | menu: viewport menu > AI Assist (sheet point) | Places an AI marker with a type and label at this point. | [AI and terminals](ourplancore-ai.md) |
    | `Explain detail (crops -> diagram)` |  | menu: viewport menu > AI Assist (sheet point) |  |  |
    | `Explain detail + image` |  | menu: viewport menu > AI Assist (sheet point) |  |  |
    | `Ask AI about this point / area` |  | menu: viewport menu > AI Assist (sheet point) | Creates an `AI Inbox` request to explain what matters at this spot of the plan. | [AI and terminals](ourplancore-ai.md) |
    | `Read text near point` |  | menu: viewport menu > AI Assist (sheet point) | Creates an `AI Inbox` request to read and summarize the text near the point. | [AI and terminals](ourplancore-ai.md) |
    | `Save observation here` |  | menu: viewport menu > AI Assist (sheet point) | Saves a manual observation tied to this point of the sheet. | [AI and terminals](ourplancore-ai.md) |
    | `Add as pending check` |  | menu: viewport menu > AI Assist (sheet point) | Adds this spot to `AI Inbox` as a check before the final measurement. | [AI and terminals](ourplancore-ai.md) |
    | `Suggest takeoff item here` |  | menu: viewport menu > AI Assist (sheet point) | Suggests a takeoff for this spot of the sheet. | [AI and terminals](ourplancore-ai.md) |
    | `Trace wall from this point` |  | menu: viewport menu > AI Assist (sheet point) | Creates a request to trace a wall from this point, with a preview. | [AI and terminals](ourplancore-ai.md) |
    | `Trace closed area` |  | menu: viewport menu > AI Assist (sheet point) | Creates a request to trace a closed area from this point, with a preview. | [AI and terminals](ourplancore-ai.md) |
    | `Check missed takeoffs on this page` |  | menu: viewport menu > AI Assist (sheet point) | Creates an AI request to check that nothing is missed on the sheet. | [AI and terminals](ourplancore-ai.md) |

??? note "viewport menu: markup (annotation) (4)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Copy Markup` |  | menu: viewport menu: markup (annotation) | Copies the selected sheet marks to the clipboard. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Paste Markups Here` |  | menu: viewport menu: markup (annotation) | Pastes the copied marks at this spot of the sheet. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Edit Note...` |  | menu: viewport menu: markup (annotation) | Opens the text of the selected sheet note for editing. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Delete Markup` |  | menu: viewport menu: markup (annotation) | Deletes the selected mark or note from the sheet. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |

??? note "viewport menu > AI Assist (measurement) (7)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `AI crop here -> note` |  | menu: viewport menu > AI Assist (measurement) | Draws a crop at this spot, the AI reads it and writes a note on the sheet. | [AI and terminals](ourplancore-ai.md) |
    | `Save measurement AI crop` |  | menu: viewport menu > AI Assist (measurement) | Saves a crop around the selected measurement as an AI entry. | [AI and terminals](ourplancore-ai.md) |
    | `Save measurement as AI marker` |  | menu: viewport menu > AI Assist (measurement) | Saves the selected measurement as an AI marker. | [AI and terminals](ourplancore-ai.md) |
    | `Explain measurement` |  | menu: viewport menu > AI Assist (measurement) | Creates an AI request to explain the measurement and check that it fits the takeoff. | [AI and terminals](ourplancore-ai.md) |
    | `Find similar` |  | menu: viewport menu > AI Assist (measurement) | Finds similar symbols or measurements using this takeoff or measurement as a sample. | [AI and terminals](ourplancore-ai.md) |
    | `Link to observation` |  | menu: viewport menu > AI Assist (measurement) | Creates a request to link this measurement to a job observation or note. | [AI and terminals](ourplancore-ai.md) |
    | `Create note from measurement` |  | menu: viewport menu > AI Assist (measurement) | Creates a job note from the data of the selected measurement. | [AI and terminals](ourplancore-ai.md) |

??? note "Attach menu (terminal) (1)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Refresh` |  | menu: Attach menu (terminal) | Rereads the list of open mintty windows for connecting to the terminal. | [AI console](ourplancore-ai-console.md) |

??? note "More menu (terminal) (2)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Detach to window` |  | menu: More menu (terminal) | Moves the terminal into a separate window, the conversation continues. | [Other](ourplancore-extras-other.md) |
    | `Settings -> Terminals` |  | menu: More menu (terminal) | Opens the `Terminals` settings section with the Claude and Codex profiles. | [AI console](ourplancore-ai-console.md) |

??? note "Style menu (Annotation ribbon) (8)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Highlighter` |  | menu: Style menu (Annotation ribbon) | Draws a semi-transparent highlighter mark on the sheet that is not part of the measurements. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Draw line` |  | menu: Style menu (Annotation ribbon) | Draws a simple line mark on the sheet that is not part of the measurements. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Arrow` |  | menu: Style menu (Annotation ribbon) | Draws a simple arrow mark on the sheet that is not part of the measurements. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Box` |  | menu: Style menu (Annotation ribbon) | Picks the rectangle mark tool, which is not part of the measurements. | [Snap and tracing](ourplancore-snap-trace.md) |
    | `Cloud` |  | menu: Style menu (Annotation ribbon) | Draws a cloud mark on the sheet to flag changes. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Area fill` |  | menu: Style menu (Annotation ribbon) | Draws a color-filled area mark on the sheet, not a measurement. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Hide area (white)` |  | menu: Style menu (Annotation ribbon) | Covers part of the sheet with solid white on screen and in the PDF export. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Note` |  | menu: Style menu (Annotation ribbon) | Writes a text note at the chosen spot on the sheet. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |

??? note "viewport menu: selected measurement (17)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Takeoff Properties...` |  | menu: viewport menu: selected measurement | Opens the properties of the takeoff the selected measurement belongs to. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Measurement Properties...` |  | menu: viewport menu: selected measurement | Opens the properties of the selected measurement for editing. | [Extras](ourplancore-extras.md) |
    | `Cut Out of This Area (X)` | `X` | menu: viewport menu: selected measurement |  | [Editing and snaps](ourplancore-editing.md) |
    | `Trace Walls Inside Area...` |  | menu: viewport menu: selected measurement | Traces the walls inside the selected area as linear measurements by thickness and minimum length. | [Snap and tracing](ourplancore-snap-trace.md) |
    | `Use Area As Joists...` |  | menu: viewport menu: selected measurement | Turns the selected area into a `Joist Area` joist layout. | [Measuring tools](ourplancore-tools.md) |
    | `Refresh Regular Joists in All Area Segments` |  | menu: viewport menu: selected measurement | Recalculates the regular joists in all areas of the `Joist Area` takeoff. | [Measuring tools](ourplancore-tools.md) |
    | `Start Extra Joists Mode (D)` | `D` | menu: viewport menu: selected measurement | Turns on the mode for drawing additional Extra Joists. | [Measuring tools](ourplancore-tools.md) |
    | `Delete Nearest Extra Joist` |  | menu: viewport menu: selected measurement | Deletes the Extra Joist nearest to the pointer. | [Editing and snaps](ourplancore-editing.md) |
    | `Set / Reset Joist Direction` |  | menu: viewport menu: selected measurement | Sets or resets the joist direction in the selected area. | [Measuring tools](ourplancore-tools.md) |
    | `Set Direction for All Areas` |  | menu: viewport menu: selected measurement | Sets one joist direction for all areas of the takeoff. | [Extras](ourplancore-extras.md) |
    | `Create Count Points Along ... Lines...` |  | menu: viewport menu: selected measurement | Places Count points along the selected lines at a set spacing. | [Editing and snaps](ourplancore-editing.md) |
    | `Break ... Lines Into Segments` |  | menu: viewport menu: selected measurement | Breaks the selected polylines into separate segments. | [Editing and snaps](ourplancore-editing.md) |
    | `Count Points At ... Line Ends...` |  | menu: viewport menu: selected measurement | Places Count points at the ends of the selected lines. | [Editing and snaps](ourplancore-editing.md) |
    | `Rename Measurement` |  | menu: viewport menu: selected measurement | Renames the selected measurement or its takeoff. | [Editing and snaps](ourplancore-editing.md) |
    | `Insert Vertex Here` |  | menu: viewport menu: selected measurement | Adds a vertex to the selected measurement at the click point. | [Editing and snaps](ourplancore-editing.md) |
    | `Remove Nearest Vertex` |  | menu: viewport menu: selected measurement | Deletes the measurement vertex nearest to the pointer. | [Editing and snaps](ourplancore-editing.md) |
    | `Delete Measurement` |  | menu: viewport menu: selected measurement | Deletes the selected measurement from the sheet and from the takeoff. | [Editing and snaps](ourplancore-editing.md) |

## Panel and window buttons built in code (22)

??? note "Observation Details window (6)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Go to Page` |  | panel: Observation Details window | Opens the sheet the selected entry, observation or measurement belongs to. | [AI and terminals](ourplancore-ai.md) |
    | `Open Crop` |  | panel: Observation Details window | Opens the crop image that an AI entry or observation was made from. | [AI and terminals](ourplancore-ai.md) |
    | `Request JSON` |  | panel: Observation Details window | Opens the JSON file of the AI request for this observation. | [AI and terminals](ourplancore-ai.md) |
    | `Run AI` |  | panel: Observation Details window | Sends the request of the selected entry or observation to the AI. | [AI and terminals](ourplancore-ai.md) |
    | `AI Response` |  | panel: Observation Details window | Adds an AI response to the observation by hand. | [AI and terminals](ourplancore-ai.md) |
    | `Project Context` |  | panel: Observation Details window | Opens the job context file for the AI. | [AI and terminals](ourplancore-ai.md) |

??? note "3D Massing panel (AI Inbox) (12)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Build 3D Draft` |  | panel: 3D Massing panel (AI Inbox) | Builds a `model.json` 3D model draft from the current AI markers. | [3D and managers](ourplancore-3d.md) |
    | `3D From Takeoffs` |  | panel: 3D Massing panel (AI Inbox) | Builds a 3D draft from the lines and areas of the Walls, Areas, Sqft levels. |  |
    | `AI 3D Sort` |  | panel: 3D Massing panel (AI Inbox) | Sends takeoff data to OpenAI to sort out roles and levels, then builds a 3D draft. |  |
    | `3D Window` |  | panel: 3D Massing panel (AI Inbox) | Opens a separate 3D window with rotation and saved marker points. |  |
    | `Auto Roof` |  | panel: 3D Massing panel (AI Inbox) | Queues AI roof marker candidates from the active sheet for review. | [3D roof](ourplancore-3d-roof.md) |
    | `Review Roof` |  | panel: 3D Massing panel (AI Inbox) | Checks and saves the roof type, pitch, notes and guide points. | [3D and managers](ourplancore-3d.md) |
    | `Review Openings` |  | panel: 3D Massing panel (AI Inbox) | Checks the door, window and opening markers before the 3D draft is accepted. |  |
    | `Accept 3D` |  | panel: 3D Massing panel (AI Inbox) | Marks the 3D draft as reviewed job context. | [3D and managers](ourplancore-3d.md) |
    | `Open JSON` |  | panel: 3D Massing panel (AI Inbox) | Opens the 3D draft file `AI_Context/3d_massing/model.json` in an external program. | [AI and terminals](ourplancore-ai.md) |
    | `Jump` |  | panel: 3D Massing panel (AI Inbox) | Opens the sheet the source marker is on. |  |
    | `Marker JSON` |  | panel: 3D Massing panel (AI Inbox) | Opens the JSON file of the selected source AI marker. |  |
    | `Crop` |  | panel: 3D Massing panel (AI Inbox) | Opens the crop image of the selected source AI marker. | [AI console](ourplancore-ai-console.md) |

??? note "Export PDF (preview) window (1)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Preview` |  | panel: Export PDF (preview) window | Shows the current sheet's PDF as it will be exported; updates when the PDF Output settings change. | [PDF and delivery](ourplancore-pdf.md) |

??? note "PlanSwift Import Complete window (1)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Open Report` |  | panel: PlanSwift Import Complete window | Opens the report on moving the PlanSwift job over. |  |

??? note "Bulk Properties window (1)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `More colors...` |  | panel: Bulk Properties window |  |  |

??? note "Takeoff Item Properties window (1)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `More colors...` |  | panel: Takeoff Item Properties window |  |  |

## Command palette (Ctrl+Shift+P) (138)

??? note "File (34)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Open / Import` | `Ctrl+O` | command palette: File | Opens the job picker; the button on the top bar also imports PDFs. | [Jobs and saving](job-creation-storage.md) |
    | `Open Project File` |  | command palette: File | Opens a portable `.ourplan` job file from disk. | [Jobs and saving](job-creation-storage.md) |
    | `Open Recent Job` | `Ctrl+Shift+O` | command palette: File | Opens the list of recent jobs for a quick pick. | [Jobs and saving](job-creation-storage.md) |
    | `Open Jobs Folder` |  | command palette: File | Opens a root folder that holds several jobs. | [Jobs and saving](job-creation-storage.md) |
    | `New PDF Job` |  | command palette: File | Creates a new OurPlanCore job from a folder of PDFs. | [Jobs and saving](job-creation-storage.md) |
    | `Blank Job` |  | command palette: File | Creates an empty OurPlanCore job without picking a PDF. | [Jobs and saving](job-creation-storage.md) |
    | `Create Sample Job` |  | command palette: File | Creates and opens a sample tutorial job with hints. | [Jobs and saving](job-creation-storage.md) |
    | `Import PlanSwift Job` |  | command palette: File | Converts a PlanSwift job into a new OurPlanCore job, the source stays unchanged. | [Other](ourplancore-extras-other.md) |
    | `Import PlanSwift to Current Job` |  | command palette: File | Imports a PlanSwift job into the current job, into the `01. planswift` folder. | [Other](ourplancore-extras-other.md) |
    | `Import PDF(s)` |  | command palette: File | Adds one or more PDFs to the current job. | [Jobs and saving](job-creation-storage.md) |
    | `Import PDF Folder` |  | command palette: File | Imports all PDFs from the selected folder and its subfolders into the current job. | [Jobs and saving](job-creation-storage.md) |
    | `Import PDF Takeoffs` |  | command palette: File | Brings PDF sheets over together with the PDF measurements and rulers into takeoffs. | [Other](ourplancore-extras-other.md) |
    | `Export PDF` |  | command palette: File | Exports the selected or all sheets to one PDF. | [PDF and delivery](ourplancore-pdf.md) |
    | `Save` | `Ctrl+S` | command palette: File | Saves the current job with all its measurements. | [Jobs and saving](job-creation-storage.md) |
    | `Save As` | `Ctrl+Shift+S` | command palette: File | Saves the current job to a new location in the same format. | [Jobs and saving](job-creation-storage.md) |
    | `Export CSV` |  | command palette: File | Exports the measurement rows to a CSV file. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Export TXT` |  | command palette: File | Exports the selected or all measurements to the PlanSwift text format. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Export Excel` |  | command palette: File | Exports the selected or all measurements to `.xlsx`, columns J, K, L starting at J10. | [Export to Excel](ourplancore-excel.md) |
    | `Create Project Excel Workbook` |  | command palette: File | Copy the bundled TemplateCom.xlsm into a chosen project location. | [Export to Excel](ourplancore-excel.md) |
    | `Export to Current Excel` |  | command palette: File | Writes the selected folder or takeoff into the active cell of the open Excel workbook. | [Export to Excel](ourplancore-excel.md) |
    | `Export Values to Current Excel` |  | command palette: File | Writes only the `Value` column for the same selection into the open Excel workbook. | [Export to Excel](ourplancore-excel.md) |
    | `Link to Excel` |  | command palette: File | Writes the selected takeoff's number into the active cell of the open workbook and keeps it there. | [Export to Excel](ourplancore-excel.md) |
    | `Auto Link` |  | command palette: File | DFL only: links right away the takeoffs whose numbers already sit in the `J:L` list. Cells do not change, a window shows the result. | [Export to Excel](ourplancore-excel.md) |
    | `Reset All Excel Links` |  | command palette: File | Removes all the job's links to Excel after a prompt. The values in the cells stay. | [Export to Excel](ourplancore-excel.md) |
    | `Update Excel Links` |  | command palette: File | Writes all pending link numbers, including into closed workbooks. | [Export to Excel](ourplancore-excel.md) |
    | `Excel Links...` |  | command palette: File | Shows all the job's links to Excel: go to the cell, break the link, clean the workbook. | [Export to Excel](ourplancore-excel.md) |
    | `Excel Macro: SQFT` |  | command palette: File | Adds the selected SQFT rows to the template and runs the `A2_SQFT_calc` macro. | [Export to Excel](ourplancore-excel.md) |
    | `Excel Macro: Walls` |  | command palette: File | Adds the wall rows with floor groups and runs the `A3_Walls_Calc_AllGroup` macro. | [Export to Excel](ourplancore-excel.md) |
    | `Excel Macro: Openings` |  | command palette: File | Adds openings from `Z158`, groups close windows by floor and runs `A5_Openings`. | [Export to Excel](ourplancore-excel.md) |
    | `Excel Macro: Gables` |  | command palette: File | Adds the selected Gables rows and runs the `A2_SQFT_calc` macro. | [Export to Excel](ourplancore-excel.md) |
    | `Excel Macro: Truss Heel` |  | command palette: File | Adds the selected Truss Heel rows and runs the `A2_SQFT_calc` macro. | [Export to Excel](ourplancore-excel.md) |
    | `Excel Macro: Parapet` |  | command palette: File | Adds the selected Parapet rows and runs the `A4_Parapet` macro. | [Export to Excel](ourplancore-excel.md) |
    | `Excel Macro: Eve / Rakes` |  | command palette: File | Adds the Eves and Rakes rows in descending length order and runs `A6_Eve_Rakes`. | [Export to Excel](ourplancore-excel.md) |
    | `Excel Macro: ALL` |  | command palette: File | Runs the whole configured chain of Excel macros for one selected building. | [Export to Excel](ourplancore-excel.md) |

??? note "View (14)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Fit Page` | `F` | command palette: View | Fits the whole active sheet into the viewer window. | [Measuring tools](ourplancore-tools.md) |
    | `Zoom In` | `Ctrl++` | command palette: View | Zooms the active sheet in by one zoom step. | [Keyboard shortcuts](ourplancore-shortcuts.md) |
    | `Zoom Out` | `Ctrl+-` | command palette: View | Zooms the active sheet out by one zoom step. | [Keyboard shortcuts](ourplancore-shortcuts.md) |
    | `Add Bookmark` | `B, K` | command palette: View | Saves the active sheet with the current zoom and position as a named bookmark. | [Keyboard shortcuts](ourplancore-shortcuts.md) |
    | `Hide / Show All Takeoffs` |  | command palette: View | Hides or shows all measurements on the active sheet; new measurements stay visible. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Hide Selected Takeoffs Only` | `H` | command palette: View | Hides on the sheet the whole takeoff of each selected measurement; the visibility toggle brings it back. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Toggle Dark Theme` |  | command palette: View | Switches between the light and dark interface theme. | [Getting started](ourplancore-start.md) |
    | `Page Background` |  | command palette: View | Opens the preset background colors under the sheet. | [Settings and modules](ourplancore-settings.md) |
    | `Toggle AI Inbox` |  | command palette: View | Collapses or expands the `AI Inbox` panel. | [AI and terminals](ourplancore-ai.md) |
    | `Quick Calculator` |  | command palette: View | Shows or hides the slide-out calculator that works in feet and inches. | [Other](ourplancore-extras-other.md) |
    | `Codex / Claude / DeepSeek Terminal` |  | command palette: View | Shows or hides the Codex and Claude terminals with the sheet, crop and bookmark context. | [AI console](ourplancore-ai-console.md) |
    | `Show Takeoffs Tab` |  | command palette: View | Opens the `Takeoffs` tab in the workspace side panel. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Show Estimating Tab` |  | command palette: View | Opens the `Estimating` tab in the workspace side panel. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Show 3D Tab` |  | command palette: View | Opens the 3D wall view tab in the right panel. | [3D and managers](ourplancore-3d.md) |

??? note "Workspace (7)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Show Main View` |  | command palette: Workspace | Switches to the workspace with the sheet and the measuring tools. | [Jobs and saving](job-creation-storage.md) |
    | `Show Sheet Manager` |  | command palette: Workspace | Switches to the sheet table with PDF metadata. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Show Takeoff Manager` |  | command palette: Workspace | Switches to the takeoff manager workspace. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Show Report Builder` |  | command palette: Workspace | Switches to the table-style report builder. | [Managers](ourplancore-managers.md) |
    | `Show Materials` |  | command palette: Workspace | Switches to the materials extraction workspace. | [Managers](ourplancore-managers.md) |
    | `Show AI Manager` |  | command palette: Workspace | Switches to the AI manager with incoming requests and markers. | [AI and terminals](ourplancore-ai.md) |
    | `Show 3D Viewer` |  | command palette: Workspace | Switches to the workspace with a clean 3D model view. | [3D and managers](ourplancore-3d.md) |

??? note "Tools (25)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Select Tool` | `E` | command palette: Tools | Turns on box selection and measurement editing. | [Measuring tools](ourplancore-tools.md) |
    | `Pan Tool` | `V` | command palette: Tools | Moves the sheet with the left mouse button; the right button moves it too. | [Measuring tools](ourplancore-tools.md) |
    | `Scale Tool` | `S` | command palette: Tools | Sets the sheet scale from a calibration line of known length. | [Measuring tools](ourplancore-tools.md) |
    | `Ruler Tool` | `R` | command palette: Tools | Measures a distance temporarily, without creating a measurement. | [Measuring tools](ourplancore-tools.md) |
    | `Pitch Tool` |  | command palette: Tools | Draws a slope line by two points and shows the pitch per 12. | [Measuring tools](ourplancore-tools.md) |
    | `Highlighter Tool` | `Shift+H` | command palette: Tools | Draws a semi-transparent mark on the sheet, like a highlighter. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Draw Line / Extra Joists` | `D` | command palette: Tools | Draws a markup line; with one `Joist Area` selected it turns on continuous Extra Joists. | [Measuring tools](ourplancore-tools.md) |
    | `Draw Box Tool` |  | command palette: Tools | Draws a rectangle mark on the sheet that is not part of the measurements. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Note Tool` | `N` | command palette: Tools | Writes a text note on the active sheet. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Count Tool` | `P` | command palette: Tools | Places count points into a takeoff. | [Measuring tools](ourplancore-tools.md) |
    | `Similar Count` |  | command palette: Tools | Finds similar symbols on the sheet and adds the verified points to a Count takeoff. | [Measuring tools](ourplancore-tools.md) |
    | `Points Along Line(s)` |  | command palette: Tools | Places Count points along the selected lines at a set spacing. | [Editing and snaps](ourplancore-editing.md) |
    | `Line Tool` | `L` | command palette: Tools | Records linear measurements into a takeoff. | [Measuring tools](ourplancore-tools.md) |
    | `Area Tool` | `A` | command palette: Tools | Records area measurements into a takeoff. | [Measuring tools](ourplancore-tools.md) |
    | `J Area Tool` | `J` | command palette: Tools | Creates a `Joist Area` takeoff and records areas into it. | [Measuring tools](ourplancore-tools.md) |
    | `Annotation Area` |  | command palette: Tools | Draw an annotation area takeoff: tree and legend 'annotation', no quantity. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Annotation Line` |  | command palette: Tools | Draw an annotation line takeoff: tree and legend 'annotation', no quantity. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Annotation Point` |  | command palette: Tools | Draw annotation points: tree and legend 'annotation', no quantity. |  |
    | `Beam Tool` | `B` | command palette: Tools | Measures the beam length, creates a Count takeoff and places the first point. | [Measuring tools](ourplancore-tools.md) |
    | `Openings Tool` | `O` | command palette: Tools | Measures the opening box, creates a Count takeoff named by size and places a point in the center. | [Measuring tools](ourplancore-tools.md) |
    | `Area Cut Tool` | `X` | command palette: Tools | Cuts a hole inside the selected area measurement. | [Editing and snaps](ourplancore-editing.md) |
    | `Toggle Record` | `Space` | command palette: Tools | Turns recording with the current measuring tool on or off. | [Measuring tools](ourplancore-tools.md) |
    | `Toggle Snap` | `F3` | command palette: Tools | Turns snapping to points of existing measurements on or off. | [Snap and tracing](ourplancore-snap-trace.md) |
    | `Toggle PDF Snap` | `Ctrl+F3` | command palette: Tools | Turns snapping to PDF vector corners and points on or off. | [Snap and tracing](ourplancore-snap-trace.md) |
    | `Toggle Ortho` | `F8` | command palette: Tools | Turns on `Ortho` mode, horizontal and vertical only; `Shift` turns it on temporarily. | [Snap and tracing](ourplancore-snap-trace.md) |

??? note "Edit (12)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Copy Selected Measurements` | `Ctrl+C` | command palette: Edit | Copies the selected measurements and marks to the app clipboard. | [Editing and snaps](ourplancore-editing.md) |
    | `Paste Measurements` | `Ctrl+V` | command palette: Edit | Pastes the copied measurements onto the active sheet at the pointer. | [Editing and snaps](ourplancore-editing.md) |
    | `Merge Selected Takeoffs / Measurements` | `Ctrl+M` | command palette: Edit | Merges the selected takeoffs from all sheets or moves the selected measurements into another takeoff. | [Editing and snaps](ourplancore-editing.md) |
    | `Split Selected Takeoffs / Measurements` | `Ctrl+Shift+M` | command palette: Edit | Splits takeoffs across all sheets or moves the selected measurements and points into a new takeoff. | [Editing and snaps](ourplancore-editing.md) |
    | `Break Lines Into Segments` | `Ctrl+Shift+B` | command palette: Edit | Breaks the selected polylines into separate segments; the total length does not change. | [Editing and snaps](ourplancore-editing.md) |
    | `Break Lines Into Horizontal / Vertical` | `Ctrl+Shift+V` | command palette: Edit | Sorts the segments of the selected lines into `Horizontal` and `Vertical` takeoffs. | [Editing and snaps](ourplancore-editing.md) |
    | `Count Points At Line Ends` |  | command palette: Edit | Places Count points at both ends of each selected line segment. | [Editing and snaps](ourplancore-editing.md) |
    | `Combine Areas: Union` |  | command palette: Edit | Merges the selected areas into one combined area. | [Editing and snaps](ourplancore-editing.md) |
    | `Combine Areas: Subtract` |  | command palette: Edit | Subtracts the areas selected later from the first selected one. | [Editing and snaps](ourplancore-editing.md) |
    | `Combine Areas: Intersect` |  | command palette: Edit | Keeps only the common part of all selected areas. | [Editing and snaps](ourplancore-editing.md) |
    | `Combine Areas: Remove Overlap` |  | command palette: Edit | Trims the overlaps of the selected areas so nothing is counted twice; the first area is the main one. | [Editing and snaps](ourplancore-editing.md) |
    | `Combine Areas: Divide` |  | command palette: Edit | Divides the selected areas into separate parts and a shared overlap area. | [Editing and snaps](ourplancore-editing.md) |

??? note "Pages (13)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Sort Pages A-Z` |  | command palette: Pages | Sorts the contents of the selected Pages folder or the root alphabetically. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Sort Pages Z-A` |  | command palette: Pages | Sorts the contents of the selected Pages folder or the root in reverse alphabetical order. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Sort Pages A/S` |  | command palette: Pages | Sorts A sheets into `Arch`, S sheets into `Struct`, the rest into others. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Blank Sheet` |  | command palette: Pages | Creates a blank sheet in the current job without a PDF. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Sort Pages D/Sec/WT` |  | command palette: Pages | Sorts sheets with suffixes into the details, sections, units folders and orders the Pages root. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Repair Measurement Links` |  | command palette: Pages | Reattaches measurements to sheets after pages are renamed or imported. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Auto Page Folders` |  | command palette: Pages | Creates the standard sheet folder tree in the selected Pages folder. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Auto Name PDF` |  | command palette: Pages | Shows and applies automatic sheet names from the PDF. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Auto Scale PDF` |  | command palette: Pages | Shows and applies automatic sheet scales from the PDF. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Auto Name + Scale PDF` |  | command palette: Pages | Shows and applies automatic sheet names and scales from the PDF. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Set Scale` | `F4` | command palette: Pages | Sets one scale on the selected sheets or on the active sheet. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Name / Scale Setup` | `F5` | command palette: Pages | Opens the window for setting the active sheet's name and scale by hand. | [Sheets (Pages)](ourplancore-pages.md) |
    | `AI Fill PDF Metadata` |  | command palette: Pages | Queues GPT for the sheets whose metadata was not found. | [AI and terminals](ourplancore-ai.md) |

??? note "Sheets (3)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Overlay` |  | command palette: Sheets | Picks a suitable sheet to overlay on the active one. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Batch Overlay` |  | command palette: Sheets | Matches pairs of base and overlay sheets across the whole job. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Move Overlay by Points` |  | command palette: Sheets | Aligns the active sheet's overlay by pairs of points. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |

??? note "Materials (1)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Extract Materials` |  | command palette: Materials | Extracts the materials and specifications found in the job's PDFs. | [Managers](ourplancore-managers.md) |

??? note "PDF Layers (3)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `PDF Layers All On` |  | command palette: PDF Layers | Turns on all PDF layers on the active sheet. | [Snap and tracing](ourplancore-snap-trace.md) |
    | `PDF Layers All Off` |  | command palette: PDF Layers | Turns off all PDF layers on the active sheet. | [Snap and tracing](ourplancore-snap-trace.md) |
    | `Clear PDF Layer Highlights` |  | command palette: PDF Layers | Removes the highlight from the highlighted PDF layers on the sheet. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |

??? note "Takeoffs (16)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `New Takeoff Folder` |  | command palette: Takeoffs | Creates a takeoff folder in the selected folder or in the root. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `New Takeoff Item` | `T` | command palette: Takeoffs | Creates a takeoff in the selected folder or in the root. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Refresh Takeoffs Tree` |  | command palette: Takeoffs | Rereads the Takeoffs tree from the current job folder. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Show Active Takeoff` |  | command palette: Takeoffs | Scrolls the Takeoffs tree to the active takeoff. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Active Takeoff Properties` |  | command palette: Takeoffs | Opens the properties of the active takeoff for editing. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Record Active Takeoff` | `Space` | command palette: Takeoffs | Starts or stops recording into the active takeoff. | [Measuring tools](ourplancore-tools.md) |
    | `Previous Takeoff Target` |  | command palette: Takeoffs | Makes the previous takeoff in the target list active. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Next Takeoff Target` |  | command palette: Takeoffs | Makes the next takeoff in the target list active. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Next Sheet Takeoff Target` |  | command palette: Takeoffs | Makes active the next takeoff that has measurements on the active sheet. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Sort Takeoffs A-Z` |  | command palette: Takeoffs | Sorts the contents of the selected Takeoffs folder or the root alphabetically. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Sort Takeoffs Z-A` |  | command palette: Takeoffs | Sorts the contents of the selected Takeoffs folder or the root in reverse alphabetical order. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Sort Takeoffs: Walls` |  | command palette: Takeoffs | Sorts the walls in the folder and subfolders: ext, corr, dem, then 2x6 and 2x4 sizes. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Sort Takeoffs: Template Order` |  | command palette: Takeoffs | Put Takeoffs folders in the folder template order (the Auto Create Takeoff Tree order), inside every building folder. |  |
    | `Sort Takeoffs: Details by Sheet` |  | command palette: Takeoffs | Groups `1/A501` style nodes by the sheet after the slash, in the Pages tree order. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Auto Takeoff Tree` |  | command palette: Takeoffs | Creates the standard takeoff folder tree for a new job. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Create Takeoffs From Pages` |  | command palette: Takeoffs | Creates top takeoff folders from the names of Pages sheets and folders typed in capitals. | [Takeoffs tree](ourplancore-takeoffs.md) |

??? note "AI (10)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `OpenAI Settings` |  | command palette: AI | Shows the OpenAI key status and the AI model settings. | [AI and terminals](ourplancore-ai.md) |
    | `Explain Detail (crops -> assembly diagram)` |  | command palette: AI | Crop one or more areas around a detail; the terminal assistant explains it and draws a step-by-step isometric diagram. |  |
    | `Explain Detail + Image` |  | command palette: AI | Like Explain Detail, plus a generated illustration image. |  |
    | `Add AI Observation` |  | command palette: AI | Saves a manual AI observation or marker note for the job and sheet. | [AI and terminals](ourplancore-ai.md) |
    | `Run Selected AI Request` |  | command palette: AI | Runs the selected request from `AI Inbox`. | [AI and terminals](ourplancore-ai.md) |
    | `Run New Crop Bookmarks` |  | command palette: AI | Sends only the new crop bookmarks to OpenAI. | [AI and terminals](ourplancore-ai.md) |
    | `Retry Failed Crop Bookmarks` |  | command palette: AI | Retries only the crop bookmarks whose request failed. | [AI and terminals](ourplancore-ai.md) |
    | `Create Marker Set` |  | command palette: AI | Saves the current filters of reviewed markers as a named set. | [AI and terminals](ourplancore-ai.md) |
    | `Manage Marker Sets` |  | command palette: AI | Opens the window for managing saved AI marker sets. | [AI and terminals](ourplancore-ai.md) |
    | `Export Marker Context` |  | command palette: AI | Exports the context of the visible reviewed markers to JSON. | [AI and terminals](ourplancore-ai.md) |

## Shortcut guide (F1) (91)

??? note "GLOBAL (18)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Show / close this shortcut guide` | `F1` | F1: GLOBAL | Opens or closes the app hotkeys help. | [Keyboard shortcuts](ourplancore-shortcuts.md) |
    | `Close help or cancel the active action` | `Esc` | F1: GLOBAL | Closes the help or cancels the current action, the tracing step and `Layer Trace` mode. | [Measuring tools](ourplancore-tools.md) |
    | `Open / import a job` | `Ctrl+O` | F1: GLOBAL | Opens the job picker; the button on the top bar also imports PDFs. | [Jobs and saving](job-creation-storage.md) |
    | `Open Recent Jobs` | `Ctrl+Shift+O` | F1: GLOBAL | Opens the list of recent jobs for a quick pick. | [Jobs and saving](job-creation-storage.md) |
    | `Save the current job` | `Ctrl+S` | F1: GLOBAL | Saves the current job with all its measurements. | [Jobs and saving](job-creation-storage.md) |
    | `Save the current project to a new location` | `Ctrl+Shift+S` | F1: GLOBAL | Saves the current job to a new location in the same format. | [Jobs and saving](job-creation-storage.md) |
    | `Merge selected measurement segments` | `Ctrl+M` | F1: GLOBAL | Merges the selected takeoffs from all sheets or moves the selected measurements into another takeoff. | [Editing and snaps](ourplancore-editing.md) |
    | `Split measurements / Count marks` | `Ctrl+Shift+M` | F1: GLOBAL | Splits takeoffs across all sheets or moves the selected measurements and points into a new takeoff. | [Editing and snaps](ourplancore-editing.md) |
    | `Break selected Lines into segments` | `Ctrl+Shift+B` | F1: GLOBAL | Breaks the selected polylines into separate segments; the total length does not change. | [Editing and snaps](ourplancore-editing.md) |
    | `Break selected Lines into Horizontal / Vertical takeoffs` | `Ctrl+Shift+V` | F1: GLOBAL | Sorts the segments of the selected lines into `Horizontal` and `Vertical` takeoffs. | [Editing and snaps](ourplancore-editing.md) |
    | `Open Command Palette` | `Ctrl+Shift+P` | F1: GLOBAL | Opens the command palette with a search across all app functions. | [Keyboard shortcuts](ourplancore-shortcuts.md) |
    | `Start / stop Record` | `Space` | F1: GLOBAL | Turns recording with the current measuring tool on or off. | [Measuring tools](ourplancore-tools.md) |
    | `Create a new takeoff item` | `T` | F1: GLOBAL | Creates a new takeoff in the selected tree folder. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Hide selected takeoffs only` | `H` | F1: GLOBAL | Hides on the sheet the whole takeoff of each selected measurement; the visibility toggle brings it back. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Add a bookmark` | `B, K` | F1: GLOBAL | Saves the active sheet with the current zoom and position as a named bookmark. | [Keyboard shortcuts](ourplancore-shortcuts.md) |
    | `Set scale on selected sheet(s)` | `F4` | F1: GLOBAL | Sets one scale on the selected sheets or on the active sheet. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Open Name / Scale` | `F5` | F1: GLOBAL | Opens the window for setting the active sheet's name and scale by hand. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Collapse Pages and Takeoffs trees` | `-` | F1: GLOBAL | Collapses all folders in the Pages and Takeoffs trees. | [Keyboard shortcuts](ourplancore-shortcuts.md) |

??? note "DRAWING TOOLS (14)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Pan` | `V` | F1: DRAWING TOOLS | Moves the sheet with the left mouse button; the right button moves it too. | [Measuring tools](ourplancore-tools.md) |
    | `Select` | `E` | F1: DRAWING TOOLS | Turns on box selection and measurement editing. | [Measuring tools](ourplancore-tools.md) |
    | `Scale` | `S` | F1: DRAWING TOOLS | Sets the sheet scale from a calibration line of known length. | [Measuring tools](ourplancore-tools.md) |
    | `Ruler` | `R` | F1: DRAWING TOOLS | Measures a distance temporarily, without creating a measurement. | [Measuring tools](ourplancore-tools.md) |
    | `Highlighter` | `Shift+H` | F1: DRAWING TOOLS | Draws a semi-transparent mark on the sheet, like a highlighter. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Draw Line / Extra Joists` | `D` | F1: DRAWING TOOLS | Draws a markup line; with one `Joist Area` selected it turns on continuous Extra Joists. | [Measuring tools](ourplancore-tools.md) |
    | `Beam` | `B` | F1: DRAWING TOOLS | Measures the beam length, creates a Count takeoff and places the first point. | [Measuring tools](ourplancore-tools.md) |
    | `Openings` | `O` | F1: DRAWING TOOLS | Measures the opening box, creates a Count takeoff named by size and places a point in the center. | [Measuring tools](ourplancore-tools.md) |
    | `Note` | `N` | F1: DRAWING TOOLS | Writes a text note on the active sheet. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Count` | `P` | F1: DRAWING TOOLS | Places count points into a takeoff. | [Measuring tools](ourplancore-tools.md) |
    | `Line` | `L` | F1: DRAWING TOOLS | Records linear measurements into a takeoff. | [Measuring tools](ourplancore-tools.md) |
    | `Area` | `A` | F1: DRAWING TOOLS | Records area measurements into a takeoff. | [Measuring tools](ourplancore-tools.md) |
    | `Joist Area` | `J` | F1: DRAWING TOOLS | Creates a `Joist Area` takeoff and records areas into it. | [Measuring tools](ourplancore-tools.md) |
    | `Area Cut` | `X` | F1: DRAWING TOOLS | Cuts a hole inside the selected area measurement. | [Editing and snaps](ourplancore-editing.md) |

??? note "VIEWPORT & DRAWING (15)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Complete the current drawing` | `C` | F1: VIEWPORT & DRAWING | Finishes the measurement or mark being drawn, like a double click. | [Keyboard shortcuts](ourplancore-shortcuts.md) |
    | `Fit sheet to viewport` | `F` | F1: VIEWPORT & DRAWING | Fits the whole active sheet into the viewer window. | [Measuring tools](ourplancore-tools.md) |
    | `Rename the selected object's takeoff` | `F2` | F1: VIEWPORT & DRAWING | Renames the takeoff that the object selected on the sheet belongs to. | [Editing and snaps](ourplancore-editing.md) |
    | `Toggle takeoff-point Snap` | `F3` | F1: VIEWPORT & DRAWING | Turns snapping to points of existing measurements on or off. | [Snap and tracing](ourplancore-snap-trace.md) |
    | `Toggle PDF vector Snap` | `Ctrl+F3` | F1: VIEWPORT & DRAWING | Turns snapping to PDF vector corners and points on or off. | [Snap and tracing](ourplancore-snap-trace.md) |
    | `Toggle Ortho` | `F8` | F1: VIEWPORT & DRAWING | Turns on `Ortho` mode, horizontal and vertical only; `Shift` turns it on temporarily. | [Snap and tracing](ourplancore-snap-trace.md) |
    | `Temporarily force Ortho` | `Shift` | F1: VIEWPORT & DRAWING | Turns on `Ortho` mode while the key is held during drawing or editing. | [Snap and tracing](ourplancore-snap-trace.md) |
    | `Toggle Box mode` | `F9` | F1: VIEWPORT & DRAWING | Turns on `Box` mode: line, area and cutout are drawn as a rectangle by two corners. | [Snap and tracing](ourplancore-snap-trace.md) |
    | `Zoom in` | `Ctrl++` | F1: VIEWPORT & DRAWING | Zooms the active sheet in by one zoom step. | [Keyboard shortcuts](ourplancore-shortcuts.md) |
    | `Zoom out` | `Ctrl+-` | F1: VIEWPORT & DRAWING | Zooms the active sheet out by one zoom step. | [Keyboard shortcuts](ourplancore-shortcuts.md) |
    | `Undo viewport action / last point` | `Ctrl+Z / Backspace` | F1: VIEWPORT & DRAWING | Undoes the last action on the sheet or the last point placed. | [Editing and snaps](ourplancore-editing.md) |
    | `Select all objects on active sheet` | `Ctrl+A` | F1: VIEWPORT & DRAWING | Selects all objects on the active sheet. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Copy selected measurements / markups` | `Ctrl+C` | F1: VIEWPORT & DRAWING | Copies the selected measurements and marks to the app clipboard. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Paste at the pointer` | `Ctrl+V` | F1: VIEWPORT & DRAWING | Pastes the copied measurements onto the active sheet at the pointer. | [Editing and snaps](ourplancore-editing.md) |
    | `Delete the selected object` | `Delete` | F1: VIEWPORT & DRAWING | Deletes the measurement or mark selected on the sheet. | [Editing and snaps](ourplancore-editing.md) |

??? note "SELECTION MODIFIERS (3)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Add to / toggle selection` | `Ctrl` | F1: SELECTION MODIFIERS | Adds an object to the selection or removes it with a click while the key is held. | [3D roof](ourplancore-3d-roof.md) |
    | `Remove from selection` | `Ctrl+Shift` | F1: SELECTION MODIFIERS | Removes objects from the selection with a click or a box while the keys are held. | [Keyboard shortcuts](ourplancore-shortcuts.md) |
    | `Select vertices / handles` | `Alt` | F1: SELECTION MODIFIERS | Selects measurement vertices and handles with a click or a box while the key is held. | [Keyboard shortcuts](ourplancore-shortcuts.md) |

??? note "PAGES TREE (10)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Clear the Pages selection` | `Esc` | F1: PAGES TREE | Clears the selection of all rows in the Pages tree. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Copy / cut / paste` | `Ctrl+C / X / V` | F1: PAGES TREE | Copies, cuts and pastes the selected rows in the Pages or Takeoffs tree. | [Editing and snaps](ourplancore-editing.md) |
    | `Duplicate with the exact name` | `Ctrl+D` | F1: PAGES TREE | Makes a copy of the selected Pages sheet or folder with the same name. | [Editing and snaps](ourplancore-editing.md) |
    | `Move page, folder, or legend row` | `Ctrl+Up / Down` | F1: PAGES TREE | Moves the selected sheet, folder or legend row up or down. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Restore the last Pages deletion` | `Ctrl+Z` | F1: PAGES TREE | Brings back the last deletion in the Pages tree. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Rename page or folder` | `F2` | F1: PAGES TREE | Renames the selected sheet or folder in the Pages tree. | [Editing and snaps](ourplancore-editing.md) |
    | `Delete selected page(s) / folder(s)` | `Delete` | F1: PAGES TREE | Deletes the selected sheets or folders from the Pages tree. | [Editing and snaps](ourplancore-editing.md) |
    | `Select a range` | `Shift+click` | F1: PAGES TREE | Selects a range of rows from the previous selection with a `Shift` click. |  |
    | `Toggle one row` | `Ctrl+click` | F1: PAGES TREE | Adds one row to the selection or removes it with a `Ctrl` click. |  |
    | `Add a range` | `Ctrl+Shift+click` | F1: PAGES TREE | Adds a range of rows to the ones already selected with a `Ctrl+Shift` click. |  |

??? note "TAKEOFFS TREE (9)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Copy / cut / paste` | `Ctrl+C / X / V` | F1: TAKEOFFS TREE | Copies, cuts and pastes the selected rows in the Pages or Takeoffs tree. | [Editing and snaps](ourplancore-editing.md) |
    | `Duplicate with the exact name` | `Ctrl+D` | F1: TAKEOFFS TREE | Makes a copy of the selected Takeoffs takeoff or folder with the same name. | [Editing and snaps](ourplancore-editing.md) |
    | `Move item, folder, or section` | `Ctrl+Up / Down` | F1: TAKEOFFS TREE | Moves the selected takeoff, folder or section up or down in the tree. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Select section measurements on canvas` | `Ctrl+Enter` | F1: TAKEOFFS TREE | Selects on the sheet the measurements of the selected Takeoffs tree sections. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Restore the last takeoff-tree deletion` | `Ctrl+Z` | F1: TAKEOFFS TREE | Brings back the last deletion in the Takeoffs tree. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Rename item, folder, or section` | `F2` | F1: TAKEOFFS TREE | Renames the selected takeoff, folder or section in the Takeoffs tree. | [Editing and snaps](ourplancore-editing.md) |
    | `Delete selected node(s)` | `Delete` | F1: TAKEOFFS TREE | Deletes the selected nodes from the Takeoffs tree. | [Editing and snaps](ourplancore-editing.md) |
    | `Range / toggle selection` | `Shift / Ctrl+click` | F1: TAKEOFFS TREE | Selects a range with a `Shift` click, adds or removes a row with a `Ctrl` click. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Start marquee selection from a row` | `Alt+drag` | F1: TAKEOFFS TREE | Starts a box selection in the tree by dragging from a row with `Alt`. | [Takeoffs tree](ourplancore-takeoffs.md) |

??? note "BOOKMARKS & AI INBOX (2)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Open the selected bookmark / AI entry` | `Enter` | F1: BOOKMARKS & AI INBOX | Opens the selected bookmark or `AI Inbox` entry on its sheet. | [Keyboard shortcuts](ourplancore-shortcuts.md) |
    | `Delete the selected bookmark` | `Delete` | F1: BOOKMARKS & AI INBOX | Deletes the selected bookmark from the bookmark list. | [Other](ourplancore-extras-other.md) |

??? note "SHEET OVERLAY (6)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Move the overlay` | `Ctrl+Alt+drag` | F1: SHEET OVERLAY | Moves the overlaid sheet by dragging with `Ctrl+Alt`. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Nudge the overlay` | `Ctrl+Alt+Arrows` | F1: SHEET OVERLAY | Shifts the overlaid sheet by a small step with the arrows and `Ctrl+Alt`. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Scale the overlay` | `Ctrl+Alt++ / -` | F1: SHEET OVERLAY | Enlarges or shrinks the overlaid sheet with the plus and minus keys and `Ctrl+Alt`. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Rotate the overlay` | `Ctrl+Alt+[ / ]` | F1: SHEET OVERLAY | Rotates the overlaid sheet with the square brackets and `Ctrl+Alt`. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Reset overlay transform` | `Ctrl+Alt+0` | F1: SHEET OVERLAY | Resets the shift, scale and rotation of the overlaid sheet. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Use fine movement / scale / rotation` | `+ Shift` | F1: SHEET OVERLAY | Makes the overlay shift, scale and rotation finer when `Shift` is added. |  |

??? note "3D ROOF GUIDE MODE (8)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Ridge guide` | `R` | F1: 3D ROOF GUIDE MODE | Draws a ridge line (`Ridge`) in 3D roof guide mode. | [3D roof](ourplancore-3d-roof.md) |
    | `Hip guide` | `H` | F1: 3D ROOF GUIDE MODE | Draws a hip line (`Hip`) in 3D roof guide mode. | [3D roof](ourplancore-3d-roof.md) |
    | `Valley guide` | `V` | F1: 3D ROOF GUIDE MODE | Draws a valley line (`Valley`) in 3D roof guide mode. | [3D roof](ourplancore-3d-roof.md) |
    | `Eave guide` | `E` | F1: 3D ROOF GUIDE MODE | Draws an eave line (`Eave`) in 3D roof guide mode. | [3D roof](ourplancore-3d-roof.md) |
    | `Rake guide` | `K` | F1: 3D ROOF GUIDE MODE | Draws a rake line (`Rake`) in 3D roof guide mode. | [3D roof](ourplancore-3d-roof.md) |
    | `Pitch guide` | `P` | F1: 3D ROOF GUIDE MODE | Draws a roof pitch guide (`Pitch`) in 3D roof guide mode. | [3D roof](ourplancore-3d-roof.md) |
    | `Remove the last guide point` | `Backspace / Ctrl+Z` | F1: 3D ROOF GUIDE MODE | Removes the last placed point of a 3D roof guide. | [Editing and snaps](ourplancore-editing.md) |
    | `Cancel guide / leave Roof mode` | `Esc` | F1: 3D ROOF GUIDE MODE | Cancels the current guide or exits 3D roof mode. | [3D roof](ourplancore-3d-roof.md) |

??? note "LAYER TRACE (3)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Cycle edge snap or trace mode / candidate` | `Tab` | F1: LAYER TRACE | Cycles the edge snap, the tracing mode or the candidate in `Layer Trace`. | [Snap and tracing](ourplancore-snap-trace.md) |
    | `Advance the trace workflow` | `Enter` | F1: LAYER TRACE | Moves to the next tracing step in `Layer Trace` mode. | [Snap and tracing](ourplancore-snap-trace.md) |
    | `Cancel trace step / leave Layer Trace` | `Esc` | F1: LAYER TRACE | Closes the help or cancels the current action, the tracing step and `Layer Trace` mode. | [Measuring tools](ourplancore-tools.md) |

??? note "DIALOGS & LISTS (3)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Accept / open the selected result` | `Enter` | F1: DIALOGS & LISTS | Accepts or opens the selected result in a window or list. |  |
    | `Close the active dialog` | `Esc` | F1: DIALOGS & LISTS | Closes the active window or dialog without applying. |  |
    | `Navigate palette / picker results` | `Up / Down` | F1: DIALOGS & LISTS | Moves the selection through palette and list results with the up and down arrows. |  |

## Default keys that are not in the palette (61)

??? note "Workspace (3)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Show / close the shortcut guide` | `F1` | key: Workspace | Opens or closes the app hotkeys help. | [Keyboard shortcuts](ourplancore-shortcuts.md) |
    | `Open Command Palette` | `Ctrl+Shift+P` | key: Workspace | Opens the command palette with a search across all app functions. | [Jobs and saving](job-creation-storage.md) |
    | `Collapse Pages and Takeoffs trees` | `-` | key: Workspace | Collapses all folders in the Pages and Takeoffs trees. | [Keyboard shortcuts](ourplancore-shortcuts.md) |

??? note "Viewport (9)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Toggle Box mode` | `F9` | key: Viewport | Turns on `Box` mode: line, area and cutout are drawn as a rectangle by two corners. | [Snap and tracing](ourplancore-snap-trace.md) |
    | `Undo viewport action / last point` | `Ctrl+Z / Backspace` | key: Viewport | Undoes the last action on the sheet or the last point placed. | [Editing and snaps](ourplancore-editing.md) |
    | `Select all objects on active sheet` | `Ctrl+A` | key: Viewport | Selects all objects on the active sheet. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Delete the selected object` | `Delete` | key: Viewport | Deletes the measurement or mark selected on the sheet. | [Editing and snaps](ourplancore-editing.md) |
    | `Rename the selected object's takeoff` | `F2` | key: Viewport | Renames the takeoff that the object selected on the sheet belongs to. | [Editing and snaps](ourplancore-editing.md) |
    | `Complete the current drawing` | `C` | key: Viewport | Finishes the measurement or mark being drawn, like a double click. | [Keyboard shortcuts](ourplancore-shortcuts.md) |
    | `Cancel the active action` | `Esc` | key: Viewport | Closes the help or cancels the current action, the tracing step and `Layer Trace` mode. | [Measuring tools](ourplancore-tools.md) |
    | `Cycle edge snap or trace mode / candidate` | `Tab` | key: Viewport | Cycles the edge snap, the tracing mode or the candidate in `Layer Trace`. | [Snap and tracing](ourplancore-snap-trace.md) |
    | `Advance the trace workflow` | `Enter` | key: Viewport | Moves to the next tracing step in `Layer Trace` mode. | [Snap and tracing](ourplancore-snap-trace.md) |

??? note "Pages (10)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Pages tree: copy` | `Ctrl+C` | key: Pages | Copies the selected sheets or folders of the Pages tree to the clipboard. | [Editing and snaps](ourplancore-editing.md) |
    | `Pages tree: cut` | `Ctrl+X` | key: Pages | Cuts the selected sheets or folders of the Pages tree for moving. | [Editing and snaps](ourplancore-editing.md) |
    | `Pages tree: paste` | `Ctrl+V` | key: Pages | Pastes the copied or cut sheets into the selected Pages folder. | [Editing and snaps](ourplancore-editing.md) |
    | `Pages tree: duplicate with the exact name` | `Ctrl+D` | key: Pages | Makes a copy of the selected Pages sheet or folder with the same name. | [Editing and snaps](ourplancore-editing.md) |
    | `Pages tree: move up` | `Ctrl+Up` | key: Pages | Moves the selected sheet or folder one row up in the Pages tree. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Pages tree: move down` | `Ctrl+Down` | key: Pages | Moves the selected sheet or folder one row down in the Pages tree. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Pages tree: restore the last deletion` | `Ctrl+Z` | key: Pages | Brings back the last deletion in the Pages tree. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Pages tree: rename page or folder` | `F2` | key: Pages | Renames the selected sheet or folder in the Pages tree. | [Editing and snaps](ourplancore-editing.md) |
    | `Pages tree: delete selected` | `Delete` | key: Pages | Deletes the selected sheets or folders from the Pages tree. | [Editing and snaps](ourplancore-editing.md) |
    | `Pages tree: clear the selection` | `Esc` | key: Pages | Clears the selection of all rows in the Pages tree. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |

??? note "Takeoffs (10)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Takeoffs tree: copy` | `Ctrl+C` | key: Takeoffs | Copies the selected takeoffs or folders of the Takeoffs tree to the clipboard. | [Editing and snaps](ourplancore-editing.md) |
    | `Takeoffs tree: cut` | `Ctrl+X` | key: Takeoffs | Cuts the selected takeoffs or folders of the Takeoffs tree for moving. | [Editing and snaps](ourplancore-editing.md) |
    | `Takeoffs tree: paste` | `Ctrl+V` | key: Takeoffs | Pastes the copied or cut takeoffs into the selected Takeoffs folder. | [Editing and snaps](ourplancore-editing.md) |
    | `Takeoffs tree: duplicate with the exact name` | `Ctrl+D` | key: Takeoffs | Makes a copy of the selected Takeoffs takeoff or folder with the same name. | [Editing and snaps](ourplancore-editing.md) |
    | `Takeoffs tree: move up` | `Ctrl+Up` | key: Takeoffs | Moves the selected takeoff, folder or section one row up in the Takeoffs tree. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Takeoffs tree: move down` | `Ctrl+Down` | key: Takeoffs | Moves the selected takeoff, folder or section one row down in the Takeoffs tree. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Takeoffs tree: restore the last deletion` | `Ctrl+Z` | key: Takeoffs | Brings back the last deletion in the Takeoffs tree. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Takeoffs tree: rename item, folder, or section` | `F2` | key: Takeoffs | Renames the selected takeoff, folder or section in the Takeoffs tree. | [Editing and snaps](ourplancore-editing.md) |
    | `Takeoffs tree: delete selected node(s)` | `Delete` | key: Takeoffs | Deletes the selected nodes from the Takeoffs tree. | [Editing and snaps](ourplancore-editing.md) |
    | `Select section measurements on canvas` | `Ctrl+Enter` | key: Takeoffs | Selects on the sheet the measurements of the selected Takeoffs tree sections. | [Takeoffs tree](ourplancore-takeoffs.md) |

??? note "Bookmarks (2)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Open the selected bookmark` | `Enter` | key: Bookmarks | Opens the selected bookmark on its sheet at the saved zoom. | [Keyboard shortcuts](ourplancore-shortcuts.md) |
    | `Delete the selected bookmark` | `Delete` | key: Bookmarks | Deletes the selected bookmark from the bookmark list. | [Other](ourplancore-extras-other.md) |

??? note "Inbox (1)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Open the selected AI entry` | `Enter` | key: Inbox | Opens the selected `AI Inbox` entry on its sheet. | [Keyboard shortcuts](ourplancore-shortcuts.md) |

??? note "Roof (8)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Ridge guide` | `R` | key: Roof | Draws a ridge line (`Ridge`) in 3D roof guide mode. | [3D roof](ourplancore-3d-roof.md) |
    | `Hip guide` | `H` | key: Roof | Draws a hip line (`Hip`) in 3D roof guide mode. | [3D roof](ourplancore-3d-roof.md) |
    | `Valley guide` | `V` | key: Roof | Draws a valley line (`Valley`) in 3D roof guide mode. | [3D roof](ourplancore-3d-roof.md) |
    | `Eave guide` | `E` | key: Roof | Draws an eave line (`Eave`) in 3D roof guide mode. | [3D roof](ourplancore-3d-roof.md) |
    | `Rake guide` | `K` | key: Roof | Draws a rake line (`Rake`) in 3D roof guide mode. | [3D roof](ourplancore-3d-roof.md) |
    | `Pitch guide` | `P` | key: Roof | Draws a roof pitch guide (`Pitch`) in 3D roof guide mode. | [3D roof](ourplancore-3d-roof.md) |
    | `Cancel guide / leave Roof mode` | `Esc` | key: Roof | Cancels the current guide or exits 3D roof mode. | [3D roof](ourplancore-3d-roof.md) |
    | `Remove the last guide point` | `Backspace / Ctrl+Z` | key: Roof | Removes the last placed point of a 3D roof guide. | [Editing and snaps](ourplancore-editing.md) |

??? note "Overlay (18)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Nudge the overlay left` | `Ctrl+Alt+Left` | key: Overlay | Shifts the overlaid sheet left by a small step. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Nudge the overlay right` | `Ctrl+Alt+Right` | key: Overlay | Shifts the overlaid sheet right by a small step. | [Keyboard shortcuts](ourplancore-shortcuts.md) |
    | `Nudge the overlay up` | `Ctrl+Alt+Up` | key: Overlay | Shifts the overlaid sheet up by a small step. | [Keyboard shortcuts](ourplancore-shortcuts.md) |
    | `Nudge the overlay down` | `Ctrl+Alt+Down` | key: Overlay | Shifts the overlaid sheet down by a small step. | [Keyboard shortcuts](ourplancore-shortcuts.md) |
    | `Scale the overlay up` | `Ctrl+Alt++` | key: Overlay | Scales the overlaid sheet up slightly by one step. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Scale the overlay down` | `Ctrl+Alt+-` | key: Overlay | Scales the overlaid sheet down slightly by one step. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Rotate the overlay left` | `Ctrl+Alt+[` | key: Overlay | Rotates the overlaid sheet left by a small angle. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Rotate the overlay right` | `Ctrl+Alt+]` | key: Overlay | Rotates the overlaid sheet right by a small angle. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Reset overlay transform` | `Ctrl+Alt+0` | key: Overlay | Resets the shift, scale and rotation of the overlaid sheet. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Fine nudge the overlay left` | `Ctrl+Alt+Shift+Left` | key: Overlay | Shifts the overlaid sheet left by the finest step. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Fine nudge the overlay right` | `Ctrl+Alt+Shift+Right` | key: Overlay | Shifts the overlaid sheet right by the finest step. | [Keyboard shortcuts](ourplancore-shortcuts.md) |
    | `Fine nudge the overlay up` | `Ctrl+Alt+Shift+Up` | key: Overlay | Shifts the overlaid sheet up by the finest step. | [Keyboard shortcuts](ourplancore-shortcuts.md) |
    | `Fine nudge the overlay down` | `Ctrl+Alt+Shift+Down` | key: Overlay | Shifts the overlaid sheet down by the finest step. | [Keyboard shortcuts](ourplancore-shortcuts.md) |
    | `Fine scale the overlay up` | `Ctrl+Alt+Shift++` | key: Overlay | Scales the overlaid sheet up by the finest step. | [Keyboard shortcuts](ourplancore-shortcuts.md) |
    | `Fine scale the overlay down` | `Ctrl+Alt+Shift+-` | key: Overlay | Scales the overlaid sheet down by the finest step. | [Keyboard shortcuts](ourplancore-shortcuts.md) |
    | `Fine rotate the overlay left` | `Ctrl+Alt+Shift+[` | key: Overlay | Rotates the overlaid sheet left by the finest angle. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Fine rotate the overlay right` | `Ctrl+Alt+Shift+]` | key: Overlay | Rotates the overlaid sheet right by the finest angle. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Reset overlay transform (fine)` | `Ctrl+Alt+Shift+0` | key: Overlay | Resets the shift, scale and rotation of the overlaid sheet, the `Shift` key variant. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |

## Settings: categories and sections (45)

??? note "Settings > Agent Bridge (1)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Agent Bridge` |  | Settings: Settings > Agent Bridge | Sets up local assistant access to the open job. | [Settings and modules](ourplancore-settings.md) |

??? note "Settings > AI Crop Notes (1)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `AI Crop Notes` |  | Settings: Settings > AI Crop Notes | Sets the format of the Tag and Size rows in notes from an AI table crop. | [AI and terminals](ourplancore-ai.md) |

??? note "Settings > Appearance (1)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Appearance` |  | Settings: Settings > Appearance | Section of the settings panel. |  |

??? note "Settings > Autocomplete (2)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Autocomplete` |  | Settings: Settings > Autocomplete | Section of the settings panel. |  |
    | `Try it` |  | Settings: Settings > Autocomplete | Section of the settings panel. |  |

??? note "Settings > Autosave Recovery (1)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Autosave Recovery` |  | Settings: Settings > Autosave Recovery | Sets the autosave retry intervals after an error, globally or per job. | [Settings and modules](ourplancore-settings.md) |

??? note "Settings > ? (7)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Beam annotation line` |  | Settings: Settings > ? | Adds a markup line with a color and dimension offset to each new Beam. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Viewport interaction` |  | Settings: Settings > ? | Sets the mouse wheel zoom step in the sheet window. | [Settings and modules](ourplancore-settings.md) |
    | `Background performance` |  | Settings: Settings > ? | Turns on background warm-up of the job's sheets and cleanup of unused raster cache. | [Settings and modules](ourplancore-settings.md) |
    | `Tree display` |  | Settings: Settings > ? | Shows the section and point rows under takeoffs in the Takeoffs tree. | [Settings and modules](ourplancore-settings.md) |
    | `Display & export defaults` |  | Settings: Settings > ? | Opens the Viewport, Display and PDF Output ribbons with the default settings. | [Settings and modules](ourplancore-settings.md) |
    | `Measurement editing` |  | Settings: Settings > ? | Section of the settings panel. |  |
    | `Sheet Manager raster DPI presets` |  | Settings: Settings > ? | Sets the values of the DPI buttons in Sheet Manager, from 72 to 400. | [Settings and modules](ourplancore-settings.md) |

??? note "Settings > Blank Sheets (1)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Blank Sheets` |  | Settings: Settings > Blank Sheets | Sets the default blank sheet size and the paper presets. | [Settings and modules](ourplancore-settings.md) |

??? note "Settings > Excel Actions (4)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Excel macro actions` |  | Settings: Settings > Excel Actions | Lists the XL strip buttons and the sequence of steps for `ALL`. | [Export to Excel](ourplancore-excel.md) |
    | `Floor folder matching` |  | Settings: Settings > Excel Actions | Sets the words that make a folder count as a floor, for example `1, 1st, first`. | [Export to Excel](ourplancore-excel.md) |
    | `Framing folders -> Excel blocks` |  | Settings: Settings > Excel Actions | Maps the framing folders in the tree to row blocks in the Excel workbook. | [Export to Excel](ourplancore-excel.md) |
    | `Walls extras: sheathing, shear walls, shaft, units, balconies` |  | Settings: Settings > Excel Actions | Sets up the Excel export of sheathing, shear walls, shaft walls, units and balconies. | [Export to Excel](ourplancore-excel.md) |

??? note "Settings > Excel Links (2)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Link to Excel behaviour` |  | Settings: Settings > Excel Links | Sets how the link writes to an open and a closed workbook, workbook copies, pauses. | [Export to Excel](ourplancore-excel.md) |
    | `Auto Link` |  | Settings: Settings > Excel Links | Sets the threshold of small whole numbers that need a name to be linked. | [Export to Excel](ourplancore-excel.md) |

??? note "Settings > Excel Rules (1)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Excel Rules: clean-up after ALL` |  | Settings: Settings > Excel Rules | Section of the settings panel. |  |

??? note "Settings > Sheet Legend (2)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `PDF legend placement` |  | Settings: Settings > Sheet Legend | Section of the settings panel. |  |
    | `Sheet Legend` |  | Settings: Settings > Sheet Legend | Sets the names and order of the automatic legend blocks by Takeoffs folder, globally or per job. | [Settings and modules](ourplancore-settings.md) |

??? note "Settings > PDF Editable Export (1)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `PDF editable export (Adobe)` |  | Settings: Settings > PDF Editable Export | Sets which measurements sit in the PDF as objects for editing in Adobe Acrobat. | [Settings and modules](ourplancore-settings.md) |

??? note "Settings > Project Storage (6)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Project format` |  | Settings: Settings > Project Storage | Shows the storage format of the open job; new jobs are always a single `.ourplan` file. | [Settings and modules](ourplancore-settings.md) |
    | `Current project` |  | Settings: Settings > Project Storage | Shows the path and total size of the open job. | [Settings and modules](ourplancore-settings.md) |
    | `Storage breakdown` |  | Settings: Settings > Project Storage | Shows how much space each part of the job takes. | [Settings and modules](ourplancore-settings.md) |
    | `Safe compact preview` |  | Settings: Settings > Project Storage | Shows what can be safely compacted in the job before compacting. | [Settings and modules](ourplancore-settings.md) |
    | `Review-only findings` |  | Settings: Settings > Project Storage | Lists job size findings that need a manual check. | [Settings and modules](ourplancore-settings.md) |
    | `Details` |  | Settings: Settings > Project Storage | Shows the detailed job storage analysis report. | [Settings and modules](ourplancore-settings.md) |

??? note "Settings > Auto Rename / Scale (4)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Deterministic Auto Name / Scale policy` |  | Settings: Settings > Auto Rename / Scale | Picks the naming and scale engine preset and tests the rules on the selected sheets. | [Settings and modules](ourplancore-settings.md) |
    | `Evidence, confidence, and preservation` |  | Settings: Settings > Auto Rename / Scale | Sets the evidence sources, confidence thresholds and protection of already reviewed names and scales. | [Settings and modules](ourplancore-settings.md) |
    | `Suffix generation rules (first enabled match wins)` |  | Settings: Settings > Auto Rename / Scale | Lists the sheet suffix rules; the first enabled matching row wins. | [Settings and modules](ourplancore-settings.md) |
    | `Learned rules (lower-priority evidence)` |  | Settings: Settings > Auto Rename / Scale | Stores learned sheet naming rules, globally or per job, at the lowest priority. | [Settings and modules](ourplancore-settings.md) |

??? note "Settings > Sheet Takeoff Routing (4)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Sheet Takeoff Routing` |  | Settings: Settings > Sheet Takeoff Routing | Sets the levels, the W, F, S, U dots and the folders where a new measurement goes. | [Settings and modules](ourplancore-settings.md) |
    | `Levels` |  | Settings: Settings > Sheet Takeoff Routing | Lists the levels: dot label, floor folders for walls, framing, shear and name tags. | [Routing and rules](ourplancore-routing.md) |
    | `Rows` |  | Settings: Settings > Sheet Takeoff Routing | Lists the routing dot rows; the U row sends all floors into units with one dot. | [Settings and modules](ourplancore-settings.md) |
    | `Tool destinations` |  | Settings: Settings > Sheet Takeoff Routing | Sets the destination folder for the measurements of each tool. | [Routing and rules](ourplancore-routing.md) |

??? note "Settings > Takeoff Colors (1)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Takeoff Colors` |  | Settings: Settings > Takeoff Colors | Sets a fixed color for takeoffs with an exact name, for example `bft`. | [Settings and modules](ourplancore-settings.md) |

??? note "Settings > Takeoff Name Routing (1)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Takeoff Name Routing` |  | Settings: Settings > Takeoff Name Routing | Sets the rules by which the name or tool sends a measurement into its folder. | [Settings and modules](ourplancore-settings.md) |

??? note "Settings > Terminals (1)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Terminals` |  | Settings: Settings > Terminals | Sets up the Claude and Codex terminals: profile, width, effort and context. | [AI console](ourplancore-ai-console.md) |

??? note "Settings > Voice Input (1)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Voice Input` |  | Settings: Settings > Voice Input | Section of the settings panel. | [Settings and modules](ourplancore-settings.md) |

??? note "Settings > Workspace (3)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Workspace` |  | Settings: Settings > Workspace | Sets up the server, device, sync and work from a second computer. | [Settings and modules](ourplancore-settings.md) |
    | `Connect another computer` |  | Settings: Settings > Workspace | Connects a second computer to the workspace with a one-time code. | [Workspace, Job Tracker, CLI](ourplancore-workspace.md) |
    | `Projects` |  | Settings: Settings > Workspace | Lists shared jobs: share the current one, open, resolve conflicts, apply shared presets. | [Settings and modules](ourplancore-settings.md) |

## Windows and dialogs (47)

??? note "Job Is Already Open window (3)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Open Read-Only` |  | window: Job Is Already Open window | Opens the job read-only, with no saving and no changes. | [Jobs and saving](job-creation-storage.md) |
    | `Retry` |  | window: Job Is Already Open window | Checks again whether the job is held by another window or computer. | [AI and terminals](ourplancore-ai.md) |
    | `Take Over` |  | window: Job Is Already Open window | Takes the job over from another window after an extra confirmation. | [Jobs and saving](job-creation-storage.md) |

??? note "Open Project window (5)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `+ Add folder` |  | window: Open Project window | Adds a folder holding OurPlanCore jobs to the list. | [Jobs and saving](job-creation-storage.md) |
    | `Remove folder` |  | window: Open Project window | Removes the selected folder from the list; the files on disk stay. | [Jobs and saving](job-creation-storage.md) |
    | `Open` |  | window: Open Project window | Opens the job selected in the list in the main window. | [Jobs and saving](job-creation-storage.md) |
    | `PDF project` |  | window: Open Project window | Creates a new job from PDF files. | [Jobs and saving](job-creation-storage.md) |
    | `Blank project` |  | window: Open Project window | Creates an empty job with no PDF sheets. | [Jobs and saving](job-creation-storage.md) |

??? note "window (28)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Create Line Grid` |  | window: window | Builds a grid of lines inside an area at a set horizontal and vertical spacing. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Batch Overlay` |  | window: window | Matches sheet pairs and applies overlays to many sheets of the job at once. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Command Palette` |  | window: window | Searches for and runs any app command by name. | [Getting started](ourplancore-start.md) |
    | `DeepSeek API key` |  | window: window | Buttons: Save and start, Later. |  |
    | `Estimating` |  | window: window | Lists all measurements in a table with a filter, a jump to the sheet, editing and row copying. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Excel Links` |  | window: window | Lists all the job's links: cell, state, reason, action buttons. | [Export to Excel](ourplancore-excel.md) |
    | `Recover Keyboard Shortcuts` |  | window: window | Restores a broken hotkeys file from a copy or resets it to the defaults. |  |
    | `Keyboard Shortcuts` |  | window: window | Assigns and resets hotkeys, globally or per job. | [Settings and modules](ourplancore-settings.md) |
    | `Rename Legend Group` |  | window: window | Renames a group of legend rows on the sheet. |  |
    | `Count Points At Line Ends` |  | window: window | Places Count points at the ends of the selected lines, a separate Count for each takeoff. | [Editing and snaps](ourplancore-editing.md) |
    | `Marker Sets` |  | window: window | Lists AI marker sets: apply the filter, rename, delete, open the JSON. | [AI and terminals](ourplancore-ai.md) |
    | `Rename Marker Set` |  | window: window | Renames the selected AI marker set in the set list. |  |
    | `Review Opening Projections` |  | window: window | Reviews the projected openings for 3D: keep, reject, save the reviewed ones. |  |
    | `Paste Measurements` |  | window: window | Asks whether to paste the measurements into the same takeoffs or into new ones. | [Editing and snaps](ourplancore-editing.md) |
    | `OpenAI Settings` |  | window: window | Saves or clears the OpenAI key in the user environment variables. | [AI and terminals](ourplancore-ai.md) |
    | `Import OurPlanCore into Current Job` |  | window: window | Imports another OurPlanCore job, an `.ourplan` file or a folder, into the current job. | [Jobs and saving](job-creation-storage.md) |
    | `Page Setup` |  | window: window | Opens a floating window for the sheet name and scale, with stepping through the job's sheets. | [Sheets (Pages)](ourplancore-pages.md) |
    | `Export PDF` |  | window: window | Picks the sheets and settings for the PDF export; `All` and `None` buttons. | [PDF and delivery](ourplancore-pdf.md) |
    | `Import PDF Takeoffs` |  | window: window | Picks a PDF, shows the measurements found and imports them into takeoffs. | [Other](ourplancore-extras-other.md) |
    | `Create Count Points Along Line(s)` |  | window: window | Places Count points along the selected lines at a set spacing. | [Editing and snaps](ourplancore-editing.md) |
    | `Project Data Recovery` |  | window: window | Restores damaged job files from a verified copy. | [Jobs and saving](job-creation-storage.md) |
    | `Review Roof Draft` |  | window: window | Reviews the roof draft for 3D: keep, reject, save the reviewed roof. |  |
    | `Crop to Sheet` |  | window: window | Copies framed details from different sheets onto one sheet at true scale. | [Crops, mask, overlays, legend](ourplancore-sheets-advanced.md) |
    | `Choose Sheet Overlay Candidate` |  | window: window | Picks a sheet to overlay and opens the check, the source or the alignment editing right away. |  |
    | `Takeoff Folder Properties` |  | window: window | Edits the takeoff folder properties: default color, price and notes for new takeoffs. | [Takeoffs tree](ourplancore-takeoffs.md) |
    | `Trace Walls Inside Area` |  | window: window | Traces the walls inside the selected area as linear measurements by thickness and minimum length. | [Snap and tracing](ourplancore-snap-trace.md) |
    | `Job Is Already Open` |  | window: window | Warns that the job is already open and offers to view it, retry or take it over. | [Jobs and saving](job-creation-storage.md) |
    | `Open Project` |  | window: window | Picks a job: job folders, open, create from PDF or empty. | [Jobs and saving](job-creation-storage.md) |

??? note "window (built in the main window code) (11)"

    | Function | Key | Where in the interface | What it does | Details |
    | --- | --- | --- | --- | --- |
    | `Create Marker Set` |  | window: window (built in the main window code) | Creates a named set from reviewed AI markers. | [AI and terminals](ourplancore-ai.md) |
    | `Merge Into Takeoff` |  | window: window (built in the main window code) | Picks the takeoff to move the selected measurements into. | [Editing and snaps](ourplancore-editing.md) |
    | `Import PDF Options` |  | window: window (built in the main window code) | Sets up PDF page import: raster cache and the black-line snap index. | [Jobs and saving](job-creation-storage.md) |
    | `PlanSwift Import Complete` |  | window: window (built in the main window code) | Reports the result of moving a PlanSwift job over and opens the report. |  |
    | `Sheet Overlay Transform` |  | window: window (built in the main window code) | Sets the shift, scale and rotation of the overlaid sheet precisely with numbers. |  |
    | `Takeoff Item Properties` |  | window: window (built in the main window code) | Edits the takeoff properties: name, joist layout, pitch, Count look, color, price and notes. | [Measuring tools](ourplancore-tools.md) |
    | `Split Selected Takeoffs` |  | window: window (built in the main window code) | Splits the selected takeoffs across all sheets: each section separately or by sheet. | [Editing and snaps](ourplancore-editing.md) |
    | `Create Takeoff From Template` |  | window: window (built in the main window code) | Creates a takeoff or a takeoff tree from a saved template. |  |
    | `Add Template Preset` |  | window: window (built in the main window code) | Adds a new takeoff template preset to the template list. |  |
    | `Edit Template Preset` |  | window: window (built in the main window code) | Edits the name and contents of the selected takeoff template preset. |  |
    | `Workspace conflicts` |  | window: window (built in the main window code) | Shows job version conflicts between the workspace computers. |  |

