# QA checklist

Используй перед отправкой job.

## Общая проверка

- Scale проверен на каждом drawing set, который использовался для takeoff.
- Arch, Structural, specs, schedules, wall types и RCP pages проверены.
- Все новые formulas сразу протестированы.
- Identical floors отмечены, но materials всё равно перечислены per floor.
- Нет двойного 1.1 waste из formulas, которые ссылаются на другие formulas.
- Notes добавлены там, где есть assumptions.

## Критические проверки COM

1. FRT scope проверен в specs и details.
2. Если exterior wall materials = FRT, exterior blocking и parapets тоже FRT.
3. Multi-layer sheathing, underlayment, sound membrane проверены.
4. Edge sheathing around floor/roof perimeter проверен.
5. Gypcrete floors проверены на double bottom plates.
6. Rigid insulation проверен.
7. Interior sheathing и holdowns проверены.
8. Parapet inside/outside sheathing проверен.
9. Piggy trusses и sleepers проверены.
10. Flat roof curb blocking проверен.
11. Exact stud heights рассчитаны.
12. S-details соблюдены, если они есть.
13. Exterior sheathing сверен с Arch/energy notes.
14. Window blocking проверен, особенно Zip R или insulation.
15. `1x3 PT strapping` проверен для Hardi paneling.
16. Exterior buildouts проверены как stick framed.
17. Shaft walls проверены.
18. Dropped soffits проверены на RCP pages.
19. Soffit plywood under roof trusses проверен.
20. Under podium / existing conditions проверены; panels не предполагаем.

## Частые пропуски

- Rim at roof TJI.
- Two rows of blocking для walls 10' и выше.
- A35 clips на shearwall-to-shearwall connections.
- Holdowns per details.
- Jamb blocking для windows и interior doors.
- Kitchen blocking: 2x6, 4 pieces of 14' per kitchen.
- Bath blocking: 2x6, 1 piece of 14' per bathroom.
- Densedeck или glass mat protection board на flat roofs.
- Extra rigid XPS layer.
- Metal studs помечены by others, если client исключает их.
- Interior trims сверены с room schedule.
- Tile base исключён, если нужен только wood base.
- Crowns включены, когда trim scope активен.

## Финальная проверка «было/стало»

Перед отправкой готового takeoff проверяй пять файлов параллельно:

1. Открыть **готовый PlanSwift** (с финальными правками).
2. Открыть свой **локальный Excel «до»** (или из папки `old`, если есть).
3. Открыть **готовый Excel** из `Example`.
4. Сравнить **Excel «было/стало»**: оформление, что добавлено/удалено, формулировки.
5. Сравнить **PDF «было/стало»**: оформление, что добавлено/удалено, формулировки.

На разбор ошибок и финальную проверку резервируй **30–60 минут** — этот этап не пропускать.

## Цикл правок (worker side)

- Открыть PlanSwift и начинать правки, параллельно задавать вопросы.
- В Trello — **жёлтая метка** + примерная дата готовности.
- Excel править.
- После завершения правок — **зелёная метка**.
- Цикл может повториться **2–3 раза** до полного согласования.

Готовые файлы (PlanSwift, Excel) — всегда хранятся в облаке (MEGA), не локально.
