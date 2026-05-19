# EIFS / Stucco / Veneer

EIFS, Stucco, Stone veneer и Brick veneer — это тоже наружная облицовка
стен, но это **отдельные trade**. Для нашего scope (wood / EWP / vinyl /
fiber-cement + trim) они почти всегда **by others**.

!!! danger "Главное правило"
    **EIFS — не считаем. Stucco — не считаем. Stone Veneer — не считаем.
    Brick Veneer — не считаем.** Это finish/masonry by others. Считаем
    только то, что в нашем scope (WRB, sheathing, furring, wood/PVC trim).

## Что это и как распознать { .kb-section-title .kb-st--amber }

=== "EIFS"

    **EIFS** = Exterior Insulation and Finish System («синтетическая
    штукатурка»). Слои: adhesive → insulation board (EPS) → base coat +
    fiberglass mesh → finish coat.

    **Распознать:** notes `EIFS`, `Synthetic Stucco`, `Dryvit`, `Sto`,
    `Senergy`, `1" / 2" EIFS`; на разрезе — insulation board + тонкие слои с
    mesh; на elevation — гладкие поля с reveals/expansion joints.

    **Кто:** EIFS sub. **By others.**

=== "Stucco"

    **Stucco** = традиционная цементная штукатурка (обычно 3-coat: scratch →
    brown → finish) по metal lath / WRB.

    **Распознать:** notes `Stucco`, `3-coat stucco`, `Cement plaster`,
    `Portland`; на разрезе — lath + 3 слоя; weep screed по низу.

    **Кто:** plaster trade. **By others.**

=== "Stone veneer"

    **Stone veneer** = облицовочный камень (manufactured/cultured или
    natural), adhered (на mortar/scratch coat) или anchored.

    **Распознать:** notes `Stone Veneer`, `Cultured Stone`, `Manufactured
    Stone`, `Stone Veneer by others`; hatch камня на elevation; на разрезе —
    WRB + lath + scratch coat + stone.

    **Кто:** mason / veneer sub. **By others.**

=== "Brick veneer"

    **Brick veneer** = кирпичная облицовочная стенка с воздушным зазором,
    brick ties к каркасу, weep holes, lintels/shelf angles.

    **Распознать:** notes `Brick Veneer`, `Brick`, brick hatch; на разрезе —
    air gap + ties + weeps; shelf angle / lintel над openings.

    **Кто:** mason. **By others.**

## Почему by others и что всё-таки считаем { .kb-section-title .kb-st--green }

EIFS / stucco / stone / brick устанавливают **другие trade**. Мы не считаем
сам finish, но рядом **остаётся наш scope**:

| Элемент рядом с EIFS/stucco/veneer | Считаем? |
| --- | --- |
| WRB / housewrap (если наш) | :material-check-bold: проверить |
| Sheathing (CDX / Zip / OSB) | :material-check-bold: свой scope |
| Furring / framing под облицовку | :material-check-bold: проверить |
| Wood / PVC trim, corner, band, soffit, fascia | :material-check-bold: ДА |
| Sam EIFS / stucco / stone / brick finish | :material-close-thick: НЕТ |
| Lath, base coat, brick ties, shelf angle | :material-close-thick: НЕТ (by others) |

- `Note: Stone Veneer by others` / `Note: Stucco by others` / `Note: EIFS by
  others` — ставь видимую note (см. [Standard notes](../../reference/standard-notes.md)).
- Если **весь** фасад EIFS/stucco/stone — siding `0 SQ FT` + note; trim может
  быть почти нулевым. Не «добивай» количество.

## J-Channel / casing bead / stop { .kb-section-title .kb-st--cyan }

EIFS и stucco — сплошные системы, их нужно **terminating** на чистую кромку.
Поэтому по периметру ставят accessory-профили:

| Условие | Профиль |
| --- | --- |
| Вокруг **окон / дверей** | `J-Channel` / `casing bead` / back-wrap |
| По **низу** EIFS/stucco | track / `weep screed` / stop bead |
| Примыкание к **dissimilar material** (siding, soffit, stone) | `J-Channel` / expansion joint |
| Поля EIFS | `expansion joint` / `reveal` (декоративный паз) |
| **Vinyl siding** рядом | `J-Channel` у corner/openings/soffit/rake |

!!! tip "J-Channel в строке takeoff"
    - С **EIFS/stucco** accessory обычно идёт с finish-системой → **by
      others**. Считаем только если явно в нашем scope.
    - С **vinyl siding** `J-Channel` — наш accessory: `LFT` по периметру
      openings + terminations; `Ext. Casing` может **и есть** `Vinyl
      J-channel` — не дублируй с wood casing.

    Полная карта где бывает J-Channel —
    [Exterior Trims → Exclusions и J-Channel](../exterior-trims/exclusions.md).

## Чек перед выводом { .kb-section-title .kb-st--magenta }

- [ ] Прочитал notes: EIFS / Synthetic Stucco / Dryvit / Sto / Stucco / Stone / Brick?
- [ ] EIFS / Stucco / Stone / Brick veneer исключены (by others) + note?
- [ ] WRB / sheathing / furring рядом — проверены по нашему scope?
- [ ] Wood / PVC trim вокруг облицовки всё равно посчитан?
- [ ] J-Channel: by others (с EIFS) vs наш (с vinyl) — не перепутал?
- [ ] Весь фасад EIFS/stone → siding `0` + note, без «добивки»?

## See also

- [Overview](overview.md) · [Underlayment](underlayment.md) · [Измерение](measure.md)
- [Exterior Trims → Exclusions и J-Channel](../exterior-trims/exclusions.md)
- [Casing, Corner & Band](../exterior-trims/casing-corner-band.md)
- [Standard notes](../../reference/standard-notes.md)
