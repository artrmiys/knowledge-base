# Exterior Walls (наружные стены)

<figure markdown>
  ![Разрез наружной стены с точками проверки](../../../assets/images/walls/exterior-wall-section.svg)
  <figcaption markdown="span">Наружная стена в разрезе: plates, studs, sheathing, WRB, insulation. Перед счётом раздели стену на слои и реши, какие из них в scope.</figcaption>
</figure>

## Что это

Exterior wall - стена по контуру здания с обшивкой снаружи. От внутренних
стен отличается слоями (sheathing, WRB, insulation), FRT-требованием и тем,
что все проёмы фасада вырезаются именно из неё. Стена на бетоне тянет за
собой [Sill Plates](sill-plates.md), а наверху - [Gable](gable.md),
[Parapet](parapet.md) и [Truss Heel](../sheathing/truss-heel.md).

## Где искать на чертежах

| Лист | Что взять |
| --- | --- |
| Планы этажей `a101 1st` | Контур и длина стен, марки типов стен |
| Wall type schedule (`wt`) | Сечение stud, шаг, слои, fire rating, FRT |
| Разрезы `a3.01 sec` | Высота стены, состав перекрытия, где кончается стена и начинается gable |
| Фасады `el`, energy sheets | Зоны Densglass и Zip, continuous insulation, смена материала |
| Структура `s101`, SW schedule | Shear walls, holdowns, blocking высоких стен |
| Code summary (`n`) | Тип конструкции: при Type III всё в плоскости наружной стены FRT |

## Как мерить в OurPlanCore

Инструмент **Line**, единица LFT. Точка листа **W** на плане этажа кладёт
новую линию в `walls/<этаж> floor walls`.

1. Веди линию по оси стены по реальным участкам. Выноски и размерные линии не обводятся.
2. Новая позиция при смене высоты, сечения, конструкции или стороны обшивки.
   Один участок с несколькими выносками остаётся одной линией.
3. Тип стены определяй по участкам, не группой: кусок demising между двумя
   наружными не становится `ext`.
4. Двойная стена - два каркаса только если на плане два каркаса.
5. Саму стену меряй в `walls` один раз как обычную (`ext`, `corr`, `dem`), даже
   если она несущая или shear. Марки BW и SW в `walls` отдельными линиями не
   рисуются: полоса несущей стены и участок SW обводятся ещё раз в своих ветках
   [BW](bearing-walls.md) и [Shear Wall](../sheathing/shear-wall.md). Длины
   трёх веток не складываются.
6. Каждой позиции свой Color.

<figure markdown>
  ![Line по наружным стенам с именем ext 2x6 9.09](../../../assets/images/ourplancore/v3/measure-line-walls.png)
  <figcaption markdown="span">Line по стенам 1-го этажа. Имя несёт категорию, сечение и высоту: `ext 2x6 9.09`.</figcaption>
</figure>

### Высота стены и стойки { #stud-height }

Высота в имени - высота стены **в сборе, с plates**: стойка + 1 нижняя + 2
верхние доски, в десятичных футах. Это **не** floor-to-floor и не отметка
потолка.

- Формула: floor-to-floor минус subfloor `3/4"` минус глубина перекрытия.
  Читай разрез каждого дома и проверь, льётся ли gypcrete поверх каркаса или
  внутрь.
- Plates **не вычитаются**: три стандартные доски (1 btm + 2 top) уже сидят
  в этой высоте.
- Вычитаются только доски сверх стандартных трёх, когда разрез их
  показывает: вторая btm plate, truss blocking поверх top plates.
