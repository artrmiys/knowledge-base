# Wall Sheathing

Source: `https://ewood.atlassian.net/wiki/spaces/work/pages/90144770/Wall+Sheathing`

<figure markdown>
  ![Wall sheathing source priority flow](../../../assets/images/sheathing/wall-sheathing-priority.svg)
  <figcaption>Wall sheathing priority: Arch/Energy can control exterior, Structural controls shear.</figcaption>
</figure>

## Count

- Exterior sheathing by Arch / energy / Zip notes.
- Interior shear wall sheathing by Structural.
- Loose/box/full-height sheathing separately when project scope distinguishes it.
- Densglass, FRT, Zip, plywood/OSB, and gypsum-based sheathing as separate lines
  when the drawings call out different products.

## Rules

- `19/32"` is `5/8"`, not `1/2"`.
- Zip on exterior walls supersedes structural sheathing notes, but keep a note.
- Non-Zip exception: if Arch says 1/2" and Structural says 5/8", use 5/8" for
  strength.
- Optional walls may need full-height sheathing; loose sheathing may be box only.
- Interior shear wall sheathing follows the shear wall schedule, including
  one-side vs both-sides requirements.
- Do not hide sheathing inside generic wall SQFT when the reviewer needs product,
  thickness, side, or location.

## Source Priority

| Situation | Default takeoff decision |
| --- | --- |
| Exterior wall has Zip note | Use Zip; keep Structural conflict as note |
| Exterior wall has no Zip, Arch 1/2" vs Structural 5/8" | Use 5/8" |
| Shear wall schedule says both sides | Count both sides, not wall area once |
| Wall type/elevation calls Densglass | Separate Densglass by level/elevation |
| FRT exterior wall material | Check if sheathing/blocking/parapet also changes |

## Check

- FRT sheathing notes at exterior walls.
- Densglass at metal walls or specific elevations.
- Shear wall schedule one-side vs both-sides requirements.
- Full-height vs box-only sheathing at optional walls.
- Floor-height sheathing around panelized COM jobs where loose material is still
  in scope.
- Draft stop sheathing at party/demising walls is not the same as shear wall
  sheathing. Keep draft stop and shear wall quantities separate.
- Draft stop can appear at walls and between floors; count each supplied scope
  in the matching section rather than combining it into one wall line.

## Sheathing Material Variants

Стандартные продукты, которые встречаются на чертежах:

| Запись на чертеже | Что брать |
| --- | --- |
| `1/2" CDX Ply` | Plywood CDX, 1/2" |
| `1/2" OSB` | OSB, 1/2" |
| `1/2" Ply` (или просто **APA RATED**) | Plywood APA-rated, 1/2" |
| `7/16" Zip` | Huber Zip System, 7/16" |
| `Zip Tape` | Лента Zip — отдельной строкой к Zip-обшивке |

- Если на плане только `APA RATED` без указания материала — это **Plywood**, не OSB.
- `Zip Tape` идёт **только** в паре с Zip-обшивкой; не забывай добавить отдельную строку.

<!-- confluence-gallery:start -->
## Confluence Images

Изображения из Confluence размещены на этой странице по исходной теме.
Подпись сохраняет группу-источник, чтобы можно было быстро проверить контекст.

| Source group | Images | Confluence |
| --- | ---: | --- |
| Sheathing | 2 | [source](https://ewood.atlassian.net/wiki/spaces/work/pages/65044604/Sheathing) |

<div class="kb-gallery">
  <a class="kb-gallery__item" href="../../../../assets/images/confluence/confluence-093.jpg" title="image-20251030-155040.png">
    <img src="../../../../assets/images/confluence/confluence-093.jpg" alt="Sheathing - wall sheathing reference 01">
    <div class="kb-gallery__caption">wall sheathing reference 01 (preview, 1299 KB raw)</div>
  </a>
  <a class="kb-gallery__item" href="../../../../assets/images/confluence/confluence-094.jpg" title="image-20251030-155003.png">
    <img src="../../../../assets/images/confluence/confluence-094.jpg" alt="Sheathing - wall sheathing reference 02">
    <div class="kb-gallery__caption">wall sheathing reference 02 (preview, 5480 KB raw)</div>
  </a>
</div>
<!-- confluence-gallery:end -->
