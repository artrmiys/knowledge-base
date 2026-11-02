# Приёмная поправок

Нашли ошибку, устаревшее правило или чего-то не хватает? Напишите здесь. Регистрация не нужна. Поправку читает только владелец сайта, он же решает, что внести.

<form id="kb-fix-form" class="kb-form">
  <p id="kb-fix-page" class="kb-form__page" hidden></p>
  <input type="hidden" name="page">
  <label>Что не так
    <textarea name="what" rows="5" maxlength="2000" required></textarea>
  </label>
  <label>Как должно быть (если знаете)
    <textarea name="how" rows="3" maxlength="2000"></textarea>
  </label>
  <label>Ваше имя (можно не писать)
    <input type="text" name="name" maxlength="80" autocomplete="name">
  </label>
  <label class="kb-form__trap" aria-hidden="true">Не заполняйте
    <input type="text" name="website" tabindex="-1" autocomplete="off">
  </label>
  <button type="submit">Отправить</button>
  <p id="kb-fix-status" class="kb-form__status" role="status"></p>
</form>
