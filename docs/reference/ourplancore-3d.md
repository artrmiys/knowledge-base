# 3D, менеджеры и Massing

Здесь - вкладки OurPlanCore 3.0, которые по умолчанию выключены: 3D (стены и крыша из замеров), Sheet Manager, Takeoff Manager, Report Builder, Materials, и честный статус старого AI Massing. Нужно, когда план крыши сложный и хочется увидеть рёбра в объёме, когда листов много и их удобнее править таблицей, или когда спрашивают "а что с 3D".

## Статус коротко

| Что | Статус в 3.0 | Где включить |
| --- | --- | --- |
| 3D стены и крыша по замерам | работает, без ИИ | `Settings > Modules > 3D` |
| Roof Qty / Roof Takeoff из 3D-крыши | работает | боковая панель вкладки 3D |
| Sheet Manager, Takeoff Manager | работают | `Settings > Modules` |
| Report Builder, Materials | работают, редко используются | `Settings > Modules` |
| AI 3D Massing (Build 3D Draft, Review, Accept) | выключен в коде с мая 2026, архив | нет |

## 3D: крыша и стены

<figure markdown>
  ![Вкладка 3D](../assets/images/ourplancore/v3/view-3d.png)
  <figcaption markdown="span">Лента 3D (Build, Rafters, Viewer), окно сцены и боковая панель с уклонами рёбер.</figcaption>
</figure>

| Группа | Кнопка | Что делает |
| --- | --- | --- |
| Build | `Auto` | стены из Line, плиты из sqft-Area и крыши из RF-Area, если они есть |
| Build | `Wall` | призмы стен из выбранных Line-takeoff |
| Build | `Roof Base` | контур крыши из выбранных Area-takeoff |
| Build | `Select Edge` | выбор рёбер контура на листе, уклон каждого ребра в боковой панели |
| Build | `Generate Roof` | ridge, hip и valley по сохранённым уклонам рёбер |
| Rafters | `Pick Faces`, `Whole Roof`, шаг, сечение, `Clear` | стропила на выбранных гранях или на всей крыше |
| Viewer | `Fit`, `Iso`, `Top`, `Front`, `Reset` | камера |

Боковая панель: уклон по умолчанию (`Default`, например `6/12`, `4` или `0.333`), для выбранного ребра галка `Defines Slope (eave)` (выключена - ребро плоское, rake или фронтон) и уклон, журнал 3D, вкладки `Roof Qty` и `Roof Takeoff` с площадями и длинами рёбер.

### Крыша за шесть шагов

1. Включить модуль 3D, нарисовать контур крыши как Area (например `rf 6`).
2. Выделить Area, вкладка 3D, `Roof Base`.
3. `Select Edge`: пройти по рёбрам на листе; у карнизов оставить `Defines Slope (eave)` и уклон, у фронтонов снять.
4. `Generate Roof`: появятся ridge, hip, valley.
5. `Rafters > Whole Roof` с шагом и сечением, если нужны стропила.
6. `Roof Qty` / `Roof Takeoff` для площадей скатов и длин рёбер; сверить с ручным замером.

Клавиши режима Roof guide на листе: ++r++ Ridge, ++h++ Hip, ++v++ Valley, ++e++ Eave, ++k++ Rake, ++p++ Pitch, ++esc++ выход, ++backspace++ назад.

??? note "Чего 3D-крыша не делает"
    Свесы с честным пересечением на hip и valley, dormers, ручная правка швов и правка рёбер прямо в 3D-окне - в планах или на уровне идеи, см. [Идеи и планы](ourplancore-ideas.md). Для сметы крыши канон остаётся Area по скатам с уклоном в имени.

## Sheet Manager

<figure markdown>
  ![Вкладка Sheet Manager](../assets/images/ourplancore/v3/sheet-manager.png)
  <figcaption markdown="span">Таблица листов с предложенными именами, масштабом, источником и уверенностью.</figcaption>
