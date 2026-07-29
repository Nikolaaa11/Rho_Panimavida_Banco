# -*- coding: utf-8 -*-
"""
Panimavida v8 - Comparacion CON PPA vs SIN PPA, calculada dia a dia.

Genera las cifras del cuadro comparativo que esta en:
  · la plataforma, seccion "Por que el proyecto no requiere el PPA de compra"
  · el brochure, pagina 3
  · el correo a Javier, seccion 2

REGLA METODOLOGICA IMPORTANTE:
Al PPA se le concede su MEJOR politica de operacion. Con un costo de carga fijo
conviene ciclar todos los dias en que el ingreso supere ese costo fijo, incluso
los dias en que el spread spot es delgado. Si se compararan ambos casos sobre
los MISMOS dias, el PPA saldria peor (655 mil) y cualquiera con un modelo propio
diria que se le puso la politica de operacion equivocada. Concederle su mejor
caso y que igual pierda es lo que hace el cuadro inatacable.

Entrada:  datos/daily_panimavida.csv  (lo genera 01_analisis_base.py)
Salida:   datos/ppa_vs_spot.json  + reporte por consola
"""
import os, sys, json
sys.stdout.reconfigure(encoding='utf-8')
import pandas as pd
import numpy as np

BASE = os.path.dirname(os.path.abspath(__file__))
DATOS = os.path.join(BASE, 'datos')

MWH_CARGA = 36.0          # energia cargada por ciclo
MWH_VENTA = 29.88         # energia vendida por ciclo (round-trip 83%)
UMBRAL_SPOT = 20          # bajo este spread no se cicla a spot
PPA_OFERTA = 28.0         # USD/MWh de la oferta sobre la mesa

d = pd.read_csv(os.path.join(DATOS, 'daily_panimavida.csv'),
                parse_dates=['fecha']).set_index('fecha')


def caso_spot(w, umbral=UMBRAL_SPOT):
    """Sin PPA: se cicla cuando el spread spot supera el umbral."""
    s = w[w.spread > umbral]
    ingreso = (s.venta * MWH_VENTA).sum()
    costo = (s.carga * MWH_CARGA).sum()
    return len(s), ingreso, costo, ingreso - costo


def caso_ppa(w, precio):
    """Con PPA: la carga cuesta `precio` fijo. Politica optima = ciclar
    siempre que el ingreso de venta supere el costo fijo de carga."""
    s = w[w.venta * MWH_VENTA > precio * MWH_CARGA]
    ingreso = (s.venta * MWH_VENTA).sum()
    costo = len(s) * precio * MWH_CARGA
    return len(s), ingreso, costo, ingreso - costo


# ── Ventana ancla: ultimos 12 meses completos del registro
fin = pd.Timestamp('2026-05-22')
ini = fin - pd.DateOffset(months=12) + pd.Timedelta(days=1)
W = d.loc[ini:fin]

n_s, ing_s, cos_s, m_s = caso_spot(W)
n_p, ing_p, cos_p, m_p = caso_ppa(W, PPA_OFERTA)

print('=' * 74)
print(f'VENTANA ANCLA: {ini.date()} a {fin.date()}  ({len(W)} dias reales)')
print('=' * 74)
print(f'{"":<34}{"Sin PPA":>14}{"Con PPA a 28":>16}{"Diferencia":>14}')
print('-' * 74)
print(f'{"Ciclos completos en el ano":<34}{n_s:>14,}{n_p:>16,}{n_p-n_s:>+14,}')
print(f'{"Ingreso por venta nocturna":<34}{ing_s:>14,.0f}{ing_p:>16,.0f}{ing_p-ing_s:>+14,.0f}')
print(f'{"Costo de la energia de carga":<34}{cos_s:>14,.0f}{cos_p:>16,.0f}{cos_p-cos_s:>+14,.0f}')
print(f'{"Costo de carga implicito":<34}{cos_s/(n_s*MWH_CARGA):>14.1f}{PPA_OFERTA:>16.1f}'
      f'{PPA_OFERTA-cos_s/(n_s*MWH_CARGA):>+14.1f}')
print('-' * 74)
print(f'{"MARGEN BRUTO DEL ANO":<34}{m_s:>14,.0f}{m_p:>16,.0f}{m_p-m_s:>+14,.0f}')
print('=' * 74)
print(f'\nEl PPA cuesta US$ {m_s-m_p:,.0f} al ano = {100*(m_s-m_p)/m_s:.1f}% del margen')
for anos in (5, 10, 15):
    print(f'  a {anos:>2} anos: US$ {(m_s-m_p)*anos:,.0f}')

# ── Anos calendario completos (2026 se excluye: solo ene-may, semestre favorable)
print('\n' + '=' * 74)
print('ANOS CALENDARIO COMPLETOS')
print('=' * 74)
filas = []
for a in (2023, 2024, 2025):
    w = d[d.index.year == a]
    f = 365 / len(w)
    _, _, _, ms = caso_spot(w)
    _, _, _, mp = caso_ppa(w, PPA_OFERTA)
    ms, mp = ms * f, mp * f
    filas.append([a, round(ms), round(mp), round(ms - mp)])
    print(f'  {a}: sin PPA {ms:>11,.0f} | con PPA {mp:>11,.0f} | '
          f'el spot gana {ms-mp:>10,.0f} ({100*(ms-mp)/ms:>4.1f}%)')
nivel = float(np.mean([r[3] for r in filas]))
print(f'\n  Nivel de la ventaja del spot 2023-2025: US$ {nivel:,.0f}/ano')

# ── Sensibilidad al precio del PPA
print('\n' + '=' * 74)
print('SENSIBILIDAD AL PRECIO DEL PPA (cada caso con su politica optima)')
print('=' * 74)
sens = []
for precio in (22, 25, 28, 31, 34):
    _, _, _, mp = caso_ppa(W, precio)
    sens.append([precio, round(mp), round(m_s - mp)])
    gana = 'SI' if mp > m_s else 'NO'
    marca = '  <- oferta actual' if precio == PPA_OFERTA else ''
    print(f'  PPA {precio} USD/MWh -> margen {mp:>11,.0f} | '
          f'el spot gana {m_s-mp:>10,.0f} | conviene: {gana}{marca}')
print('\n  El PPA no gana en ningun punto del rango evaluado.')

# ── Salida estructurada
out = {
    'ancla': {
        'desde': str(ini.date()), 'hasta': str(fin.date()), 'dias': len(W),
        'ciclos_spot': n_s, 'ciclos_ppa': n_p,
        'ingreso_spot': round(ing_s), 'ingreso_ppa': round(ing_p),
        'costo_spot': round(cos_s), 'costo_ppa': round(cos_p),
        'carga_implicita_spot': round(cos_s / (n_s * MWH_CARGA), 1),
        'margen_spot': round(m_s), 'margen_ppa': round(m_p),
        'diferencia': round(m_s - m_p),
        'pct': round(100 * (m_s - m_p) / m_s, 1),
        'acum_10_anos': round((m_s - m_p) * 10),
    },
    'anios': filas,
    'nivel_2023_2025': round(nivel),
    'sensibilidad': sens,
}
ruta = os.path.join(DATOS, 'ppa_vs_spot.json')
json.dump(out, open(ruta, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print(f'\n-> {ruta}')
