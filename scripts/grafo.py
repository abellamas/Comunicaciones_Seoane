import json, csv, sys
S='/tmp/claude-0/-home-user-TP1-MIC-Cappello-Lamas-Varela/6b889c66-861f-5cea-9d3e-6f1a9a54b59d/scratchpad/fichas'
CSV='/home/user/TP1_MIC_Cappello_Lamas_Varela/clases_comunicaciones.csv'

bloques=[
 ("b1","Transmisión, atenuación y propagación","Unidades logarítmicas, atenuación de espacio libre, antenas, propagación y líneas de transmisión."),
 ("b2","Fundamentos de señales y sistemas","Clasificación, energía y potencia de señales, análisis de Fourier, convolución, ancho de banda y filtros."),
 ("b3","Ruido","Tipos y fuentes de ruido, ruido térmico y blanco, figura y temperatura de ruido de cuadripolos en cascada y SNR."),
 ("b4","Información y capacidad","Cantidad y tasa de información, velocidad de señalización con señales M-arias y capacidad de canal de Shannon."),
 ("b5","Muestreo, cuantificación y PCM","Teorema de muestreo, muestreo real, cuantificación uniforme y no uniforme, PCM y códigos de línea."),
 ("b6","Multiplexación","Multiplexación por división de tiempo (TDM, PAM) y de frecuencia (FDM)."),
 ("b7","Modulación lineal (DSB y AM)","Por qué modular, DSB sin portadora, AM con portadora, índice de modulación y demodulación sincrónica o por envolvente."),
 ("b8","Receptores","Receptor de AM: selectividad con filtros resonantes, receptor superheterodino y control automático de ganancia."),
 ("b9","Modulación angular (FM/PM)","Definición de FM y PM, índice de modulación, espectro por funciones de Bessel y ancho de banda de Carson."),
]
# (nombre normalizado, bloque, [nombres originales en fichas])
temas_def=[
 ("Atenuación y decibeles","b1",["Atenuación y decibeles"]),
 ("Atenuación de espacio libre","b1",["Atenuación de espacio libre"]),
 ("Antenas (directividad y área efectiva)","b1",["Antenas (directividad y área efectiva)"]),
 ("Propagación y línea de vista","b1",["Propagación y línea de vista"]),
 ("Líneas de transmisión","b1",["Líneas de transmisión"]),
 ("Espectro electromagnético","b1",["Espectro electromagnético"]),
 ("Señales y espectro","b2",["Señales y espectro"]),
 ("Clasificación de señales","b2",["Clasificación de señales"]),
 ("Energía y potencia de señales","b2",["Energía y potencia de señales"]),
 ("Serie de Fourier","b2",["Serie de Fourier"]),
 ("Transformada de Fourier","b2",["Transformada de Fourier"]),
 ("Teorema de Parseval / Rayleigh","b2",["Teorema de Parseval / Rayleigh"]),
 ("Convolución","b2",["Convolución"]),
 ("Ancho de banda","b2",["Ancho de banda"]),
 ("Filtros","b2",["Filtros"]),
 ("Ruido (tipos y fuentes)","b3",["Ruido (tipos y fuentes)"]),
 ("Compatibilidad electromagnética","b3",["Compatibilidad electromagnética"]),
 ("Ruido térmico","b3",["Ruido térmico"]),
 ("Ruido blanco","b3",["Ruido blanco"]),
 ("Ruido en cuadripolos","b3",["Cuadripolos"]),
 ("Ancho de banda equivalente de ruido","b3",["Ancho de banda equivalente de ruido"]),
 ("Figura de ruido (fórmula de Friis)","b3",["Figura de ruido"]),
 ("Temperatura equivalente de ruido","b3",["Temperatura de ruido"]),
 ("Relación señal a ruido (SNR)","b3",["Relación señal a ruido (SNR)"]),
 ("Información y entropía","b4",["Información y entropía"]),
 ("Tasa de información","b4",["Tasa de información"]),
 ("Velocidad de señalización (baudios)","b4",["Velocidad de señalización (baudios)"]),
 ("Señales M-arias","b4",["Señales M-arias"]),
 ("Capacidad de canal (Shannon)","b4",["Capacidad de canal (Shannon)"]),
 ("Teorema de muestreo (Nyquist)","b5",["Teorema de muestreo (Nyquist)"]),
 ("Aliasing","b5",["Aliasing"]),
 ("Muestreo natural y flat-top","b5",["Muestreo natural y flat-top"]),
 ("Cuantificación uniforme","b5",["Cuantificación"]),
 ("Ruido de cuantificación","b5",["Ruido de cuantificación"]),
 ("Cuantificación no uniforme (companding, leyes A y μ)","b5",["Cuantificación no uniforme (companding)"]),
 ("PCM","b5",["PCM"]),
 ("Codificación de línea","b5",["Codificación de línea"]),
 ("Sincronismo","b5",["Sincronismo"]),
 ("PAM","b6",["PAM"]),
 ("Multiplexación por división de tiempo (TDM)","b6",["Multiplexación (TDM)"]),
 ("Multiplexación por división de frecuencia (FDM)","b6",["Multiplexación (FDM)"]),
 ("Modulación lineal y AM","b7",["Modulación lineal (AM)"]),
 ("Doble banda lateral sin portadora (DSB)","b7",["DSB"]),
 ("Índice de modulación (AM)","b7",[]),
 ("Demodulación / detección","b7",["Demodulación / detección"]),
 ("Receptor superheterodino","b8",["Receptor superheterodino"]),
 ("Control automático de ganancia (AGC)","b8",["Control automático de ganancia (AGC)"]),
 ("Modulación angular (FM/PM)","b9",["Modulación angular (FM/PM)"]),
 ("Índice de modulación (FM)","b9",[]),
 ("Ancho de banda de FM (Carson)","b9",["Ancho de banda de FM (Carson)"]),
]
ejer_def=[
 ("Unidades logarítmicas (dB, dBm)","b1",["Atenuación y decibeles"],["Unidades logarítmicas (dB, dBm)"]),
 ("Ganancia de cuadripolos en cascada (dB)","b1",["Atenuación y decibeles"],["Ganancia de cuadripolos en cascada (dB)"]),
 ("Atenuación de espacio libre / enlace radioeléctrico","b1",["Atenuación de espacio libre","Antenas (directividad y área efectiva)"],["Atenuación de espacio libre / enlace radioeléctrico"]),
 ("SNR en enlaces con repetidores","b1",["Relación señal a ruido (SNR)","Propagación y línea de vista"],["SNR en enlaces con repetidores (cascada)"]),
 ("Longitud de onda y dimensionado de antenas (dipolo λ/2)","b1",["Antenas (directividad y área efectiva)","Espectro electromagnético"],["Longitud de onda y dimensionado de antenas (dipolo λ/2)"]),
 ("Potencia normalizada (señales de energía y potencia)","b2",["Energía y potencia de señales"],["Potencia normalizada / señales de energía y potencia"]),
 ("Espectro de pulsos (serie y transformada de Fourier)","b2",["Serie de Fourier","Transformada de Fourier"],["Serie/Transformada de Fourier (espectro de pulsos)"]),
 ("Energía en el espectro (Parseval, primer lóbulo)","b2",["Teorema de Parseval / Rayleigh"],["Energía en el espectro (Parseval, primer lóbulo)"]),
 ("Espectros por convolución (pulso trapezoidal/triangular)","b2",["Convolución","Transformada de Fourier"],["Convolución (pulso trapezoidal/triangular)"]),
 ("Modulación por producto (traslación espectral)","b2",["Transformada de Fourier"],["Modulación por producto (traslación espectral)"]),
 ("Ruido térmico (kT, kTB)","b3",["Ruido térmico","Ruido blanco"],["Ruido térmico (densidad espectral kT, potencia kTB)"]),
 ("Ancho de banda equivalente de ruido","b3",["Ancho de banda equivalente de ruido"],["Ancho de banda equivalente de ruido"]),
 ("Figura de ruido / temperatura de ruido","b3",["Figura de ruido (fórmula de Friis)","Temperatura equivalente de ruido"],["Figura de ruido / temperatura de ruido"]),
 ("Cascada de amplificadores (Friis)","b3",["Figura de ruido (fórmula de Friis)","Temperatura equivalente de ruido"],["Cascada de amplificadores (ruido)"]),
 ("Cálculo de SNR","b3",["Relación señal a ruido (SNR)"],["Cálculo de SNR"]),
 ("Cantidad de información de un mensaje/símbolo","b4",["Información y entropía"],["Cantidad de información de un mensaje/símbolo"]),
 ("Tasa de información de una imagen/señal","b4",["Tasa de información"],["Tasa de información de una imagen/señal"]),
 ("Capacidad de canal (Shannon)","b4",["Capacidad de canal (Shannon)"],["Capacidad de canal (Shannon)"]),
 ("Velocidad de señalización (baudios) vs tasa de bits","b4",["Velocidad de señalización (baudios)","Tasa de información"],["Velocidad de señalización (baudios) vs tasa de bits"]),
 ("Bits por símbolo (señales M-arias)","b4",["Señales M-arias"],["Bits por símbolo (señales M-arias, sistemas de numeración)"]),
 ("Muestreo y aliasing (fs y filtro antialias)","b5",["Teorema de muestreo (Nyquist)","Aliasing"],["Muestreo y aliasing (frecuencia de muestreo y filtro antialias)"]),
 ("Muestreo flat-top (efecto de apertura)","b5",["Muestreo natural y flat-top"],["Muestreo flat-top (efecto de apertura)"]),
 ("Frecuencia de muestreo del CD (44,1 kHz)","b5",["Teorema de muestreo (Nyquist)","Muestreo natural y flat-top"],["Frecuencia de muestreo del CD (cálculo de 44,1 kHz)"]),
 ("Cuantificación (niveles, error, dígitos por muestra)","b5",["Cuantificación uniforme"],["Cuantificación (niveles, error de cuantificación, dígitos por muestra)"]),
 ("SNR de cuantificación (6 dB por bit)","b5",["Ruido de cuantificación"],["SNR de cuantificación (6 dB por bit)"]),
 ("Cuantificación no uniforme","b5",["Cuantificación no uniforme (companding, leyes A y μ)"],["Cuantificación no uniforme"]),
 ("Codificación binaria (signo y magnitud)","b5",["PCM","Cuantificación uniforme"],["Codificación binaria (signo y magnitud, sistemas de numeración)"]),
 ("PCM (tasa de bits, niveles)","b5",["PCM","Tasa de información"],["PCM (tasa de bits, niveles de cuantificación)"]),
 ("Conversión paralelo-serie (duración de bit)","b5",["PCM","Multiplexación por división de tiempo (TDM)"],["Conversión paralelo-serie / TDM (duración de bit)"]),
 ("Ancho de banda de una señal PCM/binaria","b5",["PCM","Ancho de banda","Codificación de línea"],["Ancho de banda de una señal PCM/binaria"]),
 ("Multiplexación TDM/FDM","b6",["Multiplexación por división de tiempo (TDM)","Multiplexación por división de frecuencia (FDM)"],["Multiplexación TDM/FDM"]),
 ("DSB/SSB (espectro, modulación y demodulación sincrónica)","b7",["Doble banda lateral sin portadora (DSB)","Demodulación / detección"],["DSB/SSB (espectro, modulación y demodulación sincrónica)"]),
 ("Modulación AM (potencia, índice, espectro)","b7",["Modulación lineal y AM","Índice de modulación (AM)"],["Modulación AM (potencia, índice, espectro)"]),
 ("Selectividad: factor Q de filtros pasabanda","b8",["Filtros","Receptor superheterodino"],["Factor de selectividad Q (filtros pasabanda)"]),
 ("Receptor superheterodino (oscilador local, FI, frecuencia imagen)","b8",["Receptor superheterodino"],["Receptor superheterodino (oscilador local, FI, frecuencia imagen)"]),
 ("Modulación FM/PM (índice, ancho de banda de Carson)","b9",["Modulación angular (FM/PM)","Índice de modulación (FM)","Ancho de banda de FM (Carson)"],["Modulación FM/PM (índice de modulación, ancho de banda Carson)"]),
 ("Espectro de FM con funciones de Bessel","b9",["Modulación angular (FM/PM)","Índice de modulación (FM)"],["Espectro de FM con funciones de Bessel (potencia por banda lateral)"]),
]
tid={}; temas=[]
for i,(nom,b,orig) in enumerate(temas_def,1):
    t=f"t{i}"; tid[nom]=t; temas.append({"id":t,"nombre":nom,"bloque":b})
