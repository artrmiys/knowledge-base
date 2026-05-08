# Важные изменения

<figure markdown>
  ![Important changes visual map](../assets/images/reference/important-changes-map.svg)
  <figcaption>Important Changes — визуальная QA map перед output.</figcaption>
</figure>

Source board:
`https://trello.com/b/wDztpnZg/изменения-очень-важно`

Импортировано из logged-in browser session и полного Trello API export:
**75 cards** и **20 attachments**.
Это визуальная shelf для high-priority rule changes.

## Визуальные правила

| Правило / напоминание | Тема | Источник |
| --- | --- | --- |
| Suspended ceiling formula: `S*0.75*2 + S*0.75*1*0.75` in `LFT`. | Formula | [Trello](https://trello.com/c/G2Stf2Ap) |
| Balcony framing: 2-ply и 2 layers of sleepers. | Balcony / Deck | [Trello](https://trello.com/c/yccc3pHP) |
| Для roof with `AJS Rafters` считай rafters вручную вместо `Rake`, когда condition похож на exposed floor overhang. | Roof / Rake | [Trello](https://trello.com/c/Bf9qwCpI) |
| `Sound insulation` только когда insulation реально required. | Insulation | [Trello](https://trello.com/c/BZTIykI8) |
| `Ribbonboard` только для trusses. | Floor / Truss | [Trello](https://trello.com/c/pUzOwM8G) |
| Каждые `10'` считать как `blocking` для `Trusses - Bracing 2x6`. | Blocking | [Trello](https://trello.com/c/ZDDIgL2Y) |
| Если post не specified, оставь правильную видимую note вместо guessing. | Post | [Trello](https://trello.com/c/CeqrmfZv) |
| Washers: не оставляй spacing unchanged; обновляй spacing. | Anchor / Washers | [Trello](https://trello.com/c/TFIsHlji) |
| Пиши `LVL` без quotation marks. | Naming | [Trello](https://trello.com/c/vhU8cDuG) |
| Если `EWP by others`, но в floor есть один `LVL` beam, напиши note. | EWP / Notes | [Trello](https://trello.com/c/RbUsIPnE) |
| Исправляй extra spaces в material names. | Output QA | [Trello](https://trello.com/c/8uM9XNkM) |
| `Cantilevered` требует такой label. | SQFT / Label | [Trello](https://trello.com/c/TKGVrLrE) |
| Используй `precut` formula, потому что manual errors частые. | Formula / Precut | [Trello](https://trello.com/c/dM3K1XRD) |

## Текстовые правила из полного export

У этих cards не всегда были полезные screenshots, но card titles — это rule.
Держи их как QA prompts перед output.

| Правило / напоминание | Тема | Источник |
| --- | --- | --- |
| Держи `Porch Trims` в одном месте, чтобы review не был split по unrelated rows. | Porch / Deck | [Trello](https://trello.com/c/ysvvsf9o) |
| Пиши `Ledger` и `Box` отдельными rows. | Ledger / Box | [Trello](https://trello.com/c/frKKbKGO) |
| Убирай unused rows/items, кроме wall formulas, которые всё ещё drive workbook. | Output QA | [Trello](https://trello.com/c/JcZI6vlz) |
| Всегда проверяй specification и пиши note, когда material приходит from specs. | Specs / Notes | [Trello](https://trello.com/c/6UUhGGJy) |
| Разделяй `EWP Floor` и `All EWP`; не считай одно другим. | EWP | [Trello](https://trello.com/c/tm4fd98q) |
| Copy repeated areas carefully, особенно porches и decks. | QA | [Trello](https://trello.com/c/ESB3FC12) |
| `8'-1"` studs — это не `9'` precut; исправь видимые wall heights/output. | Studs / Precut | [Trello](https://trello.com/c/AR3c3a3x) |
| Не меняй местами joist count и joist length. | Joist | [Trello](https://trello.com/c/I8YQv3Qv) |
| Сначала measure, потом сразу write value. | QA | [Trello](https://trello.com/c/4NIJDE9d) |
| Для headers `(3)` = three plies; не вводи one board для triple header. | Headers | [Trello](https://trello.com/c/OtYBicSr) |
| После converting repeated hanger counts перепроверь hanger quantities тоже. | Hangers | [Trello](https://trello.com/c/PRZtikXb) |
| `Vinyl Soffits` относятся к SQFT. | SQFT / Soffit | [Trello](https://trello.com/c/1oja6xP0) |
| Если materials в отдельном specification PDF, добавь `per customer note`. | Specs / Notes | [Trello](https://trello.com/c/FaECF5m9) |
| Long 2x ceiling joists могут быть split и подразумевать supporting vertical joists. | Ceiling Joist | [Trello](https://trello.com/c/JzOsk0WD) |
| Для `Tri-Force` и beams with steel plates пиши nearest foot sizes, не inches. | Beam | [Trello](https://trello.com/c/HVOouirh) |
| Не создавай `Posts` / `Post Caps` для каждого built-up beam; только когда реальные `6x6`, `4x4` и т.д. posts called out. | Post | [Trello](https://trello.com/c/xiypSXYv) |
| `Bracing` всегда `2x4`, если detail не говорит иначе. | Bracing | [Trello](https://trello.com/c/h8RfM3yY) |
| Если дом 28' wide с dropped beam, joists могут быть длиннее 14'; проверь span labels. | Joist | [Trello](https://trello.com/c/GkDZ6tIa) |
| Пиши `Schedule` и floor labels вроде `1st`, `2nd`, `3rd`. | Output QA | [Trello](https://trello.com/c/NpMOAHXq) |
| `Cross bridging for I-joists` / `TB27`: `length * 2 * 12 / 16` pcs. | Joist / Blocking | [Trello](https://trello.com/c/xRuW48W7) |
| Для attic `EWP by others` пиши note `LVLs by others`. | EWP / Notes | [Trello](https://trello.com/c/OCcTs5F6) |
| На duplex jobs проверяй multipliers дважды; missing half a building — частая ошибка. | QA | [Trello](https://trello.com/c/dlxjgOtF) |
| Box sheathing: attic floor height добавляется только к first height. | Box Sheathing | [Trello](https://trello.com/c/8q6E009W) |
| Attic subfloor can be `extra plate + box = subfloor`. | Box / Subfloor | [Trello](https://trello.com/c/QGOJY6TC) |
| `TJI 9 1/2` does not use 360 / 560 series. | Joist | [Trello](https://trello.com/c/EfzVvi99) |
| Если `Soffit Eve Vinyl` показан, вводи его в SQFT. | SQFT / Soffit | [Trello](https://trello.com/c/FJ8pga6c) |
| Для `AJS Rafters` считай rafters вручную вместо `Rake`, когда это похоже на exposed floor overhang. | Roof / Rake | [Trello](https://trello.com/c/Bf9qwCpI) |
| `Simpson HDU4-SDS2.5`: double, когда sits on a wall at upper floors; single, когда sits on LVL/steel. | Holdowns | [Trello](https://trello.com/c/73iLEt4M) |

## Полная галерея

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
    <img src="../../assets/images/reference/important-change-04.png" alt="Sound insulation только когда требуется">
    <div class="kb-gallery__caption">04. Sound insulation только когда нужен</div>
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
    <img src="../../assets/images/reference/important-change-07.png" alt="Если post не specified">
    <div class="kb-gallery__caption">07. Если post не specified</div>
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
    <img src="../../assets/images/reference/important-change-10.png" alt="LVL без кавычек">
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
    <img src="../../assets/images/reference/important-change-14.png" alt="Используй formula для precut">
    <div class="kb-gallery__caption">14. Используй formula для precut</div>
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
    <img src="../../assets/images/reference/important-change-19.png" alt="Precut formula duplicate source">
    <div class="kb-gallery__caption">19. Используй formula для precut (older card)</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/reference/important-change-20.png">
    <img src="../../assets/images/reference/important-change-20.png" alt="LVL без кавычек duplicate source">
    <div class="kb-gallery__caption">20. Write `LVL` without quotes (older card)</div>
  </a>
</div>

## Raw import

Raw markdown copies are stored in:

`imports/live-sources/trello-important-changes-full/pages/`

