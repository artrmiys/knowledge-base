# Первые шаги: 10 уроков

Курс на демо-проекте OurPlanCore 3.0: от открытия программы до PDF и Excel. Каждый урок - одна задача от начала до видимого результата, 5-10 минут. Уроки идут по порядку работы эстиматора; подробности по каждой теме - на страницах раздела, ссылки в конце урока. Демо-проект можно портить: новый создаётся плиткой `Open sample job` ([экскурсия по демо](ourplancore-start.md#demo)).

Что нужно до начала: программа установлена и запускается ярлыком с рабочего стола ([начало работы](ourplancore-start.md)); для урока 9 - Excel и копия `TemplateCom.xlsm` из папки обновлений программы.

## Урок 1. Открыть демо-проект и осмотреться { #lesson-1 }

<figure markdown>
  <video class="kb-demo" loop muted playsinline preload="none" poster="../../assets/images/ourplancore/demo/d-open-sample.png"><source src="../../assets/images/ourplancore/demo/d-open-sample.mp4" type="video/mp4"></video>
  <figcaption markdown="span">Демонстрация: `Open sample job` на стартовой карточке создаёт демо-проект; дальше листы W, F, S и U со своими легендами и вкладка 3D.</figcaption>
</figure>

Цель: открыть учебный проект и узнать, где что лежит в окне.

1. Запустите программу и нажмите плитку **Open sample job** (или **Main > Open / Import > Sample job (demo to explore)**).
2. Дождитесь статуса `Sample project created: OurPlanCore Guide Sample.`
3. Раскройте в панели **Pages** слева папку `00. Guide` и щёлкните план этажа: он открылся вкладкой в центре.
4. Найдите справа панель **Takeoffs** с деревом позиций, внизу полосу инструментов, в самом низу строку статуса.
5. Нажмите `F1`: шпаргалка клавиш поверх окна; закройте `Esc`.
6. Нажмите `Ctrl+Shift+P`, наберите `fit`, `Enter`: лист вписался в окно. То же делает клавиша `F`.

Проверь себя: в заголовке окна имя `OurPlanCore Guide Sample`, в строке статуса видны `Scale:` и `Route:`, правая кнопка мыши двигает лист, колесо меняет zoom.

Подробно: [Начало работы](ourplancore-start.md), [карта окна](ourplanecore.md#window-map).

## Урок 2. Листы: имя, масштаб, точка листа { #lesson-2 }

<figure markdown>
  <video class="kb-demo" loop muted playsinline preload="none" poster="../../assets/images/ourplancore/demo/d-sheet-rename-dot.png"><source src="../../assets/images/ourplancore/demo/d-sheet-rename-dot.mp4" type="video/mp4"></video>
  <figcaption markdown="span">Демонстрация: ++ctrl+d++ делает копию листа, ++f2++ даёт ей имя `a101 1st sw`, щелчок по точке S/1 под `Scale` задаёт маршрут `S 1st floor`.</figcaption>
</figure>

Цель: понять, что у листа есть имя по канону, масштаб и точка W/F/S/U, и научиться ставить их руками.

1. Выделите план этажа в Pages и прочитайте в статусе `Scale: 1/8" = 1'0"` (или `1:96`) и `Route: W 1st`.
2. Нажмите `R` (Ruler), щёлкните два конца размерной цепочки на листе: длина рулетки совпала с подписанным размером, значит масштаб верный.
3. Нажмите `F2` на листе, впишите то же имя (`a101 1st`), `Enter`: имя строчными, тег этажа последним; точка W под заголовком Scale осталась.
4. Нажмите `Ctrl+D`: рядом появилась копия листа с тем же именем.
5. Нажмите `F2` на копии, впишите `a101 1st sw`, `Enter`, затем ПКМ по копии и **Move to Folder...**, если хотите убрать её в отдельную папку.
6. Откройте копию и щёлкните точку в строке `S`, столбец `1`, под заголовком Scale.

<figure markdown>
  <video class="kb-demo" loop muted playsinline preload="none" poster="../../assets/images/ourplancore/demo/d-scale.png"><source src="../../assets/images/ourplancore/demo/d-scale.mp4" type="video/mp4"></video>
  <figcaption markdown="span">Демонстрация: на листе с неверным масштабом ++f4++ и ввод `1/8" = 1'0"`; длина в легенде пересчитывается сразу.</figcaption>
</figure>

Если масштаба у листа нет: нажмите `S`, щёлкните два конца известного размера, впишите длину (`20'` или `1/8" = 1'0"`), `Enter`; для нескольких листов выделите их в Pages и нажмите `F4`.

Проверь себя: на копии статус показывает `Route: S 1st`, на оригинале `Route: W 1st`; оба листа с масштабом.

Подробно: [Листы (Pages)](ourplancore-pages.md), [раскладка по листам](ourplancore-split-by-sheets.md), [имена листов](../start/takeoff-structure.md).

## Урок 3. Роутинг: куда ляжет замер { #lesson-3 }

<figure markdown>
  <video class="kb-demo" loop muted playsinline preload="none" poster="../../assets/images/ourplancore/demo/d-routing.png"><source src="../../assets/images/ourplancore/demo/d-routing.mp4" type="video/mp4"></video>
  <figcaption markdown="span">Демонстрация на реальном проекте: стена на W-листе уходит в `walls/3rd floor walls`, балка на F-листе в `framing/3rd floor framing/beams`, shear wall на копии листа с точкой S в `shear walls`.</figcaption>
</figure>

Цель: увидеть, как точка листа и имя позиции сами выбирают папку в дереве.

1. Откройте план с точкой W (`a101 1st`) и нажмите `L`.
2. В диалоге **New Takeoff Item** впишите имя `ext 2x6 9.09` и прочитайте строку назначения внизу диалога: `walls/1st floor walls`.
3. Нажмите **OK**, щёлкните два угла на листе и нажмите `C`.
4. Найдите позицию в Takeoffs: она лежит в `walls/1st floor walls`; в статусе `Takeoff: ext 2x6 9.09 (Route: W 1st)`.
5. Нажмите `L` ещё раз, впишите `eve 24 main`: строка назначения показывает `eves rakes/eves`, хотя лист тот же. Слово `eve` в имени сильнее точки листа. Нажмите **Cancel**.
6. Откройте копию с точкой S, нажмите `L`, впишите `SW1-1`: назначение `shear walls/1st floor/shear`. Нажмите **Cancel**.

Проверь себя: вы можете сказать до нажатия OK, в какую папку ляжет позиция, и видите это в строке статуса `Route:`.

Подробно: [Имена и автомаршрут](takeoff-naming.md), [Раскладка по листам и роутинг](ourplancore-split-by-sheets.md).

## Урок 4. Стены: Line { #lesson-4 }

<figure markdown>
  <video class="kb-demo" loop muted playsinline preload="none" poster="../../assets/images/ourplancore/demo/d-line-walls.png"><source src="../../assets/images/ourplancore/demo/d-line-walls.mp4" type="video/mp4"></video>
  <figcaption markdown="span">Демонстрация: ++l++, имя `ext 2x6 9.09`, строка маршрута `walls/1st floor walls`, щелчки по оси наружной стены и ++c++.</figcaption>
</figure>

Цель: нарисовать наружные стены этажа одной позицией и продолжить её через Record.

1. На плане с точкой W нажмите `L`, имя `ext 2x6 9.09` (назначение, сечение, высота в футах), **OK**.
2. Щёлкайте по оси наружной стены угол за углом; `Backspace` убирает последнюю точку.
3. Нажмите `C`: участок закрыт, в статусе `Mode: Record ext 2x6 9.09`.
4. Нарисуйте следующий несвязанный участок той же стены: он идёт в ту же позицию.
5. Нажмите `Space`, чтобы остановить Record. Выделите позицию в дереве и нажмите `Space` снова: Record продолжает её, когда вернётесь к стенам позже.
6. Для перегородок другой высоты нажмите `L` и создайте новую позицию `2x4 9.09`: новая высота или сечение - новая позиция.

Проверь себя: в `walls/1st floor walls` две позиции, у `ext 2x6 9.09` под ней секции по участкам, `Total` показывает погонные футы.

Подробно: [Инструменты замера, Line](ourplancore-tools.md), [Exterior](../work/vertical/walls/exterior.md).

## Урок 5. Проёмы: Openings { #lesson-5 }

<figure markdown>
  <video class="kb-demo" loop muted playsinline preload="none" poster="../../assets/images/ourplancore/demo/d-openings.png"><source src="../../assets/images/ourplancore/demo/d-openings.mp4" type="video/mp4"></video>
  <figcaption markdown="span">Демонстрация: ++o++, рамка по окну, имя `4.0x4.0`, остальные окна по одному щелчку; итог 4 ea.</figcaption>
</figure>

Цель: посчитать окна и двери позициями-размерами, по одной точке на проём.

1. Нажмите `O` на плане или фасаде.
2. Щёлкните два противоположных угла бокса по проёму.
3. В диалоге впишите имя `3.0x6.8 d`: ширина на высоту в футах с одной цифрой после точки, суффикс ` d` для двери (` gd` ворота, ` lv` решётка); окно - без суффикса, `4.0x4.0`.
4. Нажмите **OK**: в центре проёма точка, позиция легла в `openings` с любого листа.
5. Повторите для следующего проёма того же размера: выделите позицию и `Space`, затем бокс; разные марки одного размера - одна позиция.
6. В Takeoffs создайте под `openings` папку `1` (**New Folder**) и перетащите в неё позиции этажа.

Проверь себя: в `openings/1` позиции `3.0x6.8 d` и `4.0x4.0`, `Total` равен числу проёмов, на плане по одной точке на проём.

Подробно: [Инструменты, Openings](ourplancore-tools.md), [Windows and Doors](../work/vertical/openings/windows-doors.md).

## Урок 6. Площади: Area и Cut { #lesson-6 }

<figure markdown>
  <video class="kb-demo" loop muted playsinline preload="none" poster="../../assets/images/ourplancore/demo/d-area.png"><source src="../../assets/images/ourplancore/demo/d-area.mp4" type="video/mp4"></video>
  <figcaption markdown="span">Демонстрация: ++a++, контур этажа `1st` и ++c++; затем ++x++ (`Cut`) с ++f9++ (`Box`) вырезает ванную из площади.</figcaption>
</figure>

Цель: снять площадь этажа и вырезать из неё шахту.

1. На плане с точкой W нажмите `A`, имя `1st`, **OK**.
2. Обведите контур этажа по углам, `C` замыкает: позиция легла в `sqfts`.
3. Нажмите `X` (Cut), обведите контур шахты или лестничного проёма внутри площади, `C`.
4. Прочитайте `Total` у позиции: площадь уменьшилась ровно на вырез.
5. Для прямоугольной комнаты нажмите `A`, затем `F9` (Box) и щёлкните два угла.

Проверь себя: в `sqfts` позиция `1st`, на листе контур с дыркой, `Total` в SF.

Подробно: [Инструменты, Area](ourplancore-tools.md), [SQFT](../work/sqfts/1st2nd.md), [Правка и привязки](ourplancore-editing.md).

## Урок 7. Framing на F-листе: J Area и Beam { #lesson-7 }

<figure markdown>
  <video class="kb-demo" loop muted playsinline preload="none" poster="../../assets/images/ourplancore/demo/d-jarea.png"><source src="../../assets/images/ourplancore/demo/d-jarea.mp4" type="video/mp4"></video>
  <figcaption markdown="span">Демонстрация: ++j++, имя `2x10 16"`, контур перекрытия и линия направления joists; программа считает штуки и погонаж.</figcaption>
</figure>

Цель: посчитать joists зоной и балку с заказной длиной на структурном плане.

1. Откройте структурный план с точкой F (`s101 1st`); статус `Route: F 1st`.
2. Нажмите `J`, имя `2x10 16"` (сечение и шаг), **OK**, обведите зону joists, `C`.
3. Проведите линию направления вдоль joists, когда программа спросит; `Shift` держит направление по осям.
4. Прочитайте `Total`: штуки и погонные футы, позиция в `framing/1st floor framing/joists`.

<figure markdown>
  <video class="kb-demo" loop muted playsinline preload="none" poster="../../assets/images/ourplancore/demo/d-beam.png"><source src="../../assets/images/ourplancore/demo/d-beam.mp4" type="video/mp4"></video>
  <figcaption markdown="span">Демонстрация: ++b++, два конца балки, имя `FB1`; программа дописывает длину в имя: `FB1 52`.</figcaption>
</figure>

5. Нажмите `B`, проведите от опоры до опоры балки, в диалоге впишите марку `FB1`, **OK**: программа дописала длину в футах, округлённую вверх (`FB1 14`), позиция в `.../beams`.
6. Нажмите `P`, имя `C4 20`, щёлкните символ поста: позиция в корне `framing/1st floor framing`; перетащите её в папку `posts`.

Проверь себя: в `framing/1st floor framing` папки `joists`, `beams`, `posts` с позициями; у балки длина в имени, у joists штуки в `Total`.

Подробно: [Инструменты, J Area и Beam](ourplancore-tools.md), [Joist](../work/horizontal/floor-framing/joist.md), [Beam](../work/horizontal/floor-framing/beam.md).

## Урок 8. Проверка: легенда, Hide, Total { #lesson-8 }

<figure markdown>
  <video class="kb-demo" loop muted playsinline preload="none" poster="../../assets/images/ourplancore/demo/d-legend-groups.png"><source src="../../assets/images/ourplancore/demo/d-legend-groups.mp4" type="video/mp4"></video>
  <figcaption markdown="span">Демонстрация: две позиции под листом в Pages, правый щелчок `Legend Group > New Group`; легенда на листе делится на блоки walls и openings.</figcaption>
</figure>

Цель: убедиться, что на листе и в дереве всё на месте, прежде чем выгружать.

1. Включите **Display > Legend Show**: на листе появилась легенда с позициями этого листа.
2. ПКМ по листу в Pages, **Organize > Sort Sheet Legend by Key (before space)**: позиции отсортированы по первому слову имени.
3. Раскройте лист в Pages: под ним те же позиции, что в легенде.

<figure markdown>
  <video class="kb-demo" loop muted playsinline preload="none" poster="../../assets/images/ourplancore/demo/d-hide.png"><source src="../../assets/images/ourplancore/demo/d-hide.mp4" type="video/mp4"></video>
  <figcaption markdown="span">Демонстрация: ++h++ прячет выделенную позицию на листе, точка видимости под листом в Pages возвращает её.</figcaption>
</figure>

4. Выделите позицию `1st` в Takeoffs и нажмите `H`: площадь исчезла с листа, статус `Hidden 1 whole takeoff(s)`.
5. Щёлкните точку видимости у позиции под листом в Pages: площадь вернулась.
6. Откройте вкладку **Estimating** справа: все позиции одной таблицей с итогами. Нажмите **Delete Empty** в Takeoffs, чтобы убрать позиции без замеров.

Проверь себя: легенда читается, у каждой позиции свой цвет, в Estimating нет пустых строк и нулевых итогов.

Подробно: [Дерево Takeoffs](ourplancore-takeoffs.md#hide), [PDF и сдача, легенда](ourplancore-pdf.md#legend).

## Урок 9. Excel: полоса XL { #lesson-9 }

<!-- DEMO: d-excel-xl -->

Цель: выгрузить стены и площади в книгу DFL одной кнопкой.

1. Скопируйте `TemplateCom.xlsm` из папки обновлений программы в папку проекта под именем корпуса, откройте копию в Excel, разрешите макросы, активируйте лист `Detailed Frame List`.
2. В OurPlanCore выделите в Takeoffs корень проекта (один корпус) или папку корпуса.
3. Нажмите `LG` на полосе XL справа, впишите коды балок и постов проекта (`FB1 - (2) 1 3/4 x 11 7/8 LVL`, `C4 - 6x6`), **Save for job**.
4. Нажмите `ALL`, прочитайте предупреждение о пропущенных позициях, **Continue**.
5. Дождитесь `Completed: ...` в статусе и посмотрите книгу: матрица стен, Front Page, framing list.
6. Сохраните книгу в Excel сами: программа её не сохраняет.

Проверь себя: в `Detailed Frame List` появились строки стен с высотой `9.09`, площадь `1st` на Front Page, балка `FB1` в framing list с размером из легенды.

Подробно: [Экспорт в Excel](ourplancore-excel.md), [DFL: как устроена книга](dfl-overview.md).

## Урок 10. PDF и сдача { #lesson-10 }

<figure markdown>
  <video class="kb-demo" loop muted playsinline preload="none" poster="../../assets/images/ourplancore/demo/d-preview.png"><source src="../../assets/images/ourplancore/demo/d-preview.mp4" type="video/mp4"></video>
  <figcaption markdown="span">Демонстрация: `PDF Output > Preview`; превью листа перерисовывается при смене прозрачности и размера легенды на ленте.</figcaption>
</figure>

Цель: получить PDF только с листами, где есть замеры, и проверить его до экспорта.

1. Нажмите `Ctrl+S`, дождитесь `Save: Saved hh:mm:ss` в статусе.
2. Откройте ленту **PDF Output** и нажмите **Preview**: окно показывает текущий лист так, как он напечатается.
3. Поменяйте **Opac** на 70 и размер **Legend**: превью перерисовалось.

<figure markdown>
  <video class="kb-demo" loop muted playsinline preload="none" poster="../../assets/images/ourplancore/demo/d-export-pdf.png"><source src="../../assets/images/ourplancore/demo/d-export-pdf.mp4" type="video/mp4"></video>
  <figcaption markdown="span">Демонстрация: `Main > Export`, галки нужных листов, `Export`; статус `Exported PDF (2 sheet(s))`.</figcaption>
</figure>

4. Нажмите **Main > PDF > Export**, отметьте в диалоге только листы с замерами, оставьте галки **Measurements** и **Legend**.
5. Нажмите **Export**, назовите файл `<проект> Bldg A.pdf`, сохраните.
6. Откройте PDF и пролистайте: замеры и легенда на месте, лишних листов нет.

Проверь себя: PDF с одним-двумя листами, линии стен не закрывают размеры, легенда читается.

Подробно: [PDF и сдача](ourplancore-pdf.md), [Процесс работы, сдача](../start/workflow.md).

## Дальше

- Несколько корпусов в проекте: [Несколько зданий](ourplancore-buildings.md).
- Правка готовых замеров, Merge и Split, привязки: [Правка и привязки](ourplancore-editing.md).
- Узлы на отдельном листе и маска: [Листы: кропы, маска, наложения, легенда](ourplancore-sheets-advanced.md).
- Помощник в окне: [Консоль ИИ](ourplancore-ai-console.md).
- Порядок замеров настоящего проекта: [Процесс работы](../start/workflow.md), [Частые ошибки](../start/common-mistakes.md).