</figure>

Таблица всех листов для массовых операций. Включение модуля также добавляет на ленту Main кнопки `Name`, `Scale`, `Name+Scale`.

| Группа | Кнопки |
| --- | --- |
| PDF | `Import PDF(s)`, `PDF Takeoffs`, `Export PDF` |
| Raster | источник `PDF` / `Auto`, пресеты DPI, `Options...`, формат Auto / WebP / PNG, `Prepare`, `First On`, `First Off`, `Clean`, `Cancel` |
| Metadata | `Refresh`, `Analyze`, `Auto Name`, `Auto Scale`, `Name+Scale`, `AI Fill`, `Crop Hints`, `Apply Checked` |
| Open | `Open Sheet`, `Open Tabs`, `Detach`, `Tile M2`, `Open JSON` |
| Organize | `Sort A/S`, `D/Sec/WT`, `Repair Links`, `Auto Folders` |

Колонки: `Rename`, `Scale Action`, `Current Page`, `Current Scale`, `Proposed Name`, `Scale`, `Label`, `Suffix`, `Title`, `Name Source` / `Name Conf.`, `Suffix Source` / `Suffix Conf.`, `Scale Source` / `Scale Conf.`, `Raster`, `Why`, `Warnings`. Галки в `Rename` и `Scale Action` выбирают, что применить кнопкой `Apply Checked`.

Тяжёлые листы: выделить, формат PNG и DPI, `Prepare`, дождаться, затем `First On` - лист открывается из готового растра.

## Takeoff Manager

<figure markdown>
  ![Вкладка Takeoff Manager](../assets/images/ourplancore/v3/takeoff-manager.png)
  <figcaption markdown="span">Таблица позиций: тип, секции, итог, единица, цена, папка.</figcaption>
</figure>

Дерево Takeoffs в виде таблицы: `Item`, `Type`, `Sections`, `Total`, `Unit`, `Price`, `Cost`, `Notes`, `Folder`. Кнопки: `Save`, `Refresh`, `Set Active`, `Properties`, `Open Estimating`, `New Folder`, `New Item`, `Auto Tree`, `From Pages`, экспорт `CSV` / `TXT` / `Excel` / `Current Excel`. Удобно для проверки итогов и цен; рисование по-прежнему в Main View.

## Report Builder и Materials

<figure markdown>
  ![Вкладка Report Builder](../assets/images/ourplancore/v3/report-builder.png)
  <figcaption markdown="span">Report Builder читает TemplateCom.xlsm и показывает таблицу стен.</figcaption>
</figure>

- **Report Builder**: `Reload` (шаблон `TemplateCom.xlsm`), `Refresh` таблицы, `Apply Walls`. Основной путь в Excel сегодня - полоса XL, см. [Экспорт в Excel](ourplancore-excel.md).
- **Materials**: `Extract` материалы из дерева, `Report Sheet`, `Refresh`, открыть `JSON`, `Rows CSV`, `Summary CSV`, `Folder`. Библиотека сборок (стена = стойки + обвязка + OSB) - пока идея.

## Massing: что выключено и почему

Старый рабочий поток AI 3D Massing (кнопки `Build 3D Draft`, `Review Roof / Openings`, `Accept 3D`) отключён в коде с мая 2026 и в интерфейсе не показывается. Черновики модели от ИИ требовали ручной проверки каждой стены и крыши, а детерминированная крыша по уклонам рёбер даёт тот же результат без сети и без сюрпризов. Код остался в репозитории как архив; его удаление стоит в плане. Если где-то в старых заметках встречается "AI massing", речь об этом архиве.

## См. также

- [Идеи и планы](ourplancore-ideas.md) - крыша, менеджеры уровня Excel, AI
- [Листы Pages](ourplancore-pages.md) - Name, Scale, растр в основном окне
- [Экспорт в Excel](ourplancore-excel.md)
- [Workspace и модули](ourplancore-workspace.md#modules)
