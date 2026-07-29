# HANDOFF — Panimávida 13,2 kV · para seguir trabajando desde cualquier equipo

> **Versión vigente: v8.2** · 29-jul-2026 · reunión con el banco: 30-jul-2026 AM
> Este documento es autosuficiente: con esto y la carpeta del proyecto se puede
> reconstruir o modificar cualquier entregable sin depender de la sesión anterior.

---

## ⚡ ARRANQUE EN DOS MINUTOS

```bash
# 1. Instalar dependencias (una sola vez)
pip install pandas numpy openpyxl python-docx reportlab matplotlib pymupdf faster-whisper

# 2. Verificar que todo corre
cd "Banco_Panimavida/_scripts_v8"
python 01_analisis_base.py        # recalcula desde las 38.064 horas
python 04_build_excel_ventana.py  # regenera la calculadora
python 05_verify_excel.py         # VERIFICA que las fórmulas den los números correctos
```

Si los tres corren, el entorno está listo. Todo lo demás son variaciones.

**Regla que no se rompe:** después de tocar cualquier fórmula del Excel, correr
`05_verify_excel.py`. openpyxl **escribe** fórmulas pero **no las evalúa** — sin ese
paso no hay forma de saber si el libro calcula bien. En esta sesión ese verificador
encontró un bug real que habría llegado al banco (§9).

---

## 1. Qué es el proyecto

**Panimávida 13,2 kV** es una batería (BESS) de **9 MW / 36 MWh** en la Región del
Maule, Chile. No genera: **compra energía del nodo cuando el costo marginal cae cerca
de cero al mediodía y la vende en el pico de la noche.** El material es para el
**Comité de Crédito de un banco**.

Cliente: **RHO Generación · FIP CEHTA Capital**. Interlocutor interno: Nicolás Rietta.
Quien lleva la reunión con el banco: **Javier**.

### Dónde está parado el expediente

La **v7** (junio) respondía una pregunta: *¿conviene el PPA de compra a 28 USD/MWh?*
Respuesta: no. Eso está ganado y no se toca.

La **v8** responde tres frentes nuevos que aparecieron en el directorio del banco:

1. **Objeción de transmisión.** Un director que entiende de mercado eléctrico sostiene
   que la línea HVDC Kimal–Lo Aguirre hundirá el precio de venta nocturno.
2. **Pedido de rigor.** Otro asesor pide *"ver números y respaldo"* — y criticó que el
   material anterior *"es muy del pasado y del presente, no habla del futuro"*.
3. **Horizonte y contratación.** Mostrar que conviene marginal al menos hasta 2030–2032,
   y un plan de contratación desde el primer año de operación.

---

## 2. EL HALLAZGO CENTRAL — leer antes de tocar nada

Recalculado sobre las 38.064 horas crudas, medido en **ventanas de 12 meses completos**
(el año calendario no sirve: mezcla estacionalidad y 2026 está incompleto):

| Ventana | Carga | Venta | Spread |
|---|---|---|---|
| 23-may-2022 → 22-may-2023 | 37,7 | 200,0 | 162,3 |
| 23-may-2023 → 22-may-2024 | 12,3 | 108,2 | 96,0 |
| 23-may-2024 → 22-may-2025 | 10,1 | 98,2 | 88,1 |
| **23-may-2025 → 22-may-2026** ← **ANCLA** | **22,1** | **99,6** | **77,5** |

> **El precio de venta nocturno NO viene cayendo: está plano en 98–100 USD/MWh desde
> hace tres años. Lo que se movió, y explica casi toda la compresión reciente del
> spread, es el COSTO DE CARGA (10,1 → 22,1).**

**Por qué esto da vuelta la objeción:** el director teme que Kimal–Lo Aguirre baje el
precio de **venta**. Los datos dicen que la venta no viene cayendo. Y esa línea
transporta excedente **solar, que es diurno**: actúa sobre el costo marginal del **día**
—el lado de la **carga**— y lo empuja **a la baja**. **La línea que se teme es viento de
cola para el riesgo real del proyecto, no viento de frente.**

Y el asesor técnico tiene razón en lo que importa: su punto —que el riesgo es el alza
del costo de carga cuando baje el vertimiento— es exactamente lo que muestran los datos.
El material le da la razón a él y usa su razonamiento para responder al director.

¿La carga tiene tendencia o es hidrología? Oscila entre 8,1 y 45,0 sin tendencia
monótona: 8,1 (2024) → 24,0 (2025) → 9,6 (ene–may 2026). El alza de 2025 es consistente
con mayor hidrología y **ya revirtió**. Se trata como riesgo estructural de largo plazo,
no como tendencia instalada.

