# Underlayment (что за siding: WRB, furring, accessories)

<figure markdown>
  ![Угол стены: furring strips поверх обшивки до siding](../../assets/images/photos/siding/furring-strips-over-sheathing-corner.jpg)
  <figcaption markdown="span">Угол дома до siding: поверх обшивки с функцией WRB прибиты вертикальные furring strips (rainscreen), внизу лента по стыку с фундаментом. Furring считается LFT по шагу на площадь стены, WRB - SQ FT по площади стены. Фото: greenbuildingadvisor.com, [источник](http://www.greenbuildingadvisor.com/blogs/dept/musings/all-about-rainscreens), найдено через Pinterest.</figcaption>
</figure>

## Что это

Слои между siding и каркасом, которые не видны на фасаде: WRB (weather
resistive barrier), sheathing, furring или rainscreen, Cedar Breather,
starter, J-channel и corner posts, flashing. Смотреть wall sections и wall
types, не только elevations. Sheathing считается в
[Wall Sheathing](../vertical/sheathing/wall-sheathing.md).

## Где искать на чертежах

| Лист | Что взять |
| --- | --- |
| Wall types (`wt`) и wall sections | Порядок слоёв: siding, furring, WRB, sheathing, studs |
| Spec division 07 и notes | Продукт WRB: housewrap (Tyvek), fluid-applied, self-adhered, Zip |
| Details окон и стыков | Z-flashing, head flashing, kickout, step flashing |
| Elevations | Vinyl: где starter, J-channel, corners |

## Слои стены снаружи внутрь

1. Siding (поле, `SQ FT`), см. [Типы siding](types.md).
2. Furring или rainscreen `1x4` / `2x4`, P.T. или нет (если показан).
3. WRB по спецификации, или Zip (WRB встроен в sheathing).
4. Sheathing (CDX, OSB, Zip): свой scope.
5. Stud wall.

<figure markdown>
  ![Слои стены снаружи внутрь](../../assets/images/siding/wall-layers-wrb.svg)
  <figcaption markdown="span">Siding, furring, WRB, sheathing, stud. WRB называется по спецификации, у Zip барьер уже встроен в лист.</figcaption>
</figure>

## WRB, не Vapor Barrier

| Строка DFL | Материал в B | Unit | Правило |
| --- | --- | --- | --- |
| `Vapor Barrier` (подпись шаблона) | `Tyvek` или другой housewrap | SQ FT | только если спецификация называет housewrap; `=CEILING(G*1.1,10)`, G = площадь обшивки этой стены |
| `Vapor Barrier` | `fluid-applied` (продукт по spec) | SQ FT | Tyvek не писать |
| `Wall Sheathing` + `Tape` (Zip system) | `7/16" Zip` + `Zip Tape` | 4x8, LFT | строки `Vapor Barrier` нет: барьер встроен в лист, не дублировать |

- Наружный барьер называется WRB, weather barrier или air barrier. Строка
  в шаблоне подписана `Vapor Barrier`, и эту подпись в колонке A не меняют;
  настоящий продукт пишется в B. Ошибка это написать `Vapor Barrier` как
  продукт или поставить Tyvek, когда спецификация называет другое.
- `Zip Tape` считается в `LFT`, не в rolls. Под `Wall Sheathing`:
  `=CEILING((G*0.4+P)*1.1,10)`, где G это SQ FT Zip этого этажа, P это
  периметр окон и дверей этого этажа из таблицы проёмов. Под Box, Gable и
  Truss Heel: `=CEILING(G*0.4*1.1,10)`. Zip на кровле:
  (листы x 32 x 0.4 + ridge + valleys) x 1.1.
- Площадь WRB равна площади обшивки стены: проёмы вычитаются по своему этажу
  и один раз, окна уже 4' не вычитаем, ворота гаража вычитаем (то же
  правило, что на [Wall Sheathing](../vertical/sheathing/wall-sheathing.md)).
  Soffit porch и canopy из exterior gypsum тоже идут в WRB.
