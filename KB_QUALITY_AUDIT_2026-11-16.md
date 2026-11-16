# Аудит качества KB для эстиматоров (16.11.2026)

Только чтение рабочего дерева `E:\---\project\knowledge-base-e-wood` (с локальной правкой `docs/reference/formulas.md`). В репозитории ничего не менялось. Страницы делились на 4 части: Старт, Excel и DFL, Справочник и OurPlanCore смотрел я, раздел "Работа" и OurPDF - три помощника по группам меню; самые тяжёлые находки помощников я перепроверил сам (схемы balcony-buildup, exclusions, anchor-bolt, кадр sheet-unit, формулы shaft, расшифровка 9068, единицы soffit - всё подтвердилось).

Оценки: A - работник сделает задачу по одной этой странице, картинка показывает сам элемент с подписями; B - пользоваться можно, 1-2 дыры; C - придётся спрашивать, или главная картинка общая, нечитаемая, без подписей, или правило спорит с другой страницей; D - вводит в заблуждение. "-" в колонке Визуал: картинка этой странице не нужна (чек-лист, таблица клавиш). Итог не среднее: страница с противоречием в правиле обычно не выше B, с неверным числом или неверной схемой - C.

## Коротко

Оценено 158 страниц из 160, что были на начало аудита (пропущены `index.md` - витрина и `start/suggest-change.md` - форма).

| Часть | Страниц | A | B | C | D |
| --- | ---: | ---: | ---: | ---: | ---: |
| Старт | 6 | 2 | 4 | 0 | 0 |
| OurPDF | 12 | 5 | 6 | 1 | 0 |
| Работа | 92 | 9 | 57 | 25 | 1 |
| Excel и DFL | 7 | 1 | 5 | 1 | 0 |
| Справочник (включая 3 страницы редактора) | 10 | 0 | 8 | 2 | 0 |
| **Без OurPlanCore** | **127** | **17** | **80** | **29** | **1** |
| OurPlanCore (отдельно, текст переписывается) | 31 | 6 | 20 | 5 | 0 |
| **Всего** | **158** | **23** | **100** | **34** | **1** |

Что видно в целом:

1. **Каркас сайта хороший.** 80 страниц раздела "Работа" написаны по одному шаблону (что это, где на чертежах, как мерить, строка DFL, ошибки, пример), канон дерева и имён (`start/takeoff-structure.md`), процесс (`start/workflow.md`), ноты (`reference/standard-notes.md`) и схемы DFL (`reference/dfl-overview.md`, 11 SVG) - уровень A. Разница между "супер" и "так себе" не в структуре, а в схемах, скриншотах и согласованности чисел (пункты ниже).
2. **Два поколения схем.** Новые схемы (разрез узла, у каждой детали номер, номер = строка DFL с единицей: `sqfts/deck.svg`, `framing/rim-board.svg`, `trims/furring-jambs.svg`, `walls/parapet-section.svg`, `framing/sill-plate-assembly.svg`, `walls/bw-mark.svg`, все `reference/dfl-*.svg`, `process/takeoff-tree*.svg`) - лучшее на сайте. Старые схемы "заголовок + подзаголовок + 3-5 зелёных выносок" (`framing/anchor-bolt.svg`, `trims/exclusions.svg`, `trims/balcony-buildup.svg`, `roof/ridge-valley-hip.svg`, `roof/rake.svg`, `walls/exterior-wall-section.svg`, `walls/basement-wall-section.svg`, `work-types/residential.svg`, `work-types/reconstruction.svg`, `hangers/hanger-selection-flow.svg`, `sheathing/gable-sheathing.svg`, `trims/rails-decking.svg`) - общие, а 6 из них прямо противоречат тексту своей страницы. Перерисовать около 15 старых схем в новом стиле - главный рычаг по визуалу.
3. **Одни и те же скриншоты на разных страницах.** `ourplancore/v3/measure-beam.png` стоит на 7 страницах (beam, ridge, header, hip, valley, rafters, tools) и показывает балку перекрытия на плане квартиры; `measure-line-detail.png` - rim на 4 страницах деталей; `measure-count.png` на страницах постов и балконов показывает двери; `sheet-dots.png` на 4 страницах нечитаем. Работник видит "картинку для галочки".
4. **Единицы и числа спорят между страницами.** 34 противоречия (раздел "Противоречия"). Самые дорогие: высота стойки с plates или без (5 страниц), что лежит в колонке D (6 страниц), bracing стен в LFT или штуках (8 страниц), три формулы decking, панели shaft от длины вместо площади (недосчёт в высоту стены раз).
5. **Схема против таблицы на той же странице.** SQ FT на схеме и 4x8 в таблице (box sheathing, truss heel), LUS28 под 2x10 без Zmax (две схемы деки), Titen HD с гайкой, Balustrades в LFT, Column wrap в pcs. Схему новичок запоминает лучше текста.
6. **Арифметика примеров** не сходится в 8 местах, и 16 страниц до сих пор с плашками "Уточняется" или `TODO-PHOTO` / `TODO-SCREEN`.
7. **Личных данных серьёзных нет.** Штампов, адресов, email на картинках не нашли. Мелочи: номер дома 225 на фото siding, локальные пути `C:\Users\User\Desktop\...lnk` на кадре настроек терминалов, ролик `d-routing` снят на реальном плане (без штампа), на `start/client-rules.md` названы 8 клиентов (решение владельца, правила сайта это не запрещают).

## Топ-10: что исправить первым

Порядок по вреду: сначала то, что даёт неверное количество в книге, потом то, что учит неверно мерить, потом картинки.

| # | Страница | Итог | Почему первой |
| --- | --- | --- | --- |
| 1 | `reference/formulas.md` | C | Канон чисел для всего сайта: G, D, H, `Stock LF` нигде не определены, truss bracing `=CEILING(G/4/D,1)` без объяснения, "минус plates" спорит с exterior, D = 14/16 при `LFT` в колонке D, формулы shaft от LFT вместо площади. Правка здесь закрывает сразу шесть противоречий (1, 2, 6, 18, 20, 31). |
| 2 | `work/vertical/walls/shaft.md` | C | Панели `LFT x 1.1 / 24` при 24 SF на панель: шахта 64 LF x 10.5' даёт 4 панели вместо 32. Прямой недосчёт в книге. |
| 3 | `work/horizontal/floor-framing/details/blockingoc.md` | C | Разбор формулы неверен по размерности (куски делятся на длину доски), направление линии не сходится с формулой; нужно слово владельца, какой смысл верный. |
| 4 | `work/sheathing-and-misc/ridgevalleyhip.md` | D | Учит мерить hip и valley Line в `details`, а hip.md и valley.md - Beam в `beams`; схема с неверной геометрией. Сделать коротким обзором со ссылками. |
| 5 | `reference/hangers.md` | C | Самая используемая справка по крепежу: SUL/SUR на 30 градусов (их нет), нет таблицы для пилёного 2x (самый частый случай), схема выбора путает skew с concealed, картинки Simpson без источника, одна со значком Google Lens. |
| 6 | `work/deck/anchor-bolts.md` + `work/horizontal/floor-framing/details/bolts.md` | C, C | Общая схема `framing/anchor-bolt.svg`: "дефолт 5/8" Titen HD" с гайкой против 1/2" в тексте; на bolts.md это главная картинка к теме, которую страница исключает; 1.1 то есть, то нет; шайбы 3x3 против правила ревьюера. |
| 7 | `work/exterior-trims/soffit-fascia.md` | C | Частая позиция, и не ясно, LFT или SQ FT: пример даёт оба варианта для vinyl, eve.md велит SQ FT; нет схемы разреза свеса. |
| 8 | `work/horizontal/floor-framing/details/bracingdrywall.md` (и единица bracing на 6 страницах стен) | C | Смешаны bracing стен и опора гипса; единица LFT на corridor, demising, basement, unit, exterior-materials против штук здесь и на gable; строки `Bracing for Drywall` в DFL нет. |
| 9 | `work/exterior-trims/balcony-buildup.md` (и дубль `work/deck/balcony-trims.md`) | C | Схема сборки в невозможном порядке (EPDM на sleepers, decking на мембране), "Decking часто by others" против "здесь", post wrap на 6 постов при 12; балконы в каждом COM. |
| 10 | `work/interior-trims/casing.md` | C | Jambs `=casing/2` в LFT против правила "точками по юнитам" на двух других страницах; "две стороны" без x2 в формуле. |

Сразу за десяткой: `work/vertical/sheathing/truss-heel.md`, `work/vertical/walls/gable.md` + `work/vertical/sheathing/gable.md` (Draft Stop), `work/vertical/walls/corridor.md`, `work/siding/measure.md`, `work/horizontal/floor-framing/subfloor.md`, `work/exterior-trims/exclusions.md`, `work/horizontal/roof-framing/dbl-trpl-rafters.md`, `work/sheathing-and-misc/rake.md`, `work-types/reconstruction.md`.

### Быстрые победы (по 10-15 минут, без решений владельца)

- `work/vertical/walls/unit.md`: главный кадр `ourplancore/v3/sheet-unit.png` пустой ("Scale: not set", белый лист, чёрная половина). Переснять план юнита с линиями `A 2x4`.
- `start/workflow.md:51`: подпись про папки `00. imported/Arch`, а на `pages-panel.png` листы демо-гайда. Готовый правильный кадр уже есть: левая панель `ourplancore/v3/window.png`.
- `ourplancore/v3/measure-count.png` убрать со страниц `post.md:37` и `deck-porch-balcony-frame.md:58` (на нём двери).
- Поменять местами подписи `confluence-138/139` (`header.md`) и `confluence-140/141` (`dbl-trpl-rafters.md`).
- Исправить арифметику 8 примеров (список в разделе "Противоречия").
- `interior-trims/door-window-trim.md:41`: `9068` = 9'-0" x 6'-8".
- `start/how-to-use.md:14-19`: добавить вкладки OurPDF и "Excel и DFL".
- `reference/dfl-overview.md:273`: подпись "верно / неверно / неверно" вместо "правильный, с текстом в B и без цвета".
- Обрезать номер дома 225 на `photos/siding/board-batten-shingle-stone.jpg`, значок Google Lens на `confluence-030.png`, обрывок "See also" на `confluence-062.png`.

## Эталонные страницы

По ним стоит подтягивать остальные.

1. **`work/horizontal/floor-framing/details/rim.md`** (предметная страница). Одна схема (`framing/rim-board.svg`) показывает весь узел, рядом единица и фактор; таблица продуктов "когда какой"; правило фактора со ссылкой на канон; ошибки конкретные; скрин замера совпадает с темой.
2. **`work/exterior-trims/furring-and-jambs.md`** (схема = таблица). 10 номеров на разрезе `trims/furring-jambs.svg` совпадают со строками таблицы DFL; правило "jamb против blocking" есть и на схеме, и в тексте; критерий LFT или SQ FT записан; разрез показывает то, чего не видно на фасадах. Этот формат нужен soffit-fascia, balcony-buildup, exclusions.
3. **`work/horizontal/roof-framing/h-clips.md`** (правило + числа). Таблица кромок, сколько пролётов на лист, оговорки производителя со ссылками, ошибки с реальными цифрами ("4 на лист" против шага опор), пример сходится с соседней roof-sheathing.
4. **`start/takeoff-structure.md`** (канон процесса). Две схемы дерева, где у каждой ветки инструмент и пример имени, таблица веток и форматов, таблица "число в имени и его единица", коды флагов M под катом.
5. **`reference/standard-notes.md`** (текстовый справочник). Правило, пары "было / стало" из реальных сданных работ, "факт в строке = без ноты", таблица сокращений, библиотека формулировок под катом.

Для программных страниц эталон - `reference/ourplancore-course.md` (цель, шаги, "проверь себя", ролик) и `ourpdf/overlay.md` (что не делает - сразу наверху, задачи по шагам, таблица "что сохраняется", отладка). Рядом с ними хороши `bearing-walls.md`, `sill-plates.md`, `parapet.md`, `overframes.md`, `ourpdf/crop.md`.

**Рецепт эталона одной строкой:** разрез или план самого элемента, где каждая деталь пронумерована и номер = строка DFL с единицей; рядом таблица с формулой и фактором; ошибки с реальными цифрами; пример, который сходится арифметически и совпадает с соседними страницами; скрин замера именно этого элемента.

## Полная таблица по разделам меню

### Старт

| Страница (путь от docs) | Ясность | Полнота | Визуал | Согласованность | Итог | Главная проблема |
| --- | --- | --- | --- | --- | --- | --- |
| start/how-to-use.md | A | B | B | C | B | таблица вкладок устарела: нет OurPDF и "Excel и DFL", формулы и ноты отнесены к Справочнику |
| start/workflow.md | A | A | B | B | A | подпись к pages-panel.png не совпадает с картинкой; стрелка на work-process.svg идёт по тексту шага 3; "SF для листов" |
| start/takeoff-structure.md | A | A | B | A | A | takeoffs-root.png не показывает корпуса, о которых подпись; sheet-dots.png нечитаем |
| start/quality-checklist.md | B | A | - | C | B | высота стойки "минус plates" и "SF для листов" спорят с другими страницами; пара пунктов шифром |
| start/common-mistakes.md | A | A | C | C | B | ни одной картинки "так/не так"; высота стойки "минус plates"; ссылка на несуществующий раздел "Wall Sizing" |
| start/client-rules.md | B | B | - | B | B | строка "Reconstruction, NO metal" склеивает две разные пометки; нюансы EWP by others не описаны |

### OurPDF

