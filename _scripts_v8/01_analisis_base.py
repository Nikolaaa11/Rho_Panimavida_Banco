import openpyxl, numpy as np, pandas as pd, sys, json
sys.stdout.reconfigure(encoding='utf-8')

import os as _os
_BASE = _os.path.dirname(_os.path.abspath(__file__))
_DATOS = _os.path.join(_BASE, 'datos')


SRC = _os.path.join(_DATOS, 'FUENTE_Panimavida_Utilidades_BESS.xlsx')
wb = openpyxl.load_workbook(SRC, data_only=True, read_only=True)
ws = wb['Datos_CMg']
rows=[]
for i,r in enumerate(ws.iter_rows(min_row=2, values_only=True)):
    if r[0] is None: continue
    rows.append((r[0], r[1], r[2]))
wb.close()
df = pd.DataFrame(rows, columns=['fecha','hora','cmg'])
df['fecha']=pd.to_datetime(df['fecha'].astype(str))
df['cmg']=pd.to_numeric(df['cmg'], errors='coerce')
df['anio']=df['fecha'].dt.year
df['mes']=df['fecha'].dt.month
print('FILAS:', len(df), '| rango:', df.fecha.min().date(), '->', df.fecha.max().date())
print('nulos cmg:', df.cmg.isna().sum())
print('horas por anio:'); print(df.groupby('anio').size())

SOLAR = list(range(9,18))     # 09-17 banda carga
NOCHE = list(range(19,24)) + list(range(0,8))  # 19-23 + 00-07

def daily(g):
    s = g[g.hora.isin(SOLAR)].cmg.dropna().values
    n = g[g.hora.isin(NOCHE)].cmg.dropna().values
    if len(s)<4 or len(n)<4: return None
    carga = np.sort(s)[:4].mean()
    venta = np.sort(n)[-4:].mean()
    return pd.Series({'carga':carga,'venta':venta,'spread':venta-carga,
                      'horas0_solar':int((g[g.hora.isin(SOLAR)].cmg==0).sum())})

d = df.groupby('fecha', group_keys=False).apply(daily, include_groups=False).dropna()
d['anio']=d.index.year; d['mes']=d.index.month
print('\nDIAS:', len(d))

print('\n===== A) RESULTADO ANUAL (recalculo independiente) =====')
ann = d.groupby('anio').agg(dias=('spread','size'), carga=('carga','mean'),
    venta=('venta','mean'), spread=('spread','mean'),
    sp_p10=('spread',lambda x: np.percentile(x,10)),
    sp_p50=('spread','median'), sp_p90=('spread',lambda x: np.percentile(x,90)))
print(ann.round(1).to_string())
base = ann.loc[2023:2026]
print('\nBase 23-26 (promedio simple de anios): carga=%.1f venta=%.1f spread=%.1f' % (
    base.carga.mean(), base.venta.mean(), base.spread.mean()))

print('\n===== B) SESGO 2026: comparacion like-for-like ENE-MAY =====')
lfl = d[d.mes<=5].groupby('anio').agg(carga=('carga','mean'), venta=('venta','mean'), spread=('spread','mean'), dias=('spread','size'))
print(lfl.round(1).to_string())
print('\n-- mismo, solo JUN-DIC (2026 no tiene) --')
print(d[d.mes>5].groupby('anio').agg(carga=('carga','mean'),venta=('venta','mean'),spread=('spread','mean')).round(1).to_string())

print('\n===== C) TENDENCIA DEL PICO NOCTURNO: se esta comprimiendo? =====')
print('Venta 4h noche por anio (ENE-MAY, comparable):')
for a in sorted(lfl.index): print(f'  {a}: {lfl.loc[a,"venta"]:.1f} USD/MWh')
import numpy as np
yy = lfl.index.values.astype(float); vv = lfl.venta.values
sl = np.polyfit(yy,vv,1)[0]
print(f'  Pendiente lineal ENE-MAY: {sl:+.1f} USD/MWh por anio')
ss = np.polyfit(yy, lfl.spread.values,1)[0]
print(f'  Pendiente spread ENE-MAY: {ss:+.1f} USD/MWh por anio')

print('\n===== D) SPREAD MENSUAL (estacionalidad) =====')
piv = d.pivot_table(index='mes', columns='anio', values='spread', aggfunc='mean')
print(piv.round(0).to_string())

print('\n===== E) DIAS OPERABLES: distribucion del spread diario =====')
for a in sorted(d.anio.unique()):
    x=d[d.anio==a]
    print(f'  {a}: dias={len(x)} | spread>40: {100*(x.spread>40).mean():.0f}% | >60: {100*(x.spread>60).mean():.0f}% | >80: {100*(x.spread>80).mean():.0f}% | min={x.spread.min():.0f} max={x.spread.max():.0f}')

print('\n===== F) MARGEN POR NUMERO DE CICLOS (base 23-26) =====')
POT, DUR, EFF = 9, 4, 36/36
MWH_C = 36.0            # carga por ciclo
MWH_V = 36.0*0.83       # venta por ciclo (round-trip 83% implicita del informe)
print(f'  Carga/ciclo={MWH_C:.1f} MWh · Venta/ciclo={MWH_V:.2f} MWh')
db = d.loc['2023':'2026']
for nc in [182, 250, 300, 330, 365]:
    top = db.nlargest(min(nc, len(db)), 'spread') if nc<len(db) else db
    # margen usando los mejores nc dias/anio  -> escalamos por anio
    parts=[]
    for a in sorted(db.anio.unique()):
        x=db[db.anio==a]
        k=min(nc, len(x))
        sel=x.nlargest(k,'spread')
        marg=(sel.venta*MWH_V - sel.carga*MWH_C).sum()
        # anualizar 2026 parcial
        factor = 365/len(x) if len(x)<300 else 1.0
        parts.append((a, marg, marg*factor, len(x), k))
    prom = np.mean([p[2] for p in parts if p[0]!=2026])
    prom_all = np.mean([p[2] for p in parts])
    print(f'  {nc} ciclos/anio -> margen bruto medio 23-25: US$ {prom:,.0f}/anio | incl.2026 anualiz.: US$ {prom_all:,.0f}')

print('\n===== G) VERIFICACION del caso 182 ciclos del informe =====')
cb, vb = base.carga.mean(), base.venta.mean()
ing = 5460*vb; cos = 6570*cb
print(f'  Informe: carga={cb:.1f} venta={vb:.1f} -> ingreso={ing:,.0f} costo={cos:,.0f} margen={ing-cos:,.0f}')
print(f'  Sobrecosto PPA 28: {6570*(28-cb):,.0f} US$/anio')
print(f'  Ciclos implicitos: {6570/36:.0f} ciclos/anio ({100*6570/36/365:.0f}% de utilizacion diaria)')

d.to_csv(_os.path.join(_DATOS, 'daily_panimavida.csv'))
print('\n-> guardado datos/daily_panimavida.csv')
