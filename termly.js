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

  function syncConsent(data) {
    if (data.categories && data.categories.includes("analytics")) {
      localStorage.setItem("kosli_consent", "accepted");
    } else {
      localStorage.removeItem("kosli_consent");
    }
  }

  // Called when the Termly script finishes loading.
  window.onTermlyLoaded = function () {
    if (window.Termly && window.Termly.on) {
      Termly.on("consent", syncConsent);
    }
  };

  function init() {
    if (!document.getElementById("kosli-termly-embed")) {
      const s = document.createElement("script");
      s.id = "kosli-termly-embed";
      s.src = "https://app.termly.io/resource-blocker/c98bfcd6-2f30-4f3c-b53c-d6dbd9b8c40c?autoBlock=on";
      s.setAttribute("data-master-consents-origin", "https://www.kosli.com");
      s.setAttribute("onload", "onTermlyLoaded()");
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

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init, { once: true });
  } else {
    init();
  }
})();
