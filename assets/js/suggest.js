/* The corrections form on start/suggest-change: sends to the server, no account needed.
   The page address comes from the link "Предложить поправку" under any page. */
(function () {
  var ENDPOINT = "https://kb-fix.185.81.165.121.sslip.io/submit";

  function init() {
    var form = document.getElementById("kb-fix-form");
    if (!form) return;

    var status = document.getElementById("kb-fix-status");
    var button = form.querySelector("button");
    var page = new URLSearchParams(location.search).get("page") || "";

    if (page.indexOf("https://artrmiys.github.io/knowledge-base/") === 0) {
      form.elements.page.value = page;
      var label = document.getElementById("kb-fix-page");
      try {
        label.textContent = "Страница: " + decodeURI(new URL(page).pathname.replace("/knowledge-base/", ""));
      } catch (e) {
        label.textContent = "Страница: " + page;
      }
      label.hidden = false;
    }

    function say(text, isError) {
      status.textContent = text;
      status.className = isError ? "kb-form__status kb-form__status--error" : "kb-form__status";
    }

    form.addEventListener("submit", function (event) {
      event.preventDefault();
      button.disabled = true;
      say("Отправляю...", false);
      fetch(ENDPOINT, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          page: form.elements.page.value,
          what: form.elements.what.value,
          how: form.elements.how.value,
          name: form.elements.name.value,
          website: form.elements.website.value
        })
      })
        .then(function (response) {
          if (response.status === 429) throw new Error("Слишком много поправок подряд. Попробуйте через час.");
          if (!response.ok) throw new Error("Не отправилось. Текст остался в форме, попробуйте ещё раз позже.");
          form.elements.what.value = "";
          form.elements.how.value = "";
          say("Спасибо, поправка отправлена.", false);
        })
        .catch(function (err) {
          var known = err && /[а-я]/i.test(err.message);
          say(known ? err.message : "Нет связи с сервером. Текст остался в форме, попробуйте ещё раз позже.", true);
        })
        .finally(function () {
          button.disabled = false;
        });
    });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
