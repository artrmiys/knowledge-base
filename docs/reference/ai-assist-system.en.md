# AI help in estimating work

Here: where AI helps in the current workflow, what it does well, what stays with the estimator and how to check the result. AI speeds up reading the plan set and routine work in the workbook; the decision and the responsibility for quantities stay with the estimator.

## Where AI is used now

| Step | What AI does | What to check |
| --- | --- | --- |
| Job intake | PDF breakdown: sheet numbers and types, scope, sheet summary, a "To check" list, draft header notes | sheet numbers and scale; template notes against the scope |
| Sheet names in OurPlanCore | reads the title block on the Name command, suggests a number and a tag | tag last (`a101 1st`, `s101 f`), `f` only on the foundation |
| Detail crops | AI Crop Notes: text and a note for a detail crop | marks, sizes, layers against the source sheet |
| Agent terminals in the app | built-in terminals and Agent Bridge: the agent sees the open job and can create and fix takeoffs, the tree, names | every new takeoff by eye on the sheet; color and symbol of the new item |
| Excel workbook | inserting rows and notes by the rules, blocks copied from the reference, checking note length and rounding, a draft `Changes.txt` for a revision | compare the processed `.xlsx` with the `.xlsm`; notes per the [rules](standard-notes.md) |
| Note text | `Y_Improve_Note` in Excel rewrites a note following the samples on the `Standarts` worksheet | natural phrasing, `per <sheet>`, length up to 100 |
| Checking a delivered job | comparing the workbook with the drawings: misses, doubles, formulas pointing into another block | open every comment on the sheet, do not fix blindly |

## How to ask

1. Give the scope, sheet and scale: "S201, 3/16", second floor beams".
2. Ask for a list with sources: mark, size, sheet and detail, what is unclear.
3. Carry over only what you checked; write assumptions as `assumed; verify` notes.
4. A similar delivered job is a hint for misses, not the content of the new one.

## What not to carry over blindly

| Data | Why |
| --- | --- |
| Beam, header, post codes (`H5`, `B2`, `C5`) | per project: the legend is in this plan set's schedule |
| Wall types, holdowns, hangers, anchor spacing, insulation, sheathing | read them in the schedules and details of your own project |
| Template values (`Zip Tape`, `29 oz` adhesive, `Tyvek`) | replaced per the spec, they do not stay as defaults |
| Quantities from similar buildings | only as an order-of-magnitude check ([Benchmarks](quantity-benchmarks.md)) |

## Rules for AI in this knowledge base

- Cite the sheet or detail number, not the PDF page; no source - `assumed; verify`.
- Do not pass off an open question as fixed; do not make up hardware models: a condition not in the tables gets `TBD` with a note.
- Read the whole workbook row, including the working zones on the right ([DFL](dfl-overview.md#zones)).
- A new correction from the owner becomes a rule here and in the rules canon, it does not stay in the chat.

## See also

- [OurPlanCore: interface and tools](ourplanecore.md), [Getting started](ourplancore-start.md)
- [DFL: how the workbook is built](dfl-overview.md), [Notes in DFL](standard-notes.md), [QA checklist](../start/quality-checklist.md)
