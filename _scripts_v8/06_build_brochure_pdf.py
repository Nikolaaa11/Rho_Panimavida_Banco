# -*- coding: utf-8 -*-
"""Brochure Panimavida v8 - 3 paginas, estilo Apple, para banco y asesores."""
import sys, os
sys.stdout.reconfigure(encoding='utf-8')
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, Color
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

import os as _os
_BASE = _os.path.dirname(_os.path.abspath(__file__))
_DATOS = _os.path.join(_BASE, 'datos')


W, H = A4
INK = HexColor('#1d1d1f')
GREY = HexColor('#6e6e73')
GREYL = HexColor('#86868b')
HAIR = HexColor('#e6e6ea')
GREEN = HexColor('#218358')
GREENL = HexColor('#30a46c')
GREENBG = HexColor('#f2f9f5')
RED = HexColor('#e5484d')
REDBG = HexColor('#fdf2f2')
AMBER = HexColor('#b25e09')

FD = r'C:\Windows\Fonts'
for name, fn in [('SG', 'segoeui.ttf'), ('SGB', 'segoeuib.ttf'),
                 ('SGL', 'segoeuil.ttf'), ('SGI', 'segoeuii.ttf'),
                 ('SGSL', 'segoeuisl.ttf')]:
    pdfmetrics.registerFont(TTFont(name, os.path.join(FD, fn)))

M = 48          # margen
CW = W - 2 * M  # ancho de contenido

def make_chart():
    """Grafico de los tres escenarios, estilo Apple, para embeber en la pagina 2."""
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib import font_manager
    try:
        font_manager.fontManager.addfont(os.path.join(FD, 'segoeui.ttf'))
        fam = 'Segoe UI'
    except Exception:
        fam = 'DejaVu Sans'
    plt.rcParams.update({'font.family': fam, 'font.size': 8.5})

    anios = list(range(2027, 2036))
    esc = {
        'A · Ventana amplia': ([77.5, 77.5, 77.5, 77.5, 74.5, 71.5, 68.5, 65.5, 62.5], '#218358'),
        'B · Base':           ([77.5, 77.5, 71.0, 64.5, 58.0, 51.5, 45.0, 38.5, 32.0], '#30a46c'),
        'C · Estrés tipo NEM':([62.5, 47.5, 32.5, 19.6, 10.0, 10.0, 10.0, 10.0, 10.0], '#e5484d'),
    }
    fig, ax = plt.subplots(figsize=(7.4, 2.05), dpi=220)
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')
    for lb, (vals, col) in esc.items():
        base = lb.startswith('B')
        ax.plot(anios, vals, color=col, lw=2.6 if base else 1.7,
                marker='o' if base else None, ms=3.6,
                solid_capstyle='round', label=lb, zorder=4 if base else 3)
    ax.axhline(43.9, color='#e5484d', ls=(0, (4, 3)), lw=1.3, zorder=2)
    ax.annotate('break-even 43,9', xy=(2027.05, 45.6), color='#e5484d', fontsize=7.6)
    ax.fill_between(anios, esc['B · Base'][0], 43.9,
                    where=[v >= 43.9 for v in esc['B · Base'][0]],
                    color='#30a46c', alpha=0.09, zorder=1)
    for sp in ('top', 'right'):
        ax.spines[sp].set_visible(False)
    for sp in ('left', 'bottom'):
        ax.spines[sp].set_color('#e6e6ea')
    ax.grid(axis='y', color='#e6e6ea', lw=0.7)
    ax.set_axisbelow(True)
    ax.set_ylim(0, 90)
    ax.set_xlim(2027, 2035)
    ax.set_xticks(anios)
    ax.tick_params(colors='#6e6e73', length=0, labelsize=7.8)
    ax.set_ylabel('USD/MWh', color='#6e6e73', fontsize=8)
    ax.legend(frameon=False, loc='lower left', fontsize=7.2,
              labelcolor='#6e6e73', handlelength=1.5, ncol=3,
              borderaxespad=0.4)
    fig.tight_layout(pad=0.4)
    out = _os.path.join(_DATOS, 'bro_chart.png')
    fig.savefig(out, facecolor='white', bbox_inches='tight')
    plt.close(fig)
    return out


