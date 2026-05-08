# Important Changes

<figure markdown>
  ![Important changes visual map](../assets/images/reference/important-changes-map.svg)
  <figcaption>Important Changes — use as a visual QA map before output.</figcaption>
</figure>

Source board:
`https://trello.com/b/wDztpnZg/изменения-очень-важно`

Imported from the logged-in browser session and full Trello API export:
**75 cards** and **20 attachments**.
This page is the visual shelf for high-priority rule changes.

## Visual Rules

| Rule / reminder | Topic | Source |
| --- | --- | --- |
| Suspended ceiling formula: `S*0.75*2 + S*0.75*1*0.75` in `LFT`. | Formula | [Trello](https://trello.com/c/G2Stf2Ap) |
| Balcony framing: 2-ply and 2 layers of sleepers. | Balcony / Deck | [Trello](https://trello.com/c/yccc3pHP) |
| For roof with `AJS Rafters`, count rafters manually instead of `Rake` when the condition is like an exposed floor overhang. | Roof / Rake | [Trello](https://trello.com/c/Bf9qwCpI) |
| `Sound insulation` only when insulation is actually required. | Insulation | [Trello](https://trello.com/c/BZTIykI8) |
| `Ribbonboard` only for trusses. | Floor / Truss | [Trello](https://trello.com/c/pUzOwM8G) |
| Count every `10'` as `blocking` for `Trusses - Bracing 2x6`. | Blocking | [Trello](https://trello.com/c/ZDDIgL2Y) |
| If a post is not specified, leave the correct visible note instead of guessing. | Post | [Trello](https://trello.com/c/CeqrmfZv) |
| Washers: do not leave the spacing unchanged; update the spacing. | Anchor / Washers | [Trello](https://trello.com/c/TFIsHlji) |
| Write `LVL` without quotation marks. | Naming | [Trello](https://trello.com/c/vhU8cDuG) |
| If `EWP by others` but one `LVL` beam is in the floor, write a note. | EWP / Notes | [Trello](https://trello.com/c/RbUsIPnE) |
| Fix extra spaces in material names. | Output QA | [Trello](https://trello.com/c/8uM9XNkM) |
| `Cantilevered` needs that label. | SQFT / Label | [Trello](https://trello.com/c/TKGVrLrE) |
| Use the `precut` formula because manual errors are common. | Formula / Precut | [Trello](https://trello.com/c/dM3K1XRD) |

## Text Rules From Full Export

These cards did not always have useful screenshots, but the card titles are
the rule. Keep them as QA prompts before output.

| Rule / reminder | Topic | Source |
| --- | --- | --- |
| Keep `Porch Trims` in one place so review is not split across unrelated rows. | Porch / Deck | [Trello](https://trello.com/c/ysvvsf9o) |
| Write `Ledger` and `Box` as separate rows. | Ledger / Box | [Trello](https://trello.com/c/frKKbKGO) |
| Remove unused rows/items, except wall formulas that still drive the workbook. | Output QA | [Trello](https://trello.com/c/JcZI6vlz) |
| Always check the specification and write a note when material comes from specs. | Specs / Notes | [Trello](https://trello.com/c/6UUhGGJy) |
| Distinguish `EWP Floor` from `All EWP`; do not treat one as the other. | EWP | [Trello](https://trello.com/c/tm4fd98q) |
| Copy repeated areas carefully, especially porches and decks. | QA | [Trello](https://trello.com/c/ESB3FC12) |
| `8'-1"` studs are not `9'` precut; fix the visible wall heights/output. | Studs / Precut | [Trello](https://trello.com/c/AR3c3a3x) |
| Do not swap joist count and joist length. | Joist | [Trello](https://trello.com/c/I8YQv3Qv) |
| Measure first, then write the value immediately. | QA | [Trello](https://trello.com/c/4NIJDE9d) |
| For headers, `(3)` means three plies; do not enter one board for a triple header. | Headers | [Trello](https://trello.com/c/OtYBicSr) |
| After converting repeated hanger counts, re-check hanger quantities too. | Hangers | [Trello](https://trello.com/c/PRZtikXb) |
| `Vinyl Soffits` belong in SQFT. | SQFT / Soffit | [Trello](https://trello.com/c/1oja6xP0) |
| If materials are in a separate specification PDF, add `per customer note`. | Specs / Notes | [Trello](https://trello.com/c/FaECF5m9) |
| Long 2x ceiling joists may be split and imply supporting vertical joists. | Ceiling Joist | [Trello](https://trello.com/c/JzOsk0WD) |
| For `Tri-Force` and beams with steel plates, write nearest foot sizes, not inches. | Beam | [Trello](https://trello.com/c/HVOouirh) |
| Do not create `Posts` / `Post Caps` for every built-up beam; only when actual `6x6`, `4x4`, etc. posts are called out. | Post | [Trello](https://trello.com/c/xiypSXYv) |
| `Bracing` is always `2x4` unless a detail says otherwise. | Bracing | [Trello](https://trello.com/c/h8RfM3yY) |
| If a 28' wide house has a dropped beam, joists may be longer than 14'; verify span labels. | Joist | [Trello](https://trello.com/c/GkDZ6tIa) |
| Use the spelling `Schedule` and floor labels like `1st`, `2nd`, `3rd`. | Output QA | [Trello](https://trello.com/c/NpMOAHXq) |
| `Cross bridging for I-joists` / `TB27`: `length * 2 * 12 / 16` pcs. | Joist / Blocking | [Trello](https://trello.com/c/xRuW48W7) |
| For attic `EWP by others`, write note `LVLs by others`. | EWP / Notes | [Trello](https://trello.com/c/OCcTs5F6) |
| On duplex jobs, check multipliers twice; missing half a building is a common failure. | QA | [Trello](https://trello.com/c/dlxjgOtF) |
| Box sheathing: attic floor height is added only to the first height. | Box Sheathing | [Trello](https://trello.com/c/8q6E009W) |
| Attic subfloor can be `extra plate + box = subfloor`. | Box / Subfloor | [Trello](https://trello.com/c/QGOJY6TC) |
| `TJI 9 1/2` does not use 360 / 560 series. | Joist | [Trello](https://trello.com/c/EfzVvi99) |
| If `Soffit Eve Vinyl` is shown, enter it in SQFT. | SQFT / Soffit | [Trello](https://trello.com/c/FJ8pga6c) |
| For `AJS Rafters`, count rafters manually instead of `Rake` when it behaves like an exposed floor overhang. | Roof / Rake | [Trello](https://trello.com/c/Bf9qwCpI) |
| `Simpson HDU4-SDS2.5`: double when it sits on a wall at upper floors; single when it sits on LVL/steel. | Holdowns | [Trello](https://trello.com/c/73iLEt4M) |

## Full Gallery

<div class="kb-gallery">
  <a class="kb-gallery__item" href="../../assets/images/reference/important-change-01.png">
    <img src="../../assets/images/reference/important-change-01.png" alt="Suspended ceiling formula">
    <div class="kb-gallery__caption">01. Suspended ceiling formula</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/reference/important-change-02.png">
    <img src="../../assets/images/reference/important-change-02.png" alt="Balcony framing sleepers">
    <div class="kb-gallery__caption">02. Balcony framing / sleepers</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/reference/important-change-03.png">
    <img src="../../assets/images/reference/important-change-03.png" alt="AJS rafters roof rule">
    <div class="kb-gallery__caption">03. AJS Rafters: manual rafters</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/reference/important-change-04.png">
    <img src="../../assets/images/reference/important-change-04.png" alt="Sound insulation only when required">
    <div class="kb-gallery__caption">04. Sound insulation only when needed</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/reference/important-change-05.png">
    <img src="../../assets/images/reference/important-change-05.png" alt="Ribbonboard only for trusses">
    <div class="kb-gallery__caption">05. Ribbonboard only for trusses</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/reference/important-change-06.png">
    <img src="../../assets/images/reference/important-change-06.png" alt="Truss bracing blocking every ten feet">
    <div class="kb-gallery__caption">06. Truss bracing blocking every 10'</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/reference/important-change-07.png">
    <img src="../../assets/images/reference/important-change-07.png" alt="If post is not specified">
    <div class="kb-gallery__caption">07. If post is not specified</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/reference/important-change-08.png">
    <img src="../../assets/images/reference/important-change-08.png" alt="Important change screenshot">
    <div class="kb-gallery__caption">08. 20.10.21 screenshot</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/reference/important-change-09.png">
    <img src="../../assets/images/reference/important-change-09.png" alt="Washers spacing update">
    <div class="kb-gallery__caption">09. Washers: update spacing</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/reference/important-change-10.png">
    <img src="../../assets/images/reference/important-change-10.png" alt="Write LVL without quotes">
    <div class="kb-gallery__caption">10. Write `LVL` without quotes</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/reference/important-change-11.png">
    <img src="../../assets/images/reference/important-change-11.png" alt="EWP by others with LVL note">
    <div class="kb-gallery__caption">11. EWP by others + LVL note</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/reference/important-change-12.png">
    <img src="../../assets/images/reference/important-change-12.png" alt="Fix spaces in material names">
    <div class="kb-gallery__caption">12. Fix material-name spacing</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/reference/important-change-13.png">
    <img src="../../assets/images/reference/important-change-13.png" alt="Cantilevered label">
    <div class="kb-gallery__caption">13. Cantilevered label</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/reference/important-change-14.png">
    <img src="../../assets/images/reference/important-change-14.png" alt="Use formula for precut">
    <div class="kb-gallery__caption">14. Use formula for precut</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/reference/important-change-15.png">
    <img src="../../assets/images/reference/important-change-15.png" alt="Imported image rule">
    <div class="kb-gallery__caption">15. Imported image rule</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/reference/important-change-16.png">
    <img src="../../assets/images/reference/important-change-16.png" alt="Imported image rule">
    <div class="kb-gallery__caption">16. Imported image rule</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/reference/important-change-17.png">
    <img src="../../assets/images/reference/important-change-17.png" alt="EWP by others with LVL note duplicate source">
    <div class="kb-gallery__caption">17. EWP by others + LVL note (older card)</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/reference/important-change-18.png">
    <img src="../../assets/images/reference/important-change-18.png" alt="Fix material name spaces duplicate source">
    <div class="kb-gallery__caption">18. Fix material-name spacing (older card)</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/reference/important-change-19.png">
    <img src="../../assets/images/reference/important-change-19.png" alt="Use precut formula duplicate source">
    <div class="kb-gallery__caption">19. Use formula for precut (older card)</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/reference/important-change-20.png">
    <img src="../../assets/images/reference/important-change-20.png" alt="Write LVL without quotes duplicate source">
    <div class="kb-gallery__caption">20. Write `LVL` without quotes (older card)</div>
  </a>
</div>

## Raw Import

Raw markdown copies are stored in:

`imports/live-sources/trello-important-changes-full/pages/`

