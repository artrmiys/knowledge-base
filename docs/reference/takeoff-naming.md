# Как называть takeoffs

Правила именования takeoff-items в OurPlaneCore. Эти имена напрямую влияют на:

- **Auto-routing** — куда упадёт новый item: `sqfts`, `walls`, `framing` и т.д.
- **Sort order** — в каком порядке item появится внутри папки и в Excel export.
- **Folder matching** — нужная папка определяется по нормализованному имени, не по тому, какая папка сейчас выделена.

!!! tip "Главное правило"
    Используй короткие токены из словаря ниже. Программа лучше распарсит
    `ext 2x6 x` чем `Exterior wall 2x6 staggered`. Длинные читабельные имена
    оставляй в `Notes`.

## Нормализация имени { .kb-section-title .kb-st--cyan }

При создании item имя нормализуется:

| Шаг | Правило | Пример |
| --- | --- | --- |
| Регистр | всё → lowercase | `Ext 2x6 X` → `ext 2x6 x` |
| Разделители | `_`, `-`, `.`, лишние пробелы — токены | `ext_2x6-x` → `ext 2x6 x` |
| Compound sizes | сохраняются | `2x6`, `2x4 half` |
| Aliases | разворачиваются в long form | `cant` ↔ `cantilevered`, `blcny` ↔ `balcony` |
| Roof family | `rf x`, `rf mtl x` → `rf` family | `rf mtl 1` → `rf` |

**Правило matching:** программа ищет **токены**, не подстроки. `corners` НЕ
совпадёт с `cor` (wall token), потому что `corners` — отдельный полный токен.

## SQFT items { .kb-section-title .kb-st--green }

Если нормализованное имя содержит один из токенов ниже — item уйдёт в папку
`sqfts`:

| Группа | Токены |
| --- | --- |
| База / floors | `base`, `1st`, `2nd`, `3rd`, `4th`, `5th`, `6th`, `7th`, `8th` |
| Outdoor | `deck`, `porch`, `blcny`, `balcony`, `cant`, `cantilevered` |
| Roof areas | `flat`, `rf`, `rf mtl x` |

### Sort внутри `sqfts`

```text
base
1st → 2nd → 3rd → 4th → 5th → 6th → 7th → 8th
deck
porch
blcny / balcony
cant / cantilevered
flat
rf
unknown SQFT names — by natural name
```

!!! warning "Floors не объединяй"
    `1st`, `2nd`, `3rd`... остаются отдельными items даже если geometry похожа.
    Не суммируй totals по нескольким этажам, только потому что имена похожи —
    это правило клиента (E-Wood / WM).

## Wall items { .kb-section-title .kb-st--magenta }

Если имя начинается с одного из этих токенов — item классифицируется как wall:

| Token | Расшифровка |
| --- | --- |
| `ext` | Exterior wall |
| `cor` / `corr` | Corridor wall |
| `dem` | Demising wall |
| `2x4 x` / `2x6 x` / `2x8 x` | Wall by stud size |
| `2x4 half` / `2x6 half` | Half-height wall |

### Auto-route по active sheet

Walls попадают в подпапку `walls / {floor} floor walls`, если в имени активного
sheet есть один из суффиксов:

```text
base, 1st, 2nd, 3rd, 4th, 5th, 6th, roof, parapet
```

Suffix matching пропускает разделители: `A101 1st`, `A101-1st`, `A101_1st`,
`FLOOR PLAN 1ST` — все совпадут с `1st`.

**Пример:**

| Active sheet | New item | Куда попадёт |
| --- | --- | --- |
| `A101 1st` | `ext 2x6 x` | `walls / 1st floor walls` |
| `A102 2nd` | `cor 2x6 x` | `walls / 2nd floor walls` |
| `A103 3rd` | `corr (2) 2x4 x` | `walls / 3rd floor walls` |
| sheet без суффикса | `dem 2x6 x` | `walls/` (root) + warning |

### Sort внутри floor folder

```text
corners
ext
cor / corr
dem
2x4
2x6
2x8
half
unknown wall names — by natural name
```

## Когда auto-routing НЕ срабатывает

| Кейс | Поведение |
| --- | --- |
| Имя не совпадает ни с одним SQFT/wall токеном | Остаётся в текущей выделенной папке |
| Wall token есть, но sheet suffix не определился | `walls/` root + status: `Wall item routed to walls; sheet level was not detected` |
| Имя похоже на token, но это совпадение | Не route'ится: `corners` ≠ `cor`, `corner block` ≠ wall |
| User вручную перенёс item | Manual всегда побеждает; auto-route не повторяется |

## Примеры { .kb-section-title .kb-st--amber }

| Имя при создании | Нормализовано | Куда |
| --- | --- | --- |
| `1st` | `1st` | `sqfts` |
| `Porch` | `porch` | `sqfts` |
| `cant` | `cant` (alias `cantilevered`) | `sqfts` |
| `rf mtl 1` | `rf mtl 1` (rf family) | `sqfts` |
| `ext 2x6 x` (sheet `A101 1st`) | `ext 2x6 x` | `walls / 1st floor walls` |
| `cor 2x4 staggered` (sheet `2nd`) | `cor 2x4 staggered` | `walls / 2nd floor walls` |
| `corners` | `corners` | текущая папка (не wall) |
| `Exterior 2x6 wall` | `exterior 2x6 wall` | текущая папка (не token `ext`) |

## See also

- [OurPlaneCore — программа](ourplanecore.md)
- [Workflow](../start/workflow.md)
- [Структура takeoff](../start/takeoff-structure.md)
- [Советы и важные вещи](boss-feedback-rules.md)
