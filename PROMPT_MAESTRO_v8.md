# PROMPT MAESTRO — Panimávida 13,2 kV · v8.0

> **Encargo:** defender ante el Comité de Crédito y ante dos asesores escépticos la decisión de
> operar el BESS a **costo marginal (spot)** hasta ~2030, y firmar un PPA recién entre **2030 y 2032**.
> **Fecha:** 29-jul-2026 · **Sustituye:** v7.0 (2-jun-2026) · **Base de datos:** 38.064 h reales del CEN.

---

## 0. Cómo usar este documento

Este es el documento de encuadre. Define **qué se afirma, con qué evidencia y con qué palabras**.
Todo entregable (informe, brochure, Excel, plataforma) debe poder trazarse a una sección de aquí.
Si un número no está en §5, no se publica.

---

## 1. El encargo, en una frase

Convertir una **apuesta** ("nos vamos a marginal") en una **política de comercialización monitoreada**
("operamos a spot dentro de una ventana medida, con gatillos definidos que activan la contratación"),
y respaldarla con números que un asesor hostil no pueda desarmar.

---

## 2. Qué cambió desde la v7

La v7 respondía una sola pregunta: *¿conviene el PPA de compra a 28 USD/MWh?* Respuesta: no.
Eso ya está ganado y no se toca.

Aparecieron **tres frentes nuevos**:

1. **Objeción de transmisión.** Un asesor sostiene que la línea **Kimal–Lo Aguirre** traerá energía
   del norte al sur y hundirá el costo marginal, matando el precio de venta nocturno.
2. **Objeción de rigor.** Otro asesor pide *"ver números y respaldo"*. No discute la tesis: discute
   que esté demostrada.
3. **Horizonte y contratación.** Se necesita una hoja que muestre que conviene ir a marginal **al
   menos hasta 2030**, aprovechando la brecha en que el pipeline de BESS aún no es tangible, y un
   plan para **negociar el PPA desde el primer año de operación** y tenerlo **firmado entre 2030 y 2032**.

---

## 3. Reglas de oro

**Vigentes de la v7 (no romper):**

1. **Es una batería (BESS), no una planta solar.** Prohibido "fotovoltaico", "generación propia",
   "planta de generación". El proyecto **compra del nodo; no genera**. El costo ≈0 del mediodía se
   explica por **saturación de generación renovable zonal de terceros**.
2. **No usar promedios como mensaje.** El caso se cuenta con **conteos** (cuántas horas valen $0),
   **pisos** (el mínimo histórico) y **máximos**. Excepción acotada y ya aceptada: el *costo medio de
   carga*, etiquetado como "costo medio", nunca como "promedio".
3. **Diseño estilo Apple**: fondo blanco, tarjetas redondeadas, Segoe UI, mucho aire. Que no parezca
   hecho por IA.
4. **Lenguaje transversal**: cada párrafo sirve al técnico, al de inversiones y al director a la vez.

**Nuevas de la v8:**

5. **Underwriting al peor año, no al promedio.** El caso base pasa a ser **2026 — el año más
   comprimido del registro**. Todo lo mejor es upside. Un promedio de 4 años que incluye el pico de
   la crisis energética 2022–23 es indefendible como expectativa forward, y es exactamente por
   donde un asesor rompería el informe.
6. **Toda debilidad se divulga antes de que la encuentren.** Los tres sesgos del dataset (§10) van
   escritos en el informe, no escondidos. Divulgar convierte una vulnerabilidad en credibilidad.
7. **Cada cifra con fuente y fecha.** Los datos de transmisión y de pipeline BESS se marcan
   `HECHO VERIFICADO (fuente, fecha)` o `INFERENCIA`. Prohibido estimar y presentarlo como dato.

---

## 4. El reencuadre analítico: las dos objeciones colapsan en una sola variable

Éste es el núcleo intelectual de la v8 y debe aparecer explícito en todos los entregables.

