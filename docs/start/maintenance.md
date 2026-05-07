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

<!-- confluence-context:start -->
## Confluence Context

Эта секция показывает, какие Confluence-страницы питают эту wiki-страницу и какие соседние темы связаны с ней через исходники.

| Source | Role here | Images | Raw MD |
| --- | --- | ---: | --- |
| [регламент работы над ошибками](https://ewood.atlassian.net/spaces/work/pages/92110850) | content | 0 | `imports/live-sources/confluence-work/pages/01-92110850-регламент-работы-над-ошибками.md` |

### Source Notes

??? note "регламент работы над ошибками"
    Source: `https://ewood.atlassian.net/spaces/work/pages/92110850`
    Updated in Confluence: `2026-04-20T19:33:35.743Z`

    - 📦 Где лежат файлыВсё храним в MEGA (облако). Готовый PlanSwift и прочие финальные файлы — только в облаке.👨‍💻(проверяющий)Открываю PlanSwift и Excel, проверяю, пишу ошибки в облаке (в соответствующей заметке/файле).Если есть ошибки — в Trello ставлю 🔴 красную метку, убираю 🟢 зелёную, снимаю даты.В Telegram пишу: номер дома + “нужно/не нужно править” (ВАЖНО!).Всегда указываю, где править Excel: [локальный] или [облачный]. Пишу, какие правки я уже сделал (в облаке).Если срочно — сам ставлю дедлайн и пишу: правим всё или отправляем как есть (в этом случае коротко описать, что сделано).👩‍🦰👨‍🔧 (работник)Открывает PlanSwift и начинает правки, параллельно задаёт вопросы.В Trello 🟡 жёлтую метку и примерную дату готовности.Excel править.После завершения правок: 🟢 зелёную метку.🔁 ИтерацииЦикл может повториться 2–3 раза до полного согласования.🗂️ Финальная выкладкаГотовый PlanSwift всегда в облаке (MEGA). Все файлы — в MEGA.⏳ Время на разбор ошибокПланируем на проверку и разбор 30–60 минут.🧪 Финальная проверка “было/стало” (чек-лист)Открыть готовый PlanSwift (с финальными правками от Артёма).Открыть ваш локальный Excel “до” (или из папки old, если есть).Открыть готовый Excel из Example.Сравнить Excel “было/стало”: оформление, что добавлено/удалено, формулировки.Сравнить PDF “было/стало”: оформление, что добавлено/удалено, формулировки.

<!-- confluence-context:end -->
