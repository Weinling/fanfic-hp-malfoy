# Estado de trabajo

**Léelo lo primero** al abrir sesión o tras compactar. Se actualiza en cada paso (escena escrita, crítica aplicada, capítulo cerrado) y va en el mismo commit que el paso.

Última actualización: 17 de octubre de 2026.

## Ahora mismo

- **SESIÓN NUEVA (preparado el 17 de octubre):** lee `docs/notas/sesion-nueva-17-oct.md` justo después de este estado. Hay dos encargos: rehacer el 24, ya publicado en Webnovel, y discutir con el autor el rumbo del 25 en adelante antes de escribir nada.
  - **17 de octubre, sesión nueva abierta:** lectura obligatoria hecha (ver «Lecturas hechas en esta sesión», al final). Hechas al autor las tres preguntas del §4 de esa nota. **Ningún capítulo tocado.**
  - **Respuestas del autor (17 de octubre):**
    1. **El 24** solo tiene que dejar de parecer un calco y ser mejor capítulo, con los estándares actuales y los capítulos revisados (del 1 al 23 fusionados) como referencia. Está publicado: **no puede afectar en nada al lector que ya lo leyó** (mismos hechos). Los cambios de verdad empiezan en el 25, donde hay más libertad.
    2. **Orden:** primero el rumbo, después el 24.
    3. **Coreano:** el autor tiene la historia original entera y la va a traer (del 36 en adelante, a `coreano/`).
  - **Hecho:** leídos enteros, por la sesión principal, del 25 al 30 (`borradores/cap-25` a `cap-30`).
  - **17 de octubre, más tarde:** el autor trae del 36 al 111 en un solo archivo. **No es el coreano: es la traducción inglesa oficial** (novelpia, *The Villainess Malfoy*). Partida en `referencia/oficial-en/ko-36.md` … `ko-111.md` (commit 927797a). La historia está terminada: la trama acaba en el 106 y del 107 al 111 son epílogos. **Los capítulos parecen incompletos:** tienen entre 600 y 1.700 palabras, contra 2.000-3.500 de los completos de la misma traducción, y empiezan o acaban a mitad de escena. Preguntado al autor si tiene los completos o el coreano.
  - **Confirmado con la copia manual del autor (36 a 41, pegada en el chat):** la extracción solo trae la primera parte de cada capítulo; falta más de la mitad, y el corte no es fijo. Los del 36 al 41 están leídos enteros en esa copia (no guardada en el repositorio). Pendiente: arreglar la extracción y volver a bajar del 42 al 111 (y guardar completos del 36 al 41); los resúmenes de los agentes valen solo como esqueleto y se rehacen con el texto completo.
  - **Método acordado (autor, 17 de octubre):** el autor copia a mano la oficial completa **por tandas grandes**, en un archivo de texto con una línea `Capítulo NN: Título` por capítulo. La sesión principal lo parte con `herramientas/partir_oficial.py` (`python3 -I herramientas/partir_oficial.py ARCHIVO referencia/oficial-en`) y sustituye los `ko-NN.md` incompletos. Orden propuesto: del 36 al 54, luego 82, 83, 90, 104-106 y 108; el resto, al adaptar cada tanda. Con cada tanda completa se rehace su resumen.
  - **Los cuatro resúmenes están hechos** (commit aparte), sobre texto incompleto: valen solo como esqueleto.
  - **Resuelto el mismo día:** el autor trae una segunda extracción, **completa** (unas 245.000 palabras; 1c42554). Sustituye a la incompleta en `referencia/oficial-en/ko-36.md` … `ko-111.md`; comprobada contra la copia manual del 36, el 40 y el 41. Ya no hace falta copiar a mano. **Relanzados cuatro agentes Sonnet** que rehacen desde cero los cuatro `borradores/resumen-oficial-*.md` con el texto entero.
  - **Leído entero por la sesión principal:** la oficial del 36 al 54 (el final del cuarto año del original, los extras 52 y 53, y el principio del quinto en el 54). Hecho el del 55 al 73 (agente). Faltan los del 36-54, 74-92 y 93-111.
  - **En marcha (opción B, aprobada por el autor):** cuatro agentes Sonnet resumen la oficial por tandas en `borradores/resumen-oficial-36-54.md`, `-55-73.md`, `-74-92.md` y `-93-111.md`, con el formato de `resumen-coreano-26-35.md`; avisados de que el texto es parcial. La sesión principal lee enteros del 36 al 41 (hecho) y después los cuatro resúmenes.
  - **Siguiente:** cuando lleguen los coreanos, resumirlos por tandas con agentes Sonnet (como `resumen-coreano-26-35.md`); luego, el documento de rumbo para el autor (`sesion-nueva-17-oct.md` §3).
