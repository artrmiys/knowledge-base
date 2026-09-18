# Shaft Walls

**Shaft wall** — это стена шахты, ограждение **вертикальных шахт** в здании. На чертежах под `shaft wall` обычно понимают:

- **elevator shaft** — шахты лифтов;
- **vent shaft** — вентиляционные каналы;
- **trash chute** — мусоропроводы;
- **mechanical/communications shafts** — pipes, cables, ducts.

Shaft wall почти всегда fire-rated. На takeoff/DFL обычно встречаются два рабочих типа:
`2-1/2" CH + J-channel` или `2" H + C-channel`. Размер и тип всегда бери из wall type/detail.

## Что считать

- CH studs.
- J-channels.
- 1" liner panels.
- Fire-wall hanger conditions, когда joists hang over shaft walls.
- Для `2"` H/C assemblies: H-channels vertical/horizontal и C-channels perimeter.
- Shaft walls не пропускай как "панели by others" автоматически: если wall type/detail дает shaft assembly,
  отрази его отдельными строками в takeoff/DFL.

## Two common shaft-wall types

Если detail/wall type прямо не уточняет другое, сначала проверь эти два типовых варианта.
Не смешивай их в один блок: у них разные channels и разные формулы для panels/horizontal rows.

### Type 1: 2-1/2" CH + J-channel

Обычно для CH-stud shaft wall assembly с 1" shaftliner:

| Item | Typical |
| --- | --- |
| Studs | 2-1/2" CH studs |
| Horizontal tracks/channels | 2-1/2" J-channel |
| Liner | 1" liner panel |

DFL rows:

| Row | Material | Takeoff unit/source | Formula pattern | Stock |
| --- | --- | --- | --- | --- |
| Linear Panels | 1" Shaft Panels | LFT | `CEILING((LFT * 1.1 / 24), 2)` | 12, listed as 2x12 Panels |
| CH Channels Vertical | 2-1/2" CH-channels | LFT | `CEILING((LFT * 0.5 * 1.1 / Stock LF), 2)` | 12 |
| J Channels Horizontal | 2-1/2" J-channels | Horizontal LFT | `CEILING((Horizontal LFT * 1.1 / Stock LF), 2)` | 12 |

### Type 2: 2" H + C-channel

Обычно для H-channel shaft wall assembly, где detail требует H-channels и perimeter C-channel:

| Item | Typical |
| --- | --- |
| Vertical channels | 2" H-channels |
| Horizontal channels | 2" H-channels |
| Perimeter channels | 2" C-channels |
| Liner | 1" shaft panel |

DFL rows:

| Row | Material | Takeoff unit/source | Formula pattern | Stock |
| --- | --- | --- | --- | --- |
| Linear Panels | 1" Shaft Panels | LFT | `CEILING((LFT * 2 * 1.1 / 24), 2)` | 12, listed as 2x12 Panels |
| Channels Vertical | 2" H-channels | LFT | `CEILING((LFT * 0.5 * 1.1 / Stock LF), 2)` | 12 |
| Channels Horizontal | 2" H-channels | Horizontal LFT | `CEILING((Horizontal LFT * 2 * 1.1 / Stock LF), 2)` | 12 |
| Channels Perimeter | 2" C-channels | Perimeter LFT | `CEILING((Perimeter LFT * 1.1 / Stock LF), 2)` | 12 |

`Stock LF` is the stock length cell, usually `12`. Use the measured LFT source that matches the row:
overall shaft-wall LFT, horizontal run LFT, or perimeter LFT.

<figure markdown>
  ![C-T stud, J-track and J-L corner profiles with dimensions](../../../assets/images/confluence/confluence-129.png)
  <figcaption>Профили shaft wall: <strong>C-T (CH) stud</strong> (`2-1/2"/4"/6"`, полка `1-5/8"`), <strong>J-track</strong> и <strong>J-L corner</strong>. Размер studs/tracks бери из wall type.</figcaption>
</figure>

<figure markdown>
  ![1 inch gypsum shaftliner panel](../../../assets/images/confluence/confluence-131.png)
  <figcaption><strong>1" shaftliner</strong> — гипсовая панель-вкладыш в J-track между CH-studs. Отдельная строка.</figcaption>
</figure>

!!! note "Формулы shaft wall"
    CH-channels, J-channels и liner-панели считаются по формулам в
    [Формулы → Shaft Walls](../../../reference/formulas.md#shaft-walls).

## Проверить

- Chute Shaft wall A201/A806, wall type 7A — recurring miss.
- DHU/DGU hanger conditions относятся сюда, когда joists hang over the firewall.
- Shaft hangers помечай отдельно by floor для review.
- Typical shaft details сами по себе недостаточны; найди реальный shaft location
  на plans. Начни с trash/vent/mechanical shafts, потом проверь referenced detail.
- Если wall type показывает shaft assembly, но plan calls out только resilient
  channel, считай resilient channel condition отдельно вместо full shaft-wall quantity.
- `7/8"` resilient channel может быть ceiling/strapping item и применяться на
  всех levels, минус dropped metal-frame areas; проверь RCP/ceiling notes.

## See also

- [Формулы → Shaft Walls](../../../reference/formulas.md#shaft-walls) · [Demising Walls](demising.md) · [Hangers](../../../reference/hangers.md)

<!-- confluence-gallery:start -->
## Ещё примеры (shaft / fire wall)

??? info "Источник картинок"
    - Shaft (противопожарные стены): 5 карт. Confluence (архивный источник; ссылка не публикуется)

<details class="kb-figures">
  <summary>Показать ещё 3 иллюстрации</summary>
  <div class="kb-figure-grid">
    <a class="kb-figure" href="../../../../assets/images/confluence/confluence-130.png" target="_blank" rel="noopener"><img src="../../../../assets/images/confluence/confluence-130.png" alt="Shaft / fire wall узел 02" loading="lazy"></a>
    <a class="kb-figure" href="../../../../assets/images/confluence/confluence-132.png" target="_blank" rel="noopener"><img src="../../../../assets/images/confluence/confluence-132.png" alt="Shaft / fire wall узел 04" loading="lazy"></a>
    <a class="kb-figure" href="../../../../assets/images/confluence/confluence-133.png" target="_blank" rel="noopener"><img src="../../../../assets/images/confluence/confluence-133.png" alt="Shaft / fire wall узел 05" loading="lazy"></a>
  </div>
</details>
<!-- confluence-gallery:end -->