c = canvas.Canvas('', pagesize=A4)


def txt(x, y, s, font='SG', size=10, col=INK, align='l'):
    c.setFont(font, size)
    c.setFillColor(col)
    if align == 'l':
        c.drawString(x, y, s)
    elif align == 'r':
        c.drawRightString(x, y, s)
    else:
        c.drawCentredString(x, y, s)


def wrap(s, font, size, maxw):
    c.setFont(font, size)
    words, lines, cur = s.split(), [], ''
    for w_ in words:
        t = (cur + ' ' + w_).strip()
        if c.stringWidth(t, font, size) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


def para(x, y, s, font='SG', size=10, col=INK, maxw=None, lead=None):
    maxw = maxw or CW
    lead = lead or size * 1.55
    for ln in wrap(s, font, size, maxw):
        txt(x, y, ln, font, size, col)
        y -= lead
    return y


def card(x, y, w, h, bg=None, border=HAIR, rad=12, shadow=True):
    if shadow:
        for i, a in enumerate([0.045, 0.03, 0.018]):
            c.setFillColor(Color(0, 0, 0, alpha=a))
            c.roundRect(x + 0.7 * (i + 1), y - 0.9 * (i + 1), w, h, rad, stroke=0, fill=1)
    c.setFillColor(bg if bg else HexColor('#ffffff'))
    c.setStrokeColor(border)
    c.setLineWidth(0.7)
    c.roundRect(x, y, w, h, rad, stroke=1, fill=1)


def rule(y, x0=M, x1=None, col=HAIR, w_=0.7):
    c.setStrokeColor(col)
    c.setLineWidth(w_)
    c.line(x0, y, x1 or (W - M), y)


def eyebrow(y, s, col=GREEN):
    c.setFont('SGB', 8.2)
    c.setFillColor(col)
    c.drawString(M, y, ' '.join(s.upper()))
    return y


def foot(pag):
    rule(48)
    txt(M, 34, 'Panimávida 13,2 kV  ·  BESS 9 MW / 36 MWh  ·  RHO Generación · FIP CEHTA Capital',
        'SG', 7.6, GREYL)
    txt(W - M, 34, f'{pag} / 4', 'SG', 7.6, GREYL, 'r')


# ══════════════════════════════════════════ PAGINA 1
eyebrow(H - 62, 'Panimávida 13,2 kV  ·  análisis para el comité de crédito  ·  julio 2026')

y = H - 106
c.setFont('SGL', 30)
c.setFillColor(INK)
for ln in wrap('No está cayendo lo que se cree', 'SGL', 30, CW):
    c.drawString(M, y, ln)
    y -= 36
c.setFont('SGL', 30)
c.drawString(M, y, 'que está cayendo.')
y -= 30

y = para(M, y, 'La objeción planteada al proyecto es que la línea HVDC Kimal–Lo Aguirre hará bajar '
         'el precio de venta nocturno del nodo. Los datos del propio nodo, medidos en ventanas de '
         'doce meses completos, muestran otra cosa.', 'SG', 11, GREY, CW, 17)
y -= 14

# Tabla de ventanas de 12 meses
CH = 138
card(M, y - CH, CW, CH)
ty = y - 22
txt(M + 20, ty, 'Ventanas de 12 meses completos · 1.586 días reales del Coordinador Eléctrico Nacional',
    'SGB', 9, INK)
ty -= 20
# bordes derechos = cols[k] + 60, todos dentro del interior de la tarjeta (max W-M-20 = 527)
cols = [M + 20, M + 236, M + 326, M + 415]
for lb, cx in zip(['Ventana', 'Costo de carga', 'Precio de venta', 'Spread'], cols):
    txt(cx if lb == 'Ventana' else cx + 60, ty, lb, 'SGB', 8.2, GREY, 'l' if lb == 'Ventana' else 'r')
