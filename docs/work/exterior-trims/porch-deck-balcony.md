# Porch / Deck / Balcony (отделка крылец, deck и балконов)

Хаб по отделке открытых площадок. Каркас считается на
[Deck / Porch / Balcony Frame](../deck/deck-porch-balcony-frame.md), здесь
то, что сверху и снаружи: porch trims, перила и настил, слои балкона,
shower screen и pergola.

!!! note "Включать всегда"
    Эти элементы не видны на основных фасадах, их легко забыть. Каждый
    porch, deck и balcony проходи отдельно по своим разрезам и деталям.
    Отделку вставляй только когда она в scope; при Frame only не вставляй.

<div class="grid cards" markdown>

-   :material-fence:{ .lg .middle } **Rails & Decking** - перила по типам
    (composite система, wood поэлементно, metal by others), decking,
    hardware постов, lattice, skirt.
    [открыть](rails-decking.md)

-   :material-layers-triple:{ .lg .middle } **Balcony build-up** - все слои
    балкона, finish-строки 7-12, composition с pavers.
    [открыть](balcony-buildup.md)

-   :material-shower:{ .lg .middle } **Shower & Pergola** - privacy screen,
    pergola, trellis, canopy.
    [открыть](shower-pergola.md)

</div>

## Порядок работы

1. На планах и фасадах найди каждый porch, deck и balcony, определи тип
   и число экземпляров (см. блоки на странице каркаса).
2. Открой разрез и детали каждого: что показано (fascia, soffit, columns,
   перила), какой материал.
3. Для каждого блока после строк каркаса добавь строки отделки с
   множителем G блока. Размер не указан: `TBD` и нота.

## Porch trims

<figure markdown>
  ![Потолок крыльца: подшивка досками, кронштейны и колонны](../../assets/images/photos/trims/porch-ceiling-beadboard-columns.jpg){ width="360" }
  <figcaption markdown="span">Потолок porch снизу: подшивка досками (строка `Soffits at Porch`, SQ FT), по краю fascia (`Fascia Trim at Hdr outside`), декоративные кронштейны и обшитые колонны. Каждый элемент считается отдельной строкой с множителем блока. Фото: hbelementsinc.com, [источник](https://www.hbelementsinc.com/portfolio/soffit-ceilings/), найдено через Pinterest.</figcaption>
</figure>

| Строка DFL | Типовой size | Unit | Заметка |
| --- | --- | --- | --- |
| `Fascia Trim at Hdr outside` | `1x8` / `1x10` / `1x12` | LFT | по header снаружи |
| `Fascia Trim at Hdr inside` | `1x12` | LFT | по header изнутри |
| `Soffit Trim at Hdr` | `1x4` / `1x6` / `1x12` | LFT | |
| `Fascia Trim at House wall` | `5/4x6` / `5/4x12` | LFT | примыкание к дому |
| `Soffits at Porch` | `Beadboard` / `Beadboard Vinyl` | SQ FT | потолок крыльца, `=CEILING(W*D*1.1,10)*units` |
| `Frieze inside` | `5/4x12` | LFT | |
| `Crowns` | `3-1/2" crown` | LFT | снаружи и изнутри отдельными строками; часто `scaled` |
| `Columns` | `10"-12" Dia Fbg`, `SQ Fluted` | высота колонны (`8'`), C = штуки | круглые и декоративные колонны, см. [Soffit & Fascia](soffit-fascia.md) |
| `Post Wrap` | `1x8` (пост 6x6), `1x6` (пост 4x4) | LFT | обшивка стойки досками: G = высота x 4 стороны x число стоек, C = G x 1.1 вверх до 10 (меньше 50 - до 2) |
| `Posts at Rails` | `4x4 P.T.` | `4` (длина поста), C = штуки | плюс sleeve и cap, см. [Rails & Decking](rails-decking.md) |
| `Deck Fascia` | `1x8`, по детали `1x12 Azek` | LFT | открытые кромки настила одного блока x units |

- `Post Wrap` считается в LFT досок, не штуками: четыре доски на стойку на
  всю её высоту. Стойка 8' даёт 8 x 4 = 32 LFT, четыре такие стойки 128 LFT,
  с waste 128 x 1.1 = 140.8, вверх до 10 = 150 LFT. В блоке porch G берётся на один
  porch и формула умножается на units.
- Потолок porch в scope каркаса: одна строка `Soffit Gypsum (2)`, SQ FT,
  `=CEILING(area*2*1.1,2)*units`: два слоя стоят в подписи и один раз в
  формуле, см. [каркас](../deck/deck-porch-balcony-frame.md). Beadboard
  это отделка поверх.
- Нет деталей: `Note: No Details provided; all trims are assumed per
  elevations`, все строки с `assumed`.

<figure markdown>
  ![Отделка porch в разрезе](../../assets/images/trims/porch-trims.svg)
  <figcaption markdown="span">Разрез porch header: fascia trim снаружи и внутри, soffit trim, frieze, crown, beadboard soffit (SQ FT), обшивка колонны.</figcaption>
</figure>

## Flare / shingled bump

Расширение стены книзу под shingle: свой набор blocking и trim.

<figure markdown>
  ![Flare detail section](../../assets/images/trims/ext-flare-detail.png)
  <figcaption markdown="span">Flare: 2x blocking (rip as req'd), crown, 5/4x10 trim с drip-edge, cedar shingles. Обшивка и WRB flare идут в свои строки.</figcaption>
</figure>

| Строка DFL | Size | Unit |
| --- | --- | --- |
| `Blocking (plates double)` / `(studs double)` | `2x6` | LFT |
| `Trims` | `5/4x10` | LFT |
| `Crowns` | `2" Crowns` | LFT |
| `Flare Sheathing` | `1/2" CDX Ply` | 4x8 |
| `Vapor Barrier` (подпись шаблона) | WRB по спецификации стены | SQ FT |

## Частые ошибки

- Porch SQFT на Front Page не заполнен, когда porch стоит стопкой с балконом.
- Canopy и porch посчитаны повторно в eve и rake.
- Отделка вставлена при scope Frame only.
- Columns без типа и высоты; `Post Wrap` перепутан с column или посчитан штуками.
- Все ошибки раздела: [Deck, porch, балконы](../../start/common-mistakes.md#deck).

## См. также

- [Rails & Decking](rails-decking.md), [Balcony build-up](balcony-buildup.md), [Shower & Pergola](shower-pergola.md)
- [Soffit & Fascia](soffit-fascia.md), [Overview](overview.md)
- [Deck / Porch / Balcony Frame](../deck/deck-porch-balcony-frame.md), [Balcony Trims](../deck/balcony-trims.md), [Railing](../deck/railing.md)
- [Porch SQFT](../sqfts/porch.md), [Deck SQFT](../sqfts/deck.md), [Balcony SQFT](../sqfts/balcony.md)