**El HVDC Kimal–Lo Aguirre transporta excedente solar. El sol es un recurso diurno. La batería
vende de noche.**

De ahí se sigue:

- Más energía solar barata del norte llegando a la zona centro **profundiza el valle diurno** →
  **baja el costo de carga** → **ensancha el spread por el lado de la compra**. El HVDC, en primer
  orden, **ayuda** al proyecto.
- El precio del **pico nocturno** no lo fija el sol: lo fija el **costo variable de la última unidad
  térmica** que entra al anochecer. Ese es el piso, y es un piso de combustible, no de cero.
- Lo único que puede **trasladar** ese excedente solar diurno hacia la noche y comprimir el pico
  es **almacenamiento masivo** (o nueva capacidad firme, o gestión de demanda). No una línea.

**Conclusión:** ambas objeciones —la de transmisión y la del horizonte— se reducen a **una sola
variable: la velocidad de entrada en operación de BESS en el SEN.** Y esa variable tiene dos
propiedades que la hacen bancable: es **observable** (registro público del Coordinador y del SEA) y
tiene **plazo de anticipación largo** (RCA → construcción → operación comercial). Se puede medir y
se puede ver venir.

Esto también responde al matiz que el propio equipo ya había identificado: *"el valor de venta no
baja con Kimal–Lo Aguirre; cuando se habla de sur se habla hasta la zona centro, y se necesitan
otras líneas para llegar a Panimávida."* La v8 lo formaliza con la topología y con las fechas
decretadas de los refuerzos (§6.1).

**Evidencia directa que ya tenemos de que el mecanismo funciona así:** entre ene–may 2023 y
ene–may 2026 el **costo de carga cayó de 31,4 a 9,6 USD/MWh** (−22) mientras el precio de venta
caía de 196,1 a 85,0. El lado carga se movió exactamente como predice la saturación solar, y
absorbió ~20% de la caída del lado venta. El spread es más resiliente que el precio de venta.

---

## 5. Hallazgos duros de las 38.064 horas

*Recálculo independiente sobre los datos crudos (`Datos_CMg`), día a día. Reproduce exactamente el
Resultado_Anual del informe v7, lo que valida el modelo existente.*

### 5.1 Resultado anual (ventana 4 h)

| Año | Carga (USD/MWh) | Venta (USD/MWh) | Spread |
|---|---|---|---|
| 2022 | 45,0 | 184,8 | 139,8 |
| 2023 | 19,9 | 143,1 | 123,3 |
| 2024 | 8,1 | 93,8 | 85,7 |
| 2025 | 24,0 | 113,0 | 89,0 |
| 2026 (parcial) | 9,6 | 85,0 | 75,4 |
| **Base 23–26** | **15,4** | **108,7** | **93,4** |

Reproduce exactamente el `Resultado_Anual` del informe v7, lo que valida el modelo existente. **Pero
el año calendario no es el ancla correcta:** 2026 es parcial y cae en el semestre estacionalmente
favorable. El ancla correcta son ventanas de 12 meses completos (§5.2).

### 5.2 EL HALLAZGO CENTRAL — no está cayendo lo que el director cree que está cayendo

Ventanas de 12 meses completos, comparables entre sí:

| Ventana | Carga | Venta | Spread |
|---|---|---|---|
| 23-may-2022 → 22-may-2023 | 37,7 | 200,0 | 162,3 |
| 23-may-2023 → 22-may-2024 | 12,3 | 108,2 | 96,0 |
| 23-may-2024 → 22-may-2025 | 10,1 | 98,2 | 88,1 |
| **23-may-2025 → 22-may-2026** ← **ANCLA** | **22,1** | **99,6** | **77,5** |

> **El precio de venta nocturno está PLANO en 98–100 USD/MWh desde hace tres años (108,2 → 98,2 →
> 99,6). Lo que se movió, y explica prácticamente toda la compresión reciente del spread, es el
> COSTO DE CARGA: subió de 10,1 a 22,1 USD/MWh en la última ventana.**

