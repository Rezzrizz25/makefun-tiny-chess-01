import json,os
from urllib.request import*
E=os.getenv('MAKEFUN_ENV_URL')
P=lambda p,b:json.load(urlopen(Request(E+p,data=json.dumps(b).encode())))
V={'P':100,'N':320,'B':330,'R':500,'Q':900,'K':0}
T={p:[(ord(c)-75)*5 for c in s] for p,s in zip('PNBRQK',['KKKKKKKKUUUUUUUUMMOQQOMMLLMPPMLLKKKOOKKKLJIKKIJLLMMGGMMLKKKKKKKK','ACEEEECACGKKKKGCEKMNNMKEELNOONLEEKNOONKEELMNNMLECGKLLKGCACEEEECA','GIIIIIIGIKKKKKKIIKLMMLKIILLMMLLIIKMMMMKIIMMMMMMIILKKKKLIGIIIIIIG','KKKKKKKKLMMMMMMLJKKKKKKJJKKKKKKJJKKKKKKJJKKKKKKJJKKKKKKJKKKLLKKK','GIIJJIIGIKKKKKKIIKLLLLKIJKLLLLKJKKLLLLKJILLLLLKIIKLKKKKIGIIJJIIG','ECCAACCEECCAACCEECCAACCEECCAACCEGEECCEEGIGGGGGGIOOKKKKOOOQMKKMQO'])}
BD=(-11,-9,9,11);RD=(-10,-1,1,10);KD=BD+RD;ND=(-21,-19,-12,-8,8,12,19,21)
Z={95:'KQ',98:'K',91:'Q',25:'kq',28:'k',21:'q'}
M=10000
def sq(i):return 'abcdefgh'[i%10-1]+str(10-i//10)
def ps(f):
 a=f.split()+['-']*4;b=list(' '*20+(' ........ ')*8+' '*20);r=2;i=21
 for ch in a[0]:
  if ch=='/':r+=1;i=r*10+1
  elif ch.isdigit():i+=int(ch)
  else:b[i]=ch;i+=1
 return b,a[1]=='w',a[2]
def ak(b,s,w):
 for o in (9,11)if w else(-11,-9):
  if b[s+o]==('P' if w else 'p'):return 1
 for d in ND:
  if b[s+d]==('N' if w else 'n'):return 1
 for d in KD:
  if b[s+d]==('K' if w else 'k'):return 1
 for d in BD+RD:
  j=s+d
  while b[j]!=' ':
   if b[j]!='.':
    if b[j]==('Q' if w else 'q') or b[j]==(('B' if w else 'b') if d in BD else ('R' if w else 'r')):return 1
    break
   j+=d
 return 0
il=lambda b,w:ak(b,b.index('K' if w else 'k'),not w)
def gn(b,w,c):
 for i,p in enumerate(b):
  if p==' ' or p=='.' or p.isupper()!=w:continue
  q=p.upper()
  if q=='P':
   d=-10 if w else 10;r=2 if w else 9
   if b[i+d]=='.':
    if (i+d)//10==r:
     for q in 'QRBN' if w else 'qrbn':yield i,i+d,q
    else:
     yield i,i+d,''
     if i//10==(8 if w else 3) and b[i+2*d]=='.':yield i,i+2*d,''
   for e in (-11,-9) if w else (11,9):
    j=i+e;t=b[j]
    if t not in ' .' and t.isupper()!=w:
     if j//10==r:
      for q in 'QRBN' if w else 'qrbn':yield i,j,q
     else:yield i,j,''
  elif q in 'BRQ':
   for d in BD+RD if q=='Q' else BD if q=='B' else RD:
    j=i+d
    while b[j]!=' ':
     if b[j]=='.':yield i,j,''
     else:
      if b[j].isupper()!=w:yield i,j,''
      break
     j+=d
  else:
   for d in ND if q=='N' else KD:
    j=i+d
    if b[j]!=' ' and (b[j]=='.' or b[j].isupper()!=w):yield i,j,''
   if q=='K':
    for k,r,t,e,f in ((95,'K',97,(96,),0),(95,'Q',93,(94,92),0),(25,'k',27,(26,),1),(25,'q',23,(24,22),1)):
     if i==k and r in c and all(b[x]=='.' for x in e+(t,)) and not ak(b,k,f) and not ak(b,e[0],f) and not ak(b,t,f):yield k,t,''
def ap(b,m):
 i,j,p=m;n=b[:];n[j]=p or n[i];n[i]='.'
 if b[i] in 'Kk' and abs(j-i)==2:
  if j>i:n[i+1],n[i+3]=n[i+3],'.'
  else:n[i-1],n[i-4]=n[i-4],'.'
 return n
def uc(c,m):
 for s in m[:2]:
  for r in Z.get(s,''):c=c.replace(r,'')
 return c
def ev(b,w):
 s=0
 for i,p in enumerate(b):
  if p not in ' .':
   u=p.upper();k=i%10-1+8*(i//10-2)
   s+=V[u]+T[u][k]if p.isupper()else-V[u]-T[u][63-k]
 return s if w else-s
cs=lambda b,m:(10*V[b[m[1]].upper()] if b[m[1]]!='.' else 0)+(100 if m[2] else 0)
def qs(b,w,a,be,q=6):
 if q==0:return ev(b,w)
 s=ev(b,w)
 if s>=be:return be
 if s>a:a=s
 for m in sorted(gn(b,w,''),key=lambda m:cs(b,m),reverse=True):
  if b[m[1]]=='.':continue
  n=ap(b,m)
  if il(n,w):continue
  s=-qs(n,not w,-be,-a,q-1)
  if s>=be:return be
  if s>a:a=s
 return a
def sr(b,w,c,d,a,be):
 if d==0:return qs(b,w,a,be)
 n=0
 for m in sorted(gn(b,w,c),key=lambda m:cs(b,m),reverse=True):
  x=ap(b,m)
  if il(x,w):continue
  n+=1;s=-sr(x,not w,uc(c,m),d-1,-be,-a)
  if s>=be:return be
  if s>a:a=s
 if not n:return -M-d if il(b,w) else 0
 return a
def bt(b,w,c,d):
 bm=None;a=-M
 for m in sorted(gn(b,w,c),key=lambda m:cs(b,m),reverse=True):
  x=ap(b,m)
  if il(x,w):continue
  s=-sr(x,not w,uc(c,m),d-1,-M,M)
  if s>a:a=s;bm=m
 return bm

g=P('/game',{})
while g['status']!='done':
 while g['status']=='your_move':
  b,w,c=ps(g['fen']);m=bt(b,w,c,3)
  g=P('/move',{'game':g['game'],'move':sq(m[0])+sq(m[1])+m[2].lower() if m else g['legal_moves'][0]})
 g=P('/game',{})
