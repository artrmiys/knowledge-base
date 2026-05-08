# Maintenance

## Repo

This wiki is a MkDocs Material project.

```powershell
python -m mkdocs serve
python -m mkdocs build --strict
```

GitHub Actions deploys to `gh-pages` on push to `main`.

## Update Rules

- Keep pages short enough to scan during work.
- Put reusable rules in `Reference`.
- Put task-specific instructions in the closest `Work` page.
- Prefer tables for selection rules, factors, and client exceptions.
- Add assumptions explicitly; do not hide them in prose.

## Redaction Rules

Do not publish:

- Employee emails or UIDs.
- Salary history or private payroll tables.
- Dropbox links and private chat links.
- Credentials, API keys, server passwords, or personal contact data.

If a private source contains a useful rule, rewrite the rule without the private
identifier.

## Регламент работы над ошибками

### Файловое хранилище

- Всё хранится в **MEGA** (облако).
- Готовый PlanSwift и финальные файлы — **только в облаке**.

### Проверяющий

1. Открывает PlanSwift и Excel, проверяет, **пишет ошибки в облаке** (в соответствующей заметке/файле).
2. Если ошибки есть — в Trello ставит **красную метку**, убирает зелёную, снимает даты.
3. В Telegram пишет: **номер дома** + «нужно/не нужно править».
4. Всегда указывает, **где править Excel**: `[локальный]` или `[облачный]`. Пишет, какие правки уже сделал.
5. Если срочно — сам ставит дедлайн и указывает: правим всё или отправляем как есть (с коротким описанием, что сделано).

### Worker

1. Открывает PlanSwift и начинает правки, параллельно задаёт вопросы.
2. В Trello — **жёлтая метка** и примерная дата готовности.
3. Excel править.
4. После завершения правок — **зелёная метка**.

### Итерации

- Цикл может повториться **2–3 раза** до полного согласования.
- На разбор ошибок резервируй **30–60 минут**.

### Финальная проверка («было/стало»)

См. [Quality Checklist → Финальная проверка](quality-checklist.md).
