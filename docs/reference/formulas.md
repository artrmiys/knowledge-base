# Формулы и факторы

## Joist / Stud spacing factors

| Spacing | Фактор |
| --- | ---: |
| 12" o.c. | 1.4667 |
| 16" o.c. | 1.1 |
| 24" o.c. | 0.625 |

Для studs at 16" o.c. boss feedback говорит использовать 1:1 плюс 10% waste,
а не 0.75. Для 24" o.c. используй 0.5 плюс 25% waste.

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
