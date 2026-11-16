# Excel macros and hotkeys

Here: which VBA macros are built into the `TemplateCom.xlsm` workbook, what each one does, when to run it and in what order. These are not standard Excel shortcuts: the macros work only in a workbook with macros enabled.

<figure markdown>
  ![XL strip in OurPlanCore](../assets/images/ourplancore/v3/excel-strip.png)
  <figcaption markdown="span">The XL strip in OurPlanCore writes takeoffs into the workbook and runs the calculation macros itself. The other macros are run in Excel with a hotkey or through Alt+F8.</figcaption>
</figure>

!!! note "E-Wood tab"
    All these macros, plus the order, check and delivery buttons, are collected on the E-Wood tab, which installs from a single file: [E-Wood tab in Excel](ewood-tab.md). Some insert macros work differently from the tab than from the workbook: that is noted where it applies.

!!! warning "The macro does nothing"
    1. The open workbook is made from the `TemplateCom.xlsm` template (a copy is in the app's updates folder), not someone else's file.
    2. Macros are enabled: `File > Options > Trust Center > Macro Settings`.
    3. The cursor is in the right place: insert macros work from the selected row, calculation macros from the selected range.
    4. The hotkey did not work: `Alt+F8`, pick the macro by name.

## Hotkeys

Hotkeys checked against the macro source code. Macros without a hotkey are run through `Alt+F8` or a button.

| Hotkey | Macro | What it does |
| --- | --- | --- |
| ++ctrl+shift+b++ | `C_BeamsSort` | beams from "mark and length" pairs into `Beam` rows |
| ++ctrl+shift+j++ | `C_JoistsSort` | joists from "count and length" pairs into `Joists` rows |
| ++ctrl+shift+h++ | `C_HeadersSort` | headers into width bins `up to 48" / 60" / 72" / over 72"` |
| ++ctrl+shift+p++ | `C_PostsSort` | posts by mark with a legend |
| ++ctrl+shift+f++ | `C_SumTheSameValues` | add up identical rows (key: label + unit) |
| ++ctrl+m++ | `Y_MultiplySelectedCells` | multiply the selected cells by an address (for example, by the header's G) |
| ++ctrl+shift+i++ | `Y_Improve_Note` | rewrite a note's text following the samples on the `Standarts` worksheet (check the result by eye) |
| ++ctrl+shift+t++ | `Y_CheckEnglish` | check the English in the selection |
| ++ctrl+shift+o++ | `Y_InsertDate` | insert the date |
| ++ctrl+shift+v++ | `Y_noValidation` | remove drop-down lists (data validation) |
| ++ctrl+w++ / ++ctrl+q++ | `Y_InsertCellsUp` / `X_DeleteCellsUp` | insert / delete cells A:H with a shift. Only this way, never a whole worksheet row |
| ++ctrl+e++ | `B_DeleteZeroRowsOnlyIn_AtoH` | delete rows with a zero quantity (A:H only) |
| ++ctrl+shift+d++ | `X_DeleteRowsByColor` | delete the template's gray placeholder rows |
| ++ctrl+t++ | `B_FrameOC_InsertOneRow` | insert a `Frame N" o.c.` row under the selected one |
| ++ctrl+r++ | `B_Plate2_InsertOneRow` | insert a `Plate (2)` row under the selected one |
| `Alt+F8` | `B_BoltsAdd`, `C_TrimsCalc` and the rest | no hotkey |

??? note "Jumping between sections (Ctrl+F1 ... Alt+Shift+F9)"
    Some workbooks assign hotkeys on open that jump to a section header: ++ctrl+f1++ ... ++ctrl+f5++ `1st ... 5th Floor Walls`, ++ctrl+f6++ / ++ctrl+f7++ `Gable Walls #1 / #2`, ++ctrl+f8++ `Parapet Walls`, ++ctrl+f9++ `Wall Materials`, ++ctrl+f11++ / ++ctrl+f12++ `Foundation / Basement Floor Walls`; ++alt+f1++ ... ++alt+f4++ `1st ... 4th Floor Framing List`, ++alt+f5++ `Loft Framing List`, ++alt+f6++ / ++alt+f7++ `Roof Frame list / Roof System Misc`, ++alt+f10++ `Roof Products`, ++alt+f11++ / ++alt+f12++ `Soffits and Fascias / Exterior Trims`; ++alt+shift+f1++ `Interior Doors&Trims`, ++alt+shift+f2++ `Drywall & Insulation`, ++alt+shift+f8++ / ++alt+shift+f9++ balcony / porch by fill. The jump finds the header by its exact text.

    !!! warning "Being verified"
        The current macro source code has no navigation module; if the hotkeys do not jump in a workbook, that is not a bug.

## Macros by stage

### 1. Calculation after export (A series, run by the XL strip)

They work on the selected range in the right-hand `J:N` area. The XL strip in OurPlanCore runs them itself; by hand they are needed only to recalculate one group.

| Macro | What it does | When |
| --- | --- | --- |
| `A1_UnitTable` | units table by floor | `units` exist in the tree |
| `A2_SQFT_calc` | floor, gable and truss heel areas; roof pitches in the order they appear in the selection | after `SF`, `GB`, `TH` |
| `A3_Walls_Calc_AllGroup` / `_OneGroup` | walls from J:N into the `O:AB` matrix and Floor Walls rows; `(2)` in the name multiplies the length, `corr` = `cor` | after `WL` |
| `A4_Parapet` | parapets: three numbers from the end of the name (`prpt 6.4 5.3 0.5`) | after `PP` |
| `A5_Openings` | openings by width into header bins, flashing | after `OP` |
| `A6_Eve_Rakes` | `eve 12 main`, `rake 12 main`, `returns 24`, `canopy 36 porch` into the eave rows | after `E/R` |
| `A7_walls_sheathing` | based on the text in J (`Zip`, `OSB`, `no insulation`, `1" Insulation`) keeps the right sheathing rows and writes the spec cell `O3` or `O5` | after `SH` |
| `A8_SplitWallSuffixes_ByJ` | splits wall names into a base name for A3 and a suffix with the detail (`ext 10.09 5/S400`) | walls with a detail in the name |
| `Y_Run_First6` | A2 ... A6 in a row, A1 last (A1 rebuilds the selection) | manual full run |

### 2. Scope (A9 series)

| Macro | What it does |
| --- | --- |
| `A9_Fame_only` | removes the trim and product blocks, keeps only framing (deletes only A:H with a shift) |
| `A9_1_wall_panel` | in the `Floor Walls` sections keeps the panel-building rows, moves sheathing to the WRB and Tape row; the floors' stick rows come back below under the note `Note: Optional stick frame, if walls are not panels; verify.` |

Both are run when the workbook is created, according to the project scope. Do not rerun them on a finished workbook without a reason: they delete rows.

### 3. Structural after input (C series)

| Macro | Input | Output |
| --- | --- | --- |
| `C_BeamsSort` | pairs `H5 7` + count; legend at the end of the selection `H5 - (2) 1 3/4 x 11 7/8 LVL`; the tail `(24V48)` goes to E | `Beam` rows with the size by code; in J mode it inserts room in A:H itself |
| `C_HeadersSort` | `(2) 2x10 4`, `ext H5 7`; legend `H5 - (2) 2x10` | `Ext. Headers up to 48" / 60" / 72" / over 72"`, int separately |
| `C_JoistsSort` | count / length pairs with mark and spacing (`11 7/8 TJI 110 24"`) | identical lengths are added together; a length over 8' that is odd gets +1 |
| `C_PostsSort` | `C5 2`, `C5 12`; legend `C5 - 3 1/2 x 5 1/4 PSL 1.8E` | `Posts` rows with code and grade in E; default length 10' |
| `C_RimBoardBlockingHangers` | flags in M: `r` rim, `rb` ribbon, `b` / `b48` blocking, `h16` hangers, `s` screws, `t` ties, `blt24` anchor bolts, `l` ledger, `bd` drywall blocking, `bft` bracing for trusses; doubled letter = x2; material legend at the end (`l - 2x10`, `t24 - A35`) | rim, ribbon, blocking, hangers, ledger rows by group; a bolts + washers + nuts block |
| `C_SumTheSameValues`, `C_SumNearWindowValues` | three columns label / number / unit | collapsed totals; for windows, the sum of values next to openings for A5 |
| `C_TrimsCalc` | trim block of one element + an `EA` row | trim multiplied by the quantity ([Trim macros](../work/exterior-trims/macros.md)) |

### 4. Inserting rows and blocks (B series)

Put the cursor on the row where the block should start: the insert goes down from it, in A:H only.

| Macro | What it inserts |
| --- | --- |
| `B_DuplicateBlock` | tab only: a copy of the block below it, next number, its own units, links to takeoffs cleared ([details](ewood-tab.md#duplicate)) |
| `B_BoltsAdd` | 4 rows: `Blocking`, `Anchor Bolts`, `Washers`, `Nuts` (counted in pairs, labels from H). From the tab G is empty, inches in the label, 1.1 multiplier in C |
| `B_Plate2_InsertOneRow`, `B_FrameOC_InsertOneRow` | a `Plate (2) ... P.T.` or `Frame N" o.c.` row with a formula. From the tab `Plate (2)` does not enter `G=100` |
| `B_JambsAllBlock` | from the tab a `Jambs` row for openings, the `Wall Materials` header only if it is missing; in older workbooks the same row is called `Blocking around all openings` |
| `B_ShaftWallsBlocks` | two shaft wall blocks (liner panels + channels); from the tab the second one is called `Shaft Fire walls`, G empty |
| `B_PaversBlock` | `Pavers` with a `by others` note; from the tab without the railing rows, those are in the `Insert Block` menu |
| `B_MetalStuds_ByJ` (`_16oc`, `_24oc`) | the trio `Tracks (1) btm`, `Deflection Tracks (1) top`, `Mtl Studs` from the table on the right (size, length, unit, height) |
| `B_Balcony_Insert_Template_FromText` | a balcony block from the command `b 12x30`. In current workbooks block `#1` is already in the template: fill it in, do not insert a second one ([Blocks](dfl-blocks.md)) |
| `Y_add_2400V48` | fill in `2400 V48` values from a two-column list |

### 5. Cleanup and final (X, Y series)

| Macro | When |
| --- | --- |
| `X_DeleteRowsByColor` (++ctrl+shift+d++), `B_DeleteZeroRowsOnlyIn_AtoH` (++ctrl+e++) | after all inserts: placeholders and zeros go |
| `X_ClearColor`, `X_ClearWall_SQFTCells`, `X_ClearParapetTable` | gray fill to white; clear wall areas or the parapet table before a new calculation |
| `Y_noValidation` (++ctrl+shift+v++), `Y_CheckEnglish` (++ctrl+shift+t++), `Y_InsertDate` (++ctrl+shift+o++) | before the processed `.xlsx` |
| `Y_Improve_Note` (++ctrl+shift+i++) | draft of a note; then check it against the [note rules](standard-notes.md) |
| `Z_Dont_use_Run_ByPriority` | do not use |

## Workbook order of work

1. In OurPlanCore: the `LG` legend is filled in (beam, post and header codes, detail flags, sheathing), then `ALL` or the needed buttons of the XL strip.
2. In Excel: check that everything from the tree arrived (the export warning lists skipped takeoffs), fix J:N.
3. Structural sorts, if something was entered by hand: ++ctrl+shift+b++, ++ctrl+shift+j++, ++ctrl+shift+h++, ++ctrl+shift+p++, then `C_RimBoardBlockingHangers`.
4. Balcony, porch, holdown, bolt and jamb blocks ([Blocks](dfl-blocks.md)).
5. Cleanup: ++ctrl+shift+d++ gray rows, ++ctrl+e++ zeros, ++ctrl+shift+v++ validation.
6. Final: ++ctrl+shift+o++ date, ++ctrl+shift+t++ English, notes per the rules, Front Page filled in, then the processed `.xlsx`.

## Common mistakes

- Inserting a whole worksheet row instead of ++ctrl+w++: the right-hand areas shifted.
- `A9_*` rerun on a filled workbook: it deleted needed rows.
- `C_BeamsSort` without a legend: B shows the code `H5` instead of the size.
- A balcony block inserted by the macro on top of the template `#1`: two blocks.
- A quantity typed in as a number after a macro: it will not update on the next export.

All workbook mistakes: [Common mistakes, Excel DFL and notes](../start/common-mistakes.md#excel).

## See also

- [How the DFL workbook works](dfl-overview.md), [Balcony, porch and holdown blocks](dfl-blocks.md), [Formulas and factors](formulas.md)
- [Trim macros](../work/exterior-trims/macros.md), [OurPlanCore: Estimating and export](ourplanecore.md)
