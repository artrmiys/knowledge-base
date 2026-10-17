# Термины и спецификации

Здесь: что значат обозначения на чертежах и в спецификации, где искать источник для строки и как проверить правило. Внутренний способ расчёта (факторы, формулы) не становится отраслевой нормой; он живёт в [Формулах](formulas.md).

## Листы комплекта

| Обозначение | Что это | Что брать |
| --- | --- | --- |
| `A` (A101, A3.01) | архитектура: планы, фасады, разрезы, wall types, schedules | площади, стены, проёмы, отделка, типы стен и слоёв |
| `S` (S101, S3.0) | конструктив: framing plans, details, schedules, general notes | балки, joists, shear walls, holdowns, анкеры, толщина обшивки |
| `G`, `LS`, `CS` | обложка, code compliance, life safety | тип конструкции, FRT, rated walls |
| `M`, `E`, `P`, `FP`, `C`, `L` | инженерные сети, civil, landscape | в каркасе не нужны |
| `WS-1`, `WRS-1`, `SW-x` | wall sheathing schedule, roof sheathing schedule, shear wall schedule | разные таблицы, читать до конца |

Разрез вместе с деталями важнее плана: высота стойки, слои, FRT.

## Термины каркаса

| Термин | Значение |
| --- | --- |
| `o.c.` | on center, шаг между осями: `16" o.c.` |
| `TYP.`, `U.N.O.` | typical; unless noted otherwise: правило по умолчанию, пока деталь не говорит иначе |
| `R.O.` | rough opening, проём в каркасе = изделие плюс зазор (обычно 1") |
| Floor-to-floor, F.F.E. | отметки этажей; высотой стойки не являются |
| Plates, studs, jack, king, cripple | plates снизу и сверху, стойки, стойки проёма |
| Header | перемычка над проёмом; `(2) 2x10`, `(3) 1 3/4 x 11 7/8 LVL` |
| Rim, ribbon, blocking, bridging | торцевая доска перекрытия; врезная доска balloon framing; блоки между joists |
| Top chord bearing | ферма опирается верхним поясом: вместо ribbon blocking между фермами |
| Truss heel | высота пятки фермы у стены: полоса обшивки |
| Gable stick, gable truss | фронтон из стоек или ферма с вертикальными стойками |
| Draft stop, fire block | перегородки чердака и перекрытия по зонам; разные позиции |
| Parapet | стенка над кровлей: наружная и внутренняя высота, ширина верха |
| Shear wall, holdown, strap, anchor bolt | стена жёсткости, анкер стойки, лента, болт plate к бетону |
| Ledger, box, stringer, tread, riser | доска к стене, обвязка, косоур, проступь, подступёнок |
| Sleeper, overframe, piggyback | лежень под настил; надстройка кровли; вторая ферма поверх первой |

## Материалы и обозначения

| Обозначение | Значение |
| --- | --- |
| `P.T.`, `ACQ .25 / .40` | pressure-treated, класс пропитки; `.40` для стоек в земле и 4x4 |
| `KD`, `S4S`, `#2 & Btr`, `MSR 1650f-1.5E` | kiln-dried, строганый с четырёх сторон, сорт, машинный сорт |
| `FRT`, `FRTW` | fire-retardant treated wood: одно требование, два написания |
| `EWP`: `LVL`, `LSL`, `PSL`, `TJI`, `LPI`, `BCI`, `Rim Board` | engineered wood products; серия остаётся в строке |
| `CDX`, `OSB`, `Ply`, `T&G`, `SE` | plywood exterior glue, OSB, tongue-and-groove, square edge (только под H-clips) |
| `Zip`, `Zip R-3 / R-6 / R-9` | обшивка с интегрированным WRB; R - с утеплителем |
| `WRB`, `Air Barrier`, `AVWB` | наружный барьер: Tyvek, fluid-applied; на чертеже это не vapor barrier |
| `GWB`, `Type X`, `DensGlass`, `Durock` | гипсокартон, огнестойкий гипс, наружный гипс, цементная плита |
| `Shaft liner`, `CH`, `J`, `H`, `C` channels | стены шахт: панели 1" и профили |
| `H-clips`, `PSCL` | клипсы между листами кровли по шагу опор |
| `Zmax`, `HDG`, `SDS`, `SDWS` | оцинковка; структурные винты Simpson |

## Тип конструкции и FRT

| Тип | Следствие для каркаса |
| --- | --- |
| Type III-A, III-B | наружные стены негорючие или FRT: всё в плоскости наружной стены FRT, EWP там запрещён |
| Type V-A, V-B | обычный деревянный каркас; FRT только по детали |
| Podium (I-A снизу, III или V сверху) | деревянные стены ниже podium по правилам подиума; FRT по Code Compliance Summary |

Тип берётся с листа Code Compliance Summary или Life Safety, не из условной ноты.

## Разделы спецификации (CSI MasterFormat)

| Раздел | Тема |
| --- | --- |
| 03 | Concrete: анкеры, embed |
| 05 | Metals: стальные балки, CFMF, metal connectors |
| 06 | Wood, Plastics, Composites: каркас, EWP, обшивка, отделка, decking |
| 07 | Thermal and Moisture Protection: WRB, insulation, membrane, flashing |
| 08 | Openings: окна, двери, R.O. |
| 09 | Finishes: гипс, shaft liner, base, casing |

Обозначения в колонке E вида `07.04 WD-01` - проектные метки из легенды, не коды MasterFormat: сохранять как в источнике.

## Как проверить правило

1. Найти лист, schedule, деталь или раздел спецификации своего проекта.
2. Проверить, относится ли правило к этому материалу, узлу и scope.
3. Для изделия открыть страницу производителя нужной серии.
4. При конфликте источников записать оба листа и принятое решение нотой ([Ноты в DFL](standard-notes.md)); не прятать допущение заменой материала.
5. После расчёта пройти [QA checklist](../start/quality-checklist.md).

## См. также

- [Material catalog](material-catalog.md), [Hardware catalog](hardware-catalog.md), [Hangers](hangers.md)
- [Советы и важные вещи](boss-feedback-rules.md), [Workflow](../start/workflow.md)
