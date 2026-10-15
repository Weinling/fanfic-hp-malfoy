"""Compara cada capítulo antes y después del cotejo, y los dos contra la oficial.

Uso:
  python3 -I herramientas/comparar.py              # todos los capítulos
  python3 -I herramientas/comparar.py 1 2 yo1      # solo esos
  python3 -I herramientas/comparar.py --base REV   # otra referencia (por defecto, 888ff27: lo publicado antes del cotejo)

Por capítulo da:
  - parecido con la versión de referencia (difflib, 0 a 1) y palabras cambiadas;
  - tramos compartidos con la oficial (de 6 palabras o más, y palabras que cubren), antes y después.
La oficial se busca en referencia/oficial-en/ según MAPA; si falta, esas columnas salen con «—».
"""
import difflib, os, re, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cotejo import palabras, tramos

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OFICIAL = os.path.join(RAIZ, "referencia", "oficial-en")

# capítulo nuestro -> archivos oficiales (coreanos) que le corresponden
MAPA = {
    "1": ["cap-01-prologo.md"], "2": ["ko-02.md"], "3": ["ko-03.md"], "4": ["ko-04.md"],
    "5": ["ko-05.md"], "6": ["ko-06.md"], "7": [], "8": ["ko-07.md"], "9": ["ko-08.md"],
    "10": ["ko-09.md"], "11": ["ko-10.md"], "12": [], "13": ["ko-11.md"],
    "14": ["ko-12.md"], "15": [], "16": ["ko-12.md", "ko-13.md"], "17": ["ko-14.md"],
    "18": ["ko-15.md"], "19": ["ko-16.md", "ko-17.md"], "yo1": ["ko-18.md"],
    "20": ["ko-19.md"], "21": ["ko-20.md", "ko-21.md"], "22": ["ko-21.md", "ko-22.md"],
    "23": ["ko-23.md"], "yo2": ["ko-24.md"], "yo3": ["ko-25.md"], "yo4": ["ko-26.md"],
    "24": ["ko-27.md"], "25": ["ko-28.md", "ko-30.md"], "26": ["ko-29.md"],
    "27": ["ko-30.md"], "28": ["ko-31.md"], "29": ["ko-32.md"], "30": ["ko-33.md"],
}
ORDEN = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15",
         "16", "17", "18", "19", "yo1", "20", "21", "22", "23", "yo2", "yo3", "yo4",
         "24", "25", "26", "27", "28", "29", "30"]


def ruta_capitulo(clave):
    """Ruta actual del capítulo (manuscrito o borradores), sin fichas ni notas."""
    if clave.startswith("yo"):
        patron = re.compile(rf"extra-year-one-{clave[2:]}-(?!ficha).*\.md$")
        carpetas = ["borradores", "manuscrito"]
    else:
        patron = re.compile(rf"cap-{int(clave):02d}-(?!ficha|lector|recorte|critica).*\.md$")
        carpetas = ["manuscrito", "borradores"]
    for carpeta in carpetas:
        d = os.path.join(RAIZ, carpeta)
        for nombre in sorted(os.listdir(d)):
            if patron.match(nombre):
                return f"{carpeta}/{nombre}"
    return None


def texto_en(rev, ruta):
    """Texto del archivo en una revisión; si se movió de carpeta, prueba la otra."""
    nombre = os.path.basename(ruta)
    for r in (ruta, f"borradores/{nombre}", f"manuscrito/{nombre}"):
        try:
            return subprocess.run(["git", "-C", RAIZ, "show", f"{rev}:{r}"],
                                  capture_output=True, text=True, check=True).stdout
        except subprocess.CalledProcessError:
            continue
    return None


def cuerpo(texto):
    return re.findall(r"\S+", texto)


def solape(oficial, nuestro):
    largos = [t for t in tramos(oficial, palabras(nuestro), 6)]
    return len(largos), sum(len(t.split()) for t in largos)


def main(args):
    base = "888ff27"  # lo publicado antes del cotejo (etiqueta local antes-del-cotejo, si existe)
    if "--base" in args:
        i = args.index("--base"); base = args[i + 1]; del args[i:i + 2]
    claves = [a.lower() for a in args] or ORDEN
    print(f"Referencia: {base}\n")
    print(f"{'cap':>4} {'parecido':>8} {'cambiadas':>9} {'palabras':>8} | {'oficial antes':>14} {'oficial ahora':>14}")
    for clave in claves:
        ruta = ruta_capitulo(clave)
        if not ruta:
            print(f"{clave:>4}  (no encontrado)"); continue
        ahora = open(os.path.join(RAIZ, ruta), encoding="utf-8").read()
        antes = texto_en(base, ruta) or ""
        a, b = cuerpo(antes), cuerpo(ahora)
        m = difflib.SequenceMatcher(None, a, b, autojunk=False)
        iguales = sum(bl.size for bl in m.get_matching_blocks())
        cambiadas = max(len(a), len(b)) - iguales
        ofi = [os.path.join(OFICIAL, f) for f in MAPA.get(clave, [])]
        ofi = [f for f in ofi if os.path.exists(f)]
        if ofi:
            o = palabras("\n".join(open(f, encoding="utf-8").read() for f in ofi))
            n1, p1 = solape(o, antes); n2, p2 = solape(o, ahora)
            col = f"{n1:>4} tr/{p1:>5} p {n2:>4} tr/{p2:>5} p"
        else:
            col = f"{'—':>14} {'—':>14}"
        print(f"{clave:>4} {m.ratio():>8.3f} {cambiadas:>9} {len(b):>8} | {col}")


if __name__ == "__main__":
    main(sys.argv[1:])
