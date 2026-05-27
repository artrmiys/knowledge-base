# Flashing

## Что считать

- Exterior opening flashing, wall/roof flashing, deck/balcony flashing, and
  related jamb logic.

## Правила

- Exterior door/window jamb quantities can use flashing-style formulas.
- Если template разделяет trims и flashing, держи их отдельно.

## Flashing по типам стен

Flashing вокруг openings разделяют **по типу стены** — у metal / CMU / wood
walls разные detail и quantities:

| Строка в takeoff | Материал | Unit |
| --- | --- | --- |
| `Window Flashing` | `Flashing Tape` | `LFT` |
| `Sill Flashing` | `Sill Flashing` | `LFT` |
| `Window Flashing at Mtl Walls` | `Flashing Tape` | `LFT` |
| `Sill Flashing at Mtl Walls` | `Sill Flashing` | `LFT` |
| `Window Flashing at CMU Walls` | `Flashing Tape` | `LFT` |

- Не объединяй Mtl / CMU / wood walls в одну строку.
- Полный блок наружных материалов — [Exterior Wall Materials](../vertical/sheathing/exterior-materials.md).

## Проверить

- Rake/eve/parapet trim и flashing могут быть called out на architectural sheets,
  not structural.
