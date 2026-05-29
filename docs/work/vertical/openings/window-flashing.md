# Window Flashing & Sill

Гидроизоляция вокруг проёмов окон и дверей. Это **наш scope** (даже когда
каркас стены by others) и **отдельные строки** в takeoff от тех, что считаются
для крыши / стен. Для roof / wall / deck flashing — отдельная страница
[Flashing](../../sheathing-and-misc/flashing.md).

!!! tip "Считается автоматом из Openings"
    Когда заполнены **Windows / Doors openings** (с пометкой `d` у дверей,
    `gd` у гаражных) — макрос **`F_Openings`** автоматически выдаёт
    `Window Flashing` + `Sill Flashing` по правилам ниже. Руками длины
    не набивай: задача — корректно проставить **тип** (окно / дверь) и
    **размеры**, LFT макрос соберёт сам. Подробно про пометки и макрос —
    [Windows and Doors](windows-doors.md).

## Window Flashing vs Sill Flashing { .kb-section-title .kb-st--cyan }

Вокруг каждого окна на наружной стене у нас **две разные позиции**, и их легко
спутать. Считаются они **разной длиной**.

<div class="kb-split" markdown>

- **Window Flashing** — лента/мембрана **по 3 сторонам** проёма: левый jamb,
  правый jamb, head (верх). «Обвязка» по периметру — отводит воду в обход
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
    у двери — **threshold / door sill detail**, не pan. Поэтому у дверей
    обязательно ставится пометка `d` (у гаражных `gd`) — макрос `F_Openings`
    по этой пометке **не выдаёт Sill Flashing** для двери. Если по двери
    случайно появилась строка `Sill Flashing` — значит пометка `d` не
    проставлена, ищи на плане. Подробно про пометки — [Windows and Doors](windows-doors.md).

### Как считать (LFT)

| Позиция | По чему длина | Формула |
| --- | --- | --- |
| `Window Flashing` | 2× height + width окна (3 стороны) | `(2*H + W) * qty` |
| `Sill Flashing` | ширина окна по низу | `W * qty` |
| `Door Flashing` (3 sides) | 2× height + width двери | `(2*H + W) * qty` |
| `Door Sill Flashing` | ❌ не считаем | — |

- Размеры окон/дверей — из window/door schedule, **не** из elevation «на глаз».
- 3 sides = `Window Flashing`, bottom = `Sill Flashing` — это **две строки**,
  не объединяй.

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
  [Exterior Wall Materials](../sheathing/exterior-materials.md).
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
    [Furring & Window Jambs](../../exterior-trims/furring-and-jambs.md).

## Проверить { .kb-section-title .kb-st--magenta }

- [ ] Window Flashing = 3 стороны (`2H + W`), Sill Flashing = низ (`W`).
- [ ] У дверей **нет** `Sill Flashing` — только 3 стороны.
- [ ] Wood / Mtl / CMU walls — каждая своя строка, не слиты.
- [ ] На CMU / concrete проверил, нужен ли `Window Jamb 1x4` или `2x4` P.T.
- [ ] Openings промечены: окна без пометки, двери `d`, гаражные `gd`.

## See also

- [Windows and Doors](windows-doors.md) — типы, подписи, пометки `d` / `gd`,
  макрос `F_Openings`.
- [Exterior Wall Materials](../sheathing/exterior-materials.md)
- [Furring & Window Jambs](../../exterior-trims/furring-and-jambs.md)
- [Flashing (roof / wall / deck)](../../sheathing-and-misc/flashing.md) — это
  **другой** flashing, не путать.
- Внешние источники по детали flashing:
  [BASC / PNNL — Windows and Doors are Fully Flashed](https://basc.pnnl.gov/resource-guides/windows-and-doors-are-fully-flashed),
  [Building Science Corp — Pan Flashing for Exterior Wall Openings](https://buildingscience.com/documents/information-sheets/pan-flashing-for-exterior-wall-openings),
  [NAHB TechNote — Window and Door Flashing](https://www.homeinnovation.com/documents/Reports/TechNote-Window-and-Door-Flashing.pdf).
