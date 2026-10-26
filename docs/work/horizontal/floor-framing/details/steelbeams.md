# Steel Beam Web Fillers (nailer и fillers на стальной балке)

<figure markdown>
  ![Steel beam with wood nailer and web filler](../../../../assets/images/framing/steel-beam-nailer.svg)
  <figcaption markdown="span">Стальная балка by others, но деревянный nailer на верхней полке, filler в стенке и болты к ним - наши строки. Top nailer задаёт top-mount hanger для joists.</figcaption>
</figure>

<figure markdown>
  ![Стальная балка в подвале под деревянными joists перекрытия](../../../../assets/images/photos/framing/steel-beam-under-floor-joists.jpg)
  <figcaption markdown="span">Подвал: стальная W-балка на трубчатых колоннах несёт деревянные joists. Сталь и колонны by others; наши строки - nailer по верхней полке, болты к нему с шайбами и гайками, hangers, если joists висят сбоку. Фото: housedigest.com, [источник](https://www.housedigest.com/1919599/diy-solution-turn-steel-ugly-basement-support-beam/), найдено через Pinterest.</figcaption>
</figure>

## Что это

Nailer (nailer plate) - доска на верхней полке стальной балки, в которую бьют hangers joists; web filler - доска в стенке балки между полками для face-mount hangers или крепления. Сама сталь (W12x26, HSS) by others. Считаем дерево, болты, шайбы, гайки и hangers.

## Где искать на чертежах

| Лист | Что взять |
| --- | --- |
| S framing plan | длины стальных балок своего этажа |
| General framing notes | типовая нота: `double 2x plate bolted to top flange, 3/8" bolts staggered @ 24" o.c.` |
| Steel beam details (S4xx, S5xx) | nailer сверху и снизу, ripped to flange width, filler, тип hanger |
| Hanger schedule | top-mount на nailer или face-mount на filler |

## Как мерить в OurPlanCore

Line (L) по оси стальной балки на листе framing с точкой F: `framing/<этаж> framing/details/nailer` или `details/W12 nailer`. Длина линии = длина балки. Сталь как Beam не рисуем.

<figure markdown>
  ![Line по узлу на плане](../../../../assets/images/ourplancore/v3/measure-line-detail.png)
  <figcaption markdown="span">Line по линии применения детали: длина линии уходит в G строки DFL, имя детали даёт флаг M при экспорте.</figcaption>
</figure>

## Как назвать в дереве и строка DFL

Блок из четырёх строк рядом с балками своего этажа. Nailer по умолчанию двойной (нота `double 2x plate`); одинарный только если деталь прямо показывает один слой. Нижний nailer под полкой и filler - отдельные строки по детали.

| A (Label) | B | C | D | E |
| --- | --- | --- | --- | --- |
| `Nailer Plates for Steel Beam (2)` | `2x8` (по ширине полки, `3x DF ripped`) | `=ОКРВВЕРХ(G*2/D;1)` | `16` | `14/S400` |
| `Anchor Bolts 24" o.c. (2)` | `3/8" Ø` | `=ОКРВВЕРХ(G*12/H*2*1.1;2)` | `pcs` | `note II.B` |
| `Washers 24" o.c. (2)` | `3/8" Washers` | та же формула | `pcs` | |
| `Nuts 24" o.c. (2)` | `Nuts for 3/8" Ø` | та же формула | `pcs` | |
| `Web Filler` | `2x6` | `=ОКРВВЕРХ(G*2/D;1)` | `16` | деталь |
| `Hangers` | top-mount на nailer, face-mount на filler | по joists | `pcs` | деталь |

Шайба под болт nailer - обычная washer, `3x3` только если деталь требует.

## Nailer и packing по профилю W { #w-table }

Когда деталь не даёт размер nailer или число слоёв в стенке, бери их по профилю балки (`W12x26`: серия W12, вес 26 lb/ft). Packing (web filler) - доски в стенке балки, число слоёв на обе стороны вместе. Деталь со S-листа всегда главнее таблицы.

| Серия | Вес (lb/ft) | Nailer | Packing, слоёв на 2 стороны |
| --- | --- | --- | --- |
| W6 | x9 | `2x6` | 2 |
| W6 | x12 | `2x6` | 4 |
| W6 | x15, x16, x20, x25 | `2x8` | 4 |
| W8 | x10, x13, x15, x18, x21 | `2x6` | 4 |
| W8 | x24, x28 | `2x8` | 6 |
| W8 | x31, x35, x40, x48, x58, x67 | `2x10` | 6 |
| W10 | x12, x15, x17, x19 | `2x6` | 4 |
| W10 | x22, x26, x30 | `2x8` | 4 |
| W10 | x33, x39, x45 | `2x10` | 6 |
| W10 | x49, x54, x60, x68, x77, x88, x100 | `2x12` | 8 |
| W12 | x14, x16, x19, x22 | `2x6` | 4 |
| W12 | x26, x30, x35 | `2x8` | 6 |
| W12 | x40, x45, x50 | `2x10` | 6 |
| W12 | x53, x58, x65, x72, x79, x87, x96 | `2x12` | 8 |
| W12 | x106, x136, x170, x230 | `(2) 2x8` | 8 |
| W14 | x22, x26 | `2x6` | 4 |
| W14 | x30, x34, x38 | `2x8` | 6 |
| W14 | x43, x48, x53 | `2x10` | 6 |
| W14 | x61, x68, x74, x82 | `2x12` | 8 |
| W14 | x90, x99, x109, x120, x132, x176, x193 | `(2) 2x8` | 10 |
| W16 | x26, x31 | `2x8` | 4 |
| W16 | x36, x40, x45, x50, x57 | `2x8` | 6 |
| W16 | x67, x77, x100 | `2x12` | 8 |
| W18 | x35, x40, x46 | `2x8` | 4 |
| W18 | x50 | `2x8` | 6 |
| W18 | x55, x60, x71 | `2x10` | 6 |
| W18 | x76, x86, x97, x106, x119, x130 | `2x12` | 8 |
| W21 | x44, x50, x57 | `2x8` | 6 |
| W21 | x73 | `2x10` | 6 |

`(2) 2x8` - два nailer рядом: полка шире доски 2x12.

## Частые ошибки

- Nailer посчитан одинарным без болтов, хотя нота даёт double 2x с болтами 3/8" @ 24".
- Болты взяты по балкам другого этажа.
- Hanger выбран face-mount, а деталь даёт опору сверху на nailer (top-mount), или наоборот.
- Filler steel anchors с шайбой 3x3 без указания.
- `EWP by others`, а LVL/LSL blocking у стальной балки по детали не записан.
- [Все ошибки по перекрытиям](../../../../start/common-mistakes.md#floor)

## Пример

| A | B | C | D | E | G | H |
| --- | --- | --- | --- | --- | --- | --- |
| `Nailer Plates for Steel Beam (2)` | `2x8` | `=ОКРВВЕРХ(G*2/D;1)` | 16 | `4/S5.6` | 86 | |
| `Anchor Bolts 24" o.c. (2)` | `3/8" Ø` | `=ОКРВВЕРХ(G*12/H*2*1.1;2)` | pcs | `note II.B` | 86 | 24 |
| `Washers 24" o.c. (2)` | `3/8" Washers` | `=ОКРВВЕРХ(G*12/H*2*1.1;2)` | pcs | | 86 | 24 |
| `Nuts 24" o.c. (2)` | `Nuts for 3/8" Ø` | `=ОКРВВЕРХ(G*12/H*2*1.1;2)` | pcs | | 86 | 24 |

## См. также

- [Beam](../beam.md), [Bolts](bolts.md), [Hangers](../../../../reference/hangers.md)
- [Metal tracks](../../../vertical/walls/metal-tracks.md) - стены под стальными балками
