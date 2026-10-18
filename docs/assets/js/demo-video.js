/* Demo clips of OurPlanCore: a clip plays only while it is on screen, so a page
   with a dozen clips does not download and decode them all at once. Click
   pauses or resumes a clip, double click opens it full screen. Without JS the
   poster frame stays visible. */
(function () {
  function init() {
    var clips = document.querySelectorAll("video.kb-demo");
    if (!clips.length) return;

    clips.forEach(function (v) {
      v.addEventListener("click", function () {
        v.dataset.userPaused = v.paused ? "" : "1";
        if (v.paused) v.play().catch(function () {});
        else v.pause();
      });
      v.addEventListener("dblclick", function () {
        if (document.fullscreenElement) {
          document.exitFullscreen();
        } else if (v.requestFullscreen) {
          v.dataset.userPaused = "";
          v.play().catch(function () {});
          v.requestFullscreen().catch(function () {});
        }
      });
    });

    if (!("IntersectionObserver" in window)) {
      clips.forEach(function (v) {
        v.play().catch(function () {});
      });
      return;
    }

    var seen = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (e) {
          var v = e.target;
          if (e.isIntersecting && !v.dataset.userPaused) {
            v.play().catch(function () {});
          } else if (!e.isIntersecting && !v.paused) {
            v.pause();
          }
        });
      },
      { threshold: 0.4 }
    );
    clips.forEach(function (v) {
      seen.observe(v);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