**Consecuencia estratégica, y es el giro de toda la v8:** el director del banco teme que
Kimal–Lo Aguirre baje el **precio de venta nocturno**. Los datos del nodo dicen que el precio de venta
nocturno no viene cayendo. El que se movió es el **costo de carga diurno** — y Kimal–Lo Aguirre actúa
precisamente sobre el costo marginal **diurno**, empujándolo **a la baja**.

**La línea que se teme es, sobre la evidencia disponible, viento de cola para el riesgo real del
proyecto, no viento de frente.** Y el riesgo verdadero —el alza del costo de carga— es exactamente el
que identificó el asesor técnico en su audio. Coinciden el asesor y los datos.

¿La carga tiene tendencia o es hidrología? Oscila entre 8,1 y 45,0 sin tendencia monótona: 8,1 (2024)
→ 24,0 (2025) → 9,6 (ene–may 2026). El alza de 2025 es consistente con mayor hidrología —menos
vertimiento, menos horas a costo cero— y **ya revirtió**. Se trata como riesgo estructural de largo
plazo, no como tendencia instalada.

### 5.2 bis · El piso nocturno — enunciado CORREGIDO

⚠️ **Corrección de una afirmación previa que era falsa.** Una versión anterior de este documento
afirmaba que "en 1.586 días el precio de venta nunca bajó de 50 USD/MWh". **Eso era un artefacto de
filtrar solo ene–may.** El enunciado verificado sobre el registro completo es:

| Umbral | Días bajo el umbral | % del registro | % en o sobre el umbral |
|---|---|---|---|
| venta < 40 | 4 | 0,3% | 99,7% |
| **venta < 50** | **12** | **0,8%** | **99,2%** |
| venta < 55 | 30 | 1,9% | 98,1% |
| venta < 60 | 87 | 5,5% | 94,5% |

El mínimo absoluto del registro es **0,0 USD/MWh (30-oct-2022)**, un día atípico. En la **ventana
ancla** el peor día fue **48,8** y el percentil 10 fue **58,5**.

**Formulación publicable:** *"el 99,2% de los 1.586 días del registro tuvo precio de venta en o sobre
50 USD/MWh; en los últimos 12 meses el peor día fue 48,8."* Nunca decir "nunca bajó de 50".

### 5.3 La caída es real, pero está desacelerando y tiene forma de re-nivelación

| Métrica | Valor |
|---|---|
| Spread móvil 12M — máximo | **162,8** (may-2023) |
| Spread móvil 12M — último | **77,1** (may-2026) |
| Caída desde el máximo | **−53%** |
| Pendiente ene–may, serie completa 2022→2026 | −13,1 USD/MWh por año |
| **Pendiente móvil 12M desde jun-2024** | **−4,9 USD/MWh por año** |
| Móvil 12M entre dic-2024 y ene-2026 | **plano en 84–90** |

**Lectura obligatoria en el informe:** la pendiente de −13/año es un artefacto de medir desde el
**pico de la crisis energética 2022–2023**. Medida sobre los últimos dos años, la pendiente real es
**−4,9/año**, y el móvil 12M estuvo **plano durante 14 meses**. Lo ocurrido no es un colapso en
curso: es una **re-nivelación desde un máximo excepcional hacia un nivel estructural de 77–90**.

### 5.4 Días operables (el arbitraje funciona casi todos los días)

| Año | Spread > 40 | > 60 | > 80 |
|---|---|---|---|
| 2024 | 96% | 85% | 44% |
| 2025 | 89% | 76% | 46% |
| **2026** | **91%** | **68%** | **23%** |

### 5.5 Margen bruto día a día, por número de ciclos

*Selección diaria real (no precio medio × volumen). Carga 36 MWh/ciclo, venta 29,88 MWh/ciclo (RT 83%).*

