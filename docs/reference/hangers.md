# Hangers

Hanger выбирается не "по названию на глаз", а по condition: какой member
несём, куда он садится, какой mount type, есть ли skew/slope/firewall, и что
показывает project schedule.

<div class="kb-split" markdown>

!!! tip "Выбор за 30 секунд"
    1. Определи member: `Beam/LVL/PSL/GL`, `TJI`, `LPI`, double joist.
    2. Определи mount: `Face Mount`, `Top Flange`, `Concealed Flange`.
    3. Проверь depth: joists over 16" обычно уходят в `HIT`, не `ITS`.
    4. Проверь skew/slope: `ITS` не skewable.
    5. Проверь special condition: firewall/double gypsum, Cedar, glulam, shearwall.

<figure markdown>
  ![Hanger selection flow for common estimating decisions](../assets/images/hangers/hanger-selection-flow.svg)
  <figcaption>Схема выбора: сначала mount condition, потом depth, skew и special conditions.</figcaption>
</figure>

</div>

## Быстрый выбор

<div class="grid cards" markdown>

-   :material-view-column-outline: **Face Mount**

    ---

    Hanger висит на face of support. Часто это `HU`, `HHUS`, `HGUS`, `IUS`,
    `MIU`, `SUL/SUR`.

-   :material-dock-top: **Top Flange**

    ---

    Hanger садится сверху на support. Для joists это часто `ITS/MIT`, для beam
    conditions - `WP`, `GLT/GLTV`, `LBV`.

-   :material-vector-square: **Concealed Flange**

    ---

    Flange скрыт внутри соединения. Проверяй `HUC/HUCQ`, fasteners и detail:
    такой hanger нельзя просто заменить на обычный face mount.

-   :material-angle-acute: **Skew / Slope**

    ---

    Если есть угол, не ставь `ITS`. Для face mount смотри `SUL/SUR`, для top
    flange - `LBV`, для LPI slope/skew - `LSSU/LSSUH/LSSUI`.

-   :material-alert-octagon-outline: **Deep Joist**

    ---

    Joists больше 16" - обычно `HIT` family, например `HIT420`. `ITS`
    использовать только до 16" включительно.

-   :material-fire-alert: **Firewall / Double Gypsum**

    ---

    `DHU/DGU` относятся к double-gypsum/firewall conditions. Не применяй их к
    обычному joist-to-beam condition без detail.

</div>

## Критические правила

- `ITS` - только top-flange I-joist hanger и только до 16" depth включительно.
- `ITS` нельзя использовать для skewed condition.
- Для skewed top mount используй `WP/HUTF/LBV` family по detail/schedule.
- Для skewed face mount используй `SUL/SUR/HSUR` family.
- Для EWP (`LVL`, `PSL`, `GL`, `TJI`, `LPI`, `RED`) оставляй точный product
  family и section. Не превращай всё в generic hanger.
- Если hanger повторяется через repeated framing area, перепроверь quantity:
  repeat change может удвоить hanger count.
- Final selection всегда сверяй с structural notes, details и project
  schedule. Таблица ниже - быстрая подсказка, не замена engineer detail.

## Как читать Hanger code

`ITS2.37/11.88`

| Часть | Что значит | Пример |
| --- | --- | --- |
| `ITS` | I-joist top-flange hanger family | top mount для TJI/LPI |
| `2.37` | flange width carried member | примерно 2 5/16" |
| `11.88` | joist depth | 11 7/8" |

!!! note "Быстрый перевод размеров"
    - `1.81` примерно 1 3/4".
    - `2.06` примерно 2 1/16".
    - `2.37` примерно 2 5/16".
    - `3.56` примерно 3 1/2".
    - `11.88` = 11 7/8", `9.5` = 9 1/2".

## Визуальные типы