ty -= 6
rule(ty, M + 20, W - M - 20, GREEN, 0.9)
ty -= 17
rows = [('2022 – 2023', '37,7', '200,0', '162,3', False),
        ('2023 – 2024', '12,3', '108,2', '96,0', False),
        ('2024 – 2025', '10,1', '98,2', '88,1', False),
        ('2025 – 2026', '22,1', '99,6', '77,5', True)]
for lb, cg, vt, sp, last in rows:
    f = 'SGB' if last else 'SG'
    txt(cols[0], ty, lb, f, 9.6, INK)
    txt(cols[1] + 60, ty, cg, f, 9.6, RED if last else INK, 'r')
    txt(cols[2] + 60, ty, vt, 'SGB', 9.6, GREEN, 'r')
    txt(cols[3] + 60, ty, sp, f, 9.6, INK, 'r')
    ty -= 17
txt(cols[0], ty - 2, 'USD/MWh · ventana de 4 horas · carga 09–17 h, venta 19–07 h', 'SGI', 7.4, GREYL)
y -= CH + 20

# La conclusion, en verde
CH2 = 96
card(M, y - CH2, CW, CH2, GREENBG, GREENL)
ty = y - 24
txt(M + 20, ty, 'El precio de venta nocturno está plano desde hace tres años.', 'SGB', 12.5, GREEN)
ty -= 20
ty = para(M + 20, ty, '108,2 → 98,2 → 99,6 USD/MWh. Lo que se movió, y explica prácticamente toda la '
          'compresión reciente del spread, es el costo de cargar de día: subió de 10,1 a 22,1 USD/MWh.',
          'SG', 10, INK, CW - 40, 15)
y -= CH2 + 22

# El giro
txt(M, y, 'El giro del argumento', 'SGB', 13, INK)
y -= 20
for t in ['Kimal–Lo Aguirre transporta excedente solar. El sol es un recurso diurno; la batería vende '
          'de noche. La línea actúa sobre el costo marginal del día — es decir, sobre el lado donde está '
          'el riesgo real — y lo empuja a la baja.',
          'Sobre la evidencia disponible, la línea que se teme es viento de cola para este proyecto, no '
          'viento de frente. Y no llega al Maule: termina en Lo Aguirre, Región Metropolitana.']:
    y = para(M + 12, y, '·  ' + t, 'SG', 10, INK, CW - 24, 15.5)
    y -= 7

y -= 14
txt(M, y, 'El piso del precio de venta', 'SGB', 13, INK)
y -= 20
y = para(M, y, 'El caso no se sostiene en una cifra única, sino en la distribución completa del '
         'registro: en 1.586 días, el precio de venta de las cuatro horas de punta estuvo en o sobre '
         '50 USD/MWh el 99,2% de los días.', 'SG', 10, INK, CW, 15.5)
y -= 12

pw = (CW - 30) / 4
pisos = [('99,7%', 'en o sobre 40', '4 días bajo el umbral'),
         ('99,2%', 'en o sobre 50', '12 días bajo el umbral'),
         ('98,1%', 'en o sobre 55', '30 días bajo el umbral'),
         ('94,5%', 'en o sobre 60', '87 días bajo el umbral')]
for i, (pc, lb, sub) in enumerate(pisos):
    x = M + i * (pw + 10)
    acc = i == 1
    card(x, y - 70, pw, 70, GREENBG if acc else None, GREENL if acc else HAIR, 10)
    txt(x + 13, y - 30, pc, 'SGB', 17, GREEN if acc else INK)
    txt(x + 13, y - 45, lb + ' USD/MWh', 'SG', 8, GREY)
    txt(x + 13, y - 58, sub, 'SG', 7.4, GREYL)
y -= 84
para(M, y, 'El mínimo absoluto del registro es 0,0 USD/MWh (30-oct-2022), un día atípico. En los '
     'últimos 12 meses el peor día fue 48,8 y el percentil 10 fue 58,5 USD/MWh.', 'SGI', 8.2, GREYL, CW, 11)

