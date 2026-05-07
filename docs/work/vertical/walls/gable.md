# Gable Walls

## Count

- Gable wall framing, sheathing, and SQFT where shown.
- Exterior treatment, WRB, and trim if included in the scope.
- Exterior gables.
- Interior gables.
- Porch gables.
- Truss gables.
- Dormer gables.

## Check

- Do not confuse gable sheathing with truss heel or box sheathing.
- If gable wall is panelized, verify whether loose sheathing or only WRB is in
  scope.
- FRT and exterior sheathing rules follow the exterior wall notes.
- Exterior/interior/dormer gables can be 2x4 or 2x6; verify on drawings.
- Truss gables: remove plates and studs from the left/output side when trusses
  already include them.
- Dormers should be recorded together with wall scope.
- Add gable stud height on the left/output side.

## Output Table

Source: `https://ewood.atlassian.net/wiki/spaces/work/pages/63799300/Gable`

| Line | Material | Formula / count | Unit | Note |
| --- | --- | --- | --- | --- |
| Plates Ext `(3)` btm and dbl top | `2x6` | `=ЧЁТН(((BTM + DBL TOP)*1)*1.1)` | LFT | `= BTM + TOP * 2` |
| Studs for Gables | `2x6` | `=ЧЁТН(SQFT / height)` | height | `= SQFT` |
| Blocking | `2x6` | `=ЧЁТН((BTM)/2*1)` | LFT | `= BTM` |
| Bracing Ext Walls | `2x4` | `=(BTM)/8*1.1` | `14` | `= BTM` |
| Wall Sheathing | `1/2" CDX Ply` | `=ОКРВВЕРХ(SQFT*1.1/32;1)` | 4x8 | per page |
| Vapor Barrier | `Tyvek` | `=ОКРВВЕРХ(SQFT*1.1;10)` | SQ FT | |
| Insulation | `1 1/2" Insulation` | `=ОКРВВЕРХ(SQFT*1.1;10)` | SQ FT | |
| Wall Sheathing | `7/16" Zip` | `=ОКРВВЕРХ(SQFT/32*1.1;1)` | 4x8 | per page |
| Tape | `Zip Tape` | `=ОКРВВЕРХ((SQFT*0.4)*1.1;10)` | LFT | |

## Truss Gable Note

Source: `https://ewood.atlassian.net/wiki/spaces/work/pages/63799300/Gable`

When gable end trusses are **by others**, only the sheathing package is included:

| Line | Material | Formula / count | Unit |
| --- | --- | --- | --- |
| Wall Sheathing | `1/2" CDX Ply` | `=ОКРВВЕРХ(SQFT*1.1/32;1)` | 4x8 |
| Vapor Barrier | `Tyvek` | `=ОКРВВЕРХ(SQFT*1.1;10)` | SQ FT |
| Insulation | `1 1/2" Insulation` | `=ОКРВВЕРХ(SQFT*1.1;10)` | SQ FT |
| Wall Sheathing | `7/16" Zip` | `=ОКРВВЕРХ(SQFT/32*1.1;1)` | 4x8 |
| Tape | `Zip Tape` | `=ОКРВВЕРХ((SQFT*0.4)*1.1;10)` | LFT |

<!-- confluence-context:start -->
## Confluence Context

Эта секция показывает, какие Confluence-страницы питают эту wiki-страницу и какие соседние темы связаны с ней через исходники.

