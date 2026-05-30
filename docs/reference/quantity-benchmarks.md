# Quantity benchmarks (sanity-check)

Типовые количества и длины по корпусу из 180+ takeoff'ов — чтобы быстро понять
«нормальное ли число». Это **не жёсткие правила**: диапазоны широкие (проекты
разного размера), значение вне диапазона = «посмотри», а не «ошибка».

!!! tip "Как пользоваться"
    Сомневаешься в числе — глянь медиану и диапазон `[q1–q3]` тут.
    Напр. «66 anchor bolts при 350 ft termite shield — нормально?» → да, в норме.

## Факторы vs индустрия (сверено ✅) { .kb-section-title .kb-st--green }

| Фактор | У нас | Индустрия | Вердикт |
| --- | --- | --- | --- |
| Studs 16" o.c. | **×1.1** | «1 стойка/фут + 10% waste» (не геометрич. 0.75) | ✅ ровно стандарт |
| Studs 24" o.c. | **×0.625** | «0.5 + 25% waste» | ✅ совпадает |
| Waste general | **×1.10** | 10–15% | ✅ в норме |
| Rim EWP | **×1.05** | engineered точнее → меньше waste | ✅ обосновано |
| Bracing | 1 / 8 ft | (наш дефолт) | ок |

Вывод: факторы = индустриальные нормы, не «на глаз». См. [Формулы](formulas.md).

## Длины (стандартные stock-размеры) { .kb-section-title .kb-st--cyan }

Длины кластеризуются на доступных длинах доски — `med [q1–q3]`:

| Позиция | med длина | Норма |
| --- | --- | --- |
| Beam | 12 [8–16] | dimensional 8/10/12/14/16 |
| Joist | 12 [10–16] | — |
| Stringers | 10 [10–14] | — |
| Treads / Risers | **12** (всегда) | стандарт марша |
| Sub Fascia / Truss Bracing | **16** (всегда) | макс stock-доска |
| Posts (deck/porch) | 10 [8–10] | 6x6 PT |
| Blocking | 16 / 8 | stick |

## Количества (порядок величин) { .kb-section-title .kb-st--magenta }

| Позиция | med qty [q1–q3] |
| --- | --- |
| Foundation Anchor Bolts | 66 [34–180] |
| Foundation Washer | 120 [50–224] |
| Termite shield | 350 LFT [200–600] |
| Beam (per beam, Wall Materials) | 3 [2–4] |
| Hangers (Wall Materials) | 16 [5–62] |
| Decking Posts | 4 [2–8] |
| Sub Fascia (flat roof) | 27 [18–38] |

## Как мы проверяем (метод) { .kb-section-title .kb-st--blue }

Глобальные пороги на construction-данных не работают (проекты гетерогенны), поэтому
проверка **context-aware**: для каждой пары `(секция, строка)` строим распределение
по корпусу и применяем **Tukey fences** — значение вне `[q1 − 1.5·IQR, q3 + 1.5·IQR]`
или вне corpus min–max помечается «нетипичное количество, проверь». Robust к выбросам
(median/IQR, не среднее). Это и есть quantity-уровень в [VALIDATE](ai-assist-system.md).

## См. также

- [Формулы и факторы](formulas.md) — откуда множители.
- [Hardware catalog](hardware-catalog.md) — что за позиции.
- [QA checklist](../start/quality-checklist.md) — ручная проверка.
- [ИИ-ассистент](ai-assist-system.md) — как считаются диапазоны.
