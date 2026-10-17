# Corridor Walls (коридорные стены)

<figure markdown>
  ![Staggered stud wall: два ряда стоек 2x4 на plates 2x6](../../../assets/images/confluence/confluence-062.png)
  <figcaption markdown="span">Staggered stud wall: стойки 2x4 двумя рядами вразбежку на одной plate 2x6, утеплитель змейкой. В DFL это plates 2x6 и два ряда studs 2x4.</figcaption>
</figure>

<!-- TODO-PHOTO: staggered stud wall framing photo, EN query "staggered stud wall framing" -->

## Что это

Corridor wall - стена между квартирой и общей зоной: коридор, лестница,
гараж, вестибюль. Она fire-rated, часто на 2x6 plates со staggered 2x4
стойками, и над ней идёт ledger или drywall bracing, когда перекрытие
параллельно. Стена между двумя квартирами - это уже [Demising](demising.md),
а стена шахты - [Shaft](shaft.md).

## Где искать на чертежах

| Лист | Что взять |
| --- | --- |
| Планы этажей `a101 1st` | Марки типов стен вдоль коридоров, лестниц, гаража |
| Wall type schedule (`wt`), UL assembly | Сечение plates и studs, staggered или нет, слои gypsum, rating |
| Разрез у коридора, детали S | Ledger, corridor joists `2x10` на ledger, blocking, hangers |
| Door schedule | Fire-rated unit entry doors (`3070 ... C-lbl`) |
| Stud schedule | Если коридорная стена ещё и несущая: марка в [BW](bearing-walls.md) |

## Как мерить в OurPlanCore

Инструмент **Line**, единица LFT, на плане этажа (точка W).

1. Категория по участкам: отрезок стены у лестницы и у гаража - тоже `corr`,
   даже если он продолжает demising.
2. Имя `corr 2x6 11.7`: категория, сечение plates, высота. Двойной коридор
   (два каркаса на плане) - `corr (2) 2x6 11.7`.
3. Staggered стена - одна линия: plates по имени `2x6`, два ряда стоек
   учитываются в DFL.
4. Новая позиция при смене высоты или сечения. Высота - по разрезу своего
   дома, не floor-to-floor ([Exterior: высота стойки](exterior.md#stud-height)).
5. Если тип стены несущий, та же стена отдельно обводится в `BW/<этаж>`.

## Как назвать в дереве и строка DFL

| Имя в дереве | Строка DFL | Unit | Формула / фактор |
| --- | --- | --- | --- |
| `corr 2x6 11.7` | `Plates Corr (1) btm` 2x6 (P.T. только на бетоне) | LFT | `LFT x 1.1` |
| то же | `Plates Corr (2) dbl top` 2x6 | LFT | `LFT x 2 x 1.1` |
| то же | `Studs Corr` 2x4 staggered | pcs | `LFT x 1.1 x 2` (два ряда по 16") |
| то же | `Bracing Corridor` 2x4 | LFT | по высоте стены |
| то же | `Blocking` | LFT | по типу стены |
| то же | `Bracing for Drywall` 2x4 | LFT | где перекрытие параллельно стене |
| `corr (2) 2x6 11.7` | те же строки на два каркаса | | `x 2` |

Hangers над коридорной стеной - обычные `ITS`, если gypsum заканчивается
ниже перекрытия. `DHU` / `DGU` только там, где joists заходят над настоящей
fire wall по детали (лестница, лифт, шахта): [Hangers](../../../reference/hangers.md).
Corridor joists на кровле без детали - нота с причиной, а не `Optional` без
объяснения ([Standard notes](../../../reference/standard-notes.md)).

## Частые ошибки

- Corridor и demising перепутаны группой: в проверке 241 LF коридора стали 161, а demising выросла с 577 до 648.
- Кусок коридорной стены у лестницы записан как `ext`.
- `DHU` поставлены только потому, что стена коридорная.
- Staggered стена посчитана одним рядом стоек.
- Plates 2x6 забыты: студы 2x4, и plates записаны 2x4.
- Ledger и крепёж коридорных joists не выписаны отдельными строками по детали.

Разбор с примерами: [все ошибки по стенам](../../../start/common-mistakes.md#walls).

## Пример

```text
walls/
  2nd floor walls/
    corr 2x6 9.09        Line, 161.0 LFT
    corr (2) 2x6 9.09    Line, 24.5 LFT   (две стены у лестницы)
    dem 2x6 9.09         Line, 648.2 LFT
```

## См. также

- [Demising Walls](demising.md), [Unit Walls](unit.md), [Shaft Walls](shaft.md)
- [Bracing for Drywall](../../horizontal/floor-framing/details/bracingdrywall.md)
- [Hangers](../../../reference/hangers.md): ITS против DHU
- [Советы и важные вещи](../../../reference/boss-feedback-rules.md#dhu-dgu-vs-its)
