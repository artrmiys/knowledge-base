# Правка takeoff: Merge, Split, Break, Ends, Combine, Similar

Здесь - как собрать, разделить и достроить уже нарисованные замеры без перерисовки. Нужно, когда одна позиция оказалась в двух takeoff, когда Excel нужен по листам, когда из линий надо получить точки или когда площади легли внахлёст.

<figure markdown>
  ![Кнопки Merge, Split и Combine на полосе инструментов](../assets/images/ourplancore/v3/tool-merge-split.png)
  <figcaption markdown="span">Полоса инструментов: Merge, Split и список Combine. Break и Ends стоят левее, рядом с P Line.</figcaption>
</figure>

## Шпаргалка

| Кнопка | Клавиша | Что делает | С чем работает |
| --- | --- | --- | --- |
| Merge | ++ctrl+m++ | объединяет целые takeoff (выбор в дереве) или сегменты одного takeoff (выбор на листе) | Takeoffs, лист |
| Split | ++ctrl+shift+m++ | разделяет takeoff по секциям или по листам; на листе - отделяет сегменты или метки | Takeoffs, лист |
| Break | ++ctrl+shift+b++ | каждая Line разбивается на отдельные односегментные замеры | Line |
| Break H/V (точка на кнопке Break) | ++ctrl+shift+v++ | сегменты уходят в два takeoff: `<имя> - Horizontal` и `<имя> - Vertical` | Line |
| Ends | нет | Count-метки на обоих концах каждого сегмента Line | Line |
| P Line | нет | Count-метки вдоль Line с заданным шагом | Line |
| Combine | нет | Union, Subtract, Intersect, Remove Overlap, Divide для двух и более Area | Area |
| Cut | ++x++ | вырез в Area или стирание куска Line; ++f9++ - боксом | Area, Line |
| Similar | нет | поиск одинаковых символов на листе и на других листах | Count |

