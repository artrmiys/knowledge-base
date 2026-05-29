# Windows and Doors

Source: `https://redacted.atlassian.net/wiki/spaces/work/pages/65339393/Windows+Doors`

## Что считать

- **Окна и двери** — по типам и размерам из window / door schedule.
- **Блокировку проёмов** (`jamb blocking`) — у всех окон и у межкомнатных
  дверей.
- **Пожароустойчивые двери** в квартиры из коридоров (`fire-rated unit
  entry`) — отдельным типом, с указанием рейтинга.

## Подписи дверей

- В подписи указываем **материал** и **fire rating**, если это важно. Примеры:
    - `2670 FCW` — двустворчатая 2'6"×7'0".
    - `3070 HM C-lbl` — металлическая 3'0"×7'0", класс «C».
- Дверь в квартиру можно подписать просто `3070 Entry`.
- **Номера фурнитуры** (hardware numbers) в takeoff обычно **не нужны**.

## Проверить

- У наружных проёмов **jamb** (доска по периметру проёма) можно считать той же
  формулой, что и flashing — по 3 сторонам. Подробнее на странице
  [Window Flashing](window-flashing.md).
- У межкомнатных дверей **jamb** часто считается как `casing / 2`, если так
  заведено в проекте.
- Из Room Schedule убирай `tile base`, если в скоупе только wood base.

## Гидроизоляция вокруг проёмов

Flashing вокруг окон и дверей — отдельная страница:
**[Window Flashing & Sill](window-flashing.md)**. Там: правило «3 стороны
у окон + sill, у дверей только 3 стороны», разделение по типу стены (wood /
Mtl / CMU / concrete), и wood jamb `1x4` / `2x4 P.T.` на бетоне.

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
