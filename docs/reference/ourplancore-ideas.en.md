# Ideas and roadmap

This page lists what OurPlanCore already has in part, what is planned, what is only an idea so far and what went to the archive. Collected from the documents in the app repo (file names in the last column). It is here so you do not wait for a feature that does not exist and do not reinvent one that is already planned.

Statuses: **partly there** - part of the scenario works in 3.0; **planned** - there is a document with steps; **idea** - described, no decision; **archive** - built and turned off, or rejected. An idea is not a promise: nothing has a deadline.

## Web version

| Idea | Status | Why | Source |
| --- | --- | --- | --- |
| Web MVP: pdf.js, scale, Line / Area / Count, tree, CSV, the same job folder through the File System Access API | planned (concept, July 2026) | measure from a browser without installing; no joists, 3D, layers, Similar, AI | `WEB_MVP_PLAN.md`, `INTERACTION_SPEC.md`, `DATA_MODEL_REFERENCE.md` |
| Web job viewer (zoom, pan, showing measurements) | idea | show a takeoff to a client or checker | `DEVELOPMENT_LOG.md` (May 2026) |
| Server and multiple users | idea (v2 of the web plan) | working together | `WEB_MVP_PLAN.md` |

The plan was written for folder-based jobs; the `.ourplan` format is not covered in it.

## AI

| Idea | Status | Why | Source |
| --- | --- | --- | --- |
| AI takeoff: a draft of all walls and openings on a sheet with mandatory review, learning from edits | planned (direction A, the main bet) | faster measuring while keeping control | `STRATEGY_2026.md` |
| Cancel button and an N/M counter for AI requests, a strict JSON schema for actions | planned | do not wait on a hung request | `IMPROVEMENT_PLAN_2026_09_06.md` item 8 |
| AI Auto Trace of walls and areas, search on elevations | partly there: deterministic Trace wall, Trace closed area, Layer Trace | fewer clicks along outlines | `AUTO_TRACE_AREAS_AND_WALLS_SPEC_2026_05_12.md`, `WALL_TRACE.md` |
| Learning from markers: search across several sheets, template memory | idea | a Similar that remembers your symbols | `AI_MARKER_TRAINING_IDEAS.md` |
| Prompts in the settings, AI answer inside Similar | idea | edit prompts without a build | `STRATEGY_2026.md` |
| Similar without the 80-sheet limit | limitation | large plan sets | `CURRENT_OURPLANECORE_STATUS.md` |

What already exists: AI Fill, AI crop to a note, AI Inbox and AI Manager, markers, OCR and AI on the title block, terminals and Agent Bridge: [AI in the app](ourplancore-ai.md).

## 3D and roof

| Idea | Status | Why | Source |
| --- | --- | --- | --- |
| AI 3D Massing (Build 3D Draft, Review, Accept) | archive, turned off since May 2026 | replaced by the deterministic roof | `ARCHIVED_3D_MASSING_LOGIC_2026_05_08.md`, `CURRENT_OURPLANECORE_STATUS.md` |
| Remove the dead massing code | planned | cleaner code | `OURPLANCORE_MASTER_REMEDIATION_AND_RELEASE_PLAN.md` (Phase 7) |
| Overhangs intersecting at hips and valleys, fascia, gable end | planned | honest eave geometry | `ROOF_REVIT_WORKFLOW_PLAN.md` (Slice 4) |
| Edge editing right in the 3D window; secondary roofs and dormers | idea | complex roofs | `ROOF_REVIT_WORKFLOW_PLAN.md` (Slice 2, 5) |
| Roof face graph, solver version with a "rebuild" warning, debug layer, manual seam editing, a library of test roofs | idea | a reliable generator | `ROOF_GENERATOR_NEXT_IDEAS_2026_05_21.md` |
| The same approach for slabs, ceilings, siding, windows | idea | 3D as the estimator's "third hand" | `THIRD_HAND_PRODUCT_VISION.md` |
| AI as a fallback for the roof | idea | when the geometry cannot be read | `THREE_D_ROOF_SYSTEM_MAP.md` |

## PlanSwift parity

