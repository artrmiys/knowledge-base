# COM Commercial

Commercial jobs are large jobs such as multifamily, office, hotel, and mixed-use
buildings.

## Default Order

1. Exterior walls.
2. Corridor walls.
3. Demising walls.
4. Unit / interior walls.
5. Openings.
6. Sheathing.
7. SQFT.
8. Floor framing.
9. Roof framing.
10. Deck / porch / balcony / misc.

## Two COM Plan Types

| Type | Count | Do not count |
| --- | --- | --- |
| Normal walls | Studs, plates, blocking, sheathing, bracing, headers, openings | Items explicitly by others |
| Panelized walls | Exterior/corridor/demising bracing, floor-height plywood, box sheathing, truss heel, parapet | Studs, plates, blocking, most plywood inside panels |

For panelized exterior walls, usually only Tyvek is counted on exterior walls
unless drawings/specs call out additional loose material.

## Multipliers

- COM generally uses 1.1 waste on formulas.
- Do not apply 1.1 twice when a formula references another formula already using
  waste.
- Blocking in COM notes may be listed with factor 1, depending on scope.

## Watch Items

- FRT scope.
- Double studs at lower bearing walls.
- Wall schedule and structural notes.
- Arch details that complement structural details.
- RCP dropped soffits.
- Underlayment and sound membrane.
- Shafts, stairs, elevators.
- Metal studs by client rule.

<!-- confluence-context:start -->
## Confluence Context

Эта секция показывает, какие Confluence-страницы питают эту wiki-страницу и какие соседние темы связаны с ней через исходники.

| Source | Role here | Images | Raw MD |
| --- | --- | ---: | --- |
| [Check list 01 2026](https://ewood.atlassian.net/spaces/work/pages/227934223/Check+list+01+2026) | content | 0 | `imports/live-sources/confluence-work/pages/01-227934223-check-list-01-2026.md` |
| [COM Commercial Job](https://ewood.atlassian.net/wiki/spaces/work/pages/2359297/COM+Commercial+Job) | content + images | 13 | `imports/live-sources/confluence-work/pages/01-2359297-com-commercial-job.md`<br>`imports/live-sources/confluence-work-images/pages/01-2359297-com-commercial-job.md` |

### Related Wiki Pages

| Wiki page | Why it is connected |
| --- | --- |
| [reference/boss-feedback-rules.md](../reference/boss-feedback-rules.md) | linked from `COM Commercial Job` |
| [start/takeoff-structure.md](../start/takeoff-structure.md) | linked from `COM Commercial Job` |
| [work/vertical/walls/exterior.md](../work/vertical/walls/exterior.md) | linked from `COM Commercial Job` |

### Source Notes

??? note "Check list 01 2026"
    Source: `https://ewood.atlassian.net/spaces/work/pages/227934223/Check+list+01+2026`
    Updated in Confluence: `2026-04-18T03:08:04.019Z`

    - COM jobs Check ListCheck specificationsa)      FRT (Fire treated) lumber anywhere in specs. Important. Can be only Wall sheathing or could be entire exterior wall (sheathing; studs, plates, headers). If second most likely all exterior elements such as blocking, parapets can be FRT.Watch OSB Ext sheathing to be called “Flame Block” or Denseglas Sheathing.Denseglas is common at metal wallsb)      Glulam grades. Architectural 24F-V3, etc. Wording like “camber”c)      Stud and Plates specifications: SP plates; SPF studs vs DF, or DF#2 or HF or MSR, LSLd)      Bearing wall spacing and qnt specification. Lower levels double studs, etc. Demising studs. List as extra in a separate line.Watch for multi-layer sheathing and subfloor. Underlayment. Sound membrane.Edge sheathing can be FRT 4’ or 2’ around. Floor&Roof – see notes. Above demising alsoGypcrete floors most likely double bottom platesRigid InsulationsInterior sheathing and Holdowns! If no location called – assume each side of SW.Parapet sheathing inside is same as outside minus insulation board.Tall Trusses w Piggy trusses require 2x6 bearing plates 4’ ocFlat curb blocking at Flat roofs (2) 2x6 PT if nothing specified or if no detail.10.  Exact stud height – do math if need it. 9’, 9’1-1/8”, 9’1-1/4” etc.11.  Always follow S-details when provided.12.  Exterior Sheathing per Arch plans (unless Structural has more info); Interior sheathing per structural.13.  Watch for Blocking around windows, especially when Insulation or Zip R sheathing used.14.  Watch for 1x3 PT strapping at siding like Hardi paneling when specified.15.  Any Exterior buildouts stick framed, not panels16.  Check all new formulas immediately, not after.17.  Shaft walls18.  Check Dropped Soffits. RCP pages. Can be 2x4 soffit frame at baths or corridor.19.  Check Soffit plywood under Roof trusses. Possible.20.  Under Podium or inside existing can not be panels.