| Страница (путь от docs) | Ясность | Полнота | Визуал | Согласованность | Итог | Главная проблема |
| --- | --- | --- | --- | --- | --- | --- |
| ourpdf/index.md | A | A | B | A | A | хорошая страница-вход |
| ourpdf/how-to-measure.md | A | B | B | A | B | нет рецепта Count, Openings, Beam: слово Count на странице не встречается |
| ourpdf/window.md | B | A | B | B | B | полосы top-panel и info-line нечитаемы на 760 px; блок "Замер" снят без Beam и Openings |
| ourpdf/measure.md | B | A | B | B | B | 650 строк, редкое (Pitch, концы линий) между частым; 4 скрина окна целиком без отметок |
| ourpdf/excel-link.md | B | A | A | A | A | плотный Auto Link, но с предупреждениями и окном результата |
| ourpdf/comments-save.md | A | A | C | A | B | одна картинка, нет инструментов комментариев и окна "Сохранить как" |
| ourpdf/pages-edit.md | B | A | C | C | C | одна картинка на 6 задач; на ней "Ctrl+S сохраняет новый файл", текст `:15` говорит "в исходный файл" |
| ourpdf/overlay.md | A | A | A | A | A | эталон программной страницы |
| ourpdf/crop.md | A | A | A | A | A | ограничения наверху, таблица "что в PDF", отладка |
| ourpdf/view-settings.md | B | B | B | A | B | в таблице нет двух настроек, которые видны на скрине |
| ourpdf/shortcuts.md | A | A | - | A | A | клавиши совпали со всеми страницами |
| ourpdf/ai.md | A | B | B | A | B | общий скрин Настроек, нужная галка без отметки |

### Работа: типы работ

| Страница (путь от docs) | Ясность | Полнота | Визуал | Согласованность | Итог | Главная проблема |
| --- | --- | --- | --- | --- | --- | --- |
| work-types/residential.md | B | B | C | B | B | главная SVG - пустой контур дома, подписи указывают в пустоту |
| work-types/reconstruction.md | B | C | C | B | C | нет "как мерить и назвать" и примера; пометку черновика сняли без источника |
| work-types/com.md | B | A | B | B | B | подпись confluence-057 про чердачный draft stop, а на детали перекрытие UL L546 |
| work-types/ewp-capital.md | B | B | B | A | B | EWP by others без исключений (assumed LVL, `EWP Floors by others`) |

### Работа: стены

| Страница (путь от docs) | Ясность | Полнота | Визуал | Согласованность | Итог | Главная проблема |
| --- | --- | --- | --- | --- | --- | --- |
| work/vertical/walls/wall-panels.md | B | B | C | A | B | картинка - обычная stick-стена, не "что в панели, что loose" |
| work/vertical/walls/sill-plates.md | A | A | A | B | A | `Anchor Bolts 48" o.c.` без упоминания дефолта 36" |
| work/vertical/walls/basement.md | B | C | C | B | C | схема не рисует обещанное подписью; в DFL-таблице нет `Wall Sheathing`, `Insulation` |
| work/vertical/walls/unit.md | A | B | D | B | C | главный скриншот пустой: "Scale: not set", белый лист, чёрная половина |
| work/vertical/walls/exterior.md | A | A | B | B | B | главная SVG общая, пишет "WRB / Tyvek", стрелки мимо |
| work/vertical/walls/bearing-walls.md | A | A | A | B | A | фраза "BW в walls не рисуются" (exterior.md:38) путается с bearing-walls:13-15 |
| work/vertical/walls/metal-tracks.md | B | B | B | A | B | нет `Tracks (1) top`; деталь 2828x3922 px, 556 KB |
| work/vertical/walls/corridor.md | B | B | C | C | C | Bracing в LFT; строки `Bracing for Drywall` в DFL нет; картинка - вырезка из словаря |
| work/vertical/walls/demising.md | B | A | B | C | B | подпись и SVG "каждый каркас своя линия" против шага 2 "одна линия `dem (2)`" |
| work/vertical/walls/gable.md | B | B | C | C | C | фото "gable truss" - обычная W-ферма; Draft Stop SQ FT против 4x8 рядом |
| work/vertical/walls/parapet.md | A | A | A | B | A | подписи строк в SVG не совпадают с labels DFL |
| work/vertical/walls/shaft.md | C | B | A | B | C | панели `LFT x 1.1 / 24`: делить надо площадь (LFT x высота), сейчас недосчёт в разы |
| work/vertical/walls/furring.md | B | B | A | B | B | своего мало, канон в furring-and-jambs; в SVG снова Tyvek |
| work/vertical/walls/corners.md | B | B | A | B | B | SVG "на каждый наружный угол", текст про углы и T-пересечения |

### Работа: проёмы

| Страница (путь от docs) | Ясность | Полнота | Визуал | Согласованность | Итог | Главная проблема |
| --- | --- | --- | --- | --- | --- | --- |
| work/vertical/openings/windows-doors.md | A | B | C | B | B | подпись "фасад, рамка, 3.0x5.0", на кадре план, 3.0x4.0 и рамки нет |
| work/vertical/openings/window-flashing.md | A | B | A | C | B | строки `Door Flashing` в DFL нет; своя SVG кладёт двери в `Window Flashing` |
| work/vertical/openings/headers.md | A | A | B | B | A | в SVG "(2)/(3) = число плёнок" вместо plies |

### Работа: Floor Framing, детали, Roof Framing, Ceiling

| Страница (путь от docs) | Ясность | Полнота | Визуал | Согласованность | Итог | Главная проблема |
| --- | --- | --- | --- | --- | --- | --- |
| work/horizontal/floor-framing/post.md | B | A | B | B | B | post-height.svg: пост через 3 этажа подписан `6x6 8.2`; Count-скрин показывает двери, а не посты |
| work/horizontal/floor-framing/beam.md | A | A | C | B | B | главная картинка - общий скрин Beam (`RB1 16` при Line 50,22 ft); нет схемы flush против dropped |
| work/horizontal/floor-framing/joist.md | B | B | B | B | B | нет схемы перекрытия и зон; TJI 9 1/2 без прямого ответа; `G` в формуле hangers не определён |
| work/horizontal/floor-framing/stair.md | B | B | B | B | B | пример LSC `=8*G` при 4 stringers; схема без площадки и rise/run |
| work/horizontal/floor-framing/subfloor.md | B | C | C | C | C | panel adhesive "по норме шаблона", канон `/3`, пример даёт 1 тубу на лист |
| work/horizontal/floor-framing/details/rim.md | A | A | A | B | A | эталон; примеры с `1.05` без пометки "EWP job" |
| work/horizontal/floor-framing/details/ribbon.md | B | B | B | C | B | схема `Ribbon 1x6 LFT` против `2x4` и формулы `/D` на странице |
| work/horizontal/floor-framing/details/blocking.md | B | B | C | C | C | Bracing for Trusses: на сайте три формулы и две единицы; фото bridging против правила TB27 |
| work/horizontal/floor-framing/details/blockingoc.md | C | B | C | B | C | разбор примера неверен по размерности; на схеме joists подписаны "Blocking rows" |
| work/horizontal/floor-framing/details/bracingdrywall.md | C | B | C | C | C | смешаны bracing стен и опора гипса; длина kicker "по высоте стены" неправдоподобна |
| work/horizontal/floor-framing/details/bolts.md | B | B | D | B | C | главная схема - анкер к бетону (Titen HD с гайкой), который страница исключает |
| work/horizontal/floor-framing/details/screws.md | B | B | B | B | B | округление `;3` и "до чётного" заданы одновременно |
| work/horizontal/floor-framing/details/steelbeams.md | A | A | B | B | B | нет "no fillers at dropped steel beams"; nailer на схеме шире полки и в один слой |
| work/horizontal/roof-framing/ridge.md | B | B | C | C | B | `LSSR2.1Z` против правила Zmax; только общий скрин Beam, нет разреза ridge board и ridge beam |
| work/horizontal/roof-framing/header.md | B | B | B | C | B | `Dbl Rafters` 2 на skylight против 4 на dbl-trpl; подписи 138 и 139 перепутаны |
| work/horizontal/roof-framing/hip.md | A | A | B | C | B | ridgevalleyhip.md учит другой инструмент; строка примера в hip-valley-length.svg обрезана |
| work/horizontal/roof-framing/valley.md | B | B | C | C | B | своей схемы нет, фото HABS тёмное и без стрелок |
| work/horizontal/roof-framing/dormer.md | B | B | B | C | B | в примере нет строк DFL; `Dbl Rafters` "точки" против "точки x 2" |
| work/horizontal/roof-framing/overframes.md | A | A | A | B | A | эталон; в примере 14 листов, по формуле 15 |
| work/horizontal/roof-framing/dbl-trpl-rafters.md | B | B | C | C | C | `точки x 2` против dormer и header; `LSSR2.56Z`, `LRU212Z`; своей схемы нет |
| work/horizontal/roof-framing/canopy.md | A | A | B | C | B | подписи DFL в canopy-parts.svg не как в таблице страницы |
| work/horizontal/ceiling-soffit-framing.md | C | B | C | B | C | ветка дерева "Уточняется"; G и H меняют смысл от строки к строке; схема без plates |

### Работа: обшивка (Sheathing)

| Страница (путь от docs) | Ясность | Полнота | Визуал | Согласованность | Итог | Главная проблема |
| --- | --- | --- | --- | --- | --- | --- |
| work/vertical/sheathing/wall-sheathing.md | A | A | C | B | B | ни одной схемы: стоковое фото и скриншот Instagram |
| work/vertical/sheathing/exterior-materials.md | B | A | B | B | B | деталь в половине колонки не читается; WRB на SVG не подписан |
| work/vertical/sheathing/floor.md | B | B | B | C | B | дублирует Subfloor; subfloor.md:10 описывает её не так, как она сама (:14-15) |
| work/horizontal/roof-framing/roof-sheathing.md | A | A | C | A | B | главное фото любительское: палец в кадре, клипсы не видны |
| work/horizontal/roof-framing/h-clips.md | A | A | A | A | A | эталон |
| work/vertical/sheathing/gable.md | B | B | C | C | C | дубль Gable Walls; Draft Stop `1/2" Ply` 4x8 против OSB SQ FT; голая схема |
| work/vertical/sheathing/box-sheathing.md | A | A | B | B | B | SVG пишет SQ FT, таблица 4x8; "только между панелями" сбивает |
| work/vertical/sheathing/truss-heel.md | B | C | B | C | C | висит плашка "Уточняется" про label; SVG SQ FT против 4x8; нет Tape и Insulation |
| work/vertical/sheathing/shear-wall.md | B | B | C | B | B | `H` в формуле не объяснён; главное фото shear wall не показывает |
| work/vertical/sheathing/holdowns.md | A | A | B | B | A | строка `HD1 (2) DTT2Z` неясна по множителю |

### Работа: Roof Misc

| Страница (путь от docs) | Ясность | Полнота | Визуал | Согласованность | Итог | Главная проблема |
| --- | --- | --- | --- | --- | --- | --- |
| work/sheathing-and-misc/eve.md | B | B | C | B | B | фото без пометок eave и rake; на svg стрелки смотрят на подписи, нет frame и sub fascia |
| work/sheathing-and-misc/rake.md | C | C | C | B | C | нет формул и строк DFL; вопрос про уклон без ответа; eave нарисован по низу стен |
| work/sheathing-and-misc/returns.md | B | C | B | C | C | нет формул; svg пишет pcs, страница LFT; папка eves или rakes не решена |
| work/sheathing-and-misc/rooftype.md | B | B | B | B | B | одна схема только для flat; скатные типы без картинки |
| work/sheathing-and-misc/ridgevalleyhip.md | C | C | C | D | D | велит мерить hip и valley Line в details, а hip.md и valley.md - Beam в beams; схема с неверной геометрией |
| work/sheathing-and-misc/flashing.md | B | C | B | B | B | нет факторов; ветка "Уточняется"; в примере материал `pcs` |

### Работа: SQFTs

| Страница (путь от docs) | Ясность | Полнота | Визуал | Согласованность | Итог | Главная проблема |
| --- | --- | --- | --- | --- | --- | --- |
| work/sqfts/basement.md | B | B | A | B | B | sleepers "по шагу" без формулы |
| work/sqfts/1st2nd.md | A | B | B | B | B | правило свесов не задано (старый пункт AUDIT 6); floor.svg без x 1.1 |
| work/sqfts/loft.md | B | B | C | C | B | токен `loft` "Уточняется"; joists в примере `LFT` |
| work/sqfts/roof.md | A | B | B | B | B | входят ли свесы, не сказано; svg "membrane: by others" против строки EPDM |
| work/sqfts/deck.md | B | B | B | C | B | decking x 1.1 против `W*D*G`; deck.svg: LUS28 на 2x10 P.T. без Zmax, Titen HD на ledger |
| work/sqfts/porch.md | B | B | C | B | B | на схеме нет обязательных ceiling joists; потолок x 2 x 1.1 против canopy без 1.1 |
| work/sqfts/balcony.md | B | B | C | C | B | decking x 1.1 x units против `W*D*G` |
| work/sqfts/cantilevered.md | B | B | C | B | B | висящий текст "cantilever -"; вычитать ли вынос из этажа, не сказано |

### Работа: Deck / Porch / Balcony

| Страница (путь от docs) | Ясность | Полнота | Визуал | Согласованность | Итог | Главная проблема |
| --- | --- | --- | --- | --- | --- | --- |
| work/deck/deck-porch-balcony-frame.md | B | B | B | C | B | потолок porch `=CEILING(G*2*1.1,10)*G` с G дважды; decking `W*D*G` против dfl-blocks; скрин Count про двери |
| work/deck/railing.md | B | B | B | C | B | на схеме Balustrades в LFT, в таблице pcs; правила счёта секций на сторону нет |
| work/deck/balcony-trims.md | B | C | C | B | C | дубль Balcony build-up без примера; фото без выносок |
| work/deck/anchor-bolts.md | B | B | C | C | C | схема: дефолт 5/8" Titen HD с гайкой, текст 1/2" @ 36"; 1.1 то есть, то нет; washers 3x3 |

### Работа: Interior Trims