| Idea | Status | Why | Source |
| --- | --- | --- | --- |
| Formulas and assemblies, price database | no, known limitation | an estimate from the takeoff | `PLANSWIFT_MVP_REQUIREMENTS.md` |
| Item and Note formulas when importing a PlanSwift job | no | full transfer of old jobs | `PLANSWIFT_PROJECT_IMPORT_PLAN.md` |
| Separate X and Y scale, arcs | no | distorted scans, round elements | `OURPLANECORE_TASK_ROADMAP.md` |
| Grid, Single-Click Area / Linear / Count, Roof Area, Price per SQ FT | idea | special PlanSwift tools | `PLANSWIFT_TAKEOFF_TOOLS.md` |
| Detachable takeoff windows (AvalonDock) | idea; Detached Sheets used instead | second monitor | `OURPLANECORE_TASK_ROADMAP.md` |

What PlanSwift features already exist: Joist Area, Beam and Openings, P Line, Similar, Repeat Line, detached sheets, PlanSwift converter, auto-routing.

## Interface

| Idea | Status | Why | Source |
| --- | --- | --- | --- |
| New Open Job dialog: sources, groups, star | partly there | find a job faster | `OPEN_JOB_REDESIGN_PLAN.md` |
| Grid, side panel and drag-drop in Open Job | archive (rejected) | | `OPEN_JOB_REDESIGN_PLAN.md` |
| Excel-level managers: a grid instead of a tree, formulas, custom columns, Quick Report, Materials with assemblies, PowerRename | idea (estimate about 3 months) | edit the tree like a table | `MANAGERS_DEEP_RESEARCH.md` |
| Accessibility: Space not on a button, visible focus, modal F1, unified notifications, adaptive status bar | planned | keyboard work | `OURPLANCORE_MASTER_REMEDIATION_AND_RELEASE_PLAN.md` (Phase 8) |
| HTML interface mockups (modern-light, dark-studio, bluebeam-dense) | idea, reference | | folder `docs/mockups` |

## Reliability and speed

All items of the improvement plan from 09/06/2026 are open and planned:

| Item | Why | Source |
| --- | --- | --- |
| Protected settings: Missing / Valid / Invalid, last-good, showing the rule source | do not lose rules when the file is broken | `IMPROVEMENT_PLAN_2026_09_06.md` item 1 |
| Excel gate: error `0x800A03EC` in the wall macros, workbook backup before writing | a recoverable Excel failure | item 2 |
| Reproducible build, CI, code signing | public distribution | item 3, `..._MASTER_..._PLAN.md` (Phase 5) |
| Room for working copies, full backup manifest | disk control | item 4 |
| Shared render memory budget, overlay tiling | large jobs | item 5 |
| Trees on data models, Takeoffs reload a quarter faster | large trees | item 6 |
| Save only changed takeoffs | Save a quarter faster | item 7 |
| State coordinators instead of one big window | fewer bugs when editing | item 9 |
| `measurements.json` schema version | file compatibility | `STRATEGY_2026.md` |

Rejected: big MVVM, GPU viewport (SKGLElement). The move to .NET 10 is blocked by the Excel checks.

## Excel and estimates

| Idea | Status | Why | Source |
| --- | --- | --- | --- |
| Assembly database: wall = studs + plates + OSB | idea (direction B) | the takeoff goes straight into an estimate | `STRATEGY_2026.md` |
| CSI MasterFormat, ClosedXML | archive (historical idea) | | `OURPLANECORE_TASK_ROADMAP.md` |

## Team and distribution

| Idea | Status | Why | Source |
| --- | --- | --- | --- |
| A team tool: redo, comparing two takeoff versions, "checked" marks | idea (direction C) | checking someone else's measurements | `STRATEGY_2026.md` |
| Public release through GitHub | planned, blocked until code signing | distribution beyond one PC | `..._MASTER_..._PLAN.md` (Phase 5), `DEVELOPMENT_LOG.md` |
| Build in public on a personal channel | idea | | `CONTENT_MAP.md`, `CHANNEL_PLAYBOOK.md` |

The name OurPlanCore is settled; the logos are in `brand-assets`. There is no separate marketing plan for the app in the documents.

## See also

- [What's new](ourplancore-changelog.md) - what from the plans has already shipped
- [3D and managers](ourplancore-3d.md)
- [AI in the app](ourplancore-ai.md)
