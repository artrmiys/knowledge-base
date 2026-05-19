# Измерение siding

Siding считается по **площади** (`SQ FT` / `SF`) по elevations, стена за
стеной. Trim, accessories и flashing — отдельно (`LFT`/`pcs`), не в siding.

## Метод { .kb-section-title .kb-st--green }

1. Иди **по elevations**, стена за стеной (front / rear / left / right).
2. Площадь = ширина × высота стены, минус то, что вычитается по правилу
   проекта/клиента.
3. **Gables, dormers, bays, return walls** — отдельные площади (часто
   отдельные строки, особенно если материал другой).
4. Сумму веди формулой в Excel (видимые слагаемые), не «голым» числом.

| Label | Value | Unit |
| --- | --- | --- |
| `Siding` | `=L+R+Front+Rear …` | `SQ FT` |
| `Siding Gable front` | `=…` | `SQ FT` |
| `Siding` (offset / correction) | `-140` | `SQ FT` |

## Deductions { .kb-section-title .kb-st--cyan }

- Крупные openings (garage, большие окна/двери, проёмы) вычитаются — или
  считается gross + waste, **по правилу клиента**. Не смешивай два подхода
  на одном объекте.
- Маленькие окна часто **не** вычитают (уходит в waste) — но следуй client
  rule / Boss feedback.
- Deduction показывай **видимой** строкой/слагаемым (в воркбуке встречаются
  отрицательные строки, напр. `-140 SQ FT` — это нормально и наглядно).

!!! tip "Gross vs net"
    Если правило проекта неизвестно — спрашивай, не угадывай. Зафиксируй note
    `Siding gross, openings not deducted` или `net of large openings`.
    См. [Правила клиентов](../../start/client-rules.md).

## Waste { .kb-section-title .kb-st--magenta }

- Lap / clapboard — умеренный waste (зависит от exposure).
- **Shingle / shake — waste выше**, чем у lap.
- Diagonal / pattern / small gables — больше обрезков.
- Waste-фактор применяй по [Формулам и факторам](../../reference/formulas.md);
  держи его видимым множителем (макрос ×-ячейки — см.
  [Trim macros](../exterior-trims/macros.md)).

## By others / TBD дисциплина { .kb-section-title .kb-st--green }

- Siding by others → строка `Siding | <material> | 0 | SQ FT` + note
  (`by others` / `by customer`).
- Материал не указан → `Per customer TBD` / `verify material` в note, не
  подставляй продукт.
- EIFS / stucco / stone / brick → не считаем (см.
  [EIFS / Stucco / Veneer](eifs-stucco-veneer.md)), но trim/furring/WRB
  проверяем.

## Что НЕ входит в siding SQ FT { .kb-section-title .kb-st--cyan }

Считается **отдельно**, не в площади siding:

- Casing / corner / band / watertable — `LFT` ([Casing, Corner & Band](../exterior-trims/casing-corner-band.md)).
- Soffit / fascia / frieze — ([Soffit & Fascia](../exterior-trims/soffit-fascia.md)).
- Starter / J-channel / corners / undersill — accessories `LFT`
  ([Underlayment](underlayment.md)).
- WRB, furring, Cedar Breather, flashing — свои строки.

## Чек перед выводом { .kb-section-title .kb-st--magenta }

- [ ] Площадь по elevations, стена за стеной, формулой?
- [ ] Gables / dormers / bays / returns — отдельными площадями?
- [ ] Deductions по одному правилу (gross **или** net), видимо?
- [ ] Waste-фактор применён (выше для shingle), виден множителем?
- [ ] By others / TBD → `0` + note, без угадывания продукта?
- [ ] Trim / accessories / flashing вынесены из siding SQ FT?

## See also

- [Overview](overview.md) · [Типы siding](types.md) · [Underlayment](underlayment.md) · [EIFS / Stucco / Veneer](eifs-stucco-veneer.md)
- [Формулы и факторы](../../reference/formulas.md) · [Правила клиентов](../../start/client-rules.md)
- [Trim macros](../exterior-trims/macros.md)