Все кнопки есть и в Command Palette (++ctrl+shift+p++): `Break Lines Into Segments`, `Break Lines Into Horizontal / Vertical`, `Count Points At Line Ends`, `Combine Areas: Union` и так далее. Клавиши без назначения можно задать в [редакторе клавиш](ourplancore-shortcuts.md#remap).

## Два режима Merge и Split

- **Выделение в дереве Takeoffs** (Ctrl или Shift по строкам): работают целые takeoff со всеми секциями на всех листах. Так собирают одинаковые позиции с разных этажей и делят позицию перед Excel.
- **Выделение на листе** инструментом Select: работают сегменты и метки одного takeoff. Так склеивают две линии стены в одну или отделяют кусок.

Отмена для дерева - ++ctrl+z++ с фокусом в панели Takeoffs или ПКМ `Undo Takeoff Merge / Split`. Отмена на листе - обычный ++ctrl+z++ во вьюпорте.

## Merge целых takeoff

<figure markdown>
  ![Диалог Merge Selected Takeoffs](../assets/images/ourplancore/v3/merge-dialog.png)
  <figcaption markdown="span">Диалог Merge: выбрать, какой takeoff остаётся; остальные переезжают в него секциями.</figcaption>
</figure>

1. В Takeoffs выделите две и больше позиций одного типа (Count с Count, Line с Line, Area с Area, J Area с J Area).
2. Нажмите `Merge`, ++ctrl+m++ или ПКМ `Merge Selected Takeoffs...`.
3. Выберите позицию, которая останется. Её имя, папка, цвет и свойства сохраняются.
4. Все секции остальных позиций со всех листов переезжают в неё. Геометрия не склеивается: линии остаются отдельными сегментами, метки - отдельными метками.
5. Строка состояния: `Merged 3 takeoffs into ext 2x6 9.09 (12 sections). Ctrl+Z in Takeoffs to undo.`

Удалённые при объединении позиции уходят в `AI_Context/takeoff-merge-trash` внутри проекта, откат делает ++ctrl+z++ в дереве.

## Split целых takeoff

<figure markdown>
  ![Диалог Split Selected Takeoffs](../assets/images/ourplancore/v3/split-dialog.png)
  <figcaption markdown="span">Два режима: каждая секция в свой takeoff или один takeoff на лист.</figcaption>
</figure>

1. Выделите позицию (или несколько) в Takeoffs.
2. `Split`, ++ctrl+shift+m++ или ПКМ `Split Selected Takeoffs...`.
3. Режим `Each section into a separate takeoff` (по умолчанию) или `Separate takeoffs by sheet`.
4. Первая группа остаётся в исходной позиции, остальные становятся соседними позициями с тем же именем, папкой и свойствами. Отделённые получают новый цвет.
5. Статус: `Split 1 takeoff(s); created 2 new takeoff(s). Ctrl+Z in Takeoffs to undo.`

Пустые позиции не меняются, секции сохраняют лист, масштаб и геометрию.

## Break и Break H/V

<figure markdown>
  ![Кнопки Break с точкой H/V и Ends](../assets/images/ourplancore/v3/tool-break-ends.png)
  <figcaption markdown="span">Break с маленькой точкой H/V (закрашена = режим включён) и Ends справа.</figcaption>
</figure>

1. Выделите линии: на листе инструментом Select или Line-takeoff в дереве Takeoffs (работает и для нескольких).
2. `Break` или ++ctrl+shift+b++: каждая ломаная распадается на односегментные замеры в том же takeoff. Сумма длин не меняется.
3. С закрашенной точкой H/V или по ++ctrl+shift+v++ сегменты раскладываются в два новых takeoff рядом с исходным: `<имя> - Horizontal` и `<имя> - Vertical`. Повторный запуск переиспользует эту пару.
4. ++ctrl+z++ возвращает всё одним шагом.

++ctrl+shift+v++ в дереве Takeoffs - это Break H/V, а ++ctrl+v++ там остаётся Paste.

## Ends и P Line: точки из линий

<figure markdown>
  ![Диалог Count Points At Line Ends](../assets/images/ourplancore/v3/count-line-ends.png)
  <figcaption markdown="span">Count Points At Line Ends: одна галка `Merge points where segments meet` и кнопка Create.</figcaption>
</figure>

**Ends.** Выделите сегменты Line (на листе или takeoff в дереве), нажмите `Ends`. В диалоге `Count Points At Line Ends` галка `Merge points where segments meet` ставит одну метку в общем углу вместо двух. `Create` создаёт Count-takeoff с метками на концах; имя и папку проверьте в дереве.

**P Line.** Выделите Line, нажмите `P Line`. Диалог `Create Count Points Along Line(s)`: `Count takeoff name`, `Spacing, inches` (по умолчанию шаг линии или 16"), галка `Include line end point`. Создаётся отдельный Count-takeoff, метки стоят вдоль линии с шагом.

## Combine: площади внахлёст

Select, выделить две и больше Area, список `Combine`:

| Операция | Результат |
| --- | --- |
| Union | одна площадь из всех выбранных |
| Subtract | из первой выбранной вычесть остальные |
| Intersect | остаётся только общее пересечение |
| Remove Overlap | срезать перекрытия, побеждает первая выбранная; ничего не считается дважды |
| Divide | разбить на непересекающиеся части плюс отдельная площадь перекрытия |

Для шахт и проёмов внутри одной Area проще `Cut` (++x++): обвести вырез или ++f9++ боксом.

## Similar на других листах

Инструмент `Similar` ищет одинаковые символы по одному образцу офлайн. Для всего проекта:

1. Обведите рамкой один символ на листе.
2. Порог: `Strict` / `Default` / `Loose`; галки `Match rotated copies (90° / 180° / 270°)` и `Match mirrored copies`.
3. Галка `Search all sheets in this job`: проверенные по растру совпадения на других листах добавляются сами, кандидаты только по тексту лишь показываются. Не больше 80 других листов за поиск.
4. Синие метки добавляются сразу, оранжевые - слабые на проверку, серые галки уже посчитаны. `Include candidates` берёт и слабые, `Strong only` - только надёжные.
5. `Add` кладёт метки в активный Count-takeoff или в новый `Similar Count`. Галка `Ask AI to identify the symbol` - онлайн и только совет, нужен модуль AI и ключ.

## Сценарии

??? note "Одинаковые стены скопированы на 2-й этаж, а потом нашлись ещё на 3-м"
    1. Ctrl+C на 2-м, Ctrl+V на 3-м листе, `New takeoffs`.
    2. В Takeoffs выделить `ext 2x6 9.09` 2-го и 3-го этажей.
    3. Ctrl+M, оставить позицию 2-го этажа. Папку поправить перетаскиванием, если этажи должны быть раздельно.

??? note "Одна позиция на трёх листах, а в DFL нужен каждый лист отдельно"
    1. Выделить позицию, Ctrl+Shift+M.
    2. Режим `Separate takeoffs by sheet`, OK.
    3. Переименовать копии: `rf 6 a105`, `rf 6 a106`. Excel-полоса читает имена.

??? note "Bracing считать отдельно по горизонтали и вертикали"
    1. Нарисовать `bft` одной ломаной.
    2. Выделить, Ctrl+Shift+V.
    3. Получить `bft - Horizontal` и `bft - Vertical`; оригинал можно удалить или оставить для суммы.

??? note "Посты по концам балок"
    1. Балки нарисованы как Line (ledger, beam line).
    2. Выделить все, `Ends`, галка `Merge points where segments meet`.
    3. Переименовать новый Count в марку поста, проверить лишние метки на стыках.

??? note "Стойки забора или hangers по шагу"
    1. Линия забора как Line.
    2. `P Line`, шаг `96`, `Include line end point`.
    3. Имя Count - марка стойки. Линия остаётся и даёт погонаж.

??? note "Две площади крыши наехали друг на друга"
    1. Select, выделить обе Area.
    2. `Combine > Remove Overlap`: первая выбранная остаётся целой.
    3. Сравнить `Total` до и после: сумма должна уменьшиться ровно на перекрытие.

## Ловушки

- Merge не склеивает геометрию: две стены, нарисованные встык, остаются двумя сегментами с общей суммой.
- Split на листе и Split в дереве - разные команды; смотрите, где фокус.
- Break H/V заводит пару takeoff и при следующем запуске доливает в неё, а не создаёт новую пару.
- Similar находит похожие картинки, не одинаковое назначение: окно и дверь одной формы на схеме могут попасть в один счёт. Проверяйте оранжевые метки.
- Все операции из дерева откатываются Ctrl+Z только пока фокус в панели Takeoffs.

## См. также

- [Инструменты замера](ourplancore-tools.md) - Line, Count, Area, Beam, Openings
- [Дерево Takeoffs](ourplancore-takeoffs.md) - копирование между листами и корпусами
- [Горячие клавиши](ourplancore-shortcuts.md)
- [Частые ошибки: листы и дерево](../start/common-mistakes.md#pages)