foot(1)
c.showPage()

# ══════════════════════════════════════════ PAGINA 2
eyebrow(H - 62, 'la ventana de arbitraje  ·  2027 – 2035')
y = H - 100
c.setFont('SGL', 26)
c.setFillColor(INK)
c.drawString(M, y, 'Hasta cuándo conviene el marginal.')
y -= 26
y = para(M, y, 'Una sola variable manda: la velocidad con que el almacenamiento del sistema llega a '
         'comprimir este nodo. Se modela por los dos lados —la venta baja y la carga sube— y se compara '
         'contra el spread mínimo necesario para pagar la deuda.', 'SG', 10.5, GREY, CW, 16)
y -= 16

# Tres KPI
kw = (CW - 24) / 3
kpis = [('815', 'mil US$ / año', 'Margen bruto de los últimos\n12 meses reales · 340 ciclos', True),
        ('43,9', 'USD/MWh', 'Spread necesario para cubrir\nel servicio de la deuda', False),
        ('2034', 'escenario base', 'Año en que el spread cruza\nese umbral', False)]
for i, (num, un, lb, acc) in enumerate(kpis):
    x = M + i * (kw + 12)
    card(x, y - 92, kw, 92, GREENBG if acc else None, GREENL if acc else HAIR)
    txt(x + 16, y - 36, num, 'SGB', 25, GREEN if acc else INK)
    txt(x + 16, y - 52, un, 'SG', 8.4, GREYL)
    yy = y - 68
    for ln in lb.split('\n'):
        txt(x + 16, yy, ln, 'SG', 8.4, GREY)
        yy -= 11
y -= 126

# Escenarios
txt(M, y, 'Tres escenarios de compresión', 'SGB', 13, INK)
y -= 8
rule(y, M, W - M, GREEN, 0.9)
y -= 18
esc = [('A · Ventana amplia', 'Compresión desde 2031', '62,5', 'no cruza al 2035',
        'El almacenamiento sigue concentrado en el norte y la CNE proyecta desacople del sur hacia 2032.'),
       ('B · Base', 'Compresión desde 2029', '32,0', '2034',
        'Compresión gradual desde la entrada de Kimal–Lo Aguirre (2029–2030) y llegada parcial de BESS al centro-sur.'),
       ('C · Estrés tipo NEM', 'Compresión desde 2027', '10,0', '2029',
        'Replica el precedente australiano: spread −85% en un año al pasar la flota BESS de 4.360 a 9.000 MW.')]
c.setFont('SGB', 8.2)
c.setFillColor(GREY)
c.drawString(M, y, 'ESCENARIO')
c.drawString(M + 190, y, 'SPREAD 2035')
c.drawString(M + 285, y, 'CRUZA EL BREAK-EVEN')
y -= 16
for nm, ini, sp35, cr, just in esc:
    txt(M, y, nm, 'SGB', 10, INK)
    txt(M + 190, y, sp35, 'SG', 10, INK)
    txt(M + 285, y, cr, 'SGB', 10, GREEN if 'no cruza' in cr else (RED if cr == '2029' else AMBER))
    y -= 13
    txt(M, y, ini, 'SG', 8.2, GREYL)
    y -= 13
    yn = para(M + 12, y, just, 'SGI', 8.6, GREY, CW - 24, 12.5)
    y = yn - 9
y -= 4

# Como se lee el break-even
CH3 = 104
card(M, y - CH3, CW, CH3)
ty = y - 22
txt(M + 20, ty, 'Cómo se lee la holgura', 'SGB', 10.5, INK)
ty -= 18
for t in ['El spread observado en los últimos 12 meses completos es 77,5 USD/MWh.',
          'A 340 ciclos, cubrir un servicio de deuda de US$400 mil requiere 43,9 USD/MWh.',
          'El spread tendría que caer un 43% antes de comprometer el servicio de la deuda.',
          'En esa misma ventana, el 88% de los días superó los 40 USD/MWh de spread.']:
    txt(M + 20, ty, '·  ' + t, 'SG', 9.4, INK)
    ty -= 15
