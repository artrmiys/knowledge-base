# Приёмная поправок

Нашли ошибку, устаревшее правило или чего-то не хватает? Напишите здесь. Регистрация не нужна. Поправку читает только владелец сайта, он же решает, что внести.

К поправке можно приложить до 3 скриншотов: кнопкой, перетащив файл на форму или вставив снимок экрана через Ctrl+V. Большие картинки форма сама уменьшит перед отправкой.

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
  <div class="kb-form__shots">
    <p class="kb-form__label">Скриншоты (до 3, можно без них)</p>
    <label id="kb-fix-drop" class="kb-form__drop">
      <input type="file" name="shots" accept="image/png,image/jpeg,image/webp" multiple>
      <span>Выбрать файл, перетащить сюда или нажать Ctrl+V</span>
    </label>
    <div id="kb-fix-previews" class="kb-form__previews"></div>
  </div>
  <label class="kb-form__trap" aria-hidden="true">Не заполняйте
    <input type="text" name="website" tabindex="-1" autocomplete="off">
  </label>
  <button type="submit">Отправить</button>
  <p id="kb-fix-status" class="kb-form__status" role="status"></p>
</form>