??? note "COM Commercial Job"
    Source: `https://ewood.atlassian.net/wiki/spaces/work/pages/2359297/COM+Commercial+Job`
    Updated in Confluence: `апр. 18`

    - exterior внешние стены
    - corridor коридорные стены
    - demising меж секционные стены
    - Сначала каркас Ext Corridor Demising walls Потом по Units int walls
    - Siding Ext trims очень редко но бывает
    - Demising стены могут быть двойные - выписывать отдельно
    - Внимательнее с масштабом 1/4 SQFT от общей площади
    - Вся продукция для Commercial House умножается на 1,1
    - 2 типа Коммерческих планов
    - Стены обычные
    - Стены из панелей
    - Стены из панелей:
    - детали для перекрытия из ферм
    - Blocking Flat 48" o.c. =ОКРВВЕРХ(G242*12/48*2*1,1/D242;1)
    - Blocking Diagonal 48" o.c. =ОКРВВЕРХ(G241*12/48*2,5*1,1/D241;1)
    - На Trusses нужно считать Gables для Plywood
    - Shear walls -тоже нужно , Panel walls идет только с одной стороны Plywood
    - Holdowns Strapping Straps и тд
    - Bracing for Trusses каждые 10' 2x6 в LFT
    - Blocking могут делать из Plywood
    - детали внимательнее Huricane Ties не пропускать
    - Beams LVL нужно считать и учитывать
    - на Коридор смотреть внимательнее
    - обычно коридор 6-7' перекрывается 2x10 крепится на ledger
    - Bracing
    - 16' высота стены - 20'
    - 12' и выше - 18'
    - 10'-12' - 16'
    - все остальное - 14'
    - Самое главное это Structural Detail
    - Направление Joists перпендикулярно или параллельно
    - Trusses на полу и на крыше отличаются по высоте
    - Accessories for Trusses все что находится по периметру сначала по Structural plans (опирание - параллельно перпендикулярно и внутри на стенах)
    - Parapets
    - Balconies
    - Staggered Walls
    - 2x4 Ribbon Board

<!-- confluence-context:end -->

<!-- confluence-gallery:start -->
## Confluence Images

Изображения из Confluence размещены на этой странице по исходной теме.
Подпись сохраняет группу-источник, чтобы можно было быстро проверить контекст.

| Source group | Images | Confluence |
| --- | ---: | --- |
| COM Commercial Job | 13 | [source](https://ewood.atlassian.net/wiki/spaces/work/pages/2359297/COM+Commercial+Job) |

<div class="kb-gallery">
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-053.png" title="image-20250722-030816.png">
    <img src="../../assets/images/confluence/confluence-053.png" alt="COM Commercial Job - COM takeoff workflow/reference 01">
    <div class="kb-gallery__caption">COM takeoff workflow/reference 01 (image, 323 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-054.png" title="image-20250717-232520.png">
    <img src="../../assets/images/confluence/confluence-054.png" alt="COM Commercial Job - COM takeoff workflow/reference 02">
    <div class="kb-gallery__caption">COM takeoff workflow/reference 02 (image, 136 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-055.png" title="image-20250619-192434.png">
    <img src="../../assets/images/confluence/confluence-055.png" alt="COM Commercial Job - COM takeoff workflow/reference 03">
    <div class="kb-gallery__caption">COM takeoff workflow/reference 03 (image, 116 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-056.png" title="image-20250619-192242.png">
    <img src="../../assets/images/confluence/confluence-056.png" alt="COM Commercial Job - COM takeoff workflow/reference 04">
    <div class="kb-gallery__caption">COM takeoff workflow/reference 04 (image, 95 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-057.png" title="image-20250619-192221.png">
    <img src="../../assets/images/confluence/confluence-057.png" alt="COM Commercial Job - COM takeoff workflow/reference 05">
    <div class="kb-gallery__caption">COM takeoff workflow/reference 05 (image, 102 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-058.png" title="image-20250619-192136.png">
    <img src="../../assets/images/confluence/confluence-058.png" alt="COM Commercial Job - COM takeoff workflow/reference 06">
    <div class="kb-gallery__caption">COM takeoff workflow/reference 06 (image, 101 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-059.png" title="image-20250619-191959.png">
    <img src="../../assets/images/confluence/confluence-059.png" alt="COM Commercial Job - COM takeoff workflow/reference 07">
    <div class="kb-gallery__caption">COM takeoff workflow/reference 07 (image, 57 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-060.png" title="image-20250619-191937.png">
    <img src="../../assets/images/confluence/confluence-060.png" alt="COM Commercial Job - COM takeoff workflow/reference 08">
    <div class="kb-gallery__caption">COM takeoff workflow/reference 08 (image, 40 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-061.png" title="image-20250210-115947.png">
    <img src="../../assets/images/confluence/confluence-061.png" alt="COM Commercial Job - COM takeoff workflow/reference 09">
    <div class="kb-gallery__caption">COM takeoff workflow/reference 09 (image, 84 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-062.png" title="image-20250210-115939.png">
    <img src="../../assets/images/confluence/confluence-062.png" alt="COM Commercial Job - COM takeoff workflow/reference 10">
    <div class="kb-gallery__caption">COM takeoff workflow/reference 10 (image, 156 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-063.png" title="image-20250210-115920.png">
    <img src="../../assets/images/confluence/confluence-063.png" alt="COM Commercial Job - COM takeoff workflow/reference 11">
    <div class="kb-gallery__caption">COM takeoff workflow/reference 11 (image, 7 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-064.png" title="image-20250210-115909.png">
    <img src="../../assets/images/confluence/confluence-064.png" alt="COM Commercial Job - COM takeoff workflow/reference 12">
    <div class="kb-gallery__caption">COM takeoff workflow/reference 12 (image, 5 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-065.png" title="image-20250210-115855.png">
    <img src="../../assets/images/confluence/confluence-065.png" alt="COM Commercial Job - COM takeoff workflow/reference 13">
    <div class="kb-gallery__caption">COM takeoff workflow/reference 13 (image, 11 KB raw)</div>
  </a>
</div>
<!-- confluence-gallery:end -->