- **HECHA (17 de octubre): FUSIÓN DE VERSIONES.** Plan e informes en `docs/notas/cotejo-oficial/fusion/`. Bases:
  - revisado en el 4, 5, 8, 10, 11, 13, 18 y del 19 al 22;
  - beats nuevos en el 1, 2, 3, 14, 23 y *Year One* 1 y 2.

  En las dos bases van los injertos de los informes. Cuando un injerto calcaba la oficial, se rehízo con palabras nuevas (detalle en los commits de los bloques A y B).
  - Revisión final hecha por dos Opus nuevos (`fusion/revision-final-1.md` y `-2.md`), con todos los arreglos aplicados: el orden de la discusión en el 21, los anillos, Dumbledore en el 22, Lupin en el 19, citas del 9, el 14 y el 25/26.
  - Al día con los textos fusionados: los manuales del 1 al 23, *Year One* 1 y 2, la continuidad transversal y el handoff (1, 2 y la deuda de Lupin).
  - **Para el autor:** `docs/notas/cotejo-oficial/veredicto-publicado.md` dice qué subir, en qué grupos y qué pantallazos cambian. **Puede publicar.**
  - **Webnovel (autor, 17 de octubre):** hay 25 entregas (del 1 al 23 más *Year One* 1 y 2). Hoy sube *Year One* 3 y 4 (entregas 26 y 27), en su versión cotejada, y mañana el 24. Los retoques del 1 al 23 se actualizan en sus entregas; quien empezó antes no los verá.
  - **Siguiente:** plan del 24 al 30 (`plan-24-30.md`), en pausa hasta que el autor decida los hilos H1 a H3; falta el coreano 36.

