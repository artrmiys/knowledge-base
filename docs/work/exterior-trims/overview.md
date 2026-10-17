# Exterior Trims (наружная отделка)

Exterior Trims это wood, PVC или composite погонаж и изделия снаружи
здания: casing вокруг проёмов, corner boards, band и watertable, head
crowns, soffit и fascia, frieze, columns, отделка porch, deck и balcony.
Это отдельный scope: не siding, не EIFS, stucco или veneer и не каркас.
Считаем только материал отделки и только когда отделка в задании.

!!! danger "Что не считаем"
    EIFS, stucco, stone и brick veneer это finish-системы by others.
    Канон: [EIFS / Stucco / Veneer](../siding/eifs-stucco-veneer.md), правило
    для trim-scope и J-channel: [Exclusions и J-Channel](exclusions.md).

## Что входит и в каком порядке

<div class="grid cards" markdown>

-   :material-window-closed-variant:{ .lg .middle } **Casing, Corner & Band**

    ---

    Ext. casing (sides, heads, apron, mulls), corner boards, band и
    watertable, head crowns с cap и flashing, shutters, louvers, brackets.

    [Casing, Corner & Band](casing-corner-band.md)

-   :material-format-line-spacing:{ .lg .middle } **Furring & Window Jambs**

    ---

    Furring `1x4` / `2x4` под siding и jamb `2x4` / `2x8` / `2x10` в проёмах.
    Живут в разрезах, не на фасадах.

    [Furring & Jambs](furring-and-jambs.md)

-   :material-home-roof:{ .lg .middle } **Soffit & Fascia**

    ---

    Soffit и fascia по eves и rakes, frieze, rake moulding, returns,
    columns.

    [Soffit & Fascia](soffit-fascia.md)

-   :material-balcony:{ .lg .middle } **Porch / Deck / Balcony**

    ---

    Porch trims, flare; хаб к перилам, слоям балкона, pergola.

    [Porch / Deck / Balcony](porch-deck-balcony.md)

-   :material-fence:{ .lg .middle } **Rails & Decking**

    ---

    Канон по перилам: composite система, wood поэлементно, metal by others;
    decking, hardware постов, lattice.

    [Rails & Decking](rails-decking.md)

-   :material-layers-triple:{ .lg .middle } **Balcony build-up**

    ---

    Все слои балкона: что считает каркас, что отделка; composition с pavers.

    [Balcony build-up](balcony-buildup.md)

-   :material-shower:{ .lg .middle } **Outdoor Shower & Pergola**

    ---

    Privacy screen из IPE, pergola, trellis, canopy.

    [Shower & Pergola](shower-pergola.md)

-   :material-microsoft-excel:{ .lg .middle } **Trim macros**

    ---

    `C_TrimsCalc`, сворачивание дублей, вставка блоков jambs, pavers,
    balcony, bolts.

    [Trim macros](macros.md)

-   :material-cancel:{ .lg .middle .kb-mk--amber } **Exclusions и J-Channel**

    ---

    Что не считаем в trim-scope и где идёт J-channel.

    [Exclusions](exclusions.md)

</div>

## Порядок работы

1. Прочитай ноту о siding-материале на фасадах: Hardi, vinyl, cedar, EIFS,
   stone. Она задаёт, какой trim вообще возможен (vinyl часто значит
   J-channel вместо casing).
2. Открой window и door details, wall sections, eave details: профили,
   furring, jambs, head crown с cap и flashing.
3. Считай по группам: проёмы (casing), углы и пояса, свесы, porch и
   balcony, изделия (shutters, louvers, columns).
4. Размер не указан: `TBD` и нота `Note: All trims to be verified. Scaled
   per elevations`. Не выдумывай продукт.

## Как мерить в OurPlanCore

Корень `trims` в дереве корпуса. Тип замера задаёт физический объект:
casing, band, corner и fascia это Line по итему на профиль (`2" casing`,
`8" horizontal trim`); soffit и потолок porch это Area по реальному
контуру; shutters, columns, brackets это Count. У каждой позиции свой цвет
и свой символ точки. Фасады и RCP не имеют точки листа, поэтому проверяй,
куда лёг итем. Длины eves и rakes приходят из `eves rakes`, площадь siding
из `siding`.

## Строка в DFL

| A Description | B Size | C Qty | D Unit | E |
| --- | --- | --- | --- | --- |
| `Ext. Casing sides` | `5/4x4` | `=2*5.5*34` | LFT | `A601` |
| `Head crowns` | `3-1/2" crown` | `=3.3*34` | LFT | `scaled` |
| `CornerBoards` | `5/4x6` | `=8*28` | LFT | `A201` |
| `Soffits at Porch` | `Beadboard` | `=12*8*G` | SQ FT | `6/A550` |
| `Columns` | `12" Dia Fbg Non-taper w/c&b` | `4` | pcs | `8'` |
| `Shutters - paneled` | `20"x60"` | `12` | pairs | `A201` |

- `LFT` для погонажа, `SQ FT` для панелей и beadboard, `pcs` и `pairs`
  для изделий. Высота columns и posts отдельно, не внутри описания.
- Размер и профиль всегда видны (`5/4x4`, `3-1/2" crown`, `4" Vinyl
  corner`); generic `trim` не пишем.
- В trims workbook для макросов строка это три колонки Label, Value,
  Unit, см. [Trim macros](macros.md).

## Частые ошибки

- Trim посчитан при scope Frame only.
- Vinyl siding: J-channel и wood casing на одни проёмы.
- Canopy и porch повторно в eve и rake; porch SQFT на Front Page пустой.
- Продукт угадан вместо `TBD` и ноты.
- Все ошибки: [Excel DFL и ноты](../../start/common-mistakes.md#excel), [Deck, porch, балконы](../../start/common-mistakes.md#deck).

## См. также

- [Interior Trims](../interior-trims/overview.md), [Siding](../siding/overview.md), [Eve](../sheathing-and-misc/eve.md)
- [Material catalog](../../reference/material-catalog.md), [Standard notes](../../reference/standard-notes.md), [Takeoff item labels](../../reference/takeoff-items.md), [Excel macro hotkeys](../../reference/excel-hotkeys.md)