orig2t={o:tid[nom] for nom,b,orig in temas_def for o in orig}
eid={}; ejercicios=[]; orig2e={}
for i,(nom,b,ts,orig) in enumerate(ejer_def,1):
    e=f"e{i}"; eid[nom]=e; ejercicios.append({"id":e,"nombre":nom,"bloque":b,"temas":[tid[x] for x in ts]})
    for o in orig: orig2e[o]=e
tblock={t["id"]:t["bloque"] for t in temas}

R=lambda a,b,tp="prerrequisito": {"de":tid[a],"a":tid[b],"tipo":tp}
U="se usa en"
relaciones=[
 R("Atenuación y decibeles","Atenuación de espacio libre"),
 R("Antenas (directividad y área efectiva)","Atenuación de espacio libre"),
 R("Atenuación y decibeles","Figura de ruido (fórmula de Friis)",U),
 R("Atenuación de espacio libre","Relación señal a ruido (SNR)",U),
 R("Espectro electromagnético","Antenas (directividad y área efectiva)"),
 R("Señales y espectro","Serie de Fourier"),
 R("Serie de Fourier","Transformada de Fourier"),
 R("Energía y potencia de señales","Teorema de Parseval / Rayleigh"),
 R("Transformada de Fourier","Teorema de Parseval / Rayleigh"),
 R("Transformada de Fourier","Ancho de banda"),
 R("Convolución","Transformada de Fourier",U),
 R("Transformada de Fourier","Filtros"),
 R("Ruido térmico","Ruido blanco"),
 R("Ruido blanco","Ancho de banda equivalente de ruido"),
 R("Ruido en cuadripolos","Ancho de banda equivalente de ruido"),
 R("Ruido en cuadripolos","Figura de ruido (fórmula de Friis)"),
 R("Figura de ruido (fórmula de Friis)","Temperatura equivalente de ruido"),
 R("Ruido térmico","Relación señal a ruido (SNR)"),
 R("Relación señal a ruido (SNR)","Capacidad de canal (Shannon)"),
 R("Ancho de banda","Capacidad de canal (Shannon)"),
 R("Información y entropía","Tasa de información"),
 R("Velocidad de señalización (baudios)","Tasa de información",U),
 R("Señales M-arias","Velocidad de señalización (baudios)",U),
 R("Transformada de Fourier","Teorema de muestreo (Nyquist)"),
 R("Convolución","Teorema de muestreo (Nyquist)",U),
 R("Filtros","Teorema de muestreo (Nyquist)",U),
 R("Teorema de muestreo (Nyquist)","Aliasing"),
 R("Teorema de muestreo (Nyquist)","Muestreo natural y flat-top"),
 R("Teorema de muestreo (Nyquist)","PCM"),
 R("Cuantificación uniforme","Ruido de cuantificación"),
 R("Ruido de cuantificación","Cuantificación no uniforme (companding, leyes A y μ)"),
 R("Cuantificación uniforme","PCM"),
 R("Tasa de información","PCM",U),
 R("PCM","Codificación de línea"),
 R("Codificación de línea","Sincronismo",U),
 R("Teorema de muestreo (Nyquist)","PAM"),
 R("PAM","Multiplexación por división de tiempo (TDM)",U),
 R("PCM","Multiplexación por división de tiempo (TDM)",U),
 R("Sincronismo","Multiplexación por división de tiempo (TDM)",U),
 R("Transformada de Fourier","Doble banda lateral sin portadora (DSB)"),
 R("Antenas (directividad y área efectiva)","Modulación lineal y AM",U),
 R("Doble banda lateral sin portadora (DSB)","Modulación lineal y AM"),
 R("Doble banda lateral sin portadora (DSB)","Demodulación / detección"),
 R("Sincronismo","Demodulación / detección",U),
 R("Modulación lineal y AM","Índice de modulación (AM)"),
 R("Modulación lineal y AM","Multiplexación por división de frecuencia (FDM)",U),
 R("Modulación lineal y AM","Receptor superheterodino"),
 R("Filtros","Receptor superheterodino",U),
 R("Control automático de ganancia (AGC)","Receptor superheterodino",U),
 R("Modulación lineal y AM","Modulación angular (FM/PM)"),
]
relaciones=relaciones[:50]
# --- clases
rows=list(csv.DictReader(open(CSV,encoding='utf-8-sig')))
# misma clase (verificado por solapamiento de transcripciones y fichas)
pares={2:1,3:1,6:5,7:5,9:8,10:8,13:12,14:12,15:12,18:17,19:17,23:22,24:21,29:28,30:28,34:33,35:32,40:39,41:39,48:47,52:51}
inv={}
for b,a in sorted(pares.items()): inv.setdefault(a,b)
main={**{n:"b1" for n in (1,2,3)},4:"b2",11:"b2",20:"b2",**{n:"b3" for n in (5,6,7,8,9,10,12,13,14,15,16)},
      **{n:"b4" for n in (17,18,19)},**{n:"b5" for n in list(range(21,37))+[39,40,41,42,55]},
      44:"b6",45:"b7",49:"b7",50:"b7",51:"b8",52:"b8",38:"b9",53:"b9",
      37:"H1",43:"H1",46:"H1",47:"H1",48:"H1",54:"H2",56:"H2"}