| Source | Role here | Images | Raw MD |
| --- | --- | ---: | --- |
| [Gable (треугольные фронтоны)](https://ewood.atlassian.net/wiki/spaces/work/pages/63799300/Gable) | content + images | 9 | `imports/live-sources/confluence-work/pages/01-63799300-gable-треугольные-фронтоны.md`<br>`imports/live-sources/confluence-work-images/pages/01-63799300-gable-треугольные-фронтоны.md` |

### Related Wiki Pages

| Wiki page | Why it is connected |
| --- | --- |
| [start/takeoff-structure.md](../../../start/takeoff-structure.md) | linked from `Gable (треугольные фронтоны)` |
| [work/horizontal/roof-framing/dbl-trpl-rafters.md](../../horizontal/roof-framing/dbl-trpl-rafters.md) | linked from `Gable (треугольные фронтоны)` |
| [work/vertical/walls/exterior.md](exterior.md) | linked from `Gable (треугольные фронтоны)` |
| [work/vertical/walls/parapet.md](parapet.md) | linked from `Gable (треугольные фронтоны)` |
| [work/vertical/walls/sill-plates.md](sill-plates.md) | linked from `Gable (треугольные фронтоны)` |

### Source Notes

??? note "Gable (треугольные фронтоны)"
    Source: `https://ewood.atlassian.net/wiki/spaces/work/pages/63799300/Gable`
    Updated in Confluence: `июн. 24, 2025`

    - gables делятся на два типа:
    - gable stick - как стена
    - gable trusses - из ферм
    - определить из чего сделана крыша, на плане крыши найти заметки о Rafters - будет написано Trusses либо 2x8….2x12…..TJI360…. stick
    - крыша из досок trusses
    - крыша из досок stick
    - от этого зависит будут ли gables продолжением стены stick
    - или gables будут из ферм trusses
    - gable stick - как стена
    - plates (горизонтальные доски)
    - studs (вертикальные доски)
    - blocking и bracing (усиление)
    - sheathing (обшивка)
    - нужно в planswift измерить площадь SQFT, нижнюю грань BTM  и две верхние TOP как на примере ниже, вписать эти данные в excel как на примере ниже
    - площадь SQFT треугольника gable  брать от верхней грани стены TOP верхней доски ,
    - определить где заканчивается стена и начинается gable
    - посмотреть на разрезах/фасадах
    - все Gables треугольники (может быть несколько)  должны быть в planswift одной площадью, одной нижней доской BTM  и верхней TOP  - внесены в excel
    - Gable Walls
    - B
    - C
    - D
    - E
    - F
    - G
    - Plates Ext (3) btm and dbl top
    - 2x6
    - =ЧЁТН((( BTM + DBL TOP )*1)*1,1)
    - LFT
    - = BTM + TOP *2
    - Studs for Gables
    - 2x6
    - =ЧЁТН( SQFT / height )
    - height
    - = SQFT
    - Blocking
    - 2x6
    - =ЧЁТН(( BTM )/2*1)
    - LFT
    - = BTM
    - Bracing Ext Walls
    - 2x4
    - =( BTM )/8*1,1
    - 14
    - = BTM
    - Wall Sheathing
    - 1/2" CDX Ply
    - =ОКРВВЕРХ( SQFT *1,1/32;1)
    - 4x8
    - per page
    - = SQFT
    - Vapor Barrier
    - Tyvek
    - =ОКРВВЕРХ( SQFT  *1,1;10)
    - SQ FT
    - Insulation
    - 1 1/2" Insulation
    - =ОКРВВЕРХ( SQFT  *1,1;10)
    - SQ FT
    - Wall Sheathing
    - 7/16" Zip
    - =ОКРВВЕРХ( SQFT /32*1,1;1)
    - 4x8
    - per page
    - = SQFT
    - Tape
    - Zip Tape
    - =ОКРВВЕРХ(( SQFT *0,4)*1,1;10)
    - LFT
    - gable trusses - из ферм
    - sheathing (обшивка)
    - нужно в planswift измерить площадь SQFT, вписать эти данные в excel как на примере ниже
    - Note: Gables Ends Trusses are by
    - others; only sheathing is
    - included
    - D
    - E
    - F
    - G
    - Wall Sheathing
    - 1/2" CDX Ply
    - =ОКРВВЕРХ( SQFT *1,1/32;1)
    - 4x8
    - per page
    - = SQFT
    - Vapor Barrier
    - Tyvek
    - =ОКРВВЕРХ( SQFT  *1,1;10)
    - SQ FT
    - Insulation
    - 1 1/2" Insulation
    - =ОКРВВЕРХ( SQFT  *1,1;10)
    - SQ FT
    - Wall Sheathing
    - 7/16" Zip
    - =ОКРВВЕРХ( SQFT /32*1,1;1)
    - 4x8
    - per page
    - = SQFT
    - Tape
    - Zip Tape
    - =ОКРВВЕРХ(( SQFT *0,4)*1,1;10)
    - LFT

    Source tables:

    ### Table 1
    
    | Gable Walls | B | C | D | E | F | G |  |
    | --- | --- | --- | --- | --- | --- | --- | --- |
    | Plates Ext (3) btm and dbl top | 2x6 | =ЧЁТН((( BTM + DBL TOP )*1)*1,1) | LFT |  |  | = BTM + TOP *2 |  |
    | Studs for Gables | 2x6 | =ЧЁТН( SQFT / height ) | height |  |  | = SQFT |  |
    |  |  |  |  |  |  |  |  |
    | Blocking | 2x6 | =ЧЁТН(( BTM )/2*1) | LFT |  |  | = BTM |  |
    | Bracing Ext Walls | 2x4 | =( BTM )/8*1,1 | 14 |  |  | = BTM |  |
    |  |  |  |  |  |  |  |  |
    | Wall Sheathing | 1/2" CDX Ply | =ОКРВВЕРХ( SQFT *1,1/32;1) | 4x8 | per page |  | = SQFT |  |
    | Vapor Barrier | Tyvek | =ОКРВВЕРХ( SQFT  *1,1;10) | SQ FT |  |  |  |  |
    | Insulation | 1 1/2" Insulation | =ОКРВВЕРХ( SQFT  *1,1;10) | SQ FT |  |  |  |  |
    |  |  |  |  |  |  |  |  |
    | Wall Sheathing | 7/16" Zip | =ОКРВВЕРХ( SQFT /32*1,1;1) | 4x8 | per page |  | = SQFT |  |
    | Tape | Zip Tape | =ОКРВВЕРХ(( SQFT *0,4)*1,1;10) | LFT |  |  |  |  |

    ### Table 2
    
    | Note: Gables Ends Trusses are by | others; only sheathing is | included | D | E | F | G |  |
    | --- | --- | --- | --- | --- | --- | --- | --- |
    | Wall Sheathing | 1/2" CDX Ply | =ОКРВВЕРХ( SQFT *1,1/32;1) | 4x8 | per page |  | = SQFT |  |
    | Vapor Barrier | Tyvek | =ОКРВВЕРХ( SQFT  *1,1;10) | SQ FT |  |  |  |  |
    | Insulation | 1 1/2" Insulation | =ОКРВВЕРХ( SQFT  *1,1;10) | SQ FT |  |  |  |  |
    |  |  |  |  |  |  |  |  |
    | Wall Sheathing | 7/16" Zip | =ОКРВВЕРХ( SQFT /32*1,1;1) | 4x8 | per page |  | = SQFT |  |
    | Tape | Zip Tape | =ОКРВВЕРХ(( SQFT *0,4)*1,1;10) | LFT |  |  |  |  |


<!-- confluence-context:end -->

<!-- confluence-gallery:start -->
## Confluence Images

Изображения из Confluence размещены на этой странице по исходной теме.
Подпись сохраняет группу-источник, чтобы можно было быстро проверить контекст.

| Source group | Images | Confluence |
| --- | ---: | --- |
| Gable (треугольные фронтоны) | 9 | [source](https://ewood.atlassian.net/wiki/spaces/work/pages/63799300/Gable) |

<div class="kb-gallery">
  <a class="kb-gallery__item" href="../../../../assets/images/confluence/confluence-083.png" title="image-20250603-181446.png">
    <img src="../../../../assets/images/confluence/confluence-083.png" alt="Gable (треугольные фронтоны) - gable wall reference 01">
    <div class="kb-gallery__caption">gable wall reference 01 (image, 470 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../../../assets/images/confluence/confluence-084.png" title="image-20250603-181146.png">
    <img src="../../../../assets/images/confluence/confluence-084.png" alt="Gable (треугольные фронтоны) - gable wall reference 02">
    <div class="kb-gallery__caption">gable wall reference 02 (image, 244 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../../../assets/images/confluence/confluence-085.png" title="image-20250603-180924.png">
    <img src="../../../../assets/images/confluence/confluence-085.png" alt="Gable (треугольные фронтоны) - gable wall reference 03">
    <div class="kb-gallery__caption">gable wall reference 03 (image, 28 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../../../assets/images/confluence/confluence-086.png" title="image-20250603-180752.png">
    <img src="../../../../assets/images/confluence/confluence-086.png" alt="Gable (треугольные фронтоны) - gable wall reference 04">
    <div class="kb-gallery__caption">gable wall reference 04 (image, 11 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../../../assets/images/confluence/confluence-087.png" title="image-20250603-180136.png">
    <img src="../../../../assets/images/confluence/confluence-087.png" alt="Gable (треугольные фронтоны) - gable wall reference 05">
    <div class="kb-gallery__caption">gable wall reference 05 (image, 11 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../../../assets/images/confluence/confluence-088.png" title="image-20250603-174813.png">
    <img src="../../../../assets/images/confluence/confluence-088.png" alt="Gable (треугольные фронтоны) - gable wall reference 06">
    <div class="kb-gallery__caption">gable wall reference 06 (image, 30 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../../../assets/images/confluence/confluence-089.png" title="image-20250603-172238.png">
    <img src="../../../../assets/images/confluence/confluence-089.png" alt="Gable (треугольные фронтоны) - gable wall reference 07">
    <div class="kb-gallery__caption">gable wall reference 07 (image, 16 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../../../assets/images/confluence/confluence-090.png" title="image-20250603-172109.png">
    <img src="../../../../assets/images/confluence/confluence-090.png" alt="Gable (треугольные фронтоны) - gable wall reference 08">
    <div class="kb-gallery__caption">gable wall reference 08 (image, 31 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../../../assets/images/confluence/confluence-091.png" title="image-20250603-172051.png">
    <img src="../../../../assets/images/confluence/confluence-091.png" alt="Gable (треугольные фронтоны) - gable wall reference 09">
    <div class="kb-gallery__caption">gable wall reference 09 (image, 31 KB raw)</div>
  </a>
</div>
<!-- confluence-gallery:end -->
