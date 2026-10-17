# Hip (наружное ребро крыши)

<figure markdown>
  ![Hip rafters выделены жёлтым](../../../assets/images/confluence/confluence-142.png)
  <figcaption markdown="span">Архивный 3D-вид: жёлтым выделены hip rafters, наружные рёбра, где два ската сходятся выпуклым углом. Вверху та же крыша в плане: линия hip на плане короче настоящей доски.</figcaption>
</figure>

<!-- TODO-PHOTO: hip rafter with jack rafters during roof framing, EN query "hip rafter jack rafters roof framing" -->

## Что это

Hip - наклонное наружное ребро, где два ската сходятся выпуклым углом. Hip rafter идёт от угла стены к коньку, длиннее и часто глубже common rafter (`2x12` при rafters `2x10`), в него упираются jack rafters. Внутреннее ребро - [Valley](valley.md); верх - [Ridge](ridge.md). При крыше из trusses hip собран из hip trusses by others, считаем только детали вокруг.

## Где искать на чертежах

| Лист | Что взять |
| --- | --- |
| Roof plan (A) | где hips, уклон скатов с обеих сторон |
| Roof framing plan (S) | сечение hip rafter, stick или trusses, марка |
| Sections, elevations | подъём крыши, наклонная длина |
| Details | опирание hip на угол стены и на ridge, hangers и ties |

## Как мерить в OurPlanCore

Инструмент Beam (B) по линии hip на листе roof framing с точкой F. Линия на плане - горизонтальная проекция; настоящая длина длиннее. Два пути:

1. Взять наклонную длину с разреза или фасада, где hip виден в истинную величину.
2. Умножить плановую длину на коэффициент hip. Для hip под 45 градусов в плане (одинаковые уклоны с двух сторон): `sqrt(1 + (pitch/12)^2 / 2)`.

| Уклон | Коэффициент common rafter | Коэффициент hip и valley (45 градусов в плане) |
| --- | --- | --- |
| 4:12 | 1.054 | 1.027 |
| 6:12 | 1.118 | 1.061 |
| 8:12 | 1.202 | 1.106 |
| 10:12 | 1.302 | 1.161 |
| 12:12 | 1.414 | 1.225 |

Разные уклоны по сторонам hip - только по разрезу. Программа округляет итог до заказной длины (до 8' до фута, длиннее до чётного).

<figure markdown>
  ![Инструмент Beam](../../../assets/images/ourplancore/v3/measure-beam.png)
  <figcaption markdown="span">Инструмент Beam: две точки по элементу, длина округляется программой и попадает в имя позиции.</figcaption>
</figure>

## Как назвать в дереве и строка DFL

Путь: `framing/roof framing/beams/hip <сечение> <длина>`. Если шаблон проекта считает hip, valley и ridge одной строкой, Label `Ridge / Valley / Hip` в LFT.

| Имя в дереве | A (Label) | B | C | D | E |
| --- | --- | --- | --- | --- | --- |
| `beams/hip 2x12 18` | `Hip Rafters` | `2x12` | точки | `18` | `S201` |
| `beams/hip (2) 1 3/4 x 11 7/8 LVL 22` | `Hip Rafters (2)` | `1 3/4 x 11 7/8 LVL` | точки | `22` | `HB1` |
| Line по ridge, hip и valley | `Ridge / Valley / Hip` | `2x12` | `=ОКРВВЕРХ(G*1.1/D;1)` | `16` | |

## Частые ошибки

- Hip посчитан у truss-крыши: там hip trusses by others.
- Длина взята с плана без коэффициента или по коэффициенту common rafter (1.118 вместо 1.061).
- Jack rafters к hip не посчитаны отдельно или посчитаны как полные common rafters.
- Hip и valley перепутаны: наружный угол и внутренний угол.
- Engineered hip beam записан без продукта и plies.
- [Все ошибки по крыше](../../../start/common-mistakes.md#roof)

## Пример

| A | B | C | D | E |
| --- | --- | --- | --- | --- |
| `Hip Rafters` | `2x12` | 4 | 18 | `S201, pitch 6:12` |
| `Rafters 16" o.c.` | `2x10` | 28 | 16 | `jack rafters at hips` |

## См. также

- [Valley](valley.md), [Ridge](ridge.md), [Dbl / Trpl Rafters](dbl-trpl-rafters.md)
- [Ridge / Valley / Hip (обзор)](../../sheathing-and-misc/ridgevalleyhip.md), [Roof SQFT](../../sqfts/roof.md), [Hangers](../../../reference/hangers.md)
