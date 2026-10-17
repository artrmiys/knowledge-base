# Формулы и факторы

Здесь: множители и формулы колонки C, которые стоят в книге, и чем studs отличаются от joists. Формулы даны в английской локали (`CEILING`, `EVEN`); в русской Excel показывает их как `ОКРВВЕРХ`, `ЧЁТН` с `;` между аргументами, смысл тот же.

!!! warning "Stud и Joist считаются по разным таблицам"
    У studs и joists один и тот же `o.c.`, но разные множители: studs по правилу владельца (стойка на фут плюс waste), joists по геометрии (`12 / spacing`). Не путать таблицы.

## Stud spacing factors { #stud-spacing-factors }

Канон по стойкам. На `16" o.c.` считается одна стойка на фут стены плюс 10 процентов waste, а не геометрические `0.75`: так покрываются углы, T-пересечения, jack, king, cripple у проёмов и обрезь.

| Spacing | Фактор (pcs / LFT) | Откуда |
| --- | ---: | --- |
| 12" o.c. | **1.4667** | 1:1 с масштабом 16 к 12 (x1.333) плюс 10% waste |
| 16" o.c. | **1.1** | 1:1 плюс 10% waste |
| 24" o.c. | **0.625** | 0.5 плюс 25% waste |

- `pcs = wall LFT x фактор`; высота стойки в E строки, до 1/8" (floor-to-floor минус subfloor, минус перекрытие, минус plates).
- Bearing walls как Extra: основная линия с обычным фактором, лишние plies отдельной строкой `double extra`, базу вычесть из обычных studs. Факторы Extra: `16" o.c.` 0.75, `24" o.c.` 0.5 (без waste базовой строки).
- Double стена = два каркаса только если на плане два каркаса; staggered corridor 2x4 = два ряда на 16" o.c., plates 2x6.

## Joist spacing factors

Joists, rafters и floor trusses - по истинной геометрии center-to-center, без stud-waste.

| Spacing | Фактор (pcs / LFT ширины) |
| --- | ---: |
| 12" o.c. | **1.0** |
| 16" o.c. | **0.75** |
| 19.2" o.c. | **0.625** |
| 24" o.c. | **0.5** |

- `pcs = ширина пролёта LFT x 12 / spacing + 1` (торцевой joist на каждый run).
- Из OurPlanCore joists приходят парами "число / длина" из J Area: одинаковые длины складываются, длина больше 8' и нечётная получает +1 (правило `C_JoistsSort`); короткие до 7' идут на двойную доску (`90 x 6'` = `45 x 12'`, в E `90 pcs 6'`). Extra той же длины прибавляется к основной строке.
- Hangers по joists: на оба конца каждого joist, по сборкам; штучный крепёж меньше 50 - до чётного.

## Rim, ribbon, blocking, ledger

| Item | Unit | Фактор |
| --- | --- | --- |
| Rim Board, EWP-jobs | LFT | `1.05` |
| Rim Board, остальные (residential, COM) | LFT | `1.1` |
| Blocking, Ribbon, Ledger, Blocking for Drywall, bracing по стенам | LFT | `1.1` один раз в формуле |

- Rim и blocking остаются в LFT и не делятся на куски по 16', если output прямо не требует pcs.
- Top chord bearing trusses: вместо ribbon board blocking между фермами, часто `(2) 2x6`.
- Blocking по шагу считается кусками: формулы ниже.

## Blocking formulas { #blocking-formulas }

```excel
Flat 48" o.c.          = CEILING(LFT * 12 / 48 * 2 * 1.1 / Stock LF, 1)
Diagonal 48" o.c.      = CEILING(LFT * 12 / 48 * 2.5 * 1.1 / Stock LF, 1)
Blocking btw trusses   = CEILING(G * 12 / 48 * 2 / D * 1.1, 1)
T blocking at gables   = EVEN(G / D)
```

### Blocking factor по типу { #blocking-factor }

| Тип | Фактор кусков на пролёт |
| --- | ---: |
| Flat | `2` |
| Diagonal | `2.5` |
| Vertical | `1.5` ... `2` |

Стены 10' и выше - два ряда blocking. Kitchen: `2x6`, 4 штуки по 14' на кухню; bath: 1 штука по 14' на ванную. Kickers только там, где они есть на детали.

## Формулы колонки C по типу строки

