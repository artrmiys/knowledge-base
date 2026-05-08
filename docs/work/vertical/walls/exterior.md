# Exterior Walls

<figure markdown>
  ![Exterior wall section takeoff checkpoints](../../../assets/images/walls/exterior-wall-section.svg)
  <figcaption>Exterior wall takeoff: перед подсчётом раздели wall на layers.</figcaption>
</figure>

## Что считать

- Studs, plates, blocking, sheathing, bracing, Tyvek/WRB, insulation и exterior
  buildouts, когда они in scope.
- Для panelized COM jobs считай только loose/exterior scope: Tyvek, bracing,
  floor-height sheathing, box sheathing, truss heel и parapet items.
- Residential/Tilda checklist buckets: basement exterior walls, first floor
  exterior walls, second floor exterior walls, attic/loft exterior walls, chimney
  walls, knee walls, dormer walls, garage walls и balloon walls.

## Критические правила

- Exterior sheathing идёт по Arch / energy / Zip notes, если Structural не даёт
  более сильное non-Zip requirement.
- Если exterior wall material = FRT, exterior blocking и parapets тоже FRT.
- Exterior buildouts — stick framed, не panels.
- Для one-hour exterior walls давай exterior wall SQFT, когда это requested.
- Проверяй wall size по floor: 2x4, 2x6 или 2x8.
- Bottom plates могут требовать separate line, если lower plate = P.T.

## Wall Sizing & Height

- На плане толщина стен: **5 1/2"** для 2x6, **3 1/2"** для 2x4.
- Высота стены — от нижней доски **Btm Plate** до верхних досок **Top Plates** (включая обе доски). Брать с **elevation** или **section**, не с плана.
- В PlanSwift запись: `ext <толщина> <высота>`, например **`ext 2x6 9.0`**.

## Под Bottom Plate (на бетоне)

При посадке экстерьерной стены на бетон/фундамент в takeoff попадают три позиции — их легко забыть, потому что на плане они не показаны:

- **Sill Sealer** — поролоновая прокладка между бетоном и нижней доской.
- **Termite Shield** — металлическая защита от термитов между бетоном и Btm Plate.
- **Washers** — шайбы под анкерные болты Btm Plate к фундаменту.

См. [Anchor Bolts](../../deck/anchor-bolts.md) и [Sill Plates](sill-plates.md) для bolts/plates конкретики.

## Где смотреть

| Где на чертежах | Что взять |
| --- | --- |
| Wall type schedule | Stud size, spacing, fire rating, sheathing notes |
| Exterior elevations | Special sheathing/Densglass zones, material changes, gables |
| Energy / envelope sheets | Zip, WRB, rigid insulation, continuous insulation |
| Structural plans/details | Bracing, shear wall notes, holdowns, tall-wall blocking |
| RCP / soffit details | Dropped exterior soffit frames и buildouts |

## Вывод takeoff

- Exterior wall framing, sheathing, WRB, insulation и buildouts держи отдельными
  rows, если scope/pricing нужно проверить.
- Assumptions пиши прямо в output: `2x6 ext wall assumed from wall type` лучше,
  чем молча смешать sizes.
- Если floor repeats, всё равно list that floor separately и добавь `same as`
  note вместо combining floors.

## PlanSwift Wall Names

Source: `https://ewood.atlassian.net/wiki/spaces/work/pages/65175555/Walls`

| Wall output name | Для чего |
| --- | --- |
| `ext x` | Exterior wall run |
| `cor 2x6 x` / `corr 2x6 x` | Corridor wall, 2x6 |
| `cor 2x4 x` / `corr 2x4 x` | Corridor wall, 2x4 |
| `dem 2x6 x` | Demising wall, 2x6 |
| `dem 2x4 x` | Demising wall, 2x4 |
| `cor (2) 2x6 x` / `corr (2) 2x6 x` | Double corridor wall, 2x6 |
| `cor (2) 2x4 x` / `corr (2) 2x4 x` | Double corridor wall, 2x4 |
| `dem (2) 2x6 x` | Double demising wall, 2x6 |
| `dem (2) 2x4 x` | Double demising wall, 2x4 |
| `2x4 x` / `2x6 x` | Generic wall run by stud size |
| `2x4 half` / `2x6 half` | Half-height wall by stud size |

## Частые пропуски

- Rigid insulation.
- R6 Zip wall system.
- 5/8" Densglass on levels or elevations called out by wall type schedule.
- Dropped soffit frames from RCP pages.
- Garage doors quantity on first-floor/garage wall takeoff.
- Corner studs and corners by floor.
- Exterior blocking changing to FRT because the exterior wall material is FRT.
- Parapet framing that follows the exterior wall material rule.


<!-- confluence-gallery:start -->
## Картинки из Confluence

Изображения из Confluence размещены на этой странице по исходной теме.
Подпись сохраняет группу-источник, чтобы можно было быстро проверить контекст.

