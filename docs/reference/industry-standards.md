# Отраслевые стандарты и best practices

Куда наш takeoff/estimating ложится в общеотраслевую систему координат. Шпаргалка: на что похоже, какие стандарты, что мы и так делаем правильно.

!!! tip "Зачем эта страница"
    Чтобы говорить с GC/инженерами на одном языке (CSI-коды в спеках), не
    забывать целые куски scope (особенно Division 07), и понимать, что наш
    workflow = индустриальный **assembly-based estimating**, просто заточенный
    под E-Wood.

## Assemblies — наша единица работы { .kb-section-title .kb-st--green }

Индустрия (RSMeans и пр.) считает не каждый гвоздь отдельно, а **assemblies**
(«systems») — готовые наборы строк на единицу:

- **per 1 LFT** framing (стены, plates, bracing) — `LFT × фактор`.
- **per 1 SQFT** (sheathing, subfloor, insulation) — `area / 32` (лист) или `area × 1.1`.
- **per each** (hangers, holdowns, posts).

!!! note "Наш DFL = библиотека assemblies"
    Каждый блок DFL (Foundation, Floor Walls, Truss Heel, Roof, Decking…) —
    это assembly с формулой на LFT/SQFT/each. Waste-фактор уже внутри.
    Полная библиотека (37 блоков, формулы, провенанс из 180 проектов) — в
    Obsidian-wiki `wiki/E-Wood/blocks/`.

## CSI MasterFormat — нумерация для спеков { .kb-section-title .kb-st--cyan }

6-значные коды, «Dewey Decimal стройки». Мы **уже** их пишем в E-колонке DFL и
notes (`07.04 WD-01`, `05.01` guardrail, `07.01-07.03` EIFS).

| Div | Что | Наши работы |
| --- | --- | --- |
| **03** | Concrete | foundation (by others), sill/anchor на стыке |
| **05** | Metals | alum railings, steel beams, **Simpson коннекторы** |
| **06** | **Wood/Plastics** | **ядро** — всё framing (studs, plates, headers, sheathing, stairs, decking PT, finish carpentry) |
| **07** | **Thermal & Moisture** | sheathing-как-WRB, vapor barrier, insulation, tape, flashing, **siding**, roofing |
| **08** | Openings | двери/окна (Int Doors) |
| **09** | Finishes | gypsum/drywall, interior trims/base/casing/crown, EIFS |

!!! warning "Division 07 — не забывать"
    Boss-правило «вертикалка ≈ 50% здания» во многом про Div 07: vapor barrier,
    tape, flashing, insulation, siding. Самые частые пропуски — отсюда. Прошёлся
    по 06/07/08/09 → ничего не забыл.

## Best practices — что мы делаем правильно { .kb-section-title .kb-st--magenta }

| Best practice (индустрия) | У нас |
| --- | --- |
| Assembly per LFT/SQFT | ✅ формулы блоков |
| Waste 10-15% | ✅ `1.1` general (rim EWP `1.05`) |
| Group by size (studs/joists) | ✅ nested-IF по высоте стены |
| Templates/checklists для consistency | ✅ scope-профили + [QA checklist](../start/quality-checklist.md) |
| Flag risk / проверка раньше | ✅ validate ловит пропуски (section+row level) |
| Stud spacing factors 12/16/24 = 1.4667/1.1/0.625 (joists — отдельно по `12/spacing`) | ✅ [Формулы](formulas.md) |

## AI-takeoff контекст { .kb-section-title .kb-st--amber }

Коммерческие AI-takeoff (Togal, Kreo Caddie, Beam, Attentive) = **computer-vision
по чертежам** → детект/счёт элементов. **OurPlanCore** — наш аналог этого слоя.
Но они дают только количества; **наш DFL-wiki + правила = слой ВЫШЕ** (что собрать
+ правильно ли). Это не конкурент — это то, что идёт ПОСЛЕ замера.

## Связь с DFL-wiki (output-сторона)

Эта KB — про **как мерить** (takeoff). Парная Obsidian-wiki `wiki/E-Wood/` — про
**что собрать в Excel** (DFL-блоки, формулы, валидация). Мост:
`wiki/E-Wood/reference/takeoff-to-dfl.md` (токен ext/1st/porch → блок). Подробный
ресёрч и CSI-маппинг — там же (`research-positioning.md`, `csi-mapping.md`).

## Источники

- RSMeans — [Unit & Assembly Estimates](https://www.rsmeans.com/resources/creating-unit-assembly-estimates-rsmeans-online)
- Autodesk — [5 Steps to Lumber Takeoff](https://www.autodesk.com/blogs/construction/framing-lumber-takeoff/)
- Procore — [CSI MasterFormat](https://www.procore.com/library/csi-masterformat); Swiftlane — [Div 06](https://swiftlane.com/blog/csi-masterformat-division-06/)
- Togal.ai, Kreo, Trimble (AI takeoff 2026)