| Тип строки | C | D |
| --- | --- | --- |
| Листы 4x8 (обшивка, subfloor) | `=CEILING(G/32*1.1,1)` | `4x8` |
| Погонаж по длине стока | `=CEILING(G/D,1)` (D = 14 или 16) | `LFT` |
| Plates | `=EVEN(G*H*1.1)` (H = число plates) | `LFT` |
| Studs | `=CEILING(G*1.1,1)` на 16" o.c. | `pcs` |
| Крепёж по шагу (anchors, ties, hangers) | `=CEILING(G*12/H*1.1,2)`; при 50 и больше родная значимость `,10` или `,1` | `pcs` |
| Screws по фермам | `=CEILING(...,3)` | `pcs` |
| Washers | `=C<строка анкеров>` или `=SUM(...)` одной строкой на группу | `pcs` |
| H-clips | по толщине настила и шагу опор: `PSCL at 16"` = 6 на лист, не "4 на лист"; при T&G и настиле толще порога спецификации не нужны | `pcs` |
| Truss bracing | по умолчанию `2x6`, ряд каждые 10'; `=CEILING(G/4/D,1)` на всю площадь под крышей, включая гараж | `pcs` |
| Panel adhesive | `=C<subfloor>/3` | `tubes` |
| Resilient channels | `=CEILING(area*12/spacing*1.1,10)`, только где показаны в типе стены | `LFT` |
| Holdowns | `=G` к бетону, `=G*2` через деревянное перекрытие | `pcs` |
| Двусторонний shear wall | G = сумма двух лиц, без ещё одного x2 | `SQ FT` |

Формулы смотрят на свой блок: свой header, свой множитель units, свой этаж. Скопированный этаж со ссылками в чужой блок - самая частая ошибка книги.

## Кровля

Уклон применяется один раз: площадь в плане x `sqrt(1 + (rise/12)^2)`.

| Pitch | Фактор |
| --- | ---: |
| 4/12 | 1.054 |
| 6/12 | 1.118 |
| 8/12 | 1.202 |
| 12/12 | 1.414 |

Уклон из листа, у каждого корпуса свой (гараж 4/12 при доме 6/12). Число в имени `rf 6` - это rise на 12.

## Округление

| Что | Правило |
| --- | --- |
| Штучный крепёж меньше 50 | вверх до чётного (significance 2) |
| 50 и больше | значимость шаблона: `,10` большие ties и screws, `,1` листы и рейки |
| Доски, листы, трубы | целыми вверх; `2.75` и `9.6` в C не бывает |
| Waste | один раз: если G уже с 1.1, в C второго 1.1 нет |

## Shaft Walls { #shaft-walls }

Shaft walls отдельным блоком, даже когда стены дома идут панелями by others. Материал из wall type и детали: бывают `2-1/2"` CH + J-channel и `2"` H + C-channel. `Stock LF` обычно 12; panels в лист как `2x12 Panels`.

```excel
2-1/2" CH + J:
1" Shaft Panels        = CEILING(LFT * 1.1 / 24, 2)
CH-channels vertical   = CEILING(LFT * 0.5 * 1.1 / Stock LF, 2)
J-channels horizontal  = CEILING(Horizontal LFT * 1.1 / Stock LF, 2)

2" H + C:
1" Shaft Panels, 2 слоя = CEILING(LFT * 2 * 1.1 / 24, 2)
H-channels vertical     = CEILING(LFT * 0.5 * 1.1 / Stock LF, 2)
H-channels horizontal   = CEILING(Horizontal LFT * 2 * 1.1 / Stock LF, 2)
C-channels perimeter    = CEILING(Perimeter LFT * 1.1 / Stock LF, 2)
```

Dropped ceiling metal joists: `12" C-type = Area * 0.75 * 1.1 LF`.

## Проверка порядка величин

Число выглядит странно - сравнить с типичным для похожего дома: [Ориентиры количеств](quantity-benchmarks.md). Это проверка разумности, не норма; расхождение значит "открой деталь и единицы", а не "исправь на среднее".

## См. также

- [DFL: как устроена книга](dfl-overview.md), [Подписи строк DFL](takeoff-items.md), [Советы и важные вещи](boss-feedback-rules.md)
- [Joist](../work/horizontal/floor-framing/joist.md), [Rim Board](../work/horizontal/floor-framing/details/rim.md), [Blocking](../work/horizontal/floor-framing/details/blocking.md), [Shaft](../work/vertical/walls/shaft.md)
