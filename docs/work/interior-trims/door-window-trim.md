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

<details class="kb-figures kb-figures--rows" open>
  <summary>Скрыть 18 правил с иллюстрациями</summary>
  <figure class="kb-figure-row">
    <figcaption class="kb-figure-row__text">
      <div class="kb-figure-row__title">Считать по open door symbol</div>
      <div class="kb-figure-row__rule">Считай настоящий swing/opening.</div>
      <div class="kb-figure-row__note">Не считай только по nearby wall note.</div>
    </figcaption>
    <a class="kb-figure-row__image" href="../../../assets/images/trims/int-trims-26.png" target="_blank" rel="noopener"><img src="../../../assets/images/trims/int-trims-26.png" alt="Interior door measured by open door symbol" loading="lazy"></a>
  </figure>
  <figure class="kb-figure-row">
    <figcaption class="kb-figure-row__text">
      <div class="kb-figure-row__title">Size notation: 2680</div>
      <div class="kb-figure-row__rule"><code>2680</code> = 2'-6" x 8'-0".</div>
      <div class="kb-figure-row__note">Перед Excel conversion держи size notation одинаковой.</div>
    </figcaption>
    <a class="kb-figure-row__image" href="../../../assets/images/trims/int-trims-27.png" target="_blank" rel="noopener"><img src="../../../assets/images/trims/int-trims-27.png" alt="Door size notation 2680" loading="lazy"></a>
  </figure>
  <figure class="kb-figure-row">
    <figcaption class="kb-figure-row__text">
      <div class="kb-figure-row__title">Double doors</div>
      <div class="kb-figure-row__rule">Пиши <code>(2)2680</code>.</div>
      <div class="kb-figure-row__note">Оставляй pair marker; не своди к одной regular door.</div>
    </figcaption>
    <a class="kb-figure-row__image" href="../../../assets/images/trims/int-trims-28.png" target="_blank" rel="noopener"><img src="../../../assets/images/trims/int-trims-28.png" alt="Double door notation" loading="lazy"></a>
  </figure>
  <figure class="kb-figure-row">
    <figcaption class="kb-figure-row__text">
      <div class="kb-figure-row__title">Pocket door</div>
      <div class="kb-figure-row__rule">Пиши <code>2680 Pocket</code>.</div>
      <div class="kb-figure-row__note">Сохраняй door type в mark.</div>
    </figcaption>
    <a class="kb-figure-row__image" href="../../../assets/images/trims/int-trims-29.png" target="_blank" rel="noopener"><img src="../../../assets/images/trims/int-trims-29.png" alt="Pocket door notation" loading="lazy"></a>
  </figure>
  <figure class="kb-figure-row">
    <figcaption class="kb-figure-row__text">
      <div class="kb-figure-row__title">Slider door</div>
      <div class="kb-figure-row__rule">Пиши <code>(2)3080 Slider</code> или matching size/type.</div>
      <div class="kb-figure-row__note">Оставляй и quantity, и type.</div>
    </figcaption>
    <a class="kb-figure-row__image" href="../../../assets/images/trims/int-trims-30.png" target="_blank" rel="noopener"><img src="../../../assets/images/trims/int-trims-30.png" alt="Slider door notation" loading="lazy"></a>
  </figure>
  <figure class="kb-figure-row">
    <figcaption class="kb-figure-row__text">
      <div class="kb-figure-row__title">Shower glass doors</div>
      <div class="kb-figure-row__rule">Не вводи как interior doors.</div>
      <div class="kb-figure-row__note">Это shower/glass scope, а не interior door casing.</div>
    </figcaption>
    <a class="kb-figure-row__image" href="../../../assets/images/trims/int-trims-31.png" target="_blank" rel="noopener"><img src="../../../assets/images/trims/int-trims-31.png" alt="Shower glass doors не считать как interior doors" loading="lazy"></a>
  </figure>
  <figure class="kb-figure-row">
    <figcaption class="kb-figure-row__text">
      <div class="kb-figure-row__title">French doors</div>
      <div class="kb-figure-row__rule">Оставляй <code>French</code> / glass-door note видимой.</div>
      <div class="kb-figure-row__note">Не упрощай до plain interior door, если plan называет type.</div>
    </figcaption>
    <a class="kb-figure-row__image" href="../../../assets/images/trims/int-trims-32.png" target="_blank" rel="noopener"><img src="../../../assets/images/trims/int-trims-32.png" alt="French doors in large guest rooms" loading="lazy"></a>
  </figure>
  <figure class="kb-figure-row">
    <figcaption class="kb-figure-row__text">
      <div class="kb-figure-row__title">Bi-Fold door</div>
      <div class="kb-figure-row__rule">Оставляй <code>Bi-Fold</code> в mark.</div>
      <div class="kb-figure-row__note">Door type может влиять на review и casing notes.</div>
    </figcaption>
    <a class="kb-figure-row__image" href="../../../assets/images/trims/int-trims-33.png" target="_blank" rel="noopener"><img src="../../../assets/images/trims/int-trims-33.png" alt="Bi-Fold door notation" loading="lazy"></a>
  </figure>
  <figure class="kb-figure-row">
    <figcaption class="kb-figure-row__text">
      <div class="kb-figure-row__title">Cased opening</div>
      <div class="kb-figure-row__rule"><code>C.O.</code> — opening without a door.</div>
      <div class="kb-figure-row__note">Вводи на стороне cased-opening, не как door.</div>
    </figcaption>
    <a class="kb-figure-row__image" href="../../../assets/images/trims/int-trims-34.png" target="_blank" rel="noopener"><img src="../../../assets/images/trims/int-trims-34.png" alt="Cased opening example" loading="lazy"></a>
  </figure>
  <figure class="kb-figure-row">
    <figcaption class="kb-figure-row__text">
      <div class="kb-figure-row__title">Ввод по level</div>
      <div class="kb-figure-row__rule">Разделяй doors и C.O. по floor/level.</div>
      <div class="kb-figure-row__note">Так formulas и review output остаются согласованными.</div>
    </figcaption>
    <a class="kb-figure-row__image" href="../../../assets/images/trims/int-trims-35.png" target="_blank" rel="noopener"><img src="../../../assets/images/trims/int-trims-35.png" alt="Doors and cased openings entered by level" loading="lazy"></a>
  </figure>
  <figure class="kb-figure-row">
    <figcaption class="kb-figure-row__text">
      <div class="kb-figure-row__title">Копировать helper columns</div>
      <div class="kb-figure-row__rule">Копируй mark + quantity в helper table.</div>
      <div class="kb-figure-row__note">Helper table управляет casing formulas.</div>
    </figcaption>
    <a class="kb-figure-row__image" href="../../../assets/images/trims/int-trims-36.png" target="_blank" rel="noopener"><img src="../../../assets/images/trims/int-trims-36.png" alt="Copy helper columns for Excel entry" loading="lazy"></a>
  </figure>
  <figure class="kb-figure-row">
    <figcaption class="kb-figure-row__text">
      <div class="kb-figure-row__title">Excel door/opening table</div>
      <div class="kb-figure-row__rule">Используй table для casing formulas.</div>
      <div class="kb-figure-row__note">Не оставляй door marks только в plan notes.</div>
    </figcaption>
    <a class="kb-figure-row__image" href="../../../assets/images/trims/int-trims-37.png" target="_blank" rel="noopener"><img src="../../../assets/images/trims/int-trims-37.png" alt="Doors and cased openings Excel table" loading="lazy"></a>
  </figure>
  <figure class="kb-figure-row">
    <figcaption class="kb-figure-row__text">
      <div class="kb-figure-row__title">Переписать в left table</div>
      <div class="kb-figure-row__rule">Перед output чисто перенеси door/opening marks.</div>
      <div class="kb-figure-row__note">Так half-cleaned helper data не попадёт в final output.</div>
    </figcaption>
    <a class="kb-figure-row__image" href="../../../assets/images/trims/int-trims-38.png" target="_blank" rel="noopener"><img src="../../../assets/images/trims/int-trims-38.png" alt="Rewrite openings and doors into left table" loading="lazy"></a>
  </figure>
  <figure class="kb-figure-row">
    <figcaption class="kb-figure-row__text">
      <div class="kb-figure-row__title">Feet to inches conversion</div>
      <div class="kb-figure-row__rule"><code>2'-0" x 6'-8"</code> становится <code>24 x 80</code>.</div>
      <div class="kb-figure-row__note">Используй inches в formula table, если этого требует workbook.</div>
    </figcaption>
    <a class="kb-figure-row__image" href="../../../assets/images/trims/int-trims-39.png" target="_blank" rel="noopener"><img src="../../../assets/images/trims/int-trims-39.png" alt="Door size inches conversion" loading="lazy"></a>
  </figure>
  <figure class="kb-figure-row">
    <figcaption class="kb-figure-row__text">
      <div class="kb-figure-row__title">Много repeated doors</div>
      <div class="kb-figure-row__rule">Используй formulas, чтобы не потерять repeated quantities.</div>
      <div class="kb-figure-row__note">Manual repeated typing — частое место, где counts начинают расходиться.</div>
    </figcaption>
    <a class="kb-figure-row__image" href="../../../assets/images/trims/int-trims-40.png" target="_blank" rel="noopener"><img src="../../../assets/images/trims/int-trims-40.png" alt="Formulas для many doors" loading="lazy"></a>
  </figure>
  <figure class="kb-figure-row">
    <figcaption class="kb-figure-row__text">
      <div class="kb-figure-row__title">Sum check</div>
      <div class="kb-figure-row__rule">Сравни selected-cell sum с takeoff count.</div>
      <div class="kb-figure-row__note">Так ловятся missing doors до output.</div>
    </figcaption>
    <a class="kb-figure-row__image" href="../../../assets/images/trims/int-trims-41.png" target="_blank" rel="noopener"><img src="../../../assets/images/trims/int-trims-41.png" alt="Проверка selected cell sum" loading="lazy"></a>
  </figure>
  <figure class="kb-figure-row">
    <figcaption class="kb-figure-row__text">
      <div class="kb-figure-row__title">Excel output</div>
      <div class="kb-figure-row__rule">Final output должен совпадать с entered table.</div>
      <div class="kb-figure-row__note">Перед отправкой проверь size, quantity и note.</div>
    </figcaption>
    <a class="kb-figure-row__image" href="../../../assets/images/trims/int-trims-42.png" target="_blank" rel="noopener"><img src="../../../assets/images/trims/int-trims-42.png" alt="Doors and openings Excel output" loading="lazy"></a>
  </figure>
  <figure class="kb-figure-row">
    <figcaption class="kb-figure-row__text">
      <div class="kb-figure-row__title">Есть door schedule</div>
      <div class="kb-figure-row__rule">Сначала заполняй из schedule.</div>
      <div class="kb-figure-row__note">Plan view вторичен, если доступна schedule data.</div>
    </figcaption>
    <a class="kb-figure-row__image" href="../../../assets/images/trims/int-trims-43.png" target="_blank" rel="noopener"><img src="../../../assets/images/trims/int-trims-43.png" alt="Заполнять из door schedule, если он есть" loading="lazy"></a>
  </figure>
</details>

