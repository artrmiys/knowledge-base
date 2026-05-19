# Exclusions и J-Channel

!!! info "Полное описание EIFS / Stucco / Veneer — в разделе Siding"
    Здесь — правило исключения для **trim-scope**. Что такое EIFS / Stucco /
    Stone / Brick veneer, как распознать на чертеже и где идёт casing bead —
    в [Siding → EIFS / Stucco / Veneer](../siding/eifs-stucco-veneer.md).

## Что НЕ считаем в Exterior Trims { .kb-section-title .kb-st--amber }

!!! danger "By others — не входит в наш scope"
    | Система | Считаем? | Почему |
    | --- | --- | --- |
    | **EIFS** (synthetic stucco) | :material-close-thick: НЕТ | Finish system by others (EIFS sub). |
    | **Stucco** (cement / 3-coat) | :material-close-thick: НЕТ | Plaster trade, by others. |
    | **Stone Veneer** | :material-close-thick: НЕТ | Masonry / veneer sub, by others. |
    | **Brick Veneer** | :material-close-thick: НЕТ | Masonry, by others. |
    | **Siding** (Hardi / vinyl / cedar) | :material-close-thick: НЕТ* | Siding scope отдельно, не trim. |

    \* Siding считается в своём scope, не в Exterior Trims. Но trim **вокруг**
    siding (casing, corner, band) — наш.

- Видишь на elevation `Note: Stone Veneer by others` — пропускаем veneer,
  считаем только wood/PVC trim вокруг него.
- `EIFS`, `Synthetic Stucco`, `Dryvit`, `Sto` — это всё EIFS-семейство, не наше.
- Если весь фасад EIFS / stucco / stone — exterior **trim** может быть почти
  нулевым (только то, что явно wood/PVC). Не «добивай» количество.
- Не путай: **soffit / fascia / frieze / corner / band** — это наш trim, даже
  если стена под ними EIFS или stone.

!!! note "Что всё-таки считаем рядом с EIFS / stucco / stone"
    - Wood / PVC / composite casing, corner board, band, watertable.
    - Soffit, fascia, frieze, rake moulding.
    - Columns, porch / deck / balcony trim.
    - **J-Channel** — если он наш по scope (см. ниже).

## J-Channel { .kb-section-title .kb-st--cyan }

`J-Channel` — это профиль в форме буквы **J**, в который заводится обрезанный
край siding или EIFS / stucco stop. Он закрывает торец материала и даёт чистую
линию примыкания.

### С EIFS почти всегда есть J-Channel

EIFS — это сплошная штукатурная система, и её нужно **terminating** (останавливать)
на чистую кромку. По периметру EIFS-поля ставят:

- `J-Channel` / casing bead / stop bead вокруг **окон и дверей**;
- track / stop по **низу** EIFS (где он переходит в foundation / другой материал);
- stop там, где EIFS примыкает к **soffit, fascia, corner, dissimilar material**.

Поэтому если на elevation указан EIFS — ищи note про `J-Channel` / `casing
bead` / `stop`. Считаем его, только если он явно в нашем scope (не EIFS-sub).

### Где J-Channel бывает ещё (не только EIFS)

| Условие | Где именно идёт J-Channel |
| --- | --- |
| **Vinyl siding** | Вокруг окон/дверей, под soffit/frieze, у corner posts, на inside corners, у gable/rake. При vinyl siding ext. casing **сам бывает** `Vinyl J-channel`. |
| **Siding ↔ другой материал** | Где siding примыкает к stone/brick/EIFS, к decking, к porch ceiling. |
| **Gable / rake** | По наклонной кромке, где siding обрезается под крышу. |
| **Окна / двери** | Head, jambs, sometimes sill — заводит cut edge siding. |
| **Soffit / frieze** | Где верх siding встречается с soffit или frieze board. |

!!! tip "J-Channel в строке takeoff"
    Видишь в exterior trims `Ext. Casing | Vinyl J-channel | 0 | LFT` — это
    значит, что для vinyl siding роль casing играет именно J-channel. Тогда:

    - не дублируй ещё и `5/4x4` casing, если siding vinyl и note про J-channel;
    - количество — LFT по периметру всех openings (4 sides) + terminations;
    - оставляй слово `J-channel` в Label, не своди к generic `casing`.

## Чек перед выводом { .kb-section-title .kb-st--magenta }

- [ ] Прочитал note про siding-материал (Hardi / vinyl / cedar / EIFS / stucco)?
- [ ] EIFS / Stucco / Stone / Brick veneer исключены (by others)?
- [ ] При vinyl siding проверил, не `J-channel` ли это casing?
- [ ] J-Channel посчитан там, где siding обрезается (openings, rake, terminations)?
- [ ] Wood / PVC trim вокруг veneer всё равно посчитан?

## See also

- [Overview](overview.md)
- [Casing, Corner & Band](casing-corner-band.md)
- [Soffit & Fascia](soffit-fascia.md)
- [Furring & Window Jambs](furring-and-jambs.md)