---

## 3. ⚠️ CUATRO CORRECCIONES DE HECHOS — no romperlas

Estas cuatro cosas se afirmaban (o se iban a afirmar) y **no resisten verificación**.
Si alguien en la mesa tiene los reportes del Coordinador, desarma el expediente completo.

**1. NO decir que el precio de venta "nunca bajó de 50 USD/MWh".**
Era un artefacto de filtrar solo ene–may. Lo verificado sobre el registro completo:

| Umbral | Días bajo | % del registro | % en o sobre |
|---|---|---|---|
| < 40 | 4 | 0,3% | 99,7% |
| **< 50** | **12** | **0,8%** | **99,2%** |
| < 55 | 30 | 1,9% | 98,1% |
| < 60 | 87 | 5,5% | 94,5% |

Mínimo absoluto: **0,0 USD/MWh el 30-oct-2022** (día atípico). En la ventana ancla el
peor día fue **48,8** y el P10 fue **58,5**.
**Formulación correcta:** *"el 99,2% de los 1.586 días estuvo en o sobre 50 USD/MWh"*.

**2. NO decir que el pipeline de BESS "no es tangible".**
A nivel nacional es falso: **2.283 MW en operación** (mar-2026), proyección de **5.081 MW**
a dic-2026, **6.358 MW en construcción** (74 proyectos), y Chile superó los 2 GW en enero
de 2026 **cuatro años antes de lo previsto**. Va más rápido, no más lento.
**La brecha real es LOCACIONAL y es un argumento más fuerte:** Antofagasta 44%, Atacama
23%, Tarapacá 13,6%, RM 5% — **el Maule no figura**. ~86% está en el norte. Y la CNE
proyecta que el desacople del sur **persiste hacia 2032**.

**3. NO prometer "el PPA firmado el 2032".**
No existe mercado de PPA ni tolling de almacenamiento a escala PMG (<10 MW) en Chile.
Los contratos verificados son de cientos de MW con contrapartes investment grade.
**Hablar de instrumentos de venta alternativos:** agregador o portafolio de
comercialización, floor o collar nocturno, tolling con un actor mayor, precio
estabilizado.

**4. RIESGO REGULATORIO SIN RESOLVER.** Bajo **DS 1/2026**, incorporar almacenamiento a
un PMGD que ya optó por precio estabilizado se considera **"modificación"** y **puede
hacer perder el precio estabilizado** (vigente hasta jul-2034 solo para quien no
modifique). **Consultar al abogado regulatorio antes del Comité.**

---

## 4. CIFRAS CANÓNICAS — fuente única de verdad

Si un número no está acá, no se publica. Si aparece otro distinto en un documento viejo,
gana este cuadro.

| Concepto | Valor | Nota |
|---|---|---|
| Base de datos | 38.064 horas · 1.586 días | 2022-01-01 a 2026-05-22 |
| **Ancla de mercado** | carga **22,1** · venta **99,6** · spread **77,5** | últimos 12 meses completos |
| **Margen bruto titular** | **US$ 814.738/año** | día a día, 340 ciclos |
| Margen ciclando todos los días | US$ 810.174 | 359 ciclos — casi idéntico |
| Margen a 182 ciclos | US$ 524.363 | plan conservador |
| **Break-even de spread** | **43,9 USD/MWh** | 340 ciclos, servicio US$400 mil |
| Costo del PPA de compra | **US$ 96.557/año** (11,9%) | US$966 mil en 10 años |
| Margen con PPA a 28 | US$ 718.181 | con su política óptima (365 ciclos) |
| P10 de venta, ventana ancla | 58,5 · peor día 48,8 | |
| P10 de spread, ventana ancla | 29,2 · 88% de días > 40 | |
| Escenario base cruza break-even | **2034** | A: no cruza · C: 2029 |

**Unificación importante:** el expediente tenía dos números en conflicto —**US$493 mil**
(informe v7: precio-nivel × volumen, 182 ciclos) y **≈US$0,9 M** (correo enviado). Ambos
correctos bajo su propio método. La v8 adopta **US$815 mil** y **declara la diferencia**
antes de que la encuentren.

---

## 5. MAPA DE ARCHIVOS

Todo bajo `OneDrive/Documentos/0.2.Rho/Banco_Panimavida/`

