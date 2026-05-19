# Porch / Deck / Balcony

Porch, deck и balcony — часть **exterior scope**. Это хаб: ниже — porch trim,
дальше ссылки на полные страницы по rails/decking, balcony build-up и
shower/pergola.

!!! note "Включать всегда"
    Эти элементы легко забыть — они не на «main wall» elevation. Каждый
    porch / deck / balcony проходи отдельно по своим sections.

<div class="grid cards" markdown>

-   :material-fence:{ .lg .middle } **Rails & Decking** — railing-системы,
    decking, post hardware, ballusters, lattice, skirt.
    [:octicons-arrow-right-24: открыть](rails-decking.md)

-   :material-layers-triple:{ .lg .middle } **Balcony build-up** — полная
    сборка от posts до soffit/trim + composition by others.
    [:octicons-arrow-right-24: открыть](balcony-buildup.md)

-   :material-shower:{ .lg .middle } **Shower & Pergola** — privacy/shower
    screen, pergola, trellis, canopy.
    [:octicons-arrow-right-24: открыть](shower-pergola.md)

</div>

## Porch trims { .kb-section-title .kb-st--green }

| Label | Типовой size | Unit | Заметка |
| --- | --- | --- | --- |
| `Fascia Trim at Hdr outside` | `1x8` / `1x10` / `1x12` | `LFT` | по header снаружи |
| `Fascia Trim at Hdr inside` | `1x12` | `LFT` | по header изнутри |
| `Soffit Trim at Hdr` | `1x4` / `1x6` / `1x12` | `LFT` | |
| `Fascia Trim at House wall` | `5/4x6` / `5/4x12` | `LFT` | примыкание к дому |
| `Soffits at Porch` | `Beadboard` / `Beadboard Vinyl` | `SQ FT` | потолок крыльца |
| `Frieze inside` | `5/4x12` | `LFT` | |
| `Crowns outside` / `Crowns inside` | `3-1/2" crown` | `LFT` | часто `scaled` |
| `Columns` | `10"–12" Dia Fbg`, `SQ Fluted`, `Poly-Classic` | `pcs` + высота | см. [Soffit & Fascia](soffit-fascia.md) |
| `Column wrap` | `1x8` | `LFT` | обшивка стойки |
| `Posts at Rails` | `4x4 PT` | `pcs` + `4'` | + sleeve + cap → [Rails & Decking](rails-decking.md) |
| `Porch deck Fascia` | `1x10` | `LFT` | |

- Porch soffit обычно `Beadboard` в `SQ FT` (площадь потолка крыльца).
- Нет деталей → `Note: No Details provided; all trims are assumed per
  elevations` — все строки с `assumed`.

## Flare / shingled bump { .kb-section-title .kb-st--cyan }

Flare (расширение стены книзу с shingle) — отдельный набор trim + blocking:

<figure markdown>
  ![Flare detail section](../../assets/images/trims/ext-flare-detail.png)
  <figcaption>Flare: 2x blocking (rip as req'd), crown molding, 5/4x10 trim с drip-edge router cut, cedar shingles.</figcaption>
</figure>

| Label | Size | Unit |
| --- | --- | --- |
| `Blocking (plates double)` / `(studs double)` | `2x6` | `LFT` |
| `Trims` | `5/4x10` | `LFT` |
| `Crowns` | `2" Crowns` | `LFT` |
| `Flare Sheathing` | `1/2" CDX Ply` | `4x8` |
| `Vapor Barrier` | `Tyvek` | `SQ FT` |

## Чек перед выводом { .kb-section-title .kb-st--magenta }

- [ ] Каждый porch / deck / balcony пройден отдельно по своим sections?
- [ ] Porch: fascia (outside/inside) + soffit at hdr + porch soffit (SQ FT)?
- [ ] Columns с типом/taper/`w/c&b` и высотой; column wrap отдельно?
- [ ] Deck/rail — посчитан по [Rails & Decking](rails-decking.md)?
- [ ] Balcony — собран по [Balcony build-up](balcony-buildup.md)?
- [ ] Flare: blocking + trim + crown + sheathing + vapor barrier?

## See also

- [Rails & Decking](rails-decking.md) · [Balcony build-up](balcony-buildup.md) · [Shower & Pergola](shower-pergola.md)
- [Soffit & Fascia](soffit-fascia.md) · [Overview](overview.md)
- [Balcony Trims](../deck/balcony-trims.md) · [Railing](../deck/railing.md)
- [Porch SQFT](../sqfts/porch.md) · [Deck SQFT](../sqfts/deck.md) · [Balcony SQFT](../sqfts/balcony.md)
