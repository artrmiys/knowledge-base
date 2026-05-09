# Crown

## Правило

`Crowns` включаются, когда активен interior trim scope.

## Что считать

- Crown molding по room/area, где он показан или требуется trim scope.
- Common areas отделять от units, если finish schedule отличается.

## Проверить

- Crown может быть в finish notes, а не на plan view.
- Garage: нет `Crowns`.
- Не путай crown с exterior cornice, fascia, frieze или rake trim.
- Если trim scope есть, но crown неясен, добавь видимую note.
- Типовые no-crown spaces: garage, mechanical/equipment rooms, crawl space и
  другие rooms without finish.

## Правила из Trello

| Правило | Что проверить | Источник |
| --- | --- | --- |
| В closets нет `Crowns`. | Исключай `Closet` / `CLO.` spaces, если scope не говорит обратное. | [Trello](https://trello.com/c/Iz1T4E1L) |
| В rooms with sloped ceilings нет `Crowns`. | Следи за `slope ceiling` / sloped roof conditions. | [Trello](https://trello.com/c/a2x8EuZA) |
| В garage нет `Crowns`. | Не веди crown perimeter через garage walls. | Estimating rule |
| В rooms without finish нет `Crowns`. | Исключай unfinished areas. | [Trello](https://trello.com/c/L54HVTxD) |
| `Crowns` в bathrooms считаются, если trim scope требует это. | Не исключай bathrooms автоматически. | [Trello](https://trello.com/c/nV0U6Z32) |
| На second level считай crowns только в `Hall`, foyer и large guest rooms, где это требуется. | Держи second-floor crown logic отдельно от first-floor living areas. | [Trello](https://trello.com/c/EImvQgbn) |
| В Excel вписывай все measured values в formula. | Formula должна быть проверяемой. | [Trello](https://trello.com/c/x4SZ0PZN) |
| Проверяй material вроде `TBD Crowns`. | Оставляй видимую note, если material не указан. | [Trello](https://trello.com/c/KvJvp48a) |

## Метод takeoff

- `Crowns` меряются той же room perimeter logic, что и Baseboard.
- Garage perimeter не считается для `Crowns`.
- Каждый measured segment вписывай в Excel formula, не только final total.
- Если crown material = `TBD`, оставляй material note видимой.

## Внешняя проверка

- Crown тоже linear room-run item, но его нельзя выводить только из base.
- Перед perimeter count проверь finish schedule, ceiling notes, RCP/finish plans
  и remarks.
- Estimating exclusions остаются рабочим правилом: closets, sloped-ceiling rooms и
  no-finish rooms не считаются, если scope явно не говорит обратное.

## Визуальные правила

<div class="kb-rule-gallery">
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-17.png">
    <img src="../../../assets/images/trims/int-trims-17.png" alt="No crowns in closets">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">В closets нет Crowns</div>
      <div class="kb-rule-card__rule">Исключай <code>Closet</code> / <code>CLO.</code>, если scope прямо не включает их.</div>
      <div class="kb-rule-card__note">По умолчанию не веди crown perimeter через closet walls.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-18.png">
    <img src="../../../assets/images/trims/int-trims-18.png" alt="No crowns in slope ceiling rooms">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Нет crowns при slope ceiling</div>
      <div class="kb-rule-card__rule">Перед perimeter count проверь ceiling/roof condition.</div>
      <div class="kb-rule-card__note">Sloped ceiling condition ломает обычное crown rule.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-19.png">
    <img src="../../../assets/images/trims/int-trims-19.png" alt="Sloped ceiling crown example">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Slope ceiling example</div>
      <div class="kb-rule-card__rule">Не считай Crown только потому, что у room есть finish.</div>
      <div class="kb-rule-card__note">Если plan неясен, смотри RCP/ceiling notes.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-20.png">
    <img src="../../../assets/images/trims/int-trims-20.png" alt="No crowns in unfinished rooms">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">No finish / garage / service rooms</div>
      <div class="kb-rule-card__rule">В garage и unfinished/service spaces нет Crowns.</div>
      <div class="kb-rule-card__note">Исключай garage, mechanical/equipment rooms, crawl space, unfinished storage.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-21.png">
    <img src="../../../assets/images/trims/int-trims-21.png" alt="Crowns in bathrooms">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Bathrooms могут иметь Crowns</div>
      <div class="kb-rule-card__rule">Не исключай bathrooms автоматически.</div>
      <div class="kb-rule-card__note">Иди по finish/trim scope и material notes.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-22.png">
    <img src="../../../assets/images/trims/int-trims-22.png" alt="Second level crown locations">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Second-level Crown rule</div>
      <div class="kb-rule-card__rule">Считай только Hall, foyer и large guest rooms, если это правило применимо.</div>
      <div class="kb-rule-card__note">Держи second-floor logic отдельно от first-floor living areas.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-23.png">
    <img src="../../../assets/images/trims/int-trims-23.png" alt="Crown Excel formula values">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Crown Excel formula</div>
      <div class="kb-rule-card__rule">Каждый measured segment вписывай в formula.</div>
      <div class="kb-rule-card__note">Не прячь perimeter total без видимых run values.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-24.png">
    <img src="../../../assets/images/trims/int-trims-24.png" alt="TBD Crown material check">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">TBD Crowns</div>
      <div class="kb-rule-card__rule">Оставляй uncertainty по material видимой.</div>
      <div class="kb-rule-card__note">Не угадывай crown material, когда schedule говорит TBD.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-25.png">
    <img src="../../../assets/images/trims/int-trims-25.png" alt="Crown Excel output">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Crown Excel output</div>
      <div class="kb-rule-card__rule">Final output должен совпадать с formula и material note.</div>
      <div class="kb-rule-card__note">Перед отправкой takeoff проверь line description.</div>
    </div>
  </a>
</div>

