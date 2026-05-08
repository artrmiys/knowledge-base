# COM Commercial

Commercial jobs — это большие проекты: multifamily, office, hotel, mixed-use
buildings.

## Порядок COM

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

## Два типа COM plans

| Тип | Что считать | Что не считать |
| --- | --- | --- |
| Normal walls | Studs, plates, blocking, sheathing, bracing, headers, openings | Items, которые явно by others |
| Panelized walls | Exterior/corridor/demising bracing, floor-height plywood, box sheathing, truss heel, parapet | Studs, plates, blocking, most plywood inside panels |

Для panelized exterior walls обычно считаем только Tyvek на exterior walls, если
drawings/specs не показывают дополнительный loose material.

## Multipliers

- COM обычно использует 1.1 waste в formulas.
- Не применяй 1.1 дважды, когда formula ссылается на другую formula, где waste
  уже учтён.
- Blocking в COM notes может идти с factor 1 — зависит от scope.

## Что не пропустить

- FRT scope.
- Double studs на lower bearing walls.
- Wall schedule и structural notes.
- Arch details, которые дополняют structural details.
- RCP dropped soffits.
- Underlayment и sound membrane.
- Shafts, stairs, elevators.
- Metal studs по client rule.

## Wall Order и состав

- Сначала каркас в порядке: `Ext` → `Corridor` → `Demising`. Юнитовые `int walls` идут после.
- `Demising` стены могут быть двойные — выписывать отдельной строкой.
- На масштабе **1/4"** SQFT берется от общей площади — внимательно.
- `Siding` и `Ext trims` бывают редко — но появляются в commercial.

## Panelized Walls — что считаем и не считаем

Панели делает другой подрядчик. Наш scope — только то, что не упаковано в панель:

- **Не считаем**: `Studs`, `Plates`, `Blocking`, `Plywood` внутри панели, интерьерные стены, `Corners`, `Headers`.
- **Считаем для Bracing**: только `Exterior Walls` + несущие (`Corridor Walls`, `Demising Walls`).
- **На Exterior Walls** считаем только **Tyvek** (если в спеках не указано доп. loose-материала).
- **Plywood** идёт только на Floor Height, Box Sheathing, Truss Heel, Parapet Walls — то, что не входит в стеновую панель.
- **Plywood на панелях** — только с одной стороны. У `Shear walls` — тоже одна сторона.
- На `Trusses` считаем `Gables` для Plywood.
- `Holdowns`, `Strapping`, `Straps` — отдельно.
- `Blocking` иногда делают из `Plywood` — проверять детали.
- `Hurricane Ties` в деталях — не пропускать.
- `Beams` LVL — считать и учитывать.
- Под подиумом или внутри существующего здания **панели не применяются** — там стик-фрейм.

## Bracing — высота стены → длина

| Высота стены | Bracing length |
| --- | --- |
| `16'` | `20'` |
| `12'` и выше | `18'` |
| `10'–12'` | `16'` |
| Всё остальное | `14'` |

`Bracing for Trusses` — каждые `10'`, `2x6` в LFT.

## Blocking-формулы (panelized walls)

- `Blocking Flat 48" o.c.` = `=ОКРВВЕРХ(G242*12/48*2*1.1/D242;1)`
- `Blocking Diagonal 48" o.c.` = `=ОКРВВЕРХ(G241*12/48*2.5*1.1/D241;1)`

## Corridor

- Смотреть внимательнее — обычно коридор `6'–7'` перекрывается `2x10`, крепится на `ledger`.
- Trusses на полу и на крыше отличаются по высоте — не путать.
- Направление Joists (перпендикулярно или параллельно стенам) определять по `Structural Detail` — это самое главное.
- Accessories for Trusses (всё по периметру) — сначала по Structural plans (опирание параллельно/перпендикулярно и внутри на стенах).

## Specs Check (приходит на каждый COM)

- **FRT (Fire Treated)** — может быть только на Wall Sheathing, либо на всю экстерьерную стену (sheathing + studs + plates + headers). Если второе — то и blocking/parapets обычно тоже FRT.
- Watch OSB Ext sheathing с названиями `Flame Block` или `Densglass Sheathing`. `Densglass` часто на metal walls.
- **Glulam grades**: Architectural `24F-V3` и т.п. Слова вроде `camber` — отметить.
- **Stud / Plates specs**: `SP plates`; `SPF` studs vs `DF`, `DF#2`, `HF`, `MSR`, `LSL`.
- **Bearing walls** — spacing и количество. На нижних этажах часто **double studs**, demising studs — выписывать отдельной строкой.
- Multi-layer sheathing, subfloor, underlayment, sound membrane — проверить.
- Edge sheathing может быть `FRT 4'` или `2'` по периметру (Floor & Roof — see notes; над demising тоже).
- `Gypcrete` floors — чаще всего **double bottom plates**.
- `Rigid Insulation` — проверить.
- **Interior sheathing** и **Holdowns**: если location не указан — assume каждая сторона SW.
- **Parapet** sheathing внутри = снаружи минус insulation board.
- **Tall Trusses w Piggy trusses** требуют `2x6 bearing plates` `4' o.c.`
- **Flat curb blocking** на flat roofs — `(2) 2x6 PT`, если ничего не указано и нет детали.
- **Exact stud height** — считать вручную: `9'`, `9'1-1/8"`, `9'1-1/4"` и т.п.
- Всегда следовать **S-details**, когда они есть.
- **Exterior Sheathing** по Arch plans (если Structural не даёт более точную инфу). **Interior sheathing** — по Structural.
- **Blocking around windows** — особенно когда используется Insulation или Zip R sheathing.
- `1x3 PT strapping` под siding типа Hardi paneling — если указано.
- **Любые Exterior buildouts** — стик-фрейм, не панели.
- Все новые формулы **проверять сразу**, не потом.
- **Shaft walls** — не пропускать.
- **Dropped Soffits** — проверять RCP pages. Может быть `2x4 soffit frame` в bath или в коридоре.
- **Soffit plywood** под Roof trusses — возможно.
- Под **Podium** или внутри существующего здания — **не панели**.