<details class="kb-figures kb-figures--rows" open>
  <summary>Скрыть 5 правил с иллюстрациями</summary>
  <figure class="kb-figure-row">
    <figcaption class="kb-figure-row__text">
      <div class="kb-figure-row__title">Face Mount</div>
      <div class="kb-figure-row__rule">Hanger крепится к боковой стороне support.</div>
      <div class="kb-figure-row__note">Проверяй section, carried member depth и есть ли skew.</div>
    </figcaption>
    <a class="kb-figure-row__image" href="../../assets/images/confluence/confluence-080.png" target="_blank" rel="noopener"><img src="../../assets/images/confluence/confluence-080.png" alt="Face mount hanger on side of support" loading="lazy"></a>
  </figure>
  <figure class="kb-figure-row">
    <figcaption class="kb-figure-row__text">
      <div class="kb-figure-row__title">Top Flange</div>
      <div class="kb-figure-row__rule">Flange садится сверху на beam/wall/support.</div>
      <div class="kb-figure-row__note">Для I-joist обычно смотри <code>ITS/MIT</code>; для beam top mount - <code>WP/GLT/LBV</code>.</div>
    </figcaption>
    <a class="kb-figure-row__image" href="../../assets/images/confluence/confluence-081.png" target="_blank" rel="noopener"><img src="../../assets/images/confluence/confluence-081.png" alt="Top flange hanger sitting over support" loading="lazy"></a>
  </figure>
  <figure class="kb-figure-row">
    <figcaption class="kb-figure-row__text">
      <div class="kb-figure-row__title">Concealed Flange</div>
      <div class="kb-figure-row__rule">Flange скрыт; чаще <code>HUC/HUCQ</code> family.</div>
      <div class="kb-figure-row__note">Сверяй fastener note/detail. Не заменяй на обычный <code>HU</code> без причины.</div>
    </figcaption>
    <a class="kb-figure-row__image" href="../../assets/images/confluence/confluence-082.png" target="_blank" rel="noopener"><img src="../../assets/images/confluence/confluence-082.png" alt="Concealed flange hanger" loading="lazy"></a>
  </figure>
  <figure class="kb-figure-row">
    <figcaption class="kb-figure-row__text">
      <div class="kb-figure-row__title">CBH for Glulam</div>
      <div class="kb-figure-row__rule"><code>CBH2.37X9.75C-KT</code> - special glulam condition.</div>
      <div class="kb-figure-row__note">Используй только когда detail/schedule показывает glulam/Cedar-style special connection.</div>
    </figcaption>
    <a class="kb-figure-row__image" href="../../assets/images/confluence/confluence-030.png" target="_blank" rel="noopener"><img src="../../assets/images/confluence/confluence-030.png" alt="CBH hanger for glulam condition" loading="lazy"></a>
  </figure>
  <figure class="kb-figure-row">
    <figcaption class="kb-figure-row__text">
      <div class="kb-figure-row__title">CJTZ for Cedar</div>
      <div class="kb-figure-row__rule"><code>CJTZ</code> - special item для Cedar beams/posts.</div>
      <div class="kb-figure-row__note">Не смешивай с обычными beam hangers; это отдельная строка в output.</div>
    </figcaption>
    <a class="kb-figure-row__image" href="../../assets/images/confluence/confluence-031.png" target="_blank" rel="noopener"><img src="../../assets/images/confluence/confluence-031.png" alt="CJTZ installation for Cedar beam and post" loading="lazy"></a>
  </figure>
</details>

## Подбор по condition

| Condition | Обычно смотреть | Не забыть |
| --- | --- | --- |
| LVL/PSL/GL face mount | `HU`, `HHUS`, `HGUS` | width built-up member: (2), (3), (4) LVL |
| LVL/PSL/GL concealed | `HUC`, `HUCQ` | concealed flange и fasteners |
| LVL/PSL/GL top flange | `WP`, `GLT`, `GLTV`, `LBV` | top seat, skew, support width |
| TJI/LPI top flange | `ITS`, `MIT`, `BA`, `LBV` | depth до 16" для `ITS`; double joists отдельно |
| TJI/LPI face mount | `IUS`, `MIU`, `HU`, `SUL/SUR` | face/skew condition |
| LPI field slope/skew | `LSSU`, `LSSUH`, `LSSUI` | left/right и actual angle по detail |
| Firewall / double gypsum | `DHU`, `DGU` | только если detail прямо показывает condition |
| Cedar / glulam special | `CJTZ`, `CBH` | separate line, не generic hanger |

## Быстрая таблица Hangers

=== "Beam Face Mount"

    | Member section | Hanger |
    | --- | --- |
    | 1 3/4 x 9 1/2 | `HU9` |
    | 1 3/4 x 11 7/8 | `HU11` |
    | 1 3/4 x 14 | `HU14` |
    | 3 1/2 x 9 1/2 | `HU410` / `HHUS410` |
    | 3 1/2 x 11 7/8 | `HU412` |
    | 3 1/2 x 14 | `HU414` |
    | 5 1/2 x 11 7/8 | `HU612` / `HHUS5.50/12` |
    | 5 1/4 x 9 1/2 | `HHUS5.50/10` |
    | 7 x 11 7/8 | `HGUS7.25/12` |
    | 1 3/4 x 11 7/8 skew left 45 | `SUL1.81/11` |
    | 1 3/4 x 11 7/8 skew right 45 | `SUR1.81/11` |

=== "Beam Concealed"

    | Member section | Hanger |
    | --- | --- |
    | 1 3/4 x 9 1/2 | `HUCQ1.81/9` |
    | 1 3/4 x 11 7/8 | `HUCQ1.81/11` |
    | 3 1/2 x 11 7/8 | `HUCQ412 SDS` |
    | 5 1/2 x 9 1/2 | `HUCQ610` |
    | 3 1/2 x 9 1/2 | `HUC410` |
    | 3 1/2 x 11 7/8 | `HUC412` |
    | 3 1/2 x 14 | `HUC414` |
    | 5 1/4 x 11 7/8 | `HUC612` |