- **Nuevo frente (15 de octubre): cotejo con la traducción inglesa oficial.** El autor ha descubierto que el original coreano tiene versión inglesa oficial y quiere que el fic deje de parafrasearlo tan de cerca, sin tocar la historia. Ya hecho:
  - el prólogo oficial está en `referencia/oficial-en/`;
  - `herramientas/cotejo.py` busca frases compartidas;
  - el diagnóstico del 1, línea a línea, está en `docs/notas/cotejo-oficial/cap-01.md`;
  - la lectura completa de los 34 capítulos, con sospechas y anclas, está en `docs/notas/cotejo-oficial/lectura-completa.md`.

  - **Decidido por el autor:** se retoca lo publicado; lo que es trama, solo un poco. Publicado: Wattpad del 1 al 21; Webnovel del 1 al 23 más *Year One* 1 y 2. Los cambios se anuncian con una nota de Ash.
  - **Hecho:**
    - el 1, sobre el texto publicado, con el arranque recortado (`docs/notas/cotejo-oficial/cap-01.md`);
    - del 2 al 11 contra los coreanos 2 a 10 (`docs/notas/cotejo-oficial/caps-02-11.md`), con las citas ajustadas en el 4, 7, 10, 11, 13 y 14.
    - manuales del 1 al 13 y handoff con las citas nuevas;
    - 15 de octubre, tras compactar: oficiales 11 a 16 en `referencia/oficial-en/`; el 13, 14, 16, 17, 18 y la primera mitad del 19 retocados (`docs/notas/cotejo-oficial/caps-13-19.md`), con manuales, handoff y continuidad ajustados. Lectura hecha tras compactar: estado, guía, handoff entero, todos los manuales, continuidad transversal, el 11 al 19 enteros y las oficiales 11 a 16. Un subagente mapeó los ecos del 13 al 19 en el 20 y siguientes (`ecos-13-19.md`);
    - preparado para compactar: referencia 888ff27 (lo publicado sin retocar; la etiqueta `antes-del-cotejo` es solo local), `herramientas/comparar.py` (antes/después y parecido con la oficial, por capítulo) y **`docs/notas/cotejo-oficial/GUIA.md`** (reglas, correspondencia, orden, método y lectura al retomar).
    - 15 de octubre, más tarde: el resto del 19, el 20 y el 21, cotejados con el coreano (no hace falta la oficial: `coreano/` tiene del 14 al 35). Notas en `caps-19-21.md`. El autor va a publicar pronto el 21 en Wattpad y aún no ha subido ningún retoque.
  - 15 de octubre, al final: aplicados los arreglos de la revisión editorial del 19 al 22 (`revision-19-21.md`). **El autor subió el 21 a Wattpad con la versión vieja**, antes de los retoques; puede actualizarlo. Todavía no ha subido ningún retoque a ninguna plataforma.
  - **Condición del autor para subir los retoques** (15 de octubre): solo si las revisiones confirman que del 1 al 23 y *Year One* 1 y 2:
    - mantienen la calidad de la historia;
    - no chocan entre sí;
    - no estropean la experiencia de quien ya los leyó.

    Publicado: en Wattpad, del 1 al 21; en Webnovel, del 1 al 23 más *Year One* 1 y 2 (las entregas 24 y 25 de Webnovel).
  - **Siguiente (punto exacto para retomar, en este orden):** leer `GUIA.md` §6 y §8.
    1. Cotejar con el coreano lo que falta de lo publicado: el 22 (resto del coreano 21 y el 22), el 23 (coreano 23), *Year One* 1 (coreano 18) y *Year One* 2 (coreano 24). En cada uno, mapear los ecos y hacer la revisión editorial antes y después con Opus, como del 13 al 21.
    2. Revisión de conjunto de todo lo publicado (`GUIA.md` §8), con un veredicto para el autor: qué subir, en qué orden y con qué nota.
    3. Lo no publicado, con más libertad (autor: «más creativos o fuertes»): *Year One* 3 y 4 y del 24 al 30, manteniendo lo que fija la continuidad y lo que necesita el 31.

    El 31 queda en espera mientras tanto.
  - **15 de octubre, tras la compactación del cotejo:** el autor trae una crítica y revisión de lo hecho en el cotejo, con consejos, y pide que la revise alguien que lo haya leído todo: lo publicado sin revisar (888ff27), lo revisado y los capítulos futuros. Su ruta (`/tmp/claude-0/.../ef4eaf25-…/scratchpad/prompt-never-owe-revision.md`) es de otra sesión y no se puede leer desde esta: se le ha pedido que la pegue. **Antes de seguir con el 22 hay que valorar esa crítica.**
  - **Crítica recibida** (`docs/notas/cotejo-oficial/encargo-critico-ronda3.md`) y **valorada** (`valoracion-encargo-ronda3.md`: qué se acepta, qué no, datos de densidad y decisiones del autor). Herramienta nueva: `herramientas/densidad.py`.
  - **16 de octubre: el autor sube hoy a Webnovel *Year One* 3 y 4** (entregas 26 y 27) y no sube nada más allí hasta que se le diga. Están cotejados con los coreanos 25 y 26 (commit e02d0ee; copias de antes en el scratchpad, `yo3-antes.md` y `yo4-antes.md`). Hay una revisión editorial de Opus en marcha; sus arreglos van antes de que el autor los suba.
  - **Revisor de conjunto en marcha** (Opus, el que lo lee todo: lo publicado de 888ff27, los diffs y los futuros). Escribe `registro-publicado.md` y `revision-conjunto-clases.md` en `docs/notas/cotejo-oficial/`. Si se compacta, sus archivos bastan para seguir.
  - **Orden después:** cotejo del 22 y el 23 (con los arreglos del crítico, solo A y B), *Year One* 1 y 2 (solo A y B); densidad y tics del 1 al 14 (A), el Patronus del 10 (devolver una imagen sin perro) y el gesto de Harry en el 14 (B); el veredicto de lo publicado (GUIA §8); del 24 al 30 con cirugía mínima y semillas; el informe de vuelta al crítico.
  - **16 de octubre, hecho:** revisión de conjunto terminada (`registro-publicado.md`, `revision-conjunto-clases.md`) y sus arreglos aplicados (e9037e9); veredicto en `veredicto-publicado.md`. Densidad (clase A, mismas palabras) en el 4, 8, 9, 10 y 12; gesto de Harry en el 14 (B). Cotejo del 22 (43c484d) y del 23 (9e271c2) con el coreano, solo A y B. Revisión del 22 y el 23 y sus arreglos, aplicados (35a838e, 94ffaea); densidad también en el 1, 2, 7 y 11. **Lo publicado está listo: el autor puede subir el 1-21 a Wattpad y el 1-23 a Webnovel** (veredicto). **Siguiente:** *Year One* 1 y 2 (solo A y B); del 24 al 30 con cirugía mínima y semillas; informe de vuelta al crítico.
  - **16 de octubre, nuevo encargo del autor: cambiar los beats, no solo las frases** (que el lector adelantado siga la misma historia, pero que el nuevo tenga otra experiencia). Hecho, cada uno con revisión de Opus (sin C ni D, «mejor que antes») y sus arreglos:
    - el 1 (eee1bdc y siguiente), el 2 (03c9526, f550c81) y el 3 (4fa0bed, 07890e4), con manuales;
    - *Year One* 1 (3e726ab, aeea8be) y 2 (08a6d69, 1740acd), con manuales. Webnovel tiene publicadas las versiones viejas; las nuevas solo cambian A y B.
    - Ranking de calco de estructura del 4 al 23: `docs/notas/cotejo-oficial/calco-estructura.md` (tabla arriba, palancas por escena). **Siguiente:** rehacer los beats de los más calcados, uno a uno y con revisión de Opus: 5, 10, 11, 13, 14, 18, 19, 20 y 21 (los cuatro últimos van atados: bucle temporal), luego el 22, el 4, el 8 y el 23. Después, el plan de divergencias del 24 al 30 para que lo apruebe el autor.
    - Copias de antes en el scratchpad (`*-antes-beats.md`, `*-antes-revision.md`).
    - **Hecho después (16 de octubre):** beats rehechos del 4, 5, 8, 10, 11, 13, 14, 18, 19, 20, 21, 22 y 23, con las palancas de `calco-estructura.md`. Revisados por Opus y con arreglos aplicados: 5, 10, 11, 13, 14 y 18. Después, revisados también el 4, el 8, el 23 y el bucle 19-22, con arreglos aplicados (13712f6, 17d8f14), y todos los manuales al día (8fe2216, aedf010). **Pendiente:** avisar al autor de las frases del registro que faltan desde la primera ronda del cotejo (13: «Dithering… does not suit me», «Technically, us», «A shred of taste after all»; 18: «They come in twos, and there are three of us», «Do try.», «I’m marking *you*»); después, el plan de divergencias del 24 al 30.
  - Lectura hecha tras esta compactación: el estado, `GUIA.md`, `caps-02-11.md`, `caps-13-19.md` y `caps-19-21.md`, el handoff entero, todos los manuales (del 1 al 30 y *Year One* 1 a 4) y la continuidad transversal.