- Спек-ячейки в шапке DFL заполняются при создании job: O4 WRB, O5 Zip, O6
  Zip Tape; ссылка на лист без слова `per` (`A3.0`).

## Furring / Rainscreen

Рейка между WRB и siding, часто пропускается. `1x4` или `2x4`, P.T. или
нет по разрезу; LFT по шагу или SQ FT, если сплошной. Полное правило и
jambs: [Furring & Window Jambs](../exterior-trims/furring-and-jambs.md).

## Cedar Breather

Вентилируемая сетка под cedar shingle или shake на сплошном основании.
Считается `SQ FT` площади shingle-стен; проверь детали, если siding
cedar shingle на solid sheathing.

## Vinyl accessories

| Строка DFL | Где | Unit |
| --- | --- | --- |
| `Starter strip` | низ первого ряда | LFT |
| `J-Channel` | вокруг окон и дверей, под soffit, у corner, по rake | LFT |
| `Corner posts` (outside, inside) | углы | LFT |
| `Undersill / finish trim` | под окном, у верха стены | LFT |

При vinyl `Ext Casing` нередко и есть `J-Channel`: не дублировать с
`5/4` wood casing. Канон: [Exclusions и J-Channel](../exterior-trims/exclusions.md).

## Flashing в siding

| Flashing | Где | Unit |
| --- | --- | --- |
| Z-flashing | горизонтальные стыки panel siding | LFT |
| Head flashing / drip cap | над окнами, дверями, head trim | LFT |
| Kickout flashing | крыша встречает стену | pcs |
| Step flashing | вдоль ската у стены | LFT |
| Band / watertable flashing | под горизонтальным поясом | LFT |

Flashing видимой строкой, не растворять в siding SQ FT. Оконный flashing
подробно: [Window flashing](../vertical/openings/window-flashing.md).

## Частые ошибки

- `Vapor Barrier` записан как продукт в B вместо WRB по спецификации; Tyvek при fluid-applied.
- Zip и отдельный housewrap посчитаны вместе.
- `Zip Tape` в rolls вместо LFT, или без периметра проёмов этажа.
- Furring пропущен, потому что нет на фасаде.
- Проёмы не вычтены из WRB или вычтены дважды.
- Все ошибки по обшивке: [Обшивка](../../start/common-mistakes.md#sheathing).

## Пример

```text
Vapor Barrier   fluid-applied (spec 07 27 26)   9270  SQ FT   =CEILING(8420*1.1,10)         A3.0
Furring         1x4 P.T. @ 16" o.c.             6950  LFT     =CEILING(8420*12/16*1.1,10)   7/A401
Cedar Breather                                  1240  SQ FT   gable shingle areas           A201

Те же стены на Zip: строки Vapor Barrier нет, вместо неё Tape
Wall Sheathing  7/16" Zip                       290   4x8     =CEILING(8420/32*1.1,1)
Tape            Zip Tape                        4410  LFT     =CEILING((8420*0.4+640)*1.1,10)

WRB: 8420 x 1.1 = 9262, вверх до 10 = 9270
Furring: 8420 x 12 / 16 = 6315, x 1.1 = 6946.5, вверх до 10 = 6950
Zip: 8420 / 32 = 263.1, x 1.1 = 289.4, вверх до целого = 290 листов
Tape: 8420 x 0.4 = 3368, + 640 LFT периметра проёмов = 4008, x 1.1 = 4408.8, вверх до 10 = 4410
```

## См. также

- [Siding](overview.md), [Типы siding](types.md), [Измерение](measure.md), [EIFS / Stucco / Veneer](eifs-stucco-veneer.md)
- [Wall Sheathing](../vertical/sheathing/wall-sheathing.md), [Exterior Wall Materials](../vertical/sheathing/exterior-materials.md), [Furring & Window Jambs](../exterior-trims/furring-and-jambs.md)
- [Material catalog](../../reference/material-catalog.md)