clases=[]
for r in rows:
    n=int(r['N']); te=json.load(open(f"{S}/teoria/{n:02d}.json")); ej=json.load(open(f"{S}/ejercicios/{n:02d}.json"))
    assert te['n']==n==ej['n']
    ts=[]
    for o in te['temas']:
        if o=="Índice de modulación": t=tid["Índice de modulación (FM)"] if n in (38,53) else tid["Índice de modulación (AM)"]
        else: t=orig2t[o]
        if t not in ts: ts.append(t)
    es=[]
    for o in ej['tipos']:
        e=orig2e[o]
        if e not in es: es.append(e)
    anio=int(r['fecha_clase'][-4:])
    clases.append({"n":n,"fecha":r['fecha_clase'],"anio":anio,"playlist":r['playlist'],"pos":int(r['posicion_playlist']),
      "titulo":r['titulo'],"link":r['link'],"tipo":te['tipo'],"resumen":te['resumen'],"detalle":te['detalle'],
      "temas":ts,"ejercicios":es,"referencias":ej['referencias'],"misma_clase_que":pares.get(n,inv.get(n))})
C={c['n']:c for c in clases}
def cursada(c): return f"{c['anio']} {c['playlist']}" if c['anio']==2024 else str(c['anio'])
CURS=["2024 A","2024 B","2025","2026"]
tname={t['id']:t['nombre'] for t in temas}; ename={e['id']:e['nombre'] for e in ejercicios}

