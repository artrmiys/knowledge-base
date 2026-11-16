# Screws (структурные саморезы)

<figure markdown>
  ![Structural screws in a built-up member](../../../../assets/images/framing/screws.svg)
  <figcaption markdown="span">Structural screws (SDS, SDWS, SDWC) по деталям соединений: ledger к фермам, пакеты LVL, замена ties. Считаются в pcs по шагу или по числу на узел.</figcaption>
</figure>

<figure markdown>
  ![Ledger прикручен к стене дома структурными саморезами с шестигранной головкой](../../../../assets/images/photos/hardware/ledger-structural-screws.jpg){ width="360" }
  <figcaption markdown="span">P.T. ledger deck на стене: структурные саморезы с шестигранной головкой парами по шагу, вверху hanger под joist. Screws считаем штуками по детали ledger (число на точку на шаг), без шайб и гаек. Фото: greenbuildingadvisor.com, [источник](http://www.greenbuildingadvisor.com/homes/durable-deck-ties-home-landscape), найдено через Pinterest.</figcaption>
</figure>

## Что это

Screws - структурные саморезы из деталей: `SDS 1/4 x 4 1/2`, `SDWS 22" ledger screw`, `SDWC` (в замену H2.5A). Считаются только когда деталь их называет; гвозди не считаем. Шайбы и гайки у screws не нужны. Болты - [Bolts](bolts.md).

## Где искать на чертежах

| Лист | Что взять |
| --- | --- |
| Ledger details | тип screw, шаг или число на торец фермы (например, 3 на торец @ 16") |
| Built-up beam, multi-ply LVL details | SDS на пакет, шаг и ряды |
| Roof-to-wall details | `6" SDWC in lieu of H2.5A`: либо clips, либо screws, не оба |
| Stair detail | screws нижней опорной доски stringers |

## Как мерить в OurPlanCore

Длина из Line детали (`details/2x10 ledger + screws`, `details/12/S401`), количество узлов из Count. Отдельную позицию для screws создавать не нужно, если они идут вместе с деталью ledger.

## Как назвать в дереве и строка DFL

Строка screws стоит сразу под своим соединением, в B - screw точно как на детали: `SDWS22600DB Screws`, без кода `1/4" x 4 1/2" SDS Screws`.

Screws ledger - строка `Screws (n) at Ledger`:

- `n` - screws в одной точке (на стойку или на торец фермы), шаг точек `sp` - с детали;
- `G` - LFT ledger, те же линии, что у строки `Ledger`;
- число screws `x = G*12/sp*n`, отдельного запаса нет;
- округление одно, как у всех счётных строк: меньше 50 - вверх до чётного, от 50 - вверх до 10: `=ЕСЛИ(x<50;ОКРВВЕРХ(x;2);ОКРВВЕРХ(x;10))`.

В прошлых книгах встречается старый вид `Screws 16" o.c. (3)`: шаг в H, запас `1.05` / `1.1` и округление `;3`. Новые строки ledger так не пишем.

| A (Label) | B | C | D | E |
| --- | --- | --- | --- | --- |
| `Screws (3) at Ledger` | `SDWS22600DB Screws` | `=ЕСЛИ(G*12/16*3<50;ОКРВВЕРХ(G*12/16*3;2);ОКРВВЕРХ(G*12/16*3;10))` | `pcs` | `4/S401` |
| `Screws (2)` | `1/4" x 4 1/2" SDS Screws` | узлов x 2 | `pcs` | деталь балка-пост |
| `Screws` | `SDWS 1/4 x 4 1/4` | `=4*4*G` на лестницу | `pcs` | stair detail |
| `Screws 24" o.c.` | `SDWC 6"` | по шагу ферм | `pcs` | `in lieu of H2.5A` |

## Частые ошибки

- Screws ledger не по детали: 1 на торец вместо 3 (84 стало 132).
- Screws взяты с другого этажа, не со своего ledger.
- У строки ledger оставлены запас `1.05` / `1.1` и округление `;3` старого вида: округление одно, до чётного или до 10.
- Детали 1 и 3 похожи на картинке, но крепёж разный.
- Clips H2.5A и SDWC посчитаны оба, когда деталь даёт "in lieu of".
- Гвозди посчитаны штуками.
- [Все ошибки по перекрытиям](../../../../start/common-mistakes.md#floor)

## Пример

| A | B | C | D | E | G |
| --- | --- | --- | --- | --- | --- |
| `Ledger` | `2x10` | `=ОКРВВЕРХ(G/D;1)` | 16 | `4/S401` | 44 |
| `Screws (3) at Ledger` | `SDWS22600DB Screws` | `=ЕСЛИ(G*12/16*3<50;ОКРВВЕРХ(G*12/16*3;2);ОКРВВЕРХ(G*12/16*3;10))` | pcs | `4/S401` | 44 |

Ledger: 44 / 16 = 2.75, значит 3 доски по 16'. Screws: 3 на стойку через 16", 44 x 12 / 16 = 33 точки, x 3 = 99; это не меньше 50, значит вверх до 10 = 100 pcs.

## См. также

- [Bolts](bolts.md), [Steel Beam Web Fillers](steelbeams.md), [Hardware catalog](../../../../reference/hardware-catalog.md)
- [Hangers](../../../../reference/hangers.md)
