# Wall Panels (панельные стены: что считаем)

<figure markdown>
  ![Состав деревянной wall panel: plates, studs и framing проёма](../../../assets/images/walls/wall-panel-sbca.png){ width="760" style="background:#fff;padding:12px;border-radius:8px" }
  <figcaption markdown="span">Состав wall panel: plates, studs, каркас проёма, иногда sheathing и WRB. Иллюстрация SBCA. Что именно входит в поставку, решает проект, а не картинка.</figcaption>
</figure>

## Что это

Wall panel - заводской участок стены (studs, plates, каркас проёмов, часто
одна сторона sheathing и WRB). На panel-job мы не дублируем заводской
каркас, а считаем loose scope и stick-исключения. Слово `panels` в scope не
означает "стены не считать": стены всё равно меряются полностью, чтобы
обшивка, headers, holdowns и исключения считались от реальных длин.

## Где искать на чертежах

| Источник | Что взять |
| --- | --- |
| Scope-тег проекта (`Frame. Wall panels`), письмо клиента | Panel-job или нет; что клиент хочет видеть loose |
| Разрезы и планы | Какие стены ниже плиты или podium, какие внутри existing frame |
| Wall type schedule, SW schedule | Какая сторона sheathing в панели, какая loose |
| Panel drawings, если есть | Номера панелей, RO, bearing points |
| Details | Headers flush, build-up, короткие и наклонные стены |

## Как мерить в OurPlanCore

Стены меряются как обычно: [Exterior](exterior.md), [Corridor](corridor.md),
[Demising](demising.md), [BW](bearing-walls.md). Отличия panel-job:

1. Headers внутри панелей не рисуются: только flush и loose по scope
   ([Headers](../openings/headers.md)).
2. Sheathing одной стороны уже в панели; отдельно только требуемая вторая
   сторона и loose зоны ([Shear Wall](../sheathing/shear-wall.md)).
3. Stick-участки отмечай отдельными позициями или нотой: под плитой, в
   existing frame, короткие и наклонные.

## Правила E-Wood (подтверждены владельцем 2026-10-09)

| Участок | Что делаем |
| --- | --- |
| Обычная стена в panel package | Заводской каркас не дублируем; считаем loose scope |
| Стена под concrete slab / podium | Считаем stick: studs, plates, headers, sheathing |
| Новая стена внутри existing frame (reconstruction) | Считаем stick по объёму новой работы |
| Короткая стена, irregular sloped wall | Stick-исключение |
| Exterior build-up wall | Возможное исключение; проверяем конструкцию, не исключаем все build-ups автоматически |
| Wood wall рядом с CMU | Может быть panelized; соседство с CMU не повод для optional stick |
| Furring под insulation/siding | Отдельные рейки по detail и scope |
| Shaft, elevator | Всегда фиксируем; материал и package определяем, не теряем из-за `panels by others` |

"Под бетоном" и "на бетоне" различаются: стена, которая стоит P.T. plate
на бетонном основании, может быть panelized; исключение - стены **ниже**
плиты или podium. Границу на mixed-здании определяй по разрезам, не по
имени этажа. Полный список в
[Советах](../../../reference/boss-feedback-rules.md#wall-panels).

## Как назвать в дереве и строка DFL

| Элемент | Проверка перед отдельной строкой |
| --- | --- |
| Studs, plates, corners, in-panel blocking | В package - не считаем; в stick-исключениях считаем полностью |
| Headers, king/jack/cripple | Только flush и loose; слово `special header` само по себе не доказывает loose |
| Sheathing, shear plywood | Какая сторона и слой в панели; loose зоны по details |
| WRB, insulation, exterior gypsum | Могут быть в поставке или field scope; не дублируем и не исключаем без проверки |
| Sill plates, gasket, anchors, holdowns, straps | Свои connections, заводской каркас их не закрывает |
| Double top plate, splice | Часть монтируется в поле: проверяем loose material |
| Box sheathing, truss heel, parapet, gable, roof edge | Каждый узел отдельно; это не часть панели автоматически |
| Beams, posts, hangers, ledgers | Свой structural schedule и scope |

### Reconstruction: existing не значит "не считать" { #reconstruction-existing }

Существующую конструкцию не пересчитываем, а новые стены, замену,
reinforcement, connections и заданные покрытия считаем. Если деталь требует
new subfloor over all existing flooring, включаем всю площадь нового слоя.
Пристройка и ремонт внутри existing frame могут иметь разный scope; слово
`reconstruction` само по себе не включает и не выключает панельное правило.
Подробно: [Reconstruction](../../../work-types/reconstruction.md).

В DFL на этажах с панелями stick-блок остаётся под локальной нотой
`Note: Optional stick frame, if walls are not panels; verify`. Шаблонная
нота `Walls are panels by others` удаляется, если панелей в scope нет.
Optional без причины ревьюер снимает: у каждого optional-блока нота, почему.

## Частые ошибки

- Шахты и стены ниже podium выброшены вместе с панелями.
- Все build-ups автоматически stick; или furring у CMU добавлен как optional.
- Sheathing второй стороны посчитан, хотя одна сторона в панели и второй по schedule нет.
- Headers внутри панелей посчитаны ещё раз.
- `Optional` без объяснения, почему; shown framing назван optional из-за отсутствующего spacing.
- Новый subfloor поверх existing пола пропущен, хотя деталь его требует.

Разбор с примерами: [все ошибки по стенам](../../../start/common-mistakes.md#walls).

## Пример

```text
Note: Walls are panels by others; walls below podium counted as stick framing.
Note: Optional stick frame, if walls are not panels; verify.      (под заголовком этажа)
Note: New walls within existing frame counted as stick framing.
```

## См. также

- [COM Commercial](../../../work-types/com.md), [Reconstruction](../../../work-types/reconstruction.md)
- [Exterior Walls](exterior.md), [Furring](furring.md), [Shaft Walls](shaft.md)
- [Советы и важные вещи: Wall panels](../../../reference/boss-feedback-rules.md#wall-panels)
- [SBCA: Wall Panels](https://www.sbcacomponents.com/wall-panels)
