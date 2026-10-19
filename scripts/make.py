import re, csv, datetime as dt
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
S='/tmp/claude-0/-home-user-TP1-MIC-Cappello-Lamas-Varela/6b889c66-861f-5cea-9d3e-6f1a9a54b59d/scratchpad/'
OUT='/home/user/TP1_MIC_Cappello_Lamas_Varela/'
up={l.split()[0]:l.split()[1] for l in open(S+'ok2.txt')}
rows=[]
for pl in 'AB':
    for l in open(S+f'pl_{pl}.txt',encoding='utf-8'):
        pos,title,url,_=[x.strip() for x in l.rstrip('\n').split(' | ')]
        vid=url.split('=')[1]; u=up[vid]
        rows.append(dict(pl=pl,pos=int(pos),title=title,url=url,id=vid,upload=dt.date(int(u[:4]),int(u[4:6]),int(u[6:]))))
def parse(t):
    m=re.search(r'(?<!\d)(\d{4}) (\d{1,2}) (\d{1,2})(?!\d)',t)          # aaaa mm dd
    if m: return (int(m.group(1)),int(m.group(2)),int(m.group(3)))
    m=re.search(r'(?<!\d)(\d{1,2})([- ])(\d{1,2})\2(\d{4}|\d{2})(?!\d)',t)  # dd-mm-aaaa / dd mm aaaa
    if m: return (int(m.group(4)),int(m.group(3)),int(m.group(1)))
    return None
for r in rows:
    ymd=parse(r['title']); r['fuente']='título'; r['nota']=''
    t=r['title']
    if '30-29-2024' in t:
        r['fecha']=dt.date(2024,9,30); r['fuente']='título corregido'
        r['nota']='El título dice 30-29-2024 (mes inválido). Se corrigió a 30-09-2024, coincide con la fecha de subida (30-09-2024).'
    elif ymd and ymd[0]<100:
        r['fecha']=dt.date(2024,ymd[1],ymd[2]); r['fuente']='título corregido'
        r['nota']='El título dice 19-09-19 (año incompleto). Se tomó 19-09-2024: coincide con la Parte 1 y con la fecha de subida (19-09-2024).'
    elif ymd:
        r['fecha']=dt.date(*ymd)
    else:
        r['fecha']=r['upload']; r['fuente']='subida a YouTube'
        r['nota']='El título no tiene fecha. Se usó la fecha de subida a YouTube.'
rows.sort(key=lambda r:(r['fecha'].month,r['fecha'].day,r['fecha'].year,r['pl'],r['pos']))
for i,r in enumerate(rows,1): r['n']=i
f=lambda d:d.strftime('%d-%m-%Y')
with open(OUT+'clases_comunicaciones.csv','w',newline='',encoding='utf-8-sig') as fh:
    w=csv.writer(fh)
    w.writerow(['N','fecha_clase','origen_fecha','titulo','playlist','posicion_playlist','id','link','fecha_subida','nota'])
    for r in rows: w.writerow([r['n'],f(r['fecha']),r['fuente'],r['title'],r['pl'],r['pos'],r['id'],r['url'],f(r['upload']),r['nota']])
ss=getSampleStyleSheet()
cell=ParagraphStyle('c',parent=ss['BodyText'],fontName='Helvetica',fontSize=8,leading=10)
lnk=ParagraphStyle('l',parent=cell,textColor=colors.HexColor('#1a4fb5'))
hd=ParagraphStyle('h',parent=cell,fontName='Helvetica-Bold',textColor=colors.white)
doc=SimpleDocTemplate(OUT+'clases_comunicaciones.pdf',pagesize=landscape(A4),leftMargin=1.3*cm,rightMargin=1.3*cm,topMargin=1.3*cm,bottomMargin=1.3*cm,title='Clases de Comunicaciones (UNTREF)')
story=[Paragraph('Clases de Comunicaciones (UNTREF)',ss['Title']),
 Paragraph('Videos de las playlists A (canal "clases untref", 29 videos) y B (Lucas Pagniello, 27 videos), ordenados por día y mes de la clase; el año solo desempata. Fecha marcada con * = no sale tal cual del título (ver notas al final).',cell),Spacer(1,8)]
data=[[Paragraph(x,hd) for x in ['N°','Fecha','Título','Playlist','Link']]]
notes=[]
for r in rows:
    mark=''
    if r['nota']: notes.append((r['n'],r['nota'])); mark=' *'
    data.append([Paragraph(str(r['n']),cell),Paragraph(f(r['fecha'])+mark,cell),Paragraph(r['title'].replace('&','&amp;').replace('<','&lt;'),cell),
                 Paragraph(f"{r['pl']} (#{r['pos']})",cell),Paragraph(f'<link href="{r["url"]}">{r["url"]}</link>',lnk)])
t=Table(data,colWidths=[1.1*cm,2.5*cm,11.5*cm,2.2*cm,9.0*cm],repeatRows=1)
t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#33415c')),('VALIGN',(0,0),(-1,-1),'MIDDLE'),
 ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#f0f2f6')]),('GRID',(0,0),(-1,-1),0.3,colors.HexColor('#c5cad3'))]))
story+= [t,Spacer(1,12),Paragraph('<b>Notas</b>',cell)]
for n,txt in notes: story.append(Paragraph(f'N° {n}: {txt}',cell))
doc.build(story)
print(len(rows)); 
for r in rows: print(r['n'],f(r['fecha']),r['pl'],r['pos'],r['fuente'],'|',r['title'][:60])
