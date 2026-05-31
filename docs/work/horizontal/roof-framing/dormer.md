# Dormer

**Dormer** — надстройка с собственной крышей, выходящая из ската (со своим окном).
Объединяет правила wall + roof + opening + trim — поэтому не прячь в один item.

## Что считать

- Dormer walls, roof framing, sheathing, trims и openings как separate scope,
  когда shown.

## Проверить

- Dormers часто объединяют wall, roof, opening и trim rules.
- Проверь exterior sheathing/WRB и FRT rules.
- Не прячь dormer materials внутри generic roof lines, если pricing требует их
  separate.

## See also

- [Roof Header](header.md) · [Overframes](overframes.md) · [Exterior Walls](../../vertical/walls/exterior.md)


<!-- confluence-gallery:start -->
## Визуальная проверка

Эти картинки уже привязаны к правилам страницы. Используй их как быстрые
checkpoint-ы перед output: сначала прочитай правило выше, потом открой нужную
карточку и проверь похожий condition на плане/schedule.

??? info "Источник картинок"
    - Dormer, Shed Dormer (надстроенная крыша): [1 карт. Confluence](https://redacted.atlassian.net/wiki/spaces/work/pages/66125835/Dormer+Shed+Dormer)

<details class="kb-figures kb-figures--rows" open>
  <summary>Скрыть 1 правил с иллюстрациями</summary>
  <figure class="kb-figure-row">
    <figcaption class="kb-figure-row__text">
      <div class="kb-figure-row__title">Dormer - визуальная проверка</div>
      <div class="kb-figure-row__rule">Проверь dormer walls, roof framing, headers и sheathing scope.</div>
      <div class="kb-figure-row__note">Dormer обычно затрагивает и walls, и roof, поэтому не прячь всё в один item.</div>
    </figcaption>
    <a class="kb-figure-row__image" href="../../../../assets/images/confluence/confluence-148.png" target="_blank" rel="noopener"><img src="../../../../assets/images/confluence/confluence-148.png" alt="Dormer - визуальная проверка: Проверь dormer walls, roof framing, headers и sheathing scope." loading="lazy"></a>
  </figure>
</details>
<!-- confluence-gallery:end -->
