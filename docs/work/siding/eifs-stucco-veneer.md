# EIFS / Stucco / Veneer (облицовка by others)

<figure markdown>
  ![EIFS, stucco and veneer are by others](../../assets/images/siding/eifs-stucco-veneer.svg)
  <figcaption markdown="span">Finish-системы by others. WRB, sheathing, furring и wood/PVC trim вокруг них наши. J-channel наш только при vinyl siding.</figcaption>
</figure>

<figure markdown>
  ![Слои EIFS: плиты EPS, сетка и base coat](../../assets/images/photos/siding/eifs-eps-mesh-base-coat.jpg){ width="520" }
  <figcaption markdown="span">EIFS в работе: плиты EPS на тарельчатых дюбелях, поверх стеклосетка, которую втирают в base coat. Всё это by others; наши строки - sheathing и WRB под плитами и trim по краям. Фото: estimatingedge.com, [источник](https://www.estimatingedge.com/construction/eifs/), найдено через Pinterest.</figcaption>
</figure>
<figure markdown>
  ![Scratch coat штукатурки по metal lath на стене дома](../../assets/images/photos/siding/stucco-scratch-coat-over-lath.jpg){ width="420" }
  <figcaption markdown="span">Three-coat stucco: первый слой (scratch coat) с бороздами поверх metal lath, окна заклеены. Stucco by others; наш scope под ним - sheathing, WRB и wood trim у проёмов. Фото: hometips.com, [источник](https://www.hometips.com/buying-guides/walls-siding-stucco.html), найдено через Pinterest.</figcaption>
</figure>
<figure markdown>
  ![Укладка stone veneer на scratch coat по metal lath](../../assets/images/photos/siding/stone-veneer-over-lath-scratch-coat.jpg){ width="420" }
  <figcaption markdown="span">Adhered stone veneer: сверху видна metal lath, ниже scratch coat, на него на раствор кладут камень. Весь пакет by others; под ним наши sheathing и WRB, по краям wood trim. Фото: mountainviewstone.net, [источник](https://mountainviewstone.net/blogs/carved-in-stone/can-you-install-stone-veneer-over-drywall), найдено через Pinterest.</figcaption>
</figure>

## Что это

EIFS, stucco, stone veneer и brick veneer тоже наружная облицовка стен, но
это отдельные trades. В нашем scope (wood, EWP, vinyl, fiber cement и trim)
сам finish не считаем. Считаем то, что под ним и вокруг: WRB, sheathing,
furring, wood/PVC trim, soffit, fascia.

## Как распознать на чертежах

=== "EIFS"

    Exterior Insulation and Finish System, "синтетическая штукатурка":
    adhesive, insulation board (EPS), base coat с fiberglass mesh, finish
    coat. Notes `EIFS`, `Synthetic Stucco`, `Dryvit`, `Sto`, `Senergy`,
    `1" / 2" EIFS`; на разрезе insulation board и тонкие слои с mesh; на
    фасаде гладкие поля с reveals и expansion joints. By others (EIFS sub).

=== "Stucco"

    Цементная штукатурка, обычно 3-coat (scratch, brown, finish) по metal
    lath и WRB. Notes `Stucco`, `3-coat stucco`, `Cement plaster`,
    `Portland`; на разрезе lath и три слоя, weep screed по низу. By others
    (plaster trade).

=== "Stone veneer"

    Облицовочный камень, manufactured или natural, adhered на scratch coat
    или anchored. Notes `Stone Veneer`, `Cultured Stone`, `Manufactured
    Stone`; hatch камня на фасаде; на разрезе WRB, lath, scratch coat,
    stone. By others (mason).

=== "Brick veneer"

    Кирпичная облицовка с воздушным зазором, brick ties к каркасу, weep
    holes, lintels и shelf angles. Notes `Brick Veneer`, `Brick`, brick
    hatch; на разрезе air gap, ties, weeps. By others (mason).

## Что считаем рядом

| Элемент | Считаем? |
| --- | --- |
| WRB под облицовкой (по спецификации) | да, проверить scope; на стенах из Zip строки WRB нет, только `Tape` |
| Sheathing (CDX, OSB, Zip) | да, свой scope |
| Furring и каркас под облицовку | да, если показан |
| Wood / PVC trim, corner, band, soffit, fascia | да |
| Сам EIFS, stucco, stone, brick | нет |
| Lath, base coat, brick ties, shelf angle, casing bead | нет, by others |

- Нота обязательна, первой под заголовком Siding: `Note: Stone Veneer
  materials are by others`, `Note: EIFS, Stone and Brick Veneer materials
  are by others` (перечисли то, что есть на фасадах).
- Весь фасад EIFS, stucco или stone: siding `0 SQ FT` плюс нота, trim
  почти нулевой. Не добивай количество.
- Accessory EIFS и stucco (casing bead, stop bead, track, expansion joint)
  идут с системой by others. J-channel при vinyl siding наш; канон:
  [Exclusions и J-Channel](../exterior-trims/exclusions.md).

## Как мерить в OurPlanCore

Отдельный takeoff на облицовку by others не нужен. Площадь стен под ней
нужна для WRB и sheathing: она берётся из `walls` и высоты стен, а не из
фасада. Trim вокруг облицовки считается как обычно в `trims`.

## Частые ошибки

- Stone или brick veneer посчитаны как siding или как наша кладка.
- WRB и sheathing под EIFS пропущены, потому что "стена by others".
- На стенах из Zip под облицовкой добавлена строка WRB: у Zip барьер в листе, считается только `Tape`.
- Casing bead EIFS записан как наш J-channel.
- Нота by others не поставлена.
- Все ошибки по обшивке и WRB: [Обшивка](../../start/common-mistakes.md#sheathing).

## Пример

```text
Note: EIFS and Stone Veneer materials are by others
Siding          Per plans: EIFS by others     0      SQ FT
Wall Sheathing  7/16" Zip                     215    4x8     =CEILING(6250/32*1.1,1)           8/S3.0
Tape            Zip Tape                      3460   LFT     =CEILING((6250*0.4+640)*1.1,10)
Corner Boards   5/4x6 PVC                     124    LFT     =EVEN(56*2*1.1)                   A201

Стены на Zip: строки Vapor Barrier (WRB) нет, барьер встроен в лист
Sheathing: 6250 / 32 = 195.3, x 1.1 = 214.8, вверх до целого = 215 листов
Tape: 6250 x 0.4 = 2500, + 640 LFT периметра проёмов = 3140, x 1.1 = 3454, вверх до 10 = 3460
Corner Boards: 2 угла x 28' = 56, две доски на угол: 56 x 2 x 1.1 = 123.2, чётное вверх = 124
```

## См. также

- [Siding](overview.md), [Underlayment](underlayment.md), [Измерение](measure.md)
- [Exclusions и J-Channel](../exterior-trims/exclusions.md), [Casing, Corner & Band](../exterior-trims/casing-corner-band.md)
- [Wall Sheathing](../vertical/sheathing/wall-sheathing.md), [Standard notes](../../reference/standard-notes.md)
