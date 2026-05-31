# Формулы и факторы

!!! warning "Stud ≠ Joist — это разные факторы"
    У **studs** и **joists** один и тот же `o.c.`, но **разные множители**.
    Studs считаем по boss-rule (`1 стойка/фут + waste`), joists — по реальной
    геометрии center-to-center (`12 / spacing`). Не путай таблицы местами.

## Stud spacing factors

Канонический источник по стойкам. Boss-rule: на `16" o.c.` считаем **1:1**
(одна стойка на фут) **+ 10% waste**, а не геометрические `0.75`. Это сделано
намеренно — учитывает corners, T-intersections, jack/king/cripple вокруг
проёмов и обрезь.

| Spacing | Фактор (pcs / LFT) | Откуда |
| --- | ---: | --- |
| 12" o.c. | **1.4667** | `1:1` масштаб 16→12 (×1.333) + 10% waste |
| 16" o.c. | **1.1** | `1:1` + 10% waste |
| 24" o.c. | **0.625** | `0.5` + 25% waste |

- Формула: `pcs = wall LFT × фактор`.
- На больших COM jobs studs часто считают по **точной высоте** (nested-IF
  авто-подбор 2x4/2x6), см. [Exterior Walls](../work/vertical/walls/exterior.md).
- Сверка с индустрией — [Quantity benchmarks](quantity-benchmarks.md).

## Joist spacing factors

Joists (и rafters, и floor trusses) считаем по **истинной геометрии**
center-to-center, без stud-waste. Фактор = `12 / spacing`.

| Spacing | Фактор (pcs / LFT ширины) |
| --- | ---: |
| 12" o.c. | **1.0** |
| 16" o.c. | **0.75** |
| 19.2" o.c. | **0.625** |
| 24" o.c. | **0.5** |

- Формула: `pcs = run ширина LFT × 12 / spacing`, **+1** торцевой joist на каждый run.
- Hangers по joists: `=ЧЁТН(LFT × 12 / spacing)` — округление вверх до чётного.
- Подробно — [Joist](../work/horizontal/floor-framing/joist.md).

## Rim и Blocking

| Item | Unit | Фактор |
| --- | --- | --- |
| Rim Board (EWP-jobs) | LFT | `1.05` |
| Rim Board (residential / COM / прочее) | LFT | `1.1` |
| Blocking | LFT | без factor, если continuous |
| Ribbons / ledgers / bracing | pieces | используй 16' ceiling, когда требуется |

- `1.05` — это EWP-specific factor. На обычных jobs rim считается тем же
  `1.1`, что и blocking.

## COM Waste

- Используй 1.1 в formulas, если source value уже не содержит 1.1.
- Не дублируй waste через chained formulas.

## Shaft Walls

```text
CH channels vertical  = LFT * 0.5 * 1.1 / 12
J-channels horizontal = LFT * 2 / 10 * 1.1 / 10
Shaft panels          = LFT * 0.5 * 1.1, listed as 2x12
```

## Dropped Ceiling Metal Joists

```text
12" C-type metal joists = Area * 0.75 * 1.1 LF
```

## Blocking formulas

```excel
Flat 48" o.c.     = CEILING(G * 12 / 48 * 2 * 1.1 / D, 1)
Diagonal 48" o.c. = CEILING(G * 12 / 48 * 2.5 * 1.1 / D, 1)
```

### Blocking factor по типу

Множитель зависит от типа блокинга (сколько кусков на пролёт):

| Тип | Фактор |
| --- | ---: |
| Flat | `2` |
| Diagonal | `2.5` |
| Vertical | `1.5–2` |

Diagonal дороже flat (длиннее рез + угол); vertical — между ними, ближе к flat
при плотной раскладке. Continuous blocking считается без factor (см. выше).

## Контрольные диапазоны количеств (sanity-check)

Помимо самих формул, ИИ-ассистент сверяет **итоговые количества** готового DFL с
типовым диапазоном по `(секция, строка)` из 180+ проектов (median / IQR, Tukey
fences). Значение вне диапазона — повод проверить (опечатка, единицы, scope-аномалия),
а не ошибка. Это автопроверка к [QA checklist](../start/quality-checklist.md);
механика — в [ИИ-ассистент](ai-assist-system.md).

## Kitchen and Bath Blocking

| Location | Правило |
| --- | --- |
| Kitchen | 2x6 blocking, 4 pieces of 14' на kitchen |
| Bathroom | 2x6 blocking, 1 piece of 14' на bathroom |
