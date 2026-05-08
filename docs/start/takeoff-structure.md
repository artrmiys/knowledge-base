# Takeoff Structure

Source: `https://ewood.atlassian.net/wiki/spaces/work/pages/65961989/Deck+Porch+Balcony+-`

Эта структура повторяет рабочий порядок COM takeoff.

## Vertical Constructions

- Walls:
  - Sill Plates
  - Unit
  - Exterior
  - Corridor
  - Demising
  - Gable
  - Parapet
  - Shaft
  - Furring
  - Corners
- Openings:
  - Windows and Doors
  - Headers
- Sheathing:
  - Wall Sheathing
  - Floor
  - Gable
  - Box Sheathing
  - Truss Heel
  - Shear Wall

## SQFT

- Basement
- 1st-5th Floors
- Loft
- Roof
- Deck
- Porch
- Balcony
- Cantilevered

## Sheathing and Misc

- Eve
- Rake
- Returns
- Roof Types
- Ridge / Valley / Hip
- Flashing

## Horizontal Constructions

- Floor Framing:
  - Post
  - Beam
  - Joist
  - Stair
  - Subfloor
  - Details: Rim, Ribbon, Blocking, Bracing, Bolts, Screws, Steel Beam Web Fillers
- Roof Framing:
  - Ridge
  - Header
  - Hip
  - Valley
  - Dormer
  - Overframes
  - Dbl/Trpl Rafters
  - Canopy
  - Roof Sheathing

## Deck / Porch / Balcony

- Railing
- Balcony Trims
- Anchor Bolts

## Interior Finishes

- Interior Trims
- Base
- Casing
- Crown
- Door and Window Trim
- Room Schedule

## Naming Notes

- Keep floors separate even when identical.
- If a floor is identical, add a note such as `4th floor frame is identical to 3rd floor`,
  but still list materials separately.
- Panelized wall jobs need different counting rules; see [COM Commercial](../work-types/com.md).
- Interior trims should be separated from exterior trims and gypsum.
- The old Tilda source had many menu items as labels without active links. Current
  confirmed active work pages were Walls and Gables.

## Vertical Constructions — что входит

Вертикалка ≈ **50% здания**, важно ничего не пропустить:

- Несущие и ненесущие стены: `Ext`, `Unit`, `Corr`, `Demising` walls.
- Фронтоны — `Gables`.
- Наружная и внутренняя обшивка: `Plywood`, `OSB`, siding, gypsum.
- Обшивка торцов перекрытия — `Floor Height`.
- Обшивка торцов перекрытия — `Eve Heel` / `Truss Heel`.
- Ветроизоляция — `Tyvek`.
- Утеплитель — `Insulation`.

## Структура файла в PlanSwift

В PlanSwift сначала идут общие layers (без счёта), потом — группы по этажам и
типам. Общая идея — каждая ячейка `xxx` — это место для своей цифры.

### Background layers (не считаются)

- `wall type`, `beam schedule`, `shear wall schedule`
- `details struct`, `details arch`
- `rcp`, `sections`, `others`

### Группы (порядок в файле)

- **walls + gables**: `units`, `base`, `1st`, `2nd`, `3rd`, `4th`, `roof`, `parapet`, `el gables` (×2), `wall materials (insulation etc.)`.
- **sqfts + balconies + porch**: `1st`, `2nd`, `3rd`, `4th`.
- **roof - eve rakes**: `roof`.
- **framing + headers**: `base`, `1st`, `2nd`, `3rd`.
- **balconies / porches**: `balconies`, `porches`.
- **shear walls / holdowns / ties**: `shear walls`, `shear`, `holddowns`.
- **siding / trims**: `siding` (×2), `trims` (×2).
- **interior trims**, **drywall**.

## Floor Abbreviations

| Сокращение | Что |
| --- | --- |
| `f` | foundation — фундамент |
| `1st` | first floor |
| `2nd` | second floor |
| `3rd` | third floor |
| `5th–8th` | fifth to eighth floors |
| `el` | elevation — фасад |
| `sec` | section — разрез |
| `sec d` | section details |
| `rcp` | reflected ceiling plan |
| `wt` | wall type |
| `u` | units |
| `ext` | exterior |
| `int` | interior |
| `dem` | demising |
| `cor` | corridor |
| `str` | stair |

## SQFT-сокращения в PlanSwift