| Группа источника | Картинки | Confluence |
| --- | ---: | --- |
| Exterior (наружные стены) | 16 | [source](https://ewood.atlassian.net/wiki/spaces/work/pages/65273857/Exterior) |

<div class="kb-gallery">
  <a class="kb-gallery__item" href="../../../../assets/images/confluence/confluence-109.png" title="image-20260408-222831.png">
    <img src="../../../../assets/images/confluence/confluence-109.png" alt="Exterior (наружные стены) - exterior wall detail/reference 01">
    <div class="kb-gallery__caption">exterior wall detail/reference 01</div>
  </a>
  <a class="kb-gallery__item" href="../../../../assets/images/confluence/confluence-110.png" title="image-20260408-220422.png">
    <img src="../../../../assets/images/confluence/confluence-110.png" alt="Exterior (наружные стены) - exterior wall detail/reference 02">
    <div class="kb-gallery__caption">exterior wall detail/reference 02</div>
  </a>
  <a class="kb-gallery__item" href="../../../../assets/images/confluence/confluence-111.png" title="image-20260408-215636.png">
    <img src="../../../../assets/images/confluence/confluence-111.png" alt="Exterior (наружные стены) - exterior wall detail/reference 03">
    <div class="kb-gallery__caption">exterior wall detail/reference 03</div>
  </a>
  <a class="kb-gallery__item" href="../../../../assets/images/confluence/confluence-112.png" title="image-20260408-215533.png">
    <img src="../../../../assets/images/confluence/confluence-112.png" alt="Exterior (наружные стены) - exterior wall detail/reference 04">
    <div class="kb-gallery__caption">exterior wall detail/reference 04</div>
  </a>
  <a class="kb-gallery__item" href="../../../../assets/images/confluence/confluence-113.png" title="image-20260408-215334.png">
    <img src="../../../../assets/images/confluence/confluence-113.png" alt="Exterior (наружные стены) - exterior wall detail/reference 05">
    <div class="kb-gallery__caption">exterior wall detail/reference 05</div>
  </a>
  <a class="kb-gallery__item" href="../../../../assets/images/confluence/confluence-114.png" title="image-20260408-212441.png">
    <img src="../../../../assets/images/confluence/confluence-114.png" alt="Exterior (наружные стены) - exterior wall detail/reference 06">
    <div class="kb-gallery__caption">exterior wall detail/reference 06</div>
  </a>
  <a class="kb-gallery__item" href="../../../../assets/images/confluence/confluence-115.png" title="image-20260408-212418.png">
    <img src="../../../../assets/images/confluence/confluence-115.png" alt="Exterior (наружные стены) - exterior wall detail/reference 07">
    <div class="kb-gallery__caption">exterior wall detail/reference 07</div>
  </a>
  <a class="kb-gallery__item" href="../../../../assets/images/confluence/confluence-116.png" title="image-20251120-163603.png">
    <img src="../../../../assets/images/confluence/confluence-116.png" alt="Exterior (наружные стены) - exterior wall detail/reference 08">
    <div class="kb-gallery__caption">exterior wall detail/reference 08</div>
  </a>
  <a class="kb-gallery__item" href="../../../../assets/images/confluence/confluence-117.png" title="image-20251120-163803.png">
    <img src="../../../../assets/images/confluence/confluence-117.png" alt="Exterior (наружные стены) - exterior wall detail/reference 09">
    <div class="kb-gallery__caption">exterior wall detail/reference 09</div>
  </a>
  <a class="kb-gallery__item" href="../../../../assets/images/confluence/confluence-118.png" title="654dd981-d86a-4882-94a5-679a31b64b84.png">
    <img src="../../../../assets/images/confluence/confluence-118.png" alt="Exterior (наружные стены) - exterior wall detail/reference 10">
    <div class="kb-gallery__caption">exterior wall detail/reference 10</div>
  </a>
  <a class="kb-gallery__item" href="../../../../assets/images/confluence/confluence-119.png" title="image-20260408-211626.png">
    <img src="../../../../assets/images/confluence/confluence-119.png" alt="Exterior (наружные стены) - exterior wall detail/reference 11">
    <div class="kb-gallery__caption">exterior wall detail/reference 11</div>
  </a>
  <a class="kb-gallery__item" href="../../../../assets/images/confluence/confluence-120.png" title="image-20251120-162245.png">
    <img src="../../../../assets/images/confluence/confluence-120.png" alt="Exterior (наружные стены) - exterior wall detail/reference 12">
    <div class="kb-gallery__caption">exterior wall detail/reference 12</div>
  </a>
  <a class="kb-gallery__item" href="../../../../assets/images/confluence/confluence-121.png" title="image-20251030-161255.png">
    <img src="../../../../assets/images/confluence/confluence-121.png" alt="Exterior (наружные стены) - exterior wall detail/reference 13">
    <div class="kb-gallery__caption">exterior wall detail/reference 13</div>
  </a>
  <a class="kb-gallery__item" href="../../../../assets/images/confluence/confluence-122.png" title="image-20251030-161158.png">
    <img src="../../../../assets/images/confluence/confluence-122.png" alt="Exterior (наружные стены) - exterior wall detail/reference 14">
    <div class="kb-gallery__caption">exterior wall detail/reference 14</div>
  </a>
  <a class="kb-gallery__item" href="../../../../assets/images/confluence/confluence-123.png" title="image-20251030-161154.png">
    <img src="../../../../assets/images/confluence/confluence-123.png" alt="Exterior (наружные стены) - exterior wall detail/reference 15">
    <div class="kb-gallery__caption">exterior wall detail/reference 15</div>
  </a>
  <a class="kb-gallery__item" href="../../../../assets/images/confluence/confluence-124.png" title="image-20251030-161128.png">
    <img src="../../../../assets/images/confluence/confluence-124.png" alt="Exterior (наружные стены) - exterior wall detail/reference 16">
    <div class="kb-gallery__caption">exterior wall detail/reference 16</div>
  </a>
</div>
<!-- confluence-gallery:end -->
