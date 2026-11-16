# Door and Window Trim (список дверей и наличники)

<figure markdown>
  ![Baseboard and door casing](../../assets/images/photos/trims/base-and-casing.jpg)
  <figcaption markdown="span">Baseboard и door casing на одной стене: base считаем периметром, casing формулой от списка дверей. Фото: gemteck1, CC BY 2.0, [источник](https://www.flickr.com/photos/65303620@N00/712932547)</figcaption>
</figure>

## Что это

Список interior doors и cased openings по этажам с обозначением размера и
типа, из которого формулой считается casing. Door schedule главнее плана:
если он есть, заполняй из него. Формула casing на странице
[Casing](casing.md), окна изнутри (casing, stool, apron) только когда они
есть в finish schedule или details.

## Где искать на чертежах

| Лист | Что взять |
| --- | --- |
| Door schedule (`dr sch`) | Размер, тип (pocket, slider, bi-fold), материал, `F.R.`, `S.C.` |
| Планы этажей | Символ открытой двери (считать по нему, не по стене), cased openings `C.O.` |
| Finish schedule, interior elevations | Casing, stool, apron у окон; профиль trim |
| Notes | Производитель или special product: оставить в ноте, не сводить к размеру |

## Как мерить в OurPlanCore

Двери считаются Count точками по символу открытой двери, по итему на
размер и тип (`2680`, `(2)2680`, `4080 C.O.`), отдельно на каждый этаж.
Shower glass doors не входят. Unit entry doors с fire rating отмечай в
имени (`2680 F.R.`), hardware numbers не нужны.

## Обозначения размеров

Код размера читается так: первые цифры это ширина (футы и дюймы), последние
две это высота (фут и дюймы). `2680` = 2'-6" x 8'-0", `3068` = 3'-0" x 6'-8",
`9068` = 9'-0" x 6'-8". Дверь шире 3'-6" пишется парой: `5070` в schedule
это `(2)2670`, `4070` это `(2)2070`.

| Пример | Значение | Как записать |
| --- | --- | --- |
| `2680` | 2'-6" x 8'-0" | обычная single interior door |
| `(2)2680` | две двери 2'-6" x 8'-0" | double door, pair marker виден |
| `2680 Pocket` | pocket door | слово `Pocket` остаётся |
| `(2)3080 Slider` | две створки 3'-0" x 8'-0" | quantity и `Slider` остаются |
| `(2)2668 Bi-Fold` | closet bi-fold, две створки 2'-6" x 6'-8" | `Bi-Fold`, не сводить к slider |
| `9068` bi-fold в schedule | широкий bi-fold 9'-0" x 6'-8" | шире 3'-6", значит парой: `(2)4668 Bi-Fold`; складные панели внутри створки отдельно не считаем |
| `2680 Metal F.R. S.C.` | metal, fire-rated, self-closing | garage и mechanical; `F.R.` и `S.C.` остаются |
| `4080 C.O.` | cased opening 4'-0" x 8'-0" | вводить как cased opening, не как door |

Код стоит первым в колонке B, слова типа после него: формула шаблона читает
код и удваивает пары, от этого зависит casing. Высота дверей не указана:
принимай 6'-8" и пиши ноту в шапке.

`F.R.` у двери значит fire-rated (дверь, рама и hardware как сборка).
Не путать с `FRT`: это fire-retardant-treated пиломатериал каркаса.

## Как назвать в дереве и строка DFL

| Имя в дереве | Строка DFL | Unit | Правило |
| --- | --- | --- | --- |
| `openings/1/2680` | `Int. Doors`, в B `2680` | unit | по этажам, из schedule |
| `openings/1/(2)2680` | `Int. Doors`, в B `(2)2680` | unit | double как pair |
| `openings/1/4080 C.O.` | `Cased Openings`, в B `4080 C.O.` | unit | отдельно от дверей, после пустой строки |
| | `Casing for Int. Doors` | LFT | `=CEILING(2*SUM(perimeters)/12*1.1,10)`, см. [Casing](casing.md) |
| | `Interior Doors&Trims` | | заголовок блока с нотой о профиле |

Ввод в Excel:

1. Все двери и cased openings вводятся по этажам до формул casing.
2. Код размера стоит первым в колонке B (`2680`, `(2)2680 Bi-Fold`). Шаблон
   сам переводит его в периметр в дюймах в колонке G: `2680` это 30" + 2 x
   96" = 222", умноженные на количество; пара `(2)` удваивается.
3. Формулу в G не трогай и не заменяй числом: из суммы G считается casing.
   Одинаковые двери это одна строка с количеством, а не несколько строк.
4. Перед выводом выдели ячейки количества и сравни сумму в строке
   состояния с числом дверей на планах.

## Частые ошибки

- Двери посчитаны по стене или по ноте рядом, а не по символу двери.
- Складные панели bi-fold посчитаны как отдельные двери.
- Дверь шире 3'-6" записана одной дверью, а не парой `(2)`.
- `9068` прочитан как 9'-0" x 8'-0": последние две цифры это высота 6'-8".
- Shower glass doors введены как interior doors.
- `Pocket`, `Slider`, `F.R. S.C.` потеряны при переносе в Excel.
- Cased opening введён как дверь.
- Все ошибки по Excel: [Excel DFL и ноты](../../start/common-mistakes.md#excel).

## Пример

```text
Takeoffs/Main/openings/1/2680          Count   18
Takeoffs/Main/openings/1/(2)2680       Count   3
Takeoffs/Main/openings/1/4080 C.O.     Count   2
Takeoffs/Main/openings/1/2680 Pocket   Count   2

Int. Doors       2680           18   unit   A601
Int. Doors       (2)2680        3    unit   A601
Int. Doors       2680 Pocket    2    unit   A601

Cased Openings   4080 C.O.      2    unit   A601

Casing for Int. Doors   1x3-1/2   1150  LFT   =CEILING(2*SUM(G)/12*1.1,10)

Периметры: 2680 = 222", пара (2)2680 = 444", 4080 C.O. = 240"
SUM = 222 x 18 + 444 x 3 + 222 x 2 + 240 x 2 = 6252"
2 x 6252 / 12 = 1042 LFT, x 1.1 = 1146.2, вверх до 10 = 1150 LFT
```

<details class="kb-figures kb-figures--rows">
  <summary>Показать 8 архивных карточек с иллюстрациями</summary>
  <figure class="kb-figure-row">
    <figcaption class="kb-figure-row__text">
      <div class="kb-figure-row__title">Считать по символу открытой двери</div>
      <div class="kb-figure-row__rule">Считай настоящий swing, а не ноту у стены.</div>
    </figcaption>
    <a class="kb-figure-row__image" href="../../../assets/images/trims/int-trims-26.png" target="_blank" rel="noopener"><img src="../../../assets/images/trims/int-trims-26.png" alt="Interior door measured by open door symbol" loading="lazy"></a>
  </figure>
  <figure class="kb-figure-row">
    <figcaption class="kb-figure-row__text">
      <div class="kb-figure-row__title">Size notation 2680</div>
      <div class="kb-figure-row__rule"><code>2680</code> = 2'-6" x 8'-0". Держи обозначение одинаковым до переноса в Excel.</div>
    </figcaption>
    <a class="kb-figure-row__image" href="../../../assets/images/trims/int-trims-27.png" target="_blank" rel="noopener"><img src="../../../assets/images/trims/int-trims-27.png" alt="Door size notation 2680" loading="lazy"></a>
  </figure>
  <figure class="kb-figure-row">
    <figcaption class="kb-figure-row__text">
      <div class="kb-figure-row__title">Double doors</div>
      <div class="kb-figure-row__rule">Пиши <code>(2)2680</code>, pair marker виден.</div>
    </figcaption>
    <a class="kb-figure-row__image" href="../../../assets/images/trims/int-trims-28.png" target="_blank" rel="noopener"><img src="../../../assets/images/trims/int-trims-28.png" alt="Double door notation" loading="lazy"></a>
  </figure>
  <figure class="kb-figure-row">
    <figcaption class="kb-figure-row__text">
      <div class="kb-figure-row__title">Pocket и Slider</div>
      <div class="kb-figure-row__rule"><code>2680 Pocket</code>, <code>(2)3080 Slider</code>: тип остаётся в обозначении.</div>
    </figcaption>
    <a class="kb-figure-row__image" href="../../../assets/images/trims/int-trims-29.png" target="_blank" rel="noopener"><img src="../../../assets/images/trims/int-trims-29.png" alt="Pocket door notation" loading="lazy"></a>
  </figure>
  <figure class="kb-figure-row">
    <figcaption class="kb-figure-row__text">
      <div class="kb-figure-row__title">Shower glass doors</div>
      <div class="kb-figure-row__rule">Не вводи как interior doors: это shower scope.</div>
    </figcaption>
    <a class="kb-figure-row__image" href="../../../assets/images/trims/int-trims-31.png" target="_blank" rel="noopener"><img src="../../../assets/images/trims/int-trims-31.png" alt="Shower glass doors not counted as interior doors" loading="lazy"></a>
  </figure>
  <figure class="kb-figure-row">
    <figcaption class="kb-figure-row__text">
      <div class="kb-figure-row__title">Cased opening</div>
      <div class="kb-figure-row__rule"><code>C.O.</code> это проём без двери, вводится отдельно.</div>
    </figcaption>
    <a class="kb-figure-row__image" href="../../../assets/images/trims/int-trims-34.png" target="_blank" rel="noopener"><img src="../../../assets/images/trims/int-trims-34.png" alt="Cased opening example" loading="lazy"></a>
  </figure>
  <figure class="kb-figure-row">
    <figcaption class="kb-figure-row__text">
      <div class="kb-figure-row__title">Ввод по этажам и helper table</div>
      <div class="kb-figure-row__rule">Двери и C.O. по этажам; mark и quantity в helper table для формул casing.</div>
    </figcaption>
    <a class="kb-figure-row__image" href="../../../assets/images/trims/int-trims-37.png" target="_blank" rel="noopener"><img src="../../../assets/images/trims/int-trims-37.png" alt="Doors and cased openings Excel table" loading="lazy"></a>
  </figure>
  <figure class="kb-figure-row">
    <figcaption class="kb-figure-row__text">
      <div class="kb-figure-row__title">Есть door schedule</div>
      <div class="kb-figure-row__rule">Сначала заполняй из schedule, план вторичен.</div>
    </figcaption>
    <a class="kb-figure-row__image" href="../../../assets/images/trims/int-trims-43.png" target="_blank" rel="noopener"><img src="../../../assets/images/trims/int-trims-43.png" alt="Fill from door schedule when available" loading="lazy"></a>
  </figure>
</details>

## См. также

- [Casing](casing.md), [Base](base.md), [Room Schedule](room-schedule.md), [Interior Trims](overview.md)
- [Windows and Doors](../vertical/openings/windows-doors.md), [Standard notes](../../reference/standard-notes.md)
