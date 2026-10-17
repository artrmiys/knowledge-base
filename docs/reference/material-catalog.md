# Material catalog

Здесь: как называются материалы в книге (лист `Mat List`) и в колонке B, чтобы строка читалась и заказывалась без вопросов. Только размеры, сорта и семейства; кодов поставщика в публичной базе нет.

!!! tip "Размер всегда виден"
    `2x10 P.T.`, `(2) 1 3/4 x 11 7/8 LVL`, `4x8 3/4" CDX`, `7/16" Zip`. Общие слова `lumber`, `trim`, `I-joist` без серии в B не пишутся.

## Пилёный лес

| Семейство | Размеры | Длины | Где |
| --- | --- | --- | --- |
| **P.T. SYP** (pressure-treated, ACQ .25; `.40` для 4x4 стоек) | `2x4` ... `2x12`, `4x4`, `4x6`, `6x6` | `8'` ... `24'` | sill plates на бетоне и кладке, deck, balcony, ledger, posts на улице |
| `2x2 P.T. Clear` | `2x2` | `8'` | balusters |
| **D Fir #2 & Btr** | `2x4` ... `2x12` | `8'` ... `20'` | основной каркас |
| **D Fir studs precut** | `2x4`, `2x6` x `92-5/8`, `104-5/8`, `116-5/8` | precut | стены 8', 9', 10' |
| **KD studs** | то же, kiln-dried | precut | где спецификация требует KD |
| **MSR** (`1650f-1.5E`, `2400f-2.0E`) | по schedule | | отдельная строка, не смешивать с #2 |
| **FRT** | любой размер с пометкой `FRT` в B | | по типу конструкции (Type III: всё в плоскости наружной стены); `FRT` и `FRTW` на чертеже - разные обозначения одного требования |

- Нижняя plate P.T. только на бетоне и кладке; на деревянном перекрытии обычная.
- Посты на улице (porch, балкон, перила) всегда P.T.; под крышей - обычные.

## Engineered lumber (EWP)

| Семейство | Сечения | Назначение |
| --- | --- | --- |
| **LVL** (1 3/4" thick) | глубина `5 1/2` ... `24` | beams, headers, built-up posts; plies явно `(2)`, `(3)` |
| **LSL** (1.55E), Timberstrand | `1 1/2 x 3 1/2 ... 11 1/2`, `1 3/4 x 11 7/8`, `14` | прямые studs, rim, beams |
| **LSL Rim Board** | `1 1/4 x 9 1/2 ... 20` | rim: пишется `11-7/8" LSL Rim`; без продукта на чертеже - `11-7/8" Rim` |
| **PSL** | `3 1/2 x 5 1/4`, `5 1/4 x 7`, `5 1/2 x 11 7/8` | тяжёлые балки и стойки |
| **I-joists** | `TJI 110 / 210 / 230 / 360 / 560`, `LPI 18 / 20 / 32 / 36 / 56`, `BCI`, `RED-I` x `9 1/2`, `11 7/8`, `14`, `16` | серия остаётся в B: от неё зависит hanger |

- Scope `EWP by others`: LSL, LVL, I-joists и rim не считаем, но нота `Note: All EWP products are by others.` стоит в шапке.
- С I-joists только engineered rim; LVL rim - только когда к нему крепится deck или corridor.
- Type III: LVL, PSL, LSL в плоскости наружной стены запрещены, `LVL FRT` не пишется.

## Обшивка, настил, барьеры

| Материал | Толщины | Как пишется |
| --- | --- | --- |
| Plywood, CDX | `1/2`, `15/32`, `19/32`, `5/8`, `3/4` | `19/32" Ply`; `19/32 = 5/8`, не `1/2`. `CDX` только если так в спецификации |
| OSB | `7/16`, `15/32`, `1/2`, `5/8` | `7/16" OSB`; `LP FlameBlock` не равен `7/16 OSB FRT` |
| Zip, Zip R | `7/16`, `1/2`, `5/8`; `R-3`, `R-6`, `R-9` | `7/16" Zip R3` + `Zip Tape`; `7/16" Zip` на S и `Zip R-3` на A - один продукт |
| Subfloor | `3/4" T&G` (AdvanTech), `5/8` SE; `1/2" underlayment` | под ванны `3/4 Ply`, не под души; новый subfloor поверх существующего по детали |
| Gypsum sheathing | `5/8" DensGlass`, `1/2" Durock`, `5/8" Type X ext.` | слои по стрелкам детали: двойная стрелка = два слоя |
| Shaft liner | `1" Shaft Liner` + `CH` / `J` или `H` / `C` channels | состав по wall type |
| WRB | по спецификации: `Tyvek`, fluid-applied barrier | в книге строка `Vapor Barrier` (имя шаблона), на чертеже это WRB / Air Barrier, не vapor barrier |
| Insulation | `R-6`, `1"`, `1 1/2"`, `2"` rigid; tapered на плоской кровле | только наружный после обшивки; внутренний утеплитель и sound batt во frame-scope не считаем |
| Membrane | `EPDM`, `Ice & Water`, `Felt 15#`, `1/4" DensDeck` cover board | кровля по разрезу |

Расхождение арх и S по обшивке решается нотой: [Ноты в DFL](standard-notes.md#spec-cells).

## Accessories

| Материал | Размеры |
| --- | --- |
| Sill sealer | `1/2 x 4`, `x 6`, `x 8`, рулоны 50' |
| Termite shield | `Copper` |
| Panel adhesive | `29 oz` тубы: `=C<subfloor>/3` |
| H-clips | по толщине настила и шагу опор ([H-clips](../work/horizontal/roof-framing/h-clips.md)) |

## Отделка, настил, перила

| Группа | Типовые размеры |
| --- | --- |
| Casing, band, corner, watertable | `5/4x3` ... `5/4x12`; vinyl `3-1/2"`, `4"` |
| Fascia, soffit, frieze | fascia `1x6` ... `1x12`, `2x8`; soffit `1x`, vinyl vented, beadboard; frieze `5/4x6` ... `5/4x10` |
| Crown, moulding | `2"` ... `5-1/2"` |
| Decking | `2x6 DuxxBak` (балконы), `5/4x6` (Wd, Azek, Trex; терраса над гаражом), `5/4x4 T&G Mahogany`, `1x6 T&G Cedar` |
| Rail | `2x2` balusters, `2x4` rails, `2x6` cap rail, `4x4 P.T.` posts + sleeve + cap, `6' Rail section`, cable SS |
| Columns | `4x4 P.T.`, `6x6 P.T.`, fiberglass taper / non-taper |

## См. также

- [Подписи строк DFL](takeoff-items.md), [Ноты в DFL](standard-notes.md), [Hangers](hangers.md), [Формулы и факторы](formulas.md)
- [Exterior Wall Materials](../work/vertical/sheathing/exterior-materials.md), [Rails & Decking](../work/exterior-trims/rails-decking.md)
