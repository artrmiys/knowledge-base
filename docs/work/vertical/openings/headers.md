# Headers (перемычки над проёмами)

<figure markdown>
  ![Header над проёмом на jack studs, king studs по краям](../../../assets/images/openings/header.svg)
  <figcaption markdown="span">Header лежит на jack studs, king studs держат пакет по краям. `(2)` и `(3)` в имени - число слоёв (plies).</figcaption>
</figure>

<!-- TODO-PHOTO: window header with king and jack studs, wood framing photo, EN query "window header king stud jack stud framing" -->

## Что это

Header - балка над проёмом в стене, передаёт нагрузку на jack studs.
Наружные (`ext`) и внутренние (`int`) считаются раздельно, размер и число
plies - из header schedule, не из ширины окна. На panel-job headers внутри
панелей не считаем, только flush и loose. Header крыши (roof header) - другая
тема: [Roof Framing: Header](../../horizontal/roof-framing/header.md).

## Где искать на чертежах

| Лист | Что взять |
| --- | --- |
| Header schedule (S), типовые детали стены | Марка и сечение по пролёту и этажу: `H228`, `HPA`, `(3) 2x10` |
| Планы с тегами (`s102`) | Марки над проёмами, где инженер их показал |
| Window и door schedule, фасады | Ширина проёма, составные проёмы |
| Панельные чертежи, scope | Что внутри панели, что flush или loose |
| Code summary | FRT у headers в плоскости наружной стены при Type III |

## Как мерить в OurPlanCore

Инструмент **Count** (point), один на физический header, или **Beam** по
пролёту между опорами: Beam сам меряет длину и округляет её в имени (до 8'
вверх до целого фута, длиннее - до чётного).

1. Ветка `framing/<этаж> framing/headers/ext/` и `.../headers/int/`. Точка F
   на S-листе кладёт Count в `framing/<этаж> framing`; дальше в `headers/ext`
   переносом или выбором папки перед New Item.
2. Имя: `ext H228 4`, `int H228 4`, `HPA 4`, `ext (3) 2x10 8` - сторона,
   марка или сечение с plies, заказная длина в футах.
3. Этаж папки - реальный bearing scope, не номер архитектурного фасада.
4. Один built-up header = одна точка с `(n)`; не ставь n точек.
5. Storefront из нескольких окон не обязательно даёт столько же headers;
   составной проём может иметь общий header.
6. Деревянный header отдельно от стального элемента и его nailer.

## Как назвать в дереве и строка DFL

Кнопка `HD` полосы XL кладёт headers в блок стен этажа **ниже**; сторона
`ext` / `int` берётся из имени. В легенде `LG` строка `HP2 - (2) 2x10`
даёт размер по коду, иначе в B попадёт код.

| Имя в дереве | Строка DFL | Unit | Формула / фактор |
| --- | --- | --- | --- |
| `ext H228 4` | `Ext. Headers (2) up to 48"` `2x8` | pcs | штук x plies, длина из имени |
| `ext H228 7` | `Ext. Headers (2) up to 72"` | pcs | |
| `ext (3) 2x10 8` | `Ext. Headers (3) over 72"` `2x10` | pcs | три доски на header |
| `int H228 4` | `Int. Headers (2)` | pcs | |
| `9.0x6.8 gd` ворота | `Garage headers (3)` | pcs | по schedule |
| нет на плане | нота `The headers indicated on the plan...` | | чёрный жирный текст без заливки |

Если наружная стена FRT, headers в её плоскости тоже FRT; LVL/PSL в
плоскости наружной стены при Type III не ставятся. Образцы нот:
[Ноты в DFL](../../../reference/standard-notes.md).

## Частые ошибки

- Header выведен из ширины окна: разные несущие условия дают разные марки.
- `(3)` введено одной доской.
- Headers внутри панелей посчитаны на panel-job.
- Этаж взят по фасаду, а не по bearing scope; верхние этажи имеют другие размеры.
- Наружные headers без FRT при Type III (в проверке: 4-й этаж целиком).
- Один составной проём записан как два headers.

Разбор с примерами: [все ошибки по проёмам](../../../start/common-mistakes.md#openings).

## Пример

```text
framing/2nd floor framing/headers/
  ext/
    ext H228 4        Count, 14 ea
    ext (3) 2x10 8    Count, 2 ea     Notes: 4/S501, FRT per A001
  int/
    int H228 4        Count, 9 ea
```

## См. также

- [Windows and Doors](windows-doors.md), [Exterior Walls](../walls/exterior.md), [Wall Panels](../walls/wall-panels.md)
- [Beam](../../horizontal/floor-framing/beam.md): инструмент Beam и округление
- [Подписи строк DFL](../../../reference/takeoff-items.md)
