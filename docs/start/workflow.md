# Workflow

## 1. Подготовить PDF

1. Импортировать PDF.
2. Переименовать листы и разложить их по структуре.
3. Установить scale и проверить его по известному размеру на чертеже.
4. Просмотреть Arch + Structural + specs перед массовой разметкой.
5. Отметить сомнительные места notes, чтобы не забыть при Excel output.

## 2. Разметка takeoff

Базовый порядок для COM:

1. Vertical Constructions: Exterior, Corridor, Demising, Unit/Interior.
2. Openings.
3. Sheathing.
4. SQFT.
5. Floor Framing: Post, Beam, Joist, Details.
6. Roof Framing.
7. Sheathing and Misc.
8. Deck / Porch / Balcony.
9. Ties / Connectors.

## 3. Правила разметки

- Beams отмечать top-down / left-right.
- Длина beam зависит от точки опирания.
- Beams 8' и длиннее округлять до ближайших 2'.
- Beams меньше 8' оставлять без округления.
- Joists внутри одного run продолжать одним spacing top-down или left-right.
- Не начинать spacing заново от внутренней балки.
- Удалять joist только если он попадает прямо на beam примерно в пределах 2".

## 4. Export в Excel

- Экспортировать takeoff quantities.
- Перенести в template.
- Разнести категории: Beams, Joists, Details, Walls, Sheathing, SQFT.
- Проверять новые формулы сразу, а не после полного job.
- Не применять 1.1 повторно, если формула уже ссылается на данные с waste.

## 5. Перед отправкой

Пройти [Quality Checklist](quality-checklist.md). Для больших COM jobs делать
PDF sketch/markups, если есть риск забыть детали.
