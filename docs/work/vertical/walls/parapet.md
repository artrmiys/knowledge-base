# Parapet Walls

## Что считать

- Parapet framing, cap plates, inside/outside sheathing, insulation adjustments
  и EPDM, где required.
- FRT blocking/plates, когда exterior wall FRT rules применяются.

## Правила

- Parapets = FRT, когда exterior walls = FRT.
- Parapet sheathing может быть both sides; outside может subtract insulation board.
- Top chord bearing truss conditions могут требовать blocking between trusses,
  а не ribbon board.

## Частые пропуски

- Detail callouts вроде `(2) 2x8 FRT blocking at parapets`.
- Cap plate treatment, часто 2x6 PT.

## Типовой состав (corpus-validated) { .kb-section-title .kb-st--green }

Парапет как framed-стена — полноценный набор строк (по 65 файлам корпуса, `%` = в
скольки парапет-секциях встречается):

| Строка | % | Типично |
| --- | ---: | --- |
| Flashing | 100% | `Drip Edge` по верху |
| Inside Sheathing | 94% | OSB / `5/8" Gypsum` (внутренняя сторона) |
| Wall Sheathing | 89% | OSB / Zip (наружная сторона) |
| **Top Sheathing** | 82% | по верхней грани парапета (часто забывают) |
| Studs | 66% | размер по высоте (nested-IF) |
| Vapor Barrier | 66% | Tyvek / `=O4` |
| Plates btm + top | 58% | P.T. снизу |
| Subfloor / Hangers | 40% / — | `LUS210` / `A35` / `LSSR1.81Z` где есть |

→ Ключевое: парапет обшивается **с двух сторон** (inside + wall) **плюс top** + flashing —
это три плоскости обшивки, не одна.

## Parapet vs. Truss System

Главная развилка — входит ли парапет в truss-систему крыши:

- **Parapet integral with roof truss** — система парапетов уже включена в truss. **Обшивка (sheathing) при этом НЕ включена в truss** — её всё равно надо считать отдельно.
- **Parapet НЕ включён в truss** — смотри на ориентацию опирания truss/rafters относительно стены:
    - **Перпендикулярное опирание** — парапет выполняй отдельным каркасом (stud wall).
    - **Параллельное опирание** — стену последнего этажа **продли вверх** до высоты парапета (продолжение exterior wall).

<!-- confluence-gallery:start -->
## Визуальная проверка

Эти картинки уже привязаны к правилам страницы. Используй их как быстрые
checkpoint-ы перед output: сначала прочитай правило выше, потом открой нужную
карточку и проверь похожий condition на плане/schedule.

??? info "Источник картинок"
    - Parapet (парапет, стены крыши): [2 карт. Confluence](https://redacted.atlassian.net/wiki/spaces/work/pages/65306653/Parapet)

<details class="kb-figures">
  <summary>Показать 2 иллюстраций</summary>
  <div class="kb-figure-grid">
    <a class="kb-figure" href="../../../../assets/images/confluence/confluence-127.png" target="_blank" rel="noopener"><img src="../../../../assets/images/confluence/confluence-127.png" alt="Parapet Wall - визуальная проверка 01: Проверь parapet height, material, FRT rule и roof edge condition." loading="lazy"></a>
    <a class="kb-figure" href="../../../../assets/images/confluence/confluence-128.png" target="_blank" rel="noopener"><img src="../../../../assets/images/confluence/confluence-128.png" alt="Parapet Wall - визуальная проверка 02: Проверь parapet height, material, FRT rule и roof edge condition." loading="lazy"></a>
  </div>
</details>
<!-- confluence-gallery:end -->
