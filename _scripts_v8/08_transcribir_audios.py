import os, sys, subprocess, time, gc
sys.stdout.reconfigure(encoding='utf-8')
from faster_whisper import WhisperModel

import os as _os
_BASE = _os.path.dirname(_os.path.abspath(__file__))
_DATOS = _os.path.join(_BASE, 'datos')


BASE = r'C:\Users\nicol\OneDrive\Documentos\0.2.Rho'
FILES = [
 ('A1_16.41.22',  'WhatsApp Audio 2026-07-29 at 16.41.22.ogg'),
 ('A2_16.41.222', 'WhatsApp Audio 2026-07-29 at 16.41.222.ogg'),
 ('A3_16.56.12',  'WhatsApp Audio 2026-07-29 at 16.56.12.mp4'),
]
LADDER = [('small',1),('base',1)]

# preparar wavs
wavs={}
for tag, fn in FILES:
    w=f'{tag}.wav'
    if not os.path.exists(w):
        subprocess.run(['ffmpeg','-y','-v','error','-i',os.path.join(BASE,fn),
                        '-ar','16000','-ac','1',w], check=True)
    wavs[tag]=w
print('wavs listos', flush=True)

for size, beam in LADDER:
    pend=[t for t,_ in FILES if not os.path.exists(f'{t}.txt')]
    if not pend: break
    print(f'\n### intento con modelo={size} beam={beam} · pendientes={pend}', flush=True)
    try:
        m = WhisperModel(size, device='cpu', compute_type='int8', cpu_threads=2)
    except Exception as e:
        print(f'  no se pudo cargar {size}: {e}', flush=True); continue
    for tag in pend:
        try:
            t0=time.time()
            print(f'  >>> {tag} ...', flush=True)
            segs,_ = m.transcribe(wavs[tag], language='es', beam_size=beam,
                                  vad_filter=True, condition_on_previous_text=False,
                                  vad_parameters=dict(min_silence_duration_ms=500))
            lines=[f'[{int(s.start//60):02d}:{int(s.start%60):02d}] {s.text.strip()}' for s in segs]
            open(f'{tag}.txt','w',encoding='utf-8').write('\n'.join(lines))
            print(f'  <<< {tag} OK · {len(lines)} seg · {time.time()-t0:.0f}s', flush=True)
        except Exception as e:
            print(f'  !!! {tag} fallo: {type(e).__name__}: {e}', flush=True)
        gc.collect()
    del m; gc.collect()

print('\n=== RESUMEN ===', flush=True)
for tag,_ in FILES:
    p=f'{tag}.txt'
    print(f'  {tag}: {"OK "+str(os.path.getsize(p))+" bytes" if os.path.exists(p) else "FALTA"}', flush=True)
