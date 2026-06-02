# Panimávida · Rho Generación — Batería de arbitraje horario (v7.0)

🌐 **En vivo:** https://rho-panimavida-banco.vercel.app

Plataforma web interactiva del proyecto **Panimávida** — una batería (sistema de almacenamiento BESS de **9 MW / 36 MWh**) que **compra energía cuando el nodo vale $0 y la vende cuando alcanza su precio más alto**. Explica por qué el financiamiento **no debe condicionarse** a un PPA de compra a **28 USD/MWh** en el nodo **Panimávida 13.2 kV**.

## La idea

- **Cuántas horas a $0:** en 2026, de las 10 horas de sol (08–17 h), **6 están a costo $0**; el **72% de los días** tiene 4+ horas gratis — lo que la batería necesita para cargar.
- **Cuánto vale el pico:** entre las **20–22 h** el precio del nodo llega a **77 (2026) y 103 (2025) USD/MWh**, con máximos históricos sobre 270.
- **Cuánto cuesta cargar:** aun contando los días en que no vale $0, el costo medio en horas de sol es **15–36 USD/MWh** (11–32 en la franja óptima 12–15 h), bajo el pico y en línea con el PPA de 28.
- **Estrategia:** cargar 12–15 h (≈$0) y vender 20–22 h. Spread **62–77 USD/MWh**. Operación con un socio especialista (tipo Delfos Energy / Suncast) para el vector óptimo de carga/descarga.
- **Proyección (unit economics):** USD **1.900–3.260 por ciclo** (BESS 9 MW / 36 MWh, eficiencia 88%).

## Qué muestra el sitio

- Conteo de horas a $0 por día (distribución) y mapa de calor de frecuencia por año.
- Cuándo el precio es más alto: precio alto real (P90) por hora, con el pico 20–22 h.
- Estrategia de carga/descarga y proyección por ciclo.
- Por qué un PPA a 28 USD/MWh rompe el modelo, y recomendación al Comité de Crédito.
- Costo medio de carga en la ventana solar (09–17 h) vs. franja óptima (12–15 h), con la línea del PPA de compra.
- Descargas: resumen ejecutivo (1 p), informe completo (6 cap.) y Excel con la base de datos.

## Datos

Costos marginales **reales** del nodo BA S/E Panimávida 13.2 kV BP1, publicados por el **Coordinador Eléctrico Nacional** (versión Real Definitivo). Período: 2023 — 2026 (29.304 horas reales). Generados en `data.js`.

## Stack

Sitio estático — `index.html` + `styles.css` + `app.js` + `data.js`. Gráficos con [ECharts](https://echarts.apache.org) (CDN). Sin build.

## Ejecutar localmente

```bash
python -m http.server 8080
# abrir http://localhost:8080
```

## Publicar

Auto-deploy desde Vercel sobre la rama `main`.
