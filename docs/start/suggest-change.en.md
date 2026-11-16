# Suggest a correction

Found a mistake, an outdated rule, or something missing? Write it here. No account needed. Only the site owner reads the corrections and decides what goes in.

You can attach up to 3 screenshots: with the button, by dragging a file onto the form, or by pasting a screen capture with Ctrl+V. The form shrinks large pictures before sending.

<form id="kb-fix-form" class="kb-form">
  <p id="kb-fix-page" class="kb-form__page" hidden></p>
  <input type="hidden" name="page">
  <label>What is wrong
    <textarea name="what" rows="5" maxlength="2000" required></textarea>
  </label>
  <label>How it should be (if you know)
    <textarea name="how" rows="3" maxlength="2000"></textarea>
  </label>
  <label>Your name (optional)
    <input type="text" name="name" maxlength="80" autocomplete="name">
  </label>
  <div class="kb-form__shots">
    <p class="kb-form__label">Screenshots (up to 3, optional)</p>
    <label id="kb-fix-drop" class="kb-form__drop">
      <input type="file" name="shots" accept="image/png,image/jpeg,image/webp" multiple>
      <span>Choose a file, drag it here, or press Ctrl+V</span>
    </label>
    <div id="kb-fix-previews" class="kb-form__previews"></div>
  </div>
  <label class="kb-form__trap" aria-hidden="true">Do not fill in
    <input type="text" name="website" tabindex="-1" autocomplete="off">
  </label>
  <button type="submit">Send</button>
  <p id="kb-fix-status" class="kb-form__status" role="status"></p>
</form>