y -= CH3 + 14
txt(M, y, 'Los supuestos de deuda son editables en la calculadora; ninguna cifra de DSCR es válida '
    'hasta cargar el term sheet real.', 'SGI', 8.2, GREYL)
y -= 20

# Grafico de escenarios. El titulo va ARRIBA para no competir con el pie de pagina.
txt(M, y, 'Spread proyectado por escenario · la línea roja punteada es el break-even de 43,9 USD/MWh',
    'SGB', 8.4, GREY)
y -= 10

CHART = make_chart()
from PIL import Image as _Im
_w, _h = _Im.open(CHART).size
BOTTOM = 70                      # limite inferior: deja aire sobre el pie de pagina
avail_h = y - BOTTOM
iw = CW
ih = iw * _h / _w
if ih > avail_h:                 # si no cabe, se reduce manteniendo la proporcion
    ih = avail_h
    iw = ih * _w / _h
c.drawImage(CHART, M + (CW - iw) / 2, y - ih, width=iw, height=ih, mask='auto')
print(f'  grafico: PNG {_w}x{_h} -> {iw:.0f}x{ih:.0f} pt · espacio disponible {avail_h:.0f} pt')

foot(2)
c.showPage()

# ══════════════════════════════════════════ PAGINA 3 · CON Y SIN PPA
eyebrow(H - 62, 'el PPA de compra a 28 usd/mwh  ·  cuánto cuesta')
y = H - 100
c.setFont('SGL', 26)
c.setFillColor(INK)
c.drawString(M, y, 'Cuánto se gana con PPA y cuánto sin PPA.')
y -= 24
y = para(M, y, 'Resultado real del nodo en los últimos doce meses completos bajo las dos alternativas. '
         'Para que la comparación sea justa, al PPA se le concede su mejor política de operación: con un '
         'costo de carga fijo conviene ciclar todos los días, incluso aquellos en que el spread spot es '
         'delgado. Aun así pierde.', 'SG', 10.5, GREY, CW, 16)
y -= 14

# Tabla comparativa
CHP = 158
card(M, y - CHP, CW, CHP)
ty = y - 22
XA, XB, XC, XD = M + 20, M + 300, M + 400, M + 479
for lb, cx, al in [('', XA, 'l'), ('Sin PPA · a spot', XB, 'r'),
                   ('Con PPA a 28', XC, 'r'), ('Diferencia', XD, 'r')]:
    if lb:
        txt(cx, ty, lb, 'SGB', 8.2, GREY, al)
ty -= 6
rule(ty, M + 20, W - M - 20, GREEN, 0.9)
ty -= 17
cmpr = [('Ciclos completos en el año', '340', '365', '+25', GREY),
        ('Ingreso por venta nocturna', '997.905', '1.086.101', '+88.196', GREY),
        ('Costo de la energía de carga', '183.167', '367.920', '+184.753', RED),
        ('Costo de carga implícito', '15,0', '28,0', '+13,0', RED)]
for k, a, b, dd, dcol in cmpr:
    txt(XA, ty, k, 'SG', 9.4, INK)
    txt(XB, ty, a, 'SG', 9.4, INK, 'r')
    txt(XC, ty, b, 'SG', 9.4, INK, 'r')
    txt(XD, ty, dd, 'SG', 9.4, dcol, 'r')
    ty -= 17
ty -= 3
rule(ty + 6, M + 20, W - M - 20, GREEN, 0.9)
txt(XA, ty - 6, 'Margen bruto del año', 'SGB', 10.2, INK)
txt(XB, ty - 6, '814.738', 'SGB', 10.2, GREEN, 'r')
txt(XC, ty - 6, '718.181', 'SGB', 10.2, INK, 'r')
txt(XD, ty - 6, '−96.557', 'SGB', 10.2, RED, 'r')
ty -= 22
txt(XA, ty, 'US$ salvo donde se indique · ventana de 12 meses completos, 23-may-2025 a 22-may-2026',
    'SGI', 7.4, GREYL)
