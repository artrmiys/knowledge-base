# Beam

## Что считать

- LVL, PSL, GL, and other beams by size, ply count, and length.
- Hangers connected to beams.

## Правила

- Mark beams top-down / left-right.
- Length depends on the bearing/attachment point.
- Lengths 8' and longer round to 2' increments.
- Lengths under 8' stay exact.
- In EWP jobs, ordinary 2x beams are usually excluded.

## Standard Built-Up Sizes

| Callout | Actual built-up size |
| --- | --- |
| (2) 1 3/4 x 9 1/2 LVL | 3 1/2 x 9 1/2 |
| (3) 1 3/4 x 9 1/2 LVL | 5 1/4 x 9 1/2 |
| (4) 1 3/4 x 9 1/2 LVL | 7 x 9 1/2 |

## Проверить

- Steel top nailers or steel beam web fillers can drive separate material lines.
- Hanger selection depends on face/top/concealed/skewed condition.
- For `Tri-Force` and beams with steel plates, write nearest foot sizes; do not
  leave noisy inch fractions in the size.

## EWP Materials

Для **EWP** (Engineered Wood Products) обычные деревянные балки **2x10 / 4x12 / 6x14** не учитываем — только инженерные:

- **LVL** (Laminated Veneer Lumber, Versa Lam) — клееный брус, прочный, устойчив к деформациям.
- **PSL** (Parallel Strand Lumber) — параллельные волокна, высокая несущая способность.
- **GL** (Glued Laminated Timber, Glu Lam) — многослойный клееный брус из ламелей.

## Вывод Example

Запись балок и hangers в Excel/PlanSwift (поля: **Description**, **Size**, **Quantities**, **Units**):

| Description | Size | Qty | Units |
| --- | --- | ---: | --- |
| Beam `(3)` | `1 3/4 x 9 1/2 LVL` | 3 | 12 |
| Beam `(1)` | `5 1/2 x 11 7/8 GL` | 1 | 20 |
| Beam `(2)` | `1 3/4 x 11 7/8 LVL` | 2 | 10 |
| Hangers | `HU412` | 10 | pcs |
| Hangers | `HGUS7.25/12` | 20 | pcs |
| Hangers | `GLTV3.514` | 5 | pcs |
| Hangers | `for 7 x 11 7/8` | 10 | pcs |

Длины snap-ятся при scaling — например `scaled 12' 0 1/8"` округляем до `12`.

См. [Hangers](../../../reference/hangers.md) для подбора крепления под ширину/высоту built-up.

<!-- confluence-gallery:start -->
## Визуальная проверка

Эти картинки уже привязаны к правилам страницы. Используй их как быстрые
checkpoint-ы перед output: сначала прочитай правило выше, потом открой нужную
карточку и проверь похожий condition на плане/schedule.

??? info "Источник картинок"
    - Beam - Балки: [4 карт. Confluence](https://ewood.atlassian.net/wiki/spaces/work/pages/3735554/Beam+-)

<div class="kb-rule-gallery">
  <a class="kb-rule-card" href="../../../../assets/images/confluence/confluence-071.png" title="image-20250211-181056.png">
    <img src="../../../../assets/images/confluence/confluence-071.png" alt="Beam - визуальная проверка 01: Проверь size, ply count, length, bearing и hanger condition.">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Beam - визуальная проверка 01</div>
      <div class="kb-rule-card__rule">Проверь size, ply count, length, bearing и hanger condition.</div>
      <div class="kb-rule-card__note">Если картинка показывает special condition, перенеси его в output row или note.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../../assets/images/confluence/confluence-072.png" title="image-20250211-181023.png">
    <img src="../../../../assets/images/confluence/confluence-072.png" alt="Beam - визуальная проверка 02: Проверь size, ply count, length, bearing и hanger condition.">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Beam - визуальная проверка 02</div>
      <div class="kb-rule-card__rule">Проверь size, ply count, length, bearing и hanger condition.</div>
      <div class="kb-rule-card__note">Если картинка показывает special condition, перенеси его в output row или note.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../../assets/images/confluence/confluence-073.png" title="image-20250211-180929.png">
    <img src="../../../../assets/images/confluence/confluence-073.png" alt="Beam - визуальная проверка 03: Проверь size, ply count, length, bearing и hanger condition.">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Beam - визуальная проверка 03</div>
      <div class="kb-rule-card__rule">Проверь size, ply count, length, bearing и hanger condition.</div>
      <div class="kb-rule-card__note">Если картинка показывает special condition, перенеси его в output row или note.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../../../assets/images/confluence/confluence-074.png" title="image-20250211-180817.png">
    <img src="../../../../assets/images/confluence/confluence-074.png" alt="Beam - визуальная проверка 04: Проверь size, ply count, length, bearing и hanger condition.">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Beam - визуальная проверка 04</div>
      <div class="kb-rule-card__rule">Проверь size, ply count, length, bearing и hanger condition.</div>
      <div class="kb-rule-card__note">Если картинка показывает special condition, перенеси его в output row или note.</div>
    </div>
  </a>
</div>
<!-- confluence-gallery:end -->
