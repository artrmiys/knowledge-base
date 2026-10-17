# Правила клиентов и типов заказов

Что считаем и что нет, зависит от типа заказа и клиента. Scope читается из
пометок в папке проекта при приёме; если проект противоречит правилу ниже,
главнее чертежи и письмо клиента, а расхождение идёт нотой в шапку DFL.

## Типы заказов

| Пометка в папке / тип | Что считаем | Что не считаем | Нота в шапке DFL | Страница |
| --- | --- | --- | --- | --- |
| `Frame` (полный каркас) | Стены, проёмы, обшивка, площади, перекрытия, крыша, крепёж | Отделка, trims, interior doors | `Roof and Floor Trusses are by others` (проверить по комплекту) | [COM](../work-types/com.md), [Residential](../work-types/residential.md) |
| `Frame. Wall panels` (COM w/panel) | Loose scope: bracing, floor-height и box sheathing, truss heel, parapets, gables, shear plywood, holdowns, beams, posts; stick-исключения (под бетоном, в existing frame, короткие, наклонные) | Studs, plates, in-panel blocking и sheathing, типовые headers в панелях | `Walls are panels by others` | [Wall Panels](../work/vertical/walls/wall-panels.md) |
| `Frame. EWP by others` | Весь каркас кроме EWP: посты, обшивки, 2x, крепёж | I-joists, LVL/PSL/LSL, engineered rim | `All EWP products are by others`; `Walls are panels by others` удаляется, если panel scope нет | [EWP / Capital](../work-types/ewp-capital.md#ewp-by-others) |
| EWP only (Capital-type) | Только EWP: I-joists, LVL/PSL/GL, rim, hangers к ним | Обычный 2x, фермы, ties, гвозди | нота о составе scope | [EWP / Capital](../work-types/ewp-capital.md) |
| `Revision` / `rev` / `review` | Только изменения между комплектами; база - прошлая сдача | Старые и новые замеры не суммировать | нота о ревизии | [Процесс работы](workflow.md) |
| Reconstruction, `NO metal` | Новые и заменяемые стены stick, new-to-existing connections, новый subfloor по детали | Existing to remain, demo, стальные перегородки | `Metal Studs by others`, `Existing framing to remain - not counted` | [Reconstruction](../work-types/reconstruction.md) |
| `EXT` (только наружная отделка) | Siding, soffit, fascia, exterior trims, furring, flashing | Каркас, перекрытия, площади | нота о scope | [Siding](../work/siding/overview.md), [Exterior Trims](../work/exterior-trims/overview.md) |
| Interior trim и interior doors | Base (только wood), casing, crown, двери с материалом и fire label, shaft CH + liner | Tile base, gypsum (кроме шахт и наружных soffit), hardware numbers | нота о составе scope | [Interior Trims](../work/interior-trims/overview.md) |
| Progress set (комплект без конструктива) | Всё, что видно: стены, проёмы по рисунку, площади; остальное по допущениям | Точные балки, посты, shear, высоты - только как assumed | Развёрнутая нота: `beams, posts, balcony framing, shear walls and wall heights are assumed; verify`; стены под бетоном optional stick с нотой "verify if metal" | [Стандартные notes](../reference/standard-notes.md) |

## Типы зданий, которые приходят

| Тип | На что смотреть |
| --- | --- |
| Hotel | Porte cochere, storage и другие корпуса отдельными ветками и книгами; PTAC-проёмы; многослойный фасад (ZIP-R по типам фасада) дочитывать до всех слоёв |
| Podium, Type III | FRT всё в плоскости наружной стены: studs, plates, headers, blocking, sheathing; деревянные стены ниже podium тоже FRT. LVL/PSL/LSL в плоскости наружной стены нельзя, "LVL FRT" не писать. Стены под podium - stick, не панели |
| Жилой над паркингом | Паркинг: exterior-тип гипс и утеплитель по сборке; выше - обычный COM |
| Кондоминиумы, виллы, несколько корпусов | На каждый корпус своя папка в Takeoffs и своя книга; одинаковый конструктив близнецов - не ошибка, но каждая книга полная |
| Residential (один дом, гараж) | Гараж, porch, porte cochere - свои контуры и уклоны кровли; EWP по спецификации, не по привычке |

Тип конструкции (Type III, Type V-A, V-B) берётся из Code Compliance Summary на
обложке, это не условная нота. У Type V общего FRT нет. FRT и FRTW - разные
обозначения, писать как в проекте. Подробнее про FRT -
[Советы: FRT](../reference/boss-feedback-rules.md#frt).

## Metal studs по клиентам {#metal-studs}

| Клиент | Metal studs |
| --- | --- |
| WM | Считать и показывать |
| Timberline | Считать и показывать |
| Littleton | Считать и показывать |
| EBS | By others |
| Probuild | By others |
| Triangle | By others |
| Interstate | By others |
| Bliffert | By others |

Даже когда металл исключён, отмечай, где стоят metal studs и floors, и пиши
`Metal Studs by others`. Когда считаем: gauge в имени (`6" 18ga mtl`), deflection
track только у full-height стен до перекрытия, dropped soffits на обычных top
tracks. Подробно - [Metal Tracks / CFMF](../work/vertical/walls/metal-tracks.md).

## Что просил ревьюер клиента (октябрь 2026)

Замечания к сданным работам, принятые как правила:

- **Wall panels.** Не панели только стены под concrete slab, в existing frame,
  короткие и irregular sloped, возможно exterior build-up. Стена рядом с CMU
  спокойно делается панелью; не добавлять optional stick из-за соседства с CMU.
  Exterior build-ups не исключать из панелей автоматически: проверить конструкцию.
- **Optional.** "Be careful calling anything option, unless it totally assumed."
  У optional-блока обязательна нота с причиной: что не указано, что принято,
  что проверить. Пример: `Optional framing for unspecified roof corridor frame (assumed 2x10 - verify if truss)`.
- **H-clips** только для square edge, не для T&G.
- **Новый subfloor поверх существующего пола** по детали включать целиком:
  старое здание, старый пол, его накрывают весь.

## Указания клиентов по крепежу

- Holdown над балкой не требует transfer holdown ниже (указание клиента;
  записано как правило).
- Крепёж, явно показанный инженером, не удалять, даже если кажется лишним.
- Hangers: модель по детали, Zmax снаружи и на P.T. Формат записи -
  [Hangers](../reference/hangers.md).

## Где это применяется

| Правило | Страница |
| --- | --- |
| Состав panel package, stick-исключения | [Wall Panels](../work/vertical/walls/wall-panels.md) |
| FRT по типу конструкции | [COM Commercial](../work-types/com.md), [Советы: FRT](../reference/boss-feedback-rules.md#frt) |
| Двери: labels, fire rating, двойные | [Windows and Doors](../work/vertical/openings/windows-doors.md) |
| Interior: base, tile, common areas | [Interior Trims](../work/interior-trims/overview.md) |
| Ноты для by others и assumed | [Стандартные notes](../reference/standard-notes.md) |

## См. также

- [Типы работ: COM](../work-types/com.md), [EWP / Capital](../work-types/ewp-capital.md), [Reconstruction](../work-types/reconstruction.md), [Residential](../work-types/residential.md)
- [Советы и важные вещи](../reference/boss-feedback-rules.md)
- [Частые ошибки](common-mistakes.md)