| Страница (путь от docs) | Ясность | Полнота | Визуал | Согласованность | Итог | Главная проблема |
| --- | --- | --- | --- | --- | --- | --- |
| work/interior-trims/overview.md | B | B | C | B | B | единственная картинка - старый скрин с подписью "кок"; исключений из подписи на ней нет |
| work/interior-trims/base.md | B | B | B | B | B | архивные карточки без подписей; int-trims-12 показывает числа без формулы |
| work/interior-trims/casing.md | C | B | B | C | C | jambs `=casing/2` LFT против "точками по юнитам"; "две стороны" без x2 в формуле |
| work/interior-trims/crown.md | B | B | C | B | B | карточки 18 и 22 без подписей; на 22 лист без масштаба |
| work/interior-trims/door-window-trim.md | B | B | B | C | B | `9068` расшифрован как 9'-0" x 8'-0" (это 9'-0" x 6'-8") |
| work/interior-trims/room-schedule.md | B | B | C | B | C | нет ни одного реального room schedule, макет не совпадает с подписью |

### Работа: Exterior Trims

| Страница (путь от docs) | Ясность | Полнота | Визуал | Согласованность | Итог | Главная проблема |
| --- | --- | --- | --- | --- | --- | --- |
| work/exterior-trims/overview.md | B | B | C | C | B | ни одной картинки; подписи строк не из канона takeoff-items; corner boards без x2 |
| work/exterior-trims/exclusions.md | B | B | D | C | C | главная схема говорит обратное правилу: "J-channel часто идёт с EIFS" в зелёном |
| work/exterior-trims/casing-corner-band.md | B | B | B | C | B | corner boards x1 без 1.1; в примере `=2*5.5*34` = 374, написано 380 |
| work/exterior-trims/furring-and-jambs.md | A | A | A | B | A | эталон; мелочь в арифметике примера |
| work/exterior-trims/soffit-fascia.md | C | B | C | C | C | soffit LFT или SQ FT не ясно: 12" vinyl в SQ FT, 9" vinyl в LFT, eve.md:56 велит SQ FT |
| work/exterior-trims/porch-deck-balcony.md | B | B | C | C | B | CAD-деталь flare с битым шрифтом; Column wrap pcs на схеме, LFT в таблице |
| work/exterior-trims/rails-decking.md | B | B | B | C | B | decking `=W*D*G` против dfl-blocks; примитивная схема |
| work/exterior-trims/balcony-buildup.md | B | B | D | C | C | на схеме sleepers под EPDM и decking на мембране; post wrap на 6 постов при 12 |
| work/exterior-trims/shower-pergola.md | B | B | B | B | B | у pergola нет картинки и правила счёта trellis |
| work/exterior-trims/macros.md | B | B | C | A | B | нет скрина выделения и результата C_TrimsCalc |

### Работа: Siding

| Страница (путь от docs) | Ясность | Полнота | Визуал | Согласованность | Итог | Главная проблема |
| --- | --- | --- | --- | --- | --- | --- |
| work/siding/overview.md | B | B | B | B | B | фото без выносок трёх материалов; виден номер дома 225 |
| work/siding/types.md | B | B | B | B | B | на фото lap нет отметки exposure, а подпись про неё |
| work/siding/underlayment.md | A | B | B | C | B | Zip Tape в "rolls", на страницах обшивки LFT |
| work/siding/eifs-stucco-veneer.md | A | B | B | C | B | схема "J-channel наш" без условия; пример считает WRB вместе с Zip |
| work/siding/measure.md | B | C | C | C | C | waste нигде не задан числом; схема вычитает мелкие окна; нет скрина OurPlanCore |

### Excel и DFL

| Страница (путь от docs) | Ясность | Полнота | Визуал | Согласованность | Итог | Главная проблема |
| --- | --- | --- | --- | --- | --- | --- |
| reference/dfl-overview.md | B | A | A | C | B | колонка D описана только как единица, а в схемах и формулах D это длина доски; таблица "шаблон и готовый файл" читается как соответствие строк |
| reference/takeoff-items.md | B | A | C | C | B | пример: формула `=CEILING(G140/D140,1)` делит на D, а в D написано `LFT`; нет картинки строки A:H |
| reference/standard-notes.md | A | A | B | A | A | мелочь: одна картинка, и та общая с dfl-overview |
| reference/dfl-blocks.md | B | A | C | C | B | главная картинка - план каркаса, а не блок в Excel; пример ставит `LFT` в D там, где строка 45 велит длину 14' |
| reference/ewood-tab.md | B | A | B | B | B | плотный текст для опытного; таблица клавиш дублирует excel-hotkeys; шаги нарисованы картинками из текста |
| reference/excel-hotkeys.md | A | A | C | B | B | единственная картинка excel-strip.png 31x424 px, ничего не прочесть; дублирует ewood-tab |
| reference/formulas.md | C | A | C | C | C | G, D, H, `Stock LF` нигде не определены; `=CEILING(G/4/D,1)` у truss bracing без объяснения; высота стойки "минус plates" |

### Справочник

| Страница (путь от docs) | Ясность | Полнота | Визуал | Согласованность | Итог | Главная проблема |
| --- | --- | --- | --- | --- | --- | --- |
| reference/boss-feedback-rules.md | B | A | B | C | B | правило "минус plates" (строка 9) спорит с собственным примером в той же строке |
| reference/hangers.md | B | B | C | C | C | `SUL/SUR` то 45 градусов (строка 50), то пример на 30 (строка 89); нет таблицы для пилёного 2x; схема выбора путает skew с concealed |
| reference/hardware-catalog.md | A | B | B | B | B | правило записи `Zmax` и суффикса `Z` неочевидно; фото ties не показывает tie |
| reference/material-catalog.md | A | B | C | B | B | ни одной картинки: семейства EWP и типы обшивки новичку надо видеть |
| reference/industry-standards.md | A | B | C | A | B | нет схемы анатомии стены (plates, king, jack, cripple, header) |
| reference/quantity-benchmarks.md | B | B | - | B | B | нет даты и объёма выборки; "Bracing 1 на 8 ft" больше нигде не встречается |
| reference/ai-assist-system.md | B | B | - | B | B | нормально; строки про терминалы и AI Crop Notes 16.11 помечены "только полная версия" |
| start/maintenance.md (редактору) | B | B | - | B | B | "Проверено 17 октября 2026 (3.0.0)" устарело |
| start/images-and-schemas.md (редактору) | A | B | B | B | B | шаблоны ок; нет правила "подпись должна совпадать с картинкой" |
| start/site-preview.md (редактору) | C | C | C | D | C | описывает старый шаблон страницы ("Что считать", "Правила", PlanSwift), противоречит how-to-use.md:32-44 |

OurPlanCore (31 страница) оценён отдельно, в разделе "OurPlanCore" ниже.

## Что исправить по страницам

Для страниц C и D - все правки; для B - 1-3 правки до A; для A - что делает страницу хорошей. Номера противоречий - из следующего раздела.

### Старт

**start/how-to-use.md** (B). Картинка `ourplancore/v3/window.png`: окно целиком, обзорная, ок.
- `:14-19` таблица вкладок: добавить строки OurPDF и "Excel и DFL", убрать из Справочника "формулы, ноты, имена строк DFL" (они во вкладке Excel и DFL).
- `:26-28` поиск: хорошо; можно добавить, что синонимы eave/eve уже ищутся.

**start/workflow.md** (A, но с правками). Картинки: `process/work-process.svg` - хорошая схема 8 шагов с легендой, но стрелка 2-3 продолжена через блок 3 до блока 4 и перечёркивает текст "точки W/F/S/U"; `framing/scan-order.svg` - понятно, но вторая полоса нарисована справа налево, а подпись "слева направо"; `ourplancore/v3/pages-panel.png` - подпись `:51` про папки `00. imported/Arch`, `Struct`, `sections`, а на кадре листы демо "03 PDF Output Ribbon", "unscaled"; `ourplancore/v3/takeoffs-panel.png` - ок; `ourplancore/v3/excel-strip.png` - 31x424 px, буквы кнопок не прочесть, что значит SF, WL, GB, нигде не сказано; `ourplancore/v3/export-pdf.png` - текст диалога 6-7 px.
- `:51` переснять pages-panel на проекте с раскладкой `00. imported/...` или поправить подпись.
- `:102-103` заменить excel-strip на подписанную схему кнопок XL.
- `:112-113` "SF для листов" заменить на правило D из dfl-overview (см. противоречие 2).
- `:5` "в Справочнике" заменить на "во вкладке Excel и DFL".

**start/takeoff-structure.md** (A, эталон для страниц-канонов). Картинки: `process/takeoff-tree.svg` и `process/takeoff-tree-framing.svg` - лучшие схемы раздела: дерево, инструмент, что несёт имя, всё подписано; `ourplancore/v3/takeoffs-root.png` - подпись `:28` про переключение корпусов, а на кадре один корпус без папок `Main`/`Grge`; `ourplancore/v3/sheet-dots.png` - сетка точек 8 px, правая половина кадра чёрная, статус обрезан, подпись говорит `W 2nd`, на кадре `W 1st`.
- `:27` взять кадр `ourplancore/v3/buildings-root-switch.png` или `buildings-tree.png`.
- `:96` переснять sheet-dots крупно.

**start/quality-checklist.md** (B). Картинок нет и не нужно.
- `:20` "минус plates" (противоречие 1).
- `:40` "наружная обшивка по Arch" (противоречие 3).
- `:56` "kitchen 2x6 4 по 14', bath 1 по 14'" расшифровать как в `formulas.md:66` ("4 штуки 2x6 по 14' на кухню, 1 штука на ванную").
- `:43` "Floor-height FRT полосы 2' или 4'" и `:58` "piggyback sleepers" без объяснения; дать ссылку на страницу темы у каждого пункта.
- `:78` "SF для листов" (противоречие 2).

**start/common-mistakes.md** (B). Картинок нет. Это вторая по важности страница для новичка, и на ней лучше всего работают пары "так / не так".
- Добавить 4-5 мини-схем: разрез с высотой стойки (что вычитать), окно с head height против высоты изделия, проём на плане и фасаде (двойной вычет), дерево с одинаковыми цветами против разных, нота над и под заголовком (уже есть `reference/dfl-note-placement.svg`, просто вставить).
- `:13` ссылка "Exterior, раздел Wall Sizing": такого раздела нет, есть `exterior.md#stud-height`; "минус plates" (противоречие 1).
- `:86` "SF для листов" (противоречие 2).

**start/client-rules.md** (B).
- `:16` разделить на две строки: Reconstruction и `NO metal`, это разные пометки.
- `:13` EWP by others: нет нюансов из чек-листа 2026 (assumed LVL без марки считаем; `EWP Floors by others` - только то, что на layout перекрытий). Старый пункт 6 `OFFICE_FOLDER_COVERAGE.md` открыт.
- `:38-47` на публичном сайте названы 8 клиентов. Не нарушение правил `AGENTS.md`, но решение владельца: оставить или заменить кодами.

Пропущено как служебные: `index.md` (главная-витрина; заметки: в маршруте "Я новичок" нет `reference/dfl-overview.md`, ссылка "Ridge / Hip / Valley" ведёт только на ridge, в hero "Как мерить, Что мерить" с заглавной), `start/suggest-change.md` (форма приёмной поправок).

### Работа: типы работ, стены, проёмы, обшивка

**work-types/reconstruction.md** (C). `work-types/reconstruction.svg` - только легенда из 4 линий, плана нет.
- Нарисовать мини-план: existing серым, demo пунктиром, new зелёным, кружки на ledger и hangers в местах стыка.
- Добавить раздел "Как мерить и назвать": новые стены отдельными позициями; в каноне DFL есть строка `Window Flashing in Exist Walls`.
- Добавить `## Пример` (дерево и 3-4 строки DFL с нотами).
- Пометку черновика сняли (коммит b2586bb) без реального примера, хотя `AUDIT.md` пункт 11 просил не снимать без подтверждения. Вернуть пометку или привязать к сданному проекту.

**work-types/residential.md** (B). `residential.svg`: контур дома, подписи "Walls + openings" и "Roof framing" указывают в пустое поле. Заменить схемой "дом + гараж + porch" с ветками дерева (Main/Grge, walls, sqfts rf 6 / rf 4, eves).

**work-types/com.md** (B). `confluence-057.png`: подпись `:117` про чердачный draft stop, а на детали "1 HR FLOOR / CEILING ASSEMBLY UL L546" (это draft stop в перекрытии, `demising.md:53`). `:112` "FRT и FRTW - разные обозначения" против `boss-feedback-rules.md:33` "одно требование": написать "одно требование, обозначение как в проекте".

**work-types/ewp-capital.md** (B). `:59` добавить исключения EWP by others (assumed LVL; `EWP Floors by others`, где attic, roof и stick porch остаются наши). Подпись `:14` к `ijoists-on-beam-post.jpg` говорит про "стойку 2x", на фото engineered колонна и стальные open web joists.

**work/vertical/walls/basement.md** (C). `basement-wall-section.svg` похожа на furring wall: нет top plates, обшивки и WRB, обещанные "Box sheathing + vapor barrier" не нарисованы. Перерисовать узел. В таблицу `:43-52` добавить `Wall Sheathing` и `Insulation`. `:48` Bracing не в LFT (противоречие 6).

**work/vertical/walls/unit.md** (C). `ourplancore/v3/sheet-unit.png`: "Scale: not set", белый лист, крошечная сетка точек, чёрная половина кадра, в статусе `ext 2x6 9.09`. Линий `A 2x4` / `A 2x6` из подписи `:5` нет. Нужен кроп плана юнита с линиями и крупной точкой U, второй кадр - Count-точки `B1` на плане этажа. Текст сильный: после замены картинки страница на A.

