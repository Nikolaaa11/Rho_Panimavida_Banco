# Panimávida · Rho Generación — Plataforma de análisis para el banco

Plataforma web interactiva que explica por qué **Rho no firma hoy** la oferta de PPA de compra a **28 USD/MWh** en el nodo **Panimávida 13.2 kV**, fundamentado en datos reales del mercado eléctrico.

## Qué muestra

- **El dilema en números**: oferta 28 USD/MWh vs. costo spot del nodo ~0 USD/MWh.
- **Tendencia**: costo marginal promedio mensual 2022–2026 vs. la oferta.
- **El patrón estructural**: % de horas en 0 USD/MWh por hora del día + mapa de calor año × hora.
- **La lógica económica**: comparación firmar hoy vs. abastecerse a spot.
- **Horizonte**: por qué evaluar la firma recién hacia 2030.
- **La propuesta** final.

## Datos

Costos marginales **reales** del nodo BA S/E Panimávida 13.2 kV BP1, **Coordinador Eléctrico Nacional**.
Período: 2022 — 22 may 2026 (38.064 horas). Generados en `data.js`.

## Stack

Sitio estático — `index.html` + `styles.css` + `app.js` + `data.js`. Gráficos con [ECharts](https://echarts.apache.org) (CDN). Sin build.

## Ejecutar localmente

```bash
python -m http.server 8080
# abrir http://localhost:8080
```

## Publicar (GitHub Pages)

Settings → Pages → Branch: `main` / `/ (root)` → Save.
