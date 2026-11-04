# Cotejo automático: frases de N palabras que un capítulo nuestro comparte con la oficial.
# Uso: python3 -I ngramas.py 5 "nuestro1.md,nuestro2.md" "oficial1.md,oficial2.md"
# Filtra las coincidencias con menos de tres palabras con contenido. Las frases cortas
# (de dos a cuatro palabras, como «A useful enemy») hay que buscarlas además con grep.

import re, sys, glob, os
N = int(sys.argv[1])
ours = sys.argv[2].split(',')
offs = sys.argv[3].split(',')
def toks(path):
    t = open(path, encoding='utf-8').read()
    t = t.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"')
    return re.findall(r"[a-z']+", t.lower())
off = {}
for p in offs:
    w = toks(p)
    for i in range(len(w)-N+1):
        off.setdefault(' '.join(w[i:i+N]), os.path.basename(p))
stop = set("the of and to a in that was it he she i you his her had be not for on with as at but have is this they would what so".split())
for p in ours:
    w = toks(p)
    hits = []
    i = 0
    while i < len(w)-N+1:
        g = ' '.join(w[i:i+N])
        if g in off and sum(1 for x in w[i:i+N] if x not in stop) >= 3:
            j = i+N
            while j < len(w) and ' '.join(w[j-N+1:j+1]) in off: j += 1
            hits.append((' '.join(w[i:j]), off[g]))
            i = j
        else:
            i += 1
    print('==', os.path.basename(p), len(hits))
    for h in hits: print('   ', h[1], '|', h[0])
