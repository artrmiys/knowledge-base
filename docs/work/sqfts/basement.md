# Basement SQFT

## Что считать

- Basement floor/wall areas that drive sheathing, sleepers, insulation, or
  finish assemblies.

## Проверить

- Basement SQFT plywood and sleepers are easy to skip.
- Under slab / over slab assemblies всё ещё могут требовать underlayment.
- Existing/podium conditions нельзя считать standard panels без
  checking details.

## Basement как каркасная стена (corpus) { .kb-section-title .kb-st--green }

Если basement walls in scope — это полноценная stick-стена. Типовой состав по
корпусу (33 файла, `%` = в скольки basement-секциях):

| Строка | % | Заметка |
| --- | ---: | --- |
| **Plates Interior btm** | 67% | **всегда `P.T.`** (садится на бетон) |
| **Studs Interior** | 67% | размер авто по высоте (nested-IF) |
| Blocking | 79% | `2x` |
| Plates dbl top | 55% | |
| Plates / Studs Corridor | 30% | `2x6 P.T.` / `LSL P.T.` btm |
| Vapor Barrier | 27% | Tyvek / `=O4` |
| Box Sheathing | 24% | OSB |
| Window / Sill Flashing | 58% / 36% | проёмы в bsmt-стене |

→ Ключевое: **btm-plate цокольной стены всегда P.T.** (контакт с бетоном) — как и
у [Sill Plates](../vertical/walls/sill-plates.md). Стальной каркас (Steel/Mtl Walls)
встречается — тогда framing by others, но обшивка/изоляция наши.
