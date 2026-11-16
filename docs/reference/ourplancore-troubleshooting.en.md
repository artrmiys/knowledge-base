# OurPlanCore troubleshooting

Symptom, cause and what to do, for OurPlanCore 3.0. You need it when the app does not behave as expected: something disappeared, landed in the wrong place, is slow, does not save. Start with the table for your symptom.

## Sheets or takeoffs disappeared {#missing}

| Symptom | Cause | What to do |
| --- | --- | --- |
| No measurements on the sheet, but they are in the tree | the takeoff is hidden with the ++h++ key or with the sheet visibility dot | the visibility toggle on the takeoff in Takeoffs or the visibility dot on the sheet in Pages (`Show all takeoffs on <sheet>`) |
| A whole takeoff is gone after Merge | it was merged into the surviving one | ++ctrl+z++ with focus in Takeoffs or right-click `Undo Takeoff Merge / Split`; a copy is in `AI_Context/takeoff-merge-trash` |
| A folder disappeared after an agent edit | deleted through the Agent Bridge | `agent_bridge.py undo` or the `AI_Context/agent-trash` folder |
| A sheet vanished after sorting | Sort A/S or D/Sec/WT moved it | `Open / Import > Undo Last Page Sort`; search the sheets in Pages |
| A sheet or takeoff deleted by accident | | ++ctrl+z++ in the same tree brings back the last deletion; `Delete Empty` is undone too |
| Measurements are there, the legend is empty or wrong | a different legend order or groups | right-click the sheet: `Reset Sheet Legend Order`, `Organize > Legend Groups...` |
| After a rollback to a `.bak`, crops and masks are gone | an EXE older than 2.2.34 reads them as line markup and loses them on save | do not save the job with the old EXE; go back to 3.0 and open a copy made before the save |

## A takeoff landed in the wrong folder {#routing}

| Symptom | Cause | What to do |
| --- | --- | --- |
| No `Route:` in the status bar | the sheet has no W/F/S/U dot | set a dot under the Scale label or `Settings > Sheet Takeoff Routing > Route sheets without a dot now` |
| `Route sheets without a dot now` did not set a dot | the sheet name has a tag from Skip tags (`sec`, `el`, `d`, `rcp`...), two level tags (`1st 2nd`), or `u` is not the last word | set the dot by hand or rename the sheet |
| The takeoff went into another building | the green dot is on a different folder | in the Takeoffs header click the red dot (root), or select the right building and the green dot |
| `eve` or `gable` did not follow the sheet dot | name rules beat the dot | this is by design; change it in `Settings > Takeoff Name Routing` |
| A Count on a W sheet landed in `walls/...` | that is the default | place holdowns on an S sheet or add a name rule |
| A new takeoff is not created, a message about root | the green dot points to a deleted folder | click the red dot and pick the building again |
| A pasted copy landed in a different subfolder | the `Copies keep their source folders` checkbox | turn it on or off in `Settings > Sheet Takeoff Routing`, check the `Root:` line in the paste dialog |

The rules explained: [Takeoff routing](ourplancore-routing.md); which sheet carries which kind of work and copies for shear: [Split by sheets](ourplancore-split-by-sheets.md); several buildings: [Multiple buildings](ourplancore-buildings.md).

## Slow {#speed}

| Symptom | Cause | What to do |
| --- | --- | --- |
| Zoom stutters on a large blank sheet | fixed in 2.2.39-2.2.42 | update to 3.0; check the version in the window title |
| A heavy PDF sheet takes long to open | the raster is not prepared | Sheet Manager: select, PNG and DPI, `Prepare`, then `First On`; or `Display > Static image` |
| Slow after opening a job | background page warm-up | turn off `Settings > Defaults > Warm all job pages in background` (off by default) |
| Switching sheets, the tree or Save lags | various causes | note exactly which operation and the version; the app log has `Viewport slow frame` lines with timings for slow frames |
| Name over a whole set takes long | one sheet in a 127-page set takes about 12 s to read | this is normal; run it on a folder, not sheet by sheet |

## Saving, opening, version {#save}

| Message or situation | Cause | What to do |
| --- | --- | --- |
| `Saved in local recovery` | the `.ourplan` package is not updated yet | click `Save` and wait for `Save: Saved hh:mm:ss` before copying the file |
| `Job Is Already Open` / `This job is owned by another OurPlanCore instance` | the job is open in a second window or on another computer (Workspace) | close the second window; in Workspace wait for the sync, do not open it at the same time |
| Save failed after a sheet was moved to another folder | fixed in 2.2.16 | update |
| The job sits in a cloud sync folder, Save or opening fights with it | the sync client swaps or locks the file | keep the working job in `Desktop\OurPlanCore Jobs`, copy it to the cloud after Save; on a message about an external change, save your version with `Save As` |
| Corrupted metadata JSON | | `Open / Import > Project Data Recovery...`: an entry from the list, `Retry reading` or `Restore from copy...` |
| The `.ourplan` itself cannot be read | | open the offered local recovery; Recovery does not repair a ZIP or PDF |
| An interrupted sheet operation | | the `.undo/operations` log: `Undo Last Page Operation` |
| Not enough space | the unpacked job is bigger than the free space | free up space outside jobs and recovery |

