# HANDOFF — Proyecto Panimávida 13.2 kV (análisis de crédito para banco)

> Documento de traspaso para retomar el proyecto en otro equipo / sesión de Claude Code.
> Última actualización: **2026-06-02** · versión vigente: **v6.1**.
> Si lo quieres auto-cargado por Claude Code, renómbralo a `CLAUDE.md` en la raíz de trabajo.

---

## 1. Qué es el proyecto (en una frase)

Material para el **Comité de Crédito de un banco** que justifica financiar el proyecto **Panimávida 13.2 kV** —una **batería / BESS de 9 MW / 36 MWh**— cuyo negocio es **arbitraje horario**: comprar energía del nodo cuando vale **$0** (mediodía) y venderla en el **precio máximo** (pico nocturno 20–22 h), sin necesidad de firmar un PPA de compra a 28 USD/MWh.

Cliente/marca: **Rho Generación · Cehta Capital**. Contacto interno del audio original: "Nico" (Nicolas Rietta). Destinatario: "Banco — Martín / Comité de Crédito".

---

## 2. ⚠️ REGLAS DE ORO (no romper)

1. **Es una batería (BESS), NO una planta solar/fotovoltaica.** Prohibido escribir "fotovoltaico", "generación solar", "generación propia", "posición vendedora", "cobertura natural", "planta de generación". El proyecto compra del nodo; no genera. El costo $0 del mediodía se explica por **"saturación de generación renovable zonal"** (de terceros), nunca por generación del proyecto.
2. **NO usar promedios como mensaje.** Prohibida la palabra "promedio/promedios" en textos, gráficos y archivos. El caso se cuenta con **conteos** (cuántas horas valen $0) y **máximos** (precio del pico), no con medias. El jefe fue explícito: *"si muestro los promedios nos vamos a la chucha"*.
3. **Diseño estilo Apple**, fondo blanco, tarjetas redondeadas, tipografía limpia (Segoe UI), mucho espacio en blanco. Que "no parezca hecho por IA".
4. **Lenguaje transversal**: cada párrafo debe servir a la vez al técnico, al de inversiones y al director — un solo párrafo por idea, sin secciones por cargo.

---

## 3. Datos clave (fuente: Coordinador Eléctrico Nacional, Real Definitivo)

- Período: **2022-01-01 a 2026-05-22 = 38.064 horas reales**. Nodo BA S/E Panimávida 13.2 kV (BP1). 2026 es parcial (hasta 22-may).
- BESS: **9 MW / 36 MWh** (4 h de duración), **eficiencia 88%** → 31,7 MWh entregados por ciclo.
- **Horas a $0 (carga), ventana solar 08–17 h:** en 2026, **6 de 10 horas/día** a costo $0; **72% de los días** con ≥4 h gratis (suficiente para una carga). Mejor franja: **12–15 h**.
- **Precio de venta (pico 20–22 h):** 2026 ≈ **77**, 2025 ≈ **103** USD/MWh; máximos históricos > 270. P90 del pico 2026 ≈ 124.
- **Spread del arbitraje:** **62–77 USD/MWh** (estable desde 2024).
- **Unit economics por ciclo** (compra→venta): Conservador **USD 1.899** (15→77), Base **2.100** (20→89), Óptimo carga $0 **3.263** (0→103). Margen 60–103 USD/MWh.
- NO firmar PPA de compra a 28 USD/MWh: fijaría la carga (hoy ≈$0) muy por encima del spot y deterioraría DSCR/LLCR.

Horas en cero/día promedio por año (banda 08–17): 2022=4.3, 2023=6.5, 2024=7.6, 2025=5.4, 2026=6.0. % días ≥4h: 47/71/84/61/72.

---

## 4. Carpetas y archivos

