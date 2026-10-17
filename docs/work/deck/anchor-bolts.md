# Anchor Bolts (анкеры sill plate и крепёж ledger)

<!-- TODO-PHOTO: anchor bolt with square washer and nut through P.T. sill plate on concrete, EN: "anchor bolt sill plate washer nut concrete" -->

<figure markdown>
  ![Anchor bolt through sill plate](../../assets/images/framing/anchor-bolt.svg)
  <figcaption markdown="span">Anchor bolt с washer и nut крепит P.T. plate к бетону. Размер, заглубление и шаг только из anchorage schedule и SW schedule, дефолта нет.</figcaption>
</figure>

## Что это

Анкеры нижней plate на бетоне или кладке, крепёж ledger балкона и porch к
дому, through bolts узлов балка-пост. Каждая группа своей строкой: `Anchor
Bolts`, `Washers`, `Nuts`. Общие правила по болтам и screws на странице
[Bolts](../horizontal/floor-framing/details/bolts.md); анкеры holdowns на
[Shear Wall](../vertical/sheathing/shear-wall.md).

## Где искать на чертежах

| Лист | Что взять |
| --- | --- |
| Sill and sole plate anchorage schedule (S0.x, S5xx) | Диаметр, длина, заглубление (`emb`), шаг, продукт (Titen HD, wedge anchor, cast-in J-bolt) по типу стены |
| Shear Wall Schedule | Свой шаг анкеров под каждой маркой SW, часто чаще типового |
| Детали ledger балкона и porch (S3xx) | Through bolts или screws, шаг, washers |
| General notes S | Hilti или другой продукт by others, минимальное заглубление |

Дефолтного анкера нет: размер, заглубление и шаг только из anchorage
schedule. Schedule не найден: пиши `assumed` в E и ноту
`Note: Anchor Bolts <size> assumed; verify`.

## Как мерить в OurPlanCore

Длина линии анкеров равна LFT стен на бетоне с того же этажа
(`walls/<этаж>`, точка F для фундамента). Проёмы в этой линии (ворота,
двери) вычитаются один раз. Ledger: длина ledger из блока балкона или
porch. Шаг и тип анкера в имени не нужны, они живут в DFL.

## Как назвать в дереве и строка DFL

| Строка DFL | B (spec) | Unit | Формула |
| --- | --- | --- | --- |
| `Anchor Bolts 48" o.c.` | `1/2" Ø x 4" emb Titen HD` | pcs | `=CEILING(G*12/48,2)`, E = `for Ext Walls` |
| `Anchor Bolts 32" o.c.` | по SW schedule, тот же формат | pcs | отдельная строка на каждый шаг |
| `Washers` | `3x3` или plain по детали | pcs | равно анкерам |
| `Nuts` | | pcs | равно анкерам |
| `Through Bolts` (ledger, балка-пост) | `1/2" Ø` по детали | pcs | шаг по детали, washers и nuts своими строками |

Формат B: диаметр, длина или заглубление, продукт, в таком порядке
(`5/8" Ø x 7" emb`, `1/2" Ø x 4" emb Titen HD`); общие правила записи
крепежа в [Hangers: как записывать крепёж в DFL](../../reference/hangers.md#dfl-format).
Блок из четырёх строк (Blocking, Anchor Bolts, Washers, Nuts) вставляет
макрос `B_BoltsAdd`, см. [Excel macro hotkeys](../../reference/excel-hotkeys.md).
Мелкий крепёж до 50 штук округляется вверх до чётного. Анкеры holdowns
считаются в блоке holdowns: [Блоки DFL](../../reference/dfl-blocks.md#holdowns).

## Частые ошибки

- Один шаг анкеров на всё здание без SW schedule.
- Wedge anchor заменён на Titen HD без основания в детали.
- Проёмы не вычтены из линии анкеров, или вычтены дважды.
- Washers скопированы со старым шагом и не пересчитаны.
- Hilti by others посчитаны как наши; нота обязана остаться.
- Все ошибки раздела: [Deck, porch, балконы](../../start/common-mistakes.md#deck), [Shear walls и holdowns](../../start/common-mistakes.md#holdowns).

## Пример

```text
Anchor Bolts 48" o.c.   1/2" Ø x 4" emb Titen HD   42  pcs   =CEILING(G*12/48,2)   for Ext Walls  S0.2
Anchor Bolts 32" o.c.   1/2" Ø x 4" emb Titen HD   18  pcs   SW1 per schedule       S502
Washers                 3x3                60  pcs   =C<bolts>
Nuts                                        60  pcs   =C<bolts>
```

## См. также

- [Bolts](../horizontal/floor-framing/details/bolts.md), [Sill Plates](../vertical/walls/sill-plates.md), [Shear Wall](../vertical/sheathing/shear-wall.md)
- [Deck / Porch / Balcony Frame](deck-porch-balcony-frame.md), [Блоки DFL: holdowns](../../reference/dfl-blocks.md#holdowns), [Hangers](../../reference/hangers.md#dfl-format)
- [Hardware catalog](../../reference/hardware-catalog.md), [Standard notes](../../reference/standard-notes.md)