- **Capítulo 29, *Every Ounce*** (coreano 32), **cerrado**: `borradores/cap-29-every-ounce.md` (~4.300 palabras). Lo que está hecho:
  - ficha aprobada por el autor;
  - escritura escena a escena;
  - crítica y arreglos (`docs/notas/cap-29-critica.md`, con la nota para el crítico al final);
  - manual (`docs/capitulos/cap-29.md`);
  - continuidad transversal;
  - handoff (§15).
- **Capítulo 30, *Which One*** (coreano 33), **cerrado**: `borradores/cap-30-which-one.md` (~3.910 palabras). Lo que está hecho:
  - ficha aprobada por el autor (`borradores/cap-30-ficha-guion.md`), con el beso a través de la capa y la reacción de Harry que pidió el autor;
  - escritura escena a escena y pasada de tics;
  - crítica y arreglos (`docs/notas/cap-30-critica.md`, con la nota para el crítico al final);
  - manual (`docs/capitulos/cap-30.md`);
  - continuidad transversal;
  - handoff (§15).
- **Próximo paso: el capítulo 31** (coreano 34): las parejas del Baile, Skeeter y el «triángulo», Lyra anuncia a Krum, Potter sospecha de Moody (Lyra, con coda de Harry). Antes de la ficha, el protocolo de `CLAUDE.md`:
  - estado, handoff entero, todos los manuales y la continuidad transversal;
  - el texto completo del 29 y del 30;
  - los coreanos 34, 35 y 36 (**el 36 no está en `coreano/`: pedírselo al autor**);
  - `docs/notas/arco-29-32-lectura.md`.
