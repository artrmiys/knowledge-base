# Макросы и клавиши Excel

Здесь: какие VBA-макросы встроены в книгу `TemplateCom.xlsm`, что делает каждый, когда его жать и в каком порядке. Это не стандартные клавиши Excel: макросы работают только в книге с включёнными макросами.

<figure markdown>
  ![Полоса XL в OurPlanCore](../assets/images/ourplancore/v3/excel-strip.png)
  <figcaption markdown="span">Полоса XL в OurPlanCore пишет замеры в книгу и сама запускает расчётные макросы. Остальные макросы запускаются в Excel клавишей или через Alt+F8.</figcaption>
</figure>

!!! warning "Макрос ничего не делает"
    1. Открыта книга из шаблона `TemplateCom.xlsm` (копия в папке обновлений программы), а не чужой файл.
    2. Макросы разрешены: `File > Options > Trust Center > Macro Settings`.
    3. Курсор стоит там, где нужно: макросы вставки работают от выделенной строки, расчётные - от выделенного диапазона.
    4. Клавиша не сработала - `Alt+F8`, выбрать макрос по имени.

## Клавиши

Клавиши сверены с исходниками макросов. У макросов без клавиши запуск через `Alt+F8` или кнопку.

| Клавиша | Макрос | Что делает |
| --- | --- | --- |
| ++ctrl+shift+b++ | `C_BeamsSort` | балки из пар "марка и длина" в строки `Beam` |
| ++ctrl+shift+j++ | `C_JoistsSort` | joists из пар "число и длина" в строки `Joists` |
| ++ctrl+shift+h++ | `C_HeadersSort` | перемычки по корзинам ширины `up to 48" / 60" / 72" / over 72"` |
| ++ctrl+shift+p++ | `C_PostsSort` | стойки по марке с легендой |
| ++ctrl+shift+f++ | `C_SumTheSameValues` | сложить одинаковые строки (ключ: подпись + единица) |
| ++ctrl+m++ | `Y_MultiplySelectedCells` | домножить выделенные ячейки на адрес (например, на G заголовка) |
| ++ctrl+shift+i++ | `Y_Improve_Note` | переписать текст ноты по образцам листа `Standarts` (результат проверить глазами) |
| ++ctrl+shift+t++ | `Y_CheckEnglish` | проверка английского в выделении |
| ++ctrl+shift+o++ | `Y_InsertDate` | поставить дату |
| ++ctrl+shift+v++ | `Y_noValidation` | снять выпадающие списки (data validation) |
| ++ctrl+w++ / ++ctrl+q++ | `Y_InsertCellsUp` / `X_DeleteCellsUp` | вставить / удалить ячейки A:H со сдвигом. Только так, не целой строкой листа |
| ++ctrl+e++ | `B_DeleteZeroRowsOnlyIn_AtoH` | удалить строки с нулём в количестве (только A:H) |
| ++ctrl+shift+d++ | `X_DeleteRowsByColor` | удалить серые строки-заглушки шаблона |
| ++ctrl+t++ | `B_FrameOC_InsertOneRow` | вставить строку `Frame N" o.c.` под выделенной |
| ++ctrl+r++ | `B_Plate2_InsertOneRow` | вставить строку `Plate (2)` под выделенной |
| `Alt+F8` | `B_BoltsAdd`, `C_TrimsCalc` и остальные | без клавиши |

??? note "Прыжки по секциям (Ctrl+F1 ... Alt+Shift+F9)"
    В части книг при открытии навешиваются клавиши перехода к заголовку секции: ++ctrl+f1++ ... ++ctrl+f5++ `1st ... 5th Floor Walls`, ++ctrl+f6++ / ++ctrl+f7++ `Gable Walls #1 / #2`, ++ctrl+f8++ `Parapet Walls`, ++ctrl+f9++ `Wall Materials`, ++ctrl+f11++ / ++ctrl+f12++ `Foundation / Basement Floor Walls`; ++alt+f1++ ... ++alt+f4++ `1st ... 4th Floor Framing List`, ++alt+f5++ `Loft Framing List`, ++alt+f6++ / ++alt+f7++ `Roof Frame list / Roof System Misc`, ++alt+f10++ `Roof Products`, ++alt+f11++ / ++alt+f12++ `Soffits and Fascias / Exterior Trims`; ++alt+shift+f1++ `Interior Doors&Trims`, ++alt+shift+f2++ `Drywall & Insulation`, ++alt+shift+f8++ / ++alt+shift+f9++ балкон / porch по заливке. Переход ищет заголовок по точному тексту.

    !!! warning "Уточняется"
        В текущих исходниках макросов модуля навигации нет; если клавиши в книге не прыгают, это не ошибка.