| Año | 182 ciclos | 250 ciclos | 300 ciclos |
|---|---|---|---|
| 2023 | 910.777 | 1.096.938 | 1.212.092 |
| 2024 | 577.431 | 723.044 | 818.374 |
| 2025 | 672.716 | 811.606 | 898.237 |
| **2026 (peor año)** | **524.363** | **655.204** | **739.446** |

**Nota metodológica que resuelve una inconsistencia del expediente actual:** el informe v7 reporta
**US$493 mil/año** y el correo enviado al banco menciona **≈US$0,9 millones/año**. No es un error de
ninguno de los dos: son **dos métodos y dos niveles de utilización distintos**.

- 493 mil = precio medio anual × volumen anual, a 182 ciclos.
- 720 mil = selección día a día, a 182 ciclos *(la diferencia es la covarianza que el promedio destruye)*.
- ~976 mil = selección día a día, a 300 ciclos.

**Hay que unificarlo y declararlo explícitamente**, porque un analista de crédito va a cruzar el
correo con el informe y va a encontrar la brecha.

### 5.6 Los 182 ciclos son muy conservadores

182 ciclos/año = **50% de utilización** (un ciclo cada dos días). Pero en 2026 —el peor año— **91%
de los días tuvieron spread > 40 USD/MWh**. La operación soporta 300+ ciclos. Los 182 del "plan de
operación" deben presentarse como **piso deliberado**, y los 300 como caso operacional, no al revés.

### 5.7 Break-even de spread

*Margen anual = ciclos × (venta × 29,88 − carga × 36). Con carga ≈12 USD/MWh:*

| Servicio de deuda | A 250 ciclos requiere spread | A 300 ciclos requiere spread |
|---|---|---|
| US$ 200.000 | ~29 | ~25 |
| US$ 300.000 | ~43 | ~36 |
| US$ 400.000 | ~56 | ~47 |
| US$ 500.000 | ~69 | ~58 |

Contra un spread observado de **75,4 en el peor año** y un **P10 diario de 41,6 en ese mismo año**.
La holgura es el argumento, y se expresa como **cuánto tiene que caer el mercado antes de que
duela**, no como cuánto se gana.

---

## 6. Las dos objeciones, respondidas

### 6.1 "Kimal–Lo Aguirre va a hundir el costo marginal"

Respuesta en cuatro movimientos:

1. **Perfil horario.** El HVDC mueve excedente solar → diurno. Deprime el valle, no el pico.
   Beneficia el lado carga. *(Requiere confirmación documental — §11.)*
2. **Punto de aterrizaje.** Llega a **Lo Aguirre, Región Metropolitana**. "Sur" en la discusión de
   planificación significa *hasta la zona centro*. Panimávida está en el **Maule**, aguas abajo, en
   un nodo de **13,2 kV**. *(Confirmar topología y distancia eléctrica — §11.)*
3. **Se necesitan otras líneas.** Para que esa energía llegue a comprimir el precio en Panimávida
   hacen falta refuerzos adicionales centro-sur, con **fechas decretadas** que hay que poner en una
   tabla con fuente. *(§11.)*
4. **Quien comprime el pico es el almacenamiento, no la línea.** Y eso devuelve al punto único: la
   velocidad de entrada de BESS.

### 6.2 "Necesito ver números y respaldo"

Se responde con §5 completo, más:

- Memoria de cálculo con **fórmulas vivas** sobre las 38.064 horas (ya existe; hay que extenderla).
- **Divulgación de los tres sesgos** del dataset (§10).
- **Escenarios** de compresión del spread 2027–2035 con una sola variable explícita y su fuente.
- **Break-even y DSCR** parametrizados, con celdas editables para que el banco ponga sus propios
  supuestos y vea el resultado recalcularse. Esto convierte el modelo de "afirmación" en "herramienta".

---

## 7. Estrategia de dos fases, con gatillos

### Fase 1 · 2027–2030 — Cosecha del spread a spot
La ventana está abierta y es medible. Se opera a costo marginal con servicio de pronóstico
day-ahead. Se monitorean los gatillos trimestralmente.

