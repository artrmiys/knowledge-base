# Rim Board (торцевая доска перекрытия)

<figure markdown>
  ![Rim board at joist ends](../../../../assets/images/framing/rim-board.svg)
  <figcaption markdown="span">Rim board закрывает торцы joists по периметру перекрытия и несёт стену выше. Считается в LFT по периметру, не в 16' досках.</figcaption>
</figure>

<!-- TODO-PHOTO: engineered rim board at I-joist ends on top plate, EN query "rim board I-joist floor framing" -->

## Что это

Rim - доска по краю перекрытия, в которую упираются торцы joists: `1-1/8" OSB Rim`, `1-1/4" LSL Rim`, `1-3/4" LVL`. С I-joists только engineered rim. [Ribbon](ribbon.md) врезана в стойки и несёт joists, [Blocking](blocking.md) стоит между joists: это разные строки. Rim по периметру deck и balcony - P.T. 2x в [Deck / Porch / Balcony Frame](../../../deck/deck-porch-balcony-frame.md).

## Где искать на чертежах

| Лист | Что взять |
| --- | --- |
| Joist schedule, general notes | продукт и толщина rim по глубине joists |
| Wall sections, details перекрытия | rim у наружной стены, у demising с двух сторон, у roof TJI |
| Deck / corridor details | где rim несёт нагрузку и должен быть `1-3/4" LVL` |
| Framing plan этажа | периметр и внутренние линии, где меняется направление joists |

## Как мерить в OurPlanCore

Line (L) по линии rim на листе framing с точкой F: наружный периметр перекрытия плюс внутренние линии, где joists меняют направление или упираются в стену. Длина линии = длина применения узла. Позиция `framing/<этаж> framing/details/rim` или с номером детали `5/S400 rim`.

<figure markdown>
  ![Line по узлу на плане](../../../../assets/images/ourplancore/v3/measure-line-detail.png)
  <figcaption markdown="span">Line по линии применения детали: длина линии уходит в G строки DFL, имя детали даёт флаг M при экспорте.</figcaption>
</figure>

## Как назвать в дереве и строка DFL

Экспорт: кнопка DT ставит детали в J:L листа этажа; имя с `rim` получает флаг `r` в M, и макрос `C_RimBoardBlockingHangers` переносит длину в строку `Rim Board`.

| Имя в дереве | A (Label) | B (материал) | C | D | E |
| --- | --- | --- | --- | --- | --- |
| `details/rim` | `Rim Board` | `11-7/8" Rim` | `G x 1.05` (EWP) или `G x 1.1` | `LFT` | деталь |
| `details/rim LSL` | `Rim Board` | `11-7/8" LSL Rim` | | `LFT` | |
| `details/rim corr LVL` | `Rim Board` | `1-3/4 x 11-7/8 LVL` | | `LFT` | деталь corridor |
| `details/rim dem` | `Rim board dbl` | | `G x 2` | `LFT` | demising с двух сторон |

| Продукт | Когда |
| --- | --- |
| `1-1/8" OSB Rim` | частый тонкий rim по schedule |
| `1-1/4"` или `1-1/2" LSL Rim` | LSL указан или нужен усиленный rim |
| `1-3/4" LVL Rim` | к rim крепится deck или corridor frame, или деталь прямо требует |

Фактор один раз в формуле: `1.05` на EWP-заказах, `1.1` на остальных (residential, COM, reconstruction). Канон цифр: [Формулы](../../../../reference/formulas.md#rim-ribbon-blocking-ledger), то же в [Советах](../../../../reference/boss-feedback-rules.md#rim-board).

## Частые ошибки

- Rim назван `1-3/4 LVL`, хотя LVL не указан. По умолчанию `11-7/8" Rim`; продукт не ясен - `assumed` в note.
- Rim разбит на 16' куски. Держи LFT.
- Rim у roof TJI забыт.
- У demising посчитана одна сторона, деталь даёт rim с обеих сторон.
- На панельной работе rim посчитан с длиной стены, а не по линии перекрытия.
- [Все ошибки по перекрытиям](../../../../start/common-mistakes.md#floor)

## Пример

| A | B | C | D | E |
| --- | --- | --- | --- | --- |
| `Rim Board` | `11-7/8" LSL Rim` | `=ОКРВВЕРХ(G*1.05;1)` | LFT | `5/S400` |
| `Rim board dbl` | `11-7/8" LSL Rim` | `=ОКРВВЕРХ(G*2*1.05;1)` | LFT | `9/S400 demising` |

## См. также

- [Ribbon Board](ribbon.md), [Blocking](blocking.md), [Joist](../joist.md)
- [Советы: Rim Board](../../../../reference/boss-feedback-rules.md#rim-board), [Формулы](../../../../reference/formulas.md)