- Голая стойка = высота стены минус `4 1/2"` (три доски по 1 1/2"). Отдельно
  её считать не нужно: таблица ниже и шаблон DFL работают от высоты стены.
- Пример: 9'-6" floor-to-floor минус TJI 11 7/8" минус 3/4" subfloor =
  8'-5 3/8" = 8.45'. Это высота стены и число в имени (`ext 2x6 8.45`); сама
  стойка 8'-0 7/8", по таблице ниже это 9' precut.

В DFL та же высота стены стоит в H и E строки студов (E в футах и дюймах до
1/8"), в имени стены - десятичные футы.

<figure markdown>
  ![Разрез: высота 9'-0", TJI 11 7/8", subfloor 3/4"](../../../assets/images/confluence/confluence-110.png)
  <figcaption markdown="span">Разрез кухни: высота стены 9'-0" стоит между subfloor и низом перекрытия выше. Красные линии - границы стены, а не отметки этажей.</figcaption>
</figure>

### Какая стойка по высоте стены { #precut }

Высота стены (с plates, как в имени) определяет, какую стойку заказывать:

| Высота стены | Стойка |
| --- | --- |
| 7'-0" ... 8'-1 5/8" | 8' precut (`92-5/8`) |
| 8'-1 3/4" ... 8'-4 1/2" | 8' full height stud |
| 8'-4 3/4" ... 9'-1 5/8" | 9' precut (`104-5/8`) |
| 9'-1 3/4" ... 10'-1 5/8" | 10' precut (`116-5/8`) |
| 10'-1 3/4" ... 10'-4 1/2" | 10' full height stud |
| 10'-4 3/4" ... 12'-4 1/2" | 12' |

- 9' full height studs не бывает, 11' стоек тоже не бывает.
- 10' precut - самый высокий precut.
- Короткие стойки режутся из длинных: 4' считать как 8', 5' как 10', 6' как 12'.
- Пример: стена 8'-4 1/2" - это 8' full height, стена 12'-2" - это 12' стойка. Гейблы не всегда 12'-ые: смотри высоту каждой стойки.

## Как назвать в дереве и строка DFL

Канон имени: `<категория> <сечение> <высота>`. Старые примеры с `x`
(`ext 2x6 x`) означают то же самое: `x` стоит на месте высоты.

| Имя в дереве | Что это | Строка DFL | Unit |
| --- | --- | --- | --- |
| `ext 2x6 9.09` | Наружная 2x6 высотой 9.09' | `Studs Ext`, `Plates Ext (1) btm` P.T., `Plates Ext (2) dbl top` | studs: штуки (в D длина стойки), plates: LFT |
| `corr 2x6 11.7` | Коридорная, см. [Corridor](corridor.md) | `Studs Corridor`, `Plates Corr` | то же |
| `dem 2x6 9.09` | Межквартирная, см. [Demising](demising.md) | `Studs Demising`, `Plates Demising` | то же |
| `dem (2) 2x6 9.09` | Двойная demising, два одинаковых каркаса | те же строки `Demising`, длина линии удваивается | то же |
| `furr 2x4 9.09` | Furring wall, см. [Furring](furring.md) | `Plates Furring`, `Furring` | LFT |
| `2x4 9.09` | Обычная перегородка без префикса | `Studs Interior`, `Plates Interior` | то же |
| `2x6 half` | Половинная стена | `Studs Interior half`, plates как у перегородки | то же |

Со стеной в DFL идут:

- `Bracing Ext Walls` `2x4` - в **штуках**: одна доска на каждые 8 LFT стены
  (`=G/8*1.1`), в D длина доски по самой высокой стене группы (до 10' = 14, до 12' = 16,
  до 16' = 18, выше = 20). Только для стен от 7' и выше.
- `Blocking` в LFT, `Wall Sheathing` в листах `4x8`.
- `Vapor Barrier` в SQ FT - подпись шаблона; в B пишется WRB из спецификации,
  не Tyvek по умолчанию. При Zip этой строки нет: барьер уже в листе,
  остаётся только `Tape`.
- `Insulation` в SQ FT - только continuous insulation снаружи обшивки.
  Утеплитель между стойками by others, строки нет.
- `Holdowns` и `Ext. Headers`.

Факторы стоек (16" = 1.1, 24" = 0.625) - один канон в
[Формулах](../../../reference/formulas.md#stud-spacing-factors). Кнопка `WL`
полосы XL переносит стены в блок этажа; суффикс после высоты (`ext 2x6 10.09
5/S400`) отделяется сам.

Правила слоёв - на отдельных страницах: [Wall Sheathing](../sheathing/wall-sheathing.md),
[Exterior Wall Materials](../sheathing/exterior-materials.md). FRT: если
наружная стена FRT, то FRT и blocking, и парапет, и headers в её плоскости.
Build-out фасада считай отдельно на вертикаль и горизонталь, FRT по узлу.
Metal stud и CMU стены: каркас by others, но exterior gypsum, insulation,
flashing и window jambs остаются нашими ([Metal Tracks](metal-tracks.md)).

## Частые ошибки

- Высота стены взята как floor-to-floor или отметка потолка, или из неё ещё раз вычтены plates.
- Тип стены задан группой: corridor и demising перепутаны, кусок demising попал в exterior.
- P.T. plate на деревянном перекрытии: P.T. только на бетоне и кладке.
- Двойная нижняя plate везде, хотя деталь показывает её только на части этажей.
- В строке барьера записан Tyvek при fluid-applied WRB: продукт из спецификации.
- Проёмы вычтены из обшивки дважды или не вычтены вовсе.
- Пропущены rigid insulation, Densglass по зонам фасада, dropped soffit с RCP.

Разбор с примерами: [все ошибки по стенам](../../../start/common-mistakes.md#walls).

## Пример

```text
walls/
  1st floor walls/
    ext 2x6 9.09      Line, 412.3 LFT
    corr 2x6 9.09     Line, 161.0 LFT
    dem (2) 2x4 9.09  Line, 96.5 LFT
    2x4 9.09          Line, 540.8 LFT
  2nd floor walls/
    ext 2x6 8.45      Line, 410.9 LFT
```

## См. также

- [Bearing Walls](bearing-walls.md), [Sill Plates](sill-plates.md), [Corners](corners.md)
- [Wall Panels](wall-panels.md): что в панели, что loose
- [Имена takeoffs и точки листа](../../../reference/takeoff-naming.md)
- [Windows and Doors](../openings/windows-doors.md), [Headers](../openings/headers.md)
- [Советы и важные вещи](../../../reference/boss-feedback-rules.md#studs)
