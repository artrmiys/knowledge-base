# Door and Window Trim

<figure markdown>
  ![Interior door and cased opening schedule rules](../../assets/images/trims/door-opening-schedule.svg)
  <figcaption>Interior doors and cased openings — read plan tags, convert sizes, then fill Excel.</figcaption>
</figure>

## Door Trim

- Unit entry doors may be fire-rated and should be labeled clearly in door
  takeoff, but hardware numbers are not needed for trim.
- Interior door jamb trim can use casing divided by 2 where the local method
  applies.
- Separate common-area doors from unit doors if trim type differs.

## Window Trim

- Count casing/stool/apron only if the finish schedule or details include them.
- Do not reuse exterior window trim logic for interior trims without checking
  scope.

## Check

- Door/window trim can be hidden in finish schedules, interior elevations, or
  details rather than framing sheets.
- Keep trim notes separate from blocking/jamb framing notes.
- If the schedule names a manufacturer or special product, keep it in the note
  instead of flattening the opening to a generic size.

## Door Notation

| Example | Meaning | Use |
| --- | --- | --- |
| `2680` | 2'-6" wide x 8'-0" high | Regular single interior door |
| `(2)2680` | Two doors, each 2'-6" x 8'-0" | Double door pair |
| `2680 Pocket` | Pocket door, 2'-6" x 8'-0" | Keep `Pocket` in the mark |
| `(2)3080 Slider` | Two 3'-0" x 8'-0" sliding leaves | Keep both quantity and `Slider` |
| `2680 Metal F.R. S.C.` | Metal, fire-rated, self-closing door | Garage/mechanical/fire-rated condition |
| `4080 C.O.` | 4'-0" x 8'-0" cased opening | Enter as cased opening, not door |

`F.R.` on a door means **fire-rated**. Do not confuse it with `FRT` lumber /
fire-retardant-treated framing material.

## Trello Rules