```
PROMPT_MAESTRO_v8.md            ← documento de encuadre. Leer primero
HANDOFF_CASA_v8.md              ← este archivo
FUENTES_v8_transmision.md       ← Kimal–Lo Aguirre, topología, PET, con URLs
FUENTES_v8_bess_mercado.md      ← pipeline BESS, Ley 21.505, contratos, con URLs

_scripts_v8/                    ← TODO lo que regenera los entregables
  01_analisis_base.py             recalcula desde las horas crudas → daily_panimavida.csv
  02_analisis_estacionalidad.py   estacionalidad, tendencia, piso, break-even
  03_ppa_vs_spot.py               el cuadro con PPA vs sin PPA
  04_build_excel_ventana.py       genera la calculadora (10 hojas)
  05_verify_excel.py              ⚠ VERIFICA las fórmulas con LibreOffice
  06_build_brochure_pdf.py        brochure PDF, 4 páginas
  07_build_brochure_word.py       brochure Word editable
  08_transcribir_audios.py        transcribe audios con faster-whisper
  _patch_rutas.py                 ya corrido; deja las rutas relativas
  datos/
    FUENTE_Panimavida_Utilidades_BESS.xlsx   ← LA FUENTE (hoja Datos_CMg)
    daily_panimavida.csv                      serie diaria derivada
    ppa_vs_spot.json                          cifras del cuadro PPA
    bro_chart.png                             gráfico de escenarios
    transcripciones/                          los 3 audios del 29-jul

entrega_banco_v8/               ← entregables vigentes
  Panimavida_Ventana_Arbitraje_v8.xlsx      la calculadora
  Panimavida_Brochure_v8.pdf                brochure 4 páginas
  Panimavida_Brochure_v8_EDITABLE.docx      brochure Word
  Correo_Javier_v8.txt                      el correo

PARA_ENVIAR_Javier_reunion_30-07-2026/   ← carpeta lista para adjuntar
  LEEME.txt + 7 archivos numerados

Rho_Panimavida_Banco/           ← repo Git de la plataforma
  index.html · glosario.html · app.js · data.js · styles.css
  downloads/ · assets/ · HANDOFF.md
```

**Entregables v7 (base documental, siguen válidos):** `entrega_banco_v7/` con el informe
de 6 capítulos, el resumen ejecutivo y la memoria de utilidades.

---

## 6. ENTORNO

```bash
pip install pandas numpy openpyxl python-docx reportlab matplotlib pymupdf faster-whisper
```

| Herramienta | Para qué | Nota |
|---|---|---|
| **Python 3.12+** | todo | `export PYTHONUTF8=1` **siempre** (acentos) |
| **LibreOffice** | verificar fórmulas y convertir a PDF | `C:\Program Files\LibreOffice\program\soffice.exe` |
| **git** | desplegar la plataforma | credencial `store` o PAT de GitHub |
| MS Excel / Word | opcional, solo si se edita un libro **existente** con gráficos | vía `pywin32` COM |
| Fuentes Segoe UI | brochure PDF y Word | ya vienen en Windows |

En Linux o Mac hay que ajustar en `06_build_brochure_pdf.py` la ruta `FD` de las fuentes
y en `05_verify_excel.py` la ruta `SOF` de LibreOffice.

---

## 7. RECETAS

### Recalcular con datos nuevos del Coordinador
La base termina el **22-may-2026**; faltan ~2 meses.
1. Descargar las horas nuevas y pegarlas en la hoja `Datos_CMg` de
   `_scripts_v8/datos/FUENTE_Panimavida_Utilidades_BESS.xlsx`.
2. `python 01_analisis_base.py` → regenera `daily_panimavida.csv`.
3. `python 02_analisis_estacionalidad.py` y `03_ppa_vs_spot.py` → cifras nuevas.
4. Actualizar a mano las constantes en `04_build_excel_ventana.py` (bloque `sup`, ancla)
   y en `data.js` (bloque `window.RHO_DATA.ventana`).
5. `python 04_build_excel_ventana.py && python 05_verify_excel.py`.
6. Regenerar brochures y desplegar.

### Cargar los términos de deuda (lo que falta)
Abrir `Panimavida_Ventana_Arbitraje_v8.xlsx`, hoja **Panel**, celdas azules: CAPEX,
deuda/CAPEX, tasa, plazo, DSCR mínimo. Y en **Supuestos**: OPEX y reserva de degradación.
El DSCR y el gatillo 6 se calculan solos. **No hay que tocar código.**

### Cambiar los escenarios
Hoja **Escenarios**, celdas azules: año de inicio de compresión, Δ venta y Δ carga por
año. Todo lo demás recalcula. En la plataforma, editar `esc` en `data.js`.

