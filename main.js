/* =========================================================
   Dr. Nazif Mahbub — Portfolio interactions
   ========================================================= */
(function () {
  "use strict";

  /* ---- mobile nav ---- */
  var toggle = document.querySelector(".nav-toggle");
  var links = document.querySelector(".nav-links");
  if (toggle && links) {
    toggle.addEventListener("click", function () {
      var open = links.classList.toggle("open");
      toggle.classList.toggle("open", open);
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    links.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () {
        links.classList.remove("open");
        toggle.classList.remove("open");
      });
    });
  }

  /* ---- nav scrolled state ---- */
  var nav = document.querySelector(".nav");
  if (nav) {
    var onScroll = function () { nav.classList.toggle("scrolled", window.scrollY > 12); };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /* ---- scroll reveal ---- */
  var reveals = document.querySelectorAll("[data-reveal]");
  if ("IntersectionObserver" in window && reveals.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -8% 0px" });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("in"); });
  }

  /* ---- animated stat counters ---- */
  var counted = false;
  var statsEl = document.querySelector(".stats");
  function runCounters() {
    if (counted || !statsEl) return;
    counted = true;
    document.querySelectorAll(".num[data-count]").forEach(function (el) {
      var target = parseFloat(el.getAttribute("data-count"));
      var suffix = el.getAttribute("data-suffix") || "";
      var prefix = el.getAttribute("data-prefix") || "";
      var dur = 1400, start = null;
      el.innerHTML = prefix + "0<span>" + suffix + "</span>";
      function step(ts) {
        if (!start) start = ts;
        var p = Math.min((ts - start) / dur, 1);
        var eased = 1 - Math.pow(1 - p, 3);
        var val = Math.floor(eased * target);
        el.innerHTML = prefix + val.toLocaleString() + "<span>" + suffix + "</span>";
        if (p < 1) requestAnimationFrame(step);
      }
      requestAnimationFrame(step);
    });
  }
  if (statsEl && "IntersectionObserver" in window) {
    var sio = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { runCounters(); sio.disconnect(); } });
    }, { threshold: 0.4 });
    sio.observe(statsEl);
  } else { runCounters(); }

  /* ---- contact form ---- */
  var form = document.getElementById("contactForm");
  if (form) {
    var status = document.getElementById("formStatus");
    var btn = form.querySelector("button[type=submit]");
    var RECIPIENT = "dr.nazif.mahbub@gmail.com";

    function show(type, msg) {
      status.className = "form-status show " + type;
      status.textContent = msg;
    }

    form.addEventListener("submit", function (ev) {
      ev.preventDefault();
      var data = {
        name: form.name.value.trim(),
        email: form.email.value.trim(),
        subject: form.subject ? form.subject.value.trim() : "",
        message: form.message.value.trim()
      };
      if (!data.name || !data.email || !data.message) {
        show("err", "Please fill in your name, email, and message.");
        return;
      }

      var action = form.getAttribute("action") || "";
      var usingFormspree = action.indexOf("formspree.io/f/") !== -1 &&
                           action.indexOf("YOUR_FORM_ID") === -1;

      if (usingFormspree) {
        btn.disabled = true;
        var original = btn.textContent;
        btn.textContent = "Sending…";
        var body = new FormData(form);
        fetch(action, { method: "POST", body: body, headers: { Accept: "application/json" } })
          .then(function (r) {
            if (r.ok) {
              form.reset();
              show("ok", "Thank you — your message has been sent. Dr. Nazif will be in touch soon.");
            } else {
              return r.json().then(function (d) {
                throw new Error((d && d.error) || "Submission failed");
              });
            }
          })
          .catch(function () {
            show("err", "Something went wrong. Please email dr.nazif.mahbub@gmail.com directly.");
          })
          .finally(function () { btn.disabled = false; btn.textContent = original; });
      } else {
        /* zero-setup fallback: open the visitor's mail client, pre-filled */
        var subject = data.subject || ("Portfolio enquiry from " + data.name);
        var lines = [
          "Name: " + data.name,
          "Email: " + data.email,
          data.subject ? "Subject: " + data.subject : "",
          "",
          data.message
        ].filter(Boolean).join("\n");
        var href = "mailto:" + RECIPIENT +
          "?subject=" + encodeURIComponent(subject) +
          "&body=" + encodeURIComponent(lines);
        window.location.href = href;
        show("ok", "Opening your email app to send the message to Dr. Nazif. If nothing happens, email " + RECIPIENT + " directly.");
      }
    });
  }

  /* ---- footer year ---- */
  var yr = document.getElementById("year");
  if (yr) yr.textContent = new Date().getFullYear();
})();
