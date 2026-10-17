import re, sys, pathlib
src, outdir = sys.argv[1], pathlib.Path(sys.argv[2])
lines = pathlib.Path(src).read_text(encoding='utf-8').splitlines()
heads = [i for i,l in enumerate(lines) if re.match(r'^Capítulo \d+:', l)]
for k,i in enumerate(heads):
    m = re.match(r'^Capítulo (\d+): (.*)$', lines[i]); n, title = int(m.group(1)), m.group(2).strip().rstrip('_')
    end = heads[k+1] if k+1 < len(heads) else len(lines)
    body = lines[i+1:end]
    # quitar las líneas de ==== que rodean el título
    while body and (not body[0].strip() or set(body[0].strip()) == {'='}): body.pop(0)
    while body and (not body[-1].strip() or set(body[-1].strip()) == {'='}): body.pop()
    hdr = f"# Traducción inglesa oficial — coreano {n}: {title}\n\nPegado por el autor el 2026-10-17 (novelpia, *The Villainess Malfoy*, del 36 al 111 en un solo archivo; segunda extracción, completa). Solo para consulta y cotejo; nunca para copiar.\n\n---\n\n"
    (outdir / f"ko-{n:02d}.md").write_text(hdr + "\n".join(body) + "\n", encoding='utf-8')
print(len(heads))
