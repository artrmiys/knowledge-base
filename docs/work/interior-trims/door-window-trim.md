# Door and Window Trim

## Door Trim

- Unit entry doors могут быть fire-rated; в door takeoff это нужно подписывать
  явно, но hardware numbers для trim обычно не нужны.
- Interior door jamb trim может использовать casing divided by 2, если это
  локальный метод.
- Common-area doors отделяй от unit doors, если trim type отличается.

## Window Trim

- Casing/stool/apron считай только если они есть в finish schedule или details.
- Не применяй exterior window trim logic к interior trims без проверки scope.

## Проверить

- Door/window trim может быть спрятан в finish schedules, interior elevations
  или details, а не на framing sheets.
- Trim notes держи отдельно от blocking/jamb framing notes.
- Если schedule указывает manufacturer или special product, оставляй это в
  note, не превращай opening в generic size.

## Door notation

| Пример | Значение | Как использовать |
| --- | --- | --- |
| `2680` | 2'-6" wide x 8'-0" high | Обычная single interior door |
| `(2)2680` | Две doors, каждая 2'-6" x 8'-0" | Double door pair |
| `2680 Pocket` | Pocket door, 2'-6" x 8'-0" | Оставляй `Pocket` в mark |
| `(2)3080 Slider` | Две 3'-0" x 8'-0" sliding leaves | Оставляй и quantity, и `Slider` |
| `2680 Metal F.R. S.C.` | Metal, fire-rated, self-closing door | Garage/mechanical/fire-rated condition |
| `4080 C.O.` | 4'-0" x 8'-0" cased opening | Вводить как cased opening, не как door |

`F.R.` на door значит **fire-rated**. Не путай это с `FRT` lumber /
fire-retardant-treated framing material.

## Внешняя проверка

