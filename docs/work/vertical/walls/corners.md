# Corners (углы стен)

<figure markdown>
  ![Три варианта угла в плане: 2-stud, 3-stud, California corner](../../../assets/images/framing/corners.svg)
  <figcaption markdown="span">Угол стены в плане: 2-stud L, 3-stud, California corner с backing под gypsum. Stick: отдельная строка по этажам. Panels: не считаем.</figcaption>
</figure>

<!-- TODO-PHOTO: three stud corner wood framing photo, EN query "three stud corner framing" -->

## Что это

Corner - пакет стоек на стыке двух стен: 2, 3 стойки или California corner.
Фактор студов `1.1` (одна стойка на фут плюс waste) закрывает обрезь и стойки
у проёмов, но углы и T-пересечения на stick-каркасе считаются отдельной
строкой. На panel-job углы уже внутри панели.

## Где искать на чертежах

| Лист | Что взять |
| --- | --- |
| Планы этажей | Число наружных углов и T-пересечений по этажу |
| Typical wall details, corner detail | Сколько стоек в углу, backing под gypsum |
| Structural details | Corner holdowns, extra studs, где called out |
| Scope | Stick или panels: на panel-job углы не считаем |

## Как мерить в OurPlanCore

Инструмент **Count** (точки), по одной в каждый наружный угол и каждое
T-пересечение на плане этажа. Позиция `corners` в
`walls/<этаж> floor walls` (точка W кладёт Count в walls; слово `corners`
само считается wall-токеном). Свой CountSymbol, чтобы точки отличались от holdowns.

## Как назвать в дереве и строка DFL

| Имя в дереве | Строка DFL | Unit | Формула / фактор |
| --- | --- | --- | --- |
| `corners` (Count, 1-й этаж) | `Corners` 2x6 (сечение стены) | pcs | `углы x стоек в углу` (2 или 3 по детали), длина = высота стойки |
| `corners` (Count, 2-й этаж) | `Corners` отдельной строкой | pcs | по этажам, не одной суммой |

Если деталь угла не показана, пиши видимую ноту: `Corners assumed 3 studs; verify`.

## Частые ошибки

- Углы посчитаны на panel-job: они уже в панели.
- Все этажи сложены в одну строку.
- T-пересечения и backing забыты, хотя деталь их показывает.
- Угол посчитан 2 стойки при детали с 3.

Разбор с примерами: [все ошибки по стенам](../../../start/common-mistakes.md#walls).

## Пример

```text
walls/1st floor walls/
  corners      Count, 14 ea     Notes: 3-stud per 5/A701
walls/2nd floor walls/
  corners      Count, 14 ea
```

## См. также

- [Exterior Walls](exterior.md), [Sill Plates](sill-plates.md)
- [COM Commercial: studs, extra, dbl](../../../work-types/com.md)
- [Hardware catalog](../../../reference/hardware-catalog.md)