=== "Beam Top Flange"

    | Member section / condition | Hanger |
    | --- | --- |
    | 1 3/4 x 9 1/2 | `WP9` |
    | 1 3/4 x 11 7/8 | `WP11` |
    | 1 3/4 x 14 | `WP14` |
    | 1 3/4 x 16 | `WP16` |
    | 1 3/4 x 11 7/8 skew left 45 | `LBV1.81/11.88XL45` |
    | 1 3/4 x 11 7/8 skew right 45 | `LBV1.81/11.88XR45` |
    | 3 1/2 x 9 1/2 | `MIT49.5` / `GLTV3.59` |
    | 3 1/2 x 11 7/8 | `GLTV3.511` / `GLT4/11.88` |
    | 3 1/2 x 14 | `GLTV3.514` |
    | 5 1/2 x 11 7/8 | `GLTV5.511` / `GLT6/11.88` |
    | 5 1/2 x 14 | `GLTV5.5/14` |
    | 7 x 11 7/8 | `HGLTV411.88 2` |

=== "TJI"

    | Joist | Top flange | Face mount |
    | --- | --- | --- |
    | 11 7/8 TJI 110 | `ITS1.81/11.88` | `IUS1.81/11.88` |
    | 11 7/8 TJI 210 | `ITS2.06/11.88` | `IUS2.06/11.88` |
    | 11 7/8 TJI 230 / 360 | `ITS2.37/11.88` | `IUS2.37/11.88` |
    | 11 7/8 TJI 560 | `ITS3.56/11.88` | `IUS3.56/11.88` |
    | (2) 11 7/8 TJI 110 | `MIT3.12/11.88` | `MIU3.12/11` |
    | (2) 11 7/8 TJI 210 | `MIT4.12/11.88` | `MIU4.12/11` |
    | (2) 11 7/8 TJI 360 | `MIT4.75/11.88` | `MIU4.75/11` |
    | (2) 11 7/8 TJI 560 | `BA412-2` | `HU412-2` |

=== "LPI"

    | Joist | Top flange | Face mount |
    | --- | --- | --- |
    | 9 1/2 LPI 18/20/32 | `ITS2.56/9.5` | `IUS2.56/9.5` |
    | 11 7/8 LPI 18/20/32 | `ITS2.56/11.88` | `IUS2.56/11.88` |
    | 14 LPI 18/20/32 | `ITS2.56/14` | `IUS2.56/14` |
    | 11 7/8 LPI 36 | `ITS2.37/11.88` | `IUS2.37/11.88` |
    | 14 LPI 36 | `ITS2.37/14` | `IUS2.37/14` |
    | 11 7/8 LPI 56 | `ITS3.56/11.88` | `IUS3.56/11.88` |
    | 14 LPI 56 | `ITS3.56/14` | `IUS3.56/14` |
    | Double 9 1/2 LPI 18/20/32 | `MIT39.5 2` | `MIU5129` |
    | Double 11 7/8 LPI 36 | - | `MIU4.75/11` |

=== "Skew / Slope"

    | Condition | Hanger |
    | --- | --- |
    | LPI 56 field slope and skew | `LSSU410` |
    | LPI 18/20/32 field slope and skew | `LSSUH310` |
    | LPI 36 field slope and skew | `LSSUI35` |
    | LPI 18/20/32 skew left 45 | `SUL2.56/9` |
    | LPI 18/20/32 skew right 45 | `SUR2.56/9` |
    | LPI 36 skew left 45 | `SUL2.37/9` |
    | LPI 36 skew right 45 | `SUR2.37/9` |
    | LPI 18/20/32 top flange skew left | `LBV2.56/9.5XL45` / `LBV2.56/11.88XL45` |
    | LPI 18/20/32 top flange skew right | `LBV2.56/9.5XR45` / `LBV2.56/11.88XR45` |

## Особые позиции

| Item | Когда использовать | Проверка перед output |
| --- | --- | --- |
| `CJTZ` | Cedar beams/posts | Должен быть Cedar/detail callout |
| `CBH2.37X9.75C-KT` | Glulam special connection | Сверить glulam condition и carried member |
| `A35 clips` | Shearwall connections | Только если требуют general notes/details |
| `Simpson HDU4-SDS2.5` | Holdown condition | Double if sits on wall at upper floors; single if directly on LVL/steel beam |
| `DHU/DGU` | Double-gypsum/firewall | Не использовать без firewall/double gypsum detail |

## Финальная проверка

- Сверь hanger family, size, skew, top/face mount и support condition.
- Если на плане есть schedule, он важнее default table.
- Если connection выглядит нестандартно, открой detail и не угадывай по
  миниатюре.
- Для repeated areas проверь, что count повторился столько же раз, сколько
  framing.