| Rule | What to check | Source |
| --- | --- | --- |
| Measure interior doors by the open door symbol. | Count the actual door swing/opening, not nearby wall notes. | [Trello](https://trello.com/c/IZ2sNLWl) |
| Door size `2680` means width `2'-6"` and height `8'-0"`. | Keep size notation consistent before Excel conversion. | [Trello](https://trello.com/c/hCU71d7H) |
| Double doors are written like `(2)2680`. | Keep the pair marker visible. | [Trello](https://trello.com/c/eQgpc2fU) |
| Pocket doors are written like `2680 Pocket`. | Preserve the `Pocket` note. | [Trello](https://trello.com/c/YhlqMraY) |
| Slider doors are written like `(2)3080 Slider`. | Preserve both quantity and type. | [Trello](https://trello.com/c/sgMGFbJN) |
| Garage/mechanical metal doors can be `F.R S.C.`. | Note fire-rated and self-close conditions. | [Trello](https://trello.com/c/aFiv0hIM) |
| Do not enter glass shower doors as interior doors. | Exclude shower glass doors from interior door count. | [Trello](https://trello.com/c/43ZyybeD) |
| Large guest rooms may use `French doors`. | Keep glass/French door note visible. | [Trello](https://trello.com/c/cb8EWYy1) |
| `Cased Openings` are openings without doors. | Write cased openings separately from doors. | [Trello](https://trello.com/c/GIxtgKCI) |
| `4080 C.O.` is a cased-opening notation. | Convert and enter it in the cased-opening side, not doors. | [Trello](https://trello.com/c/XYT9cr0q) |
| Enter interior doors and cased openings for each level in Excel. | Separate floors before trim formulas. | [Trello](https://trello.com/c/Zy0M8kcH) |
| If a door schedule exists, fill from the schedule. | Prefer schedule data over manual plan-only entry. | [Trello](https://trello.com/c/C0LHSgXl) |

## Excel Entry

- After all doors/openings are written, copy the opening mark and quantity
  columns into the right-side Excel helper table for casing formulas.
- Rewrite all door and cased-opening sizes into the left table in inches:
  `2'-0" x 6'-8"` becomes `24 x 80`.
- For many repeated doors, use an Excel formula instead of manual repeated
  typing.
- Before output, select the entered door/opening cells and check the status-bar
  sum against the takeoff count.

## Picture Guide

| Image | Rule | How to write/check it |
| --- | --- | --- |
| [26](../../assets/images/trims/int-trims-26.png) | Measure by open door symbol. | Count the actual swing/opening, not only a nearby wall label. |
| [27](../../assets/images/trims/int-trims-27.png) | Door size notation. | `2680` = 2'-6" x 8'-0". |
| [28](../../assets/images/trims/int-trims-28.png) | Double doors. | Write `(2)2680`, keeping the pair marker. |
| [29](../../assets/images/trims/int-trims-29.png) | Pocket doors. | Write `2680 Pocket`. |
| [30](../../assets/images/trims/int-trims-30.png) | Slider doors. | Write `(2)3080 Slider` or matching size/type. |
| [31](../../assets/images/trims/int-trims-31.png) | Shower glass doors. | Do not count as interior doors. |
| [32](../../assets/images/trims/int-trims-32.png) | French doors. | Keep `French` / glass-door note visible when shown. |
| [33](../../assets/images/trims/int-trims-33.png) | Bi-Fold door. | Keep `Bi-Fold` in the mark; do not flatten to a plain door. |
| [34](../../assets/images/trims/int-trims-34.png) | Cased openings. | C.O. is an opening without a door. |
| [35](../../assets/images/trims/int-trims-35.png) | Excel by level. | Enter doors and C.O. separately for each floor/level. |
| [36](../../assets/images/trims/int-trims-36.png) | Helper table copy. | Copy mark + quantity columns into the right-side helper table. |
| [37](../../assets/images/trims/int-trims-37.png) | Excel door/opening table. | Use the table to drive casing formulas. |
| [38](../../assets/images/trims/int-trims-38.png) | Rewrite into left table. | Cleanly re-enter door/opening marks before output. |
| [39](../../assets/images/trims/int-trims-39.png) | Feet to inches conversion. | `2'-0" x 6'-8"` -> `24 x 80`. |
| [40](../../assets/images/trims/int-trims-40.png) | Many repeated doors. | Use formulas to avoid missing repeated quantities. |
| [41](../../assets/images/trims/int-trims-41.png) | Sum check. | Select cells and compare status-bar sum to takeoff count. |
| [42](../../assets/images/trims/int-trims-42.png) | Excel output. | Confirm final output matches the entered table. |
| [43](../../assets/images/trims/int-trims-43.png) | Door schedule exists. | Fill from schedule first; plan view is secondary. |

## Visual Examples

<div class="kb-gallery">
  <a class="kb-gallery__item" href="../../../assets/images/trims/int-trims-26.png">
    <img src="../../../assets/images/trims/int-trims-26.png" alt="Interior door measured by open door symbol">
    <div class="kb-gallery__caption">Measure by open door</div>
  </a>
  <a class="kb-gallery__item" href="../../../assets/images/trims/int-trims-27.png">
    <img src="../../../assets/images/trims/int-trims-27.png" alt="Door size notation 2680">
    <div class="kb-gallery__caption">Size notation: 2680</div>
  </a>
  <a class="kb-gallery__item" href="../../../assets/images/trims/int-trims-28.png">
    <img src="../../../assets/images/trims/int-trims-28.png" alt="Double door notation">
    <div class="kb-gallery__caption">Double door: (2)2680</div>
  </a>
  <a class="kb-gallery__item" href="../../../assets/images/trims/int-trims-29.png">
    <img src="../../../assets/images/trims/int-trims-29.png" alt="Pocket door notation">
    <div class="kb-gallery__caption">Pocket door</div>
  </a>
  <a class="kb-gallery__item" href="../../../assets/images/trims/int-trims-30.png">
    <img src="../../../assets/images/trims/int-trims-30.png" alt="Slider door notation">
    <div class="kb-gallery__caption">Slider door</div>
  </a>
  <a class="kb-gallery__item" href="../../../assets/images/trims/int-trims-31.png">
    <img src="../../../assets/images/trims/int-trims-31.png" alt="Do not count shower glass doors">
    <div class="kb-gallery__caption">No shower glass doors</div>
  </a>
  <a class="kb-gallery__item" href="../../../assets/images/trims/int-trims-32.png">
    <img src="../../../assets/images/trims/int-trims-32.png" alt="French doors in large guest rooms">
    <div class="kb-gallery__caption">French doors</div>
  </a>
  <a class="kb-gallery__item" href="../../../assets/images/trims/int-trims-33.png">
    <img src="../../../assets/images/trims/int-trims-33.png" alt="Bi-Fold door notation">
    <div class="kb-gallery__caption">Bi-Fold</div>
  </a>
  <a class="kb-gallery__item" href="../../../assets/images/trims/int-trims-34.png">
    <img src="../../../assets/images/trims/int-trims-34.png" alt="Cased opening example">
    <div class="kb-gallery__caption">Cased opening</div>
  </a>
  <a class="kb-gallery__item" href="../../../assets/images/trims/int-trims-35.png">
    <img src="../../../assets/images/trims/int-trims-35.png" alt="Doors and cased openings entered by level">
    <div class="kb-gallery__caption">Enter by level</div>
  </a>
  <a class="kb-gallery__item" href="../../../assets/images/trims/int-trims-36.png">
    <img src="../../../assets/images/trims/int-trims-36.png" alt="Copy helper columns for Excel entry">
    <div class="kb-gallery__caption">Copy helper columns</div>
  </a>
  <a class="kb-gallery__item" href="../../../assets/images/trims/int-trims-37.png">
    <img src="../../../assets/images/trims/int-trims-37.png" alt="Doors and cased openings Excel table">
    <div class="kb-gallery__caption">Excel table</div>
  </a>
  <a class="kb-gallery__item" href="../../../assets/images/trims/int-trims-38.png">
    <img src="../../../assets/images/trims/int-trims-38.png" alt="Rewrite openings and doors into left table">
    <div class="kb-gallery__caption">Rewrite left table</div>
  </a>
  <a class="kb-gallery__item" href="../../../assets/images/trims/int-trims-39.png">
    <img src="../../../assets/images/trims/int-trims-39.png" alt="Door size inches conversion">
    <div class="kb-gallery__caption">Size conversion to inches</div>
  </a>
  <a class="kb-gallery__item" href="../../../assets/images/trims/int-trims-40.png">
    <img src="../../../assets/images/trims/int-trims-40.png" alt="Use formulas for many doors">
    <div class="kb-gallery__caption">Use formulas</div>
  </a>
  <a class="kb-gallery__item" href="../../../assets/images/trims/int-trims-41.png">
    <img src="../../../assets/images/trims/int-trims-41.png" alt="Check selected cell sum">
    <div class="kb-gallery__caption">Check sum</div>
  </a>
  <a class="kb-gallery__item" href="../../../assets/images/trims/int-trims-42.png">
    <img src="../../../assets/images/trims/int-trims-42.png" alt="Doors and openings Excel output">
    <div class="kb-gallery__caption">Excel output</div>
  </a>
  <a class="kb-gallery__item" href="../../../assets/images/trims/int-trims-43.png">
    <img src="../../../assets/images/trims/int-trims-43.png" alt="Fill from door schedule when present">
    <div class="kb-gallery__caption">Use door schedule</div>
  </a>
</div>