### Which version is running {#version}

The version is in the window title: `OurPlanCore 3.0.0 - <job>`, and in the `Version ...` line of the app log. There is one install: the updates folder `Desktop\updates\OurPlanCore`, the rollback is the `.bak` file next to the EXE (the file name carries the version, for example `ourplancore.exe.2.2.42-....bak`). The old separate Preview is no longer used. If a feature from [What's new](ourplancore-changelog.md) does not work, check the version in the title first.

## Terminal, Agent Bridge, Workspace {#terminal}

| Symptom | Cause | What to do |
| --- | --- | --- |
| The assistant writes `context_unavailable` | fixed in 2.2.36 for sheets with crops and markup | update; the `Context` button opens the file, it should contain `state: open` |
| `Run` does not start the terminal | no Git Bash or assistant shortcut | install Git Bash, sign in to the CLI once; with Workspace no shortcut is needed |
| The agent does not see the job | the bridge is off or the job is read-only | `Settings > Agent Bridge > Enable local assistant access`; `agent_bridge.py sessions` |
| The agent answered with a timeout | the outcome is unknown | do not repeat the request with a new ID; `inspect` and check the tree |
| `Synchronization is running` | a sync is in progress | wait and repeat `Sync now` or `Share current saved project` |
| Job version conflict | edited on two computers | `Settings > Workspace > Review conflicts`: `Keep this computer`, `Use server version` or `Open preserved files` |

All terminal panel messages and what to do with them: [AI console, if the terminal does not start](ourplancore-ai-console.md#not-starting).

## Pipeline and Job Tracker {#cli}

| Message | What to do |
| --- | --- |
| `Refused to ...: OurPlanCore is running. Close it first.` | the pipeline changes the package only when the app is closed: close the window and repeat |
| `'<name>' has no leading project number (expected 'NN. Name')` | rename the job to `NN. Name`; the `In Progress` button takes the number from the name |
| No `In Progress` button | `Settings > Modules`, the Job Tracker module |
| PDF export by building gave one file | the green dot is not set or the red one is; or it was run with `--grouping single` | set the green dot on the building, save, repeat |

## PDF and Excel {#pdf}

| Symptom | Cause | What to do |
| --- | --- | --- |
| A crop is missing in the PDF, the log says `Crop skipped on '<sheet>'` | the crop's source sheet was deleted | delete the crop or bring back the sheet; find the crop with the red cross on the sheet |
| The Hide mask or crops do not print | the Annotations module is off | turn the module on; Markups can stay off |
| Lines in the PDF cover the drawing | | `PDF Output > Opac` below 100 |
| The PDF does not look like the screen | the Viewport ribbon sets up the screen, PDF Output sets up the output | `PDF Output > Preview` before export |
| Excel: `ALL` stopped | no unambiguous building root, or a step failed | set the green dot; the failed steps are listed in the warning; a second run does not damage the template |
| Excel got extra rows | a different workbook, worksheet or cell is active | check the active workbook and cell; `Value` writes into the active cell |
| Notes did not reach Excel | the "comments" dot on the Excel button is off | fill the dot and repeat the export |
| Moved a line in Acrobat, the label and legend show the old number | Adobe does not recalculate them | fix the measurement in the app and export again: [PDF in Adobe](ourplancore-pdf.md#adobe) |
| In Acrobat the points or the joist area do not move | that is how it is, only lines, areas and labels move | [what moves](ourplancore-pdf.md#adobe) |
| The link icon is yellow or red, the cell did not update | the link is waiting or broken, the reason is in the icon tooltip | [Link to Excel states](ourplancore-excel.md#link-states) |
| After editing a measurement the number appeared in someone else's `J:L` row | Auto Link linked it as `Probable`: the same number was there | `Unlink` on the takeoff, fix the number in the cell by hand: [when Probable is wrong](ourplancore-excel.md#auto-link) |

## A button or key does not work

| Symptom | What to check |
| --- | --- |
| No tab or button | `Settings > Modules`: the module is on, and the job copy does not turn it off |
| The key types a letter | the focus is in a text field: ++esc++ and click on the sheet |
| A binding does not fire | [key editor](ourplancore-shortcuts.md#remap): the command context and conflicts |
| Editing is blocked | the job is read-only or open in another window |
| Mirror is unavailable | select suitable measurements; mirroring selected objects and flipping the sheet are different commands |

## See also

- [Getting started](ourplancore-start.md)
- [Jobs and saving](job-creation-storage.md)
- [Takeoff routing](ourplancore-routing.md)
- [Hotkeys](ourplancore-shortcuts.md)
- [What's new](ourplancore-changelog.md)
