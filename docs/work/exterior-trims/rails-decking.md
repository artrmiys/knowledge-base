# Rails & Decking (перила и настил: канон по типам)

<figure markdown>
  ![План балкона: decking, посты и секции перил, fascia](../../assets/images/trims/rails-decking.svg)
  <figcaption markdown="span">План балкона: decking по площади W x D, два поста перил по внешним углам, секции перил по фронту и открытым бокам, fascia по открытому периметру. Composite перила считаем системой, деревянные крашеные поэлементно.</figcaption>
</figure>

<figure markdown>
  ![Composite перила deck: пост в sleeve с cap, top rail, balusters](../../assets/images/photos/deck/composite-railing-post-cap.jpg){ width="360" }
  <figcaption markdown="span">Composite railing на deck: пост закрыт белым sleeve с cap, сверху cap rail под дерево, balusters между top и bottom rail, настил composite. Такую систему считаем секциями (`Rail sections`, unit) по сторонам плюс посты штуками; decking отдельно SQ FT. Фото: timbertech.com, [источник](https://www.timbertech.com/products/railing/), найдено через Pinterest.</figcaption>
</figure>

## Что это

Перила и настил балконов, porch и deck: railing-системы (composite, Azek,
wood, cable, metal), decking, hardware постов, balusters, cap rail, deck
fascia, skirt, risers, lattice. Это не trim и не каркас: каркас на
[Deck / Porch / Balcony Frame](../deck/deck-porch-balcony-frame.md), слои
балкона на [Balcony build-up](balcony-buildup.md). Эта страница канон по
типам перил; короткая версия для блока балкона на [Railing](../deck/railing.md).

## Где искать на чертежах

| Лист | Что взять |
| --- | --- |
| Elevations | Тип перил (composite, wood, cable, aluminum), высота 36" или 42", decking виден или нет |
| Детали A5xx (railing detail, deck edge) | Post, sleeve, cap, rail sections или balusters, cap rail, fascia, skirt |
| Spec и notes | `Railing by others`, продукт (Trex, Azek, DuxxBak), `verify` |
| Планы | Длина перил по сторонам, количество балконов и порчей каждого типа |

## Как мерить в OurPlanCore

Decking и перила берутся из размеров блока: площадь `W x D`, перила фронт
`W` плюс открытые бока `D`, умноженные на число экземпляров (units). Площадь
балконов и порчей как Area лежит в `sqfts/blcny` и `sqfts/porch`; deck у
земли со сложным контуром обводят Area в `sqfts` с понятным именем, перила
по изломанному контуру Line. Продукт и высоту в имя не писать, они живут в DFL.

<figure markdown>
  ![Railing: система или поэлементно](../../assets/images/trims/railing-system-vs-elements.svg)
  <figcaption markdown="span">Слева composite как система (посты с sleeve и cap, секции 6'), справа wood painted поэлементно (posts, balusters, rails, cap rail). Два поста на балкон, способы в одном блоке не смешивать.</figcaption>
</figure>

## Как назвать в дереве и строка DFL

Способ счёта один на участок: **система** (заводские секции) или
**поэлементно**. Composite и Azek всегда система; поэлементно только wood
painted. Не смешивать.

| Тип | Строки DFL | Unit | Правило |
| --- | --- | --- | --- |
| Composite / Azek (система) | `Note: Railing called composite per A501; decking assumed; verify`, `Posts at Rails` `4x4 P.T.`, `Post Sleeve` `Sleeve for 4x4`, `Post Cap` `Cap for 4x4`, `Rail sections` `8' Rail section` | pcs, unit; у постов в D длина `4` | посты `=2*units`; `Rail sections`: строка на каждую длину секции, C = число секций этой длины на балкон x units |
| Wood painted (поэлементно) | `Posts at Rails` `4x4 P.T.`, `Balustrades` `2x2 balusters`, `Rails (top & bottom)` `2x4 rails`, `Cap Rail` `2x6 cap rail` | pcs, LFT | `Balustrades =EVEN(G*2.2)*units`, `Rails (top & bottom) =EVEN(G*2.2)*units`, `Cap Rail =EVEN(G*1.1)*units`, G = LFT перил одного балкона |
| Cable | `Posts at Rails` `4x4 P.T.` или `Mtl post`, sleeve/cap, `Cables SS`, `Cap Rail` `2x6 cap rail` | pcs, LFT | cables = прогон x число тросов (`assumed 7 runs`), нота `verify product` |
| Aluminum / metal | `Note: Aluminum railing materials are by others; verify components` | | материал не считаем, нота обязательна |

Секции composite покупают готовой длиной, поэтому `Rail sections` это не
одна строка на балкон, а строка на каждую длину:

- одна секция на пролёт между постами (или между постом и стеной);
- в B ближайшая стандартная длина выше стороны: фронт `7'-4"` это
  `8' Rail section`, бок `6'` это `6' Rail section`;
- в E сторона и реальная длина: `front 7'-4"`, `sides 6'`;
- cap у composite входит в секцию, строки `Cap Rail` нет.

Decking и периметр:

| Строка DFL | Материал | Unit | Правило |
| --- | --- | --- | --- |
| `Decking` балкона | по детали: `2x6 DuxxBak`, `Composite Decking`, `5/4" Decking` | SQ FT | `=CEILING(W*D*units*1.1,10)`: площадь одного балкона x units x waste 1.1; в Terrace над гаражом `5/4x6` на `Sleepers 2x4 P.T.` |
| `Decking` deck / porch | `5/4x6` Composite, Azek, Wd, `5/4x4 T&G Mahogany` | SQ FT | та же формула; продукт по spec, иначе `TBD Decking` и нота |
| `Treads` | по материалу decking | LFT / pcs | отдельно от площади |
| `Deck Fascia` / `Deck Skirt` | `1x8`, `1x10`, `1x12 Azek` | LFT | по открытому периметру |
| `Deck Risers`, `Stringer trim` | `1x6`, `1x8`, `1x12` | LFT | лестница deck |
| `Lattice` + `Lattice wrap trim` | `PVC lattice`, `5/4x6` | SQ FT + LFT | площадь плюс обрамление |

Посты на улице всегда `P.T.`, и под крышей porch тоже; без P.T. только пост
внутри отапливаемого объёма, как его даёт schedule.
Post base и anchor (`ABU66 Zmax`, `DTT2Z`) только когда деталь их показывает,
строки каркаса с деталью в E, формат по [Hangers](../../reference/hangers.md#dfl-format).
Полный состав блока: [Блоки DFL](../../reference/dfl-blocks.md).

## Частые ошибки

- Три поста на балкон вместо двух; угловой балкон у двух стен несёт один.
- Система и поэлементный счёт смешаны: `Rail sections` вместе с `Balustrades`.
- `Rail sections` одной строкой на весь балкон без длины секции и стороны в E.
- Decking без waste: `=W*D*units` вместо `=CEILING(W*D*units*1.1,10)`.
- Aluminum перила посчитаны как материал.
- `Rails (top & bottom)` взяты одной ниткой вместо двух.
- Decking балкона `5/4x6` вместо `2x6 DuxxBak` по детали.
- Продукт угадан вместо `TBD` и ноты `Decking & Railing products to verify`.
- Все ошибки раздела: [Deck, porch, балконы](../../start/common-mistakes.md#deck).

## Пример

```text
Балкон 7'-4" x 6', 6 units, composite railing

Note: Railing called composite per A501; decking assumed; verify
Posts at Rails   4x4 P.T.          12   4      =2*6       assumed
Post Sleeve      Sleeve for 4x4    12   pcs    =C<posts>
Post Cap         Cap for 4x4       12   pcs    =C<posts>
Rail sections    8' Rail section   6    unit   =1*6       front 7'-4"
Rail sections    6' Rail section   12   unit   =2*6       sides 6'
Decking          2x6 DuxxBak       300  SQ FT  =CEILING(7.33*6*6*1.1,10)   5/A550

Decking: 7.33 x 6 = 44 SQ FT на балкон, x 6 = 264, x 1.1 = 290.4, вверх до 10 = 300
```

## См. также

- [Railing](../deck/railing.md), [Deck / Porch / Balcony Frame](../deck/deck-porch-balcony-frame.md), [Balcony build-up](balcony-buildup.md)
- [Porch / Deck / Balcony](porch-deck-balcony.md), [Soffit & Fascia](soffit-fascia.md)
- [Блоки DFL](../../reference/dfl-blocks.md), [Material catalog](../../reference/material-catalog.md), [Standard notes](../../reference/standard-notes.md)