### Fase 2 · 2030–2032 — Transición contractual
Se negocia **desde el primer año de operación** para tener el contrato **firmado entre 2030 y 2032**.
La diferencia frente a firmar hoy: se firma **con tres a cinco años de historia operacional propia
del activo** y con el mercado de contratos para almacenamiento ya formado. Se firma **con
información, no con incertidumbre** — y eso es precio.

### Sistema de gatillos (el entregable que gana el comité)

Convierte la decisión en una política revisable. Cada gatillo tiene métrica, umbral, fuente y acción.

| # | Gatillo | Métrica y fuente | Acción al activarse |
|---|---|---|---|
| 1 | Compresión de spread | Spread móvil 12M del nodo (CEN) bajo el umbral definido | Acelerar negociación de contrato |
| 2 | Erosión del piso nocturno | P10 mensual del pico 4 h bajo umbral | Revisar caso base y perfil de deuda |
| 3 | Materialización de BESS | MW en **operación** en el SEN (Coordinador) | Reponderar horizonte de la Fase 1 |
| 4 | Refuerzo de transmisión | Entrada en operación de obra centro-sur relevante | Reevaluar exposición locacional |
| 5 | Cobertura de deuda | DSCR proyectado bajo el mínimo del covenant | Activar contratación parcial |

Los umbrales se fijan cuando estén los datos de §11 y los términos de deuda. **No inventar umbrales.**

---

## 8. Distinción de instrumentos — corregir una ambigüedad del expediente

El expediente actual dice "no PPA ahora, reevaluar hacia 2030". Un lector atento pregunta: *¿no
querían PPA o sí querían PPA?* La respuesta requiere separar **dos contratos distintos** que hoy se
nombran igual:

| | **PPA de compra a 28 USD/MWh** *(la oferta sobre la mesa)* | **Contrato de venta / floor nocturno / tolling** *(el instrumento de 2030–2032)* |
|---|---|---|
| Qué fija | El precio al que el proyecto **compra** su energía de carga | El precio al que el proyecto **vende** en la noche |
| Riesgo que cubre | Que **suba** el precio de compra | Que **caiga** el precio de venta |
| ¿Es el riesgo del proyecto? | **No.** El proyecto es posición vendedora | **Sí.** Es exactamente el riesgo real |
| Efecto en el margen | Lo **destruye** (~83 mil/año) | Lo **estabiliza** |
| Veredicto | **Rechazar de forma permanente**, no "por ahora" | **Negociar desde el año 1, firmar 2030–2032** |

**Este cuadro debe ir en el informe y en el brochure.** Elimina la aparente contradicción y sube el
nivel de la conversación: no es "spot vs contrato", es *"el contrato correcto en el momento correcto"*.

Y precisa el veredicto sobre la oferta actual: el PPA de compra a 28 **no mejora hacia 2030**. Mientras
persista la saturación solar diurna, comprar carga a 28 seguirá siendo peor que comprarla a spot.
Lo que se reevalúa en 2030 **no es esa oferta**: es un instrumento distinto.

---

## 9. Entregables y criterios de aceptación

| # | Entregable | Criterio de aceptación |
|---|---|---|
| 1 | **Hoja "Ventana de arbitraje 2027–2035"** (Excel, fórmulas vivas) | Escenarios manejados por **una** variable explícita; break-even y DSCR con celdas editables; sin números hard-coded |
| 2 | **Hoja "Gatillos"** | 5 gatillos con métrica, fuente, umbral y acción; semáforo automático |
| 3 | **Hoja "Mapa de transmisión"** | Obras centro-sur con capacidad, año y **URL de fuente** por fila |
| 4 | **Hoja "Compra vs Venta"** | El cuadro de §8 con el cálculo de sobrecosto asociado |
| 5 | **Informe v8** | Integra §4, §5, §6, §7, §8 y §10; reglas de oro respetadas; cada cifra trazable |
| 6 | **Brochure** | 2–4 páginas, estilo Apple, para banco y asesores. Hero = el piso de 50 USD/MWh, no un promedio |
| 7 | **Plataforma actualizada** | Nueva sección de ventana/gatillos; datos de `data.js` regenerados; deploy verificado en vivo |
| 8 | **HANDOFF actualizado** | Refleja v8, nuevas reglas y estado de los insumos pendientes |

