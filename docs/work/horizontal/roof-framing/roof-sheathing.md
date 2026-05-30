# Roof Sheathing

## Что считать

- Roof OSB/Plywood.
- Flat roof cover board, Densedeck/glass mat, rigid insulation, and XPS layers.
- Soffit plywood under roof trusses where shown.

## Проверить

- Flat roof trusses often need Densedeck over the same area as rigid insulation.
- Extra rigid XPS layer is a recurring miss.
- Piggy truss sleepers can be hidden in roof details.
- 1x3 strapping under roof trusses может требоваться.
- For roofs framed with `AJS Rafters`, count rafters manually instead of `Rake`
  когда condition ведёт себя как exposed floor overhang.
- Some details call for every other rafter to be doubled; do not average this
  into a generic rafter run.

## Companion-каркас (corpus) { .kb-section-title .kb-st--cyan }

Секция roof sheathing почти всегда тянет за собой **overhang/eave-каркас** —
по корпусу (flat 68 файлов / pitched 32):

| Строка | % | Типично |
| --- | ---: | --- |
| Sub Fascia | 91% | `2x6` / `2x8` |
| Blocking at Eves | 81% | `2x6` |
| Truss Bracing | 78% | `2x4` (длина `16'`) |
| Clips (H-clip) | 62% | сшивка листов |
| Simpson Ties at Eves | 62% | `H2.5` |
| Frame for Soffits / Rakes | 56% / 25% | `2x4` |
| Insulation (flat) | 87% | tapered / rigid |

**Flat-roof overhang с опорами** (canopy-style): Posts `8x8 Timber` / `6x6 Western
Cedar` / `4x4 P.T.`; Beams `5¼x7¼ LVL`; Post Caps `CBH…` (timber connectors);
Ledger `2x8 FRT` / `2x10`. Детали overhang-обшивки — [Eve / Eave](../../sheathing-and-misc/eve.md).


<!-- confluence-gallery:start -->
## Визуальная проверка

Эти картинки уже привязаны к правилам страницы. Используй их как быстрые
checkpoint-ы перед output: сначала прочитай правило выше, потом открой нужную
карточку и проверь похожий condition на плане/schedule.

??? info "Источник картинок"
    - Roof Sheathing (обшивка): [2 карт. Confluence](https://redacted.atlassian.net/wiki/spaces/work/pages/66125845/Roof+Sheathing)

<details class="kb-figures kb-figures--rows" open>
  <summary>Скрыть 2 правил с иллюстрациями</summary>
  <figure class="kb-figure-row">
    <figcaption class="kb-figure-row__text">
      <div class="kb-figure-row__title">Roof Sheathing - визуальная проверка 01</div>
      <div class="kb-figure-row__rule">Сверь roof planes, openings, overhangs и sheathing material/thickness.</div>
      <div class="kb-figure-row__note">Не считай roof sheathing как простую footprint area, если planes/details дают другое.</div>
    </figcaption>
    <a class="kb-figure-row__image" href="../../../../assets/images/confluence/confluence-149.png" target="_blank" rel="noopener"><img src="../../../../assets/images/confluence/confluence-149.png" alt="Roof Sheathing - визуальная проверка 01: Сверь roof planes, openings, overhangs и sheathing material/thickness." loading="lazy"></a>
  </figure>
  <figure class="kb-figure-row">
    <figcaption class="kb-figure-row__text">
      <div class="kb-figure-row__title">Roof Sheathing - визуальная проверка 02</div>
      <div class="kb-figure-row__rule">Сверь roof planes, openings, overhangs и sheathing material/thickness.</div>
      <div class="kb-figure-row__note">Не считай roof sheathing как простую footprint area, если planes/details дают другое.</div>
    </figcaption>
    <a class="kb-figure-row__image" href="../../../../assets/images/confluence/confluence-150.png" target="_blank" rel="noopener"><img src="../../../../assets/images/confluence/confluence-150.png" alt="Roof Sheathing - визуальная проверка 02: Сверь roof planes, openings, overhangs и sheathing material/thickness." loading="lazy"></a>
  </figure>
</details>
<!-- confluence-gallery:end -->
