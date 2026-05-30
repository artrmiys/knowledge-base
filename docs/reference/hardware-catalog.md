# Hardware catalog (Simpson) — corpus-derived

Что **реально стоит** в проектах: словарь крепежа Simpson Strong-Tie, собранный по
корпусу из 180+ takeoff'ов. Частота = в скольки файлах встречается. Это словарь
(«какой spec под какое соединение»), а выбор за 30 секунд — в [Hangers](hangers.md).

!!! tip "Как читать"
    `Zmax`/`Z`-суффикс = горячая оцинковка (наружка / PT-древесина). `E`-суффикс у
    holdown = embedded (заливной анкер, не post-installed). Цифра в модели обычно =
    сечение/нагрузка (`ABU66` → 6x6 post; `HDU8` > `HDU4` по нагрузке).

!!! warning "Это словарь, не дефолты"
    Все spec'и — **per-project по деталям/schedule**. Список показывает, что
    типично, но конкретная модель берётся из structural notes проекта.

## Joist / beam hangers { .kb-section-title .kb-st--green }

| Spec | freq | Назначение |
| --- | ---: | --- |
| `LUS210` (+`-2/-3`, `Zmax`) | 17 | стандартный face-mount для 2x10 (`-2/-3` = 2/3-ply) |
| `LUS26` / `LUS28` | 10 / 4 | для 2x6 / 2x8 (`-3` = 3-ply, `Zmax` наружка) |
| `LUS212` / `LUS24` | 5 / 3 | для 2x12 / 2x4 |
| `LUC26` | 9 | concealed-flange 2x6 |
| `HUC210-2/-3`, `HUC410-2`, `HUC214-3` | 1–2 | heavy face-mount (2/3-ply, `Zmax`) |
| `HU9` / `HU410` / `HU412` / `HU48` | 1–3 | heavy U-hanger |
| `HHUS5.50/10·/12·/14`, `HHUS48`, `HHUS210-3` | 2+ | heavy hi-cap (LVL / большие балки) |
| `HUCQ210-3`, `HUCQ610`, `HUCQ412 Zmax` | 1–2 | concealed heavy (лестница / platform / balcony beams) |
| `LRU210Z` / `LRU212Z` / `LRU24Z` / `LRU28Z` | 8 / 6 / 6 / 3 | **rafter/slope hangers** (skewed/sloped — porch/roof) |
| `MIT`, `ML26Z`, `ML24Z`, `ML28` | — | misc / lite beam hanger |

## Ties / clips (uplift, truss/rafter→plate) { .kb-section-title .kb-st--cyan }

| Spec | freq | Назначение |
| --- | ---: | --- |
| `H2.5` / `H2.5A` | 30 / 3 | hurricane tie — **самый частый** (truss/rafter-to-plate) |
| `H1` / `H3` / `H8` / `H10` | 1–2 | tie по нагрузке |
| `A35` | 11 | framing angle (универсальный) |
| `A34` | 2 | framing angle (меньше) |
| `HGA10` / `HGA10KT` | 1 / 2 | hurricane gusset angle (+KT kit) |
| `A35 or LTP4` | 14 | framing angle ИЛИ lateral tie plate (взаимозаменяемы) |

## Straps (continuity / tension) { .kb-section-title .kb-st--magenta }

| Spec | freq | Назначение |
| --- | ---: | --- |
| `MSTC66` / `MSTC40` / `MSTC52` / `MSTC48` | 9 / 6 / 5 / 2 | medium strap coiled (длина в имени) |
| `MSTA49` | 7 | medium strap 49" (continuity across floors) |
| `MST72` / `MSTD4` | 4 / 4 | medium strap прямой |
| `LSTA24` | 14 | light strap 24" |
| `CS16` / `CS14` / `CS20` | 14 / 9 / 6 | coiled strap (режется по футажу) |

## Post bases / caps { .kb-section-title .kb-st--amber }

| Spec | freq | Назначение |
| --- | ---: | --- |
| `ABU66 Zmax` / `ABU44` / `ABU88` / `ABU68` | 37 / 7 / 7 / 2 | **ABU post base** (размер = сечение поста: 44/66/68/88) |
| `BCS2-3/6 Zmax` / `BCS2-2/4` | 15 / 4 | post cap/base (2-3 ply / 6x) |
| `CCQ66` / `CCQ46` / `CCQ44` / `CCQ68` | 2–7 | **CCQ column cap** (по сечению) |
| `ECCQ66` / `ECCQ46` Zmax | 3 / 4 | **end column cap** (cantilever / край) |
| `PC6Z` / `PCZ` / `PB66 Zmax` / `CBSQ66 Zmax` | 3–4 | post cap / post base (lite / standoff) |

## Holdowns (shear wall) { .kb-section-title .kb-st--blue }

| Spec | freq | Назначение |
| --- | ---: | --- |
| `DTT2Z` | 24 | deck/light tension (1-storey, лёгкая) |
| `HDU8/4/2/5/11/14/19` | 17/15/11/9/9/6/2 | **HDU-серия — рабочая лошадка** (цифра = модель по нагрузке) |
| `HDUE7/5/3/9/13` | 12/11/9/6/2 | **HDU Embedded** (заливной анкер, не post-installed) |
| `HTT5KT` / `HTT5K` | 10 / 1 | tension holdown (KT = kit) |
| `TBD HD` | — | placeholder когда shear walls не определены |

!!! note "Holdown на практике"
    Почти всегда из **HDU / HDUE-серии**, выбор по нагрузке из shear-wall schedule
    (`HDU2 < 4 < 5 < 8 < 11 < 14 < 19`). `HTT5K` реже; `DTT2Z` — лёгкие / deck.

## Structural screws { .kb-section-title .kb-st--orange }

| Spec | Назначение |
| --- | --- |
| `SDS25600` / `SDS25312` / `SDS25300` | структурные SDS-винты (по длине) |
| `SDWS22500DB` / `SDWS22600DB` | structural wood screw 5" / 6" (stair / deck) |
| `SDWC6` | truss screw |

## Шпаргалка по умолчанию

- **Hanger** — по балке/нагрузке/mount: 2x10 → `LUS210`; 3-ply → `-3`; heavy/LVL →
  `HUC`/`HHUS`; наружка/PT → `Zmax`. Логика выбора — [Hangers](hangers.md).
- **Tie** по умолчанию `H2.5` (uplift); framing angle `A35`.
- **Post 6x6:** база `ABU66 Zmax` + кап `BCS2-3/6` или `CCQ66`; консоль → `ECCQ66`.
- **Holdown** по shear-wall schedule; нет данных → `TBD HD`.

## См. также

- [Hangers](hangers.md) — выбор hanger по condition (mount / depth / skew).
- [Material catalog](material-catalog.md) — древесина и материалы.
- [Quantity benchmarks](quantity-benchmarks.md) — сколько штук типично.
- [ИИ-ассистент](ai-assist-system.md) — откуда корпус-частоты.