## Макросы по этапам

### 1. Расчёт после экспорта (серия A, запускает полоса XL)

Работают по выделенному диапазону в правой зоне `J:N`. Полоса XL в OurPlanCore запускает их сама; руками они нужны только при повторном расчёте одной группы.

| Макрос | Что делает | Когда |
| --- | --- | --- |
| `A1_UnitTable` | таблица units по этажам | есть `units` в дереве |
| `A2_SQFT_calc` | площади этажей, фронтонов, truss heel; уклоны кровли по порядку появления в выделении | после `SF`, `GB`, `TH` |
| `A3_Walls_Calc_AllGroup` / `_OneGroup` | стены из J:N в матрицу `O:AB` и строки Floor Walls; `(2)` в имени множит длину, `corr` = `cor` | после `WL` |
| `A4_Parapet` | парапеты: три числа из хвоста имени (`prpt 6.4 5.3 0.5`) | после `PP` |
| `A5_Openings` | проёмы по ширине в корзины headers, flashing | после `OP` |
| `A6_Eve_Rakes` | `eve 12 main`, `rake 12 main`, `returns 24`, `canopy 36 porch` в строки карнизов | после `E/R` |
| `A7_walls_sheathing` | по тексту в J (`Zip`, `OSB`, `no insulation`, `1" Insulation`) оставляет нужные строки обшивки и пишет спек-ячейку `O3` или `O5` | после `SH` |
| `A8_SplitWallSuffixes_ByJ` | делит имена стен на базовое имя для A3 и суффикс с деталью (`ext 10.09 5/S400`) | стены с деталью в имени |
| `Y_Run_First6` | A2 ... A6 подряд, A1 последним (A1 перестраивает выделение) | ручной полный прогон |

### 2. Scope (серия A9)

| Макрос | Что делает |
| --- | --- |
| `A9_Fame_only` | убирает блоки отделки и продуктов, оставляет только каркас (удаление только A:H со сдвигом) |
| `A9_1_wall_panel` | в секциях `Floor Walls` оставляет строки панельного дома, обшивку переносит в строку WRB и Tape; стик-строки этажей возвращаются ниже под нотой `Note: Optional stick frame, if walls are not panels; verify.` |

Оба запускаются при создании книги по scope проекта. На готовой книге повторно не гонять без причины: они удаляют строки.

### 3. Структурные после ввода (серия C)

| Макрос | Вход | Выход |
| --- | --- | --- |
| `C_BeamsSort` | пары `H5 7` + число; легенда в конце выделения `H5 - (2) 1 3/4 x 11 7/8 LVL`; хвост `(24V48)` уходит в E | строки `Beam` с размером по коду; в J-режиме сам вставляет место в A:H |
| `C_HeadersSort` | `(2) 2x10 4`, `ext H5 7`; легенда `H5 - (2) 2x10` | `Ext. Headers up to 48" / 60" / 72" / over 72"`, int отдельно |
| `C_JoistsSort` | пары число / длина с маркой и шагом (`11 7/8 TJI 110 24"`) | одинаковые длины складываются; длина больше 8' и нечётная получает +1 |
| `C_PostsSort` | `C5 2`, `C5 12`; легенда `C5 - 3 1/2 x 5 1/4 PSL 1.8E` | строки `Posts` с кодом и сортом в E; длина по умолчанию 10' |
| `C_RimBoardBlockingHangers` | флаги в M: `r` rim, `rb` ribbon, `b` / `b48` blocking, `h16` hangers, `s` screws, `t` ties, `blt24` anchor bolts, `l` ledger, `bd` drywall blocking, `bft` bracing for trusses; двойная буква = x2; легенда материала в конце (`l - 2x10`, `t24 - A35`) | строки rim, ribbon, blocking, hangers, ledger по группам; блок bolts + washers + nuts |
| `C_SumTheSameValues`, `C_SumNearWindowValues` | три колонки подпись / число / единица | свёрнутые суммы; у окон - сумма значений рядом с проёмами для A5 |
| `C_TrimsCalc` | блок отделки одного элемента + строка `EA` | отделка умноженная на количество ([Trim macros](../work/exterior-trims/macros.md)) |

