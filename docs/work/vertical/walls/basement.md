# Basement Walls (стены подвала)

<figure markdown>
  ![Цокольная стена на бетонной плите](../../../assets/images/walls/basement-wall-section.svg)
  <figcaption markdown="span">Деревянная стена подвала на плите: btm plate P.T., studs, box sheathing и WRB по верху. Бетонная стена подвала каркаса не даёт.</figcaption>
</figure>

## Что это

Basement walls - деревянные стены уровня `base`: наружные на плите, стены
под подиумом, перегородки и коридоры подвала. Это полноценная stick-стена
со своими plates, studs и обшивкой, даже когда дом выше идёт панелями.
Площадь этажа считается отдельно в [Basement SQFT](../../sqfts/basement.md),
здесь только каркас.

## Где искать на чертежах

| Лист | Что взять |
| --- | --- |
| План подвала `a100 base` | Какие стены деревянные, какие бетон или CMU |
| Foundation plan `s101 f` | Плита, фундаментные стены, sill plates |
| Wall section у плиты | Высота стойки: на подвале часто три разные высоты |
| Wall type schedule | Сечение, P.T., furring у бетона |
| Code summary | FRT ниже podium при Type III |

## Как мерить в OurPlanCore

Инструмент **Line**, единица LFT, на плане `a100 base` (точка W, уровень B).
Ветка `walls/base floor walls`, имена как у обычных стен:
`ext 2x6 9.24`, `corr 2x6 9.24`, `2x4 9.24`.

1. Бетонная или CMU стена каркаса не даёт: не рисуй её в `walls`. Furring
   перед бетоном - отдельная позиция `furr 2x4 9.24` ([Furring](furring.md)).
2. Высота по разрезу каждого участка: в подвале перекрытие и балки меняют
   высоту чаще, чем на этажах. Одна высота на весь подвал - ошибка.
3. Стены под concrete slab или podium считаются stick даже на panel-job
   ([Wall Panels](wall-panels.md)).
4. Metal walls подвала: каркас by others, но box sheathing, WRB и flashing
   остаются нашими ([Metal Tracks](metal-tracks.md)).

## Как назвать в дереве и строка DFL

| Имя в дереве | Строка DFL | Материал | Unit | Формула / фактор |
| --- | --- | --- | --- | --- |
| `ext 2x6 9.24` | `Plates Ext (1) btm` | `2x6 P.T.` (на бетоне всегда) | LFT | `LFT x 1.1` |
| то же | `Plates Ext (2) dbl top` | `2x6` | LFT | `LFT x 2 x 1.1` |
| то же | `Studs Ext` | размер по высоте | pcs | `LFT x 1.1` (16") |
| то же | `Blocking` `2x`, `Bracing` `2x4` | | LFT | по типу стены |
| то же | `Box Sheathing` OSB, `Vapor Barrier` (WRB по спецификации) | | 4x8, SQ FT | [Box Sheathing](../sheathing/box-sheathing.md) |
| `corr 2x6 9.24` | `Plates Corr btm` `2x6 P.T.` или `LSL P.T.` | | LFT | по детали |
| проёмы подвала | `Window Flashing`, `Sill Flashing` | | LFT | [Window Flashing](../openings/window-flashing.md) |
| `2x4 9.24` (под podium) | `Studs Interior` FRT при Type III | | pcs | нота с источником |

## Частые ошибки

- Одна высота стойки на весь подвал при трёх разных высотах по разрезу.
- Высота взята как floor-to-floor без вычета subfloor и перекрытия.
- Стены ниже podium выброшены как "panels by others".
- Бетонная стена обведена как деревянная.
- Treated furring подвала не выделен в отдельную P.T.-сборку.
- В строке `Vapor Barrier` записан Tyvek, хотя спецификация даёт другой WRB.

Разбор с примерами: [все ошибки по стенам](../../../start/common-mistakes.md#walls).

## Пример

```text
walls/base floor walls/
  ext 2x6 10.3        Line, 21.1 LFT    Notes: W4A, 1/A701, FRT below podium
  ext 2x6 9.24        Line, 15.7 LFT
  furr 2x4 9.24       Line, 36.8 LFT    Notes: 8/A500, P.T. at concrete
```

## См. также

- [Sill Plates](sill-plates.md), [Exterior Walls](exterior.md), [Corridor Walls](corridor.md)
- [Box Sheathing](../sheathing/box-sheathing.md), [Furring](furring.md)
- [Basement SQFT](../../sqfts/basement.md)
