# Porch SQFT (площадь крытого крыльца)

<figure markdown>
  ![Разрез porch: post, beam, soffit, decking](../../assets/images/sqfts/porch.svg)
  <figcaption markdown="span">Porch: пол на своём каркасе и потолок (soffit) под крышей. Площадь пола - Area `porch`; крыша над porch - своя Area в roof.</figcaption>
</figure>

## Что это

Porch - крытая площадка у входа на своём каркасе. Его площадь даёт пол
(decking или subfloor) и потолок (наружный гипс; два слоя - это одна строка
`Soffit Gypsum (2)` с x 2 в формуле). Крыша над porch - отдельная площадь по
[Roof SQFT](roof.md), карниз porch - отдельная позиция `eve 12 porch`.
Porch считается независимо от балконов, даже если похож. Общие правила
замера - [Floor SQFT, раздел правил](1st2nd.md#rules).

## Где искать на чертежах

| Лист | Что взять |
| --- | --- |
| Floor plan (`a101 1st`) | Контур porch, posts |
| Framing plan, details (S) | Ceiling joists, ledger, hangers, балки, posts; каркас не показан - Note |
| RCP (`rcp`) | Материал потолка: `5/8" Ext Gyp`, DensGlass, beadboard |
| Elevations, sections | Крыша porch, уклон, колонны |

## Как мерить в OurPlanCore

1. Area по контуру пола porch на плане (точка W). Имя `porch`. Несколько
   одинаковых porch - полигоны в одной позиции; разные типы - разные.
2. Типовые porch в многоквартирном доме размечаются блоками: одна позиция
   Count на тип, точка на каждый экземпляр (см.
   [Deck / Porch / Balcony Frame](../deck/deck-porch-balcony-frame.md)).
3. Крышу porch обводи в `sqfts` отдельно (`rf 4` porch или `rf mtl 4`).

## Как назвать в дереве и строка DFL

| Имя в дереве | Строка DFL (блок Porch) | Материал | Unit | Формула |
| --- | --- | --- | --- | --- |
| `sqfts/porch` | Front Page, `Porches` | | `SQ FT` | как измерено |
| `sqfts/porch` | `Decking` или `Subfloor` | по детали | `SQ FT` / `4x8` | `=ОКРВВЕРХ(W*D*units*1.1;10)` или `=ОКРВВЕРХ(SQFT/32*1.1;1)` |
| `sqfts/porch` | `Soffit Gypsum (2)` | `5/8" Ext Gyp` или тип плиты по assembly | `SQ FT` | `=ОКРВВЕРХ(W*D*2*1.1;2)*units`; один слой: `Soffit Gypsum` без x 2 |
| та же площадь | `Ceiling Joists 16" o.c.` + `Ledger` + `Hangers` | по детали, `2x4 P.T.`; не показано: `2x6 P.T.`, `assumed` | длина доски; hangers `pcs` | число joists = `ОКРВВЕРХ(W*12/16;1)+1` на porch x units; отдельно от rafters |
| posts | `Posts` | всегда `P.T.`, и под крышей porch | длина поста в футах | число постов одного porch x units |

Каркас не показан: `Note: Porch framing is not specified; all framing
assumed; verify` сразу под заголовком блока.

## Частые ошибки

- Porch SQFT на Front Page пустой (итог дома не сошёлся).
- Porch зеркален с балконов вместо отдельного счёта.
- Потолок porch посчитан как обычный interior gypsum, а не exterior.
- Два слоя гипса записаны двумя строками, или x 2 стоит и в подписи, и ещё раз в площади.
- Крыша porch попала в main `rf 6` с чужим уклоном.
- Карниз porch посчитан ещё раз внутри `eve 24 main`.

Все ошибки по площадям: [common-mistakes](../../start/common-mistakes.md#sqft).

## Пример

```text
Takeoffs/Main/sqfts/
  porch       Area   96 SF   (12' x 8')
  rf 4        Area  118 SF   (крыша porch)
Covered Front Porch Framing List
Note: Porch framing is not specified; all framing assumed; verify.
Ceiling Joists 16" o.c.   2x6 P.T.        10   8       assumed   12 x 12/16 = 9, плюс 1; глубина 8'
Soffit Gypsum (2)         5/8" Ext Gyp   212   SQ FT             96 x 2 x 1.1 = 211.2, вверх до 2
```

## См. также

- [Deck / Porch / Balcony Frame](../deck/deck-porch-balcony-frame.md), [Porch / Deck / Balcony trims](../exterior-trims/porch-deck-balcony.md)
- [Eve / Eave](../sheathing-and-misc/eve.md), [Soffit and Fascia](../exterior-trims/soffit-fascia.md), [Roof SQFT](roof.md)
