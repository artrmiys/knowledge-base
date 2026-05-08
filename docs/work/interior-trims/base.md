# Base

## Count

- Wood base marked `Wd`, `Wood`, or equivalent in room schedules.
- Unit base separately from corridors, lobby, and other common areas.
- Floor-by-floor quantities when finish schedules differ.

## Exclude

- Garage: no `Baseboard`.
- Tile base when the scope asks for wood base.
- Rubber/vinyl/metal base unless specifically part of the trim scope.
- Rooms where finish schedule clearly says no wood base.

## Check

- Room schedule may have multiple finish columns; verify the base column rather
  than relying on room name.
- Bathrooms often have tile base and should be excluded from wood-base counts.
- Common areas must be separated because they may use another base type.

## Trello Rules

| Rule | What to check | Source |
| --- | --- | --- |
| No `Baseboard` behind kitchen cabinets. | Remove cabinet-backed wall segments from base formula. | [Trello](https://trello.com/c/gKHc74Lu) |
| `Baseboard` is present below windows unless the finish notes say otherwise. | Do not accidentally skip short under-window runs. | [Trello](https://trello.com/c/6Eg4OGuD) |
| No `Baseboard` where stair trim/wall junction makes it not applicable. | Check stair-to-wall intersections visually. | [Trello](https://trello.com/c/zCvVfJN2) |
| `Baseboard` is counted in toilets and shower rooms when shown by finish scope. | Verify against base material, because tile base may override wood base. | [Trello](https://trello.com/c/EZBqumHc) |
| No `Baseboard` in garage. | Do not carry the room perimeter through garage walls. | E-Wood rule |
| No `Baseboard` in non-living rooms or rooms without finish. | Exclude unfinished / service spaces unless schedule says otherwise. | [Trello](https://trello.com/c/bf2p8wqf) |
| In Excel, write all measured values into the formula. | Keep formula inspectable, not just a final number. | [Trello](https://trello.com/c/Zu0NI5a3) |
| Check material such as `TBD Base`. | Leave a visible note if material is not specified. | [Trello](https://trello.com/c/Q8YQ3KtC) |

## Takeoff Method

- Baseboard and crowns are measured by perimeter. Start at the entry door and
  trace continuously so breaks are intentional, not accidental.
- Garage perimeter is not counted for `Baseboard`.
- Bathroom / shower-room base can be separated from the main base quantity when
  review needs it.
- Typical no-base spaces: garage, mechanical/equipment rooms, crawl space, and
  other unfinished rooms.

## External Cross-Check

- General trim guides also treat base as a linear/wall-run item; this matches
  the current perimeter method.
- The finish schedule `Base` column controls the material. If it says tile,
  rubber/vinyl, metal, or `TBD`, keep that visible instead of forcing wood base.
- E-Wood rule still overrides the generic method: no base behind kitchen
  cabinets, no-finish rooms excluded, toilets/shower rooms verified by material.

## Visual Rules

<div class="kb-rule-gallery">
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-07.png">
    <img src="../../../assets/images/trims/int-trims-07.png" alt="No baseboard behind kitchen cabinets">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">No base behind kitchen cabinets</div>
      <div class="kb-rule-card__rule">Subtract cabinet-backed wall runs.</div>
      <div class="kb-rule-card__note">Do not carry base through the cabinet line just because the room perimeter continues.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-08.png">
    <img src="../../../assets/images/trims/int-trims-08.png" alt="Baseboard below windows">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Base below windows</div>
      <div class="kb-rule-card__rule">Keep under-window runs unless notes exclude them.</div>
      <div class="kb-rule-card__note">Window openings do not automatically remove the base segment below.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-09.png">
    <img src="../../../assets/images/trims/int-trims-09.png" alt="No baseboard at stair wall junction">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Stair / wall junction</div>
      <div class="kb-rule-card__rule">Stop base where stair trim makes it not applicable.</div>
      <div class="kb-rule-card__note">Add a note if the stair condition is unclear.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-10.png">
    <img src="../../../assets/images/trims/int-trims-10.png" alt="Baseboard in toilet and shower rooms">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Toilets / shower rooms</div>
      <div class="kb-rule-card__rule">Verify material before excluding.</div>
      <div class="kb-rule-card__note">Wood base counts; tile base does not count as wood base.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-11.png">
    <img src="../../../assets/images/trims/int-trims-11.png" alt="No baseboard in unfinished rooms">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">No finish / garage / service rooms</div>
      <div class="kb-rule-card__rule">No Baseboard in garage or unfinished/service spaces.</div>
      <div class="kb-rule-card__note">Exclude garage, mechanical/equipment rooms, crawl space, unfinished storage.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-12.png">
    <img src="../../../assets/images/trims/int-trims-12.png" alt="Baseboard Excel formula values">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Excel formula values</div>
      <div class="kb-rule-card__rule">Show measured segments, not only a final number.</div>
      <div class="kb-rule-card__note">The reviewer should be able to trace each value back to the plan.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-13.png">
    <img src="../../../assets/images/trims/int-trims-13.png" alt="Baseboard Excel formula continuation">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Formula continuation</div>
      <div class="kb-rule-card__rule">Keep long formulas inspectable.</div>
      <div class="kb-rule-card__note">Do not hide deductions or repeated room segments.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-14.png">
    <img src="../../../assets/images/trims/int-trims-14.png" alt="Baseboard Excel formula example">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Formula example</div>
      <div class="kb-rule-card__rule">Use visible arithmetic for perimeter runs.</div>
      <div class="kb-rule-card__note">This is the audit trail for the base output.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-15.png">
    <img src="../../../assets/images/trims/int-trims-15.png" alt="TBD Base material check">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">TBD Base</div>
      <div class="kb-rule-card__rule">Keep material uncertainty visible.</div>
      <div class="kb-rule-card__note">Write a note instead of choosing a product that is not specified.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-16.png">
    <img src="../../../assets/images/trims/int-trims-16.png" alt="Baseboard Excel output">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Baseboard Excel output</div>
      <div class="kb-rule-card__rule">Final output must match formula and material note.</div>
      <div class="kb-rule-card__note">Check line description before sending the takeoff.</div>
    </div>
  </a>
</div>

## Output Notes

If base type is unclear, keep a note such as `Base not specified in room
schedule` instead of assigning a material.

