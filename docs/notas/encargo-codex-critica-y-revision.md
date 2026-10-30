# Encargo para Codex: crítica, revisión y arreglos de la tanda 41-50

*30 de octubre de 2026. Lo preparó la sesión principal (Claude) a petición del autor, Edén, que se lo pasa a Codex. Háblale al autor en español; los capítulos están en inglés británico.*

**Cómo está repartido en este proyecto, y cómo se reparte aquí.** Con Claude, cada capítulo pasa por tres manos distintas:
- la **sesión principal** lo escribe;
- un **crítico** (subagente Opus) lo lee **a ciegas**: conoce la historia escrita, pero no el plan ni el futuro, y propone notas;
- la sesión principal, que sí conoce el plan, **decide** qué notas acepta, cada una con su motivo, y las aplica.

El autor quiere conservar esa separación: que quien aplica no sea el mismo que critica. Por eso este encargo tiene **dos papeles en dos pasadas separadas**. Lo ideal es hacerlas en **dos sesiones** de Codex, o con un subagente para la crítica. Si solo puede ser una sesión, entonces:
- la crítica se escribe entera en su archivo antes de abrir el guion;
- después, el revisor la lee como si fuera de otra persona.

---

## 0. Los dos prompts para pegar

**Sesión A, el crítico (solo lee y escribe notas; no toca los capítulos):**

> Trabajas en el repositorio `/Users/eden/Documents/fanfic-hp-malfoy`, rama `claude/wizardly-albattani-vazqyr`. Es la adaptación al inglés británico de una fanfic coreana de Harry Potter con Lyra Malfoy, genderbend de Draco. Eres el **crítico**. Lee `docs/notas/encargo-codex-critica-y-revision.md`, solo las secciones §1 y §2, y haz lo que dice el §2: critica a ciegas, uno por uno y en orden de lectura, los capítulos de la tanda 41-50. Escribe cada crítica en `docs/notas/codex/critica-NN.md`. No toques ningún capítulo ni ningún otro archivo. No leas lo que el §2 prohíbe. Háblame en español.

**Sesión B, el revisor y editor (decide y aplica):**

> Trabajas en el repositorio `/Users/eden/Documents/fanfic-hp-malfoy`, rama `claude/wizardly-albattani-vazqyr`. Eres el **revisor y editor** de la tanda 41-50. Lee entero `docs/notas/encargo-codex-critica-y-revision.md` y haz lo que dicen el §3 y el §4. Las críticas a ciegas están en `docs/notas/codex/critica-NN.md`: son de otra persona, y decides tú, con motivo, qué aceptas. Haz además tu propia revisión informada y aplica los arreglos. Después pon al día manuales, continuidad, estado y la nota para el autor, con commit y push tras cada paso. Háblame en español.

---

## 1. Qué es esto y qué no se toca

- **El proyecto.** Léelo en `CLAUDE.md` y en `docs/handoff-v3.0.md` §2 a §4 (identidad, motor y reglas de escritura, con los tics). La tanda 41-50 va del verano de 1995 a la Navidad del quinto curso.
- **Los capítulos de la tanda, en orden de lectura** (y de publicación):

  | Orden | Archivo | Palabras | Crítica |
  |---|---|---|---|
  | 41 | `borradores/cap-41-the-sleeve.md` | ~3.060 | Ya criticado y arreglado (Claude) |
  | *Interlude* | `borradores/interludio-2-the-wrong-night.md` | ~3.730 | Ya criticado y arreglado (Claude) |
  | 42 | `borradores/cap-42-badges.md` | ~2.930 | Pendiente |
  | *Year One* 5 | `borradores/extra-year-one-5-the-forest.md` | ~2.490 | Pendiente |
  | *Year One* 6 | `borradores/extra-year-one-6-the-black-pieces.md` | ~2.110 | Pendiente |
  | 43 | `borradores/cap-43-prefects.md` | ~3.040 | Pendiente |
  | 44 | `borradores/cap-44-rounds.md` | ~3.120 | Pendiente |
  | 45 | `borradores/cap-45-lines.md` | ~3.000 | Pendiente |
  | 46 | `borradores/cap-46-where-the-sea-is.md` | ~3.000 | Pendiente |
  | 47 | `borradores/cap-47-pretext.md` | ~2.820 | Pendiente |
  | 48 | `borradores/cap-48-him-and-now-you.md` | ~2.900 | Pendiente |
  | 49 | `borradores/cap-49-the-button-warmer.md` | ~3.250 | Pendiente |
  | 50 | `borradores/cap-50-the-east-cottage.md` | ~3.420 | Pendiente |

  Los *Year One* son extras de primer curso (1992) que van entre el 42 y el 43. Los interludios están contados desde Harry y no llevan número.
