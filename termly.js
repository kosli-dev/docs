// Termly cookie consent banner + cross-subdomain consent sync from www.kosli.com.
// Mintlify auto-includes any .js file at the content root on every page,
// so this loads on every doc page on docs.kosli.com.
//
// Companion config: docs.json `integrations.cookies` gates Mintlify's own
// telemetry on the `kosli_consent` localStorage flag we set below.

(function () {
  if (window.__kosliTermlyLoaded) return;
  window.__kosliTermlyLoaded = true;

  window.TERMLY_CUSTOM_BLOCKING_MAP = {
    "kosli.com": "essential",
    "unpkg.com": "essential",
    "youtube.com": "essential"
  };

  function init() {
    if (!document.getElementById("kosli-termly-embed")) {
      const s = document.createElement("script");
      s.id = "kosli-termly-embed";
      s.src = "https://app.termly.io/embed.min.js";
      s.setAttribute("data-auto-block", "on");
      s.setAttribute("data-website-uuid", "c98bfcd6-2f30-4f3c-b53c-d6dbd9b8c40c");
      s.setAttribute("data-master-consents-origin", "https://www.kosli.com");
      document.head.appendChild(s);
    }

    if (!document.getElementById("kosli-consent-sync")) {
      const f = document.createElement("iframe");
      f.id = "kosli-consent-sync";
      f.src = "https://www.kosli.com/consent-sync.html";
      f.title = "consent sync";
      f.setAttribute("aria-hidden", "true");
      f.style.display = "none";
      (document.body || document.documentElement).appendChild(f);
    }
  }

  window.addEventListener("termly.consent", function (e) {
    const analytics = e && e.detail && e.detail.analytics;
    if (analytics) {
      localStorage.setItem("kosli_consent", "accepted");
    } else {
      localStorage.removeItem("kosli_consent");
    }
  });

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init, { once: true });
  } else {
    init();
  }
})();