def cover(cands,targets,key):
    left=set(targets); chosen=[]
    while left:
        best=max(cands,key=lambda n:(len(left&set(key(C[n]))),len(C[n]['detalle']),-n),default=None)
        if best is None or not (left&set(key(C[best]))): break
        chosen.append(best); left-=set(key(C[best])); cands=[x for x in cands if x!=best]
    return sorted(chosen)

linea=[]
# la teoría introductoria se recomienda aunque otra clase cubra los mismos temas
FORZAR={('b9','2025'):[38,53],('b7','2025'):[45,49]}
def bloque_entry(b):
    bt=[t['id'] for t in temas if t['bloque']==b]
    recs=[]; opts={}
    for cu in CURS:
        cands=[n for n in C if main[n]==b and cursada(C[n])==cu]
        ch=FORZAR.get((b,cu)) or cover(cands,bt,lambda c:c['temas'])
        if ch: opts[cu]=ch
    def score(cu):
        cov=set().union(*[C[n]['temas'] for n in opts[cu]])&set(bt)
        return (len(cov),sum(len(C[n]['detalle']) for n in opts[cu]),-len(opts[cu]))
    princ=max(opts,key=score) if opts else None
    for cu in CURS:
        for n in opts.get(cu,[]):
            cov=[tname[t] for t in C[n]['temas'] if t in bt]
            recs.append({"n":n,"cursada":cu,"principal":cu==princ,"motivo":"Cubre: "+", ".join(cov)+"."})
    recn={x['n'] for x in recs}
    otras=sorted(n for n in C if n not in recn and (main[n]==b or set(C[n]['temas'])&set(bt)))
    return {"bloque":b,"temas":bt,"clases_recomendadas":recs,"otras_clases":otras,"hito":None}
