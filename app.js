/* Rho · Panimávida — interacciones y gráficos */
(function () {
  "use strict";
  var D = window.RHO_DATA;
  var GREEN = "#1f9d4d", GREEND = "#147a3a", AMBER = "#ff7a1a", INK = "#1d1d1f", GRAY = "#86868b";
  var YCOL = { 2022: "#c4ccc3", 2023: "#9ed8a8", 2024: "#5cc16f", 2025: "#1f9d4d", 2026: "#0f6a32" };
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
    var x = (e.clientX / window.innerWidth - 0.5);
    var y = (e.clientY / window.innerHeight - 0.5);
    blobs.forEach(function (b, i) {
      var f = (i + 1) * 14;
      b.style.transform = "translate(" + (x * f) + "px," + (y * f) + "px)";
    });
  });

  /* ---------- Reveal on scroll ---------- */
  var revObs = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (en.isIntersecting) { en.target.classList.add("in"); revObs.unobserve(en.target); }
    });
  }, { threshold: 0.16 });
  document.querySelectorAll(".reveal").forEach(function (el) { revObs.observe(el); });

  /* ---------- Counters ---------- */
  function fmt(n) { return n.toLocaleString("es-CL"); }
  function animateCount(el) {
    var to = parseInt(el.getAttribute("data-to"), 10);
    var dur = 1500, t0 = null;
    function step(ts) {
      if (!t0) t0 = ts;
      var p = Math.min((ts - t0) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = fmt(Math.round(to * eased));
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  var cntObs = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (en.isIntersecting) { animateCount(en.target); cntObs.unobserve(en.target); }
    });
  }, { threshold: 0.5 });
  document.querySelectorAll(".cnt").forEach(function (el) { cntObs.observe(el); });

  /* ---------- Progress dots ---------- */
  var ids = ["hero", "cifras", "tendencia", "estructural", "logica", "horizonte", "propuesta"];
  var dots = document.getElementById("dots");
  ids.forEach(function (id) {
    var b = document.createElement("button");
    b.title = id;
    b.addEventListener("click", function () {
      var t = document.getElementById(id);
      if (t) t.scrollIntoView({ behavior: "smooth" });
    });
    dots.appendChild(b);
  });
  var dotEls = dots.querySelectorAll("button");
  var secObs = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (en.isIntersecting) {
        var i = ids.indexOf(en.target.id);
        dotEls.forEach(function (d, k) { d.classList.toggle("active", k === i); });
      }
    });
  }, { threshold: 0.5 });
  ids.forEach(function (id) { var s = document.getElementById(id); if (s) secObs.observe(s); });

  /* ---------- ECharts: lazy init on reveal ---------- */
  var charts = [];
  window.addEventListener("resize", function () { charts.forEach(function (c) { c.resize(); }); });

  function baseGrid() { return { left: 54, right: 28, top: 54, bottom: 46 }; }
  function axisCommon() {
    return {
      axisLine: { lineStyle: { color: "#e4e8e3" } },
      axisTick: { show: false },
      axisLabel: { color: GRAY, fontFamily: FONT, fontSize: 12 },
      splitLine: { lineStyle: { color: "#f0f3ef" } }
    };
  }

  function initMensual() {
    var el = document.getElementById("chartMensual");
    var c = echarts.init(el, null, { renderer: "canvas" });
    var labels = D.mensual.labels;
    c.setOption({
      grid: baseGrid(),
      tooltip: {
        trigger: "axis", backgroundColor: "rgba(255,255,255,.96)", borderColor: "#e4e8e3",
        textStyle: { color: INK, fontFamily: FONT }, borderWidth: 1,
        formatter: function (p) {
          var d = p[0];
          return "<b>" + d.axisValue + "</b><br/>" + Math.round(d.data) + " USD/MWh";
        }
      },
      xAxis: Object.assign({
        type: "category", data: labels, boundaryGap: false,
        axisLabel: { color: GRAY, fontFamily: FONT, fontSize: 12, interval: 0,
          formatter: function (v) { return v.slice(5) === "01" || v.indexOf("-01") === 4 ? v.slice(0, 4) : ""; } }
      }, { axisLine: { lineStyle: { color: "#e4e8e3" } }, axisTick: { show: false }, splitLine: { show: false } }),
      yAxis: Object.assign({ type: "value", name: "USD/MWh", nameTextStyle: { color: GRAY, fontFamily: FONT }, min: 0 }, axisCommon()),
      series: [{
        name: "CMg mensual", type: "line", data: D.mensual.vals, smooth: false, symbol: "none",
        lineStyle: { width: 3, color: GREEND },
        areaStyle: { color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
          { offset: 0, color: "rgba(31,157,77,.30)" }, { offset: 1, color: "rgba(31,157,77,.02)" }]) },
        markLine: {
          symbol: "none", silent: true,
          data: [{ yAxis: D.oferta }],
          lineStyle: { color: AMBER, type: "dashed", width: 2 },
          label: { formatter: "Oferta PPA · 28 USD/MWh", color: AMBER, fontFamily: FONT, fontSize: 12, position: "insideEndTop" }
        }
      }],
      animationDuration: 1600, animationEasing: "cubicOut"
    });
    charts.push(c);
  }

  function initCero() {
    var el = document.getElementById("chartCero");
    var c = echarts.init(el, null, { renderer: "canvas" });
    var hours = D.perfilCero.horas.map(function (h) { return h + "h"; });
    var series = D.anios.map(function (y, idx) {
      return {
        name: String(y), type: "line", smooth: true, symbol: "none",
        data: D.perfilCero.series[y],
        lineStyle: { width: y >= 2024 ? 3 : 2, color: YCOL[y] },
        emphasis: { focus: "series" },
        markArea: idx === 0 ? {
          silent: true, itemStyle: { color: "rgba(124,195,107,.12)" },
          data: [[{ xAxis: "9h", name: "Horas solares", label: { color: GREEND, fontFamily: FONT, fontSize: 11 } }, { xAxis: "17h" }]]
        } : undefined
      };
    });
    c.setOption({
      grid: { left: 54, right: 28, top: 46, bottom: 70 },
      color: D.anios.map(function (y) { return YCOL[y]; }),
      legend: { bottom: 6, textStyle: { color: GRAY, fontFamily: FONT }, icon: "roundRect" },
      tooltip: {
        trigger: "axis", backgroundColor: "rgba(255,255,255,.96)", borderColor: "#e4e8e3", borderWidth: 1,
        textStyle: { color: INK, fontFamily: FONT },
        valueFormatter: function (v) { return v + "%"; }
      },
      xAxis: Object.assign({ type: "category", data: hours, boundaryGap: false,
        axisLabel: { color: GRAY, fontFamily: FONT, fontSize: 11, interval: 1 } },
        { axisLine: { lineStyle: { color: "#e4e8e3" } }, axisTick: { show: false }, splitLine: { show: false } }),
      yAxis: Object.assign({ type: "value", name: "% horas en 0", nameTextStyle: { color: GRAY, fontFamily: FONT }, min: 0, max: 100,
        axisLabel: { color: GRAY, fontFamily: FONT, formatter: "{value}%" } }, axisCommon()),
      series: series,
      animationDuration: 1600, animationEasing: "cubicOut"
    });
    charts.push(c);
  }

  function initHeat() {
    var el = document.getElementById("chartHeat");
    var c = echarts.init(el, null, { renderer: "canvas" });
    var hours = D.perfilCero.horas.map(function (h) { return h + "h"; });
    var years = D.anios.map(String);
    c.setOption({
      grid: { left: 64, right: 24, top: 18, bottom: 64 },
      tooltip: {
        backgroundColor: "rgba(255,255,255,.96)", borderColor: "#e4e8e3", borderWidth: 1,
        textStyle: { color: INK, fontFamily: FONT },
        formatter: function (p) {
          return years[p.value[1]] + " · " + hours[p.value[0]] + "<br/><b>" + p.value[2] + "%</b> de horas en 0 USD/MWh";
        }
      },
      xAxis: { type: "category", data: hours, splitArea: { show: false },
        axisLabel: { color: GRAY, fontFamily: FONT, fontSize: 11, interval: 1 },
        axisLine: { lineStyle: { color: "#e4e8e3" } }, axisTick: { show: false } },
      yAxis: { type: "category", data: years, splitArea: { show: false },
        axisLabel: { color: INK, fontFamily: FONT, fontSize: 13, fontWeight: 600 },
        axisLine: { lineStyle: { color: "#e4e8e3" } }, axisTick: { show: false } },
      visualMap: {
        min: 0, max: 100, calculable: true, orient: "horizontal", left: "center", bottom: 6,
        inRange: { color: ["#eef6ee", "#a8e0b3", "#34c759", "#147a3a", "#0c4f25"] },
        textStyle: { color: GRAY, fontFamily: FONT }, text: ["100%", "0%"]
      },
      series: [{
        name: "% horas en 0", type: "heatmap", data: D.heat,
        label: { show: false }, progressive: 0,
        itemStyle: { borderColor: "#fff", borderWidth: 1.5 },
        emphasis: { itemStyle: { shadowBlur: 10, shadowColor: "rgba(20,90,45,.4)" } }
      }],
      animationDuration: 1400
    });
    charts.push(c);
  }

  var chartInit = {
    chartMensual: initMensual,
    chartCero: initCero,
    chartHeat: initHeat
  };
  var done = {};
  var chartObs = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (en.isIntersecting && !done[en.target.id]) {
        done[en.target.id] = true;
        chartInit[en.target.id]();
        chartObs.unobserve(en.target);
      }
    });
  }, { threshold: 0.25 });
  Object.keys(chartInit).forEach(function (id) {
    var el = document.getElementById(id); if (el) chartObs.observe(el);
  });
})();
