# Maintaining the knowledge base

This page describes how the KB site is maintained. What was checked and when:

- the texts of the OurPlanCore section were rewritten for Lite on November 16, 2026 (Lite 3.0.36-lite, full version 3.0.35);
- the screenshots in `ourplancore/v3/` were added on October 17, 2026 on OurPlanCore 3.0 and have hardly been retaken since: at the next check compare every frame with the current window;
- the rules on which pages disagreed with each other (units, factors, formulas of DFL rows) were checked against the DFL template and its macros on November 16, 2026.

The order of checking and delivering a project is in the [QA checklist](quality-checklist.md).

## Corrections from readers

Readers send corrections through the [suggestion page](suggest-change.md), no sign-up needed. The form sends them to a server; the receiver and the update procedure are described in `tools/feedback-server/README.md`. Corrections are visible only to the owner on a private page; its address is in the same file. Only the owner puts them on the site.

## Where to update the app description

- Overview, window map and the path to delivery: [OurPlanCore 3.0](../reference/ourplanecore.md).
- The section describes OurPlanCore Lite, the build estimators have. What Lite
  lacks (AI models, terminal, 3D, Workspace) lives in the menu block "AI, terminal
  and 3D (full version)"; small things inside regular pages are marked with the words
  "full version only". List of differences: [Lite vs full version](../reference/ourplancore-lite.md);
  check it against `docs/LITE_BUILD.md` and `Models/AppEdition.cs` in the app source.
- Each feature is described on one page of its level: "Every day"
  (jobs, sheets, tools, tree, Excel, PDF) or "Advanced".
- Shortcuts: [one canon](../reference/ourplancore-shortcuts.md).
- Version changes: [what's new](../reference/ourplancore-changelog.md).
- 3.0 screenshots: `docs/assets/images/ourplancore/v3/`, taken on the demo job
  (`Open sample job`) in a separate app profile, with no client data.
- Symbols that are not on the keyboard (long dash, arrows, guillemets) are caught by
  `python tools/check_symbols.py`; run it before committing.

One feature should have one detailed description. On other pages leave
a short route to it. Do not copy the shortcut table into several places.

## What to check when updating

1. State the version and the date of the check.
2. Check the command name, module availability, scope of action and how the
   result is saved against the current app.
3. Separate finished features from plans and experimental modules.
4. Check links and images. Keep the URLs of existing pages and useful
   anchors when reworking text.
5. Check that the image matches its caption. Mark a screenshot of an old version as such;
   do not present it as a check of the new EXE.
6. Check the final page on a wide and a narrow screen, the search and expandable
   instructions. Keep the previous version for rollback.

## Checking the local build

The site is built with MkDocs Material. From the root of its repository:

```powershell
.\.venv\Scripts\python.exe -m mkdocs build --strict
.\.venv\Scripts\python.exe -m mkdocs serve -a 127.0.0.1:8000
```

A successful local build does not yet mean the public site is updated.
Publishing is a separate step, after checking the result and with the owner's
permission. The exact publishing route and configuration are in the repository;
an old record about stopped Actions should not be taken as the current state of CI.

## Working with sources

An estimating rule must have a context where it applies and a source. Statistics
from past jobs help find an unusual value, but they do not replace the drawings and scope
of the current project. A conflict between sources must be shown, not silently resolved.

The public KB includes anonymized rules, instructions and examples. The user's working
paths, correspondence, access credentials, personal data and project materials
stay internal unless permission is given.

## See also

- [How to use the KB](how-to-use.md)
- [Images and diagrams](images-and-schemas.md)
- [Page preview](site-preview.md)
- [QA checklist](quality-checklist.md)
