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
- **Metal stud / CMU стены:** даже если каркас by others, обшивка (exterior
  gypsum), insulation (вкл. `Insulation at CMU`), flashing, `Bracing 2x4` и
  window jambs остаются нашими. Полный блок — [Exterior Wall Materials](../sheathing/exterior-materials.md).

## Wall Sizing & Height

- На плане толщина стен: **5 1/2"** для 2x6, **3 1/2"** для 2x4.
- Высота стены — от нижней доски **Btm Plate** до верхних досок **Top Plates** (включая обе доски). Брать с **elevation** или **section**, не с плана.
- В PlanSwift запись: `ext <толщина> <высота>`, например **`ext 2x6 9.0`**.

## Под Bottom Plate (на бетоне)

При посадке экстерьерной стены на бетон/фундамент в takeoff попадают три
скрытые позиции (Sill Sealer / Termite Shield / Washers) — их легко забыть,
потому что на плане они не показаны. Полный разбор и иллюстрации —
[Sill Plates → Что считать вместе с Sill Plate](sill-plates.md#что-считать-вместе-с-sill-plate)
и [Anchor Bolts](../../deck/anchor-bolts.md).

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

Source: `https://redacted.atlassian.net/wiki/spaces/work/pages/65175555/Walls`

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

## Полнота строки { .kb-section-title .kb-st--cyan }

На full-frame проектах 1st-floor-стена — это полный каркас, не только bracing+sheathing.
Типовой набор:

| Строка | Заметка |
| --- | --- |
| Studs Ext / Int / Dem | размер авто по высоте стены (nested-IF) |
| Bracing Ext / Dem / Corr | `2x4` |
| Vapor Barrier | Tyvek |
| Wall / Box Sheathing | OSB чаще Zip |
| Blocking | `2x4`–`2x10` |
| **Holdowns** | `DTT2Z` / `HTT5KT` / `HDU…` / `TBD HD` — частый пропуск |
| Plates btm (P.T.) + dbl top | btm `2x6/2x4 P.T.` |
| Ext. Headers | `2x10`/`2x8`/`2x12` по пролёту |

→ **Holdowns** — если есть shear walls, не забудь (выбор по SW-schedule,
[Hardware catalog](../../../reference/hardware-catalog.md)). Studs auto-sized по высоте —
коэффициенты spacing в [Формулах](../../../reference/formulas.md).

## Частые пропуски

- Rigid insulation.
- R6 Zip wall system.
- 5/8" Densglass on levels or elevations called out by wall type schedule.
- Dropped soffit frames from RCP pages.
- Garage doors quantity on first-floor/garage wall takeoff.
- Corner studs and corners by floor.
- Exterior blocking changing to FRT because the exterior wall material is FRT.
- Parapet framing that follows the exterior wall material rule.
- Exterior gypsum sheathing на metal стенах (material нужен, даже если studs чужие).
- `Insulation at CMU` — отдельная строка от обычной wall insulation.
- Window jambs (доска) в проёмах metal стен; flashing at Mtl/CMU walls.


<!-- confluence-gallery:start -->
## Визуальная проверка

Эти картинки уже привязаны к правилам страницы. Используй их как быстрые
checkpoint-ы перед output: сначала прочитай правило выше, потом открой нужную
карточку и проверь похожий condition на плане/schedule.

??? info "Источник картинок"
    - Exterior (наружные стены): [16 карт. Confluence](https://redacted.atlassian.net/wiki/spaces/work/pages/65273857/Exterior)

<details class="kb-figures">
  <summary>Показать 16 иллюстраций</summary>
  <div class="kb-figure-grid">
    <a class="kb-figure" href="../../../../assets/images/confluence/confluence-109.png" target="_blank" rel="noopener"><img src="../../../../assets/images/confluence/confluence-109.png" alt="Exterior Wall - визуальная проверка 01: Проверь wall type, height, sheathing/WRB, FRT и bottom-plate accessories." loading="lazy"></a>
    <a class="kb-figure" href="../../../../assets/images/confluence/confluence-110.png" target="_blank" rel="noopener"><img src="../../../../assets/images/confluence/confluence-110.png" alt="Exterior Wall - визуальная проверка 02: Проверь wall type, height, sheathing/WRB, FRT и bottom-plate accessories." loading="lazy"></a>
    <a class="kb-figure" href="../../../../assets/images/confluence/confluence-111.png" target="_blank" rel="noopener"><img src="../../../../assets/images/confluence/confluence-111.png" alt="Exterior Wall - визуальная проверка 03: Проверь wall type, height, sheathing/WRB, FRT и bottom-plate accessories." loading="lazy"></a>
    <a class="kb-figure" href="../../../../assets/images/confluence/confluence-112.png" target="_blank" rel="noopener"><img src="../../../../assets/images/confluence/confluence-112.png" alt="Exterior Wall - визуальная проверка 04: Проверь wall type, height, sheathing/WRB, FRT и bottom-plate accessories." loading="lazy"></a>
    <a class="kb-figure" href="../../../../assets/images/confluence/confluence-113.png" target="_blank" rel="noopener"><img src="../../../../assets/images/confluence/confluence-113.png" alt="Exterior Wall - визуальная проверка 05: Проверь wall type, height, sheathing/WRB, FRT и bottom-plate accessories." loading="lazy"></a>
    <a class="kb-figure" href="../../../../assets/images/confluence/confluence-114.png" target="_blank" rel="noopener"><img src="../../../../assets/images/confluence/confluence-114.png" alt="Exterior Wall - визуальная проверка 06: Проверь wall type, height, sheathing/WRB, FRT и bottom-plate accessories." loading="lazy"></a>
    <a class="kb-figure" href="../../../../assets/images/confluence/confluence-115.png" target="_blank" rel="noopener"><img src="../../../../assets/images/confluence/confluence-115.png" alt="Exterior Wall - визуальная проверка 07: Проверь wall type, height, sheathing/WRB, FRT и bottom-plate accessories." loading="lazy"></a>
    <a class="kb-figure" href="../../../../assets/images/confluence/confluence-116.png" target="_blank" rel="noopener"><img src="../../../../assets/images/confluence/confluence-116.png" alt="Exterior Wall - визуальная проверка 08: Проверь wall type, height, sheathing/WRB, FRT и bottom-plate accessories." loading="lazy"></a>
    <a class="kb-figure" href="../../../../assets/images/confluence/confluence-117.png" target="_blank" rel="noopener"><img src="../../../../assets/images/confluence/confluence-117.png" alt="Exterior Wall - визуальная проверка 09: Проверь wall type, height, sheathing/WRB, FRT и bottom-plate accessories." loading="lazy"></a>
    <a class="kb-figure" href="../../../../assets/images/confluence/confluence-118.png" target="_blank" rel="noopener"><img src="../../../../assets/images/confluence/confluence-118.png" alt="Exterior Wall - визуальная проверка 10: Проверь wall type, height, sheathing/WRB, FRT и bottom-plate accessories." loading="lazy"></a>
    <a class="kb-figure" href="../../../../assets/images/confluence/confluence-119.png" target="_blank" rel="noopener"><img src="../../../../assets/images/confluence/confluence-119.png" alt="Exterior Wall - визуальная проверка 11: Проверь wall type, height, sheathing/WRB, FRT и bottom-plate accessories." loading="lazy"></a>
    <a class="kb-figure" href="../../../../assets/images/confluence/confluence-120.png" target="_blank" rel="noopener"><img src="../../../../assets/images/confluence/confluence-120.png" alt="Exterior Wall - визуальная проверка 12: Проверь wall type, height, sheathing/WRB, FRT и bottom-plate accessories." loading="lazy"></a>
    <a class="kb-figure" href="../../../../assets/images/confluence/confluence-121.png" target="_blank" rel="noopener"><img src="../../../../assets/images/confluence/confluence-121.png" alt="Exterior Wall - визуальная проверка 13: Проверь wall type, height, sheathing/WRB, FRT и bottom-plate accessories." loading="lazy"></a>
    <a class="kb-figure" href="../../../../assets/images/confluence/confluence-122.png" target="_blank" rel="noopener"><img src="../../../../assets/images/confluence/confluence-122.png" alt="Exterior Wall - визуальная проверка 14: Проверь wall type, height, sheathing/WRB, FRT и bottom-plate accessories." loading="lazy"></a>
    <a class="kb-figure" href="../../../../assets/images/confluence/confluence-123.png" target="_blank" rel="noopener"><img src="../../../../assets/images/confluence/confluence-123.png" alt="Exterior Wall - визуальная проверка 15: Проверь wall type, height, sheathing/WRB, FRT и bottom-plate accessories." loading="lazy"></a>
    <a class="kb-figure" href="../../../../assets/images/confluence/confluence-124.png" target="_blank" rel="noopener"><img src="../../../../assets/images/confluence/confluence-124.png" alt="Exterior Wall - визуальная проверка 16: Проверь wall type, height, sheathing/WRB, FRT и bottom-plate accessories." loading="lazy"></a>
  </div>
</details>
<!-- confluence-gallery:end -->