---

## 10. Divulgaciones obligatorias de integridad de datos

Van escritas en el informe. No son notas al pie: son parte del argumento de credibilidad.

1. **2026 es parcial y cae en el semestre favorable.** Cubre 1-ene a 22-may (142 días). El factor
   estacional medido Jun-Dic/Ene-May es **0,683**, es decir el segundo semestre es sistemáticamente
   peor. Por lo tanto el 75,4 de 2026 **sobreestima el año completo**, que se estima en **61,4**.
   Consecuencia: la "Base 23–26" de 93,4 corregida estacionalmente es **89,8**.
2. **2024 está incompleto.** Faltan 17 días (15–31 de julio de 2024): 349 de 366 días.
3. **La base termina el 22-may-2026.** A la fecha de este documento hay ~2 meses de datos nuevos
   del Coordinador sin incorporar. Debe actualizarse antes de enviar al banco.

---

## 11. Insumos que faltan (bloquean partes del trabajo)

| Insumo | Bloquea | Estado |
|---|---|---|
| CAPEX, monto de deuda, tasa, plazo, gracia, covenant DSCR | DSCR/LLCR y gatillo #6 | **PENDIENTE — es el único bloqueo real.** El libro ya está parametrizado; las celdas están vacías y marcadas en rojo |
| OPEX anual y reserva de degradación | DSCR definitivo | **PENDIENTE** |
| Fechas y capacidades de refuerzos centro-sur; aterrizaje y perfil horario del HVDC | §6.1 y hoja Transmisión | ✅ **Resuelto** — ver `FUENTES_v8_transmision.md` |
| MW de BESS en operación vs. anunciados en el SEN | Gatillo #4 y escenarios | ✅ **Resuelto** — ver `FUENTES_v8_bess_mercado.md` |
| Datos del CEN posteriores al 22-may-2026 | Divulgación #3 | Pendiente de descarga (~2 meses) |
| Contenido de los tres audios del 29-jul-2026 | Encuadre y prioridades | ✅ **Resuelto** — ver §13 |
| Confirmación regulatoria del riesgo DS 1/2026 | Estructura del proyecto | **PENDIENTE — consultar abogado regulatorio antes del Comité** |

---

## 13. Lo que aportaron los audios del 29-jul-2026

Tres audios transcritos: dos del asesor técnico (≈7 min) y uno de conversación interna (≈10 min).

### 13.1 Hay una reunión MAÑANA
Fija la prioridad: primero la hoja de cálculo, después el brochure, después la plataforma.

### 13.2 Quién es el escéptico
Un **director** de la contraparte que **entiende de mercado eléctrico** — no un lego. Cree que la línea
Kimal–Lo Aguirre hará que el precio de venta nocturno de Panimávida sea más bajo. Consecuencia de
encuadre: el material tiene que ser técnicamente sólido y citable, no marketing. Nada de afirmaciones
sin fuente.

### 13.3 La crítica exacta al material ya enviado
> *"Ese documento es muy del pasado y del presente. Entonces no habla del futuro."*

Es la crítica más útil de todo el material. El informe v7 documenta 2022–2026 impecablemente y **no
dice nada sobre 2027–2032**. Eso es precisamente el vacío que llena la v8.

### 13.4 Lo que piden, literal
Una **"hoja"** y **"tener la calculadora"** — *"algo que sea certero"*. No un informe más: un
instrumento con el que se pueda mover un supuesto y ver el resultado. De ahí el diseño del libro con
Panel de palancas y escenarios editables.

