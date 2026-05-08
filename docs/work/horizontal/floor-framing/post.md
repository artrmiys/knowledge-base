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
## Картинки из Confluence

Изображения из Confluence размещены на этой странице по исходной теме.
Подпись сохраняет группу-источник, чтобы можно было быстро проверить контекст.

| Группа источника | Картинки | Confluence |
| --- | ---: | --- |
| Post (колоны) | 1 | [source](https://ewood.atlassian.net/wiki/spaces/work/pages/65831004/Post) |

<div class="kb-gallery">
  <a class="kb-gallery__item" href="../../../../assets/images/confluence/confluence-134.png" title="image-20250608-021518.png">
    <img src="../../../../assets/images/confluence/confluence-134.png" alt="Post (колоны) - post/column reference 01">
    <div class="kb-gallery__caption">post/column reference 01</div>
  </a>
</div>
<!-- confluence-gallery:end -->