y -= CHP + 18

# El saldo, en verde
CHG = 82
card(M, y - CHG, CW, CHG, GREENBG, GREENL)
ty = y - 24
txt(M + 20, ty, 'El PPA cuesta US$97 mil al año. En diez años de deuda, US$966 mil.', 'SGB', 12, GREEN)
ty -= 19
para(M + 20, ty, 'Con el PPA el proyecto cicla 25 veces más y captura US$88 mil más de ingreso — pero '
     'paga US$185 mil más por la energía de carga. El saldo son 11,9% menos de margen.',
     'SG', 9.8, INK, CW - 40, 14)
y -= CHG + 20

# Sensibilidad
txt(M, y, '¿Y si el PPA fuera más barato?', 'SGB', 12.5, INK)
y -= 18
y = para(M, y, 'La conclusión no depende del precio ofertado. Evaluado entre 22 y 34 USD/MWh, y dándole '
         'a cada caso su política óptima de operación, el PPA de compra no gana en ningún punto del rango.',
         'SG', 10, INK, CW, 15)
y -= 10
XS = [M + 20, M + 250, M + 360, M + 460, M + 479]
txt(XS[0], y, 'PRECIO DEL PPA', 'SGB', 8, GREY)
txt(XS[1], y, 'MARGEN CON PPA', 'SGB', 8, GREY, 'r')
txt(XS[2], y, 'MARGEN SIN PPA', 'SGB', 8, GREY, 'r')
txt(XS[3], y, 'VENTAJA DEL SPOT', 'SGB', 8, GREY, 'r')
y -= 6
rule(y, M, W - M, HAIR, 0.7)
y -= 16
for pr, mp_, dif, cur in [('22 USD/MWh', '797.021', '17.717', False),
                          ('25 USD/MWh', '757.601', '57.137', False),
                          ('28 USD/MWh · oferta actual', '718.181', '96.557', True),
                          ('31 USD/MWh', '678.761', '135.977', False),
                          ('34 USD/MWh', '639.341', '175.397', False)]:
    f = 'SGB' if cur else 'SG'
    txt(XS[0], y, pr, f, 9.4, INK)
    txt(XS[1], y, mp_, f, 9.4, INK, 'r')
    txt(XS[2], y, '814.738', f, 9.4, GREEN, 'r')
    txt(XS[3], y, dif, f, 9.4, INK, 'r')
    txt(W - M, y, 'No', 'SGB', 9.4, RED, 'r')
    y -= 16
y -= 6
y = para(M, y, 'El PPA de compra cubre el riesgo de que suba el precio de compra. El proyecto es una '
         'posición vendedora: su riesgo es que caiga el precio de venta nocturno. El contrato agrega un '
         'costo fijo sin cubrir un riesgo real del activo — y por eso no mejora a ningún precio mientras '
         'persista la saturación solar diurna.', 'SGI', 8.8, GREY, CW, 13)

foot(3)
c.showPage()

# ══════════════════════════════════════════ PAGINA 4
eyebrow(H - 62, 'qué contrato, y cuándo  ·  monitoreo')
y = H - 100
c.setFont('SGL', 26)
c.setFillColor(INK)
c.drawString(M, y, 'El contrato correcto, en su momento.')
y -= 24
y = para(M, y, 'Decir "no PPA ahora, reevaluar hacia 2030" suena contradictorio. No lo es: son dos '
         'contratos distintos que hoy se llaman igual.', 'SG', 10.5, GREY, CW, 16)
y -= 16

