# Shaft Walls

**Shaft wall** — это стена шахты, ограждение **вертикальных шахт** в здании. На чертежах под `shaft wall` обычно понимают:

- **elevator shaft** — шахты лифтов;
- **vent shaft** — вентиляционные каналы;
- **trash chute** — мусоропроводы;
- **mechanical/communications shafts** — pipes, cables, ducts.

Shaft wall почти всегда fire-rated и собирается из CH-stud + shaft liner.

## Что считать

- CH studs.
- J-channels.
- 1" liner panels.
- Fire-wall hanger conditions, когда joists hang over shaft walls.

## Default assumption

Когда иначе не specified, notes часто используют:

| Item | Typical |
| --- | --- |
| Studs | 2-1/2" CH studs |
| Tracks | 2-1/2" J-channel |
| Liner | 1" liner panel |

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
    - Shaft (противопожарные стены): [5 карт. Confluence](https://redacted.atlassian.net/wiki/spaces/work/pages/65306667/Shaft)

<details class="kb-figures">
  <summary>Показать ещё 3 иллюстрации</summary>
  <div class="kb-figure-grid">
    <a class="kb-figure" href="../../../../assets/images/confluence/confluence-130.png" target="_blank" rel="noopener"><img src="../../../../assets/images/confluence/confluence-130.png" alt="Shaft / fire wall узел 02" loading="lazy"></a>
    <a class="kb-figure" href="../../../../assets/images/confluence/confluence-132.png" target="_blank" rel="noopener"><img src="../../../../assets/images/confluence/confluence-132.png" alt="Shaft / fire wall узел 04" loading="lazy"></a>
    <a class="kb-figure" href="../../../../assets/images/confluence/confluence-133.png" target="_blank" rel="noopener"><img src="../../../../assets/images/confluence/confluence-133.png" alt="Shaft / fire wall узел 05" loading="lazy"></a>
  </div>
</details>
<!-- confluence-gallery:end -->
