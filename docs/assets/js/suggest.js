/* The corrections form on start/suggest-change (and its English copy): sends to the server, no account needed.
   The page address comes from the link "Предложить поправку" / "Suggest a correction" under any page.
   Up to 3 screenshots: the button, drag and drop, or Ctrl+V anywhere on the page.
   Big pictures are shrunk in the browser to JPEG before sending. Messages follow the page language. */
(function () {
  var ENDPOINT = "https://kb-fix.185.81.165.121.sslip.io/submit";
  var MAX_SHOTS = 3;
  var MAX_SIDE = 2400;
  var KEEP_BYTES = 1.2 * 1024 * 1024; // a PNG or JPEG this small and not too large goes as is
  var MAX_DATA = 2.6 * 1024 * 1024; // data URL length that still fits the server limit of 2 MB

  var EN = (document.documentElement.lang || "").toLowerCase().indexOf("en") === 0;
  var T = EN ? {
    page: "Page: ",
    shot: "Screenshot ",
    remove: "Remove screenshot ",
    max: "You can attach up to " + MAX_SHOTS + " screenshots.",
    tookFirst: function (n) { return "Took the first " + n + ", no more than " + MAX_SHOTS + " allowed."; },
    big: "The picture is too large, take a smaller screenshot.",
    bad: "Could not open this picture. PNG, JPG and WebP work.",
    sendingShots: "Sending with screenshots...",
    sending: "Sending...",
    rate: "Too many corrections in a row. Try again in an hour.",
    images: "The screenshots were not accepted. Remove them or use smaller ones and send again.",
    what: "Write at least a few words in \"What is wrong\".",
    full: "The corrections storage is full. Please contact the site owner directly.",
    failed: "Not sent. Your text is still in the form, try again later.",
    thanks: "Thank you, the correction has been sent.",
    offline: "No connection to the server. Your text is still in the form, try again later."
  } : {
    page: "Страница: ",
    shot: "Скриншот ",
    remove: "Убрать скриншот ",
    max: "Можно приложить не больше " + MAX_SHOTS + " скриншотов.",
    tookFirst: function (n) { return "Взял первые " + n + ", больше " + MAX_SHOTS + " нельзя."; },
    big: "Картинка слишком большая, сделайте скриншот поменьше.",
    bad: "Эту картинку не получилось открыть. Подойдут PNG, JPG, WebP.",
    sendingShots: "Отправляю вместе со скриншотами...",
    sending: "Отправляю...",
    rate: "Слишком много поправок подряд. Попробуйте через час.",
    images: "Скриншоты не приняты. Уберите их или замените на поменьше и отправьте ещё раз.",
    what: "Напишите в поле \"Что не так\" хотя бы пару слов.",
    full: "Хранилище поправок переполнено. Напишите владельцу сайта напрямую.",
    failed: "Не отправилось. Текст остался в форме, попробуйте ещё раз позже.",
    thanks: "Спасибо, поправка отправлена.",
    offline: "Нет связи с сервером. Текст остался в форме, попробуйте ещё раз позже."
  };

  function readAsDataUrl(blob) {
    return new Promise(function (resolve, reject) {
      var reader = new FileReader();
      reader.onload = function () { resolve(reader.result); };
      reader.onerror = function () { reject(reader.error); };
      reader.readAsDataURL(blob);
    });
  }

  function loadImage(file) {
    return new Promise(function (resolve, reject) {
      var url = URL.createObjectURL(file);
      var img = new Image();
      img.onload = function () { URL.revokeObjectURL(url); resolve(img); };
      img.onerror = function () { URL.revokeObjectURL(url); reject(new Error("image")); };
      img.src = url;
    });
  }

  function toJpeg(img, side, quality) {
    var scale = Math.min(1, side / Math.max(img.naturalWidth, img.naturalHeight));
    var canvas = document.createElement("canvas");
    canvas.width = Math.max(1, Math.round(img.naturalWidth * scale));
    canvas.height = Math.max(1, Math.round(img.naturalHeight * scale));
    var ctx = canvas.getContext("2d");
    ctx.fillStyle = "#fff"; // transparent parts of a PNG would turn black in JPEG
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
    return canvas.toDataURL("image/jpeg", quality);
  }

  function prepare(file) {
    return loadImage(file).then(function (img) {
      var plain = file.type === "image/png" || file.type === "image/jpeg";
      var fits = Math.max(img.naturalWidth, img.naturalHeight) <= MAX_SIDE;
      if (plain && fits && file.size <= KEEP_BYTES) return readAsDataUrl(file);
      var data = toJpeg(img, MAX_SIDE, 0.88);
      if (data.length > MAX_DATA) data = toJpeg(img, 1600, 0.8);
      if (data.length > MAX_DATA) throw new Error("big");
      return data;
    });
  }

  function init() {
    var form = document.getElementById("kb-fix-form");
    if (!form) return;

    var status = document.getElementById("kb-fix-status");
    var button = form.querySelector('button[type="submit"]');
    var input = form.elements.shots;
    var previews = document.getElementById("kb-fix-previews");
    var drop = document.getElementById("kb-fix-drop");
    var page = new URLSearchParams(location.search).get("page") || "";
    var shots = []; // { data: "data:image/..." }
    var busy = 0;

    if (page.indexOf("https://artrmiys.github.io/knowledge-base/") === 0) {
      form.elements.page.value = page;
      var label = document.getElementById("kb-fix-page");
      try {
        label.textContent = T.page + decodeURI(new URL(page).pathname.replace("/knowledge-base/", ""));
      } catch (e) {
        label.textContent = T.page + page;
      }
      label.hidden = false;
    }

    function say(text, isError) {
      status.textContent = text;
      status.className = isError ? "kb-form__status kb-form__status--error" : "kb-form__status";
    }

    function render() {
      previews.textContent = "";
      shots.forEach(function (shot, i) {
        var item = document.createElement("div");
        item.className = "kb-form__shot";
        var img = document.createElement("img");
        img.src = shot.data;
        img.alt = T.shot + (i + 1);
        var remove = document.createElement("button");
        remove.type = "button";
        remove.className = "kb-form__shot-remove";
        remove.setAttribute("aria-label", T.remove + (i + 1));
        remove.textContent = "×";
        remove.addEventListener("click", function () {
          shots.splice(i, 1);
          render();
        });
        item.appendChild(img);
        item.appendChild(remove);
        previews.appendChild(item);
      });
      drop.hidden = shots.length >= MAX_SHOTS;
    }

    function add(files) {
      var images = Array.prototype.filter.call(files || [], function (f) {
        return f && /^image\//.test(f.type);
      });
      if (!images.length) return;
      var room = MAX_SHOTS - shots.length - busy;
      if (room <= 0) {
        say(T.max, true);
        return;
      }
      if (images.length > room) say(T.tookFirst(room), true);
      images.slice(0, room).forEach(function (file) {
        busy += 1;
        button.disabled = true;
        prepare(file)
          .then(function (data) {
            shots.push({ data: data });
            render();
          })
          .catch(function (err) {
            say(err && err.message === "big" ? T.big : T.bad, true);
          })
          .finally(function () {
            busy -= 1;
            if (!busy) button.disabled = false;
          });
      });
    }

    input.addEventListener("change", function () {
      add(input.files);
      input.value = "";
    });

    // Ctrl+V anywhere on the page: the screenshot goes into the form, text pastes as usual.
    document.addEventListener("paste", function (event) {
      var items = (event.clipboardData && event.clipboardData.items) || [];
      var files = [];
      for (var i = 0; i < items.length; i += 1) {
        if (items[i].kind === "file" && /^image\//.test(items[i].type)) files.push(items[i].getAsFile());
      }
      if (!files.length) return;
      event.preventDefault();
      add(files);
    });

    ["dragenter", "dragover"].forEach(function (name) {
      form.addEventListener(name, function (event) {
        if (!event.dataTransfer || Array.prototype.indexOf.call(event.dataTransfer.types, "Files") < 0) return;
        event.preventDefault();
        form.classList.add("kb-form--drag");
      });
    });
    ["dragleave", "drop"].forEach(function (name) {
      form.addEventListener(name, function () { form.classList.remove("kb-form--drag"); });
    });
    form.addEventListener("drop", function (event) {
      if (!event.dataTransfer || !event.dataTransfer.files.length) return;
      event.preventDefault();
      add(event.dataTransfer.files);
    });

    form.addEventListener("submit", function (event) {
      event.preventDefault();
      if (busy) return;
      button.disabled = true;
      say(shots.length ? T.sendingShots : T.sending, false);
      fetch(ENDPOINT, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          page: form.elements.page.value,
          what: form.elements.what.value,
          how: form.elements.how.value,
          name: form.elements.name.value,
          website: form.elements.website.value,
          images: shots.map(function (s) { return s.data; })
        })
      })
        .then(function (response) {
          if (response.ok) return response;
          return response.json().catch(function () { return {}; }).then(function (body) {
            var code = body && body.error;
            if (response.status === 429) throw new Error(T.rate);
            if (response.status === 413 || code === "image") throw new Error(T.images);
            if (code === "what") throw new Error(T.what);
            if (response.status === 507) throw new Error(T.full);
            throw new Error(T.failed);
          });
        })
        .then(function () {
          form.elements.what.value = "";
          form.elements.how.value = "";
          shots = [];
          render();
          say(T.thanks, false);
        })
        .catch(function (err) {
          var known = err && err.message && err.message !== "Failed to fetch" && err.name !== "TypeError";
          say(known ? err.message : T.offline, true);
        })
        .finally(function () {
          button.disabled = false;
        });
    });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
