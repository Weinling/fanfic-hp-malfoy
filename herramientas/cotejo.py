"""Busca tramos de texto compartidos entre la traducción oficial y un capítulo nuestro.

Uso: python3 herramientas/cotejo.py OFICIAL.md NUESTRO.md [n=4]

Normaliza comillas, mayúsculas y puntuación, busca n-gramas de palabras comunes
y los une en tramos. Ignora tramos hechos solo de palabras vacías.
"""
import re
import sys

VACIAS = set("""a an the and or but of to in on at for with by from as is was were be been
it its it's he she his her him they them their you your i me my we our us that this
there here not no do did does had has have would could will just so if then than""".split())


def palabras(texto):
    texto = texto.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    texto = texto.lower().replace("dad", "father").replace("lyra", "malfoy").replace("carina", "malfoy")
    return re.findall(r"[a-z']+", texto)


def tramos(a, b, n):
    indice = {}
    for i in range(len(b) - n + 1):
        indice.setdefault(tuple(b[i:i + n]), []).append(i)
    vistos, salida = set(), []
    for i in range(len(a) - n + 1):
        if i in vistos or tuple(a[i:i + n]) not in indice:
            continue
        j = indice[tuple(a[i:i + n])][0]
        k = n
        while i + k < len(a) and j + k < len(b) and a[i + k] == b[j + k]:
            k += 1
        vistos.update(range(i, i + k))
        tramo = a[i:i + k]
        if sum(p not in VACIAS for p in tramo) >= 2:
            salida.append(" ".join(tramo))
    return salida


if __name__ == "__main__":
    n = int(sys.argv[3]) if len(sys.argv) > 3 else 4
    oficial = palabras(open(sys.argv[1], encoding="utf-8").read())
    nuestro = palabras(open(sys.argv[2], encoding="utf-8").read())
    for t in sorted(set(tramos(oficial, nuestro, n)), key=len, reverse=True):
        print(f"[{len(t.split())}] {t}")