### 4.1 Carpeta de trabajo (este equipo)
`C:\Users\DELL\Documents\0.2 rho\costo marginal panimavida\`

| Archivo | Qué es |
|---|---|
| `WhatsApp Ptt 2026-06-01 at 19.33.44.ogg` | Audio original del jefe (el brief). |
| `2024.xlsx`, `2024-07-15.xlsx`, `2025.xlsx`, `2026.xlsx` | Data cruda de CMg por hora (col `PANIMAVIDA____013`). |
| `Panimavida_Datos_Banco_v2.xlsx` | Workbook base con hoja `Datos_CMg` (38.064 filas) — **fuente para todos los cálculos**. |
| `Panimavida_Informe_Banco_v6.docx` / `.pdf` | **Informe vigente** (5 capítulos). |
| `Panimavida_Resumen_Ejecutivo_v6.docx` / `.pdf` | **Ejecutivo vigente** (1 página). |
| `Panimavida Datos Banco.xlsx` | Workbook de datos v6 (renombrado por el usuario). |
| `Correo_Banco_Panimavida_v6.docx` | Correo para el banco (versión estratégica, adjuntos). |
| `v6_carga.png, v6_freq.png, v6_kpis.png, v6_venta.png, v6_tabla.png` | Gráficos v6 (los del informe/ejecutivo). |
| `v5_estrategia.png, v5_proyeccion.png, v5_tabla_unit.png, v5_reco.png` | Assets reutilizados en v6. |
| `_backup_originales/` | Originales intactos (con fotovoltaico) por si hay que comparar. |
| Versiones viejas v2/v4/v5 | Históricas; **la vigente es v6/v6.1**. |

### 4.2 Plataforma web (repo Git)
- **GitHub:** https://github.com/Nikolaaa11/Rho_Panimavida_Banco (rama `main`)
- **En vivo:** https://rho-panimavida-banco.vercel.app (auto-deploy de Vercel desde `main`)
- Clonada en este equipo en `C:\Users\DELL\Documents\0.2 rho\Rho_Panimavida_Banco\`
- Sitio **estático** (sin build): `index.html` + `styles.css` + `app.js` + `data.js`, gráficos con **ECharts 5.5.1** (CDN). Carpeta `downloads/` con los 3 archivos v6. `assets/` con el logo Rho.

---

## 5. Cómo regenerar cada cosa (recetas)

Entorno de este equipo (Windows + PowerShell): Python 3.13 con `pandas, numpy, matplotlib, python-docx, openpyxl, pywin32 (win32com), fitz (pymupdf)`. **MS Word y Excel instalados** (se usan vía COM). `git` (credencial `store` con GitHub) y `vercel` CLI (logueado como `nicolasrietta-1798`). Setear `$env:PYTHONUTF8=1` antes de correr Python por los acentos. Matar procesos colgados antes de COM: `Get-Process WINWORD,EXCEL | Stop-Process -Force`.

### Sistema de diseño (matplotlib, estilo Apple)
- Fuente: `Segoe UI`. Colores: ink `#1d1d1f`, gris `#6e6e73`, hairline `#e6e6ea`, **verde $0 `#30a46c`/`#218358`**, **rojo precio máximo `#e5484d`**.
- Tarjetas: `FancyBboxPatch` con `boxstyle="round,...,rounding_size=0.18"`, fondo blanco, borde hairline, sombra suave (3 rects desplazados con alpha 0.05/0.04/0.03).
- Charts: sin spines top/right, grid horizontal `#e6e6ea`, fondo blanco, líneas `solid_capstyle='round'`.

### Gráficos v6
- **v6_carga** = "6 de 10" + histograma de horas a $0/día (verde si ≥4, gris si <4) con línea "4 h = carga completa".
- **v6_freq** = % de días con $0 por hora (área verde), pico al mediodía.
- **v6_venta** = P90 del precio por hora (rojo, con área), zona 19–22 h sombreada, anotación "pico ~77–103". **Sin** línea de promedio.
- **v6_kpis** = 4 tarjetas: "6 de 10 horas $0", "103 precio máximo", "62–77 spread", "1.900–3.260 USD/ciclo".
- **v6_tabla** = tarjeta-tabla por año (horas $0/día, %días≥4h, precio pico, precio máximo).
- Cálculos desde `Panimavida_Datos_Banco_v2.xlsx` hoja `Datos_CMg`: `cero = (CMg==0)`, ventana solar `range(8,18)`, pico `[20,21,22]`, P90 con `np.percentile(...,90)`.

### Informe / Ejecutivo (Word → PDF)
- Construidos con `python-docx` (estilo Normal = Segoe UI 10.5; títulos grandes; capítulos con eyebrow "CAPÍTULO N" verde). Imágenes insertadas a ancho de contenido (en el ejecutivo, los charts altos a 0.80×ancho para que quepa en 1 página).
- DOCX→PDF con **Word COM**: `win32com ... Documents.Open(...).ExportAsFixedFormat(OutputFileName, ExportFormat=17)`. Reintentar si COM da "llamada rechazada" (instancia ocupada): hasta 6 intentos con `sleep 3` y matar WINWORD antes.
- Estructura del informe v6 (5 cap.): 1 Resumen ejecutivo · 2 Cuántas horas vale $0 · 3 Cuándo el precio es más alto · 4 Estrategia + proyección · 5 Riesgos y recomendación.

