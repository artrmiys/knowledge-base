# Door and Window Trim

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

## External Cross-Check

| Check | What it means for takeoff | Source |
| --- | --- | --- |
| Fire-rated door is an assembly. | Keep the rating note visible; door, frame, hardware, glazing/label can matter. | [UL fire-rated doors guide](https://www.ul.com/thecodeauthority/knowledge/ul-fire-rated-doors-guide) |
| Hollow-metal fire doors need closing/latching hardware. | `F.R. S.C.` should stay in the door note; do not flatten it to a plain `2680`. | [NAAMM/HMMA checklist](https://www.naamm.org/news/31/hollow-metal-doors-and-frames-fire-rating-checklist) |
| Steel fire door specs call for positive latching and usually closers. | If the plan/schedule shows `MTL`, `HM`, `FR`, or `SC`, preserve those terms. | [Steel Door Institute](https://steeldoor.org/tips-for-specifying-fire-door-assemblies/) |
| `FRT` is treated wood, not a door fire-rating mark. | Do not mix `F.R.` door notation with `FRTW` lumber/material scope. | [American Wood Council FRTW FAQ](https://awc.org/faq/can-surface-coated-wood-products-be-approved-for-use-in-applications-where-fire-retardant-treated-wood-is-permitted/) |

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

## Visual Rules

<div class="kb-rule-gallery">
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-26.png">
    <img src="../../../assets/images/trims/int-trims-26.png" alt="Interior door measured by open door symbol">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Measure by open door symbol</div>
      <div class="kb-rule-card__rule">Count the actual swing/opening.</div>
      <div class="kb-rule-card__note">Do not count from a nearby wall note only.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-27.png">
    <img src="../../../assets/images/trims/int-trims-27.png" alt="Door size notation 2680">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Size notation: 2680</div>
      <div class="kb-rule-card__rule"><code>2680</code> = 2'-6" x 8'-0".</div>
      <div class="kb-rule-card__note">Keep size notation consistent before Excel conversion.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-28.png">
    <img src="../../../assets/images/trims/int-trims-28.png" alt="Double door notation">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Double doors</div>
      <div class="kb-rule-card__rule">Write <code>(2)2680</code>.</div>
      <div class="kb-rule-card__note">Keep the pair marker; do not flatten to one regular door.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-29.png">
    <img src="../../../assets/images/trims/int-trims-29.png" alt="Pocket door notation">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Pocket door</div>
      <div class="kb-rule-card__rule">Write <code>2680 Pocket</code>.</div>
      <div class="kb-rule-card__note">Preserve the door type in the mark.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-30.png">
    <img src="../../../assets/images/trims/int-trims-30.png" alt="Slider door notation">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Slider door</div>
      <div class="kb-rule-card__rule">Write <code>(2)3080 Slider</code> or matching size/type.</div>
      <div class="kb-rule-card__note">Keep both quantity and type.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-31.png">
    <img src="../../../assets/images/trims/int-trims-31.png" alt="Do not count shower glass doors">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Shower glass doors</div>
      <div class="kb-rule-card__rule">Do not enter as interior doors.</div>
      <div class="kb-rule-card__note">This belongs to shower/glass scope, not interior door casing.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-32.png">
    <img src="../../../assets/images/trims/int-trims-32.png" alt="French doors in large guest rooms">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">French doors</div>
      <div class="kb-rule-card__rule">Keep <code>French</code> / glass-door note visible.</div>
      <div class="kb-rule-card__note">Do not simplify to a plain interior door when the plan names the type.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-33.png">
    <img src="../../../assets/images/trims/int-trims-33.png" alt="Bi-Fold door notation">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Bi-Fold door</div>
      <div class="kb-rule-card__rule">Keep <code>Bi-Fold</code> in the mark.</div>
      <div class="kb-rule-card__note">Door type can affect review and casing notes.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-34.png">
    <img src="../../../assets/images/trims/int-trims-34.png" alt="Cased opening example">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Cased opening</div>
      <div class="kb-rule-card__rule"><code>C.O.</code> is an opening without a door.</div>
      <div class="kb-rule-card__note">Enter it on the cased-opening side, not as a door.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-35.png">
    <img src="../../../assets/images/trims/int-trims-35.png" alt="Doors and cased openings entered by level">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Enter by level</div>
      <div class="kb-rule-card__rule">Separate doors and C.O. by floor/level.</div>
      <div class="kb-rule-card__note">This keeps formulas and review output aligned.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-36.png">
    <img src="../../../assets/images/trims/int-trims-36.png" alt="Copy helper columns for Excel entry">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Copy helper columns</div>
      <div class="kb-rule-card__rule">Copy mark + quantity into the helper table.</div>
      <div class="kb-rule-card__note">The helper table drives casing formulas.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-37.png">
    <img src="../../../assets/images/trims/int-trims-37.png" alt="Doors and cased openings Excel table">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Excel door/opening table</div>
      <div class="kb-rule-card__rule">Use the table to drive casing formulas.</div>
      <div class="kb-rule-card__note">Do not leave door marks only in the plan notes.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-38.png">
    <img src="../../../assets/images/trims/int-trims-38.png" alt="Rewrite openings and doors into left table">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Rewrite into left table</div>
      <div class="kb-rule-card__rule">Cleanly re-enter door/opening marks before output.</div>
      <div class="kb-rule-card__note">This prevents half-cleaned helper data from reaching final output.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-39.png">
    <img src="../../../assets/images/trims/int-trims-39.png" alt="Door size inches conversion">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Feet to inches conversion</div>
      <div class="kb-rule-card__rule"><code>2'-0" x 6'-8"</code> becomes <code>24 x 80</code>.</div>
      <div class="kb-rule-card__note">Use inches in the formula table when required by the workbook.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-40.png">
    <img src="../../../assets/images/trims/int-trims-40.png" alt="Use formulas for many doors">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Many repeated doors</div>
      <div class="kb-rule-card__rule">Use formulas to avoid missing repeated quantities.</div>
      <div class="kb-rule-card__note">Manual repeated typing is where counts drift.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-41.png">
    <img src="../../../assets/images/trims/int-trims-41.png" alt="Check selected cell sum">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Sum check</div>
      <div class="kb-rule-card__rule">Compare selected-cell sum against takeoff count.</div>
      <div class="kb-rule-card__note">Catch missing doors before output.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-42.png">
    <img src="../../../assets/images/trims/int-trims-42.png" alt="Doors and openings Excel output">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Excel output</div>
      <div class="kb-rule-card__rule">Final output must match the entered table.</div>
      <div class="kb-rule-card__note">Review size, quantity, and note before sending.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-43.png">
    <img src="../../../assets/images/trims/int-trims-43.png" alt="Fill from door schedule when present">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Door schedule exists</div>
      <div class="kb-rule-card__rule">Fill from schedule first.</div>
      <div class="kb-rule-card__note">Plan view is secondary when schedule data is available.</div>
    </div>
  </a>
</div>

