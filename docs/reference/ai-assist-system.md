# ИИ-ассистент: предсказание и проверка DFL

Как ИИ использует эту KB (+ парную output-wiki по DFL) чтобы **предсказывать состав
takeoff по словам/scope, помогать заполнять per-project и проверять готовую работу** —
и куда система движется. Это «карта стратегии».

!!! abstract "В одну фразу"
    Эта wiki описывает **как мерить** (takeoff-структура, правила, формулы).
    Парная output-wiki (`wiki/E-Wood/`, 37 блоков DFL) описывает **что строить**
    в Excel. ИИ соединяет их в петлю: по scope предсказывает состав → помогает
    читать per-project с чертежа → пересчитывает блоки → сверяет готовый DFL с
    корпусом из 180+ проектов.

## Полная петля { .kb-section-title .kb-st--green }

```text
①  Новый проект (scope.txt + Plans/*.pdf)
        │  scope-теги + ⚑спец-флаги (EWP BO / not-zip / stick / revision / RUSH)
        ▼
②  SUGGEST состав DFL  —  CORE-секции под scope (из модели 180 файлов)
        ▼
③  ИЗМЕРЕНИЕ на PDF (PlanSwift / OurPlanCore) → SQFT/walls
        ▼
④  PER-PROJECT данные  —  где на чертеже schedules → читать B/H/wall/F-P-W коды
        │  locked-дефолты пред-заполнены (Zip Tape, 29OZ)
        ▼
⑤  DFL пересчитывает БЛОКИ (формулы + waste внутри)
        ▼
⑥  VALIDATE  —  сверка готового DFL с корпусом (секции / строки / количества)
        ▼
⑦  INGEST готового → корпус растёт → следующее предсказание точнее
```

Каждый завершённый проект делает петлю умнее — это **compounding** база, а не
статичная инструкция.

## Три операции ассистента { .kb-section-title .kb-st--cyan }

=== "SUGGEST (по словам → состав)"

    Вход — scope словами (`COM frame walls panels`, `EWP siding`). Выход —
    **стартовый состав DFL**: CORE-секции под этот scope (ранжированы по частоте
    в корпусе) + что пред-заполнить (locked-дефолты) + что читать с чертежа
    (per-project ячейки). Отвечает на «что вообще собирать».

=== "VALIDATE (3 уровня)"

    Сверяет готовый файл с тем, что делают проекты того же scope:

    1. **Секции** — ожидалась, но отсутствует (есть у ≥60% peers) → вероятный пропуск.
    2. **Строки** — внутри секции нет типовой строки (есть у ≥70% peers того же scope).
    3. **Количества** — значение вне типового диапазона (IQR/Tukey по `(секция, строка)`
       из 180 проектов) → проверить (опечатка/единицы/scope-аномалия).

    Это автоматический дубль к [QA checklist](../start/quality-checklist.md) —
    ловит «забыл Anchor Bolts в Foundation» (есть почти у всех похожих) до отправки.

=== "PDF→spec (читать с чертежа)"

    Находит, на каких листах лежат BEAM/HEADER/SHEAR WALL/HOLDOWN schedules и
    spec-ноты (roof/wall sheathing) → кропит регион в high-DPI → ИИ читает коды.
    Тот же механизм, что `crop→AI` в [OurPlanCore](ourplanecore.md);
    закрывает шаг ④ «читать per-project».

## Stable-дефолты vs per-project { .kb-section-title .kb-st--magenta }

Ключевой принцип: ассистент **пред-заполняет только стабильное** и **никогда не
копирует per-project вслепую**.

| Категория | Примеры | Откуда |
| --- | --- | --- |
| **Locked** (авто-префил) | Zip Tape, 29OZ membrane | константа по всему корпусу |
| **Common default** (поставить, проверить) | `7/16" Zip`, `3/4" T&G` subfloor | дефолт, но смотреть scope |
| **Per-project** (читать с чертежа) | wall sheathing override, roof/insulation specs, anchor spacing, **beam/header B-/H-коды**, holdowns, hangers | schedule/детали PDF |

!!! warning "Per-project — всегда с чертежа"
    Beam B-коды, porch slope, anchor spacing, holdown-марки **разные в каждом
    проекте**. Detail callouts (N/Sheet) сверять в PDF, не копировать из нот
    вслепую. См. [boss-feedback-rules](boss-feedback-rules.md).

## Куда движемся (roadmap) { .kb-section-title .kb-st--blue }

- [x] Корпус прочитан и описан (180+ DFL, секции/строки/количества/hardware).
- [x] SUGGEST — scope → CORE-состав; брифинг входящих батчем.
- [x] VALIDATE — 3 уровня (секции / строки / количества, scope-условно).
- [x] PDF→spec — доказан end-to-end (locate → crop → читать).
- [x] Позиционирование в индустрии — [assemblies / CSI](industry-standards.md).
- [ ] **Авто-парсинг** прочитанной schedule-таблицы в структурный legend (B/H/wall → спеки).
- [ ] **Validate по спеке** (не только количества): сверять master-cells со spec-нотами PDF.
- [ ] **NL→Excel** — целевое: по словам + чертежу собрать черновик DFL на проверку.
- [ ] Масштаб 500+ проектов — каждый ingest уточняет частоты и диапазоны.

!!! note "Что НЕ делает ассистент"
    Не правит формулы (они — авторская работа, ценность KB = состав под scope и
    проверка, не пере-инжиниринг). Не считает за оценщика — даёт стартовый
    состав, подсказки и контроль. Решение всегда за человеком.

## См. также

- [Отраслевые стандарты](industry-standards.md) — assemblies / CSI / best-practices.
- [OurPlanCore](ourplanecore.md) — программа: измерение + crop→AI.
- [Формулы и факторы](formulas.md) — что пересчитывают блоки.
- [QA checklist](../start/quality-checklist.md) — ручная проверка, которую дублирует VALIDATE.
- [Workflow](../start/workflow.md) — общий рабочий процесс.