### Workbook (editar SIEMPRE con Excel COM, NO openpyxl)
openpyxl **borra los gráficos** al guardar. Usar `win32com Excel.Application`, `ws.Cells.Replace(...)`, `wb.Save()`. Cabeceras de marca: relleno verde `1A4A1A` (BGR) texto blanco; o estilo limpio: sin relleno, negrita, borde inferior verde. Ocultar cuadrículas: `excel.ActiveWindow.DisplayGridlines=False` por hoja.

### Plataforma (deploy)
1. Editar `index.html` / `app.js` / `data.js` / `styles.css` y/o `downloads/`.
2. `git -C <repo> add -A; git commit -m "..."; git push origin main` (con `$env:GIT_TERMINAL_PROMPT=0`).
3. Vercel **auto-despliega** desde `main` en ~20–60 s. Verificar: `curl https://rho-panimavida-banco.vercel.app/?cb=RANDOM | grep -i promedi` (debe dar 0) o comprobar "Versión 6.0".
4. `data.js` = `window.RHO_DATA = {...}` (JSON); tiene `cargaCount` (mean/pct4/dist por año), `ventaP90`, `peak`, `unit`, `bess`, además de `perfilPrecio/perfilCero/heat/mensual/sens`. Los charts (chartCount, chartHeat, chartVenta, chartMensual) se inicializan lazy al hacer scroll (IntersectionObserver).

---

## 6. Correo para el banco

- **Word:** `Correo_Banco_Panimavida_v6.docx`. Borrador en Gmail (cuenta autenticada): el válido es el último creado (los anteriores se pueden borrar).
- **Asunto:** "Panimávida 13.2 kV — Ingresos por arbitraje horario y servicio de la deuda".
- Mensaje estratégico: abre con "de dónde provienen los ingresos que respaldan el servicio de la deuda" → 3 bullets (carga gratis / venta en el pico / spread estable) → recomendación (no PPA) → adjuntos → 1 línea de plataforma.
- **Antes de enviar:** (1) agregar correos del banco; (2) **adjuntar los 3 archivos** (el conector Gmail no adjunta binarios automáticamente): `Panimavida_Resumen_Ejecutivo_v6.pdf`, `Panimavida_Informe_Banco_v6.pdf`, y el Excel de datos v6.
- La plataforma se menciona SOLO como lugar para visualizar los cambios.

---

## 7. Historial de versiones

- **v2/v3.2** (original): framing solar+BESS, con fotovoltaico y promedios. (En `_backup_originales/`.)
- **v4.0**: se quitó "fotovoltaico" → BESS de arbitraje; informe reestructurado (12 secciones); se integraron tablas horarias al Excel.
- **v5.0**: rediseño estilo Apple (tarjetas redondeadas), 5 capítulos, lenguaje transversal, proyección unit economics.
- **v6.0**: corrección de fondo tras re-escuchar el audio → el protagonista pasa a ser el **conteo de horas a $0** y el **precio máximo** (antes el hero era un promedio). Plataforma actualizada y deployada.
- **v6.1** (vigente): se eliminó **toda** mención a "promedios" en correo, plataforma y archivos. Verificado 0 ocurrencias en producción y en los PDFs/Excel.

---

## 8. Pendientes / notas

- Recipientes del banco y adjuntos físicos del correo: los pone el usuario.
- Hay borradores de Gmail antiguos (versiones previas del correo) que conviene eliminar.
- Las credenciales (GitHub, Vercel, Gmail) son de este equipo; en el equipo del trabajo habrá que autenticar git (`store`/PAT), `vercel login` y el conector de Gmail de Claude.
- Si se recalcula con data nueva del Coordinador, actualizar `Panimavida_Datos_Banco_v2.xlsx`/`Datos_CMg` y regenerar charts → docs → `data.js` → push.

---

## 9. Prompt sugerido para arrancar en el otro equipo

> "Lee HANDOFF.md. Vamos a seguir con el proyecto Panimávida (BESS de arbitraje para el banco). Respeta las reglas de oro: es una batería (no solar/fotovoltaico), nunca usar promedios como mensaje (usar conteos y máximos), diseño Apple. La versión vigente es v6.1; la plataforma es el repo Rho_Panimavida_Banco con auto-deploy en Vercel."
