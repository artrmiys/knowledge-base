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

## Flashing Table

Source: `https://redacted.atlassian.net/wiki/spaces/work/pages/65044582/Openings`

| Opening item | Output |
| --- | --- |
| Window Flashing | Sill Flashing |

## PlanSwift Marking & Macro

- Подсчёт всех openings — макрос **`F_Openings`** (даёт Window Flashing + Sill Flashing).
- У всех **дверей** обязательно ставь пометку **`d`**.
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

<div class="kb-rule-gallery">
  <a class="kb-rule-card" href="../../../../assets/images/confluence/confluence-092.png" title="image-20251030-161759.png">
    <img src="../../../../assets/images/confluence/confluence-092.png" alt="Window/Door Opening - визуальная проверка: Проверь schedule, rough opening, header need и exterior-only scope.">
    <div class="kb-rule-card__body">
      <div class="kb-rule-card__title">Window/Door Opening - визуальная проверка</div>
      <div class="kb-rule-card__rule">Проверь schedule, rough opening, header need и exterior-only scope.</div>
      <div class="kb-rule-card__note">Openings не считай по символам вслепую, если schedule даёт размер/material/fire notes.</div>
    </div>
  </a>
</div>
<!-- confluence-gallery:end -->
