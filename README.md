# Panimávida · Rho Generación — Plataforma de análisis para el banco (v2.0)

🌐 **En vivo:** https://rho-panimavida-banco.vercel.app

Plataforma web interactiva que explica por qué **no es la alternativa económicamente óptima** suscribir hoy la oferta de PPA de compra a **28 USD/MWh** en el nodo **Panimávida 13.2 kV**, fundamentado en datos reales del Coordinador Eléctrico Nacional.

## Qué muestra

- **El dilema en números**: oferta 28 USD/MWh vs. costo spot del nodo ~0 USD/MWh en horas solares.
- **Tendencia**: costo marginal promedio mensual 2022–2026 vs. la oferta.
- **El patrón estructural**: % de horas en 0 USD/MWh por hora del día + mapa de calor año × hora.
- **La lógica económica**: comparación firmar hoy vs. abastecerse a spot.
- **Horizonte**: por qué evaluar la firma recién hacia 2030.
- **La propuesta** final.
- **Descargas v2**: PDF ejecutivo + Word editable + Excel con fórmulas en vivo (`Ahorro_vs_PPA`).

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
