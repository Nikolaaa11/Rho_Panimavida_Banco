import pandas as pd, numpy as np, sys
sys.stdout.reconfigure(encoding='utf-8')

import os as _os
_BASE = _os.path.dirname(_os.path.abspath(__file__))
_DATOS = _os.path.join(_BASE, 'datos')

d = pd.read_csv(_os.path.join(_DATOS,'daily_panimavida.csv'), parse_dates=['fecha']).set_index('fecha')
d['anio']=d.index.year; d['mes']=d.index.month

print('===== 1) INTEGRIDAD: dias faltantes por anio =====')
for a in sorted(d.anio.unique()):
    x=d[d.anio==a]; esp = 142 if a==2026 else (366 if a%4==0 else 365)
    print(f'  {a}: {len(x)} dias de {esp} esperados  -> faltan {esp-len(x)}')
g24 = pd.date_range('2024-01-01','2024-12-31')
falt = [t.date() for t in g24 if t not in d.index]
print(f'  2024 faltantes: {falt[:20]}{" ..." if len(falt)>20 else ""}')

print('\n===== 2) ESTACIONALIDAD: factor semestral (Jun-Dic / Ene-May) =====')
fs={}
for a in [2023,2024,2025]:
    h1=d[(d.anio==a)&(d.mes<=5)].spread.mean(); h2=d[(d.anio==a)&(d.mes>5)].spread.mean()
    fs[a]=h2/h1; print(f'  {a}: Ene-May={h1:.1f}  Jun-Dic={h2:.1f}  factor={h2/h1:.3f}')
fac=np.mean(list(fs.values())); print(f'  Factor medio Jun-Dic/Ene-May = {fac:.3f}')
s26=d[d.anio==2026].spread.mean(); v26=d[d.anio==2026].venta.mean(); c26=d[d.anio==2026].carga.mean()
n1,n2=151,214
s26_full=(n1*s26+n2*s26*fac)/365; v26_full=(n1*v26+n2*v26*fac)/365
print(f'\n  >> 2026 medido (Ene-May): spread={s26:.1f}  venta={v26:.1f}  carga={c26:.1f}')
print(f'  >> 2026 ESTIMADO ano completo: spread={s26_full:.1f} (venta~{v26_full:.1f})')
print(f'  >> El informe usa {s26:.1f}: SESGO AL ALZA de +{s26-s26_full:.1f} USD/MWh en 2026')
base_rep=np.mean([d[d.anio==a].spread.mean() for a in [2023,2024,2025,2026]])
base_adj=np.mean([d[d.anio==a].spread.mean() for a in [2023,2024,2025]]+[s26_full])
print(f'  >> Base 23-26 informe={base_rep:.1f} | ajustada estacionalmente={base_adj:.1f}')

print('\n===== 3) DESCOMPOSICION: que lado mueve el spread? (Ene-May comparable) =====')
lfl=d[d.mes<=5].groupby('anio')[['carga','venta','spread']].mean()
print(lfl.round(1).to_string())
b=lfl.loc[2023]
print('\n  Cambio vs 2023 (Ene-May):')
for a in [2024,2025,2026]:
    r=lfl.loc[a]
    print(f'   {a}: venta {r.venta-b.venta:+.1f} | carga {r.carga-b.carga:+.1f} (carga baja = AYUDA) | spread neto {r.spread-b.spread:+.1f}')
print('\n  Interpretacion: la caida del spread se explica por el lado VENTA;')
print('  el lado CARGA compenso parcialmente (energia de carga cada vez mas barata).')

print('\n===== 4) PISO DEL PRECIO NOCTURNO (se derrumba o tiene suelo?) =====')
print('  Percentiles del precio de venta 4h noche, por anio (Ene-May comparable):')
for a in sorted(lfl.index):
    x=d[(d.anio==a)&(d.mes<=5)].venta
    print(f'   {a}: P10={np.percentile(x,10):6.1f}  P25={np.percentile(x,25):6.1f}  P50={np.percentile(x,50):6.1f}  P75={np.percentile(x,75):6.1f}')
print('\n  Dias con venta < 50 USD/MWh (Ene-May):')
for a in sorted(lfl.index):
    x=d[(d.anio==a)&(d.mes<=5)]
    print(f'   {a}: {100*(x.venta<50).mean():.0f}% de los dias | <40: {100*(x.venta<40).mean():.0f}% | <30: {100*(x.venta<30).mean():.0f}%')

print('\n===== 5) SPREAD MOVIL 12 MESES (metrica de trigger) =====')
m = d.spread.resample('MS').mean()
roll = m.rolling(12).mean().dropna()
print('  Ultimos 18 valores del spread movil 12M:')
for t,v in roll.tail(18).items(): print(f'   {t.date()}: {v:.1f}')
print(f'\n  Maximo historico movil12M: {roll.max():.1f} ({roll.idxmax().date()})')
print(f'  Ultimo movil12M: {roll.iloc[-1]:.1f} ({roll.index[-1].date()})')
print(f'  Caida desde el maximo: {100*(roll.iloc[-1]/roll.max()-1):+.0f}%')
r2=roll[roll.index>='2024-06-01']
yy=np.arange(len(r2)); sl=np.polyfit(yy,r2.values,1)[0]*12
print(f'  Pendiente movil12M desde jun-2024: {sl:+.1f} USD/MWh por anio  <-- tendencia reciente')

print('\n===== 6) MARGEN BRUTO ANUAL a distintos ciclos, dia-a-dia (para escenarios) =====')
MC,MV=36.0,29.88
for a in sorted(d.anio.unique()):
    x=d[d.anio==a]; f=365/len(x)
    out=[]
    for nc in [182,250,300]:
        k=min(nc,len(x)) if len(x)>=300 else min(int(nc*len(x)/365),len(x))
        sel=x.nlargest(k,'spread'); marg=(sel.venta*MV-sel.carga*MC).sum()*f if len(x)<300 else (x.nlargest(nc,'spread').venta*MV-x.nlargest(nc,'spread').carga*MC).sum()
        out.append(f'{nc}c=US${marg:,.0f}')
    print(f'  {a}: '+' | '.join(out))

print('\n===== 7) BREAK-EVEN: spread minimo por nivel de servicio de deuda =====')
print('  Margen bruto anual = ciclos x (venta x 29,88 - carga x 36)')
print('  Aprox: si carga~12 USD/MWh, margen/ciclo = venta*29,88 - 432')
for nc in [182,250,300]:
    print(f'\n  A {nc} ciclos/anio:')
    for ds in [200_000,300_000,400_000,500_000]:
        # venta necesaria
        vn=(ds/nc+432)/29.88
        print(f'    servicio deuda US${ds:,} -> requiere venta media {vn:5.1f} USD/MWh (spread ~{vn-12:5.1f})')
