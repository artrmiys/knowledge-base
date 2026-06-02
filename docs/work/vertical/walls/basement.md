# Basement Walls

<figure markdown>
  ![Basement wall on concrete slab](../../../assets/images/sqfts/basement.svg)
  <figcaption>Цокольная стена на бетоне: btm plate всегда P.T.; box sheathing + vapor barrier.</figcaption>
</figure>

Если basement walls in scope — это полноценная stick-стена, а не только
обшивка по площади. Площадь basement-этажа считается отдельно в
[Basement SQFT](../../sqfts/basement.md); здесь — состав каркаса.

## Что считать

- Studs, plates, blocking, double top plates по высоте стены.
- Box sheathing (OSB), vapor barrier (Tyvek).
- Window / sill flashing в проёмах цокольной стены.
- Corridor-строки внутри подвала (если есть).

## Критические правила

- **Btm-plate цокольной стены всегда `P.T.`** — садится на бетон (контакт с
  влажным основанием), как и у [Sill Plates](sill-plates.md).
- Studs — размер авто по высоте (nested-IF), как на full-frame уровнях.
- Corridor в подвале: `2x6 P.T.` / `LSL P.T.` для btm.
- **Steel / Mtl walls** встречаются — тогда framing by others, но обшивка
  (box sheathing), vapor barrier и flashing остаются нашими (как в
  [Exterior Walls → Metal stud / CMU](exterior.md)).

## Типовой состав строки { .kb-section-title .kb-st--green }

| Строка | Заметка |
| --- | --- |
| **Plates Interior btm** | **всегда `P.T.`** (садится на бетон) |
| **Studs Interior** | размер авто по высоте (nested-IF) |
| Blocking | `2x` |
| Plates dbl top | |
| Plates / Studs Corridor | `2x6 P.T.` / `LSL P.T.` btm |
| Vapor Barrier | Tyvek |
| Box Sheathing | OSB |
| Window / Sill Flashing | проёмы в bsmt-стене |

## See also

- [Sill Plates](sill-plates.md) · [Exterior Walls](exterior.md) · [Corridor Walls](corridor.md)
- [Box Sheathing](../sheathing/box-sheathing.md)
- [Basement SQFT](../../sqfts/basement.md) — площадь basement-этажа