- **Lo que no se toca nunca:**
  - `manuscrito/`, que es lo publicado. Una errata se apunta en `docs/notas/erratas-publicado.md`.
  - `coreano/`, `fuentes/` y `referencia/`, que son solo de consulta.
  - Los hechos del guion aprobado por el autor (`borradores/guion-tanda-41-50.md`) y el rumbo (handoff §8).

  Un arreglo cambia frases, orden, énfasis o una línea de continuidad, no un hecho. Si una nota pide cambiar un hecho, no se aplica: se apunta con ⚠ en `docs/notas/autonomo/PARA-EL-AUTOR.md`.
- **Contenido:** los personajes tienen quince años (en los *Year One*, once). Nada sexual ni sensual.
- **Convenciones de prosa:**
  - comillas y apóstrofos tipográficos (“ ” ’);
  - separador de escena `⁂`;
  - cursivas con `*…*`;
  - «Mr» y «Mrs» sin punto;
  - ortografía británica.

  En el punto de vista de Lyra, Harry es «Potter». En el de Harry, ella es «Malfoy» o «she», y «Lyra» solo en momentos marcados.
- **Extensión:** de 3.000 a 4.200 palabras por capítulo; los extras tienen más margen. **Se quedaron cortos el 42, el 47 y el 48** (unas 2.800-2.930): que el revisor decida si ganan con una escena o un momento más, o si se quedan así. Si recortar pierde más de lo que gana, no se recorta.

## 2. El crítico (a ciegas)

Juzga como un lector listo de Wattpad, **sin saber lo que viene**.

- **Lee:**
  - `docs/critico-v2.0.md` §1 a §6 (encargo y rúbrica);
  - `docs/notas/critico-arranque-29.md` §2 y `docs/notas/critico-arranque-31.md`;
  - las notas de crítica anteriores: `docs/notas/cap-31-critica.md` a `cap-41-critica.md`, `interludio-1-critica.md` e `interludio-2-critica.md`. Dicen qué se pidió, qué se aceptó y qué tics han ido cayendo;
  - **el texto completo, en orden de lectura:**
    - `borradores/cap-31-whether-i-do.md`;
    - `cap-32-plain-silver.md`;
    - `interludio-1-the-seventh-lock.md`;
    - del `cap-33` al `cap-40`;
    - y la tanda entera de la tabla del §1.

    De la historia anterior (del 1 al 30 y los *Year One* 1 a 4) basta con lo que citan las notas de crítica. Si quieres el contexto de los *Year One* 5 y 6, lee también `borradores/extra-year-one-2-nobody-asked-you.md` y `extra-year-one-4-what-scared-actually-is.md`.
- **No leas** (llevan trama futura o el secreto de Harry):
  - fichas, guiones y resúmenes de `borradores/`;
  - `docs/handoff-*`, `docs/capitulos/`, `docs/estado-de-trabajo.md`, `docs/fable/`, `docs/notas/autonomo/`, `docs/notas/lo-que-sabe-harry.md` y `docs/notas/revisiones/`;
  - `coreano/` y `referencia/`;
  - y, dentro de este encargo, nada del §3 en adelante.
- **Formato de cada crítica** (`docs/notas/codex/critica-NN.md`): el de la sección 6 de `docs/critico-v2.0.md`. Modelo: `docs/notas/cap-41-critica.md` y `interludio-2-critica.md`. Lleva:
  - un veredicto;
  - puntuaciones de 1 a 10 en emoción, romance, gancho, ritmo, calor, trama, personajes y prosa;
  - las tres preguntas del lector de Wattpad (dónde comentaría, qué citaría, dónde se iría);
  - lo que funciona;
  - los problemas por prioridad (graves, medios y menores), cada uno con su línea y una propuesta concreta;
  - la prosa y los tics;
  - y el **ranking acumulado** del 31 en adelante. El último es: 39 ≈ 40 > Interludio 2 ≈ Interludio 1 ≈ 32 ≈ 37 > 35 ≈ 38 > 41 ≈ 33 ≈ 36 > 34 > 31.
