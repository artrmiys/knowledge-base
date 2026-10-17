# Subfloor Sheathing (настил перекрытия)

<figure markdown>
  ![Subfloor T and G on joists](../../../assets/images/framing/subfloor.svg)
  <figcaption markdown="span">Subfloor по умолчанию 3/4" T&G на клею по joists. FRT-полоса у наружной стены, underlayment и настил поверх существующего пола - отдельные строки.</figcaption>
</figure>

## Что это

Subfloor - листовой настил по joists: `3/4" T&G OSB` или `AdvanTech`, на panel adhesive. Отдельно считаются FRT-полоса по периметру, underlayment под отделку, настил под ваннами и настил поверх существующего пола. Вертикальная полоса обшивки на уровне перекрытия - страница [Floor-height Sheathing](../../vertical/sheathing/floor.md), не subfloor.

## Где искать на чертежах

| Лист | Что взять |
| --- | --- |
| Floor assembly (A5xx, A6xx), general notes | толщина и продукт, T&G, adhesive, слои сверху |
| S general notes, FRT-нота | полоса FRT 2' или 4' от наружной стены; blocking под её кромкой |
| Finish schedule, bath details | underlayment 1/2", 3/4" ply под ваннами |
| Reconstruction details | новый subfloor поверх существующего пола, если деталь требует |
| Deck и balcony sections | structural subfloor балконов, отдельный материал |

## Как мерить в OurPlanCore

Площадь берётся из `sqfts/<этаж>` (Area этажа), отдельный замер не нужен. Для FRT-полосы нужна длина наружного периметра своего этажа: Line по наружным стенам или сумма `ext` стен этажа.

- Листы = SQ FT / 32 x 1.1, округление вверх до листа (`4x8`).
- FRT-полоса: периметр этажа x ширину полосы (2' или 4'), своим этажом. Полоса 4' на 10 листов вместо 54 - типичный недосчёт.
- Panel adhesive: строка `Panel Adheasive` `29OZ` по норме шаблона; строка часто забывается.

## Как назвать в дереве и строка DFL

Замеров в `framing` обычно нет: строки берут площадь из листа SQFT. Кнопка SF полосы XL переносит площади в `A2_SQFT_calc`, субфлор считается в каждом `Floor Framing List`.

| A (Label) | B (материал) | C | D | E |
| --- | --- | --- | --- | --- |
| `Subfloor` | `3/4" T&G OSB` | `=ОКРВВЕРХ(G/32*1.1;1)` | `4x8` | лист assembly |
| `Subfloor FRT 4'` | `3/4" T&G FRT` | периметр x 4 / 32 x 1.1 | `4x8` | нота FRT |
| `Panel Adheasive` | `29OZ` | по норме шаблона | `pcs` | |
| `Underlayment` | `1/2" Ply` | площадь / 32 x 1.1 | `4x8` | finish schedule |
| `Plywood at Tubs` | `3/4" Ply` | по числу ванн | `4x8` | `Addendum A` |
| `Blocking` | `2x` | периметр FRT-полосы | `LFT` | под кромкой FRT |

## Частые ошибки

- FRT-полоса посчитана не по периметру своего этажа или вовсе пропущена.
- Underlayment по всей площади, хотя деталь даёт 3/4" ply только под ваннами, а не под душевыми.
- Новый subfloor поверх существующего пола не включён, хотя деталь реконструкции его требует.
- Panel adhesive нет в строках.
- Настил балкона и terrace посчитан как subfloor дома: там свой материал по разрезу.
- [Все ошибки по перекрытиям](../../../start/common-mistakes.md#floor)

## Пример

| A | B | C | D | E |
| --- | --- | --- | --- | --- |
| `Subfloor` | `3/4" T&G OSB` | 60 | 4x8 | `A501` |
| `Subfloor FRT 4'` | `3/4" T&G FRT` | 24 | 4x8 | `S001 note 12` |
| `Panel Adheasive` | `29OZ` | 84 | pcs | |

<figure markdown>
  ![AdvanTech subfloor nailing](../../../assets/images/confluence/confluence-154.png)
  <figcaption markdown="span">Архивное фото: лист AdvanTech прибивают к joists. Продукт пишется как в спецификации (`AdvanTech`, `3/4" T&G OSB`), не обобщённо.</figcaption>
</figure>

## См. также

- [Joist](joist.md), [Floor SQFT](../../sqfts/1st2nd.md), [Floor-height Sheathing](../../vertical/sheathing/floor.md)
- [Blocking](details/blocking.md), [Reconstruction](../../../work-types/reconstruction.md)
