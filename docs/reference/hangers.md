# Hangers

<figure markdown>
  ![Hanger selection flow for common estimating decisions](../assets/images/hangers/hanger-selection-flow.svg)
  <figcaption>Быстрый выбор hanger: сначала mount condition, потом depth, skew и firewall condition.</figcaption>
</figure>

## Основные правила выбора

- Joists 16" и ниже могут использовать ITS, если подходит top-flange hanger.
- Joists over 16" используют HIT hangers, например HIT420.
- ITS нельзя skew.
- Skewed top mount: используй WP / HUTF family.
- Skewed face mount: используй SUR / HSUR family.
- DHU/DGU — только для double-gypsum/firewall conditions; проверяй details.

## Быстрые проверки

| Вопрос | Почему важно |
| --- | --- |
| Joist глубже 16"? | Обычно это меняет ITS на HIT |
| Hanger skewed? | ITS не skewable; используй WP/HUTF или SUR/HSUR family |
| Это face mount или top flange? | Меняет HU/HUC/IUS vs ITS/WP/GLTV |
| Есть double gypsum/firewall? | DHU/DGU относится только к таким conditions |
| Это beam, glulam или Cedar member? | Может требовать HHUS/HGUS/CBH/CJTZ special item |

## Как читать ITS

`ITS2.37/11.88`

- `ITS` = I-joist top-flange hanger.
- `2.37` = joist flange width, примерно 2 5/16".
- `11.88` = joist height, 11 7/8".

## Beam Face Mount

| Section | Hanger |
| --- | --- |
| 1 3/4 x 9 1/2 | HU9 |
| 1 3/4 x 11 7/8 | HU11 |
| 1 3/4 x 14 | HU14 |
| 3 1/2 x 9 1/2 | HU410 |
| 3 1/2 x 11 7/8 | HU412 |
| 3 1/2 x 14 | HU414 |
| 5 1/2 x 11 7/8 | HU612 |
| 3 1/2 x 9 1/2 | HHUS410 |
| 5 1/4 x 9 1/2 | HHUS5.50/10 |
| 7 x 11 7/8 | HGUS7.25/12 |
| 1 3/4 x 11 7/8 skew left 45 | SUL1.81/11 |
| 1 3/4 x 11 7/8 skew right 45 | SUR1.81/11 |

## Beam Concealed

| Section | Hanger |
| --- | --- |
| 1 3/4 x 9 1/2 | HUCQ1.81/9 |
| 1 3/4 x 11 7/8 | HUCQ1.81/11 |
| 3 1/2 x 11 7/8 | HUCQ412 SDS |
| 5 1/2 x 9 1/2 | HUCQ610 |
| 3 1/2 x 9 1/2 | HUC410 |
| 3 1/2 x 11 7/8 | HUC412 |
| 3 1/2 x 14 | HUC414 |
| 5 1/4 x 11 7/8 | HUC612 |

## Beam Top Flange

| Section | Hanger |
| --- | --- |
| 1 3/4 x 9 1/2 | WP9 |
| 1 3/4 x 11 7/8 | WP11 |
| 1 3/4 x 14 | WP14 |
| 3 1/2 x 9 1/2 | GLTV3.59 |
| 3 1/2 x 11 7/8 | GLTV3.511 |
| 3 1/2 x 14 | GLTV3.514 |
| 5 1/2 x 11 7/8 | GLTV5.511 |
| 5 1/2 x 14 | GLTV5.5/14 |

## TJI Top Flange

| Joist | Hanger |
| --- | --- |
| 11 7/8 TJI 110 | ITS1.81/11.88 |
| 11 7/8 TJI 210 | ITS2.06/11.88 |
| 11 7/8 TJI 230 / 360 | ITS2.37/11.88 |
| 11 7/8 TJI 560 | ITS3.56/11.88 |
| (2) 11 7/8 TJI 110 | MIT3.12/11.88 |
| (2) 11 7/8 TJI 210 | MIT4.12/11.88 |
| (2) 11 7/8 TJI 360 | MIT4.75/11.88 |
| (2) 11 7/8 TJI 560 | BA412-2 |

## LPI

| Joist | Face mount | Top flange |
| --- | --- | --- |
| 9 1/2 LPI 18/20/32 | IUS2.56/9.5 | ITS2.56/9.5 |
| 11 7/8 LPI 18/20/32 | IUS2.56/11.88 | ITS2.56/11.88 |
| 14 LPI 18/20/32 | IUS2.56/14 | ITS2.56/14 |
| 11 7/8 LPI 36 | IUS2.37/11.88 | ITS2.37/11.88 |
| 11 7/8 LPI 56 | IUS3.56/11.88 | ITS3.56/11.88 |