- **Mira en especial:**
  - que Lyra no olvide lo que sabe;
  - que cada capítulo mueva la relación (sube o baja, y se ve);
  - el ritmo de la tanda (nunca dos capítulos planos seguidos);
  - los finales, que no se repitan de tipo;
  - y, en el 50, si la deducción de Lyra se gana con piezas que el lector ya tenía.
- **Tics que hay que buscar:**
  - «did not» como señal de emoción (como mucho unos cuatro por cada mil palabras);
  - «She did not need to»; «she found (that)»;
  - «at all» (dos por capítulo, mejor en diálogo);
  - «the way…» en serie; «for a long moment»; «all at once»;
  - «before she had decided to» y sus variantes;
  - lecturas de cara; la cara quieta; «held his eyes»;
  - la sonrisa de la madre para las esposas de los ministros (o para la ópera);
  - «Lyra read it twice»; «It came out…»;
  - «No X. Y.» (una por capítulo); «never once»;
  - la coletilla con «which» (tres por capítulo);
  - los símiles «like a man» o «as a man»;
  - la metáfora de las sumas para pensar; la vela que se apaga; guardar algo «por dentro» junto a otras cosas;
  - frases recicladas de capítulos anteriores (el té frío, «held on», «beautifully», «a book she was not reading», «the far end of the train»);
  - y que un capítulo repita la última línea o la imagen final del anterior.

## 3. El revisor (informado)

Ahora sí se lee lo planeado, para comprobar fidelidad y continuidad, y para juzgar las críticas.

- **Lee:**
  - `docs/handoff-v3.0.md` entero;
  - `docs/capitulos/continuidad-transversal.md`;
  - `borradores/guion-tanda-41-50.md`: §0, §2, §5 «Avisos», §7 «Hilos» y §8 «Fable 004»;
  - las fichas `borradores/cap-NN-ficha-guion.md`, `interludio-2-ficha-guion.md` y `extra-year-one-5-y-6-ficha-guion.md`;
  - los manuales `docs/capitulos/cap-41.md` a `cap-50.md`, `interludio-2.md` y `extra-year-one-5-y-6.md`;
  - `docs/fable/004-guion-tanda-41-50.md`;
  - y las críticas de la sesión A.
- **Comprueba con grep en el texto** cada nombre, fecha, objeto o «primera vez» que toque un capítulo. Busca en:
  - `manuscrito/cap-*.md`;
  - `borradores/cap-*.md`, sin fichas;
  - `borradores/extra-year-one-*.md`, sin fichas;
  - `borradores/interludio-*.md`, sin fichas.

  Si el texto y el manual no coinciden, manda el texto.
- **Qué mirar:**
  1. **Fidelidad al guion aprobado:** motor, peldaño, deseo del lector, pantallazo y gancho de cada capítulo.
  2. **Los criterios de Fable 004:**
     - toda pieza que el lector necesita para una deducción de Lyra está en el texto antes de que la use. En el 50 son el retrato dormido y la viruela (41), la letra del sobre que ya no tiembla (49), las manos (41) y el viejo de la visión (46);
     - Harry hace algo con cada Horrocrux que sabe dónde está, o el texto dice por qué no.
  3. **La cuenta de lo que sabe cada uno** (continuidad §3 y §4, con todas las secciones «Lo que cambia en el NN» hasta el 50):
     - **Lyra no puede saber:** lo de Pettigrew en Azkaban, que Harry destruyó la diadema, ni nada del capítulo desde Harry;
     - **Harry no sabe** lo de Draco y el séptimo piso hasta que lo deduce (46-48);
     - **Granger sabe la primera capa desde el 48. Weasley, no.**
  4. **El saber de Harry falla** donde el guion lo dice (los dementores, el anillo de Gaunt, la casa del norte, el viejo) y acierta donde no depende del regreso (Umbridge, la pluma).
  5. **Continuidad ya detectada que hay que vigilar:**
     - la diadema se destruyó en **septiembre de 1994**, la primera noche del curso;
     - Pettigrew lo atraparon el 2 de febrero de 1994;
     - Lyra llevó la posdata de Narcissa **catorce meses** (33);
     - el retrato de Abraxas era el más bajo de los **cuatro** del despacho (2, 17, 41) y en el 50 lo han quitado;
     - el calentador de botón es de latón, del tamaño de un sickle, con clip (13), y Lyra lo tiró por un hueco del suelo de la Casa de los Gritos (14);
     - las clases con Snape son los jueves a las ocho (44);
     - el anillo de Lyra vuelve a ella en el 46: azul, sin ponérselo, en el bolsillo.
  6. **Escalera y racha** (handoff §3 y §4):
     - nunca dos capítulos planos seguidos;
     - como mucho un capítulo de cada cuatro sin escena de los dos;
     - **ningún beso** en esta tanda (es lo decidido);
     - «I love you» sale una sola vez (45) y no se vende como «primero» en boca del narrador.
  7. **Que no haya calco de la oficial.** Pasa el cotejo automático con los originales de referencia que da la cabecera de cada ficha:
     `python3 -I docs/notas/cotejo-oficial/ngramas.py 5 borradores/cap-NN-*.md "referencia/oficial-en/ko-AA.md,referencia/oficial-en/ko-BB.md"`

