# OurPDF keyboard shortcuts

Here: all OurPDF 1.0.0 keys with their default assignments, by group; mouse and modifiers; how the keys differ from OurPlanCore; how to reassign them. "None" in the key column means the command has no default key; you can assign one in Settings.

A key does not work while the focus is in a text box: the letter is typed there. Click the sheet and the keys work again.

In the app itself, ++f1++ opens a panel with all active keys, a second ++f1++ or ++esc++ closes it.

## Tools and selection { #tools }

| Key | Action |
| --- | --- |
| ++v++ | Select: the normal mode, pick, move, edit points; empty space moves the sheet |
| ++e++ | Frame selection: left to right takes what is wholly inside, right to left what is touched |
| ++t++ | Select PDF text: drag or double-click a word, ++ctrl+c++ copies |
| ++h++ | Hand: move the sheet |
| none | Measure (ruler); since version 0.9.31 ++ctrl+shift+m++ is Split, as in OurPlanCore |
| ++ctrl+6++ | Note |
| none | Polyline (not a measurement) |

## Measurements { #measure }

| Key | Action |
| --- | --- |
| ++r++ | Distance (Ruler in OurPlanCore) |
| ++l++ | Line by points, perimeter (Line in OurPlanCore) |
| ++a++ | Area (Area in OurPlanCore) |
| ++j++ | Joists / rafters (Joist Area in OurPlanCore) |
| ++p++ | Count: count points |
| ++b++ | Beam: two clicks along the beam, a dimension and Count `Beam 12` ([Beam and Openings](measure.md#beam-openings)) |
| ++o++ | Openings: two corners of the opening, width, height and Count `3.0x6.8` |
| ++ctrl+m++ | Merge: the selected measurements into another takeoff ([Merge, Split, Combine](measure.md#merge-split)) |
| ++ctrl+shift+m++ | Split: the selected measurements into a new takeoff |
| none | Combine: Union, Subtract, Intersect, Remove Overlap, Divide |
| ++f3++ | Snap to measurements on and off, as in OurPlanCore |
| ++ctrl+f3++ | Snap to PDF lines on and off, as in OurPlanCore |
| ++ctrl+shift+b++ | Break: split the selected polyline into segments |
| ++space++ | Continue the takeoff of the selected measurement, again to stop |
| ++x++ | Cut from areas and lines: a box or polygon (hole, bite or split) |
| ++f9++ | Box: area, line, joists, cut and both sides of a distance by two opposite corners |
| ++f8++ | Ortho: strictly horizontal or vertical |
| ++tab++ | While measuring, before the first point: the drawing edge under the cursor, a second time the contour |
| ++c++ | Finish the measurement, as in OurPlanCore |
| ++enter++ | Finish a perimeter, area, cloud |
| ++backspace++ | Remove the last point of the measurement |
| ++d++ | Extra joists on the selected joists area: clicks place joists, ++d++ or ++esc++ exits |
| none | Show or hide measurement value labels |
| none | Line lengths (LF) only on hover or always on the sheet |
| ++ctrl+e++ | Into open Excel: values only |
| ++ctrl+t++ | Into open Excel: name or color, number, unit |
| none | Export measurements to an Excel file |
| none | [Excel link](excel-link.md): link the selected row, Auto Link, update links, reset all links, link list |
| none | J2 joist rounding |
| none | Pitch, P Line, Ends |
| none | Rotate, mirror, rotate and scale the selected measurements |
| none | Snap: all types on and off |
| none | Legend on the sheet: keep or remove |
| none | Show measurements hidden in the legend |
| none | Reset toolbar: blocks back to their default places |

## Editing { #edit }

| Key | Action |
| --- | --- |
| ++ctrl+z++ | Undo |
| ++ctrl+y++ | Redo |
| ++esc++ | Cancel what is being drawn, clear the selection, return to Select |
| ++ctrl+c++ | Copy the selected comments and measurements, or text |
| ++ctrl+v++ | Paste comments and measurements (onto another sheet in the same spot) |
| ++delete++ | Delete the selection: the selected points or edges, otherwise the whole measurement or comment |

## File { #file }

| Key | Action |
| --- | --- |
| ++ctrl+o++ | Open a PDF |
| ++ctrl+s++ | Write markups into this PDF (a copy of the previous file is kept) |
| ++ctrl+shift+s++ | Save As |
| ++ctrl+p++ | Print |
| ++ctrl+w++ | Close the tab |
| ++ctrl+shift+t++ | Reopen closed file |
| ++ctrl+comma++ | Settings |
| none | Open the PDF backup folder |

## Search { #find }

| Key | Action |
| --- | --- |
| ++ctrl+f++ | Find text |
| none | Find next (++enter++ in the search box); since version 1.0 ++f3++ is snap to measurements, as in OurPlanCore |
| ++shift+f3++ | Find previous |

## Sheet overlay { #overlay }

| Key | Action |
| --- | --- |
| ++ctrl+alt+left++ ++ctrl+alt+right++ ++ctrl+alt+up++ ++ctrl+alt+down++ | nudge the active layer, 6 pt; with ++shift++ 1 pt |
| ++ctrl+alt+plus++ ++ctrl+alt+minus++ | layer scale, x1.05; with ++shift++ x1.01 |
| ++ctrl+alt++ and `[` or `]` | rotate the layer, 1 degree; with ++shift++ 0.25 degree |
| ++ctrl+alt+0++ | reset the layer position |
| ++ctrl+alt++ and drag | move the layer with the mouse without the panel; with ++shift++ finer |
| none | "Overlay" panel, add a layer, Auto Fit, Next Match, Edit by Points, Batch |

## Crop and new sheets { #crop }

| Key | Action |
| --- | --- |
| none | "Crop" panel |
| none | Crop to Sheet |
| none | Lock or unlock the sheet's crops |
| none | New blank sheet, from visible area, from box |

## Pages and navigation { #pages }

| Key | Action |
| --- | --- |
| ++page-down++ | Next page |
| ++page-up++ | Previous page |
| ++home++ | First page |
| ++end++ | Last page |
| ++ctrl+g++ | Go to page |

## View { #view }

| Key | Action |
| --- | --- |
| ++ctrl+0++ | Fit page |
| ++ctrl+2++ | Fit width |
| ++ctrl+plus++ | Zoom in |
| ++ctrl+minus++ | Zoom out |
| ++ctrl+r++ | Rotate view clockwise |
| ++ctrl+shift+r++ | Rotate view counterclockwise |
| ++ctrl+3++ | Continuous scrolling, fit width |
| ++ctrl+1++ | Single page, fit page |
| ++ctrl+h++ | Reading mode |
| ++ctrl+l++ | Full screen |
| ++ctrl+alt+r++ | Show or hide rulers |
| ++ctrl+shift+n++ | New separate view window |
| ++f4++ | Show or hide the left panel |
| ++f5++ | Show or hide the right panel |

## Pages, layers and PDF editing { #edit-pdf }

| Key | Action |
| --- | --- |
| none | Organize Pages (page grid, drag into a folder) |
| none | Crop pages |
| none | Edit PDF content (move, delete, text) |
| none | PDF layers panel |
| none | Which layer: click a line or text on the sheet |
| ++ctrl+a++ | Edit PDF: select all objects on the page |
| ++left++ ++right++ ++up++ ++down++ | Move the selection left, right, up, down (in Edit PDF, 1 pt steps) |
| ++shift+left++ ++shift+right++ ++shift+up++ ++shift+down++ | The same in a large step (in Edit PDF, 10 pt) |
| none | Edit PDF: add text to the page |
| none | Edit PDF: add an image to the page |
| none | Edit PDF: delete everything inside a frame |
| none | Edit PDF: white out a frame |

## Mouse and modifiers { #mouse }

| What | Action |
| --- | --- |
| middle or right button, drag | move the sheet in any tool |
| wheel | scroll; in single-page view turns pages |
| ++ctrl++ and wheel | zoom |
| right button (click) | menu: with the ruler on, the measure menu; on a measurement, its actions; at the bottom, zoom levels |
| double-click | finish a line or area; on a finished measurement - label; on a joists area - its settings; on text - edit |
| ++ctrl++ and click | add a measurement, comment, point or edge to the selection |
| ++ctrl++ and a frame (++e++) | add to the selection |
| ++shift++ while drawing | Ortho for a moment (with Ortho on, frees the line instead) |
| ++shift++ while dragging an edge | strictly horizontal or vertical |
| ++alt++ and drag | move the whole measurement |
| ++shift++ and click in extra joists mode | remove the nearest extra |
| click the icon of a legend row | hide or show the takeoff |
| toolbar block handle, drag | move the block; right-click the handle: reset toolbar |
| ++shift++ while drawing a shape | straight: square, circle, 45 degrees |
| ++ctrl+enter++ | finish text on the sheet |

## Differences from OurPlanCore { #vs-ourplancore }

The measurement keys are the same: ++r++, ++l++, ++a++, ++j++, ++x++, ++c++, ++b++, ++o++, ++ctrl+m++, ++ctrl+shift+m++, ++f3++, ++ctrl+f3++, ++f8++, ++f9++, ++d++, ++p++, ++space++, ++ctrl+shift+b++, ++tab++, ++backspace++, ++esc++, ++f1++, the overlay keys with ++ctrl+alt++. The rest differ:

| Key | OurPDF | OurPlanCore |
| --- | --- | --- |
| ++v++ | Select | Pan |
| ++e++ | Frame selection | Select |
| ++h++ | Hand | hide the takeoff of the selection |
| ++ctrl+y++ | Redo | no Redo |
| ++f4++, ++f5++ | left and right panels | Set Scale, Name / Scale Setup |
| ++f++ | none (fit page on ++ctrl+0++) | Fit: whole sheet |

The full OurPlanCore table: [OurPlanCore keyboard shortcuts](../reference/ourplancore-shortcuts.md).

## Assign or change a key { #remap }

1. Open Settings: ++ctrl+comma++ or `Help > Keyboard shortcuts and settings`.
2. Scroll down to the section "Keyboard shortcuts (empty = default, None = off)". Each row has the command, its default key and a box.
3. Type the combination in the box as text: `Ctrl+Shift+F`, `F3`, `PageDown`. Several combinations separated by commas: `V, E`.
4. An empty box keeps the default key, `None` turns the command off.
5. If two actions got the same combination, "Shortcut conflict" appears under the table with their list.
6. Click "Save". The app does not accept a combination it cannot read and shows an example.

Key names are in English, as in the default column: the digit 6 is `D6` (`Ctrl+D6`), plus and minus are `OemPlus` and `OemMinus`, comma is `Oemcomma`, Backspace is `Back`, Esc is `Escape`. "Reset to defaults" at the bottom of the window restores all keys (and the other settings) to defaults.

## See also

- [Measurements](measure.md)
- [View and settings](view-settings.md)
- [OurPlanCore keyboard shortcuts](../reference/ourplancore-shortcuts.md)
