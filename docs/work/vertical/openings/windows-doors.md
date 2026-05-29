# Windows and Doors

Source: `https://redacted.atlassian.net/wiki/spaces/work/pages/65339393/Windows+Doors`

## Что считать

- Window and door openings by type/size.
- Jamb blocking for all windows and interior doors.
- Fire-rated unit entry doors from corridors.

## Door Labels

- Используй material и fire rating, где это важно: `2670 FCW`, `3070 HM C-lbl`.
- Unit entries can be labeled `3070 Entry`.
- Hardware numbers usually are not needed in the takeoff list.

## Проверить

- Exterior jambs can use flashing-style formulas.
- Interior door jambs can use casing divided by 2 where that is the local method.
- Room schedule tile base исключай, если нужен только wood base.

## Flashing из Openings

Source: `https://redacted.atlassian.net/wiki/spaces/work/pages/65044582/Openings`

Когда openings заполнены — flashing **считается автоматом** через макрос
`F_Openings`. Руками длины не набиваем; задача — правильно проставить тип
(окно / дверь) и размеры, а LFT макрос соберёт сам.

| Opening | Что выдаёт макрос | Правило |
| --- | --- | --- |
| Window | `Window Flashing` (3 стороны: head + 2 jambs) + `Sill Flashing` (низ) | Окну считается **и то, и то** |
| Door (`d`) | `Window Flashing` (3 стороны) | У двери **нет** `Sill Flashing` — снизу threshold |
| Garage door (`gd`) | `Window Flashing` (3 стороны) | Аналогично двери, sill нет |

- **Sides + head** считаются как `Window Flashing` LFT = `(2*H + W) * qty`.
- **Bottom** считается как `Sill Flashing` LFT = `W * qty` — **только для окон**.
- Полная логика «что такое flashing, что такое sill, и как разделять по типу
  стены (wood / Mtl / CMU/concrete)» — на странице
  [Flashing](../../sheathing-and-misc/flashing.md).
- На CMU / concrete стенах часто нужен ещё `Window Jamb 1x4` или `2x4 P.T.` —
  отдельной строкой, см. там же.

## PlanSwift Marking & Macro

- Подсчёт всех openings — макрос **`F_Openings`** (даёт Window Flashing + Sill Flashing).
- У всех **дверей** обязательно ставь пометку **`d`** — макрос по этой пометке
  **не считает** sill flashing.
- У **гаражных** дверей — пометка **`gd`**.
- Если **окно и дверь объединены одним хэдером** (например, sliding patio в blocks с фиксом сбоку) — считай их **вместе** одним openings, ставь **`d`**.
- Все openings **вырезаются из sheathing** — не забывай subtract при подсчёте Wall Sheathing SQFT.

<!-- confluence-gallery:start -->
## Визуальная проверка

Эти картинки уже привязаны к правилам страницы. Используй их как быстрые
checkpoint-ы перед output: сначала прочитай правило выше, потом открой нужную
карточку и проверь похожий condition на плане/schedule.

??? info "Источник картинок"
    - Openings: [1 карт. Confluence](https://redacted.atlassian.net/wiki/spaces/work/pages/65044582/Openings)

<details class="kb-figures">
  <summary>Показать 1 иллюстраций</summary>
  <div class="kb-figure-grid">
    <a class="kb-figure" href="../../../../assets/images/confluence/confluence-092.png" target="_blank" rel="noopener"><img src="../../../../assets/images/confluence/confluence-092.png" alt="Window/Door Opening - визуальная проверка: Проверь schedule, rough opening, header need и exterior-only scope." loading="lazy"></a>
  </div>
</details>
<!-- confluence-gallery:end -->