**work/vertical/walls/corridor.md** (C). `confluence-062.png` - вырезка из словаря без размеров, в `:9` остался `TODO-PHOTO`. Нарисовать разрез: plates 2x6, два ряда 2x4 по 16", ledger, joists, bracing. `:49` Bracing в штуках; `:51` строка `Bracing for Drywall` в DFL не существует, опора гипса это `Blocking for Drywall` в Floor Framing List; `:48` `Studs Corr`, в каноне `Studs Corridor`.

**work/vertical/walls/gable.md** (C). `confluence-083.png`: W-ферма без вертикальных стоек, а подпись `:6` про gable truss со стойками; 470 KB PNG на 752x231. `confluence-090.png`: старый инструмент, линия top по одному скату, хотя 70.3 FT означает два. Заменить фото на настоящую gable-end truss или схему "truss против stick"; свежий скриншот OurPlanCore; `:66` переписать "SQFT / D, D - заказная стойка 12'"; `:73` Draft Stop согласовать (противоречие 13).

**work/vertical/walls/shaft.md** (C). `:47-48` и `:55-56`: `1" Shaft Panels` = `LFT x 1.1 / 24`. 24 - это площадь панели 2'x12', значит делить надо площадь стены (LFT x высота). Шахта 64 LF x 10.5' даёт 4 панели вместо 32. То же в `reference/formulas.md:116-123`. Horizontal и perimeter оставить в LFT. `:23` "Перимeтральные" с латинской e.

**work/vertical/walls/demising.md** (B). `:5` и `demising-double-wall.svg` ("Line на каждый") привести к правилу `:36-38` ("одна линия `dem (2)`").

**work/vertical/walls/exterior.md** (B). `exterior-wall-section.svg` пишет "WRB / Tyvek" против `:95-96` и `:115`, стрелка Studs упирается в утеплитель. Лучше поставить на место главной картинки схему высоты стойки (`:49-54`). `:38` "BW и shear walls в walls не рисуются" переписать, чтобы не спорило с `bearing-walls.md:13-15`.

**work/vertical/openings/windows-doors.md** (B). `measure-openings.png` переснять на фасаде с рамкой проёма и именем из подписи.

**work/vertical/openings/window-flashing.md** (B). `:43` убрать `Door Flashing`; `:41-43` и пример `:69-72` с x 1.1.

**work/vertical/sheathing/wall-sheathing.md** (B). Обе картинки не по правилу (`confluence-094.jpg` сток, `confluence-093.jpg` скриншот Instagram с кнопками). Нарисовать фасад: LFT x высота, проём шире 4' вырезан, узкое окно не вычитается, полосы box, heel, gable отдельно.

**work/vertical/sheathing/gable.md** (C). Дубль `walls/gable.md`; `gable-sheathing.svg` - голый треугольник, выноска пересекает скат, heel из подписи нет; `:49` Draft Stop `1/2" Ply` 4x8 против `walls/gable.md:73` OSB SQ FT.

**work/vertical/sheathing/truss-heel.md** (C). `:56-58` плашка "Уточняется" про label, а label в каноне DFL есть (`Truss Heel Sheathing`). `truss-heel.svg`: SQ FT при 4x8 в таблице `:52`, стрелка "Roof sheathing" упирается в top chord. `raised-heel-truss-at-wall.jpg` мягкое, в кадре синяя полоса интерфейса. Добавить строки Tape и Insulation.

**work/vertical/sheathing/roof-sheathing.md** и **shear-wall.md** (B). Главные фото не показывают предмет (палец в кадре; shear wall не узнать). Заменить схемой ската и схемой плана SW; в `shear-wall.md:49` объяснить `H`.

### Работа: перекрытия, детали, кровля, roof misc, площади

**work/sheathing-and-misc/ridgevalleyhip.md** (D). `:33-34` "Hip и valley rafters: Line по линии ребра, в `framing/roof framing/details/<сечение> hip`", а `hip.md:25`, `:52` и `valley.md:28`: инструмент Beam, путь `framing/roof framing/beams/hip ...`. Предупреждение `:39-41` "ветка не зафиксирована" устарело. `:48` `Hip plates` против `hip.md:56` `Hip Rafters`; `:54` опечатка "труss" (кириллица внутри слова). Схема `roof/ridge-valley-hip.svg`: hips не сходятся с коньком, valley идёт внутри пристройки, а не по стыку скатов. Сделать страницу коротким обзором со ссылками на hip, valley, ridge, схему заменить фрагментом `roof/hip-valley-length.svg` (он нарисован верно).

**work/horizontal/floor-framing/subfloor.md** (C). `:28`, `:38` "по норме шаблона" - записать норму: канон `formulas.md:81` и `material-catalog.md:59` дают `=C<subfloor>/3`, а пример `:58` даёт 84 тубы на 60 + 24 листа (1 на лист). `:36-37`, `:56-57` сказать, вычитается ли FRT-полоса из основного `Subfloor`. `framing/subfloor.svg` без FRT-полосы, о которой подпись. `confluence-154.png` 736 KB.

**work/horizontal/floor-framing/details/blocking.md** (C). Bracing for Trusses: `:44` "1 ряд на каждые 10' по площади", `:72` `=ОКРВВЕРХ(G*1.1/D;1)`, `formulas.md:80` `=CEILING(G/4/D,1)` с новым исключением (не над несущими стенами, не там, где stick или TJI), `roof-sheathing.md:58` unit `LFT`. Нужна одна формула и порядок замера. `:53` cross bridging TB27 в pcs, а `takeoff-items.md:63` и подпись фото `:10` в LFT; добавить "or solid blocking; verify". `framing/blocking.svg` пишет "LFT (без factor)" против `:48` "LFT x 1.1".

**work/horizontal/floor-framing/details/blockingoc.md** (C). `:56` "60 рядов, x 2 = 120 кусков, x 1.1 = 132, / 16 = 9 досок": куски делятся на длину доски в футах, размерность не сходится. Формула верна, только если множитель - длина одного куска (flat 2', diagonal 2.5'), а `G*12/H` - число кусков вдоль линии. Если ряды идут поперёк всей зоны, как говорят `:22` и схема, формула занижает в разы. Нужно слово владельца, какой смысл верный; та же неясность в `formulas.md:58-62`. `:44` "1.1 второй раз, хотя G уже содержит waste" - G это длина линии, waste в ней нет. `framing/blocking-oc.svg` подписывает длинный элемент (joist) как "Blocking rows".

