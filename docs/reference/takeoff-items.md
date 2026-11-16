# Подписи строк DFL (Labels) и формат

Здесь: как называется строка в колонке A, что стоит в остальных колонках и какие подписи считаются каноническими. Подпись берётся из шаблона (лист `Standarts`), потому что макросы сортируют и суммируют строки по тексту, а проверяющий ищет позицию по знакомому имени.

## Формат строки

| Колонка | Правило | Пример |
| --- | --- | --- |
| A | подпись из словаря ниже; шаг, plies и назначение в подписи | `Studs Ext 16" o.c.`, `Plates Ext (2) dbl top`, `Beam (3) Flush` |
| B | сечение или модель; P.T., FRT, сорт после размера | `2x6 P.T.`, `2x10 FRT`, `(2) 1 3/4 x 11 7/8 LVL`, `11-7/8" TJI 210`, `LUS210 Zmax` |
| C | формула от G и H своего блока | `=EVEN(G33*H33*1.1)` |
| D | единица: `LFT` (не `FT`), `SQ FT` (не `SF`), `4x8`, `pcs`, `unit`, `tubes`, `50' rolls`. У леса штуками (studs, joists, beams, posts, headers, rim, ribbon, blocking в framing list, ledger, bracing) - длина доски в футах, C тогда число досок | `LFT`, `16` |
| E | лист или деталь, марка SW, высота стойки, назначение; дюймы со знаком `"` | `8/S3.0`, `SW-2`, `9' 1 1/8"`, `for Ext Walls` |
| G | замер из OurPlanCore без запаса: площадь под листы, длина под доски и погонаж, число точек под штучное | `3760` |
| H | шаг в дюймах, plies, высота; что именно, зависит от строки: [Формулы](formulas.md#legend) | `16`, `2` |

- Подпись совпадает с расчётом: `Plates (2)` при H = 1 и `Posts (3)` при одном посте в детали - ошибка.
- `(n)` в конце подписи - число слоёв (plies) в одном месте. C считает все доски: число мест x n. `Beam (3)` с двумя балками на плане = 6 в C; `Dbl Rafters` = места x 2. В дереве одна составная балка - одна точка, а не n точек.
- Другой сорт или материал - отдельная строка: из 18 досок 2x12 шесть MSR 1650f-1.5E пишутся своей строкой.
- Caps, bases, hangers, ties, bolts - в `pcs`. Rim, ribbon, blocking, ledger в framing list обычной книги - досками по 16': C `=CEILING(G/D,1)`, D `16`. В `LFT` они остаются только на EWP-only заказе; blocking в стенах и в `Wall Materials` всегда в `LFT`. В дереве линию детали на куски не режут.
- Этажи: `1st`, `2nd`, `3rd`, `4th`; этаж над последним полным - `Loft`. `Schedule`, не `Shedule`; модели без опечаток (`SDWS`, `PC6Z`, `MPB66`).
- Скопированный блок: подписи, E и ссылки в C поправлены под новый этаж.

## Округление

| Что | Правило |
| --- | --- |
| Штучный крепёж, результат меньше 50 | вверх до чётного: `=CEILING(G*12/H*1.1,2)` |
| Штучный крепёж, 50 и больше | родная значимость шаблона (`,10` у больших ties и screws, `,1` у листов) |
| Screws по фермам | по 3 на точку: `=CEILING(...,3)` |
| Доски, листы, трубы | целыми вверх; `2.75` и `9.6` в C не бывает |

## Словарь подписей

Канон - лист `Standarts`. Ниже самые нужные группы. Варианты в скобках подставляются по месту: `(2)`, `(3)` plies, шаг `16" o.c.`, назначение `Ext`, `Int`, `Corr`, `Demising`.

### Заголовки секций

`Foundation Walls`, `Basement Floor Walls`, `1st ... 4th Floor Walls`, `Gable Walls`, `Parapet Walls`, `Wall Materials`, `1st ... 4th Floor Framing List`, `Loft Framing List`, `Roof Frame list`, `Roof System Misc`, `Roof Products`, `Covered Front Porch Framing List`, `#N Upper Balcony List W' x D'`, `#N Porch Framing List W' x D'`, `Canopy Framing List`, `Exterior Trims`, `Interior Doors&Trims`.

Оформление: жирный, цветной фон, столбцы B-F пустые. Подсекции групп: `Rear Ground Deck Frame`, `Balcony Railing`, `Ground Deck Decking (rear)`, `Canopy Trims`, `Porch Trims`. [Формат файла](dfl-overview.md#source-format).

### Стены

| Подпись | Когда |
| --- | --- |
| `Plates Ext (1) btm`, `Plates Ext (2) dbl top`, `Plates (bottom and dbl top)`, `PT Plates (single)`, `PT Sill Plates at ext. found`, `Plates Furring`, `Eve Plates (single)`, `Hip Plates (2)` | число plies в подписи и в H; P.T. только на бетоне и кладке |
| `Studs Ext 16" o.c.`, `Studs Interior 16" o.c.`, `Studs Demising 16" o.c.`, `Studs for Gables`, `Blocking Studs` | высота стойки в E |
| `Bracing Ext Walls`, `Bracing Corridor`, `Bracing Demising`, `Bracing 48" o.c.` | по типу стены |
| `Blocking`, `Blocking (2)`, `Blocking 48" o.c.`, `Blocking for Drywall`, `Blocking at Eves`, `Blocking (3) Plates`, `Blocking around all openings` | шаг или назначение в подписи |
| `Ext. Headers up to 48"`, `... up to 60"`, `... up to 72"`, `Ext. Headers over 72"`, `Int. Headers (2)`, `Garage headers (3)` | plies в подписи |
| `Wall Sheathing`, `Box Sheathing`, `Inside Sheathing`, `Tape`, `Vapor Barrier` (WRB по спецификации), `Insulation`, `Rigid Insulation`, `Window Flashing`, `Sill Flashing` | B тянет спек-ячейку (`=$O$3`) |
| `Holdowns (1) btm`, `Holdowns (2) btm top`, `SW Anchor Bolts 12" o.c.`, `Anchor Bolts 48" o.c.`, `Washers`, `Nuts` | модель в B, марка SW в E |
| `Tracks (1) btm`, `Deflection Tracks (1) top`, `Mtl Studs 16" o.c.` | металлические стены, в этом порядке |
| `Buildout Horizontal`, `Buildout Vertical 16" o.c.` | build-out фасада, FRT по узлу |
| `Draft Stop` | в `Gable Walls` после пустой строки |

### Перекрытия и каркас

| Подпись | Когда |
| --- | --- |
| `Beam`, `Beam (2) Flush`, `Beam (3)`, `Beam Rim`, `Beam Stairs`, `Beam balcony`, `Ext Beam`, `Platform Beam (2)`, `Nailer Plates for Steel Beam` | plies в подписи, `Flush` только когда schedule помечает балку flush (Dropped в подписи не пишут), код балки в E |
| `Joists 16" o.c.`, `Joist J1`, `Dbl Joists 16" o.c.`, `Extra joists`, `End Joists`, `Ceiling Joists 16" o.c.`, `Rafters 24" o.c.`, `Dbl Rafters`, `Collar ties 16" o.c.` | серия I-joist в B (`11-7/8" TJI 210`) |
| `Rim Board`, `Rim Board (2)`, `Ribbon Board`, `Ledger`, `Ledger (2)`, `Ledger and Box`, `Box`, `Bracing for Trusses` | доски по 16' (D `16`); rim без `LVL` в B, если продукт не назван |
| `Cross Bridging`, `Cross Bridging for I Joists` | деревянный `1x3` досками по 16'; `TB27` у I-joists в `pcs` |
| `Hangers`, `Hangers 16" o.c.`, `Hangers on demising`, `Clips`, `Ties`, `Simpson Ties at Eves` | модель в B: `LUS210 Zmax`, `H2.5A` |
| `Posts`, `Posts (2)`, `Post Bases`, `Post Caps`, `Post Blocking`, `Post Sheathing`, `Columns` | высота в E, модель крепежа в B |
| `Stringers (4)`, `Treads`, `Risers`, `Platform`, `Platform Ledger` | `2x12 Tread`, `1x8 Riser` |
| `Subfloor`, `Panel Adheasive`, `Plywood`, `Linear Panels`, `Liner Panels` | подпись шаблона сохраняется как есть |

### Кровля и карнизы

`Ridge`, `Ridge (2)`, `Ridge Vent`, `Frame for Rakes 24" o.c.`, `Frame for Soffits 24" o.c.`, `Rafter Frame for returns`, `Sub Fascia`, `Truss Bracing`, `Blocking at Eves`, `Metal Roofs`, `Felt for Roof`, `Ice and Water (eves&valleys)`, `EPDM at flat roofs`, `Hclips` (спека `5/8 Hclip` по толщине настила).

### Deck, porch, балкон, перила

`Decking`, `Deck Fascia`, `Deck Risers`, `Sleepers`, `Posts at Rails 4x4`, `Post Sleeve`, `Post Cap`, `Rail sections 6'`, `Balustrades`, `Rails (top & bottom)`, `Cap Rail`, `Cables`, `Brackets`, `Railing`. Состав блоков: [Блоки балконов, porch и holdowns](dfl-blocks.md).

### Отделка и прочее

`Ext Casing`, `Casing for Int. Doors`, `Corner Boards`, `Crowns`, `Frieze Board`, `Fascia at Eves`, `Fascia at Rakes`, `Over Fascia Trims`, `Furring`, `Baseboard`, `Head Trim Flashing`, `Flashings at Wall`, `Int. Doors` (`3070 1 unit MARK FIRE LABEL`, двери шире 3'-6" как двойные `(2)2670`), `Cased Openings`, `Drywall at Walls`, `Drywall at Ceiling`, `Insulation at 6" Ext. Walls` (drywall и утеплитель между стойками - только когда они прямо в scope, обычно by others), `Lath Horiz 4" o.c.`, `Lath Vert 16" o.c.`.

## Частые ошибки

- `FT` или `SF` в D; крепёж в `LFT`; у досок в D единица вместо длины доски, и формула делит на текст.
- Линия детали (rim, blocking) в дереве разбита на куски по 16': меряется вся длина, на доски делит формула.
- Подпись не совпадает с расчётом (`Plates (2)` при одной plate в детали).
- `1-3/4 LVL Rim`, когда LVL не назван на чертеже: пиши `11-7/8" Rim` или `11-7/8" LSL Rim`.
- Модель крепежа с опечаткой или в своём формате (`ABU66Z` вместо `ABU66 Zmax`): [Hangers, как записывать](hangers.md#dfl-format).
- Свободные подписи вместо словаря: макросы сортировки их не находят.

Все ошибки по книге: [Частые ошибки, Excel DFL и ноты](../start/common-mistakes.md#excel).

## Пример

```text
A                           B                      C                        D      E            G     H
2nd Floor Framing List
Note: Floor Trusses are by others
Beam (3) Flush              1 3/4 x 11 7/8 LVL     =2*3                     14     FB2
Corridor Joists             2x10                   43                       14     86 pcs 7'
Rim Board                   1 1/8 x 24 Rim Board   =CEILING(G144/D144,1)    16     5/S401       310
Blocking for Drywall        2x4                    =CEILING(G145/D145,1)    16     6/S401       420
Bracing for Trusses         2x6                    =CEILING(G147/D147,1)    16     assumed      288
Hangers                     LUS210                 =2*86                    pcs    7/S401
```

Как читать пример:

- `Beam (3) Flush`: две балки по три слоя, C = 2 x 3 = 6 досок по 14'. `(3)` в подписи - число слоёв в одном месте, C считает все доски.
- `Corridor Joists`: 86 кусков по 7' режутся по два из доски 14', поэтому C = 43, а число кусков записано в E.
- `Rim Board`: 310 / 16 = 19.4, это 20 досок по 16'. В D стоит длина доски, поэтому формула делит на D. Напиши в D `LFT` - и формула поделит на текст.
- `Blocking for Drywall`: 420 / 16 = 26.3, это 27 досок. `Bracing for Trusses`: 288 / 16 = 18 досок.
- `Hangers`: по два на каждый кусок joist, 2 x 86 = 172.
- Rim с фактором `1.05` в `LFT` бывает только на EWP-only заказе: [Формулы](formulas.md#rim-ribbon-blocking-ledger).

## См. также

- [DFL: как устроена книга](dfl-overview.md), [Ноты в DFL](standard-notes.md), [Блоки балконов, porch и holdowns](dfl-blocks.md)
- [Material catalog](material-catalog.md), [Hardware catalog](hardware-catalog.md), [Макросы и клавиши Excel](excel-hotkeys.md)