- **Para el 31, ya avisado:**
  - **No es pago romántico** (crítico): el 26, el 27, el 29 y el 30 lo fueron. El próximo beso no se vende como otro «primero».
  - Empieza con Parkinson carraspeando detrás de Lyra ante el aviso del Baile.
  - La capa de Harry está en la bolsa de Lyra; la herida del hombro, el escarabajo y el ojo de Moody, abiertos.
  - Lyra sabe que la Saeta de Potter es suya y que él confundió la pluma de Skeeter.
- **Cerrados:** *Year One* 4 y del 24 al 30, con manual, nota y handoff. Del 23 al 28, revisados además por el revisor (`docs/notas/revisiones/tanda-23-a-28.md`).

## Si se compacta durante el cotejo

Seguir `docs/notas/cotejo-oficial/GUIA.md` §6. Lo de abajo vale para cuando se vuelva al 31.

## Si se compacta (arco del 29 al 32)

Seguir `docs/notas/arco-29-32-lectura.md` §1: el protocolo de `CLAUDE.md` más ese archivo; sin releer la historia entera; grep y lectura dirigida en texto completo según su §4; ante una duda de continuidad, preguntar al crítico (vivo, no se compacta con la sesión principal y lo ha leído todo).

## Lecturas hechas en esta sesión (protocolo de `CLAUDE.md`)