`deck`, `blcny`, `porch`, `cant`, `base`, `1st`, `2nd`, `3rd`, `4th`, `flat`,
`rf x`, `rf mtl x`, `overframe x`, `gable truss`, `gable stick`.

## Details — короткие коды

| Код | Что |
| --- | --- |
| `r` | rim board |
| `rr` | rim board × 2 |
| `l` | ledger |
| `ll` | ledger × 2 |
| `b` | blocking |
| `bи` | blocking × 2 |
| `b48` | blocking 48" o.c. |
| `bb48` | blocking 48" o.c. × 2 |
| `rb` | ribbon board |
| `bd` | blocking for drywall |
| `bft` | bracing for trusses |
| `h16` | hangers 16" o.c. |
| `hh16` | hangers 16" o.c. × 2 |

## Material Override Legend

В конце выделения добавляется override для конкретного материала. Формат:

| Код | Что записать |
| --- | --- |
| `r` | `1 3/4 x 11 7/8 LVL` |
| `r 1` | `1 3/4 x 18 LVL` |
| `b` | `11 7/8 TJI 230` |
| `b48` | `2x10` |
| `h16` | `ITS2.56/9.5` |
| `l` | `2x12 P.T.` |
| `l 1` | `2x10` |

<!-- confluence-gallery:start -->
## Confluence Images

Изображения из Confluence размещены на этой странице по исходной теме.
Подпись сохраняет группу-источник, чтобы можно было быстро проверить контекст.

