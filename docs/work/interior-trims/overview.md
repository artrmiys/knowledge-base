# Interior Trims

Interior Trims — это отдельный scope, не exterior trims, не drywall и не
framing. Используй этот раздел, когда в scope есть finish trim items из room
schedules, door/window schedules или finish plans.

## Что считать

- Base / wood base.
- Door casing и jamb trim.
- Window casing, stool, apron и related trim, если они показаны.
- Crown, когда trim scope активен.
- Common-area trims отдельно от unit trims.

## Не смешивать

- Exterior casing, mullion, sill, head, corner board, watertable, siding trim.
- Gypsum board для стен.
- Framing blocking, если trim не требует backing и scope не просит это считать.

## Основные правила

- Если trims не указаны, пиши `not specified`.
- Garage: нет `Baseboard` и нет `Crowns`.
- В room schedules может быть tile base; исключай tile base, когда takeoff нужен
  только для wood base.
- Common areas вроде corridors и lobbies держи отдельно: trim type может
  отличаться.
- `Crowns` включаются, когда interior trim scope активен.
- Сначала сделай interior-trim PDFs/sheets, потом меряй `Baseboard` и `Crowns`
  continuous room perimeter.
- Casing для interior doors заполняется после interior-door list; casing для
  exterior doors/windows — после exterior openings.

## Визуальный workflow

На Trello board `int trims` есть 43 исходные картинки. Карточки ниже связывают
картинку с правилом; полный набор смотри на отдельных topic pages.

<details class="kb-figures kb-figures--rows" open>
  <summary>Скрыть 6 правил с иллюстрациями</summary>
  <figure class="kb-figure-row">
    <figcaption class="kb-figure-row__text">
      <div class="kb-figure-row__title">1. Подготовить trim PDFs</div>
      <div class="kb-figure-row__rule">Сначала сделай листы, которые можно проверить.</div>
      <div class="kb-figure-row__note">Не начинай formulas по памяти; сначала отдели interior-trim scope.</div>
    </figcaption>
    <a class="kb-figure-row__image" href="../../../assets/images/trims/int-trims-01.png" target="_blank" rel="noopener"><img src="../../../assets/images/trims/int-trims-01.png" alt="Create interior trim PDF files" loading="lazy"></a>
  </figure>
  <figure class="kb-figure-row">
    <figcaption class="kb-figure-row__text">
      <div class="kb-figure-row__title">2. Мерить perimeter items</div>
      <div class="kb-figure-row__rule">Baseboard и Crowns — это LF / perimeter work.</div>
      <div class="kb-figure-row__note">Веди trace непрерывно; breaks должны быть намеренными и видимыми.</div>
    </figcaption>
    <a class="kb-figure-row__image" href="../../../assets/images/trims/int-trims-02.png" target="_blank" rel="noopener"><img src="../../../assets/images/trims/int-trims-02.png" alt="Baseboard and crown perimeter example" loading="lazy"></a>
  </figure>
  <figure class="kb-figure-row">
    <figcaption class="kb-figure-row__text">
      <div class="kb-figure-row__title">Baseboard</div>
      <div class="kb-figure-row__rule">За kitchen cabinets Baseboard не считается.</div>
      <div class="kb-figure-row__note">Открой страницу Base для картинок 07-16 и Excel-output checks.</div>
    </figcaption>
    <a class="kb-figure-row__image" href="../../../assets/images/trims/int-trims-07.png" target="_blank" rel="noopener"><img src="../../../assets/images/trims/int-trims-07.png" alt="Baseboard is not counted behind kitchen cabinets" loading="lazy"></a>
  </figure>
  <figure class="kb-figure-row">
    <figcaption class="kb-figure-row__text">
      <div class="kb-figure-row__title">Crown</div>
      <div class="kb-figure-row__rule">В closets нет Crowns; в garage тоже нет Crowns.</div>
      <div class="kb-figure-row__note">Открой страницу Crown для картинок 17-25 и всех exclusions.</div>
    </figcaption>
    <a class="kb-figure-row__image" href="../../../assets/images/trims/int-trims-17.png" target="_blank" rel="noopener"><img src="../../../assets/images/trims/int-trims-17.png" alt="Crown is not counted in closets" loading="lazy"></a>
  </figure>
  <figure class="kb-figure-row">
    <figcaption class="kb-figure-row__text">
      <div class="kb-figure-row__title">Door / Window Trim</div>
      <div class="kb-figure-row__rule">Interior doors считай по open door symbol.</div>
      <div class="kb-figure-row__note">Открой Door page для картинок 26-43: sizes, C.O., Pocket, Slider и F.R. S.C.</div>
    </figcaption>
    <a class="kb-figure-row__image" href="../../../assets/images/trims/int-trims-26.png" target="_blank" rel="noopener"><img src="../../../assets/images/trims/int-trims-26.png" alt="Interior doors are measured by open door swing" loading="lazy"></a>
  </figure>
  <figure class="kb-figure-row">
    <figcaption class="kb-figure-row__text">
      <div class="kb-figure-row__title">Сначала door schedule</div>
      <div class="kb-figure-row__rule">Если есть door schedule, заполняй из schedule.</div>
      <div class="kb-figure-row__note">Plan view вторичен, когда schedule даёт size/material/fire notes.</div>
    </figcaption>
    <a class="kb-figure-row__image" href="../../../assets/images/trims/int-trims-43.png" target="_blank" rel="noopener"><img src="../../../assets/images/trims/int-trims-43.png" alt="Door schedule source for interior doors" loading="lazy"></a>
  </figure>
</details>

## Карта картинок

| Картинки | Тема | Куда открыть |
| --- | --- | --- |
| `01` - `06` | Workflow: PDFs, perimeter, casing automation | Эта страница |
| `07` - `16` | Baseboard rules и Excel checks | [Base](base.md) |
| `17` - `25` | Crown rules и Excel checks | [Crown](crown.md) |
| `26` - `43` | Interior doors, `F.R. S.C.`, C.O., Excel entry | [Door and Window Trim](door-window-trim.md) |

## Внешняя проверка

Internet references — только проверка terminology. Что именно считать, всё ещё
задают Estimating/Trello rules.

| Проверка | Что подтверждает | Источник |
| --- | --- | --- |
| Finish schedule | Columns Base / Ceiling / Remarks могут управлять trim scope; не полагайся только на room name. | [Helonic finish schedule guide](https://helonic.com/knowledge-base/finish-schedule-guide) |
| Linear measurement | Base/crown trim обычно проверяется wall-by-wall / room run, а не по room area. | [Metrie measuring guide](https://www.metrie.com/how-do-i-measure) |
| Estimating exceptions | Kitchen cabinets, closets, garage, slope ceilings, no-finish rooms и `TBD` notes остаются project-specific estimating rules. | [Trello Source Map](../../reference/trello-source-map.md) |

## Статус источников

Импортированный source board:
`https://trello.com/b/TyUKA0Zw/int-trims`.