Se apunta aquí lo leído tras cada compactación, para que se pueda comprobar.
- **Tras la última compactación (11 de octubre):** estado, handoff (§2, §4, §14 y §15; no entero), capítulo 26 entero, fichas del 25 al 27, fragmentos del 5, 14, 19 y 25. **No se leyeron todos los manuales**, como exige el protocolo. Consecuencia: en la ficha del 27, el handoff y un mensaje al autor se llamó «el beso de verdad» al del 29, cuando ya hubo dos en la boca (3 y 19, ambos en sus manuales). No llegó al texto de ningún capítulo; lo cazó el lector del 29 y está corregido.
- **11 de octubre, después:** handoff entero y todos los manuales, enteros. Con ellos, `docs/capitulos/continuidad-transversal.md` (nuevo).
- **Pendiente antes del 29:** el 29 abre arco (29 a 32): leer la historia entera en texto completo, en un contexto limpio (tras compactar o en sesión nueva). El crítico se reinicia para el 29. **Hecho (abajo).**
- **Sesión nueva del 29 (11 de octubre), en contexto limpio, todo entero y en orden:** `CLAUDE.md`; este estado; el handoff entero (`docs/handoff-v2.0.md`, las 795 líneas); todos los manuales de `docs/capitulos/` (1 a 28 y *Year One* 1 a 4), enteros; `docs/capitulos/continuidad-transversal.md`; la historia en texto completo: `manuscrito/cap-01` a `cap-15`, `borradores/cap-16` a `cap-23`, `borradores/extra-year-one-1` a `4` y `borradores/cap-24` a `cap-28`; los coreanos 32, 33 y 34 enteros; `borradores/plan-coreano-26-35.md`; `borradores/cap-29-lector.md`; `docs/notas/critico-arranque-29.md`; la ficha del 28 como modelo de formato.
- **Compactación del 12 de octubre, con el 30 ya escrito entero** (las cinco escenas, commiteadas antes de compactar, con la lectura completa del arco en contexto). Después de compactar se leyó solo esto: el estado, `docs/notas/arco-29-32-lectura.md`, el 30 entero, el manual del 29, la continuidad transversal y el final del handoff (§15). Se buscó con grep y se leyeron trozos del 4, del 8, del 13 y del 23 (la pluma, el «No need», el claustro y el eco del tren). **No se cumplió el protocolo entero:** quedaron sin leer el handoff completo, el resto de manuales, el 28 y el 29 en texto completo, y los coreanos 33 a 35. Con eso se hicieron la pasada de tics, los arreglos de la crítica, el manual, la continuidad y el handoff; la continuidad la comprobó además el crítico, que lo tiene todo leído. **Antes de la ficha del 31 hay que hacer el protocolo completo.**
- **Crítico del 29:** lanzado (Opus) con `docs/critico-v2.0.md` y `docs/notas/critico-arranque-29.md`. Leyó todo lo adaptado (`docs/notas/critico-29-lectura-inicial.md`) y criticó el 29.
- **Sesión nueva del 17 de octubre (rehacer el 24 y rumbo del 25 en adelante), en contexto limpio.** Leído entero, por la sesión principal, lo que pide `docs/notas/sesion-nueva-17-oct.md` §5:
  - `CLAUDE.md`, este estado y `docs/notas/sesion-nueva-17-oct.md`;
  - el handoff entero (`docs/handoff-v2.0.md`, §1 a §15);
  - todos los manuales de `docs/capitulos/` (1 a 30 y *Year One* 1 a 4) y `continuidad-transversal.md`;
  - el texto completo del 22, el 23 y el 24;
  - los coreanos 27, 28 y 29;
  - para el rumbo: `docs/notas/cotejo-oficial/plan-24-30.md` entero, `docs/notas/arco-29-32-lectura.md` y `borradores/resumen-coreano-26-35.md` entero;
  - para el 24: `borradores/cap-24-ficha-guion.md` y `docs/notas/cap-24-critica.md`.

  **Sin leer todavía:** la historia entera en texto completo (el autor la autoriza, igual que los agentes; se hará al abrir la discusión del rumbo si la decisión lo pide) y los coreanos 30 a 35 en coreano (están resumidos en `resumen-coreano-26-35.md`; se leen enteros si se planea una tanda propia desde el 31). Hechas al autor las tres preguntas del §4; se espera respuesta antes de tocar ningún capítulo.

## Texto que solo existe en contexto

Ninguno. Todo está commiteado y subido.

## Agentes vivos

- **Crítico:** el del cuarto año (criticó del 24 al 28) está retirado. **El del 29 está vivo** (Opus, arrancado con `docs/notas/critico-arranque-29.md`): leyó entero todo lo adaptado, criticó el 29 y el 30, y espera el 31. Se le reutiliza hasta que se le llene el contexto (`CLAUDE.md`). El anterior (17 a 23, *Year One*, revisión del 1 al 3) está retirado.
- **Revisor:** es el chat paralelo del autor. Sus informes llegan a `docs/notas/revisiones/`.

## Decisiones pendientes del autor

- En qué capítulo obtiene Lyra alguna pieza de lo que sabe Harry (en el 29 no: la copa de Hufflepuff no se nombra).
- La publicación la lleva el autor (consejos: titular los extras «Year One, Part N»; en Webnovel la numeración automática se adelanta cuatro respecto a la interna).