**work/horizontal/floor-framing/details/bracingdrywall.md** (C). Смешаны две вещи: bracing стены (`Bracing Ext Walls`, одна доска на 8 LFT, длина по высоте стены) и опора гипса у стены параллельно joists (`Blocking for Drywall`, LFT). `demising.md:51-52` их разделяет, а `:5`, `:12`, `:28` называют bracing опорой гипса. `framing/drywall-bracing.svg` показывает длину kicker у верха стены "по высоте стены" - от высоты зависит диагональный brace, а не kicker; подписи `LFT` против pcs в тексте. Таблица длин `:38-43` (14' до 10', 16' до 12', 18' до 16') расходится с чек-листом Ural 2026 (14' до 9', 16' до 11', 18' до 14', 20' выше).

**work/horizontal/floor-framing/details/bolts.md** (C, визуал D). Главная `framing/anchor-bolt.svg` - анкер sill plate в бетон, "Дефолт 5/8" Titen HD" с гайкой, а страница `:12` такие анкеры исключает, примеры болтов 3/8". У Titen HD гайки нет. Нужна схема through bolt балка-пост или болтов nailer на стальной балке. `:33`, `:57` подпись `Anchor Bolts 24" o.c. (2)` для болтов nailer объяснить как подпись шаблона.

**work/horizontal/roof-framing/dbl-trpl-rafters.md** (C). `:38` `точки x 2`, `:39` `точки x 3` против `dormer.md:52` и `header.md:58` (точки; для одного skylight здесь 4, там 2). `:40`, `:57` `LSSR2.56Z`, `LRU212Z` - формат Zmax (противоречие 5). Своей схемы нет; подпись `:61` "ближе" стоит у общего вида (`confluence-141.png`), крупный план - 140.

**work/horizontal/ceiling-soffit-framing.md** (C). `:28`, `:30-31` ветка дерева "Уточняется": без ответа владельца новичок не знает, куда класть замер. `:46` G и H меняют смысл от строки к строке (периметр или площадь, число plates или шаг): расписать для каждой строки. `:41` у Frame нет x 1.1, у Plate есть. `framing/ceiling-soffit.svg` без plates и frame с шагом; на фото короба не видно.

**work/sheathing-and-misc/rake.md** (C). `:28-29` "решай один раз, нужна ли наклонная длина" - дать правило (план x фактор уклона или фасад), как на hip.md. В таблице `:36-41` нет формул; в примере только дерево. `roof/rake.svg`: eave нарисован по низу стен, свеса нет.

**work/sheathing-and-misc/returns.md** (C). `:50-52` нет формул (soffit return, fascia, crown). `:41` папка `eves rakes/rakes` против `soffit-fascia.md:51` `eves rakes/eves/returns 12`. `roof/returns.svg` пишет `LFT или pcs`, у pork chop `pcs`, страница `:40` LFT. У `trims/ext-pork-chop.png` и `ext-eave-return.png` нет источника.

**work/horizontal/floor-framing/post.md** (B). `framing/post-height.svg`: непрерывный пост через три этажа подписан `6x6 8.2` (это около 27 ft). `measure-count.png` показывает двери, а подпись `:38` про посты. `:55` `Posts (3)` "точки x 3" против `beam.md` (противоречие про `(n)`).

**work/horizontal/floor-framing/beam.md** (B). Главную картинку заменить разрезом flush против dropped (`Beam (2) Flush`, `Beam (3) Dropped`); скрин Beam перенести в "Как мерить", с длиной в имени, совпадающей с линией. `:105` `HU412` не подходит ни к `(2) 2x10`, ни к `(3) 1 3/4 x 11 7/8 LVL` из примера.

**work/horizontal/floor-framing/joist.md** (B). `:65` дописать ответ "TJI 9 1/2: серии 110, 210, 230" (видно на `confluence-007.png`, старый пункт `AUDIT.md` 5). `:46` объяснить G в `=ЧЁТН(G*12/16)`; `:47` `LFT x 1.05` пометить "EWP job". Добавить схему перекрытия сверху: зоны J Area, rim, blocking, hangers, extra и double joists.

**work/horizontal/floor-framing/stair.md** (B). `:85` `Hangers LSC =8*G` при `Stringers (4) =4*G` и правиле `:53` "LSC один на верхний конец stringer". В `framing/stair.svg` нет площадки и треугольника rise/run.

**work/horizontal/roof-framing/hip.md**, **valley.md**, **ridge.md** (B). Свести с ridgevalleyhip. В `roof/hip-valley-length.svg` строка примера уходит за viewBox, "заказ 20'" обрезано, ASCII-стрелка `->`. `hip.md:52` "`Ridge / Valley / Hip` в LFT" против `:58` (доски по 16'). `valley.md` - своей схемы нет, вырезать из hip-valley-length. `ridge.md:43` `LSSR2.1Z`; нужен разрез ridge board против ridge beam. Фото HABS и HAER (`valley-rafters-attic-habs.jpg`, `dormer-framing-attic-habs.jpg`, `dormer-opening-header-haer.jpg`) тёмные, без стрелок элемент не найти.

**work/horizontal/roof-framing/canopy.md** (B). `roof/canopy-parts.svg` подписи (`Subfloor 3/4" T&G SQ FT`, `Beam (2) 2x10 LFT`) против таблицы `:55`, `:60`, `:62`. `:62`, `:90` soffit SQ FT x слои без waste против `porch.md:41` x 2 x 1.1.

**work/sheathing-and-misc/eve.md** (B). Подписать eave и rake на главном фото; в `roof/eave-parts-takeoff.svg` стрелки Truss heel и Fascia смотрят на подписи, нет frame for soffit и sub fascia; добавить скрин Line `eve 24 main`.

**work/sqfts/1st2nd.md**, **roof.md**, **cantilevered.md** (B). Ни одна из 8 страниц площадей не говорит, входят ли свесы (старый пункт `AUDIT.md` 6 открыт): одно правило в `1st2nd.md:16-33`. `sqfts/floor.svg` "sheets = SQFT / 32" без x 1.1. `sqfts/roof-sqft.svg` "membrane: by others" против `roof.md:46` EPDM. `sqfts/cantilevered.svg` висящий текст "cantilever -".

**work/sqfts/deck.md**, **balcony.md**, **porch.md** (B). Decking x 1.1 против `W*D*G` (противоречие 16). `sqfts/deck.svg`: `LUS28` под 2x10 P.T. без Zmax, `Titen HD` на ledger к дереву, ASCII `->`. `sqfts/porch.svg` без ceiling joists, ledger и hangers, которые страница называет обязательными.

### Работа: deck, trims, siding

**work/deck/balcony-trims.md** (C). Дублирует `exterior-trims/balcony-buildup.md:42-50` (дубли запрещены, `AGENTS.md` раздел 8): сделать указателем или слить. Нет примера. `confluence-152.png` без выносок, flashing у стены не виден; 648 KB.

**work/deck/anchor-bolts.md** (C). `framing/anchor-bolt.svg`: "Дефолт 5/8" Titen HD", а текст `:31`, `:47` говорит 1/2" @ 36"; у Titen HD на схеме нарисованы шайба и гайка, у этого анкера гайки нет. Фактор 1.1 в `:47` есть, в `:58` и `:84` нет. Шайбы 3x3 (`:48`, `:60`, `:86`) против `boss-feedback-rules.md:86` "по таблице, не универсальные 3x3". Страница в разделе Deck, а почти вся про анкеры sill plate фундамента.

**work/deck/deck-porch-balcony-frame.md** (B). `:90` потолок porch: `=CEILING(G*2*1.1,10)*G` множит на G дважды, как в `sqfts/porch.md:41` должно быть `W*D*2*1.1`. `framing/deck-frame-plan.svg`: `LUS28` под joists 2x10, без Zmax, ledger на `Titen HD 5/8"` вместо screws `SDWS22400DB` (`:83`, `:86`). `measure-count.png` про двери, а подпись `:59` про балконы.

**work/interior-trims/casing.md** (C). `:36`, `:56` и SVG: jambs `=casing/2` в LFT, а `boss-feedback-rules.md:123` и `windows-doors.md:62-63` велят "точками по юнитам". `:34` записать формулу как `=(2*H+W)*2*qty` (сейчас x2 только в примере). Waste 1.1 из шаблона не отражён.

**work/interior-trims/room-schedule.md** (C). Нет ни одного реального room schedule (`:8` TODO-SCREEN), а страница о том, как его читать. `room-schedule.svg` - макет с колонками Room/Base/Crown/"Считать?", подпись обещает Floor/Base/Walls/Ceiling/Remarks.

**work/interior-trims/door-window-trim.md** (B). `:41` `9068` это 9'-0" x 6'-8". Оговорить, что bi-fold шире 4' - исключение из правила "двойные".

**work/exterior-trims/exclusions.md** (C). `trims/exclusions.svg`: "J-channel часто идёт с EIFS", J-channel и casing bead в зелёном "проверяем". Это обратное `:39` и `:57` ("J-channel с EIFS записан как наш" - ошибка). Перерисовать как разрез стыка vinyl siding с облицовкой: что наше, что by others.

**work/exterior-trims/soffit-fascia.md** (C). Единицы: `:45` "доска LFT, panel SQ FT", пример `:81` 12" vinyl в SQ FT, `:84` 9" vinyl в LFT, `eve.md:56` "vinyl soffit в SQ FT". Нужно одно правило с порогом (старый вопрос `AUDIT.md` Q5). Нужна схема разреза свеса: soffit, fascia, sub fascia, frieze, trim over fascia, rake moulding с единицами. Дефолт soffit по типу siding из тренинга 7.4.24 не перенесён. `ext-eave-return.png`, `ext-pork-chop.png` - журнальные скетчи без строк DFL.

**work/exterior-trims/balcony-buildup.md** (C). `trims/balcony-buildup.svg`: снизу вверх subfloor, sleepers, EPDM, decking - мембрана поверх sleepers и decking прямо на мембране, так не строят; сверить с реальным разрезом. На схеме "Decking (часто by others)", а `:45` "здесь". Пример `:78` post wrap на 6 постов, а в блоке `deck-porch-balcony-frame.md:130` их 12. `:41` "часто 2 слоя" sleepers (вопрос `AUDIT.md` Q7) не решён.

**work/exterior-trims/casing-corner-band.md** и **overview.md** (B). Corner boards x1 без x2 и без 1.1 (`casing-corner-band.md:50`, `:75`, `:80`; `overview.md:125`) - старый пункт 1 `OFFICE_FOLDER_COVERAGE.md` открыт. `casing-corner-band.md:77` `=2*5.5*34` даёт 374, написано 380 (та же ошибка в `macros.md:29`). На overview нет ни одной картинки: нужна схема фасада с группами отделки и единицами.

**work/siding/measure.md** (C). `:52-54` waste без числа, ссылка на `formulas.md`, где siding нет. `measure.svg` вычитает мелкие окна (правило 4' нарушено) и пишет "Waste 1.1", которого в тексте нет. `:8` нет скрина OurPlanCore.

**work/siding/overview.md** (B). На `board-batten-shingle-stone.jpg` виден номер дома 225: обрезать.

### OurPDF

**ourpdf/pages-edit.md** (C). На `ourpdf/pages-tab.png` подсказка "Ctrl+S сохраняет новый файл", текст `:15` и `comments-save.md:234` говорят "в исходный файл". Одна картинка на 6 задач: нужны сетка "Систематизировать страницы", полоса "Редактировать PDF", панель "Слои", результат "Обвести слой".

**ourpdf/how-to-measure.md** (B). Нет рецепта Count, Openings, Beam. **ourpdf/window.md** (B): `block-measure.png` и `top-panel.png` сняты до 0.9.30, без Beam и Openings, хотя `measure.md:79`, `:210` их описывает. **ourpdf/measure.md** (B): переставить по частоте, Pitch, P Line, Break, Ends, концы линий в "Дополнительно"; 4 скрина окна целиком обрезать и отметить нужное.

### Excel и DFL

**reference/dfl-overview.md** (B, по картинкам эталон). Все 11 SVG просмотрены: единый стиль "лист Excel + стрелки + верно/неверно", лучший визуальный набор сайта. Мелочи: `dfl-sections-order.svg` - легенда внизу обрезана справа ("кровл", "отдел", "начало таблиц"); `dfl-options.svg` - персиковый и FFC000 (противоречие 8); `dfl-special-rows.svg` и `dfl-options.svg` пишут единицы `LF`, `SF`, `SQFT`, `Unit`, хотя страница требует `LFT` и `SQ FT`; `dfl-headers.svg` ок, но подпись `:273` "Заголовок правильный, с текстом в B и без цвета" читается как три правильных варианта.
- `:85` переписать D: "у штучного погонажа длина доски в футах (14, 16), у остального единица".
- `:179-187` таблица "шаблон и готовый файл" выглядит как соответствие строк, а это два независимых списка. Сделать два нумерованных списка или схему.
- `:140-144` и `:278-282` одна и та же таблица цветов два раза (третий раз в `ewood-tab.md:361-372`).
- `:273` подпись: "Верно: жирный и фон, B-F пустые. Неверно: текст в B. Неверно: нет цвета".
- `:412` добавить "если insulation в scope" (противоречие 7).

**reference/takeoff-items.md** (B).
- `:97-98` пример: в D должна стоять длина (14), а не `LFT`, иначе формула делит на текст.
- `:99` rim `*1.05` в не-EWP примере (противоречие 9).
- Добавить одну картинку "анатомия строки": одна строка DFL с выносками A..H (можно вырезать из `reference/dfl-layout.svg`).

**reference/standard-notes.md** (A, эталон для текстовых справочников): правило, пары "было / стало" из реальных сданных работ, "факт в строке = без ноты", библиотека готовых формулировок под катом. Улучшить: одна своя картинка "черновик ноты и финальная нота в Excel".

**reference/dfl-blocks.md** (B). Картинки: `framing/deck-frame-plan.svg` - хороший план каркаса с номерами и строками; `photos/hardware/holdown-at-stud-base.jpg` - 336x448, мелкое, но с источником.
- Страница про блоки в Excel, а картинки про каркас. Добавить схему заполненного блока балкона в стиле `dfl-floor-cycle.svg` (заголовок с units, строки, Decking под своим заголовком).
- `:45` против `:111-112`: в примере D = `LFT`, должно быть 14.
- `:109` пример `Posts 6x6 P.T. =2*G pcs 10' S4.1`: колонки не подписаны, 10' это E или D, не ясно. Дать шапку колонок, как в `takeoff-items.md:94`.

**reference/ewood-tab.md** (B). Просмотрено: `tab-1.png`, `tab-2.png` (лента, читается), 4 SVG-шага (`book-path`, `install-steps`, `duplicate-steps`, `check-steps`: текст в рамках, ничего не добавляют к тексту), `dup-before.png`, `ins-decking-cable.png` (Excel-кадры 1325 px, на 760 px шрифт около 8 px, читается только по клику), иконки 64x64 выборочно.
- `:404-417` таблица клавиш - копия `excel-hotkeys.md:23-40`. Оставить один канон, во втором ссылка.
- Термины "формула размера блока", "микрогруппы" (`:276`, `:283`) объяснены только в dfl-overview: дать ссылку.

**reference/excel-hotkeys.md** (B).
- `:6` единственная картинка - `excel-strip.png` 31x424 px, к макросам Excel отношения почти не имеет. Поставить кадр вкладки E-Wood (`reference/ewood-tab/tab-2.png`) или схему "до и после" для `C_JoistsSort`.
- Решить, где канон клавиш Excel: здесь или в `ewood-tab.md#keys`.

**reference/formulas.md** (C).
- В начале страницы дать легенду переменных: G = замер из OurPlanCore, H = шаг, plies или высота, D = длина доски (14, 16), `Stock LF` = длина стока. Сейчас `:51-56` и `:114-125` используют их без определения (старый пункт `AUDIT.md` про G/D закрыт только на `blockingoc`, не здесь).
- `:80` truss bracing `=CEILING(G/4/D,1)`: что такое `/4` при "ряд каждые 10'", не объяснено. Расписать на примере.
- `:18` "минус plates" (противоречие 1); `:73` D = 14/16 при `LFT` в колонке D (противоречие 2).
- Добавить 2 схемы: "стойки на 16 o.c. = 1 на фут + 10%" (почему не 0.75) и "blocking flat / diagonal / vertical" с фактором кусков.

### Справочник

**reference/boss-feedback-rules.md** (B). Картинки: `confluence-062.png` - сырой скрин с веб-страницы (обрывок "See also: partition, stud", жёлтая точка), но по делу; `confluence-061.png` - деталь ribbon, обрезан текст справа, водяной знак; `confluence-028.png` - деталь holdown с красными стрелками, хорошо.
- `:9` правило и пример спорят (противоречие 1).
- `:19` заменить скрин staggered wall на свою схему или кроп без обрывков веб-страницы.

**reference/hangers.md** (C).
- `:89` убрать пример `SUL28` на 30 градусов: SUL/SUR только 45 (противоречие 4); другой угол по тренингу `HU... SK<угол> L/R`.
- `:170-257` быстрых таблиц шесть, а для пилёного 2x (самый частый случай, `hardware-catalog.md:22`) таблицы нет: добавить `2x6 LUS26`, `2x8 LUS28`, `2x10 LUS210`, `2x12 LUS212`, двойные `-2`, `HU` для тяжёлых.
- `:15` схема `hangers/hanger-selection-flow.svg`: ветка "Concealed / firewall?" ведёт в "SUL / SUR, HUC" - skew не про concealed; нет ветки "пилёный 2x - LUS". Перерисовать: что несём (2x / I-joist / beam), потом mount, потом skew, потом firewall.
- `:121-153` картинки: `confluence-080/081/082` - 3D-рендеры без подписей полки и опоры; `confluence-030.png` - скрин из поиска картинок со значком Google Lens в углу; `confluence-030/031` - картинки каталога Simpson без указания источника, хотя правило сайта (урок kb-program-guide-style) требует ссылку на оригинал.

**reference/hardware-catalog.md** (B). Фото с источниками; `photos/hardware/truss-strap-tie-top-plate.jpg` (резкость низкая) показывает металлические пластины ферм, tie у плиты не виден, а подпись про ties.
- `:12` разделить: `Z` в конце модели у Simpson (`DTT2Z`, `ML210Z`) и наша запись `Zmax` отдельным словом для hangers и баз (противоречие 5).
- `:93` заменить фото на крупный план H2.5A у top plate.

**reference/material-catalog.md** (B).
- Ни одной картинки. Добавить одну схему "семейства EWP в разрезе" (LVL, PSL, LSL, I-joist, rim board) и одну "листы: Ply, OSB, Zip, DensGlass" - новичок их путает на чертеже.
- `:48` против `dfl-overview.md:412` (противоречие 7).

**reference/industry-standards.md** (B). Добавить схему анатомии стены и проёма (plates, studs, king, jack, cripple, header, sill): термины `:25-26` есть, картинки нет.

**reference/quantity-benchmarks.md** (B). Указать дату и число работ в выборке; `:20` "Bracing стен 1 на 8 ft" согласовать с противоречием 6.

**reference/ai-assist-system.md** (B). Коммит 16.11 пометил терминалы и AI Crop Notes "только полная версия"; осталось сверить Agent Bridge в `:12` с Lite.

**start/site-preview.md** (C, страница редактора). Описывает старый шаблон и PlanSwift (`:50-58`, противоречие 11). Либо переписать под действующий шаблон из `how-to-use.md:32-44`, либо убрать из меню работника (решает владелец, `AGENTS.md` раздел 14).

## Противоречия

Каждое противоречие проверено чтением обеих строк (свои - мной, остальные - помощниками; самые тяжёлые я перепроверил сам). Пункты 1-9 и 13-25 требуют одного слова владельца, остальное можно поправить без решения.

### Правила, числа и единицы

1. **Высота стойки: с plates или без.** `work/vertical/walls/exterior.md:49`: "Высота в имени - высота стены с plates", пример 9'-6" минус TJI 11 7/8" минус 3/4" = 8.45' (plates не вычитаются), таблица precut `:63` тоже от высоты с plates. Против: `reference/boss-feedback-rules.md:9`, `reference/formulas.md:18`, `start/common-mistakes.md:13`, `start/quality-checklist.md:20` - "минус plates". Пример в той же строке `boss-feedback-rules.md:9` (`11'1" wall - 22" truss - 3/4" subfloor = 9'2" stud`) plates не вычитает. Решить, что идёт в имя стены и в E строки студов, и поправить 4 страницы.
2. **Что лежит в колонке D.** `reference/dfl-overview.md:85`, `reference/takeoff-items.md:12`: D - единица (`LFT`, `SQ FT`, `4x8`, `pcs`). `start/workflow.md:112-113`, `start/quality-checklist.md:78`, `start/common-mistakes.md:86`: "SF для листов". `reference/formulas.md:72`: для листов `4x8`; `:73`: `=CEILING(G/D,1)` "(D = 14 или 16)", а в колонке D той же строки `LFT`. `reference/dfl-blocks.md:45`: "длинная доска в D (14')", а пример `:111-112` пишет в D `LFT`. `reference/takeoff-items.md:97-98`: `=3*CEILING(G140/D140,1)` с `LFT` в D (формула делит на текст). Так же `work/sqfts/loft.md:60`, `porch.md:66`, `sqfts/deck.svg` пишут joists в `LFT`, а `joist.md:41-47` - число и длину. Схема `dfl-floor-cycle.svg` и кадр `reference/ewood-tab/dup-before.png` показывают в D числа 16, 14, 8, 4. По книге: у штучного погонажа в D длина доски в футах, у остального единица. Написать это в `dfl-overview.md:85` и поправить примеры.
3. **Чей лист главнее для обшивки.** `start/quality-checklist.md:40`: "Наружная обшивка по Arch и energy notes, внутренняя по Structural". `start/workflow.md:40-41` "structural главнее", `reference/standard-notes.md:86` "Структурный лист главнее", `reference/boss-feedback-rules.md:38` "Структурный лист главнее по толщине; Zip по арх превалирует". Схема `walls/exterior-wall-section.svg`: "Источник: Arch / Energy / Wall-type notes".
4. **Skewed hangers SUL/SUR.** `reference/hangers.md:50`: "SUL / SUR (45 градусов), другой угол LSSR". `reference/hangers.md:89`: пример `SUL28 Zmax` с углом "skewed 30°". SUL/SUR у Simpson только 45 градусов (старый пункт 2 `OFFICE_FOLDER_COVERAGE.md`).
5. **Как писать Zmax.** `reference/hangers.md:87`: `Zmax` отдельным словом, `ABU66Z`, `LSSR28Z`, `LUS210Z` - "не так". Но `reference/dfl-blocks.md:40` и `reference/hardware-catalog.md:51` дают `ABA66Z`; `hardware-catalog.md:12` "`Zmax`, `Z`" одной строкой; кровельные страницы `ridge.md:43` `LSSR2.1Z`, `header.md:60` `LSSR210Z`, `dbl-trpl-rafters.md:40`, `:57` `LSSR2.56Z`, `LRU212Z`. По тренингу 7.4.24 в кровле hangers вообще без Z и Zmax, кроме `LRUZ` (старый пункт 3 `OFFICE_FOLDER_COVERAGE.md` открыт).
6. **Bracing стен: LFT или штуки, и чем он отличается от опоры гипса.** LFT: `walls/corridor.md:49`, `demising.md:51`, `basement.md:48`, `unit.md:56`, `sheathing/exterior-materials.md:74`, `:105`, `reference/formulas.md:43`. Штуки длиной по высоте стены: `details/bracingdrywall.md:28` ("одна доска на каждые 8 LFT"), `walls/gable.md:68` (`pcs`, `BTM / 8 x 1.1`), `dfl-floor-cycle.svg` (`Bracing Ext Walls 2x4 76 14`), `quantity-benchmarks.md:20`. Строка `Bracing for Drywall` (`corridor.md:51`, `demising.md:52`) в DFL не существует, опора гипса - `Blocking for Drywall` в Floor Framing List (`bracingdrywall.md:45`). Длины по высоте `bracingdrywall.md:38-43` расходятся с чек-листом Ural 2026 (14' до 9', 16' до 11', 18' до 14', 20' выше).
7. **Утеплитель между стойками.** `reference/material-catalog.md:48`, `boss-feedback-rules.md:16`, `sheathing/exterior-materials.md:89`: не считаем, это ошибка. `reference/dfl-overview.md:412` даёт как "верно" `Batt Insulation R-21`, `takeoff-items.md:79` держит подпись `Insulation at 6" Ext. Walls`, `dfl-special-rows.svg` показывает `Batt R-21 900 SQFT`. Дописать "если insulation в scope".
8. **Цвет опции на картинке против текста.** `reference/dfl-overview.md:455`: "для опций персиковые оттенки не берите"; `:377`: оранжевый `FABF8F`. `reference/dfl-options.svg` красит опцию "Option Panel" в персиковый `FCE5D7`, а "оранжевый" рисует как `FFC000`.
9. **Rim 1.05 в обычных примерах.** `reference/formulas.md:41-42`: `1.05` только EWP-jobs. Примеры без пометки EWP: `reference/takeoff-items.md:99` (обычный job с фермами), `details/rim.md:67-68`, `floor-framing/joist.md:47`.
10. **Карта сайта.** `start/how-to-use.md:14-19`: вкладок четыре, формулы, ноты и подписи DFL "в Справочнике". В `mkdocs.yml` вкладок семь, эти страницы в "Excel и DFL", OurPDF не упомянут. То же `start/workflow.md:5`.
11. **Шаблон предметной страницы.** `start/how-to-use.md:32-44` - действующий шаблон. `start/site-preview.md:50-58` - старый (Что считать, Правила, Где смотреть, Визуальная проверка, Проверить) и PlanSwift.
12. **Beam: Count или Line.** `reference/ourplancore-tools.md:24` и `floor-framing/beam.md:5`: Beam создаёт Count-позицию с длиной в имени (`FB1 8`). Кадр `ourplancore/v3/measure-beam.png` (на 7 страницах), легенды `window-map.png` и `window.png`: `RB1 16`, `FB1 48` как Line с `total 50,22 ft`.
13. **Draft Stop: SQ FT или 4x8, OSB или Ply.** `walls/gable.md:73`: `1/2" OSB`, SQ FT. `sheathing/gable.md:49`: `1/2" Ply` или `5/8" Type X`, `4x8`; `sheathing/shear-wall.md:52`: `4x8`. По канону DFL с 24.10.2026 SQ FT.
14. **Hip и valley: чем мерить.** `roof-framing/hip.md:25`, `:52` и `valley.md:28`: Beam, `framing/roof framing/beams/hip ...`. `sheathing-and-misc/ridgevalleyhip.md:33-34`: Line в `framing/roof framing/details/<сечение> hip`; там же `:48` `Hip plates` против `hip.md:56` `Hip Rafters`.
15. **Dbl Rafters и смысл `(n)`.** `dbl-trpl-rafters.md:38` "точки x 2" (пример `:55`: 4 на skylight) против `dormer.md:52` и `header.md:58` "точки" (2 на тот же skylight). `beam.md:59-63`: `Beam (3)` с C = точки; `post.md:55`: `Posts (3)` "точки x 3"; `takeoff-items.md:97`: `=3*CEILING(...)`. Нужно одно правило, что значит `(n)` в подписи.
16. **Decking: какой запас.** `deck/deck-porch-balcony-frame.md:87`, `exterior-trims/rails-decking.md:61`, `exterior-trims/balcony-buildup.md:45`: `=W*D*G` без запаса. `reference/dfl-blocks.md:117`: `=CEILING(12*7*1.1,10)*G`. `sqfts/deck.md:39`, `sqfts/balcony.md:40`: `SQFT x 1.1` (x units). В старых файлах Office `CEILING(SQFT x 1.05, 10)`. Сейчас три варианта.
17. **Два слоя наружного гипса на потолке.** `sqfts/porch.md:41`: `SQFT x 2 x 1.1`. `roof-framing/canopy.md:62`, `:90`: SQ FT x слои без 1.1 (96 x 2 = 192). `deck/deck-porch-balcony-frame.md:90`: `=CEILING(G*2*1.1,10)*G` - G умножен дважды.
18. **Bracing for Trusses.** `details/blocking.md:44` "1 ряд на каждые 10' по площади", `:72` `=ОКРВВЕРХ(G*1.1/D;1)`; `reference/formulas.md:80` `=CEILING(G/4/D,1)` + исключения (локальная правка, на blocking.md их нет); `roof-framing/roof-sheathing.md:58` unit `LFT`. Внутри `formulas.md:80` "каждые 10'" и `G/4` не сходятся.
19. **Panel adhesive.** `floor-framing/subfloor.md:38` "по норме шаблона", пример `:58` 84 тубы на 84 листа. `reference/formulas.md:81`, `material-catalog.md:59`: `=C<subfloor>/3`.
20. **Blocking, ribbon, cross bridging: LFT или доски.** `details/blocking.md:38`, `:42-45` и `ribbon.md:40`: доски по 16' через `/D`. `reference/formulas.md:45`, `takeoff-items.md:19`: "остаются в LFT, не делить на 16' без нужды". Cross bridging TB27: `blocking.md:53` pcs, `takeoff-items.md:63` в группе LFT.
21. **Анкеры sill plate.** Шаг: `walls/sill-plates.md:67` и SVG `Anchor Bolts 48" o.c.` против дефолта 36" (`deck/anchor-bolts.md:31-32`, `standard-notes.md:156`). Размер: `framing/anchor-bolt.svg` "Дефолт 5/8" Titen HD" против 1/2" (`anchor-bolts.md:31`, `:47`). Запас: `anchor-bolts.md:47` и `formulas.md:76` с 1.1, `anchor-bolts.md:58`, `:84` без. Шайбы: `anchor-bolts.md:48`, `:60`, `:86` "3x3" против `boss-feedback-rules.md:86` "по таблице, не универсальные 3x3".
22. **Jambs межкомнатных дверей.** `interior-trims/casing.md:36`, `:56` и SVG: `=casing/2` в LFT. `boss-feedback-rules.md:123`, `openings/windows-doors.md:62-63`: точками по юнитам, сечение по соседней стене.
23. **Vinyl soffit: LFT или SQ FT.** `exterior-trims/soffit-fascia.md:45` "доска LFT, panel SQ FT", пример `:81` 12" vinyl SQ FT, `:84` 9" vinyl LFT. `sheathing-and-misc/eve.md:56`: vinyl soffit в SQ FT. Порога ширины нет (вопрос `AUDIT.md` Q5).
24. **Rail sections.** `deck/railing.md:51`, `dfl-blocks.md:60`: фронт и бока отдельными строками, unit. `dfl-blocks.md:119`: одна строка `=EVEN(19/6*G)` pcs. Правила "сколько секций на сторону" нет нигде.
25. **Zip Tape.** `siding/underlayment.md:44`: в "rolls". `sheathing/wall-sheathing.md:65`, `box-sheathing.md:44`, `walls/gable.md:72`: LFT, `SQFT x 0.4 x 1.1`, без периметра проёмов (старый пункт 7 `OFFICE_FOLDER_COVERAGE.md` открыт).
26. **Подписи строк отделки против словаря.** `exterior-trims/overview.md:123`, `:125`, `soffit-fascia.md:47-48` пишут `Ext. Casing sides`, `CornerBoards`, `Crowns`, `Frieze`, `Trim over fascia`; канон `reference/takeoff-items.md:79`: `Ext Casing`, `Corner Boards`, `Crown`, `Frieze Board`, `Over Fascia Trim`. Макросы суммируют строки по тексту подписи.
27. **Двойная demising.** `walls/demising.md:5` и `demising-double-wall.svg`: "каждый каркас своя линия". `demising.md:36`: "одинаковые каркасы - одна линия `dem (2) 2x6 9.09`".
28. **Door Flashing.** `openings/window-flashing.md:43`: отдельная строка `Door Flashing`. Своя SVG страницы и канон DFL кладут двери в `Window Flashing`.
29. **Что такое floor.md.** `floor-framing/subfloor.md:10`: "вертикальная полоса обшивки на уровне перекрытия - страница Floor-height Sheathing". `sheathing/floor.md:14-15`: "полоса на высоте перекрытия - это Box Sheathing, не эта страница".
30. **Returns.** `sheathing-and-misc/returns.md:41`, `:50`: `eves rakes/rakes/returns 12`, LFT. `soffit-fascia.md:51`: `eves rakes/eves/returns 12`; `roof/returns.svg`: "LFT или pcs", pork chop pcs.
31. **Shaft: от длины или площади.** `walls/shaft.md:47-48`, `:55-56` и `reference/formulas.md:116-123`: панели `LFT x 1.1 / 24`. 24 - площадь панели 2'x12', значит G должен быть площадью; по канону DFL G = длина x высота. Недосчёт в высоту стены раз.
32. **WRB при Zip.** `siding/eifs-stucco-veneer.md:96-97` считает WRB вместе с Zip; `siding/underlayment.md:44`, `:95` это запрещают.
33. **OurPDF: Beam и Openings.** `ourpdf/measure.md:79`, `:210` описывает их в блоке "Замер", на `ourpdf/window.md:89` и кадрах `block-measure.png`, `top-panel.png` их нет (сняты до 0.9.30).
34. **OurPDF: куда пишет Ctrl+S.** `ourpdf/pages-edit.md:15`, `comments-save.md:234`: в исходный файл. Подсказка на `ourpdf/pages-tab.png`: "сохраняет новый файл".

### Арифметика в примерах

Пример, который не сходится, хуже, чем отсутствие примера: новичок сверяет по нему свою книгу.
- `exterior-trims/casing-corner-band.md:77`: `=2*5.5*34` даёт 374, написано 380; та же ошибка `exterior-trims/macros.md:29`.
- `exterior-trims/furring-and-jambs.md:69`: `(2*5.5+3.3)*42` = 600.6, написано 612.
- `roof-framing/overframes.md:66`: 410 SF при 4:12 даёт 410 x 1.054 / 32 x 1.1 = 14.9, то есть 15 листов, написано 14.
- `floor-framing/stair.md:85`: `Hangers LSC =8*G` при `Stringers (4) =4*G` и правиле "один LSC на stringer" (`:53`).
- `exterior-trims/balcony-buildup.md:78`: post wrap на 6 постов, в том же блоке `deck-porch-balcony-frame.md:130` их 12.
- `details/blockingoc.md:56`: куски делятся на длину доски в футах (размерность).
- `interior-trims/door-window-trim.md:41`: `9068` это 9'-0" x 6'-8", не 8'-0".
- `deck/railing.md:76`: `16 unit` секций для боков 2x8' при G=6 из правила не выводится.

## Проблемы картинок

Пути от `docs/assets/images/`. Порядок - по вреду.

### 1. Картинка противоречит правилу (перерисовать)

| Картинка | Страницы | Что не так |
| --- | --- | --- |
| `framing/anchor-bolt.svg` | `deck/anchor-bolts.md`, `details/bolts.md` (главная) | "Дефолт 5/8" Titen HD" против 1/2" в тексте; у Titen HD нарисованы шайба и гайка; на bolts.md это анкер к бетону, который страница исключает |
| `trims/exclusions.svg` | `exterior-trims/exclusions.md` | "J-channel часто идёт с EIFS", J-channel в зелёном "проверяем" - обратное правилу `:39`, `:57` |
| `trims/balcony-buildup.svg` | `exterior-trims/balcony-buildup.md` | EPDM поверх sleepers, decking прямо на мембране; "Decking часто by others" против `:45` |
| `roof/ridge-valley-hip.svg` | `sheathing-and-misc/ridgevalleyhip.md` | hips не сходятся с коньком, valley не по стыку скатов (верная геометрия есть в `roof/hip-valley-length.svg`) |
| `framing/deck-frame-plan.svg`, `sqfts/deck.svg` | `deck-porch-balcony-frame.md`, `reference/dfl-blocks.md`, `sqfts/deck.md` | `LUS28` под joists 2x10 P.T., без Zmax; ledger на `Titen HD` (анкер в бетон) вместо screws |
| `siding/eifs-stucco-veneer.svg` | `siding/eifs-stucco-veneer.md` | "J-channel наш" без условия "только при vinyl" |
| `siding/measure.svg` | `siding/measure.md` | вычитает мелкие окна (правило 4'), пишет "Waste 1.1", которого нет в тексте |
| `framing/drywall-bracing.svg` | `details/bracingdrywall.md` | длина kicker "по высоте стены"; подписи LFT против pcs |
| `framing/blocking-oc.svg`, `framing/blocking.svg` | `blockingoc.md`, `blocking.md` | joist подписан "Blocking rows"; "LFT (без factor)" против x 1.1 |
| `framing/post-height.svg` | `floor-framing/post.md` | непрерывный пост через 3 этажа подписан `6x6 8.2` |
| `reference/dfl-options.svg` | `reference/dfl-overview.md` | опция в персиковом `FCE5D7`, который текст запрещает; "оранжевый" как `FFC000`, а не `FABF8F` |
| `hangers/hanger-selection-flow.svg` | `reference/hangers.md` | SUL/SUR под вопросом "concealed / firewall"; нет ветки пилёного 2x (LUS) |
| `walls/exterior-wall-section.svg`, `framing/furring.svg` | `walls/exterior.md`, `walls/furring.md` | "WRB / Tyvek", хотя страницы запрещают Tyvek по умолчанию; стрелки мимо деталей |
| `walls/demising-double-wall.svg` | `walls/demising.md` | "Line на каждый" против `:36` "одна линия `dem (2)`" |
| `walls/basement-wall-section.svg` | `walls/basement.md` | нет top plates, обшивки и WRB, похоже на furring wall |
| `roof/rake.svg` | `sheathing-and-misc/rake.md` | eave нарисован по низу стен, свеса нет |
| `sqfts/roof-sqft.svg` | `sqfts/roof.md` | "membrane: by others" против строки EPDM |

### 2. Подпись не про эту картинку

| Картинка | Страницы | Что не так |
| --- | --- | --- |
| `ourplancore/v3/measure-count.png` | `post.md:37`, `deck-porch-balcony-frame.md:58`, `ourplancore-tools.md:96` | Count дверей `3.0x6.8 d`, подписи про посты и балконы |
| `ourplancore/v3/measure-beam.png` | `beam.md` (главная), `ridge`, `header`, `hip`, `valley`, `dbl-trpl-rafters`, `ourplancore-tools.md` | балка перекрытия на плане квартиры, `RB1 16` при `Line total 50,22 ft`; подпись beam.md обещает Count `FB1 8` |
| `ourplancore/v3/sheet-unit.png` | `walls/unit.md` (главная) | пустой лист, "Scale: not set", линий из подписи нет |
| `ourplancore/v3/measure-openings.png` | `openings/windows-doors.md` | подпись "фасад, рамка, 3.0x5.0", на кадре план, 3.0x4.0, рамки нет |
| `ourplancore/v3/pages-panel.png` | `start/workflow.md:50` | подпись про `00. imported/Arch`, на кадре листы демо-гайда |
| `ourplancore/v3/takeoffs-root.png` | `start/takeoff-structure.md:27` | подпись про переключение корпусов, на кадре один корпус |
| `confluence/confluence-057.png` | `work-types/com.md:117` | подпись про чердачный draft stop, на детали перекрытие UL L546 |
| `confluence/confluence-083.png` | `walls/gable.md:6` | обычная W-ферма, а подпись про gable truss со стойками |
| `confluence/confluence-139.png`, `confluence-141.png` | `header.md:64`, `dbl-trpl-rafters.md:61` | подпись "ближе" у общего вида; крупный план - 138 и 140 |
| `photos/hardware/truss-strap-tie-top-plate.jpg` | `reference/hardware-catalog.md:93` | видны пластины ферм, tie у top plate не виден; фото мягкое |
| `photos/work-types/ijoists-on-beam-post.jpg` | `work-types/ewp-capital.md:14` | подпись про "стойку 2x", на фото engineered колонна и open web joists |
| `confluence/confluence-155.png` | `walls/sill-plates.md:17` | очень мягкая (самая низкая резкость на сайте), сюжет спорит с `:11-13` |
| `photos/siding/furring-strips-over-sheathing-corner.jpg` | `siding/underlayment.md:4` | rigid foam назван "обшивкой с WRB" |
| `photos/framing/joist-cross-bridging.jpg` | `details/blocking.md:10` | подпись "LFT как blocking" против TB27 в pcs на той же странице |
| `trims/room-schedule.svg` | `interior-trims/room-schedule.md` | макет с колонками Room/Base/Crown, подпись обещает Floor/Base/Walls/Ceiling/Remarks; реального schedule нет |
| `trims/int-trims-02.png` | `interior-trims/overview.md`, `start/site-preview.md` | старый скрин с "кок 98.64 фт", исключений из подписи нет |

### 3. Не читается на 760 px

| Картинка | Страницы | Что сделать |
| --- | --- | --- |
| `ourplancore/v3/sheet-dots.png` | `start/takeoff-structure.md`, `ourplancore-pages.md`, `ourplancore-routing.md`, `takeoff-naming.md` | сетка точек 8 px, правая половина чёрная: кроп сетки крупно с подписями W/F/S/U |
| `ourplancore/v3/excel-strip.png` (31x424 px) | `start/workflow.md`, `reference/excel-hotkeys.md`, `ourplancore-excel.md` | заменить подписанной схемой кнопок XL (SF, WL, GB, TH, PP, E/R, OP, SH, SW, SHF, UN, BL, FR) |
| `ourplancore/v3/start-screen.png`, `export-pdf.png` | `ourplancore-start.md`, `job-creation-storage.md`, `workflow.md`, `ourplancore-pdf.md` | кроп на карточку старта и на галки Measurements, Markups, Legend |
| `trims/ext-flare-detail.png` | `exterior-trims/porch-deck-balcony.md` | битый шрифт CAD, не читается и в полном размере |
| `sheathing/ext-gypsum-wd-stud-2layer.png` | `sheathing/exterior-materials.md` | в `kb-split` около 370 px: дать на полную ширину |
| `ourpdf/top-panel.png`, `info-line.png`, `excel-selection.png` | `ourpdf/window.md`, `ourpdf/measure.md` | порезать полосы на куски |
| `walls/metal-deflection-head.png` (2828x3922, 556 KB) | `walls/metal-tracks.md` | портрет на 1050 px высоты, текст обрезан: кроп узла |
| `ourplanecore/sheets-to-tree.svg`, `routing-layers.svg` | `ourplancore-split-by-sheets.md`, `ourplancore-routing.md` | текст 7-8 px на 760 px |
| Excel-кадры `reference/ewood-tab/ins-*.png`, `dup-*.png` (1325 px) | `reference/ewood-tab.md` | читаются только по клику; кроп A:F |

### 4. Сырые веб-скрины, водяные знаки, нет источника

- `confluence/confluence-030.png` (`hangers.md:145`): скрин из поиска картинок со значком Google Lens; `confluence-030`, `-031` - картинки каталога Simpson без ссылки на источник, хотя правило сайта (урок kb-program-guide-style) требует ссылку на оригинал.
- `confluence/confluence-062.png` (`boss-feedback-rules.md`, `com.md`, `corridor.md`): обрывок веб-словаря "See also: partition, stud", жёлтая точка.
- `confluence/confluence-093.jpg` (`wall-sheathing.md`): скриншот Instagram с кнопками карусели.
- `confluence/confluence-061.png` (`ribbon.md`, `boss-feedback-rules.md`): бледный логотип производителя ферм.
- Без источника: `confluence/confluence-151.png` (`railing.md`), `trims/ext-pork-chop.png`, `trims/ext-eave-return.png` (`returns.md`, `soffit-fascia.md`).
- Любительские или тёмные фото без стрелок: `photos/roof/rm-roof-sheathing-plywood.jpg` (палец в кадре), `photos/sheathing/raised-heel-truss-at-wall.jpg` (синяя полоса интерфейса), `photos/sheathing/sh-shear-wall-interior-osb.jpg`, ч/б HABS/HAER на valley, dormer, header.

### 5. Единицы и подписи на схеме не как в таблице своей страницы

`sheathing/box-sheathing.svg`, `sheathing/truss-heel.svg` (SQ FT против 4x8); `trims/railing-system-vs-elements.svg` (Balustrades LFT против pcs); `trims/porch-trims.svg` (Column wrap pcs против LFT); `roof/returns.svg` (pcs против LFT); `roof/canopy-parts.svg` (Subfloor SQ FT, Beam LFT против `Roof Sheathing at Canopy` 4x8 и `Beams (3)`); `framing/ribbon-board.svg` (1x6 LFT против 2x4 и `/D`); `walls/parapet-section.svg` (подписи не из словаря DFL); `reference/dfl-special-rows.svg`, `dfl-options.svg` (`LF`, `SF`, `SQFT`, `Unit` на странице, которая требует `LFT` и `SQ FT`); `openings/header.svg` ("число плёнок" вместо plies).

### 6. Мелкие дефекты вёрстки в SVG

`process/work-process.svg` (стрелка 2-3 идёт через текст шага 3), `framing/scan-order.svg` (вторая полоса справа налево при подписи "слева направо"), `reference/dfl-sections-order.svg` (легенда обрезана справа), `roof/hip-valley-length.svg` (строка примера за viewBox, ASCII `->`), `sqfts/deck.svg` (ASCII `->`), `sqfts/cantilevered.svg` (висящий "cantilever -"), `roof/flashing.svg`, `sheathing/box-sheathing.svg`, `roof/eave-parts-takeoff.svg` (выноски пересекаются или смотрят на подписи), `trims/int-casing.svg` ("Stool" наезжает на дверь), `sheathing/gable-sheathing.svg` (выноска через скат). `tools/check_symbols.py` ловит длинные тире и стрелки-символы, но не ASCII `->`.

### 7. Картинки-текст и пустые схемы

4 SVG-шага на `reference/ewood-tab.md` (`book-path`, `install-steps`, `duplicate-steps`, `check-steps`) - текст в рамках, ничего не добавляют и не ищутся поиском; `work-types/residential.svg` (контур дома, подписи в пустоту), `work-types/reconstruction.svg` (только легенда), `trims/rails-decking.svg` (примитив; на том же сайте есть хорошая `railing-system-vs-elements.svg`).

### 8. Тяжелее 500 KB (правило `AGENTS.md` раздел 7)

`confluence-174.png` 765 KB и `confluence-172.png` 736 KB (`sheathing/floor.md`), `confluence-154.png` 736 KB (`subfloor.md`), `confluence-152.png` 648 KB (`balcony-trims.md`), `walls/metal-deflection-head.png` 556 KB; фото в PNG (`confluence-083`, `-131`, `-156`, `-160`, `-170`) стоит перевести в JPG.

### 9. Где картинки нет, а нужна

`sheathing/wall-sheathing.md` (схема площади фасада с вычетами), `exterior-trims/overview.md` (фасад с группами отделки), `reference/material-catalog.md` (семейства EWP и листы), `reference/industry-standards.md` (анатомия стены и проёма), `start/common-mistakes.md` (пары "так / не так"), `reference/formulas.md` (стойки на 16" и куски blocking), `reference/takeoff-items.md` (анатомия строки A:H), `reference/dfl-blocks.md` (заполненный блок балкона в Excel), `interior-trims/room-schedule.md` (реальный schedule), `exterior-trims/shower-pergola.md` (pergola), `exterior-trims/macros.md` (C_TrimsCalc до и после), `roof-framing/valley.md`, `dbl-trpl-rafters.md`, `ourpdf/pages-edit.md`, `ourpdf/comments-save.md`, `ourplancore-extras-other.md`.

### 10. Неиспользуемые файлы

181 картинка (22 МБ) лежит в `assets/images`, но ни одна страница на неё не ссылается: 116 в `confluence/`, 25 в `trims/`, 15 в `ourplanecore/`, 13 в `ourplancore/v3/`. Удалять без владельца нельзя, но это готовый запас: прежде чем рисовать новую схему для страницы из пункта 9, стоит посмотреть неиспользуемые чертёжные кропы `confluence/`.

## OurPlanCore (оценка текущего текста, он будет переписан под Lite)

**Важно про время.** Пока шёл аудит, в `main` влили переписку под Lite (коммиты `ddd3cc2`, `3b21683`, `de5f088`, 16.11 17:13-17:20): изменены 21 страница OurPlanCore, `start/workflow.md`, `reference/excel-hotkeys.md`, `reference/ai-assist-system.md`, `start/maintenance.md`, появилась новая страница `reference/ourplancore-lite.md` (теперь на сайте 161 страница). Оценки OurPlanCore ниже - по тексту до этих коммитов, новую страницу я не оценивал; часть замечаний (пункты 2, 4 и 6 списка "Что учесть") эти коммиты могли уже закрыть. Страницы вне OurPlanCore я перепроверил после коммитов: изменения там касаются только полосы XL и Lite, находки отчёта остаются в силе (номера строк workflow.md поправлены).

Оценена 31 страница раздела по тексту и выборке картинок (просмотрено 29 картинок, схем и постеров роликов из 235 ссылок раздела; все 11 SVG-схем `assets/images/ourplanecore/` просмотрены, они в целом хорошие, но `sheets-to-tree.svg` и `routing-layers.svg` слишком мелкие для 760 px). Тексты этих страниц сейчас переписывают под Lite, поэтому ниже то, что стоит учесть при переписке, а не список правок к текущему тексту.

### Общая картина

- Сильная сторона: страницы "Каждый день" написаны как рецепты (зачем, что нужно, шаги, результат), почти у каждой ролик 10-20 секунд и скриншот. Курс из 10 уроков (`reference/ourplancore-course.md`) - лучший вход в программу на сайте: цель, шаги, "проверь себя", ссылки.
- Слабая сторона: слои "Продвинутое" и "Дополнительно" написаны для разработчика, а не для эстиматора: пути `AI_Context/...`, `%LOCALAPPDATA%`, `agent_bridge.py undo`, номера сборок 2.2.34-2.2.42, DeepSeek, Agent Bridge (`ourplancore-troubleshooting.md`, `ourplancore-settings.md:23`, `ourplancore-ai-console.md`, `ourplancore-workspace.md`, `ourplancore-sheets-advanced.md`).
- Одна тема живёт в 4-5 местах: точки листа и маршрут описаны в `start/takeoff-structure.md:85-101`, `reference/takeoff-naming.md`, `reference/ourplancore-routing.md`, `reference/ourplancore-split-by-sheets.md`, `reference/ourplancore-pages.md` (раздел dots); правка замеров в `ourplancore-editing.md` и `ourplancore-edit-takeoffs.md` (9 общих роликов); AI Inbox и в `ourplancore-ai.md`, и в `ourplancore-managers.md`. Для Lite стоит оставить одну страницу на тему.
- Скриншоты сняты на 3.0.0-3.0.2 (в заголовке окна `window-map.png` видно 3.0.0), а `ourplancore-changelog.md` уже на 3.0.30. При переписке под Lite все кадры `ourplancore/v3/` и ролики `demo/` придётся снять заново.

### Таблица

| Страница (путь от docs) | Ясность | Полнота | Визуал | Согласованность | Итог | Главная проблема |
| --- | --- | --- | --- | --- | --- | --- |
| reference/ourplanecore.md | A | A | A | B | A | блок "что появилось за два месяца (15.08-17.10)" устарел |
| reference/ourplancore-course.md | A | A | A | A | A | эталон для программных страниц |
| reference/ourplancore-start.md | B | A | B | B | B | start-screen.png 1920 px почти пустой, карточка в центре нечитаема на 760 px |
| reference/job-creation-storage.md | A | A | B | A | B | тот же start-screen.png; settings-project-storage.png показывает пустой отчёт |
| reference/ourplancore-pages.md | A | A | C | A | B | sheet-dots.png: сетка точек мелкая, правая половина кадра чёрная |
| reference/ourplancore-split-by-sheets.md | B | A | B | B | B | повтор темы маршрута с takeoff-naming и routing |
| reference/ourplancore-tools.md | A | A | B | C | B | таблица: Beam создаёт Count, а measure-beam.png показывает `Line \| total 50,22 ft`; measure-count.png про Count показывает двери |
| reference/ourplancore-takeoffs.md | A | A | B | A | A | estimating.png 278x783 узкая полоса, но читается |
| reference/ourplancore-buildings.md | A | A | B | A | A | buildings-tree.png 307x260 мелкий |
| reference/takeoff-naming.md | A | A | C | B | B | та же sheet-dots.png; тема повторена на 4 страницах |
| reference/ourplancore-excel.md | B | A | C | B | B | excel-strip.png 31x424 px вместо подписанной схемы кнопок XL |
| reference/ourplancore-pdf.md | A | A | B | A | A | export-pdf.png: текст диалога 6-7 px на 760 px |
| reference/ourplancore-editing.md | B | A | B | C | B | 394 строки, дублирует edit-takeoffs (9 тех же роликов) |
| reference/ourplancore-edit-takeoffs.md | A | A | A | C | B | дублирует editing |
| reference/ourplancore-routing.md | B | A | B | C | B | четвёртое описание маршрута |
| reference/ourplancore-sheets-advanced.md | B | A | B | B | B | ссылки на сборки 2.2.34-2.2.42 |
| reference/ourplancore-settings.md | C | A | B | B | C | справочник настроек для админа: пути `AI_Context/settings`, `%LOCALAPPDATA%`, движки `Ideal v3` |
| reference/ourplancore-ai-console.md | C | A | B | B | C | для разработчика: Claude/Codex/DeepSeek, Agent Bridge; settings-terminals.png показывает пути `C:\Users\User\Desktop\...lnk` |
| reference/ourplancore-ai.md | B | B | B | C | B | AI Inbox описан и здесь, и в managers |
| reference/ourplancore-workspace.md | C | B | C | B | C | CLI конвейера и модули: не задача эстиматора; одна картинка из settings |
| reference/ourplancore-3d-roof.md | B | A | A | B | B | хорошие ролики; функция редкая для работника |
| reference/ourplancore-extras.md | B | B | B | B | B | нормально как оглавление редкого |
| reference/ourplancore-snap-trace.md | B | A | B | B | B | ок для продвинутых |
| reference/ourplancore-managers.md | B | B | B | C | B | дубль AI Inbox и Job Tracker |
| reference/ourplancore-3d.md | B | B | B | B | B | статус "что выключено" полезен, но функция не для работника |
| reference/ourplancore-extras-other.md | B | B | D | B | C | ни одной картинки на 6 функций |
| reference/ourplancore-ideas.md | B | - | - | B | B | планы разработки, работнику не нужны в меню |
| reference/ourplancore-shortcuts.md | A | A | A | A | A | единый канон клавиш, F1 и редактор показаны |
| reference/ourplancore-troubleshooting.md | B | A | - | B | B | половина строк про сборки 2.2.x, `agent_bridge.py`, `AI_Context` |
| reference/ourplancore-changelog.md | B | A | - | A | B | история сборок; для работника нужен только "что поменялось в моей работе" |
| reference/ourplancore-all-functions.md | C | A | - | A | C | 2113 строк автогенерированного инвентаря; как страница меню для работника не читается |

### Что учесть при переписке под Lite

1. Взять за образец курс (`ourplancore-course.md`): цель, 5-7 шагов, "проверь себя", ролик. Каждую страницу "Каждый день" держать в этом формате.
2. Убрать из рабочих страниц всё, что про разработку и ИИ-инфраструктуру (пути `AI_Context`, `agent_bridge.py`, номера сборок 2.2.x, DeepSeek, CLI конвейера), или вынести в отдельный раздел "для владельца".
3. Одна страница на тему маршрута: точки W/F/S/U и правила по имени. Остальные три места - короткая ссылка.
4. Переснять кадры, которые сейчас не работают: `ourplancore/v3/sheet-dots.png` (крупно сетку точек, без чёрной половины), `ourplancore/v3/excel-strip.png` (полоса с подписями кнопок: SF площади, WL стены, GB фронтоны, TH truss heel, PP парапеты, E/R карнизы, OP проёмы, SH обшивка, SW shear, SHF шахты, UN units, BL балконы, FR framing), `ourplancore/v3/start-screen.png` (кроп на карточку), `ourplancore/v3/export-pdf.png` (кроп на галки Measurements, Markups, Legend), `ourplancore/v3/measure-count.png` (настоящие посты или holdowns, не двери), `ourplancore/v3/measure-beam.png` (балка с подписью длины и тип позиции как в таблице).
5. Проверить, чем на самом деле становится Beam: таблица `ourplancore-tools.md:24` и `work/horizontal/floor-framing/beam.md:5` говорят Count с длиной в имени, кадр `measure-beam.png` и легенда в `window-map.png` показывают `RB1 16` как Line с `total 50,22 ft`.
6. `ourplancore-all-functions.md`, `ourplancore-ideas.md`, `ourplancore-changelog.md` убрать из меню работника или свести в один раздел "Справка для продвинутых".
7. Ролик `demo/d-routing` снят на реальном проекте (`example-153`, настоящий structural plan с notes). Штампа в кадре нет, но `start/maintenance.md:17-18` обещает кадры только с демо-проекта. Для Lite снять на демо.

## Старые находки: что закрыто, что нет

Пункты `AUDIT.md` (май и сентябрь 2026) и топ-10 `OFFICE_FOLDER_COVERAGE.md` (октябрь 2026) по текущему тексту.

| Пункт | Статус | Где |
| --- | --- | --- |
| AUDIT: FRT parapet против shear-wall sheathing | закрыт | `boss-feedback-rules.md:31`, `parapet.md:25`, `shear-wall.md:63` |
| AUDIT: rim 1.05 против 1.1 | закрыт в каноне, примеры без пометки EWP | `formulas.md:41-42`; `rim.md:67-68`, `joist.md:47`, `takeoff-items.md:99` |
| AUDIT: приоритет Zip и структурного листа | частично | `boss-feedback-rules.md:38`, `wall-sheathing.md:31`; чек-лист `quality-checklist.md:40` живёт по другому правилу (противоречие 3) |
| AUDIT: серии TJI 9 1/2 | открыт | `joist.md:65`; ответ (110, 210, 230) виден на `confluence-007.png` той же страницы |
| AUDIT: SQFT и свесы | открыт | ни одна из 8 страниц площадей не говорит |
| AUDIT: порог soffit узкий и широкий | частично | `soffit-fascia.md:45` по продукту, порога нет, спорит с `eve.md:56` |
| AUDIT: furring LFT или SQ FT | закрыт | `furring-and-jambs.md:29`, `:39` |
| AUDIT: sleepers 1 или 2 слоя | открыт | `balcony-buildup.md:41`, SVG, `deck-porch-balcony-frame.md:93` |
| AUDIT: reconstruction черновик | частично | пометку сняли без источника и примера |
| AUDIT: G и D в blockingoc | закрыт на странице, новая ошибка размерности | `blockingoc.md:32`, `:56`; в `formulas.md` переменные по-прежнему без определения |
| OFFICE 1: corner boards x2 | открыт | `casing-corner-band.md:50`, `:75`, `:80`; `exterior-trims/overview.md:125` |
| OFFICE 2: skewed hangers на 2x | открыт | `hangers.md:89` |
| OFFICE 3: Zmax в кровле | открыт | `ridge.md:43`, `header.md:60`, `dbl-trpl-rafters.md:40`, `:57` |
| OFFICE 4: precut stud таблица | закрыт | `exterior.md:61-77` |
| OFFICE 5: дефолтные headers и балки | закрыт | `headers.md:31-49`, `beam.md:26-40` |
| OFFICE 6: EWP by others нюансы | открыт | `ewp-capital.md:59`, `client-rules.md:13` |
| OFFICE 7: Zip Tape с периметром проёмов, Zip на кровле | открыт, плюс новое расхождение rolls против LFT | `wall-sheathing.md:65`, `underlayment.md:44` |
| OFFICE 8: soffit по типу siding | открыт | `soffit-fascia.md:29`, `:57` |
| OFFICE 9: build-outs | на сайте согласовано | `wall-panels.md:46`, `client-rules.md:59` (расходится только чек-лист в Dropbox) |
| OFFICE 10: bracing и страпы | частично | длины есть (`bracingdrywall.md:38-43`), но пороги не как в чек-листе 2026; формул strapping и CS20 нет |
| OFFICE: таблица W-профилей | закрыт | `steelbeams.md:50-85`; правила "no fillers at dropped steel beams" нет |
| OFFICE: cross bridging | открыт | `blocking.md:53` одна строка, единица спорит с `takeoff-items.md:63` |
| OFFICE: decking 1.05 | хуже: теперь три варианта | противоречие 16 |
| OFFICE: waste 1.1 у casing и base | открыт | `casing.md:34`, `:55`; `base.md:51`, `:71` |
| OFFICE: анкеры 48"/72" против 36" | частично | `sill-plates.md:67` |

## Как проверяли

- Каждая страница прочитана целиком, правила сверены grep-ом по всему `docs/` (факторы, единицы, дефолты, клавиши); там, где сайт спорит сам с собой, помощник h1 сверялся с каноном `dfl-rules` / `dfl-final-fill` только как с источником фактов.
- Картинки: PNG и JPG открывались как есть, SVG рендерились headless Chrome в 1200 px (PyMuPDF красит паттерны в чёрное, им не пользовались). Читаемость оценивалась на 760 px (ширина колонки сайта) и в полном размере. Для всех 600 ссылок снят инвентарь (размеры, вес, резкость, есть ли подпись).
- **Просмотрено около 285 уникальных картинок из 508, на которые ссылаются страницы:** раздел "Работа" - все (h1 66 ссылок, h2 83, h3 58); Старт, Excel и DFL, Справочник - 45 (все, кроме 60 иконок 64x64 вкладки E-Wood); OurPDF - 29 из 50; OurPlanCore - 29 из примерно 150 уникальных (выборка, раздел переписывается). На всех страницах с оценкой C и D вне OurPlanCore просмотрены все картинки.
- Пропущены как служебные: `index.md` (витрина: в маршруте "Я новичок" нет `reference/dfl-overview.md`, ссылка "Ridge / Hip / Valley" ведёт только на ridge) и `start/suggest-change.md` (форма). Страницы редактора (`start/maintenance.md`, `images-and-schemas.md`, `site-preview.md`) оценены, но отмечены.
- Временные файлы аудита лежали в `scratchpad\kb-audit\` и удалены, кроме этого отчёта.
