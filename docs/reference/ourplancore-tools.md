# Инструменты замера

Здесь: все инструменты нижней полосы по частоте использования, клавиши, шаги и что появляется в дереве. Нужно каждый день; предметные правила (что именно обводить) живут на страницах раздела "Работа".

<figure markdown>
  ![Нижняя полоса инструментов](../assets/images/ourplancore/v3/toolstrip.png)
  <figcaption markdown="span">Строка 1: инструменты и переключатели привязок. Строка 2: Transform, масштаб листа, Fit и zoom. Справа кнопки `Value` и `Excel`.</figcaption>
</figure>

## Общие правила

- Кнопка инструмента (`L`, `A`, `P`, `J`, `B`, `O`) создаёт **новую** позицию: открывается диалог `New Takeoff Item` с именем, цветом и предпросмотром папки назначения. Продолжить **существующую** позицию: выделить её и `Space` (Record).
- Рисование: клик ставит точку, `C` завершает, `Esc` отменяет недорисованное, `Ctrl+Z` или `Backspace` убирает последнюю точку, `Tab` переключает варианты трассы при PDF Snap.
- Строка статуса показывает `Mode: Record <позиция>` и `Takeoff: <позиция> (Route: W 1st)`: что рисуешь и куда ляжет.
- Без масштаба листа Line и Area не создаются ([масштаб](ourplancore-pages.md#scale)).
- Правая кнопка мыши всегда двигает лист, колесо меняет zoom, `F` вписывает лист в окно.

## Таблица инструментов

| Кнопка | Клавиша | Что делает | Что в дереве |
| --- | --- | --- | --- |
| `Line` | `L` | ломаная по оси стены или узла, погонные футы | позиция Line, LFT |
| `Area` | `A` | замкнутый контур, квадратные футы; `F9` бокс двумя углами | позиция Area, SF |
| `Count` | `P` | точка на символ, штуки | позиция Count, ea |
| `J Area` | `J` | зона joists с направлением и шагом | позиция Joist Area: штуки и LFT |
| `Beam` | `B` | длина балки между опорами, одна точка на балку | позиция Count с длиной в имени |
| `Open` | `O` | бокс по проёму, точка в центре | позиция Count `ШxВ` |
| `P Line` | - | Count-точки вдоль выбранных Line с шагом | позиция Count |
| `Cut` | `X` | вырез в Area или стирание куска Line; `F9` бокс | меняет существующий замер |
| `Similar` | - | найти похожие символы на листе и собрать в Count | позиция Count |
| `Scale` | `S` | масштаб листа по известному размеру | - |
| `Ruler` | `R` | рулетка-размер на листе без количества; точка на кнопке прячет рулетки листа | разметка |
| `Pitch` | - | уклон крыши `rise:12` по двум точкам | разметка |
| `Select` | `E` | выбор и правка замеров; `Ctrl+C` / `Ctrl+V` | - |
| `Pan` | `V` | двигать лист | - |
| `Snap` | `F3` | привязка к точкам своих замеров | - |
| `PDF` | `Ctrl+F3` | привязка к углам вектора PDF и чёрным линиям растра | - |
| `Ortho` | `F8` | только горизонталь и вертикаль; `Shift` включает временно | - |
| `Box` | `F9` | Line и Area двумя противоположными углами | - |
| `Repeat` (стрелка у Line и Beam) | - | серия отдельных двухточечных отрезков или балок, `Esc` останавливает | одна позиция, много секций |
| `Merge`, `Split`, `Break`, `Ends`, `Combine` | `Ctrl+M`, `Ctrl+Shift+M`, `Ctrl+Shift+B` | правка готовых замеров и позиций | [Правка takeoffs](ourplancore-edit-takeoffs.md) |

Кнопки `Value` и `Excel` справа пишут выбранную позицию в открытую книгу Excel: [Экспорт в Excel](ourplancore-excel.md#value).

## Line (L): стены, shear walls, карнизы, парапеты, детали

<figure markdown>
  ![Line по стенам](../assets/images/ourplancore/v3/measure-line-walls.png)
  <figcaption markdown="span">Позиция `ext 2x6 9.09`: назначение, сечение, высота в футах. Несвязанные участки - отдельные замеры одной позиции.</figcaption>
</figure>

Когда: всё, что считается в погонных футах: стены, BW, shear walls, eve и rake, truss heel, parapets, ledger и rim в деталях.

1. `L`, имя по схеме `<назначение> <сечение> <высота>`: `ext 2x6 9.09`, `corr 2x6 11.7`, `eve 24 main`, `prpt 6.4 5.3 0.5 par`.
2. Клики по оси стены, `C` завершает участок; следующий участок рисуется в той же позиции, пока включён Record.
3. `F8` держит прямые углы, `Ctrl+F3` цепляется к линиям чертежа.
4. Новая высота или сечение - новая позиция, не продолжение.

В дереве: при точке W в `walls/<этаж> floor walls`, при F в `framing/<этаж> framing/details`, при S в `shear walls/<этаж>/shear`; имена с `eve`, `rake`, `prpt`, `trussheel`, `gable` уходят в свои корни с любого листа. Правила: [Exterior](../work/vertical/walls/exterior.md), [Bearing Walls](../work/vertical/walls/bearing-walls.md), [Shear Wall](../work/vertical/sheathing/shear-wall.md), [Eve](../work/sheathing-and-misc/eve.md), [Parapet](../work/vertical/walls/parapet.md), [Truss Heel](../work/vertical/sheathing/truss-heel.md).

## Area (A): площади, кровля, обшивка

<figure markdown>
  ![Area площади этажа](../assets/images/ourplancore/v3/measure-area-floor.png)
  <figcaption markdown="span">Контур по реальной границе этажа. Шахты вырезаются `Cut`, не вторым контуром.</figcaption>
</figure>

Когда: SQFT этажей, балконов и porch, скаты кровли, фронтоны, обшивка фасадов.

1. `A`, имя `1st`, `blcny`, `rf 6`, `gable`, `siding/6" vertical`.
2. Обвести контур по углам, `C` замыкает. `F9` для прямоугольника двумя кликами.
3. Отверстие внутри (шахта, open to below): `X` и обвести вырез внутри площади.
4. Пересечение двух площадей: `Combine > Remove Overlap`.

В дереве: при точке W в `sqfts`, при F в `framing/<этаж> framing/joists` (для joists используй `J Area`, не Area), при S в shear. Правила: [SQFT 1st, 2nd](../work/sqfts/1st2nd.md), [Roof](../work/sqfts/roof.md), [Gable](../work/vertical/walls/gable.md), [Wall Sheathing](../work/vertical/sheathing/wall-sheathing.md).

## Count (P): посты, holdowns, крепёж

<figure markdown>
  ![Count точками](../assets/images/ourplancore/v3/measure-count.png)
  <figcaption markdown="span">Одна точка на физический символ. Значок и цвет позиции отличают её от соседей в легенде.</figcaption>
</figure>

1. `P`, имя по марке или модели: `C4 20`, `HDU11 SB1x30 S2.2`, `MPB88Z S2.1`, `int H228 4`.
2. Клик по центру символа; у holdown - на конце shear wall. Значок точки выбирается в диалоге (`Count display`: circle, cross, square, star, triangle, diamond, ring).
3. Промах: `E`, перетащить точку или `Delete`.

В дереве: при точке W в `walls/<этаж> floor walls`, при F в `framing/<этаж> framing` (посты и headers потом переносятся в `posts` и `headers/ext|int`), при S в `shear walls/<этаж>/holdowns`. Правила: [Post](../work/horizontal/floor-framing/post.md), [Holdowns](../work/vertical/sheathing/holdowns.md), [Headers](../work/vertical/openings/headers.md).

## J Area (J): joists и rafters

<figure markdown>
  ![J Area с направлением и шагом](../assets/images/ourplancore/v3/measure-joist-area.png)
  <figcaption markdown="span">Зона joists: контур, направление, шаг. Программа считает штуки и длины сама.</figcaption>
</figure>

1. `J`, имя `<сечение или серия> <шаг>`: `2x8 16"`, `11 7/8 TJI 16"`.
2. Обвести зону, `C`. Программа спрашивает направление: провести линию вдоль joists; `Shift` держит направление ортогонально.
3. В свойствах: шаг, крайние joists (end joists), сдвоенные. Отверстие - `X`.
4. Дополнительные joists под стенами: выделить зону и `D` (Extra Joists).

В дереве: при точке F в `framing/<этаж> framing/joists`. Смена направления, шага или материала - новая зона. Обычная Area с именем `2x8 16"` в Excel joists не даст. Правила: [Joist](../work/horizontal/floor-framing/joist.md).

## Beam (B): балки и перемычки с длиной

<figure markdown>
  ![Beam с длиной в имени](../assets/images/ourplancore/v3/measure-beam.png)
  <figcaption markdown="span">Провёл от опоры до опоры, назвал марку: длина добавилась в имя уже округлённой.</figcaption>
</figure>

1. `B`, провести от опоры до опоры.
2. В диалоге имя марки или сечения: `FB1`, `(2) 1 3/4 x 18 LVL`, `ext H228`. Программа дописывает заказную длину в футах.
3. Получается позиция Count с первой точкой на балке; вторая такая же балка - `Space` и ещё одна точка.
4. Серия балок подряд: стрелка `Repeat` у кнопки Beam.

Округление длины делает инструмент: до 8' вверх до целого фута, длиннее 8' вверх до чётного (`8.3` даёт `10`, `13.2` даёт `14`). Футы руками не прибавлять и `(n)` вместе с n точками не ставить. В дереве: при точке F в `framing/<этаж> framing/beams`. Правила: [Beam](../work/horizontal/floor-framing/beam.md), [Headers](../work/vertical/openings/headers.md).

## Openings (O): окна, двери, ворота

<figure markdown>
  ![Openings](../assets/images/ourplancore/v3/measure-openings.png)
  <figcaption markdown="span">Бокс по проёму на фасаде, точка в центре, имя-размер `4.3x7.8`.</figcaption>
</figure>

1. `O`, два угла бокса по проёму.
2. Имя `<ширина>x<высота>` в десятичных футах с одной цифрой после точки: `4.3x7.8`; суффикс ` d` дверь, ` gd` ворота, ` lv` решётка. Разные марки одного размера - одна позиция.
3. Одна точка на проём; повтор на плане и фасаде не удваивает.

В дереве: инструмент Openings идёт в `openings` с любого листа, кроме U; этаж - папка `openings/<0|1|2|roof>`. Правила: [Windows and Doors](../work/vertical/openings/windows-doors.md).

## Остальные инструменты

| Инструмент | Когда и как |
| --- | --- |
| `P Line` | посты или анкеры по длине стены с шагом: выделить Line, `P Line`, задать шаг и имя; получается Count |
| `Cut` (`X`) | шахты и вырезы в Area, стирание куска Line; `F9` переключает бокс |
| `Similar` | много одинаковых символов (окна одной марки, holdowns): `Similar`, выбрать образец, проверить найденные, назвать позицию |
| `Pitch` | уклон крыши по разрезу: две точки по скату, результат `rise:12` для имени `rf 6` |
| `Ruler` (`R`) | проверка масштаба и размеров; количества не даёт |
| `Record` (`Space`) | продолжить выбранную позицию; ещё раз `Space` останавливает |
| `Snap` / `PDF` / `Ortho` / `Box` | привязки: к своим точкам, к чертежу, к осям, двумя углами. `Viewport > PDF SNAP > Bridge` задаёт радиус продолжения трассы при `Tab` |

## Правка замеров { #editing }

- `E`: клик выбирает замер, рамка выбирает несколько; `Alt` показывает вершины для перетаскивания; `Delete` удаляет; `Ctrl+Z` отменяет.
- Строка `Transform`: `Flip H`, `Flip V` зеркалят выбранное, `Rot` поворачивает (`Shift` шаг 15 градусов), `Scale` масштабирует геометрию выбранного.
- `Ctrl+C` / `Ctrl+V` переносят замеры на другой лист: [копирование](ourplancore-takeoffs.md#copy).
- `Merge`, `Split`, `Break`, `Ends`, `Combine`: [Правка takeoffs](ourplancore-edit-takeoffs.md).

## См. также

- [Дерево Takeoffs](ourplancore-takeoffs.md): Record, корень корпуса, копирование
- [Имена и автомаршрут](takeoff-naming.md): почему позиция легла в эту папку
- [Процесс работы: замеры по порядку](../start/workflow.md), [Частые ошибки](../start/common-mistakes.md)