def hito_entry(h,nombre):
    bl=[x for x in main if main[x]==h]
    recs=[]; opts={}
    for cu in CURS:
        cands=[n for n in bl if cursada(C[n])==cu]
        allE=set().union(*[C[n]['ejercicios'] for n in cands]) if cands else set()
        ch=cover(cands,allE,lambda c:c['ejercicios'])
        if ch: opts[cu]=ch
    princ=max(opts,key=lambda cu:(len(set().union(*[C[n]['ejercicios'] for n in opts[cu]])),-len(opts[cu])))
    for cu in CURS:
        for n in opts.get(cu,[]):
            c=C[n]; m=("Resolución del parcial" if 'Resolución' in c['titulo'] else "Repaso con ejercicios")+f" ({len(c['ejercicios'])} tipos de ejercicio)."
            recs.append({"n":n,"cursada":cu,"principal":cu==princ,"motivo":m})
    recn={x['n'] for x in recs}
    return {"bloque":None,"hito":nombre,"temas":[],"clases_recomendadas":recs,"otras_clases":sorted(n for n in bl if n not in recn)}
for b,_,_ in bloques[:5]: linea.append(bloque_entry(b))
linea.append(hito_entry("H1","Repaso y 1er parcial"))
for b,_,_ in bloques[5:]: linea.append(bloque_entry(b))
linea.append(hito_entry("H2","Repaso y 2do parcial"))
# motivos más claros para clases que repiten otra grabación
for e in linea:
    for r in e['clases_recomendadas']:
        m=C[r['n']]['misma_clase_que']
        if m and r['cursada']=="2024 B": r['motivo']+=f" Otra grabación de la clase n.º {m}."
out={"bloques":[{"id":b,"nombre":nm,"orden":i,"descripcion":d} for i,(b,nm,d) in enumerate(bloques,1)],
     "temas":temas,"ejercicios":ejercicios,"relaciones":relaciones,"clases":clases,"linea_de_tiempo":linea}
json.dump(out,open(f"{S}/grafo.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print(len(bloques),len(temas),len(ejercicios),len(relaciones))
for e in linea:
    print(e.get('bloque') or e['hito'],[(r['n'],r['cursada'],'*' if r['principal'] else '') for r in e['clases_recomendadas']],e['otras_clases'])
