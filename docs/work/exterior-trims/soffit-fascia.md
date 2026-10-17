# Soffit & Fascia (подшивка свесов, торцевые доски, columns)

<!-- TODO-PHOTO: house eave with vented soffit panel, fascia board and frieze under it, EN: "roof eave soffit fascia frieze house" -->

<figure markdown>
  ![Cornice eave return](../../assets/images/trims/ext-eave-return.png)
  <figcaption markdown="span">Угол фронтона: eave с soffit и fascia уходит вдоль стены, rake по скату, в углу return. Proper cornice return это отдельный набор строк.</figcaption>
</figure>

## Что это

Soffit (подшивка свеса), fascia (торцевая доска), frieze (доска по стене
под soffit), rake moulding, returns и columns porch. Обычно отдельный блок
`Soffits and Fascias`. Длины eves и rakes приходят из
[Eve](../sheathing-and-misc/eve.md) и [Rake](../sheathing-and-misc/rake.md);
обшивка soffit (5/8" exterior gypsum, plywood) это
[Sheathing](../vertical/sheathing/wall-sheathing.md), не trim.

## Где искать на чертежах

| Лист | Что взять |
| --- | --- |
| Eave и rake details (A5xx) | Ширина свеса, материал soffit (vinyl vented, beadboard, 1x), fascia, frieze, rake moulding |
| Elevations | Где eaves, где rakes, returns (cornice или pork-chop), columns и их тип |
| RCP и porch sections | Потолок porch и canopy: материал, площадь, 5/8" exterior gypsum под отделкой |
| Spec | `Soffits assumed Vinyl; Fascias assumed PVC or 1x Alum wrapped; verify` |

## Как мерить в OurPlanCore

Длины свесов это Line в `eves rakes/eves` и `eves rakes/rakes` с выносом в
дюймах в имени (`eve 24 main`, `rake 12 main`, `returns 12`): одна линия
питает и trim, и обшивку свеса. Soffit как площадь (beadboard, panel) это
Area по реальному нижнему контуру в `trims` или в принятой ветке проекта
(`rcp 1.6`), контур не равен roof deck. Не корми одну площадь дважды:
или `длина x ширина`, или Area. Canopy не входит в eve и rake, у него свои
строки. Columns это Count точками.

## Как назвать в дереве и строка DFL

| Имя в дереве | Строка DFL | Size | Unit | Правило |
| --- | --- | --- | --- | --- |
| `eves rakes/eves/eve 24 main` | `Soffits at Eves` | `12" Vinyl vented`, `1x12`, `T&G beadboard` | LFT или SQ FT | доска постоянной ширины LFT; panel и beadboard SQ FT = длина x вынос |
| | `Fascia at Eves` | `1x8`, `2x8`, `5/4x10` | LFT | |
| | `Frieze` | `5/4x6` / `5/4x8` | LFT | по стене под soffit |
| | `Trim over fascia` | `1x3` / `1x4` | LFT | доп. полоса |
| `eves rakes/rakes/rake 12 main` | `Soffits at Rakes`, `Fascia at Rakes` | `1x8`, `9" Vinyl` | LFT / SQ FT | отдельно от eves: другой размер и материал |
| | `Rake Moulding`, `Crown at Frieze` | `3" crown` | LFT | |
| `eves rakes/eves/returns 12` | `Soffit / Fascia / Crown at Returns` | по детали | LFT | cornice return как мини-набор; pork-chop только fascia и малый soffit |
| `trims/soffit porch` | `Soffits at Porch`, `at Canopy`, `at Floor Overhangs` | `Beadboard`, `Azek Beadboard` | SQ FT | свои строки, не в main eves |
| `trims/columns` | `Columns` | `12" Dia Fbg Non-taper w/c&b` | pcs + высота | `w/c&b`, taper, round/square в строке; высота отдельно |
| | `Column wrap` | `1x8` | LFT | обшивка стойки, не column |
| | `Posts at Rails`, `Post Sleeve`, `Post cap` | `4x4 P.T.`, `Sleeve for 4x4` | pcs | набор, см. [Rails & Decking](rails-decking.md) |

Материал не указан: `Note: Soffits assumed Vinyl; Fascias assumed PVC or
1x Alum wrapped; verify`. Не подставляй wood, если возможен vinyl или alum.

<figure markdown>
  ![Pork-chop eave return](../../assets/images/trims/ext-pork-chop.png)
  <figcaption markdown="span">Pork-chop return: простой треугольный обрубок. Trim минимальный, но fascia и маленький soffit считаем.</figcaption>
</figure>

## Частые ошибки

- Canopy и porch посчитаны повторно в eve и rake.
- Soffit panel посчитан и как LFT x ширина, и как Area.
- Eves и rakes одной строкой при разных размерах.
- Returns не определены (cornice или pork-chop), trim по returns пропущен.
- Columns без типа, taper и высоты; column wrap перепутан с column.
- 5/8" exterior gypsum soffit записан в trim вместо обшивки и WRB.
- Все ошибки по крыше: [Крыша](../../start/common-mistakes.md#roof).

## Пример

```text
Takeoffs/Main/eves rakes/eves/eve 24 main     Line   310 LFT
Takeoffs/Main/eves rakes/rakes/rake 12 main   Line   96 LFT

Soffits at Eves     12" Vinyl vented   620  SQ FT  =310*2
Fascia at Eves      1x8                310  LFT
Frieze              5/4x6              310  LFT
Soffits at Rakes    9" Vinyl           96   LFT
Fascia at Rakes     1x6                96   LFT
Columns             12" Dia Fbg Non-taper w/c&b   4  pcs   8'
```

## См. также

- [Overview](overview.md), [Casing, Corner & Band](casing-corner-band.md), [Porch / Deck / Balcony](porch-deck-balcony.md)
- [Eve](../sheathing-and-misc/eve.md), [Rake](../sheathing-and-misc/rake.md), [Returns](../sheathing-and-misc/returns.md), [Canopy](../horizontal/roof-framing/canopy.md)
- [Porch SQFT](../sqfts/porch.md), [Standard notes](../../reference/standard-notes.md)