## Special

- CJTZ для Cedar beams/posts.
- CBH2.37X9.75C-KT для glulam.
- A35 clips на shearwall connections, если требуют general notes.
- После converting repeated hanger counts перепроверь hanger quantity. Framing
  repeat change может удвоить hanger count тоже.
- `Simpson HDU4-SDS2.5`: double, когда sits on a wall at upper floors; single,
  когда sits directly on an LVL/steel beam.


<!-- confluence-gallery:start -->
## Визуальная проверка

Эти картинки уже привязаны к правилам страницы. Используй их как быстрые
checkpoint-ы перед output: сначала прочитай правило выше, потом открой нужную
карточку и проверь похожий condition на плане/schedule.

??? info "Источник картинок"
    - Hangers - Крепления: [4 карт. Confluence](https://ewood.atlassian.net/wiki/spaces/work/pages/4816897/Hangers+-)
    - Hangers and Ties Schedule: [2 карт. Confluence](https://ewood.atlassian.net/wiki/spaces/work/pages/12124257/Hangers+and+Ties+Schedule)

<div class="kb-rule-gallery">
  <a class="kb-rule-card" href="../../assets/images/confluence/confluence-030.png" title="image-20250224-000530.png">
    <img src="../../assets/images/confluence/confluence-030.png" alt="Hanger - schedule/detail проверка 01: Сверь hanger family, size, skew, top/face mount и support condition.">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Hanger - schedule/detail проверка 01</div>
      <div class="kb-rule-card__rule">Сверь hanger family, size, skew, top/face mount и support condition.</div>
      <div class="kb-rule-card__note">Hanger не выбирается только по ширине: смотри material, bearing и detail.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../assets/images/confluence/confluence-031.png" title="image-20250224-000451.png">
    <img src="../../assets/images/confluence/confluence-031.png" alt="Hanger - schedule/detail проверка 02: Сверь hanger family, size, skew, top/face mount и support condition.">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Hanger - schedule/detail проверка 02</div>
      <div class="kb-rule-card__rule">Сверь hanger family, size, skew, top/face mount и support condition.</div>
      <div class="kb-rule-card__note">Hanger не выбирается только по ширине: смотри material, bearing и detail.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../assets/images/confluence/confluence-079.png" title="image-20250211-180817.png">
    <img src="../../assets/images/confluence/confluence-079.png" alt="Hanger - schedule/detail проверка 03: Сверь hanger family, size, skew, top/face mount и support condition.">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Hanger - schedule/detail проверка 03</div>
      <div class="kb-rule-card__rule">Сверь hanger family, size, skew, top/face mount и support condition.</div>
      <div class="kb-rule-card__note">Hanger не выбирается только по ширине: смотри material, bearing и detail.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../assets/images/confluence/confluence-080.png" title="image-20250211-180929.png">
    <img src="../../assets/images/confluence/confluence-080.png" alt="Hanger - schedule/detail проверка 04: Сверь hanger family, size, skew, top/face mount и support condition.">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Hanger - schedule/detail проверка 04</div>
      <div class="kb-rule-card__rule">Сверь hanger family, size, skew, top/face mount и support condition.</div>
      <div class="kb-rule-card__note">Hanger не выбирается только по ширине: смотри material, bearing и detail.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../assets/images/confluence/confluence-081.png" title="image-20250211-181023.png">
    <img src="../../assets/images/confluence/confluence-081.png" alt="Hanger - schedule/detail проверка 05: Сверь hanger family, size, skew, top/face mount и support condition.">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Hanger - schedule/detail проверка 05</div>
      <div class="kb-rule-card__rule">Сверь hanger family, size, skew, top/face mount и support condition.</div>
      <div class="kb-rule-card__note">Hanger не выбирается только по ширине: смотри material, bearing и detail.</div>
    </div>
  </a>
  <a class="kb-rule-card" href="../../assets/images/confluence/confluence-082.png" title="image-20250211-181056.png">
    <img src="../../assets/images/confluence/confluence-082.png" alt="Hanger - schedule/detail проверка 06: Сверь hanger family, size, skew, top/face mount и support condition.">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Hanger - schedule/detail проверка 06</div>
      <div class="kb-rule-card__rule">Сверь hanger family, size, skew, top/face mount и support condition.</div>
      <div class="kb-rule-card__note">Hanger не выбирается только по ширине: смотри material, bearing и detail.</div>
    </div>
  </a>
</div>
<!-- confluence-gallery:end -->
