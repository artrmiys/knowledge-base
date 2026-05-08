# Советы и важные вещи

Ключевая страница wiki: правила, собранные из реальных правок и фидбэка по
проектам. Многих из этих вещей нет в общих гайдах по estimating — это локальная
память команды.

## Rim Board

| Ошибка | Как правильно |
| --- | --- |
| `1-3/4 LVL Rim`, когда LVL не указан | `11-7/8" Rim` или product с пометкой assumed |
| Rim разбит на 16' pieces | Держать rim в LFT с factor 1.05 |

- Если LSL указан, пиши `11-7/8" LSL Rim`.
- `1-3/4 LVL Rim` используется только когда к нему что-то крепится for strength,
  например deck или corridor frame.
- Rim нужен и at roof TJI, не только на floors.

## Blocking

- Walls 10' и выше требуют two rows of blocking.
- Blocking остаётся в LFT, если output прямо не требует pieces.
- Для framing elements вроде drywall blocking, rim и upper walls используй 10%
  waste.
- Для top chord bearing trusses не добавляй 2x4 ribbon board; используй
  blocking between trusses, часто `(2) 2x6`.

## FRT

| Элемент | Правило |
| --- | --- |
| Exterior blocking | FRT, если exterior wall material = FRT |
| Parapets | FRT, если exterior walls = FRT |
| Subfloor perimeter | Проверить 2' или 4' FRT perimeter notes |
| Demising shear wall sheathing | Regular sheathing, если schedule не говорит FRT |
| Stair / CMU two-hour walls | Часто FRT; проверять details |

## DHU / DGU vs ITS

- DHU/DGU только там, где joists hang over firewall conditions at stairs,
  elevators или shafts.
- Regular demising conditions, где gypsum stops under the floor, обычно используют ITS.
- DHU может стоить в разы больше ITS, поэтому перед listing проверяй details.
- Stair / Elevator / Shaft hangers помечай отдельно, чтобы review был ясным.

## Studs

| Spacing | Фактор | Waste |
| --- | ---: | ---: |
| 16" o.c. | 1:1 | 10% |
| 24" o.c. | 0.5 | 25% |

- На больших COM jobs используй exact heights: `9'0-3/8"`, `9'1-1/8"` и т.д.
- Пример math: `11'1" wall - 22" truss - 3/4" subfloor = 9'2" stud`.
- Corridor 2x4 staggered означает two rows at 16" o.c.; plates должны быть 2x6.
- Bearing walls on lower floors могут требовать double studs по structural notes.

## Sheathing

- `19/32"` equals `5/8"`, not `1/2"`.
- Exterior sheathing идёт по Arch / energy / Zip notes, если Structural не даёт
  более сильное non-Zip requirement.
- Interior sheathing идёт по Structural.
- Zip sheathing на exterior walls перекрывает structural sheathing notes, но
  оставляй note.
- Optional walls могут требовать full-height sheathing, а loose/box sheathing
  остаётся box only.

## Частые пропуски

- `1/2" plywood underlayment` per floor assembly.
- Piggy truss sleepers: often 2x6 between upper truss parts.
- `1/4" Densedeck` or glass mat cover board at flat roofs.
- Additional rigid XPS layer.
- Drywall ledger: 2x4 at demising walls both sides and exterior walls one side
  where parallel with framing.
- Chute shaft wall A201/A806, wall type 7A.
- A35 clips at shearwall connections.
- Jamb blocking for all windows and interior doors.
- Kitchen and bath blocking.
- Holdowns per S-details.

## Doors

- Unit entry doors from corridors обычно fire rated.
- Используй labels вроде `3070 Entry`, `2670 FCW` или `3070 HM C-lbl`.
- Door hardware numbers обычно не идут в takeoff list.
- Interior door jamb trim может использовать casing divided by 2, если это
  local estimating method.

## Interior Trims

- Room schedule: включай только wood base / `Wd`; tile base исключай.
- Corridors, lobbies и другие common areas перечисляй отдельно, потому что trim
  type может отличаться от units.
- Crowns включаются, когда interior trim scope активен.
- Если trims не указаны, пиши `not specified`, а не придумывай trim type.

## Client Metal Rule

| Считать metal | Исключить / by others |
| --- | --- |
| WM | EBS |
| Timberline | Probuild |
| Littleton | Triangle |
|  | Interstate |
|  | Bliffert |

Когда metal исключён, всё равно отмечай locations как `by others`.

## Formatting и output

- Не объединяй floors, даже если они одинаковые; copy data отдельно.
- Добавляй note, когда floor frame identical to another floor.
- Stair treads: указывай `2x12 Tread` и добавляй `1x8 Riser`.
- Nails не считай; bolts и Simpson screws указывай, где они required.
- Не оставляй copied detail labels без правки.
- Пиши `Schedule`, не `Shedule`.
- Floor labels: `1st`, `2nd`, `3rd`, `4th` и т.д.
- Если material приходит из отдельного specification PDF, добавляй note вроде
  `per customer note`.
- Убирай unused rows/items из output, кроме formulas, которые всё ещё drive wall
  calculations.
- Не меняй местами count и length columns для joists и похожих repeated members.
- Для duplex / repeated-building jobs проверяй multipliers дважды, чтобы не
  пропустить half a building.


<!-- confluence-gallery:start -->
## Картинки из Confluence

Изображения из Confluence размещены на этой странице по исходной теме.
Подпись сохраняет группу-источник, чтобы можно было быстро проверить контекст.

