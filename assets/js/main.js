(function () {
  var WA_NUMBER = "56997979827";
  var EMAIL = "fcalixto.abogado@gmail.com";
  var DEFAULT_MSG = "Hola, vengo desde la página web y me gustaría agendar una consulta con un abogado.";
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function $(sel, ctx) { return (ctx || document).querySelector(sel); }
  function $$(sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); }
  function waUrl(text) { return "https://wa.me/" + WA_NUMBER + "?text=" + encodeURIComponent(text); }

  // Medición de conversiones: si el sitio tiene Google Ads / GA4 (gtag) instalado,
  // cada clic en WhatsApp, llamada, correo o envío de formulario queda registrado.
  function track(action, label) {
    if (typeof window.gtag === "function") {
      window.gtag("event", action, { event_category: "contacto", event_label: label || "" });
    }
    if (Array.isArray(window.dataLayer)) {
      window.dataLayer.push({ event: action, contacto_origen: label || "" });
    }
  }

  // Enlaces de WhatsApp con mensaje prellenado (y materia, si corresponde)
  $$(".js-wa").forEach(function (a) {
    var area = a.getAttribute("data-area");
    var msg = area ? "Hola, vengo desde la página web y necesito asesoría en " + area + ". ¿Podemos agendar una consulta?" : DEFAULT_MSG;
    a.href = waUrl(msg);
    a.target = "_blank";
    a.rel = "noopener";
    a.addEventListener("click", function () { track("click_whatsapp", a.getAttribute("data-track")); });
  });
  $$(".js-call").forEach(function (a) {
    a.addEventListener("click", function () { track("click_llamada", a.getAttribute("data-track")); });
  });
  $$(".js-mail").forEach(function (a) {
    a.addEventListener("click", function () { track("click_correo", a.getAttribute("data-track")); });
  });

  // Formularios: validan y arman el mensaje para WhatsApp o correo
  function readForm(form) {
    var data = {};
    new FormData(form).forEach(function (v, k) { data[k] = String(v).trim(); });
    return data;
  }
  function validate(form) {
    var ok = true;
    $$("[required]", form).forEach(function (el) {
      var bad = !el.value.trim();
      el.classList.remove("err");
      if (bad) { void el.offsetWidth; el.classList.add("err"); }
      if (bad && ok) { el.focus(); ok = false; }
    });
    return ok;
  }
  function compose(d) {
    var lines = ["Hola, quiero agendar una consulta (enviado desde la web)."];
    if (d.nombre) lines.push("Nombre: " + d.nombre);
    if (d.telefono) lines.push("Teléfono: " + d.telefono);
    if (d.email) lines.push("Correo: " + d.email);
    if (d.area) lines.push("Materia: " + d.area);
    if (d.modalidad) lines.push("Modalidad: " + d.modalidad);
    if (d.mensaje) lines.push("Caso: " + d.mensaje);
    return lines.join("\n");
  }
  $$(".js-form [required]").forEach(function (el) {
    el.addEventListener("input", function () { el.classList.remove("err"); });
    el.addEventListener("change", function () { el.classList.remove("err"); });
  });
  $$(".js-form").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!validate(form)) return;
      track("envio_formulario", form.id + "-whatsapp");
      window.open(waUrl(compose(readForm(form))), "_blank", "noopener");
      var ok = $(".form-ok", form);
      if (ok) { ok.hidden = false; }
    });
  });
  $$(".js-form-mail").forEach(function (a) {
    a.addEventListener("click", function (e) {
      e.preventDefault();
      var form = document.getElementById(a.getAttribute("data-form"));
      if (!form || !validate(form)) return;
      var d = readForm(form);
      track("envio_formulario", form.id + "-correo");
      window.location.href = "mailto:" + EMAIL + "?subject=" + encodeURIComponent("Solicitud de consulta - " + (d.area || "Web")) + "&body=" + encodeURIComponent(compose(d));
    });
  });

  // Menú móvil
  var toggle = $(".menu-toggle");
  var nav = $("#nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open);
      document.body.classList.toggle("menu-open", open);
    });
    $$("a", nav).forEach(function (a) {
      a.addEventListener("click", function () {
        nav.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
        document.body.classList.remove("menu-open");
      });
    });
  }

  // Submenú de servicios: accesible con teclado y táctil
  $$(".has-sub").forEach(function (item) {
    var btn = $(".sub-toggle", item);
    if (!btn) return;
    btn.addEventListener("click", function (e) {
      e.preventDefault();
      var open = item.classList.toggle("open");
      btn.setAttribute("aria-expanded", open);
    });
    document.addEventListener("click", function (e) {
      if (!item.contains(e.target)) { item.classList.remove("open"); btn.setAttribute("aria-expanded", "false"); }
    });
  });

  // Palabras rotativas (título del hero y barra superior)
  function rotate(nodes, every) {
    if (nodes.length < 2 || reduceMotion) return;
    var i = 0;
    setInterval(function () {
      var cur = nodes[i];
      cur.classList.remove("on"); cur.classList.add("out");
      i = (i + 1) % nodes.length;
      nodes[i].classList.remove("out");
      void nodes[i].offsetWidth;
      nodes[i].classList.add("on");
      setTimeout(function () { cur.classList.remove("out"); }, 650);
    }, every);
  }
  rotate($$(".rotator > span"), 2600);

  // Horario de atención (hora de Chile)
  var open = null;
  try {
    var parts = new Intl.DateTimeFormat("en-US", { timeZone: "America/Santiago", weekday: "short", hour: "2-digit", minute: "2-digit", hour12: false }).formatToParts(new Date());
    var get = function (t) { return (parts.find(function (p) { return p.type === t; }) || {}).value; };
    var day = get("weekday"), mins = (parseInt(get("hour"), 10) % 24) * 60 + parseInt(get("minute"), 10);
    var weekday = ["Mon", "Tue", "Wed", "Thu", "Fri"].indexOf(day) !== -1;
    open = weekday && ((mins >= 540 && mins < 780) || (mins >= 900 && mins < 1110));
  } catch (e) {}
  if (open !== null) {
    $$(".open-now").forEach(function (badge) {
      badge.textContent = open ? "Abierto ahora" : "Cerrado ahora";
      badge.classList.add(open ? "yes" : "no");
      badge.hidden = false;
    });
    var tkStatus = $("#tk-status");
    if (tkStatus && !open) {
      tkStatus.innerHTML = '<i class="live-dot off"></i> Fuera de horario · <b>escríbenos y te contactamos</b>';
    }
  }
  rotate($$(".ticker > *"), 4000);

  // Franja de urgencia: se puede cerrar (se recuerda durante la visita)
  var alertBar = $("#alert-bar");
  if (alertBar) {
    try { if (sessionStorage.getItem("alertClosed") === "1") alertBar.classList.add("hide"); } catch (e) {}
    var closeBtn = $(".close", alertBar);
    if (closeBtn) closeBtn.addEventListener("click", function () {
      alertBar.classList.add("hide");
      try { sessionStorage.setItem("alertClosed", "1"); } catch (e) {}
    });
  }

  // Animaciones al hacer scroll
  var items = $$(".reveal");
  if ("IntersectionObserver" in window && !reduceMotion) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); } });
    }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add("in"); });
  }

  // Brillo que sigue al cursor en las tarjetas
  $$(".service, .post").forEach(function (card) {
    card.addEventListener("pointermove", function (e) {
      var r = card.getBoundingClientRect();
      card.style.setProperty("--mx", (e.clientX - r.left) + "px");
      card.style.setProperty("--my", (e.clientY - r.top) + "px");
    });
  });

  // Cifras que cuentan hacia arriba al aparecer
  var counters = $$(".count[data-to]");
  if (counters.length && "IntersectionObserver" in window && !reduceMotion) {
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        cio.unobserve(en.target);
        var el = en.target, raw = el.getAttribute("data-to"), dec = raw.indexOf(",") > -1 ? 1 : 0;
        var to = parseFloat(raw.replace(",", ".")), prefix = el.textContent.trim().charAt(0) === "+" ? "+" : "";
        var t0 = null;
        function step(ts) {
          if (!t0) t0 = ts;
          var k = Math.min(1, (ts - t0) / 1400), v = to * (1 - Math.pow(1 - k, 3));
          el.textContent = prefix + v.toFixed(dec).replace(".", ",");
          if (k < 1) requestAnimationFrame(step);
        }
        requestAnimationFrame(step);
      });
    }, { threshold: 0.5 });
    counters.forEach(function (el) { cio.observe(el); });
  }

  // Header compacto, barra de progreso, botón "arriba" y barra móvil
  var header = $(".header");
  var progress = $(".progress");
  var toTop = $(".to-top");
  var mobileBar = $(".mobile-bar");
  var ticking = false;
  function onScroll() {
    var y = window.scrollY;
    var max = document.documentElement.scrollHeight - innerHeight;
    if (header) header.classList.toggle("scrolled", y > 20);
    if (progress) progress.style.transform = "scaleX(" + (max > 0 ? y / max : 0) + ")";
    if (toTop) toTop.classList.toggle("show", y > 700);
    if (mobileBar) mobileBar.classList.toggle("show", y > 200);
    ticking = false;
  }
  window.addEventListener("scroll", function () { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
  onScroll();
  if (toTop) toTop.addEventListener("click", function () { window.scrollTo({ top: 0, behavior: reduceMotion ? "auto" : "smooth" }); });

  // Mensaje del botón flotante de WhatsApp a los pocos segundos
  var waFloat = $(".wa-float");
  if (waFloat) setTimeout(function () {
    waFloat.classList.add("peek");
    setTimeout(function () { waFloat.classList.remove("peek"); }, 5000);
  }, 6000);

  // Rendimiento: pausa las animaciones de las secciones que no se ven en pantalla
  if ("IntersectionObserver" in window) {
    var animIo = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { en.target.classList.toggle("anim-off", !en.isIntersecting); });
    });
    $$(".hero, .page-hero, .final-cta, .quote-band, .marquee, .call-mock, .alert-bar").forEach(function (el) { animIo.observe(el); });
  }

  $$(".js-year").forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