### 4. Вставка строк и блоков (серия B)

Встать на строку, с которой нужен блок: вставка идёт от неё вниз, только в A:H.

| Макрос | Что вставляет |
| --- | --- |
| `B_BoltsAdd` | 4 строки: `Blocking`, `Anchor Bolts`, `Washers`, `Nuts` (счёт парами, подписи из H) |
| `B_Plate2_InsertOneRow`, `B_FrameOC_InsertOneRow` | строка `Plate (2) ... P.T.` или `Frame N" o.c.` с формулой |
| `B_JambsAllBlock` | блок `Blocking around all openings` по проёмам |
| `B_ShaftWallsBlocks` | блоки shaft walls (liner panels + channels) |
| `B_PaversBlock` | `Pavers` с нотой `by others` и строками рейлинга |
| `B_MetalStuds_ByJ` (`_16oc`, `_24oc`) | тройка `Tracks (1) btm`, `Deflection Tracks (1) top`, `Mtl Studs` из таблицы справа (размер, длина, единица, высота) |
| `B_Balcony_Insert_Template_FromText` | балконный блок по команде `b 12x30`. В текущих книгах блок `#1` уже есть в шаблоне: заполнять его, а не вставлять второй ([Блоки](dfl-blocks.md)) |
| `Y_add_2400V48` | проставить значения `2400 V48` по двухколоночному списку |

### 5. Чистка и финал (серии X, Y)

| Макрос | Когда |
| --- | --- |
| `X_DeleteRowsByColor` (++ctrl+shift+d++), `B_DeleteZeroRowsOnlyIn_AtoH` (++ctrl+e++) | после всех вставок: заглушки и нули долой |
| `X_ClearColor`, `X_ClearWall_SQFTCells`, `X_ClearParapetTable` | серая заливка в белую; очистить площади стен или таблицу парапетов перед новым расчётом |
| `Y_noValidation` (++ctrl+shift+v++), `Y_CheckEnglish` (++ctrl+shift+t++), `Y_InsertDate` (++ctrl+shift+o++) | перед processed `.xlsx` |
| `Y_Improve_Note` (++ctrl+shift+i++) | черновик ноты; потом проверить по [правилам нот](standard-notes.md) |
| `Z_Dont_use_Run_ByPriority` | не использовать |

## Порядок работы с книгой

1. В OurPlanCore: легенда `LG` заполнена (коды балок, стоек, перемычек, флаги деталей, обшивка), затем `ALL` или нужные кнопки полосы XL.
2. В Excel: проверить, что всё из дерева дошло (предупреждение экспорта перечисляет пропущенные позиции), поправить J:N.
3. Структурные сорты, если что-то выгружалось руками: ++ctrl+shift+b++, ++ctrl+shift+j++, ++ctrl+shift+h++, ++ctrl+shift+p++, затем `C_RimBoardBlockingHangers`.
4. Блоки балконов, porch, holdowns, bolts, jambs ([Блоки](dfl-blocks.md)).
5. Чистка: ++ctrl+shift+d++ серые, ++ctrl+e++ нули, ++ctrl+shift+v++ validation.
6. Финал: ++ctrl+shift+o++ дата, ++ctrl+shift+t++ английский, ноты по правилам, Front Page заполнен, затем processed `.xlsx`.

## Частые ошибки

- Вставка целой строки листа вместо ++ctrl+w++: правые зоны поехали.
- `A9_*` запущен повторно на заполненной книге: удалил нужные строки.
- `C_BeamsSort` без легенды: в B стоит код `H5` вместо размера.
- Балконный блок вставлен макросом поверх шаблонного `#1`: два блока.
- Количество вписано числом после макроса: при повторном экспорте не обновится.

Все ошибки по книге: [Частые ошибки, Excel DFL и ноты](../start/common-mistakes.md#excel).

## См. также

- [DFL: как устроена книга](dfl-overview.md), [Блоки балконов, porch и holdowns](dfl-blocks.md), [Формулы и факторы](formulas.md)
- [Trim macros](../work/exterior-trims/macros.md), [OurPlanCore: Estimating и экспорт](ourplanecore.md)
