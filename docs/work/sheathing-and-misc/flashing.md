# Flashing

## Что считать

- Exterior opening flashing, wall/roof flashing, deck/balcony flashing, and
  related jamb logic.

## Правила

- Exterior door/window jamb quantities can use flashing-style formulas.
- Если template разделяет trims и flashing, держи их отдельно.

## Window Flashing vs Sill Flashing { .kb-section-title .kb-st--cyan }

Вокруг каждого окна на наружной стене у нас **две разные позиции**, и их легко
спутать. Это не «одно и то же», и считаются они **разной длиной**.

!!! tip "Это считается автоматом из Openings"
    Когда заполняешь **Windows / Doors openings** (с пометкой `d` у дверей,
    `gd` у гаражных) — макрос **`F_Openings`** автоматически выдаёт
    `Window Flashing` + `Sill Flashing` по правилам ниже. Руками длину не
    набивай: проверь, что в openings проставлены **типы и размеры**, прогон
    макроса соберёт LFT сам. Подробно про макрос и пометки —
    [Windows and Doors](../vertical/openings/windows-doors.md).

<div class="kb-split" markdown>

- **Window Flashing** — лента/мембрана **по 3 сторонам** проёма: левый jamb,
  правый jamb, head (верх). Это «обвязка» по периметру — отводит воду в обход
  рамы и интегрируется с WRB.
- **Sill Flashing (Sill Pan)** — **только низ** проёма, форма «корытца» с
  поднятыми бортиками: задний борт + два боковых борта + передний слив. Ловит
  всё, что просочилось внутрь, и сливает наружу. Это **не одна линия по низу** —
  это pan, но считается LFT по ширине sill.
- Sides + head = Window Flashing. Bottom = Sill Flashing. Это **две строки** в
  takeoff, не объединяй.

<figure markdown>
  ![Pan flashing installed at window rough sill](https://basc.pnnl.gov/sites/default/files/styles/node_page/public/DSC00934%20copy.jpg)
  <figcaption>Sill pan на rough sill — «корытце» с задним и боковыми бортами. Источник: <a href="https://basc.pnnl.gov/resource-guides/windows-and-doors-are-fully-flashed">BASC / PNNL (US DOE)</a>.</figcaption>
</figure>

</div>

<figure markdown>
  ![Window flashed on three sides — head and both jambs over the flange](https://basc.pnnl.gov/sites/default/files/styles/node_page/public/images/WM213_flashwindow5_PNNL20139_04-21-12.jpg)
  <figcaption>Window flashing — head + 2 jambs (3 стороны) поверх flange окна, интегрировано с WRB / foam sheathing. Источник: <a href="https://basc.pnnl.gov/resource-guides/windows-and-doors-are-fully-flashed">BASC / PNNL</a>.</figcaption>
</figure>

!!! danger "У дверей sill flashing НЕТ"
    Двери получают flashing **только по 3 сторонам** (head + 2 jambs). Снизу
    у двери — **threshold / door sill detail**, не pan. Не вписывай `Sill
    Flashing` для doors — даже если openings macro подтягивает периметр 4
    сторон, sill-строку по дверям руками **обнуляй / убирай**.

### Как считать (LFT)

| Позиция | По чему длина | Формула |
| --- | --- | --- |
| `Window Flashing` | 2× height + width окна (3 стороны) | `(2*H + W) * qty` |
| `Sill Flashing` | ширина окна по низу | `W * qty` |
| `Door Flashing` (3 sides) | 2× height + width двери | `(2*H + W) * qty` |
| `Door Sill Flashing` | ❌ не считаем | — |

- Размеры окон/дверей — из window/door schedule, **не** из elevation «на глаз».
- Если openings macro собирает периметр 4 сторон, **раздели на 2 строки**:
  3 sides → Window Flashing, bottom → Sill Flashing.

## Flashing по типам стен { .kb-section-title .kb-st--green }

Flashing вокруг openings разделяют **по типу стены** — у metal / CMU / wood
walls разные detail и quantities. Wood walls — это **default**, а Mtl и
CMU/concrete добавляются **опционально, отдельными строками**, даже если
detail одинаковый по геометрии.

| Строка в takeoff | Материал | Unit |
| --- | --- | --- |
| `Window Flashing` | `Flashing Tape` | `LFT` |
| `Sill Flashing` | `Sill Flashing` | `LFT` |
| `Window Flashing at Mtl Walls` | `Flashing Tape` | `LFT` |
| `Sill Flashing at Mtl Walls` | `Sill Flashing` | `LFT` |
| `Window Flashing at CMU Walls` | `Flashing Tape` | `LFT` |
| `Sill Flashing at CMU Walls` | `Sill Flashing` | `LFT` |

- **Не объединяй** Mtl / CMU / wood walls в одну строку — у клиента это
  обычно разные подрядчики / разные WRB-системы.
- **Wood walls** — базовая строка идёт всегда, если есть окна на wood-каркасе.
- **Mtl stud walls** — добавляем опционально (по wall type schedule); flashing
  наш, даже если studs by others. См.
  [Exterior Wall Materials](../vertical/sheathing/exterior-materials.md).
- **CMU / Concrete walls** — добавляем опционально отдельным блоком. Часто
  flashing нужно прибить, поэтому смотри jamb ниже.

!!! tip "Concrete / CMU → возможно нужен wood jamb P.T."
    На бетонной / CMU стене у flashing нет nailing-плоскости. Часто в детали
    окна пишут **деревянный jamb** `1x4 P.T.` или `2x4 P.T.` по периметру
    проёма — к нему уже крепится flashing tape и (потом) casing.

    | Строка | Материал | Unit |
    | --- | --- | --- |
    | `Window Jamb at CMU/Concrete` | `1x4 P.T.` или `2x4 P.T.` | `LFT` |

    Бери size из window detail (тонкая стена → `1x4`, толще → `2x4`). Это
    отдельная строка от flashing — flashing считается даже без jamb, jamb
    добавляется когда деталь его показывает. Подробнее про jamb-логику —
    [Furring & Window Jambs](../exterior-trims/furring-and-jambs.md).

## Проверить { .kb-section-title .kb-st--magenta }

- [ ] Window Flashing = 3 стороны (`2H + W`), Sill Flashing = низ (`W`).
- [ ] У дверей **нет** `Sill Flashing` — только 3 стороны.
- [ ] Wood / Mtl / CMU walls — каждая своя строка, не слиты.
- [ ] На CMU / concrete проверил, нужен ли `Window Jamb 1x4` или `2x4` P.T.
- [ ] Rake/eve/parapet trim и flashing могут быть called out на architectural
      sheets, not structural — открыл и тот, и другой набор листов.

## See also

- [Exterior Wall Materials](../vertical/sheathing/exterior-materials.md)
- [Furring & Window Jambs](../exterior-trims/furring-and-jambs.md)
- [Windows and Doors](../vertical/openings/windows-doors.md)
- Внешние источники по детали flashing:
  [BASC / PNNL — Windows and Doors are Fully Flashed](https://basc.pnnl.gov/resource-guides/windows-and-doors-are-fully-flashed),
  [Building Science Corp — Pan Flashing for Exterior Wall Openings](https://buildingscience.com/documents/information-sheets/pan-flashing-for-exterior-wall-openings),
  [NAHB TechNote — Window and Door Flashing](https://www.homeinnovation.com/documents/Reports/TechNote-Window-and-Door-Flashing.pdf).
