# Формулы и факторы

!!! warning "Stud ≠ Joist — это разные факторы"
    У **studs** и **joists** один и тот же `o.c.`, но **разные множители**.
    Studs считаем по boss-rule (`1 стойка/фут + waste`), joists — по реальной
    геометрии center-to-center (`12 / spacing`). Не путай таблицы местами.

## Stud spacing factors

Канонический источник по стойкам. Boss-rule: на `16" o.c.` считаем **1:1**
(одна стойка на фут) **+ 10% waste**, а не геометрические `0.75`. Это сделано
намеренно — учитывает corners, T-intersections, jack/king/cripple вокруг
проёмов и обрезь.

| Spacing | Фактор (pcs / LFT) | Откуда |
| --- | ---: | --- |
| 12" o.c. | **1.4667** | `1:1` масштаб 16→12 (×1.333) + 10% waste |
| 16" o.c. | **1.1** | `1:1` + 10% waste |
| 24" o.c. | **0.625** | `0.5` + 25% waste |

- Формула: `pcs = wall LFT × фактор`.
- На больших COM jobs studs часто считают по **точной высоте** (nested-IF
  авто-подбор 2x4/2x6), см. [Exterior Walls](../work/vertical/walls/exterior.md).
- Сравнение с примерами сопоставимого scope и его ограничения —
  [Quantity benchmarks](quantity-benchmarks.md). Это проверка разумности результата,
  а не универсальная отраслевая норма, заменяющая чертежи и правила проекта.

## Joist spacing factors

Joists (и rafters, и floor trusses) считаем по **истинной геометрии**
center-to-center, без stud-waste. Фактор = `12 / spacing`.

| Spacing | Фактор (pcs / LFT ширины) |
| --- | ---: |
| 12" o.c. | **1.0** |
| 16" o.c. | **0.75** |
| 19.2" o.c. | **0.625** |
| 24" o.c. | **0.5** |

- Формула: `pcs = run ширина LFT × 12 / spacing`, **+1** торцевой joist на каждый run.
- Hangers по joists: `=ЧЁТН(LFT × 12 / spacing)` — округление вверх до чётного.
- Подробно — [Joist](../work/horizontal/floor-framing/joist.md).

## Rim и Blocking

| Item | Unit | Фактор |
| --- | --- | --- |
| Rim Board (EWP-jobs) | LFT | `1.05` |
| Rim Board (residential / COM / прочее) | LFT | `1.1` |
| Blocking | LFT | без factor, если continuous |
| Ribbons / ledgers / bracing | pieces | используй 16' ceiling, когда требуется |

- `1.05` — это EWP-specific factor. На обычных jobs rim считается тем же
  `1.1`, что и blocking.

## COM Waste

- Используй 1.1 в formulas, если source value уже не содержит 1.1.
- Не дублируй waste через chained formulas.

## Shaft Walls

Shaft walls записывай отдельным блоком, даже если основной wall scope идет как panels/by others.
Материал бери из wall type / detail: бывают `2-1/2"` CH + J-channel и `2"` H + C-channel assemblies.

!!! note "Excel"
    В русской локали Excel `CEILING(...)` отображается как `ОКРВВЕРХ(...)`.
    В формулах ниже использованы единицы измерения: `LFT`, `Horizontal LFT`,
    `Perimeter LFT`, `Stock LF`. В Excel подставляй реальные source/stock cells.

`Stock LF` обычно = `12`; panels идут в лист как `2x12 Panels`.

### 2-1/2" CH + J-channel assembly

```excel
1" Shaft Panels       = CEILING(LFT * 1.1 / 24, 2)
CH-channels vertical  = CEILING(LFT * 0.5 * 1.1 / Stock LF, 2)
J-channels horizontal = CEILING(Horizontal LFT * 1.1 / Stock LF, 2)
```

### 2" H + C-channel assembly

```excel
1" Shaft Panels, 2 слоя = CEILING(LFT * 2 * 1.1 / 24, 2)
H-channels vertical     = CEILING(LFT * 0.5 * 1.1 / Stock LF, 2)
H-channels horizontal   = CEILING(Horizontal LFT * 2 * 1.1 / Stock LF, 2)
C-channels perimeter    = CEILING(Perimeter LFT * 1.1 / Stock LF, 2)
```

## Dropped Ceiling Metal Joists

```text
12" C-type metal joists = Area * 0.75 * 1.1 LF
```

## Blocking formulas

```excel
Flat 48" o.c.     = CEILING(LFT * 12 / 48 * 2 * 1.1 / Stock LF, 1)
Diagonal 48" o.c. = CEILING(LFT * 12 / 48 * 2.5 * 1.1 / Stock LF, 1)
```

### Blocking factor по типу

Множитель зависит от типа блокинга (сколько кусков на пролёт):

| Тип | Фактор |
| --- | ---: |
| Flat | `2` |
| Diagonal | `2.5` |
| Vertical | `1.5–2` |

Diagonal дороже flat (длиннее рез + угол); vertical — между ними, ближе к flat
при плотной раскладке. Continuous blocking считается без factor (см. выше).

## Контрольные диапазоны количеств (sanity-check)

Если для задачи отдельно настроен внешний процесс проверки и доступен проверенный
корпус сопоставимых проектов, **итоговые количества** DFL можно сравнить по
`(секция, строка)`, единицам и scope. Median / IQR и Tukey fences — способы
статистического сравнения, а не обязательные нормы расхода. Выход за диапазон
требует проверки причины: опечатка, единицы или особенность scope; сам по себе
он не доказывает ошибку.

Упоминание `VALIDATE` и корпуса **180+ проектов** относится к прежнему описанию
внешнего процесса; эта страница не подтверждает их текущую готовность или запуск.
Не считай такую сверку встроенной автопроверкой OurPlanCore. Выполненную проверку
подтверждает конкретный отчёт с источниками и замечаниями. Ручной
[QA checklist](../start/quality-checklist.md) остаётся обязательным; границы
внешнего процесса — в [ИИ-ассистент](ai-assist-system.md).

## Kitchen and Bath Blocking

| Location | Правило |
| --- | --- |
| Kitchen | 2x6 blocking, 4 pieces of 14' на kitchen |
| Bathroom | 2x6 blocking, 1 piece of 14' на bathroom |
