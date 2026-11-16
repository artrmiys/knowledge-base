# Блоки балконов, porch и holdowns в DFL

Здесь: как расписать в книге блок балкона, блок porch и блок holdowns так, как это делается в сданных работах. Блок = заголовок с заливкой, ноты под ним, строки с формулами, белые пустые строки между группами. Блок вставляется копией эталона (блок `#1` шаблона или блок из прошлой сдачи), а не набирается руками.

!!! warning "Новые правила оформления групп (ноябрь 2026)"
    Группа лежит внутри Framing, желательно сразу после framing list своего этажа. Decking, railing и trims стоят сразу за каркасом **под своими заголовками**. Ноты только под заголовком. Полное правило со схемой: [Формат файла, группы](dfl-overview.md#groups).

<figure markdown>
  ![Каркас балкона в плане](../assets/images/framing/deck-frame-plan.svg)
  <figcaption markdown="span">Каркас балкона: ledger у стены, joists с hangers, beam на posts, box или rim по периметру. Каждый элемент - своя строка блока.</figcaption>
</figure>

## Перед блоками

1. Второй блок в той же книге: [Duplicate Block](ewood-tab.md#duplicate) копирует его со своими единицами. Первый блок: открыть сданную работу с похожим балконом или porch и посмотреть, как блок расписан там.
2. Посчитать типы отдельно: балконы по размеру и числу постов, porch отдельно от балконов (у porch свой счёт, он не зеркалит балконы). Количество экземпляров - по дверям на планах этажей, умноженное на этажи, со сверкой с deck-joist callouts на S-планах: дверь без деревянных joists - бетонный или ферменный балкон, это другой блок.
3. Замеры взять из OurPlanCore: площади `sqfts/blcny`, `sqfts/porch`, точки блоков (одна позиция на тип, точка на экземпляр, `xN` в имени), holdowns из `shear walls/<этаж>/holdowns`.
4. Все детали соединений на S прочитать до конца: балка к посту, край перекрытия, балка в балку.

## Оформление блока

| Элемент | Как |
| --- | --- |
| Заголовок балкона | `="#N Upper Balcony List W' x D' "&G&" unit"&H`, заливка A:B, жирный чёрный; в шаблоне заливка `FABF8F`, в эталонах заголовки групп зелёные `99CC00`, для нового заголовка берите зелёный ([что пока не уточнено](dfl-overview.md#open)); терраса над гаражом - `Upper Balcony/Terrace List` |
| Заголовок porch | `#N Porch Framing List W' x D'`, заливка A:B зелёная `99CC00`, жирный чёрный |
| Заголовок ground deck | обязательно `Deck` и `Frame` или `Framing`, плюс уровень и расположение: `Rear Ground Deck Frame`, `Ground Deck Framing List (left)`. `Rear Deck` программа не распознает |
| Текст в заголовке | только в A, столбцы B-F пустые; деталь или лист пишите заметкой под заголовком |
| Несколько одинаковых по типу | указывайте расположение: где какой балкон, какой porch |
| Units | G заголовка = число экземпляров; площадные строки парсят W и D из заголовка и множат на G заголовка |
| Ноты | под заголовком, не над ним; префикс и жёлтый фон ([Заметки](dfl-overview.md#notes)) |
| Decking, railing, trims | сразу за каркасом, каждый под своей строкой-заголовком: `Balcony Railing`, `Ground Deck Decking (rear)`, `Canopy Trims`, `Decking and Railing`, `Porch Trims` |
| Пустые строки | белые, формат с белой пустой строки; заливка только на нотах и заголовке |
| Нули | строки с C = 0 и пустые шаблонные строки удалить |

## Блок балкона

| Строка | Как считать | Откуда |
| --- | --- | --- |
| `Posts` | `P.T.`, по плану: обычно 2, угловой или нишевый балкон может нести 1 | план, S-деталь |
| `Post Bases` | модель по детали (`ABA66 Zmax`, `ABU66 Zmax`) | S-деталь |
| `Post Caps` | по plies балки: 3-ply `BCS2-3/6 Zmax`, 2-ply `BC46 Zmax`; модель per schedule, не дефолт | S-деталь, schedule |
| `Beam` фронт и бока | plies ведущим множителем в C (`=3*...`, `=2*...`); коды балок из легенды проекта (пример: балкон `2x12 P.T.` B3/B4, porch `2x10` B1/B2) | beam schedule |
| `Ledger` + screws | screws `SDWS22400DB` по 3 на точку (`=CEILING(...,3)`) | деталь ledger |
| `Box` | только если балка не flush; flush-балка заменяет box и rim | S-план |
| `Joists` | `2x12 P.T.` или `2x10 P.T.`, счёт `W*12/16+1`; длинная доска в D (14') и `/2` в C, короткие D не плодить | S-план |
| `End Joists` | крайние joists другим сечением, hangers `LUC210 Zmax` (скрытые полки) | S-деталь |
| `Hangers` | `LUS210 Zmax` joist к ledger; `HUC212-2 Zmax` балка в балку; LVL-балка `HUC410 Zmax` | S-детали |
| Соединения балка к посту | `ML210Z`, `HL33Z`, through bolts + washers + nuts, SDS: каждое своей строкой, E = деталь | S-детали |
| `Decking` | под своим заголовком; `2x6 DuxxBak`, SQ FT: площадь одного балкона x units x 1.1 (`=CEILING(W*D*G*1.1,10)`, меньше 50 - до чётного), E = деталь; `5/4x6` только на террасе над гаражом (там subfloor `3/4" Ply` + sleepers `2x4 P.T.` + `5/4x6`) | A-деталь |
| `Fascia`, `Soffits`, `Post Wrap`, flashing | под заголовком trims (`Balcony Trims`), только если отделка в scope; Frame only - не вставлять | scope |

Бетонные и ферменные балконы (низ - жилое, LW concrete) в деревянный блок не входят: bases = 0 на этих стеках и нота `counted separately`.

## Перила

Railing всегда есть у балкона: либо системой, либо поэлементно, по детали. Не смешивать на одном балконе. Строки перил идут сразу за каркасом под своим заголовком (`Balcony Railing` или общий `Decking and Railing`), нота про систему под ним.

| Тип | Строки |
| --- | --- |
| Composite, Azek, система | нота про систему + `Posts at Rails 4x4 P.T.` (`=2*G`, два на балкон) + `Post Sleeve` + `Post Cap` + `Rail sections`: строка на каждую длину секции, в B `8' Rail section`, в D `unit`, в E сторона и её настоящая длина (`front 7'-4"`). Секция на пролёт между постами; длина секции - ближайшая стандартная больше стороны |
| Wood painted, поэлементно | `Posts at Rails 4x4 P.T.` (`=2*G`) + `Balustrades =EVEN(G*2.2)*units` (`pcs`) + `Rails (top & bottom) =EVEN(G*2.2)*units` (`LFT`) + `Cap Rail =EVEN(G*1.1)*units` (`LFT`), где G = длина перил одного балкона в LFT (периметр без стороны у стены), units = G заголовка блока |
| Aluminum, metal | нота `Note: Aluminum railing materials are by others; verify components.`; материал не считаем |

Типы систем и их состав: [Rails & Decking](../work/exterior-trims/rails-decking.md).

## Блок porch

- `Ceiling Joists 16" o.c.` + ledger + hangers обязательны и идут отдельно от rafters.
- Каркас porch на чертежах не показан - нота сразу под заголовком: `Note: Porch framing is not specified; all framing assumed; verify.`
- Porch над балконом с кровлей на фермах: только `Posts` + `Beams` (+ caps), units = стеки, rafters и ridge из шаблона убрать.
- Потолок porch с огнестойкой сборкой (на разрезе названа UL или GA сборка): одна строка `Soffit Gypsum (2)`, B `5/8" Type X`, C `=CEILING(G*2*1.1,2)*units`, D `SQ FT`, где G = площадь одного porch. Два слоя стоят в подписи и множителем `*2` один раз; двух строк гипса не бывает. Открытый porch без показанного потолка строку не получает.
- Rafter-блок настоящей кровли porch: box + ledger + sub fascia, ridge beam по детали.
- Лес porch, балкона, deck и навеса на улице всегда `P.T.`: посты, балки, joists, ledger, rafters, посты перил, под крышей он или нет. Обычный лес только внутри тёплого контура (пол эркера, внутренние посты). Крепёж снаружи и на P.T. с `Zmax` ([Hangers](hangers.md#dfl-format)).

## Блок holdowns { #holdowns }

Место: в секции стен того этажа, чьи shear walls держит holdown (`1st Floor Walls`, `2nd Floor Walls`), не в Framing List. Блок в конце секции: после последней строки `Tape` (под Box Sheathing), пустая строка до и после.

| Строка | C | Когда |
| --- | --- | --- |
| `Holdowns (1) btm` | `=G` | к бетону, нижний уровень, как нарисовано на плане |
| `Holdowns (2) btm top` | `=G*2` | через деревянное перекрытие: один снизу, другой сверху |

- B = модель по SW schedule (`HDU5-SDS2.5`), G = число точек из OurPlanCore, E = марка SW (`SW-2`). Строка на каждую модель.
- Holdown над балкой не требует transfer holdown ниже (указание клиента); явно показанный инженером крепёж не удалять. Threaded rod только если показан.
- Holdowns на плане не размечены: `TBD HD` + нота `Note: Locations of shear walls and holdowns are assumed; verify.`
- Анкеры shear walls: A текстом `SW Anchor Bolts 12" o.c.`, B размер из anchorage schedule (`1/2" Ø x 4" emb Titen HD`), E марка SW, шаг в H из таблицы sill and sole plate anchorage; washers одной строкой `=SUM(...)` с моделью (`BP1/2-3`). Wedge anchor не менять на Titen HD без основания; считать только для SW первого этажа к бетону; у двустороннего SW анкеровка двойная. Подробно: [Anchor Bolts](../work/deck/anchor-bolts.md), [Shear Wall](../work/vertical/sheathing/shear-wall.md).

<figure markdown>
  ![Holdown на стойке shear wall](../assets/images/photos/hardware/holdown-at-stud-base.jpg)
  <figcaption markdown="span">Holdown у основания стойки shear wall, анкер в бетон: строка `Holdowns (1) btm`. Фото: Thester11, CC BY-SA 3.0, [источник](https://commons.wikimedia.org/wiki/File:HoldDown.JPG)</figcaption>
</figure>

## Частые ошибки

- Балконный блок без своего множителя units или с множителем из чужого блока.
- Нота над заголовком блока; decking и railing прямо под заголовком каркаса; группа вынесена в конец листа.
- Porch зеркалён с балконов вместо отдельного счёта; porch SQFT на Front Page пуст.
- Три поста на перила вместо двух; система и поэлементный railing смешаны.
- Hangers балкона без `Zmax`; cap `BCS2-3/6` на всё подряд без учёта plies.
- Один holdown через деревянное перекрытие вместо двух; модель не из таблицы своего корпуса.

Все ошибки: [Deck, porch, балконы](../start/common-mistakes.md#deck), [Shear walls и holdowns](../start/common-mistakes.md#holdowns).

## Пример

```text
A                          B                  C                              D      E
#2 Upper Balcony List 8' x 6'   4 unit                                             (G заголовка = 4)
Posts                      6x6 P.T.           =2*G                           10     S4.1
Post Caps                  BC46 Zmax          =2*G                           pcs    3/S4.1
Beam (2)                   2x12 P.T.          =1*2*G                         8      B3
Joists 16" o.c.            2x12 P.T.          =CEILING((8*12/16+1)/2,1)*G    12     28 pcs 6'
Hangers                    LUS210 Zmax        =7*G                           pcs    7/S4.1

Balcony Decking and Railing                                                        (свой заголовок)
Note: Railing is composite per A6.2; posts, sleeves, caps and rail sections counted.
Decking                    2x6 DuxxBak        =CEILING(8*6*G*1.1,10)         SQ FT  5/A5.5
Posts at Rails             4x4 P.T.           =2*G                           4      assumed
Rail sections              8' Rail section    =1*G                           unit   front 7'-4"
Rail sections              6' Rail section    =2*G                           unit   sides 6'
```

Что получается при 4 балконах:

- `Posts`: 2 x 4 = 8 постов, в D длина поста 10'. `Beam (2)`: одна балка в два слоя на балкон, 1 x 2 x 4 = 8 досок по 8'.
- `Joists`: на ширину 8' при шаге 16" выходит 8 x 12 / 16 + 1 = 7 joists по 6'. Два куска по 6' режутся из доски 12', поэтому 4 доски на балкон, 16 на все; в D длина доски 12, число кусков в E.
- `Hangers`: joist висит на hanger у ledger, второй конец лежит на балке: 7 x 4 = 28.
- `Decking`: 8 x 6 x 4 x 1.1 = 211.2, вверх до 10 = 220 SQ FT.
- `Rail sections`: секция на пролёт между постами, длина секции - ближайшая стандартная больше стороны. Фронт 7'-4" закрывает одна секция 8', два бока по 6' - две секции 6'. На 4 балкона: 4 и 8.

## См. также

- [Frame (deck/porch/balcony)](../work/deck/deck-porch-balcony-frame.md), [Railing](../work/deck/railing.md), [Rails & Decking](../work/exterior-trims/rails-decking.md)
- [DFL: как устроена книга](dfl-overview.md), [Ноты в DFL](standard-notes.md), [Hardware catalog](hardware-catalog.md)
