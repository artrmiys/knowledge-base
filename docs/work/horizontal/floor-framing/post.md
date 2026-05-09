# Post

## Что считать

- Wood posts, steel posts, bearing posts и built-up post groups, когда in scope.
- Post caps/bases только когда specifically called out.
- Posts в крыше — опора для [Ridge](../roof-framing/ridge.md) и [Header](../roof-framing/header.md).

## Критические правила

- Posts могут быть **цельные** (`5 1/4 x 5 1/4 PSL`, `6x6`, `4x4`) или **сборные** из нескольких досок (`(2) 2x6`, `(4) 2x4`).
- **Длина Posts очень важна** — может идти от фундамента сквозь несколько этажей. Проверяй elevation/section.
- Post в крыше опирается **либо на балку, либо на несущую стену**.
- Указывать кол-во и длину **в футах с округлением до 2'**.

## Проверить

- Material может отличаться по location: dimensional, LVL, PSL, GL, steel.
- Posts в panelized wall systems могут быть by others, если не показаны как
  loose structural material.
- Перед assumption, что post входит в wall panels, проверь load path details.
- Не создавай `Posts` / `Post Caps` для каждого built-up beam. Считай их только
  когда настоящий post material указан: `6x6`, `4x4`, PSL, steel или другой
  explicit post.
- Если post не specified, оставь видимую note вместо guessing post and cap.

## Connectors

Снизу — **Post Base** к фундаменту/балке. Сверху — **Post Cap** к балке. Примеры: `ABU66`, `PC46`, `CCQ66`.

## Таблицы вывода

| Name | Size | Qty | Length |
| --- | --- | --- | --- |
| Posts | `5 1/4 x 5 1/4 PSL` | `2` | `8` |
| Posts | `6x6` | `5` | `10` |
| Posts `(3)` | `2x4` | `3` | `12` |

| Connector | Size | Qty | Unit |
| --- | --- | --- | --- |
| Posts Base | `ABU66` | `5` | pcs |
| Posts Caps | `CCQ66` | `3` | pcs |


<!-- confluence-gallery:start -->
## Визуальная проверка

Эти картинки уже привязаны к правилам страницы. Используй их как быстрые
checkpoint-ы перед output: сначала прочитай правило выше, потом открой нужную
карточку и проверь похожий condition на плане/schedule.

??? info "Источник картинок"
    - Post (колоны): [1 карт. Confluence](https://redacted.atlassian.net/wiki/spaces/work/pages/65831004/Post)

<details class="kb-figures">
  <summary>Показать 1 иллюстраций</summary>
  <div class="kb-figure-grid">
    <a class="kb-figure" href="../../../../assets/images/confluence/confluence-134.png" target="_blank" rel="noopener"><img src="../../../../assets/images/confluence/confluence-134.png" alt="Post / Column - визуальная проверка: Проверь post size, height, material и connection to beam/foundation." loading="lazy"></a>
  </div>
</details>
<!-- confluence-gallery:end -->
