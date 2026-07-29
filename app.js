/* Rho · Panimávida v6 — interacciones y gráficos (foco: horas a $0 y precio máximo) */
(function () {
  "use strict";
  var D = window.RHO_DATA;
  var GREEN = "#30a46c", GREEND = "#218358", RED = "#e5484d", INK = "#1d1d1f", GRAY = "#86868b", GRAYL = "#c7c7cc";
  var YCOL = { 2023: "#9ed8a8", 2024: "#5cc16f", 2025: "#30a46c", 2026: "#0f6a32" };
  var FONT = "Inter, -apple-system, Segoe UI, sans-serif";

  /* ---------- NAV show on scroll ---------- */
  var nav = document.getElementById("nav");
  function onScroll() {
    if (window.scrollY > window.innerHeight * 0.7) nav.classList.add("show");
    else nav.classList.remove("show");
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* ---------- Hero blobs parallax ---------- */
  var blobs = document.querySelectorAll(".blob");
  window.addEventListener("mousemove", function (e) {
    var x = (e.clientX / window.innerWidth - 0.5), y = (e.clientY / window.innerHeight - 0.5);
    blobs.forEach(function (b, i) { var f = (i + 1) * 14; b.style.transform = "translate(" + (x * f) + "px," + (y * f) + "px)"; });
  });

  /* ---------- Reveal on scroll ---------- */
  var revObs = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("in"); revObs.unobserve(en.target); } });
  }, { threshold: 0.16 });
  document.querySelectorAll(".reveal").forEach(function (el) { revObs.observe(el); });

  /* ---------- Counters ---------- */
  function fmt(n) { return n.toLocaleString("es-CL"); }
  function animateCount(el) {
    var to = parseInt(el.getAttribute("data-to"), 10), dur = 1500, t0 = null;
    function step(ts) {
      if (!t0) t0 = ts;
      var p = Math.min((ts - t0) / dur, 1), eased = 1 - Math.pow(1 - p, 3);
      el.textContent = fmt(Math.round(to * eased));
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  var cntObs = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) { if (en.isIntersecting) { animateCount(en.target); cntObs.unobserve(en.target); } });
  }, { threshold: 0.5 });
  document.querySelectorAll(".cnt").forEach(function (el) { cntObs.observe(el); });

  /* ---------- ECharts ---------- */
  var charts = [];
  window.addEventListener("resize", function () { charts.forEach(function (c) { c.resize(); }); });
  function baseGrid() { return { left: 54, right: 28, top: 46, bottom: 46 }; }
  function axisCommon() {
    return { axisLine: { lineStyle: { color: "#e4e8e3" } }, axisTick: { show: false },
      axisLabel: { color: GRAY, fontFamily: FONT, fontSize: 12 }, splitLine: { lineStyle: { color: "#f0f3ef" } } };
  }

  /* Distribución: cuántas horas a $0 por día (2026) */
  function initCount() {
    var c = echarts.init(document.getElementById("chartCount"), null, { renderer: "canvas" });
    var dist = D.cargaCount.dist["2026"];
    var xs = []; for (var i = 0; i <= 10; i++) xs.push(i);
    var bars = dist.map(function (v, i) {
      return { value: v, itemStyle: { color: i >= 4 ? GREEN : "#d8d8dd", borderRadius: [6, 6, 0, 0] } };
    });
    c.setOption({
      grid: { left: 52, right: 24, top: 30, bottom: 54 },
      tooltip: { trigger: "axis", backgroundColor: "rgba(255,255,255,.96)", borderColor: "#e4e8e3", borderWidth: 1,
        textStyle: { color: INK, fontFamily: FONT }, formatter: function (p) { return "<b>" + p[0].axisValue + " h</b> a $0<br/>" + p[0].data.value + "% de los días"; } },
      xAxis: Object.assign({ type: "category", data: xs, name: "horas a $0 por día", nameLocation: "middle", nameGap: 32, nameTextStyle: { color: GRAY, fontFamily: FONT } },
        { axisLine: { lineStyle: { color: "#e4e8e3" } }, axisTick: { show: false }, axisLabel: { color: GRAY, fontFamily: FONT }, splitLine: { show: false } }),
      yAxis: Object.assign({ type: "value", axisLabel: { color: GRAY, fontFamily: FONT, formatter: "{value}%" }, min: 0 }, axisCommon()),
      series: [{ type: "bar", data: bars, barWidth: "62%",
        markLine: { symbol: "none", silent: true, data: [{ xAxis: 3.5 }], lineStyle: { color: INK, type: "dashed", width: 1.5 },
          label: { formatter: "4 h = carga completa", color: INK, fontFamily: FONT, fontSize: 12, position: "insideEndTop" } } }],
      animationDuration: 1400, animationEasing: "cubicOut"
    });
    charts.push(c);
  }

  /* Heatmap frecuencia de horas a $0 (año × hora) */
  function initHeat() {
    var c = echarts.init(document.getElementById("chartHeat"), null, { renderer: "canvas" });
    var hours = D.perfilCero.horas.map(function (h) { return h + "h"; });
    var years = D.anios.map(String);
    var data = D.heat;
    c.setOption({
      grid: { left: 64, right: 24, top: 18, bottom: 64 },
      tooltip: { backgroundColor: "rgba(255,255,255,.96)", borderColor: "#e4e8e3", borderWidth: 1, textStyle: { color: INK, fontFamily: FONT },
        formatter: function (p) { return years[p.value[1]] + " · " + hours[p.value[0]] + "<br/><b>" + Math.round(p.value[2]) + "% de horas a $0</b>"; } },
      xAxis: { type: "category", data: hours, splitArea: { show: false }, axisLabel: { color: GRAY, fontFamily: FONT, fontSize: 11, interval: 1 }, axisLine: { lineStyle: { color: "#e4e8e3" } }, axisTick: { show: false } },
      yAxis: { type: "category", data: years, splitArea: { show: false }, axisLabel: { color: INK, fontFamily: FONT, fontSize: 13, fontWeight: 600 }, axisLine: { lineStyle: { color: "#e4e8e3" } }, axisTick: { show: false } },
      visualMap: { min: 0, max: 85, calculable: true, orient: "horizontal", left: "center", bottom: 4,
        inRange: { color: ["#ffffff", "#bfe3cf", "#30a46c", "#147a3a"] },
        text: ["% horas a $0", ""], textStyle: { color: GRAY, fontFamily: FONT, fontSize: 11 }, itemWidth: 14, itemHeight: 110 },
      series: [{ name: "% a $0", type: "heatmap", data: data, label: { show: false }, progressive: 0,
        itemStyle: { borderColor: "#fff", borderWidth: 1.5 }, emphasis: { itemStyle: { shadowBlur: 10, shadowColor: "rgba(20,90,45,.4)" } } }],
      animationDuration: 1400
    });
    charts.push(c);
  }

  /* Costo medio de carga en ventana solar (09–17 h) vs ventana óptima (12–15 h) · línea PPA 28 */
  function initCargaCosto() {
    var c = echarts.init(document.getElementById("chartCargaCosto"), null, { renderer: "canvas" });
    var years = D.anios.map(String);
    var solarV = years.map(function (y) { return D.cargaSolar.solar[y]; });
    var chargeV = years.map(function (y) { return D.cargaSolar.carga[y]; });
    var pct0 = years.map(function (y) { return D.cargaSolar.pct0[y]; });
    var ppa = D.cargaSolar.ppa;
    c.setOption({
      grid: { left: 56, right: 28, top: 54, bottom: 46 },
      legend: { data: ["Horas de sol (09–17 h)", "Ventana óptima de carga (12–15 h)"], top: 6,
        textStyle: { color: GRAY, fontFamily: FONT, fontSize: 12 }, itemWidth: 14, itemHeight: 10, icon: "roundRect" },
      tooltip: { trigger: "axis", backgroundColor: "rgba(255,255,255,.96)", borderColor: "#e4e8e3", borderWidth: 1,
        textStyle: { color: INK, fontFamily: FONT },
        formatter: function (p) {
          var i = p[0].dataIndex;
          var s = "<b>" + p[0].axisValue + "</b><br/>";
          p.forEach(function (it) { s += it.marker + it.seriesName + ": <b>" + Math.round(it.data) + " USD/MWh</b><br/>"; });
          s += "<span style='color:#86868b'>" + pct0[i] + "% de las horas de sol a $0</span>";
          return s;
        } },
      xAxis: Object.assign({ type: "category", data: years,
        axisLabel: { color: INK, fontFamily: FONT, fontSize: 13, fontWeight: 600 } },
        { axisLine: { lineStyle: { color: "#e4e8e3" } }, axisTick: { show: false }, splitLine: { show: false } }),
      yAxis: Object.assign({ type: "value", name: "USD/MWh", nameTextStyle: { color: GRAY, fontFamily: FONT }, min: 0 }, axisCommon()),
      series: [
        { name: "Horas de sol (09–17 h)", type: "bar", data: solarV, barWidth: "26%",
          itemStyle: { color: "#5cc16f", borderRadius: [6, 6, 0, 0] },
          label: { show: true, position: "top", color: INK, fontFamily: FONT, fontSize: 12, fontWeight: 600, formatter: "{c}" },
          markLine: { symbol: "none", silent: true, data: [{ yAxis: ppa }],
            lineStyle: { color: RED, type: "dashed", width: 1.6 },
            label: { formatter: "PPA de compra · " + ppa + " USD/MWh", color: RED, fontFamily: FONT, fontSize: 12, position: "insideEndTop" } } },
        { name: "Ventana óptima de carga (12–15 h)", type: "bar", data: chargeV, barWidth: "26%",
          itemStyle: { color: GREEND, borderRadius: [6, 6, 0, 0] },
          label: { show: true, position: "top", color: GREEND, fontFamily: FONT, fontSize: 12, fontWeight: 600, formatter: "{c}" } }
      ],
      animationDuration: 1400, animationEasing: "cubicOut"
    });
    charts.push(c);
  }

  /* Venta: precio alto real (P90) por hora · 2026, pico 20–22 h */
  function initVenta() {
    var c = echarts.init(document.getElementById("chartVenta"), null, { renderer: "canvas" });
    var hours = D.ventaP90.horas.map(function (h) { return h + "h"; });
    c.setOption({
      grid: { left: 56, right: 28, top: 36, bottom: 48 },
      tooltip: { trigger: "axis", backgroundColor: "rgba(255,255,255,.96)", borderColor: "#e4e8e3", borderWidth: 1, textStyle: { color: INK, fontFamily: FONT }, valueFormatter: function (v) { return Math.round(v) + " USD/MWh"; } },
      xAxis: Object.assign({ type: "category", data: hours, boundaryGap: false, axisLabel: { color: GRAY, fontFamily: FONT, fontSize: 11, interval: 1 } },
        { axisLine: { lineStyle: { color: "#e4e8e3" } }, axisTick: { show: false }, splitLine: { show: false } }),
      yAxis: Object.assign({ type: "value", name: "USD/MWh", nameTextStyle: { color: GRAY, fontFamily: FONT }, min: 0 }, axisCommon()),
      series: [
        { name: "Precio del nodo por hora (P90)", type: "line", smooth: true, symbol: "none", data: D.ventaP90.series["2026"],
          lineStyle: { width: 3.4, color: RED },
          areaStyle: { color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{ offset: 0, color: "rgba(229,72,77,.16)" }, { offset: 1, color: "rgba(229,72,77,.01)" }]) },
          markArea: { silent: true, itemStyle: { color: "rgba(229,72,77,.10)" },
            data: [[{ xAxis: "19h", name: "Pico de venta · 20–22 h", label: { color: RED, fontFamily: FONT, fontSize: 11 } }, { xAxis: "22h" }]] } }
      ],
      animationDuration: 1500, animationEasing: "cubicOut"
    });
    charts.push(c);
  }

  /* Tendencia mensual */
  function initMensual() {
    var c = echarts.init(document.getElementById("chartMensual"), null, { renderer: "canvas" });
    c.setOption({
      grid: baseGrid(),
      tooltip: { trigger: "axis", backgroundColor: "rgba(255,255,255,.96)", borderColor: "#e4e8e3", borderWidth: 1, textStyle: { color: INK, fontFamily: FONT },
        formatter: function (p) { return "<b>" + p[0].axisValue + "</b><br/>" + Math.round(p[0].data) + " USD/MWh"; } },
      xAxis: Object.assign({ type: "category", data: D.mensual.labels, boundaryGap: false,
        axisLabel: { color: GRAY, fontFamily: FONT, fontSize: 12, interval: 0, formatter: function (v) { return v.indexOf("-01") === 4 ? v.slice(0, 4) : ""; } } },
        { axisLine: { lineStyle: { color: "#e4e8e3" } }, axisTick: { show: false }, splitLine: { show: false } }),
      yAxis: Object.assign({ type: "value", name: "USD/MWh", nameTextStyle: { color: GRAY, fontFamily: FONT }, min: 0 }, axisCommon()),
      series: [{ name: "CMg mensual", type: "line", data: D.mensual.vals, smooth: false, symbol: "none",
        lineStyle: { width: 3, color: GREEND },
        areaStyle: { color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{ offset: 0, color: "rgba(48,164,108,.30)" }, { offset: 1, color: "rgba(48,164,108,.02)" }]) } }],
      animationDuration: 1600, animationEasing: "cubicOut"
    });
    charts.push(c);
  }

  /* ═══════════ v8 · Ventana de arbitraje 2027–2035 ═══════════ */
  var vChart = null, vEsc = "B";
  var ESCCOL = { A: "#218358", B: "#30a46c", C: "#e5484d" };

  function ventanaOption() {
    var V = D.ventana, be = V.breakeven;
    var series = ["A", "B", "C"].map(function (k) {
      var on = k === vEsc;
      return {
        name: "Escenario " + k + " · " + V.esc[k].nombre,
        type: "line", data: V.esc[k].spread,
        smooth: false, symbol: "circle", symbolSize: on ? 7 : 0,
        z: on ? 5 : 2,
        lineStyle: { width: on ? 3.4 : 1.6, color: ESCCOL[k], opacity: on ? 1 : 0.3 },
        itemStyle: { color: ESCCOL[k], opacity: on ? 1 : 0.3 },
        areaStyle: on ? { color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
          { offset: 0, color: "rgba(48,164,108,.22)" }, { offset: 1, color: "rgba(48,164,108,.01)" }]) } : null,
        markLine: on ? {
          silent: true, symbol: "none",
          lineStyle: { color: RED, type: "dashed", width: 1.6 },
          label: { formatter: "break-even  " + String(be).replace(".", ",") + " USD/MWh",
                   color: RED, fontFamily: FONT, fontSize: 12, position: "insideEndTop" },
          data: [{ yAxis: be }]
        } : null
      };
    });
    return {
      grid: { left: 58, right: 30, top: 52, bottom: 46 },
      legend: { top: 8, icon: "roundRect", itemWidth: 12, itemHeight: 4,
                textStyle: { color: GRAY, fontFamily: FONT, fontSize: 12 } },
      tooltip: { trigger: "axis", backgroundColor: "rgba(255,255,255,.96)", borderColor: "#e4e8e3",
        borderWidth: 1, textStyle: { color: INK, fontFamily: FONT },
        formatter: function (ps) {
          var s = "<b>" + ps[0].axisValue + "</b><br/>";
          ps.forEach(function (p) {
            s += p.marker + " " + p.seriesName.split(" · ")[0] + ": <b>" +
                 String(p.data).replace(".", ",") + "</b> USD/MWh<br/>";
          });
          return s + '<span style="color:#e5484d">break-even ' +
                 String(D.ventana.breakeven).replace(".", ",") + "</span>";
        } },
      xAxis: Object.assign({ type: "category", data: D.ventana.anios, boundaryGap: false,
        axisLabel: { color: GRAY, fontFamily: FONT, fontSize: 12 } },
        { axisLine: { lineStyle: { color: "#e4e8e3" } }, axisTick: { show: false }, splitLine: { show: false } }),
      yAxis: Object.assign({ type: "value", name: "Spread · USD/MWh",
        nameTextStyle: { color: GRAY, fontFamily: FONT }, min: 0, max: 90 }, axisCommon()),
      series: series,
      animationDuration: 1100, animationEasing: "cubicOut"
    };
  }

  function paintVentana() {
    var V = D.ventana, e = V.esc[vEsc];
    var just = document.getElementById("escJust");
    if (just) just.textContent = e.just;
    var cr = document.getElementById("vCruce");
    if (cr) cr.textContent = e.cruce ? e.cruce : "no cruza al 2035";
    document.querySelectorAll(".esc-btn").forEach(function (b) {
      b.classList.toggle("is-on", b.getAttribute("data-esc") === vEsc);
      b.setAttribute("aria-pressed", b.getAttribute("data-esc") === vEsc ? "true" : "false");
    });
    if (vChart) vChart.setOption(ventanaOption(), true);
  }

  function initVentana() {
    var el = document.getElementById("chartVentana");
    if (!el || !D.ventana) return;
    vChart = echarts.init(el, null, { renderer: "canvas" });
    vChart.setOption(ventanaOption());
    charts.push(vChart);
    paintVentana();
  }

  document.querySelectorAll(".esc-btn").forEach(function (b) {
    b.addEventListener("click", function () {
      vEsc = b.getAttribute("data-esc");
      paintVentana();
    });
  });
  (function () {
    var m = document.getElementById("vMargen");
    if (m && D.ventana) m.textContent = Math.round(D.ventana.ancla.margen / 1000).toLocaleString("es-CL");
    var j = document.getElementById("escJust");
    if (j && D.ventana) j.textContent = D.ventana.esc[vEsc].just;
  })();

  var chartInit = { chartCount: initCount, chartCargaCosto: initCargaCosto, chartHeat: initHeat, chartVenta: initVenta, chartMensual: initMensual, chartVentana: initVentana };
  var done = {};
  var chartObs = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (en.isIntersecting && !done[en.target.id]) { done[en.target.id] = true; chartInit[en.target.id](); chartObs.unobserve(en.target); }
    });
  }, { threshold: 0.25 });
  Object.keys(chartInit).forEach(function (id) { var el = document.getElementById(id); if (el) chartObs.observe(el); });
})();
