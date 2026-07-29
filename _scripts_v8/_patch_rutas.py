# -*- coding: utf-8 -*-
"""Hace que todos los scripts usen rutas relativas al propio directorio,
para que la carpeta funcione tal cual en cualquier equipo.
Se corre UNA vez; es idempotente."""
import io, os, sys
sys.stdout.reconfigure(encoding='utf-8')

BASE = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE)

PRE = (
    "\nimport os as _os\n"
    "_BASE = _os.path.dirname(_os.path.abspath(__file__))\n"
    "_DATOS = _os.path.join(_BASE, 'datos')\n"
)

FUENTE_OLD = "SRC = r'C:" + chr(92) + "Users" + chr(92) + "nicol" + chr(92) + \
             "Downloads" + chr(92) + "Panimavida_Utilidades_BESS (1).xlsx'"
FUENTE_NEW = "SRC = _os.path.join(_DATOS, 'FUENTE_Panimavida_Utilidades_BESS.xlsx')"

PATCHES = {
    '01_analisis_base.py': [
        (FUENTE_OLD, FUENTE_NEW),
        ("d.to_csv('daily_panimavida.csv')",
         "d.to_csv(_os.path.join(_DATOS, 'daily_panimavida.csv'))"),
        ("print('\\n-> guardado daily_panimavida.csv')",
         "print('\\n-> guardado datos/daily_panimavida.csv')"),
    ],
    '02_analisis_estacionalidad.py': [
        ("pd.read_csv('daily_panimavida.csv'",
         "pd.read_csv(_os.path.join(_DATOS,'daily_panimavida.csv')"),
    ],
    '04_build_excel_ventana.py': [],
    '05_verify_excel.py': [
        ("WORK = os.path.dirname(os.path.abspath(__file__))",
         "WORK = _os.path.join(_BASE, '_tmp_verify')\nos.makedirs(WORK, exist_ok=True)"),
    ],
    '06_build_brochure_pdf.py': [
        ("CHART = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bro_chart.png')",
         "CHART = _os.path.join(_DATOS, 'bro_chart.png')"),
        ("out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bro_chart.png')",
         "out = _os.path.join(_DATOS, 'bro_chart.png')"),
    ],
    '07_build_brochure_word.py': [
        ("CHART = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bro_chart.png')",
         "CHART = _os.path.join(_DATOS, 'bro_chart.png')"),
    ],
    '08_transcribir_audios.py': [],
}

for fn, subs in PATCHES.items():
    if not os.path.exists(fn):
        print(f'  {fn}: NO EXISTE'); continue
    s = io.open(fn, encoding='utf-8').read()
    orig = s
    if '_BASE = _os.path' not in s:
        lines = s.split('\n')
        ins = 0
        for i, l in enumerate(lines[:30]):
            if l.startswith(('import ', 'from ')) or l.startswith('sys.stdout'):
                ins = i + 1
        lines.insert(ins, PRE)
        s = '\n'.join(lines)
    hit = 0
    for old, new in subs:
        if old in s:
            s = s.replace(old, new); hit += 1
    io.open(fn, 'w', encoding='utf-8').write(s)
    est = 'sin cambios' if s == orig else f'{hit}/{len(subs)} rutas + preambulo'
    print(f'  {fn}: {est}')

# limpiar el CSV que quedo suelto en la raiz por una corrida anterior
suelto = os.path.join(BASE, 'daily_panimavida.csv')
if os.path.exists(suelto):
    os.remove(suelto)
    print('  limpiado: daily_panimavida.csv suelto en la raiz')
print('\nlisto')
