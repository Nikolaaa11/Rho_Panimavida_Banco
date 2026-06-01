# Panimávida · Rho Generación — Modelo de arbitraje horario (v3.1)

🌐 **En vivo:** https://rho-panimavida-banco.vercel.app

Plataforma web interactiva que explica el modelo de **arbitraje horario** del proyecto Panimávida (solar + almacenamiento por batería) y por qué el financiamiento **no debe condicionarse** a la suscripción de un PPA de compra a **28 USD/MWh** en el nodo **Panimávida 13.2 kV**.

## El modelo

- **Banda solar (09–17 h):** el costo marginal del nodo cae a cero por saturación de la generación solar. El proyecto **carga su batería** con energía a costo cercano a cero.
- **Banda nocturna (19–07 h):** el precio del nodo se recompone. El proyecto **descarga y vende** al sistema.
- **Spread capturado en 2026:** 48 USD/MWh.

## Qué muestra el sitio

- El modelo de negocio en una vista (carga / descarga).
- Perfil intradiario del precio del nodo, año por año.
- Tendencia mensual 2022–2026.
- Mapa de calor del precio (verde por debajo de la oferta del PPA · ámbar/rojo por encima).
- Por qué un PPA a 28 USD/MWh rompe el modelo.
- Sensibilidad ante renegociación entre 22 y 34 USD/MWh.
- Recomendación al Comité de Crédito.
- Descargas: PDF ejecutivo (8 pp), Word editable, Excel con fórmulas en vivo (`Sobreprecio_PPA`, `Sensibilidad_PPA`).

## Datos

Costos marginales **reales** del nodo BA S/E Panimávida 13.2 kV BP1, publicados por el **Coordinador Eléctrico Nacional** (versión Real Definitivo). Período: 2022 — 2026 (38.064 horas reales). Generados en `data.js`.

## Stack

Sitio estático — `index.html` + `styles.css` + `app.js` + `data.js`. Gráficos con [ECharts](https://echarts.apache.org) (CDN). Sin build.

## Ejecutar localmente

```bash
python -m http.server 8080
# abrir http://localhost:8080
```

## Publicar

Auto-deploy desde Vercel sobre la rama `main`.