## 4. Decidir y aplicar

- **Decide con motivo.** Cada nota de la crítica y cada hallazgo propio se acepta, se acepta en parte o no se acepta, siempre con una razón de una línea. Formato: una tabla «Nota | Decisión | Motivo», como en `docs/notas/cap-41-critica.md`. Escribe:
  - `docs/notas/cap-NN-critica.md` para cada capítulo, con el veredicto y las puntuaciones de la crítica, el ranking y la tabla de decisiones;
  - y `docs/notas/revisiones/revision-tanda-41-50-codex.md` con lo de conjunto: continuidad entre capítulos, ritmo de la tanda y lo que queda para la tanda siguiente.
- **Aplica en el texto** con el mínimo cambio que resuelva la nota. Manda la voz del fic: frases variadas, densidad de novela, humor que sale del carácter, un lector listo, y que el narrador no explique lo que la escena ya mostró.
- **Después de aplicar:** cuenta las palabras (`wc -w`), vuelve a pasar los tics y repite el cotejo con la oficial.
- **En el mismo paso, pon al día:**
  - el manual del capítulo (`docs/capitulos/cap-NN.md`), con las escenas y frases literales que hayan cambiado, quién sabe qué y la continuidad fácil de romper;
  - `docs/capitulos/continuidad-transversal.md`, si algo cambia;
  - cualquier otro capítulo o manual que cite una frase literal cambiada;
  - `docs/estado-de-trabajo.md`, en «Ahora mismo», arriba del todo: qué hiciste y el siguiente paso exacto;
  - `docs/notas/autonomo/PARA-EL-AUTOR.md`: qué queda listo para subir (título y palabras) y cualquier ⚠.
- **Git:**
  - commits con rutas explícitas, uno por paso (crítica, arreglos, manuales);
  - después de cada commit, `git push -q origin HEAD && git push -q origin HEAD:main`;
  - el repositorio es privado y sigue siéndolo.

## 5. Dónde está cada cosa

| Qué | Dónde |
|---|---|
| Reglas del repositorio | `CLAUDE.md` |
| Lo vigente (motor, reglas, rumbo) | `docs/handoff-v3.0.md` |
| Estado | `docs/estado-de-trabajo.md` («Ahora mismo») |
| Guion de la tanda (aprobado) | `borradores/guion-tanda-41-50.md` |
| Fichas | `borradores/cap-NN-ficha-guion.md`, `interludio-2-ficha-guion.md`, `extra-year-one-5-y-6-ficha-guion.md` |
| Manuales | `docs/capitulos/cap-NN.md`, `interludio-2.md`, `extra-year-one-5-y-6.md` |
| Continuidad | `docs/capitulos/continuidad-transversal.md` |
| Encargo y rúbrica del crítico | `docs/critico-v2.0.md` |
| Notas de crítica (modelo) | `docs/notas/cap-41-critica.md`, `interludio-2-critica.md` |
| Cotejo con la oficial | `docs/notas/cotejo-oficial/ngramas.py` |
| Para el autor | `docs/notas/autonomo/PARA-EL-AUTOR.md` |
