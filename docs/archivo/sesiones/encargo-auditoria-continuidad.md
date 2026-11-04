# Encargo: auditoría de continuidad y lógica de la historia entera

*30 de octubre de 2026. Preparado por la sesión principal (Claude) a petición del autor. Sirve para Claude (subagentes Opus) o para Codex. Se habla al autor en español.*

## Por qué así

La historia tiene unas **225.000 palabras** (del 1 al 50, los seis *Year One* y los dos interludios), que son unos **300.000 tokens**. Los manuales de cada capítulo y la continuidad transversal suman unas **87.000 palabras** más (unos 115.000 tokens). Un solo lector podría con todo, pero con tanto texto los detalles se le escapan: quién sabía qué en qué fecha, dónde estaba un objeto, qué se prometió. Por eso:

1. **Cuatro lectores**, cada uno con un tramo **en texto completo**. Del resto de la historia leen los **manuales**, que recogen escenas, frases literales, quién sabe qué y la continuidad fácil de romper. Así todos conocen el conjunto y cada uno conoce su tramo a fondo.
2. **Un conciliador** que junta los cuatro informes, quita repeticiones y ordena por gravedad.
3. **Verificación con grep** de cada hallazgo antes de aceptarlo: los informes se equivocan con la misma seguridad con la que aciertan.

## Los cuatro lectores (en paralelo)

Todos leen primero, enteros:
- `CLAUDE.md`;
- `docs/handoff-v3.0.md`;
- `docs/capitulos/continuidad-transversal.md`;
- `docs/notas/lo-que-sabe-harry.md`.

Después, cada uno lee su tramo en texto completo y el resto en manuales (`docs/capitulos/cap-NN.md`, `extra-year-one-N.md`, `extra-year-one-5-y-6.md`, `interludio-1.md`, `interludio-2.md`):

| Lector | Texto completo | Manuales |
|---|---|---|
| A | `manuscrito/cap-01` a `cap-15`; `borradores/extra-year-one-1` a `-4` | Del 16 al 50 y el resto de extras |
| B | `borradores/cap-16` a `cap-30` | Del 1 al 15, del 31 al 50 y los extras |
| C | `borradores/cap-31` a `cap-40`; `interludio-1-the-seventh-lock.md` | Del 1 al 30, del 41 al 50 y los extras |
| D | `borradores/cap-41` a `cap-50`; `interludio-2-the-wrong-night.md`; `extra-year-one-5` y `-6` | Del 1 al 40 y los extras 1 a 4 |

(En los capítulos, sin fichas: los nombres que llevan `ficha`, `lector` o `recorte` no se leen.)

**Qué busca cada uno en su tramo**, contrastándolo con el resto:
1. **Fechas y calendario:** días de la semana, meses, edades y cursos que no cuadran entre capítulos.
2. **Quién sabe qué y desde cuándo:** personajes que saben algo antes de poder saberlo, o que lo olvidan después de saberlo. Sobre todo Lyra; también Harry (lo que sabe por la otra vida y lo que no), Granger, Weasley, Lucius, Narcissa, Snape, Dumbledore y Moody.
3. **Objetos y fichas:** dónde está cada uno en cada momento (los anillos y sus colores, la capa, el mapa, el pañuelo, el calentador, la posdata, la nota de Regulus, la pluma de azúcar, la lista de Draco, la caja).
4. **Promesas, deudas y cuentas:** lo que se debe, lo que se paga y lo que se olvida.
5. **Hilos abiertos:** lo que se planta y no vuelve. Cada uno con el capítulo en que se plantó y el último en que se tocó.
6. **Lógica de las motivaciones:** ¿tiene el personaje razón y medios para hacer lo que hace? ¿Actúa alguien contra lo que sabe? ¿Hay algo que solo pasa porque la trama lo necesita?
7. **Canon:** discrepancias clasificadas de la A a la D (handoff §6). Las B, que son cambios deliberados, no se tocan.
8. **Choques con los manuales:** cuando el texto dice una cosa y el manual otra, manda el texto, y el manual se apunta para corregirlo.

**Formato del informe** (`docs/notas/auditoria/lector-X.md`): una tabla con **Nº | Tipo (1-8) | Dónde (archivo:línea) | Qué choca con qué (cita breve de los dos lados) | Gravedad (grave/media/menor) | Propuesta**. Después, en una lista aparte, los hilos abiertos con el capítulo de la última mención. Como mucho unas 60 filas: si sale más, solo lo grave y lo medio.

## El conciliador

Lee los cuatro informes, el handoff, la continuidad y el guion de la tanda en curso. Escribe `docs/notas/auditoria/conciliado.md`:
- junta los hallazgos repetidos;
- quita los que son cambios deliberados (B), que lo dicen el handoff y los manuales;
- ordena por gravedad;
- y marca en cada hallazgo si toca **lo publicado**. Lo publicado (`manuscrito/`, y lo que el autor ya ha subido según `CLAUDE.md`, «Publicación») no se cambia: se apunta en `docs/notas/erratas-publicado.md` y decide el autor.

## La verificación y el arreglo

La sesión principal comprueba cada hallazgo con grep en el texto antes de aceptarlo, decide con motivo (tabla «Hallazgo | Decisión | Motivo» en `docs/notas/auditoria/decisiones.md`) y arregla lo que no está publicado. Después pone al día los manuales y la continuidad. Commit y push tras cada paso.

## Coste aproximado

Cada lector, unos 150.000 a 200.000 tokens de lectura. El conciliador, unos 60.000. Con Claude son cinco subagentes Opus; conviene avisar al autor antes de lanzarlos.

## Para las tandas siguientes

`CLAUDE.md` ya lo prevé a partir de unas 200.000 palabras: al empezar una tanda se lee **entera la tanda anterior** y, del resto, **los manuales**. Esta auditoría es lo que lo complementa: hacerla una vez por tanda, al cerrarla, para que los manuales sigan siendo fiables como índice.
