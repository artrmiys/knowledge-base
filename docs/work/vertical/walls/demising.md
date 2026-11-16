# Demising Walls (межквартирные стены)

<figure markdown>
  ![Двойная demising стена в разрезе с draft stop и gypsum, в плане одна линия](../../../assets/images/walls/demising-double-wall.svg)
  <figcaption markdown="span">Двойная demising стена: два каркаса с зазором, gypsum с обеих сторон, draft stop в перекрытии. Одинаковые каркасы меряются одной линией `dem (2) 2x4 9.09` по оси стены, длина в DFL удваивается сама.</figcaption>
</figure>

## Что это

Demising (party) wall - стена между двумя квартирами. Бывает одинарной и
двойной: два самостоятельных каркаса с воздушным зазором. Она rated,
часто несёт double studs на нижних этажах и требует draft stop в
перекрытии и на чердаке. Стена квартира-коридор - это [Corridor](corridor.md).

## Где искать на чертежах

| Лист | Что взять |
| --- | --- |
| Планы этажей `a101 1st` | Марка типа стены между юнитами; один каркас или два |
| Wall type schedule (`wt`), UL assembly | Сечение каждого каркаса, слои gypsum, sound insulation |
| Детали стыка с перекрытием (`a701`) | Draft stop (`1/2" OSB`), solid blocking, acoustic sealant |
| Stud schedule, S-планы | Double studs, марки BW на demising |
| SW schedule | Shear sheathing на одной стороне demising |
| Draftstops plan, roof plan | Draft stop на чердаке: см. [Gable](gable.md) |

<figure markdown>
  ![Деталь unit separation wall type 2 с draft stop](../../../assets/images/confluence/confluence-058.png)
  <figcaption markdown="span">Деталь dwelling unit separation wall: 1/2" OSB draft stop над стеной, solid blocking на концах joists, fire-rated seal. Draft stop здесь - отдельная строка, не часть обшивки.</figcaption>
</figure>

## Как мерить в OurPlanCore

Инструмент **Line**, единица LFT, на плане этажа (точка W).

1. Имя `dem 2x6 9.09`: категория, сечение, высота.
2. Двойная стена с одинаковыми каркасами - **одна линия** по оси стены:
   `dem (2) 2x4 9.09`. `(2)` в имени удваивает длину при переносе в DFL, вторую
   линию не рисуй.
3. Двойная стена с разными каркасами бок о бок - тоже одна линия, в имени оба
   сечения и обе высоты в одном порядке: `dem 2x4 2x6 9.09 11.16`.
4. Staggered studs на одной plate (стойки 2x4 вразбежку на plate 2x6) - это
   один каркас: `dem 2x6 stag 9.09`, не `(2)`.
5. Двойной каркас только если на плане два каркаса: не делай стену двойной по названию.
6. Draft stop в перекрытии не рисуется отдельно: его длина равна длине
   demising стены, площадь считается в DFL. Draft stop чердака - треугольник
   Area в `gables/gable trusses/draft stop` на архитектурном плане кровли.
7. Несущая demising дополнительно обводится в `BW/<этаж>` по марке.

## Как назвать в дереве и строка DFL

| Имя в дереве | Строка DFL | Unit | Формула / фактор |
| --- | --- | --- | --- |
| `dem 2x6 9.09` | `Plates Demising (1) btm`, `(2) top` | LFT | `LFT x 1.1`, `x 2 x 1.1` |
| то же | `Studs Demising` 2x6 | штуки, в D длина стойки | `LFT x 1.1` (16") или `x 0.625` (24") |
| то же | `Bracing Demising` 2x4 | штуки, в D длина доски: до 10' = 14, до 12' = 16, до 16' = 18, выше = 20 | `LFT / 8 x 1.1`: одна доска на 8 LFT стены; только стены от 7' |
| то же | `Blocking` | LFT | по матрице шаблона, до чётного |
| то же | `Draft Stop` `1/2" OSB` (материал по детали) | SQ FT | `LFT x глубина перекрытия x 1.1`, обычный материал, не P.T.; строка стоит в секции Gable Walls, отдельно от чердачного Draft Stop |
| `dem (2) 2x6 9.09` | те же строки, одна группа на оба каркаса | | длина линии `x 2` (удваивает макрос) |
| марка BW на demising | `Extra Studs Demising 16" o.c.` (шаг по stud schedule) | штуки | [Bearing Walls](bearing-walls.md) |

Опора гипса там, где joists параллельны стене (у demising с обеих сторон), -
строка `Blocking for Drywall` (`2x4`, `=ОКРВВЕРХ(G/D;1)`, D `16`) в Floor Framing
List этажа, а не в стенах. Строки `Bracing for Drywall` в DFL нет:
[Bracing стен и Blocking for Drywall](../../horizontal/floor-framing/details/bracingdrywall.md).

Shear sheathing на demising может быть с одной стороны или на части длины:
по SW schedule, страница [Shear Wall](../sheathing/shear-wall.md). Hangers над
demising с gypsum под перекрытием - `ITS`; `DHU` только над настоящей fire
wall по детали.

## Частые ошибки

- Draft stop пропущен или скопирован из суммы shear walls.
- Draft stop записан P.T. или его толщина не сверена с деталью (7/16" против 1/2").
- Стена сделана двойной по слову "demising", хотя на плане один каркас.
- Двойная стена обведена двумя линиями и названа `dem (2)`: длина удвоилась дважды.
- Staggered стена названа `dem (2) 2x4` вместо `dem 2x6 stag`.
- Тип задан группой: 10 LFT demising попали в exterior, коридорная стена названа `dem`.
- Double studs нижних этажей из stud schedule не выписаны.
- Межэтажный draft stop и чердачный draft stop смешаны в одну строку.

Разбор с примерами: [все ошибки по стенам](../../../start/common-mistakes.md#walls).

## Пример

```text
walls/
  3rd floor walls/
    dem (2) 2x6 9.09    Line, 282.4 LFT     (двойная стена, одинаковые каркасы: одна линия)
    dem 2x4 9.09        Line, 36.0 LFT      (одинарная у лестницы)
gables/
  gable trusses/
    draft stop          Area, 3 треугольника   Notes: A1-00, A4.1
```

## См. также

- [Corridor Walls](corridor.md), [Bearing Walls](bearing-walls.md), [Gable](gable.md)
- [Shear Wall](../sheathing/shear-wall.md), [Bracing стен и Blocking for Drywall](../../horizontal/floor-framing/details/bracingdrywall.md)
- [Hangers](../../../reference/hangers.md)