| Source group | Images | Confluence |
| --- | ---: | --- |
| Roof Framing - конструкции крыши | 2 | [source](https://ewood.atlassian.net/wiki/spaces/work/pages/65962048/Roof+Framing+-) |
| Vertical Constructions | 10 | [source](https://ewood.atlassian.net/wiki/spaces/work/pages/65110035/Vertical+Constructions) |
| Walls | 3 | [source](https://ewood.atlassian.net/wiki/spaces/work/pages/65175555/Walls) |
| work | 9 | [source](https://ewood.atlassian.net/wiki/spaces/work/overview) |
| work - large GIF attachments | 2 | [source](https://ewood.atlassian.net/wiki/spaces/work/overview) |

<div class="kb-gallery">
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-032.jpg" title="3.gif">
    <img src="../../assets/images/confluence/confluence-032.jpg" alt="work - large GIF attachments - takeoff structure reference 01">
    <div class="kb-gallery__caption">takeoff structure reference 01 (preview, 87734 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-033.jpg" title="1.gif">
    <img src="../../assets/images/confluence/confluence-033.jpg" alt="work - large GIF attachments - takeoff structure reference 02">
    <div class="kb-gallery__caption">takeoff structure reference 02 (preview, 19363 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-034.png" title="image-20251103-183255.png">
    <img src="../../assets/images/confluence/confluence-034.png" alt="work - takeoff structure reference 01">
    <div class="kb-gallery__caption">takeoff structure reference 01 (image, 21 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-035.jpg" title="struct.jpg">
    <img src="../../assets/images/confluence/confluence-035.jpg" alt="work - takeoff structure reference 02">
    <div class="kb-gallery__caption">takeoff structure reference 02 (image, 155 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-036.png" title="image-20250619-200240.png">
    <img src="../../assets/images/confluence/confluence-036.png" alt="work - takeoff structure reference 03">
    <div class="kb-gallery__caption">takeoff structure reference 03 (image, 25 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-037.png" title="image-20250619-200019.png">
    <img src="../../assets/images/confluence/confluence-037.png" alt="work - takeoff structure reference 04">
    <div class="kb-gallery__caption">takeoff structure reference 04 (image, 25 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-038.png" title="image-20250524-215800.png">
    <img src="../../assets/images/confluence/confluence-038.png" alt="work - takeoff structure reference 05">
    <div class="kb-gallery__caption">takeoff structure reference 05 (image, 121 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-039.png" title="Без-имени-2.png">
    <img src="../../assets/images/confluence/confluence-039.png" alt="work - takeoff structure reference 06">
    <div class="kb-gallery__caption">takeoff structure reference 06 (image, 275 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-040.png" title="c27beda1-ce6d-4252-98d2-63be7f261548.png">
    <img src="../../assets/images/confluence/confluence-040.png" alt="work - takeoff structure reference 07">
    <div class="kb-gallery__caption">takeoff structure reference 07 (image, 13 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-041.png" title="e8eea12d-25c0-4ac0-99ca-8bd8764ab780.png">
    <img src="../../assets/images/confluence/confluence-041.png" alt="work - takeoff structure reference 08">
    <div class="kb-gallery__caption">takeoff structure reference 08 (image, 13 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-042.png" title="image-20250210-113643.png">
    <img src="../../assets/images/confluence/confluence-042.png" alt="work - takeoff structure reference 09">
    <div class="kb-gallery__caption">takeoff structure reference 09 (image, 20 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-096.png" title="image-20250625-035545.png">
    <img src="../../assets/images/confluence/confluence-096.png" alt="Vertical Constructions - vertical construction overview 01">
    <div class="kb-gallery__caption">vertical construction overview 01 (image, 342 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-097.png" title="image-20250625-035410.png">
    <img src="../../assets/images/confluence/confluence-097.png" alt="Vertical Constructions - vertical construction overview 02">
    <div class="kb-gallery__caption">vertical construction overview 02 (image, 267 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-098.png" title="image-20250625-035202.png">
    <img src="../../assets/images/confluence/confluence-098.png" alt="Vertical Constructions - vertical construction overview 03">
    <div class="kb-gallery__caption">vertical construction overview 03 (image, 267 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-099.png" title="image-20250625-034853.png">
    <img src="../../assets/images/confluence/confluence-099.png" alt="Vertical Constructions - vertical construction overview 04">
    <div class="kb-gallery__caption">vertical construction overview 04 (image, 97 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-100.png" title="image-20250625-034719.png">
    <img src="../../assets/images/confluence/confluence-100.png" alt="Vertical Constructions - vertical construction overview 05">
    <div class="kb-gallery__caption">vertical construction overview 05 (image, 188 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-101.png" title="image-20250625-034639.png">
    <img src="../../assets/images/confluence/confluence-101.png" alt="Vertical Constructions - vertical construction overview 06">
    <div class="kb-gallery__caption">vertical construction overview 06 (image, 320 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-102.png" title="image-20250625-034357.png">
    <img src="../../assets/images/confluence/confluence-102.png" alt="Vertical Constructions - vertical construction overview 07">
    <div class="kb-gallery__caption">vertical construction overview 07 (image, 67 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-103.png" title="image-20250625-034132.png">
    <img src="../../assets/images/confluence/confluence-103.png" alt="Vertical Constructions - vertical construction overview 08">
    <div class="kb-gallery__caption">vertical construction overview 08 (image, 87 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-104.png" title="image-20250625-033747.png">
    <img src="../../assets/images/confluence/confluence-104.png" alt="Vertical Constructions - vertical construction overview 09">
    <div class="kb-gallery__caption">vertical construction overview 09 (image, 102 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-105.png" title="image-20250625-033553.png">
    <img src="../../assets/images/confluence/confluence-105.png" alt="Vertical Constructions - vertical construction overview 10">
    <div class="kb-gallery__caption">vertical construction overview 10 (image, 75 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-106.png" title="image-20250625-041034.png">
    <img src="../../assets/images/confluence/confluence-106.png" alt="Walls - wall type overview 01">
    <div class="kb-gallery__caption">wall type overview 01 (image, 76 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-107.png" title="image-20250625-035805.png">
    <img src="../../assets/images/confluence/confluence-107.png" alt="Walls - wall type overview 02">
    <div class="kb-gallery__caption">wall type overview 02 (image, 92 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-108.png" title="image-20250625-035800.png">
    <img src="../../assets/images/confluence/confluence-108.png" alt="Walls - wall type overview 03">
    <div class="kb-gallery__caption">wall type overview 03 (image, 92 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-135.png" title="image-20250603-180752.png">
    <img src="../../assets/images/confluence/confluence-135.png" alt="Roof Framing - конструкции крыши - roof framing overview 01">
    <div class="kb-gallery__caption">roof framing overview 01 (image, 11 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-136.png" title="image-20250603-180924.png">
    <img src="../../assets/images/confluence/confluence-136.png" alt="Roof Framing - конструкции крыши - roof framing overview 02">
    <div class="kb-gallery__caption">roof framing overview 02 (image, 28 KB raw)</div>
  </a>
</div>
<!-- confluence-gallery:end -->