<!-- confluence-gallery:start -->
## Картинки из Confluence

Изображения из Confluence размещены на этой странице по исходной теме.
Подпись сохраняет группу-источник, чтобы можно было быстро проверить контекст.

| Группа источника | Картинки | Confluence |
| --- | ---: | --- |
| COM Commercial Job | 13 | [source](https://ewood.atlassian.net/wiki/spaces/work/pages/2359297/COM+Commercial+Job) |

<div class="kb-gallery">
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-053.png" title="image-20250722-030816.png">
    <img src="../../assets/images/confluence/confluence-053.png" alt="COM Commercial Job - COM takeoff workflow/reference 01">
    <div class="kb-gallery__caption">COM takeoff workflow/reference 01</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-054.png" title="image-20250717-232520.png">
    <img src="../../assets/images/confluence/confluence-054.png" alt="COM Commercial Job - COM takeoff workflow/reference 02">
    <div class="kb-gallery__caption">COM takeoff workflow/reference 02</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-055.png" title="image-20250619-192434.png">
    <img src="../../assets/images/confluence/confluence-055.png" alt="COM Commercial Job - COM takeoff workflow/reference 03">
    <div class="kb-gallery__caption">COM takeoff workflow/reference 03</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-056.png" title="image-20250619-192242.png">
    <img src="../../assets/images/confluence/confluence-056.png" alt="COM Commercial Job - COM takeoff workflow/reference 04">
    <div class="kb-gallery__caption">COM takeoff workflow/reference 04</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-057.png" title="image-20250619-192221.png">
    <img src="../../assets/images/confluence/confluence-057.png" alt="COM Commercial Job - COM takeoff workflow/reference 05">
    <div class="kb-gallery__caption">COM takeoff workflow/reference 05</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-058.png" title="image-20250619-192136.png">
    <img src="../../assets/images/confluence/confluence-058.png" alt="COM Commercial Job - COM takeoff workflow/reference 06">
    <div class="kb-gallery__caption">COM takeoff workflow/reference 06</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-059.png" title="image-20250619-191959.png">
    <img src="../../assets/images/confluence/confluence-059.png" alt="COM Commercial Job - COM takeoff workflow/reference 07">
    <div class="kb-gallery__caption">COM takeoff workflow/reference 07</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-060.png" title="image-20250619-191937.png">
    <img src="../../assets/images/confluence/confluence-060.png" alt="COM Commercial Job - COM takeoff workflow/reference 08">
    <div class="kb-gallery__caption">COM takeoff workflow/reference 08</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-061.png" title="image-20250210-115947.png">
    <img src="../../assets/images/confluence/confluence-061.png" alt="COM Commercial Job - COM takeoff workflow/reference 09">
    <div class="kb-gallery__caption">COM takeoff workflow/reference 09</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-062.png" title="image-20250210-115939.png">
    <img src="../../assets/images/confluence/confluence-062.png" alt="COM Commercial Job - COM takeoff workflow/reference 10">
    <div class="kb-gallery__caption">COM takeoff workflow/reference 10</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-063.png" title="image-20250210-115920.png">
    <img src="../../assets/images/confluence/confluence-063.png" alt="COM Commercial Job - COM takeoff workflow/reference 11">
    <div class="kb-gallery__caption">COM takeoff workflow/reference 11</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-064.png" title="image-20250210-115909.png">
    <img src="../../assets/images/confluence/confluence-064.png" alt="COM Commercial Job - COM takeoff workflow/reference 12">
    <div class="kb-gallery__caption">COM takeoff workflow/reference 12</div>
  </a>
  <a class="kb-gallery__item" href="../../assets/images/confluence/confluence-065.png" title="image-20250210-115855.png">
    <img src="../../assets/images/confluence/confluence-065.png" alt="COM Commercial Job - COM takeoff workflow/reference 13">
    <div class="kb-gallery__caption">COM takeoff workflow/reference 13</div>
  </a>
</div>
<!-- confluence-gallery:end -->