# Dos columnas comparativas
cw2 = (CW - 16) / 2
CH4 = 202
card(M, y - CH4, cw2, CH4, REDBG, HexColor('#f4c7c7'))
card(M + cw2 + 16, y - CH4, cw2, CH4, GREENBG, GREENL)
for x, tit, col, items, verd in [
    (M, 'PPA de COMPRA a 28 USD/MWh', RED,
     [('Qué fija', 'El precio al que el proyecto compra su energía de carga'),
      ('Riesgo que cubre', 'Que suba el precio de compra'),
      ('¿Es el riesgo real?', 'No. El proyecto es posición vendedora'),
      ('Efecto', 'Destruye ~US$83 mil/año de margen')],
     'Rechazar de forma permanente,\nno "por ahora"'),
    (M + cw2 + 16, 'Instrumento de VENTA · 2030–2032', GREEN,
     [('Qué fija', 'El precio al que el proyecto vende en la noche'),
      ('Riesgo que cubre', 'Que caiga el precio de venta'),
      ('¿Es el riesgo real?', 'Sí. Es exactamente el riesgo del activo'),
      ('Efecto', 'Estabiliza el margen y la caja')],
     'Negociar desde el año 1,\nfirmar entre 2030 y 2032')]:
    ty = y - 22
    for ln in wrap(tit, 'SGB', 10, cw2 - 32):
        txt(x + 16, ty, ln, 'SGB', 10, col)
        ty -= 13
    ty -= 5
    for k, v in items:
        txt(x + 16, ty, k, 'SGB', 8, GREY)
        ty -= 11
        for ln in wrap(v, 'SG', 8.8, cw2 - 32):
            txt(x + 16, ty, ln, 'SG', 8.8, INK)
            ty -= 11
        ty -= 4
    ty -= 2
    rule(ty, x + 16, x + cw2 - 16, col, 0.8)
    ty -= 13
    for ln in verd.split('\n'):
        txt(x + 16, ty, ln, 'SGB', 9, col)
        ty -= 11
y -= CH4 + 30

# La brecha locacional
txt(M, y, 'Por qué la ventana existe: la brecha es locacional, no temporal', 'SGB', 12, INK)
y -= 18
y = para(M, y, 'El almacenamiento en Chile es real y avanza rápido: 2.283 MW en operación y 6.358 MW '
         'en construcción. Pero está concentrado en el norte — Antofagasta 44%, Atacama 23%, Tarapacá '
         '13,6% — y el Maule no figura en el desglose oficial. La Comisión Nacional de Energía proyecta '
         'que el desacople de costos marginales de la zona sur persiste hacia 2032 incluso con las obras '
         'de 500 kV previstas.', 'SG', 10, INK, CW, 15.5)
y -= 16

# Gatillos
txt(M, y, 'La decisión se monitorea, no se apuesta', 'SGB', 12, INK)
y -= 18
y = para(M, y, 'Seis gatillos con métrica, fuente, umbral y acción predefinida, revisados '
         'trimestralmente: compresión del spread, erosión del piso nocturno, alza del costo de carga, '
         'MW de almacenamiento en operación en el centro-sur, entrada de obras de transmisión y '
         'cobertura de deuda. El precedente australiano —spread −85% en un año— es la razón por la que '
         'la revisión es trimestral y no anual.', 'SG', 10, INK, CW, 15.5)
y -= 18

rule(y)
y -= 16
txt(M, y, 'FUENTES', 'SGB', 8, GREY)
y -= 13
for s in ['Coordinador Eléctrico Nacional, Real Definitivo · nodo BA S/E Panimávida 13,2 kV (BP1) · '
          '38.064 horas, 2022–2026',
          'Comisión Nacional de Energía · Informe Final Plan de Expansión de la Transmisión 2026',
          'CNE · Norma Técnica de Conexión y Operación de PMGD, 19-feb-2026 · ACERA · Energy-Storage.News']:
    for ln in wrap(s, 'SG', 7.8, CW):
        txt(M, y, ln, 'SG', 7.8, GREYL)
        y -= 10

foot(4)

out = (r'C:\Users\nicol\OneDrive\Documentos\0.2.Rho\Banco_Panimavida'
       r'\entrega_banco_v8\Panimavida_Brochure_v8.pdf')
os.makedirs(os.path.dirname(out), exist_ok=True)
c._filename = out
c.save()
print('OK ->', out, os.path.getsize(out), 'bytes')
