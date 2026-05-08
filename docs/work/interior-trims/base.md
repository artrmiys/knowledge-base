# Base

## Что считать

- Wood base, помеченный `Wd`, `Wood` или аналогично в room schedules.
- Unit base отдельно от corridors, lobby и других common areas.
- Количества по floor, если finish schedules отличаются.

## Что исключать

- Garage: нет `Baseboard`.
- Tile base, если scope просит wood base.
- Rubber/vinyl/metal base, если это не отдельная часть trim scope.
- Rooms, где finish schedule прямо говорит no wood base.

## Проверить

- Room schedule может иметь несколько finish columns; проверяй column `Base`,
  а не только room name.
- Bathrooms часто имеют tile base; исключай их из wood-base counts, если так
  показано.
- Common areas отделяй, потому что там может быть другой base type.

## Правила из Trello

| Правило | Что проверить | Источник |
| --- | --- | --- |
| За kitchen cabinets нет `Baseboard`. | Убрать wall segments behind cabinets из base formula. | [Trello](https://trello.com/c/gKHc74Lu) |
| `Baseboard` под windows считается, если finish notes не говорят обратное. | Не пропускать короткие under-window runs случайно. | [Trello](https://trello.com/c/6Eg4OGuD) |
| Нет `Baseboard`, где stair trim / wall junction делает его неприменимым. | Визуально проверить stair-to-wall intersections. | [Trello](https://trello.com/c/zCvVfJN2) |
| `Baseboard` в toilets и shower rooms считается, если это показано finish scope. | Проверить base material: tile base может заменить wood base. | [Trello](https://trello.com/c/EZBqumHc) |
| В garage нет `Baseboard`. | Не вести room perimeter через garage walls. | E-Wood rule |
| В non-living rooms или rooms without finish нет `Baseboard`. | Исключать unfinished / service spaces, если schedule не говорит обратное. | [Trello](https://trello.com/c/bf2p8wqf) |
| В Excel вписывай все measured values в formula. | Formula должна быть проверяемой, не только final number. | [Trello](https://trello.com/c/Zu0NI5a3) |
| Проверяй material вроде `TBD Base`. | Оставляй видимую note, если material не указан. | [Trello](https://trello.com/c/Q8YQ3KtC) |

## Метод takeoff

- Baseboard и Crowns меряются по perimeter. Начинай от entry door и веди trace
  непрерывно, чтобы breaks были намеренными.
- Garage perimeter не считается для `Baseboard`.
- Bathroom / shower-room base можно отделить от main base quantity, если так
  проще проверить.
- Типовые no-base spaces: garage, mechanical/equipment rooms, crawl space и
  другие unfinished rooms.

## Внешняя проверка

- General trim guides тоже считают base как linear/wall-run item; это совпадает
  с текущим perimeter method.
- Finish schedule column `Base` управляет material. Если там tile,
  rubber/vinyl, metal или `TBD`, оставляй это видимым, не подставляй wood base.
- E-Wood rule важнее generic method: за kitchen cabinets base не считаем,
  no-finish rooms исключаем, toilets/shower rooms проверяем по material.

## Визуальные правила

<div class="kb-rule-gallery">
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-07.png">
    <img src="../../../assets/images/trims/int-trims-07.png" alt="No baseboard behind kitchen cabinets">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Нет base behind kitchen cabinets</div>
      <div class="kb-rule-card__rule">Вычитай cabinet-backed wall runs.</div>
      <div class="kb-rule-card__note">Не продолжай base через cabinet line только потому, что room perimeter идёт дальше.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-08.png">
    <img src="../../../assets/images/trims/int-trims-08.png" alt="Baseboard below windows">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Base below windows</div>
      <div class="kb-rule-card__rule">Оставляй under-window runs, если notes не исключают их.</div>
      <div class="kb-rule-card__note">Window openings сами по себе не убирают base segment below.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-09.png">
    <img src="../../../assets/images/trims/int-trims-09.png" alt="No baseboard at stair wall junction">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Stair / wall junction</div>
      <div class="kb-rule-card__rule">Останавливай base там, где stair trim делает его неприменимым.</div>
      <div class="kb-rule-card__note">Добавь note, если stair condition неясен.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-10.png">
    <img src="../../../assets/images/trims/int-trims-10.png" alt="Baseboard in toilet and shower rooms">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Toilets / shower rooms</div>
      <div class="kb-rule-card__rule">Перед исключением проверь material.</div>
      <div class="kb-rule-card__note">Wood base считается; tile base не считается как wood base.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-11.png">
    <img src="../../../assets/images/trims/int-trims-11.png" alt="No baseboard in unfinished rooms">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">No finish / garage / service rooms</div>
      <div class="kb-rule-card__rule">В garage и unfinished/service spaces нет Baseboard.</div>
      <div class="kb-rule-card__note">Исключай garage, mechanical/equipment rooms, crawl space, unfinished storage.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-12.png">
    <img src="../../../assets/images/trims/int-trims-12.png" alt="Baseboard Excel formula values">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Excel formula values</div>
      <div class="kb-rule-card__rule">Показывай measured segments, а не только final number.</div>
      <div class="kb-rule-card__note">Reviewer должен видеть, откуда взялось каждое значение на plan.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-13.png">
    <img src="../../../assets/images/trims/int-trims-13.png" alt="Baseboard Excel formula continuation">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Formula continuation</div>
      <div class="kb-rule-card__rule">Держи длинные formulas проверяемыми.</div>
      <div class="kb-rule-card__note">Не прячь deductions или repeated room segments.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-14.png">
    <img src="../../../assets/images/trims/int-trims-14.png" alt="Baseboard Excel formula example">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Formula example</div>
      <div class="kb-rule-card__rule">Используй видимую арифметику для perimeter runs.</div>
      <div class="kb-rule-card__note">Это audit trail для base output.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-15.png">
    <img src="../../../assets/images/trims/int-trims-15.png" alt="TBD Base material check">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">TBD Base</div>
      <div class="kb-rule-card__rule">Оставляй uncertainty по material видимой.</div>
      <div class="kb-rule-card__note">Пиши note вместо выбора product, который не указан.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../assets/images/trims/int-trims-16.png">
    <img src="../../../assets/images/trims/int-trims-16.png" alt="Baseboard Excel output">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Baseboard Excel output</div>
      <div class="kb-rule-card__rule">Final output должен совпадать с formula и material note.</div>
      <div class="kb-rule-card__note">Перед отправкой takeoff проверь line description.</div>
    </div>
  </a>
</div>

## Заметки по выводу

Если base type неясен, оставь note вроде `Base not specified in room schedule`
вместо назначения material наугад.