### 13.5 El asesor técnico CONFIRMA nuestra tesis sobre el HVDC — y señala el riesgo verdadero
- Sobre Kimal–Lo Aguirre: *"no lo veo mucho efecto en cuanto al tema de los desacoples"*, porque
  Panimávida *"está en el Maule, bastante retirado de lo que es Lo Aguirre, que es la Región
  Metropolitana"*.
- Advierte que la congestión desde **Alto Jahuel al sur** persiste si no se refuerza **de aquí a
  2029–30**.
- **El riesgo real que identifica:** *"indistintamente de esas situaciones de transmisión, la
  incorporación masiva de energía renovable y principalmente de BESS […] se va a ir haciendo más
  estrecho entre el horario día y el horario noche"*.
- Y el mecanismo preciso: *"mientras menos vertimiento se tenga, eso significa que los costos
  marginales ya no van a ser ceros […] por lo tanto ahí el spread puede que tenga un efecto
  relevante"*.
- Además corrige un error de encuadre frecuente: los precios cero **no** son principalmente por
  congestión de transmisión sino por **sobreoferta** diurna — *"no es un tema de congestión de
  transmisión, como se ha enfocado por parte de algunos actores; hay […] principalmente una
  sobreoferta"*.

**Esto es oro: el asesor experto de la contraparte apunta al mismo riesgo que los datos del nodo
—el alza del costo de carga— y no al que teme el director.** El material debe darle la razón
explícitamente al asesor y usar su propio razonamiento para responder al director.

### 13.6 La premisa que hay que corregir
El audio dice: *"hay mucho proyecto de integración de BESS, no es tan [tangible] en este momento […]
un proyecto se demora 4 y 5 años […] esa es la brecha que queremos aprovechar."*

⚠️ **A nivel nacional esa premisa es falsa y sostenerla destruiría la credibilidad.** Los datos
oficiales: **2.283 MW / 9.346 MWh en operación** (mar-2026), proyección de **5.081 MW** a dic-2026,
**6.358 MW en construcción** (74 proyectos), y Chile **superó la meta de 2 GW en enero de 2026, cuatro
años antes de lo previsto**. El almacenamiento en Chile es tangible y va **más rápido** de lo previsto.

**La brecha real es LOCACIONAL, no temporal — y es un argumento más fuerte:** del MW en construcción,
**Antofagasta 44%, Atacama 23%, Tarapacá 13,6%, RM 5%. El Maule no figura.** ~86% está en el norte.
Y la **CNE proyecta que el desacople de la zona sur persiste hacia 2032** incluso con las obras de
500 kV. Eso sí se puede defender ante un director que entiende el mercado.

### 13.7 Corrección al plan de la Fase 2
El audio plantea *"firmar el PPA el 2032, negociándolo desde el primer año de operación"*. La
investigación de mercado no encontró **ningún** PPA ni tolling de almacenamiento a escala PMG
(<10 MW) en Chile: los contratos verificados son de cientos de MW con contrapartes investment grade.
**Prometer al banco "un PPA en 2032" para 9 MW es una promesa sin mercado que la respalde.** Hay que
renombrarla como estrategia de contratación con instrumentos alternativos (§8 y hoja `Instrumentos`).

---

## 12. Orden de ejecución

1. Integrar los audios y ajustar este documento si cambian el encuadre.
2. Cerrar la investigación de transmisión y de pipeline BESS; llenar la hoja de fuentes.
3. Construir el modelo de escenarios y gatillos sobre los datos ya recalculados.
4. Unificar la cifra de margen (§5.5) y fijar el caso base en 2026.
5. Informe v8 → brochure → plataforma → HANDOFF.

---

*Toda cifra de §5 proviene del recálculo independiente sobre `Datos_CMg` (38.064 horas, Coordinador
Eléctrico Nacional, Real Definitivo). El script de recálculo queda versionado junto a los entregables.*
