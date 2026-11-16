# Deck / Porch / Balcony Frame (каркас балконов, порчей и deck)

<figure markdown>
  ![Porch deck framing: P.T. ledger, joists, rim, posts](../../assets/images/photos/deck/porch-deck-framing.jpg)
  <figcaption markdown="span">Каркас porch deck: P.T. ledger у стены дома, joists с hangers, rim по периметру, посты. Каждый элемент в DFL своя строка. Фото: NPS Photo, public domain, [источник](https://commons.wikimedia.org/wiki/File:Framing_for_the_front_porch_deck_is_being_installed._%28defb68bd-1bfc-4ad2-bacf-bbdd675758c9%29.jpg)</figcaption>
</figure>

<figure markdown>
  ![Deck framing plan](../../assets/images/framing/deck-frame-plan.svg)
  <figcaption markdown="span">План каркаса: ledger к зданию, joists и hangers, beam на posts, rim и blocking. Единицы: posts, beam и joists штуками с длиной доски в D, hangers pcs.</figcaption>
</figure>

## Что это

Структурный каркас открытых площадок: posts с base и cap, beams, ledger,
box или rim, joists с hangers, blocking, sleepers, structural subfloor,
stringers. **Balcony** стоит у стены верхнего этажа на постах или консоли,
**porch** это крытое крыльцо с крышей и потолком (ceiling joists), **deck**
это площадка у земли на постах. Отделка (decking как finish, soffit, trims,
перила по типу) живёт на страницах
[Balcony build-up](../exterior-trims/balcony-buildup.md) и
[Rails & Decking](../exterior-trims/rails-decking.md); здесь только несущее.

## Где искать на чертежах

| Лист | Что взять |
| --- | --- |
| Планы этажей A1xx | Балконные двери (tag), размер W x D каждого типа, сколько штук и на каких этажах |
| S-планы перекрытий | Callout deck joists (сечение, шаг), марки балок B1..B5, посты |
| Разрезы A4xx и детали S3xx/S6xx | Ledger и его крепёж, post cap и base, hangers, End Joists, flush или dropped beam |
| Schedule постов и крепежа (S6xx) | Модель cap по числу plies, base, through bolts |
| Roof plan и разрез porch | Крыша porch, ceiling joists, потолок (gypsum), есть ли каркас вообще |

Дверь без callout деревянных joists на S-плане обычно значит бетон или
фермы под балконом (terrace над гаражом). Это отдельный блок, не копия
деревянного.

## Как мерить в OurPlanCore

1. Площадь: `sqfts/blcny` и `sqfts/porch`, инструмент Area по реальному
   контуру на листе с точкой W. Разные балконы не соединять перемычкой;
   прямоугольник под известное число не рисовать.
2. Блоки: один Count-итем на **тип** балкона в папке `Balcony blocks`
   (porch в `Porch blocks`), точка на каждый экземпляр. Имя итема
   `#4 Balcony 12.9x7.83 (2GZO x7)`, где `x7` равно числу точек; в Notes
   точки unit-тег, сторона и этаж (`2GZO S 2nd fl`). Точки ставят на копиях
   план-листов (`a120 balcony`), рабочие планы остаются чистыми. Число точек
   равно множителю G заголовка блока в Excel.
3. Счёт экземпляров: балконные двери на планах, умноженные на этажи, со
   сверкой по deck-joist callout на S-планах.
4. **Porch считать отдельно по планам**, не зеркалить с балконов: число
   блоков, размеры и количество порчей обычно не совпадают с балконами.
5. Узлы с номером детали (`5/S311`) считаются Line-итемом в
   `framing/<этаж>/details`, по итему на деталь; см.
   [Framing details](../horizontal/floor-framing/details/rim.md).

<figure markdown>
  ![Count points for balcony blocks](../../assets/images/ourplancore/v3/measure-count.png)
  <figcaption markdown="span">Count точками: одна точка на каждый экземпляр балкона, имя итема несёт тип, размер и число экземпляров.</figcaption>
</figure>

<figure markdown>
  ![Разрез балкона у стены](../../assets/images/framing/balcony-block-section.svg)
  <figcaption markdown="span">Балкон у стены: ledger со screws, joists P.T. на hangers Zmax, end joist, beam на посту с cap, decking и перила. Каждая выноска это строка блока в DFL.</figcaption>
</figure>

## Как назвать в дереве и строка DFL

Заголовок блока: `#N Upper Balcony List W' x D' <G> unit`; porch
`#N Porch Framing List W' x D'`, заливка A:B зелёная `99CC00`; каркас ground deck
обязательно со словами `Deck` и `Frame` или `Framing`. Группа стоит внутри Framing,
decking, railing и trims идут за каркасом под своими заголовками, ноты под
заголовком: [Формат файла, группы](../../reference/dfl-overview.md#groups). Строки с
нулём и пустые строки шаблона удаляются. Подробный состав блока с формулами:
[Блоки DFL](../../reference/dfl-blocks.md).

В формулах W и D - ширина и глубина одного балкона в футах, G - число
экземпляров из заголовка блока. У досок (posts, beam, ledger, box, joists) в
колонке D стоит заказная длина доски в футах, в C число досок; `LFT` у них не
пишется.

| Имя в дереве | Строка DFL | Unit (D) | Формула или правило |
| --- | --- | --- | --- |
| `Balcony blocks/#1 Balcony 12x8 (x6)` | `Posts` `6x6 P.T.` | длина поста (10, 12) | 2 на балкон, `=2*G`; угловой балкон у двух стен может нести 1 |
| | `Post Bases` | pcs | `=C<posts>`; на бетоне `ABU66 Zmax`, на дереве `ABA66 Zmax`; модель со schedule важнее |
| | `Post Caps` | pcs | `=C<posts>`; по числу plies балки: 3-ply `BCS2-3/6 Zmax`, 2-ply `BC46 Zmax`; читать schedule |
| | `Beam (3)` `2x12 P.T.` фронт (B4), `Beam (2)` `2x12 P.T.` бока (B3) | длина доски | C = plies x число балок x G: `=3*G`; D - чётная длина не короче балки; марка в E |
| | `Ledger` `2x12 P.T.` | длина доски | `=1*G`, D не короче ширины балкона |
| | `Screws (8) at Ledger` или `Screws at Ledger`, `SDWS22400DB` | pcs | деталь даёт число: `=8*G`; деталь даёт шаг (два ряда на 16"): `=CEILING(W*12/16*2*G,3)` |
| | `Box` тем же сечением, что joists | длина доски | `=1*G`; только когда балка идёт под joists, у flush beam строки нет |
| | `Joists 16" o.c.` `2x12 P.T.` | длина доски | на балкон `CEILING(W*12/16,1)+1`, C = это число x G, D не короче глубины; короткие joists: одна длинная доска на два куска, `=CEILING(n*G/2,1)` |
| | `Hangers` `LUS210 Zmax`, `End Joists` + `LUC210 Zmax`, `HUC212-2 Zmax` | pcs | 2 на joist, когда оба конца висят (ledger и flush beam); балка под joists: 1 на joist, у ledger; снаружи всегда Zmax |
| | `Decking` `2x6 DuxxBak` | SQ FT | `=CEILING(W*D*G*1.1,10)`: запас 1.1 всегда, меньше 50 - вверх до 2; `5/4x6` только на Terrace над гаражом |
| `Porch blocks/#1 Porch 12x7 (x5)` | `Ceiling Joists 16" o.c.` + `Ledger` + `Hangers` | длина доски, pcs | число joists `CEILING(W*12/16,1)+1` x G; отдельно от rafters, обязательно |
| | `Beam (2)` `2x10` (B1), `Beam (3)` `2x10` (B2) | длина доски | plies x число балок x G; коды porch отличаются от балконных |
| | `Soffit Gypsum (2)`, `5/8" Type X` или плита по assembly | SQ FT | два слоя - одна строка: `(2)` в подписи и x 2 в формуле один раз, `=CEILING(W*D*2*1.1,2)*G` |

Terrace над гаражом (фермы и LW concrete): `Subfloor 3/4" Ply` в листах
4x8, `Sleepers 2x4 P.T.` (на террасу `CEILING(W*12/16,1)+1` штук, в D длина
доски не короче глубины), `Decking 5/4x6`; bases у таких стеков 0.

## Правила, которые ломают блок

- Посты на улице (porch, балкон, перила) всегда `P.T.`, и под крышей porch
  тоже. Остальной каркас под крышей (rafters, ceiling joists): P.T. или нет,
  решает чертёж.
- Каркас porch не показан: сразу под заголовком блока
  `Note: Porch framing is not specified; all framing assumed; verify`.
- Все узлы соединений с S-листа своей строкой с деталью в E: балка к посту
  (`ML210 Zmax`, `HL33 Zmax`, through bolts с washers и nuts, SDS), балка в балку
  (`HUC...-2`), крайние joists другим сечением (`End Joists`). Формат записи
  крепежа: [Hangers: как записывать крепёж в DFL](../../reference/hangers.md#dfl-format).
- Перила: 2 поста на балкон, система или поэлементно по типу, см.
  [Rails & Decking](../exterior-trims/rails-decking.md) и [Railing](railing.md).
- Flashings, Trims, Soffits, Post Wrap только когда они в scope; при
  Frame only их не вставлять. Исключение - `Flashings at Wall` у Terrace с
  мембраной: это строка самого блока.
- Порч и балкон стопкой: в Front Page строка Porches заполняется отдельно,
  балкон её не заменяет.

## Частые ошибки

- Балконный блок без своего множителя units (900 SF вместо 60).
- Порчи зеркалены с балконов вместо отдельного счёта по планам.
- Post cap по умолчанию `BCS2-3/6 Zmax` вместо модели по plies со schedule.
- Hangers только на один конец при flush beam, или без Zmax на улице.
- Posts не P.T. на улице (под крышей porch посты тоже P.T.).
- Beam и joists записаны в `LFT`, decking без 1.1, два слоя гипса умножены дважды.
- Porch SQFT на Front Page пустой; canopy и porch повторно в eve и rake.
- Все ошибки раздела: [Deck, porch, балконы](../../start/common-mistakes.md#deck).

## Пример

```text
Takeoffs/Main/sqfts/blcny                      Area   6 polygons
Takeoffs/Main/Balcony blocks/#1 Balcony 12x8 (2GZO x6)   Count 6 pts
Takeoffs/Main/Porch blocks/#1 Porch 12.8x7.3 (x5)        Count 5 pts

#1 Upper Balcony List 12' x 8' 6 unit
Posts             6x6 P.T.          12   12      =2*G                      S611
Post Bases        ABU66 Zmax        12   pcs     =C<posts>                 S611
Post Caps         BCS2-3/6 Zmax     12   pcs     =C<posts>, 3-ply          S611
Beam (3)          2x12 P.T.         18   12      =3*G                      B4
Joists 16" o.c.   2x12 P.T.         60   8       =10*G                     S130     12 x 12/16 = 9, плюс 1
Hangers           LUS210 Zmax      120   pcs     =2*10*G                   8/S311
Decking           2x6 DuxxBak      640   SQ FT   =CEILING(12*8*G*1.1,10)   5/A550   633.6, вверх до 10
```

## См. также

- [Блоки DFL](../../reference/dfl-blocks.md), [Rails & Decking](../exterior-trims/rails-decking.md), [Balcony build-up](../exterior-trims/balcony-buildup.md)
- [Railing](railing.md), [Balcony Trims](balcony-trims.md), [Anchor Bolts](anchor-bolts.md)
- [Beam](../horizontal/floor-framing/beam.md), [Joist](../horizontal/floor-framing/joist.md), [Post](../horizontal/floor-framing/post.md), [Hangers](../../reference/hangers.md)
- [Balcony SQFT](../sqfts/balcony.md), [Porch SQFT](../sqfts/porch.md), [Deck SQFT](../sqfts/deck.md), [Standard notes](../../reference/standard-notes.md)