| Группа источника | Картинки | Confluence |
| --- | ---: | --- |
| --- | 19 | [source](https://ewood.atlassian.net/wiki/spaces/work/pages/11796656/---) |
| Need to sort | 4 | [source](https://ewood.atlassian.net/wiki/spaces/work/pages/229638146/Need+to+sort) |

<div class="kb-gallery">
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-011.png" title="image-20250224-003901.png">
    <img src="../../assets/images/confluence/confluence-011.png" alt="--- - unsorted field rule/reference 01">
    <div class="kb-gallery__caption">unsorted field rule/reference 01</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-012.png" title="image-20250224-003844.png">
    <img src="../../assets/images/confluence/confluence-012.png" alt="--- - unsorted field rule/reference 02">
    <div class="kb-gallery__caption">unsorted field rule/reference 02</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-013.png" title="image-20250224-003828.png">
    <img src="../../assets/images/confluence/confluence-013.png" alt="--- - unsorted field rule/reference 03">
    <div class="kb-gallery__caption">unsorted field rule/reference 03</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-014.png" title="image-20250224-003817.png">
    <img src="../../assets/images/confluence/confluence-014.png" alt="--- - unsorted field rule/reference 04">
    <div class="kb-gallery__caption">unsorted field rule/reference 04</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-015.png" title="image-20250224-003802.png">
    <img src="../../assets/images/confluence/confluence-015.png" alt="--- - unsorted field rule/reference 05">
    <div class="kb-gallery__caption">unsorted field rule/reference 05</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-016.png" title="image-20250224-003754.png">
    <img src="../../assets/images/confluence/confluence-016.png" alt="--- - unsorted field rule/reference 06">
    <div class="kb-gallery__caption">unsorted field rule/reference 06</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-017.png" title="image-20250224-003754.png">
    <img src="../../assets/images/confluence/confluence-017.png" alt="--- - unsorted field rule/reference 07">
    <div class="kb-gallery__caption">unsorted field rule/reference 07</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-018.png" title="image-20250224-003743.png">
    <img src="../../assets/images/confluence/confluence-018.png" alt="--- - unsorted field rule/reference 08">
    <div class="kb-gallery__caption">unsorted field rule/reference 08</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-019.png" title="image-20250224-003657.png">
    <img src="../../assets/images/confluence/confluence-019.png" alt="--- - unsorted field rule/reference 09">
    <div class="kb-gallery__caption">unsorted field rule/reference 09</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-020.png" title="image-20250224-003439.png">
    <img src="../../assets/images/confluence/confluence-020.png" alt="--- - unsorted field rule/reference 10">
    <div class="kb-gallery__caption">unsorted field rule/reference 10</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-021.png" title="image-20250224-003424.png">
    <img src="../../assets/images/confluence/confluence-021.png" alt="--- - unsorted field rule/reference 11">
    <div class="kb-gallery__caption">unsorted field rule/reference 11</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-022.png" title="image-20250224-003400.png">
    <img src="../../assets/images/confluence/confluence-022.png" alt="--- - unsorted field rule/reference 12">
    <div class="kb-gallery__caption">unsorted field rule/reference 12</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-023.png" title="image-20250224-002726.png">
    <img src="../../assets/images/confluence/confluence-023.png" alt="--- - unsorted field rule/reference 13">
    <div class="kb-gallery__caption">unsorted field rule/reference 13</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-024.png" title="image-20250224-002706.png">
    <img src="../../assets/images/confluence/confluence-024.png" alt="--- - unsorted field rule/reference 14">
    <div class="kb-gallery__caption">unsorted field rule/reference 14</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-025.png" title="image-20250224-002653.png">
    <img src="../../assets/images/confluence/confluence-025.png" alt="--- - unsorted field rule/reference 15">
    <div class="kb-gallery__caption">unsorted field rule/reference 15</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-026.png" title="image-20250224-002632.png">
    <img src="../../assets/images/confluence/confluence-026.png" alt="--- - unsorted field rule/reference 16">
    <div class="kb-gallery__caption">unsorted field rule/reference 16</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-027.png" title="image-20250224-002609.png">
    <img src="../../assets/images/confluence/confluence-027.png" alt="--- - unsorted field rule/reference 17">
    <div class="kb-gallery__caption">unsorted field rule/reference 17</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-028.png" title="image-20250224-002542.png">
    <img src="../../assets/images/confluence/confluence-028.png" alt="--- - unsorted field rule/reference 18">
    <div class="kb-gallery__caption">unsorted field rule/reference 18</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-029.png" title="image-20250224-002525.png">
    <img src="../../assets/images/confluence/confluence-029.png" alt="--- - unsorted field rule/reference 19">
    <div class="kb-gallery__caption">unsorted field rule/reference 19</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-049.png" title="image-20250214-155931.png">
    <img src="../../assets/images/confluence/confluence-049.png" alt="Need to sort - unsorted field rule/reference 01">
    <div class="kb-gallery__caption">unsorted field rule/reference 01</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-050.png" title="image-20250214-155410.png">
    <img src="../../assets/images/confluence/confluence-050.png" alt="Need to sort - unsorted field rule/reference 02">
    <div class="kb-gallery__caption">unsorted field rule/reference 02</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-051.png" title="image-20250214-150802.png">
    <img src="../../assets/images/confluence/confluence-051.png" alt="Need to sort - unsorted field rule/reference 03">
    <div class="kb-gallery__caption">unsorted field rule/reference 03</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-052.png" title="image-20250224-004123.png">
    <img src="../../assets/images/confluence/confluence-052.png" alt="Need to sort - unsorted field rule/reference 04">
    <div class="kb-gallery__caption">unsorted field rule/reference 04</div>
  </a>
</div>
<!-- confluence-gallery:end -->
