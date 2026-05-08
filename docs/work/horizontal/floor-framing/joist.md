# Joist

<figure markdown>
  ![Joist run, rim, blocking, and support checkpoints](../../../assets/images/framing/joist-run-rim-blocking.svg)
  <figcaption>Joist runs: keep spacing, rim, blocking, supports, and hangers reviewable.</figcaption>
</figure>

## Count

- I-joists: TJI, LPI, RED, BCI, RFPI, Nordic.
- Joist hangers.
- Rim and blocking related to joist runs.
- Web stiffeners, squash blocks, or special blocking only when called out by
  details/general notes.

## Spacing

| Spacing | Factor |
| --- | ---: |
| 12" o.c. | 1.4667 |
| 16" o.c. | 1.1 |
| 24" o.c. | 0.625 |

## Rules

- Continue spacing top-down / left-right inside a run.
- Do not restart spacing from an inside beam.
- Remove joist only when it lands directly on top of beam, about plus/minus 2".
- For 18"/20"/22"/24" joists, use HIT hangers, not ITS.
- ITS is only for light floor applications up to 16".
- Keep joist depth/product visible in the row name: `11-7/8 TJI 230` is easier
  to review than a generic `TJI joist`.
- Treat top chord bearing conditions separately; they can change ribbon/rim and
  blocking requirements.

## Where To Look

| Drawing area | What to verify |
| --- | --- |
| Framing plan | Direction, spacing, depth, product family, repeated areas |
| Beam schedule | Support condition and hanger family |
| General notes | Web stiffeners, blocking rows, rim material, squash blocks |
| Details | Top chord bearing, skewed hangers, firewall conditions |

## Check

- Add a note when odd lengths are intentional.
- If joists are top chord bearing, ribbon board may not apply.
- Check that rim is still counted at roof TJI conditions.
- Do not split rim into 16' pieces unless the output format specifically asks
  for pieces.

## EWP Joist Materials

Для **EWP** учитываем только инженерные joists (обычные деревянные 2x — не считаем):

- **I-Joists** (двутавровые, OSB-стенка + LVL/OSB полки) — самый частый вариант.
- **LVL Joists** — для больших пролётов, прочные на изгиб.
- **PSL Joists** — высокие нагрузки, residential + COM.
- **GL Joists** — открытые балки, архитектурные решения.

### Common I-Joist series

`TJI` · `RED` · `LP` / `LPI` · `RFPI` · `BCI` (+ `s`) · `Nordic Joist` (`NI-20` / `NI-40x` / `NI-60`).

## Standard O.C. Spacing

Шаг (Spacing) меряется **on center (O.C.)** — от центра одной балки до центра следующей. Стандарты:

- `12" O.C.`
- `16" O.C.`
- `19.2" O.C.`
- `24" O.C.`

## Output Example

| Description | Size | Qty | Units |
| --- | --- | ---: | --- |
| Joists `16" o.c.` | `11 7/8 TJI 230` | 3 | 12 |
| Joists `16" o.c.` | `11 7/8 TJI 230` | 36 | 20 |
| Joists `16" o.c.` | `11 7/8 TJI 230` | 2 | 10 |
| Hangers | `ITS2.37/11.88` | `=ЧЁТН(lft * 12/16)` | pcs |

Формула для hangers по joists 16" O.C.: `=ЧЁТН(lft * 12 / spacing)` — округление вверх до чётного.


<!-- confluence-gallery:start -->
## Confluence Images

Изображения из Confluence размещены на этой странице по исходной теме.
Подпись сохраняет группу-источник, чтобы можно было быстро проверить контекст.

| Source group | Images | Confluence |
| --- | ---: | --- |
| Joist - Ригели | 1 | [source](https://ewood.atlassian.net/wiki/spaces/work/pages/3735565/Joist+-) |
| Joist Series | 10 | [source](https://ewood.atlassian.net/wiki/spaces/work/pages/11796606/Joist+Series) |

<div class="kb-gallery">
  <a class="kb-gallery__item" href="../../../../assets/images/confluence/confluence-001.png" title="image-20260225-174526.png">
    <img src="../../../../assets/images/confluence/confluence-001.png" alt="Joist Series - joist series/reference 01">
    <div class="kb-gallery__caption">joist series/reference 01 (image, 121 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../../../assets/images/confluence/confluence-002.png" title="image-20260225-174331.png">
    <img src="../../../../assets/images/confluence/confluence-002.png" alt="Joist Series - joist series/reference 02">
    <div class="kb-gallery__caption">joist series/reference 02 (image, 42 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../../../assets/images/confluence/confluence-003.png" title="image-20250414-190026.png">
    <img src="../../../../assets/images/confluence/confluence-003.png" alt="Joist Series - joist series/reference 03">
    <div class="kb-gallery__caption">joist series/reference 03 (image, 119 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../../../assets/images/confluence/confluence-004.png" title="image-20250303-145752.png">
    <img src="../../../../assets/images/confluence/confluence-004.png" alt="Joist Series - joist series/reference 04">
    <div class="kb-gallery__caption">joist series/reference 04 (image, 345 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../../../assets/images/confluence/confluence-005.png" title="image-20250224-002107.png">
    <img src="../../../../assets/images/confluence/confluence-005.png" alt="Joist Series - joist series/reference 05">
    <div class="kb-gallery__caption">joist series/reference 05 (image, 74 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../../../assets/images/confluence/confluence-006.png" title="image-20250224-001906.png">
    <img src="../../../../assets/images/confluence/confluence-006.png" alt="Joist Series - joist series/reference 06">
    <div class="kb-gallery__caption">joist series/reference 06 (image, 146 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../../../assets/images/confluence/confluence-007.png" title="image-20250224-001558.png">
    <img src="../../../../assets/images/confluence/confluence-007.png" alt="Joist Series - joist series/reference 07">
    <div class="kb-gallery__caption">joist series/reference 07 (image, 94 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../../../assets/images/confluence/confluence-008.png" title="image-20250224-001240.png">
    <img src="../../../../assets/images/confluence/confluence-008.png" alt="Joist Series - joist series/reference 08">
    <div class="kb-gallery__caption">joist series/reference 08 (image, 329 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../../../assets/images/confluence/confluence-009.png" title="image-20250224-001144.png">
    <img src="../../../../assets/images/confluence/confluence-009.png" alt="Joist Series - joist series/reference 09">
    <div class="kb-gallery__caption">joist series/reference 09 (image, 165 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../../../assets/images/confluence/confluence-010.png" title="image-20250224-000933.png">
    <img src="../../../../assets/images/confluence/confluence-010.png" alt="Joist Series - joist series/reference 10">
    <div class="kb-gallery__caption">joist series/reference 10 (image, 360 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../../../assets/images/confluence/confluence-075.png" title="image-20250211-185836.png">
    <img src="../../../../assets/images/confluence/confluence-075.png" alt="Joist - Ригели - joist layout/reference 01">
    <div class="kb-gallery__caption">joist layout/reference 01 (image, 40 KB raw)</div>
  </a>
</div>
<!-- confluence-gallery:end -->
