# Dbl Trpl Rafters

## Count

- Double/triple rafters and built-up roof members.

## Critical Rules

- **Dbl/Trpl Rafters** работают **параллельно Rafters**, как внутренняя усиленная балка крыши.
- Сечения и материалы — любые: `1 3/4 x 11 7/8 LVL`, `2x12`, `(2) 2x10` и т.д.
- Опирание — на **Ridge**, **перекрытие** или **стену**.
- **Длина** как у обычных Rafters — **всегда сверять по разрезам и фасадам**, не брать с плана.
- Указывать кол-во и длину **в футах с округлением до 2'**.
- Hangers нужны только если Dbl/Trpl Rafters **опираются на несущий [Ridge](ridge.md)**, либо это явно указано на плане. См. [Hangers](../../../reference/hangers.md).

## Check

- Product can be dimensional lumber, LVL, PSL, or GL.
- Built-up member length and ply count must both be visible in output.
- Use hangers/connectors matching the actual built-up width.

## Output Tables

| Name | Size | Count | Length / pcs |
| --- | --- | --- | --- |
| Dbl Rafters | `2x12` | `2` | `18` |
| Trpl Rafters | `1 3/4 x 11 7/8 LVL` | `3` | `28` |

| Connector | Size | Count | Unit |
| --- | --- | --- | --- |
| Hangers | `LSSR2.56Z` | `2` | pcs |
| Hangers | `LRU212Z` | `1` | pcs |


<!-- confluence-gallery:start -->
## Confluence Images

Изображения из Confluence размещены на этой странице по исходной теме.
Подпись сохраняет группу-источник, чтобы можно было быстро проверить контекст.

| Source group | Images | Confluence |
| --- | ---: | --- |
| Dbl Trpl Rafters (двойные тройные стропила) | 2 | [source](https://ewood.atlassian.net/wiki/spaces/work/pages/66093077/Dbl+Trpl+Rafters) |

<div class="kb-gallery">
  <a class="kb-gallery__item" href="../../../../assets/images/confluence/confluence-140.png" title="image-20250608-052309.png">
    <img src="../../../../assets/images/confluence/confluence-140.png" alt="Dbl Trpl Rafters (двойные тройные стропила) - double/triple rafter reference 01">
    <div class="kb-gallery__caption">double/triple rafter reference 01 (image, 365 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../../../assets/images/confluence/confluence-141.png" title="image-20250608-052021.png">
    <img src="../../../../assets/images/confluence/confluence-141.png" alt="Dbl Trpl Rafters (двойные тройные стропила) - double/triple rafter reference 02">
    <div class="kb-gallery__caption">double/triple rafter reference 02 (image, 138 KB raw)</div>
  </a>
</div>
<!-- confluence-gallery:end -->
