"""Densidad y tics por capítulo, antes y después (encargo del crítico de la ronda 3).

Uso:
  python3 -I herramientas/densidad.py              # todos los capítulos
  python3 -I herramientas/densidad.py 1 2 9 10     # solo esos
  python3 -I herramientas/densidad.py --base REV   # otra referencia (por defecto, 888ff27)
  python3 -I herramientas/densidad.py --largos 9   # lista los párrafos de más de 80 palabras del 9

Por capítulo, en la referencia y ahora:
  - palabras;
  - % de párrafos de más de 80 y de más de 120 palabras (sin contar los ⁂);
  - «as though» y «as if» por cada mil palabras;
  - «very» por cada mil palabras, y cuántos van en el narrador (fuera de comillas).
"""
import os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from comparar import ORDEN, ruta_capitulo, texto_en

DIALOGO = re.compile(r"“[^”]*”")


def parrafos(texto):
    salida = []
    for p in re.split(r"\n\s*\n", texto):
        p = p.strip()
        if not p or p == "⁂" or p.startswith("#"):
            continue
        salida.append(p)
    return salida


def n_palabras(t):
    return len(re.findall(r"[A-Za-z’']+", t))


def medidas(texto):
    ps = parrafos(texto)
    tam = [n_palabras(p) for p in ps]
    total = sum(tam) or 1
    narr = DIALOGO.sub(" ", texto)
    low = texto.lower()
    return {
        "pal": total,
        "p80": 100 * sum(t > 80 for t in tam) / max(len(ps), 1),
        "p120": 100 * sum(t > 120 for t in tam) / max(len(ps), 1),
        "asif": 1000 * len(re.findall(r"\bas (?:though|if)\b", low)) / total,
        "very": 1000 * len(re.findall(r"\bvery\b", low)) / total,
        "very_n": len(re.findall(r"\bvery\b", narr.lower())),
        "very_t": len(re.findall(r"\bvery\b", low)),
    }


def main(args):
    base = "888ff27"
    if "--base" in args:
        i = args.index("--base"); base = args[i + 1]; del args[i:i + 2]
    if "--largos" in args:
        i = args.index("--largos"); clave = args[i + 1]
        ruta = ruta_capitulo(clave)
        texto = open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ruta), encoding="utf-8").read()
        for p in parrafos(texto):
            n = n_palabras(p)
            if n > 80:
                print(f"[{n}] {p[:110]}…")
        return
    claves = args or ORDEN
    raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(f"{'cap':>4} | {'palabras':>13} | {'%>80':>11} | {'%>120':>11} | {'as if/1000':>11} | {'very/1000':>11} | very narr.")
    for c in claves:
        ruta = ruta_capitulo(c)
        if not ruta:
            continue
        ahora = medidas(open(os.path.join(raiz, ruta), encoding="utf-8").read())
        viejo_t = texto_en(base, ruta)
        antes = medidas(viejo_t) if viejo_t else None
        def par(k, fmt="{:.1f}"):
            a = fmt.format(antes[k]) if antes else "—"
            return f"{a:>5}→{fmt.format(ahora[k]):>5}"
        print(f"{c:>4} | {par('pal', '{:d}'):>13} | {par('p80'):>11} | {par('p120'):>11} | {par('asif'):>11} | {par('very'):>11} | {ahora['very_n']}/{ahora['very_t']}")


if __name__ == "__main__":
    main(sys.argv[1:])