### Regenerar los brochures
```bash
python 07_build_brochure_word.py   # Word (genera el gráfico si falta)
python 06_build_brochure_pdf.py    # PDF 4 páginas
```
Para revisar visualmente antes de entregar:
```python
import fitz
d = fitz.open('.../Panimavida_Brochure_v8.pdf')
for i, p in enumerate(d): p.get_pixmap(dpi=105).save(f'p{i+1}.png')
```

### Transcribir audios nuevos
Editar la lista `FILES` en `08_transcribir_audios.py` y correrlo. Tiene escalera de
degradación automática (`small` → `base`) por si falta memoria.

---

## 8. DESPLEGAR LA PLATAFORMA

```bash
cd Banco_Panimavida/Rho_Panimavida_Banco
git add -A
git commit -m "..."
GIT_TERMINAL_PROMPT=0 git push origin main
```

Vercel **auto-despliega desde `main`** en 20–60 s. Las dos URLs son alias del mismo
proyecto y sirven lo mismo:
- https://rho-panimavida-banco-qdfj.vercel.app
- https://rho-panimavida-banco.vercel.app

Verificar en vivo:
```bash
curl -s "https://rho-panimavida-banco-qdfj.vercel.app/?cb=$RANDOM" | grep -c 'id="ventana"'
curl -s "https://rho-panimavida-banco-qdfj.vercel.app/?cb=$RANDOM" | grep -oic 'promedi'  # debe dar 0
```

**Estructura del sitio:** estático, sin build. `index.html` + `glosario.html` +
`styles.css` + `app.js` + `data.js`, gráficos con ECharts 5.5.1 por CDN. Los charts se
inicializan con `IntersectionObserver` al hacer scroll (`chartInit` al final de `app.js`).

---

## 9. TRAMPAS DESCUBIERTAS — esto ahorra horas

**1. openpyxl escribe fórmulas pero NO las evalúa.**
Un libro puede verse perfecto y estar mal. **Siempre** correr `05_verify_excel.py`, que
lo recalcula con LibreOffice headless y lee los valores resultantes.
*En esta sesión encontró un bug real:* las celdas puente al Panel (`ws['C8']`)
**sobrescribían celdas de datos** de la tabla de break-even, dejando 41,2 donde debía ir
58,1. La solución fue construir el Panel al final del script y apuntar a las direcciones
reales, más un `assert` que falla si la dirección cambia.

**2. openpyxl BORRA los gráficos** al guardar un libro existente que los tenga. Para
libros **nuevos** es seguro; para editar uno **existente con gráficos**, usar Excel COM.

**3. Fórmulas matriciales: evitarlas.** Un `MATCH(TRUE, rango<valor, 0)` exige
Ctrl+Shift+Enter y se rompe silenciosamente. Se reemplazó por **tres filas auxiliares
visibles** (año / spread del escenario activo / flag 1-0) y un `MATCH(1, flags, 0)`. Más
robusto y además el banco ve el cálculo.

**4. Rutas de Windows dentro de heredocs de bash rompen Python.** Un `r'C:\Users\...'`
dentro de `<< 'EOF'` da `SyntaxError: truncated \UXXXXXXXX escape`. Escribir el script a
archivo con la herramienta Write y después ejecutarlo.

**5. `PYTHONUTF8=1` siempre.** Sin eso, cualquier `print` con acentos revienta con
`UnicodeEncodeError` en la consola de Windows.

**6. faster-whisper y la memoria.** Con poca RAM libre da
`RuntimeError: mkl_malloc: failed to allocate memory`. `large-v3` no cargó; `medium`
tampoco; `small` cargó pero falló al generar con `beam_size=5`. Lo que funciona:
**`small` con `beam_size=1` y `cpu_threads=2`**, más `MKL_NUM_THREADS=1` y
`OMP_NUM_THREADS=1`. El script ya trae la escalera de degradación.

**7. `pdftoppm` no está instalado**, así que la herramienta Read no renderiza PDFs.
Usar **pymupdf** (`fitz`) para convertir páginas a PNG y revisarlas.

**8. reportlab y el desborde de columnas.** El interior de una tarjeta llega hasta
`W - M - 20 = 527 pt`. Cualquier columna alineada a la derecha más allá de eso se corta
sin aviso. Verificar **siempre** renderizando a PNG.

**9. Los avisos LF→CRLF de git son inofensivos** en este repo.

