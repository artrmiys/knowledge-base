# Reconstruction / Реконструкция

Reconstruction jobs — это проекты, где часть здания уже существует, часть
демонтируется, а часть добавляется заново. Главная сложность: не считать весь
дом как new construction и не потерять места, где new framing должен
подключиться к existing.

!!! note "Черновик"
    Эта страница пока написана как рабочая шпаргалка без отдельного source.
    Когда появятся реальные project notes / feedback, перенеси сюда точные
    правила и обнови source map.

## Типовой scope

- New walls, openings, floor/roof framing и sheathing, которые показаны как new.
- Repair/rebuild areas: rotten framing, replaced subfloor, patched roof,
  rebuilt porch/deck, new beams/posts.
- New connection materials: hangers, straps, anchors, bolts, blocking, ledgers.
- Temporary or permanent bracing, если это показано в structural notes.
- Exterior envelope changes: WRB/Tyvek, sheathing patches, siding backing,
  insulation, flashing.

## Что не считать автоматически

- Existing framing, который остаётся без изменений.
- Demolition-only items, если takeoff scope не просит demo.
- Existing walls/openings, которые только показаны для context.
- Old joists/rafters/studs, если note says `existing to remain`.
- Finish materials, если scope только structural/framing.

## Разделяй existing / demo / new

| Mark на чертежах | Как читать | Что делать в takeoff |
| --- | --- | --- |
| `Existing` / `E` | Уже построено | Не считать, если не shown as repair/replacement. |
| `Existing to remain` | Остаётся | Не добавлять material. Проверить только connection к new work. |
| `Demo` / dashed removal | Удаляется | Считать только если demo scope requested. |
| `New` / dark line / keyed note | Новая работа | Считать как обычный material scope. |
| `Replace in kind` | Заменить таким же | Считать replacement area/length, но не весь existing run. |
| `Patch` / `Repair` | Локальный ремонт | Считать только указанную зону и добавить note. |

## Главные правила

- Сначала прочитай legend: line weights, dashed lines, hatch и keynote symbols.
- Не используй план существующего этажа как полный takeoff plan. Он часто нужен
  только для context.
- New-to-existing connections важнее обычных повторов: ledgers, anchors,
  straps, hangers, blocking и bearing points легко пропустить.
- Если drawings показывают только область ремонта, не умножай её на весь floor.
- Если opening переносится или расширяется, проверь header, king/jack studs,
  sill condition и sheathing patch.
- Если existing roof/floor вскрывается, проверь temporary support notes и
  sistering/scab/reinforcement details.
- Old sizes могут не совпадать с new sizes: не предполагай `2x10`, если detail
  показывает actual existing member.

## Где смотреть

| Где на чертежах | Что проверить |
| --- | --- |
| Cover / code / general notes | Что входит в remodel/reconstruction scope |
| Demo plans | Что удаляется и что остаётся |
| New work plans | Где реально появляется new framing |
| Structural details | Connections to existing, ledgers, straps, anchors |
| Elevations / sections | Height changes, roof tie-ins, wall rebuild zones |
| Keynotes | Patch/repair/replace notes, которые не видны на плане |
| Photos / field notes | Existing condition, если drawings неполные |

## Частые items

| Item | Когда появляется | Проверить |
| --- | --- | --- |
| Ledgers | New floor/deck/roof attaches to existing wall | Size, fasteners, PT/FRT, spacing |
| Hangers | New joists connect to existing beam/wall/ledger | Top mount vs face mount, skew, width |
| Blocking | Edge support, drywall backing, roof/floor patch | Это new blocking или existing? |
| Sistered joists/rafters | Усиление existing member | Length, count, side, fasteners |
| New headers | New/expanded openings | Ply count, LVL/2x, bearing |
| Anchor bolts / straps | New wall or ledger to existing concrete/framing | Material, spacing, embed/detail |
| Sheathing patch | Wall/roof/floor repair | Thickness, FRT/Zip/OSB/CDX, one side or both |
| Flashing / WRB | Tie-in at envelope | Не смешивать с full new wall sheathing |

## Output notes

Пиши assumptions видимо, особенно когда scope неясный:

- `Existing framing to remain - not counted.`
- `Counted new work only per shaded/keyed repair area.`
- `Header counted only at enlarged opening.`
- `Ledger/hangers counted at new-to-existing connection.`
- `Demo shown for context only - no demo material counted.`

## Проверить перед сдачей

- [ ] Existing и new work разделены.
- [ ] Demo plan не принят за material takeoff.
- [ ] Все new-to-existing connections проверены.
- [ ] Patch/repair zones не растянуты на весь floor.
- [ ] Headers/openings проверены только там, где opening new/modified.
- [ ] Notes в output объясняют, что не считалось и почему.

## See also

- [Residential](residential.md)
- [COM Commercial](com.md)
- [Exterior Walls](../work/vertical/walls/exterior.md)
- [Headers](../work/vertical/openings/headers.md)
- [Hangers](../reference/hangers.md)