| Проверка | Что значит для takeoff | Источник |
| --- | --- | --- |
| Fire-rated door is an assembly. | Оставляй rating note видимой: door, frame, hardware, glazing/label могут быть важны. | [UL fire-rated doors guide](https://www.ul.com/thecodeauthority/knowledge/ul-fire-rated-doors-guide) |
| Hollow-metal fire doors need closing/latching hardware. | `F.R. S.C.` должен остаться в door note; не своди всё к простому `2680`. | [NAAMM/HMMA checklist](https://www.naamm.org/news/31/hollow-metal-doors-and-frames-fire-rating-checklist) |
| Steel fire door specs call for positive latching and usually closers. | Если plan/schedule показывает `MTL`, `HM`, `FR` или `SC`, сохраняй эти terms. | [Steel Door Institute](https://steeldoor.org/tips-for-specifying-fire-door-assemblies/) |
| `FRT` is treated wood, not a door fire-rating mark. | Не смешивай `F.R.` door notation с `FRTW` lumber/material scope. | [American Wood Council FRTW FAQ](https://awc.org/faq/can-surface-coated-wood-products-be-approved-for-use-in-applications-where-fire-retardant-treated-wood-is-permitted/) |

## Правила из Trello

| Правило | Что проверить | Источник |
| --- | --- | --- |
| Interior doors считай по open door symbol. | Считать настоящий door swing/opening, а не nearby wall notes. | [Trello](https://trello.com/c/IZ2sNLWl) |
| Door size `2680` значит width `2'-6"` и height `8'-0"`. | Перед Excel conversion держи size notation одинаковой. | [Trello](https://trello.com/c/hCU71d7H) |
| Double doors пишутся как `(2)2680`. | Оставляй pair marker видимым. | [Trello](https://trello.com/c/eQgpc2fU) |
| Pocket doors пишутся как `2680 Pocket`. | Сохраняй `Pocket` note. | [Trello](https://trello.com/c/YhlqMraY) |
| Slider doors пишутся как `(2)3080 Slider`. | Сохраняй и quantity, и type. | [Trello](https://trello.com/c/sgMGFbJN) |
| Garage/mechanical metal doors могут быть `F.R S.C.`. | Отмечай fire-rated и self-close conditions. | [Trello](https://trello.com/c/aFiv0hIM) |
| Glass shower doors не вводятся как interior doors. | Исключай shower glass doors из interior door count. | [Trello](https://trello.com/c/43ZyybeD) |
| Large guest rooms могут иметь `French doors`. | Оставляй glass/French door note видимой. | [Trello](https://trello.com/c/cb8EWYy1) |
| `Cased Openings` — openings without doors. | Cased openings пиши отдельно от doors. | [Trello](https://trello.com/c/GIxtgKCI) |
| `4080 C.O.` — cased-opening notation. | Convert и вводи на стороне cased-opening, не doors. | [Trello](https://trello.com/c/XYT9cr0q) |
| Interior doors и cased openings вводятся для каждого level в Excel. | Floors разделить до trim formulas. | [Trello](https://trello.com/c/Zy0M8kcH) |
| Если есть door schedule, заполняй из schedule. | Schedule data лучше, чем ручной plan-only entry. | [Trello](https://trello.com/c/C0LHSgXl) |

## Ввод в Excel

- После ввода всех doors/openings скопируй opening mark и quantity columns в
  right-side Excel helper table для casing formulas.
- Все door и cased-opening sizes перепиши в left table в inches:
  `2'-0" x 6'-8"` становится `24 x 80`.
- Для многих repeated doors используй Excel formula вместо ручного repeated
  typing.
- Перед output выдели введённые door/opening cells и сравни status-bar sum с
  takeoff count.

## Визуальные правила

<div class="kb-rule-gallery">
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-26.png">
    <img src="../../../assets/images/trims/int-trims-26.png" alt="Interior door measured by open door symbol">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Считать по open door symbol</div>
      <div class="kb-rule-card__rule">Считай настоящий swing/opening.</div>
      <div class="kb-rule-card__note">Не считай только по nearby wall note.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-27.png">
    <img src="../../../assets/images/trims/int-trims-27.png" alt="Door size notation 2680">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Size notation: 2680</div>
      <div class="kb-rule-card__rule"><code>2680</code> = 2'-6" x 8'-0".</div>
      <div class="kb-rule-card__note">Перед Excel conversion держи size notation одинаковой.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-28.png">
    <img src="../../../assets/images/trims/int-trims-28.png" alt="Double door notation">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Double doors</div>
      <div class="kb-rule-card__rule">Пиши <code>(2)2680</code>.</div>
      <div class="kb-rule-card__note">Оставляй pair marker; не своди к одной regular door.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-29.png">
    <img src="../../../assets/images/trims/int-trims-29.png" alt="Pocket door notation">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Pocket door</div>
      <div class="kb-rule-card__rule">Пиши <code>2680 Pocket</code>.</div>
      <div class="kb-rule-card__note">Сохраняй door type в mark.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-30.png">
    <img src="../../../assets/images/trims/int-trims-30.png" alt="Slider door notation">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Slider door</div>
      <div class="kb-rule-card__rule">Пиши <code>(2)3080 Slider</code> или matching size/type.</div>
      <div class="kb-rule-card__note">Оставляй и quantity, и type.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-31.png">
    <img src="../../../assets/images/trims/int-trims-31.png" alt="Shower glass doors не считать как interior doors">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Shower glass doors</div>
      <div class="kb-rule-card__rule">Не вводи как interior doors.</div>
      <div class="kb-rule-card__note">Это shower/glass scope, а не interior door casing.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-32.png">
    <img src="../../../assets/images/trims/int-trims-32.png" alt="French doors in large guest rooms">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">French doors</div>
      <div class="kb-rule-card__rule">Оставляй <code>French</code> / glass-door note видимой.</div>
      <div class="kb-rule-card__note">Не упрощай до plain interior door, если plan называет type.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-33.png">
    <img src="../../../assets/images/trims/int-trims-33.png" alt="Bi-Fold door notation">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Bi-Fold door</div>
      <div class="kb-rule-card__rule">Оставляй <code>Bi-Fold</code> в mark.</div>
      <div class="kb-rule-card__note">Door type может влиять на review и casing notes.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-34.png">
    <img src="../../../assets/images/trims/int-trims-34.png" alt="Cased opening example">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Cased opening</div>
      <div class="kb-rule-card__rule"><code>C.O.</code> — opening without a door.</div>
      <div class="kb-rule-card__note">Вводи на стороне cased-opening, не как door.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-35.png">
    <img src="../../../assets/images/trims/int-trims-35.png" alt="Doors and cased openings entered by level">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Ввод по level</div>
      <div class="kb-rule-card__rule">Разделяй doors и C.O. по floor/level.</div>
      <div class="kb-rule-card__note">Так formulas и review output остаются согласованными.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-36.png">
    <img src="../../../assets/images/trims/int-trims-36.png" alt="Copy helper columns for Excel entry">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Копировать helper columns</div>
      <div class="kb-rule-card__rule">Копируй mark + quantity в helper table.</div>
      <div class="kb-rule-card__note">Helper table управляет casing formulas.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-37.png">
    <img src="../../../assets/images/trims/int-trims-37.png" alt="Doors and cased openings Excel table">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Excel door/opening table</div>
      <div class="kb-rule-card__rule">Используй table для casing formulas.</div>
      <div class="kb-rule-card__note">Не оставляй door marks только в plan notes.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-38.png">
    <img src="../../../assets/images/trims/int-trims-38.png" alt="Rewrite openings and doors into left table">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Переписать в left table</div>
      <div class="kb-rule-card__rule">Перед output чисто перенеси door/opening marks.</div>
      <div class="kb-rule-card__note">Так half-cleaned helper data не попадёт в final output.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-39.png">
    <img src="../../../assets/images/trims/int-trims-39.png" alt="Door size inches conversion">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Feet to inches conversion</div>
      <div class="kb-rule-card__rule"><code>2'-0" x 6'-8"</code> становится <code>24 x 80</code>.</div>
      <div class="kb-rule-card__note">Используй inches в formula table, если этого требует workbook.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-40.png">
    <img src="../../../assets/images/trims/int-trims-40.png" alt="Formulas для many doors">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Много repeated doors</div>
      <div class="kb-rule-card__rule">Используй formulas, чтобы не потерять repeated quantities.</div>
      <div class="kb-rule-card__note">Manual repeated typing — частое место, где counts начинают расходиться.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-41.png">
    <img src="../../../assets/images/trims/int-trims-41.png" alt="Проверка selected cell sum">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Sum check</div>
      <div class="kb-rule-card__rule">Сравни selected-cell sum с takeoff count.</div>
      <div class="kb-rule-card__note">Так ловятся missing doors до output.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-42.png">
    <img src="../../../assets/images/trims/int-trims-42.png" alt="Doors and openings Excel output">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Excel output</div>
      <div class="kb-rule-card__rule">Final output должен совпадать с entered table.</div>
      <div class="kb-rule-card__note">Перед отправкой проверь size, quantity и note.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-43.png">
    <img src="../../../assets/images/trims/int-trims-43.png" alt="Заполнять из door schedule, если он есть">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Есть door schedule</div>
      <div class="kb-rule-card__rule">Сначала заполняй из schedule.</div>
      <div class="kb-rule-card__note">Plan view вторичен, если доступна schedule data.</div>
    </div>
  </a>
</div>