**10. La regla de "cero promedios" se audita.** Antes de entregar:
```bash
python -c "import fitz,re; t=''.join(p.get_text() for p in fitz.open('brochure.pdf')); print(len(re.findall('promedi',t,re.I)))"
```
Debe dar 0. Cuidado: se puede colar al *repudiar* los promedios ("el piso, y no el
promedio"). Reformular sin la palabra.

---

## 10. REGLAS DE ORO

**Heredadas de la v7 (no romper):**

1. **Es una batería (BESS), no una planta solar.** Prohibido "fotovoltaico",
   "generación propia", "planta de generación". El proyecto **compra del nodo; no
   genera**. El costo ≈0 del mediodía es por **saturación de generación renovable zonal
   de terceros**.
2. **No usar promedios como mensaje.** El caso se cuenta con **conteos**, **pisos** y
   **máximos**. Única excepción aceptada: el *costo medio de carga*, etiquetado "costo
   medio", nunca "promedio".
3. **Diseño estilo Apple:** fondo blanco, tarjetas redondeadas, Segoe UI o Inter, mucho
   aire. Que no parezca hecho por IA.
4. **Lenguaje transversal:** cada párrafo sirve al técnico, al de inversiones y al
   director a la vez.

**Nuevas de la v8:**

5. **Underwriting al peor dato, no al promedio.** El ancla incluye la hidrología alta de
   2025 (costo de carga más caro): el caso ya está construido con el lado desfavorable.
6. **Toda debilidad se divulga antes de que la encuentren.** Los tres sesgos del dataset
   van escritos: 2026 parcial y en el semestre favorable (factor Jun-Dic/Ene-May = 0,683);
   a 2024 le faltan 17 días (15–31 jul); la base termina el 22-may-2026.
7. **Cada cifra con fuente y fecha.** Lo marcado NO VERIFICADO **no se publica**.

---

## 11. LO QUE FALTA

| Insumo | Bloquea | Estado |
|---|---|---|
| CAPEX, deuda, tasa, plazo, covenant DSCR | DSCR/LLCR y gatillo 6 | **ÚNICO BLOQUEO REAL.** Celdas vacías y en rojo |
| OPEX anual y reserva de degradación | DSCR definitivo | Pendiente |
| Confirmación del riesgo DS 1/2026 | estructura del proyecto | **Consultar abogado regulatorio** |
| Datos del CEN posteriores al 22-may-2026 | actualización de la base | ~2 meses sin incorporar |
| Correo de Javier | el borrador de Gmail | Quedó dirigido a Nicolás como marcador |
| Nombre del director que objetó | correo y material | La transcripción no permitió confirmar el apellido |

**Nada más está bloqueado.** Margen, spread, break-even, escenarios, el cuadro de PPA y
todo el material ya son válidos y no dependen de estos datos.

---

## 12. PROMPT PARA ARRANCAR CON CLAUDE EN OTRO EQUIPO

> Lee `Banco_Panimavida/HANDOFF_CASA_v8.md` y `PROMPT_MAESTRO_v8.md`. Vamos a seguir con
> Panimávida (BESS de arbitraje, material para el Comité de Crédito de un banco). La
> versión vigente es v8.2. Respeta las reglas de oro: es una batería y no una planta
> solar, nunca usar promedios como mensaje, diseño Apple. Respeta también las cuatro
> correcciones de hechos de la sección 3 — sobre todo que el pipeline de BESS **sí** es
> tangible a nivel nacional y que la brecha es locacional, y que el precio de venta
> estuvo en o sobre 50 USD/MWh el 99,2% de los días, no "nunca bajó de 50". Los scripts
> están en `_scripts_v8/` y después de tocar cualquier fórmula del Excel hay que correr
> `05_verify_excel.py`. La plataforma es el repo `Rho_Panimavida_Banco` con auto-deploy
> de Vercel desde `main`.

---

## 13. HISTORIAL

| Versión | Qué cambió |
|---|---|
| v2 – v5 | Framing inicial; rediseño Apple; se quitó "fotovoltaico" |
| v6 | El protagonista pasa a ser el conteo de horas a $0 y el precio máximo |
| v6.1 | Se eliminó toda mención a "promedios" |
| v7 | Se excluyó 2022; capítulo de costo medio de carga; asesoría de operación |
| **v8.0** | Ancla de 12 meses completos; el hallazgo venta plana / carga al alza; escenarios y gatillos; la calculadora; secciones `#transmision` y `#ventana` |
| **v8.1** | Cuadro con PPA vs sin PPA; brochure a 4 páginas; brochure Word editable |
| **v8.2** | Glosario de 53 términos con buscador (`glosario.html`) |
