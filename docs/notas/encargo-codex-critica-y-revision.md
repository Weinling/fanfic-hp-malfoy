# Encargo para Codex: crítica, revisión y arreglos de los capítulos nuevos

*30 de octubre de 2026. Preparado por la sesión principal (Claude) a petición del autor, Edén, que se lo pasa a Codex. Codex hace aquí tres papeles seguidos —crítico, revisor y quien aplica los arreglos—, siguiendo la estructura de trabajo de este repositorio. Háblale al autor en español; los capítulos están en inglés británico.*

---

## 0. El prompt para pegar

> Trabajas en el repositorio `/Users/eden/Documents/fanfic-hp-malfoy` (rama `claude/wizardly-albattani-vazqyr`). Es la adaptación al inglés británico de una fanfic coreana de Harry Potter con Lyra Malfoy, genderbend de Draco. Lee entero `docs/notas/encargo-codex-critica-y-revision.md` y síguelo al pie de la letra: primero la crítica a ciegas, después la revisión informada, después los arreglos, y por último manuales, continuidad, estado y nota para el autor. Capítulos de este encargo: **42** (sin crítica), y la revisión de conjunto del **41**, el ***Interlude: The Wrong Night*** y el **42**. Si hay capítulos nuevos escritos después (mira «Ahora mismo» en `docs/estado-de-trabajo.md`), haz con cada uno lo mismo que con el 42. Háblame en español.

---

## 1. Qué es esto y qué no se toca

- **El proyecto:** `CLAUDE.md` (léelo primero) y `docs/handoff-v3.0.md` (identidad, motor, reglas de escritura, tics, rumbo). La historia va por el quinto curso, verano de 1995.
- **No se toca nunca:** `manuscrito/` (lo publicado; una errata se apunta en `docs/notas/erratas-publicado.md`), `coreano/`, `fuentes/`, `referencia/` (solo consulta). Ni los hechos aprobados del guion (`borradores/guion-tanda-41-50.md`, aprobado por el autor) ni el rumbo (handoff §8). Un arreglo cambia frases, orden, énfasis, una línea de continuidad; si una nota pide cambiar un hecho del guion, no se aplica: se apunta en `docs/notas/autonomo/PARA-EL-AUTOR.md` con ⚠.
- **Contenido:** los personajes tienen quince años. Nada sexual ni sensual.
- **Convenciones de prosa:** comillas y apóstrofos tipográficos (“ ” ’), separador de escena `⁂`, cursivas con `*…*`, «Mr» y «Mrs» sin punto, ortografía británica. En el punto de vista de Lyra, Harry es «Potter»; en el de Harry, ella es «Malfoy» o «she», y «Lyra» solo en momentos marcados.
- **Extensión:** de 3.000 a 4.200 palabras por capítulo; si recortar pierde más de lo que gana, no se recorta.
- **La oficial no se calca:** ninguna línea nuestra sale de la traducción inglesa oficial (`referencia/oficial-en/ko-NN.md`). Tras cada arreglo, el cotejo automático:
  `python3 -I docs/notas/cotejo-oficial/ngramas.py 5 borradores/cap-NN-*.md "referencia/oficial-en/ko-AA.md,referencia/oficial-en/ko-BB.md"` (los originales de referencia de cada capítulo están en la cabecera de su ficha), más un grep de las frases cortas.

## 2. Primer papel: el crítico (a ciegas)

El crítico juzga como un lector listo de Wattpad, **sin saber lo que viene**.
- **Lee:** `docs/critico-v2.0.md` §1 a §6 (encargo y rúbrica); `docs/notas/critico-arranque-29.md` §2 y `docs/notas/critico-arranque-31.md`; las notas de crítica `docs/notas/cap-3*-critica.md`, `cap-40-critica.md`, `cap-41-critica.md`, `interludio-1-critica.md` e `interludio-2-critica.md` (te dicen qué se pidió, qué se aceptó y qué tics han ido cayendo); y el **texto completo**, en orden de lectura: `borradores/cap-31-whether-i-do.md`, `cap-32-plain-silver.md`, `interludio-1-the-seventh-lock.md`, `cap-33` a `cap-40`, `cap-41-the-sleeve.md`, `interludio-2-the-wrong-night.md`, `cap-42-badges.md`.
- **En este papel no leas:** fichas, guiones, resúmenes, `docs/handoff-*`, `docs/capitulos/`, `docs/estado-de-trabajo.md`, `docs/fable/`, `docs/notas/autonomo/`, `docs/notas/lo-que-sabe-harry.md` (llevan trama futura o el secreto de Harry).
- **Formato:** el de la sección 6 de `docs/critico-v2.0.md` (veredicto; puntuaciones de 1 a 10 en emoción, romance, gancho, ritmo, calor, trama, personajes y prosa; las tres preguntas del lector de Wattpad; lo que funciona; problemas por prioridad, graves/medios/menores, cada uno con su línea y una propuesta concreta; prosa y tics; y el **ranking acumulado** del 31 en adelante). Último ranking: 39 ≈ 40 > Interludio 2 ≈ Interludio 1 ≈ 32 ≈ 37 > 35 ≈ 38 > 41 ≈ 33 ≈ 36 > 34 > 31.
- **Tics que hay que buscar** (handoff §4 y la lista viva): «did not» como señal de emoción (máx. ~4 por mil palabras); «She did not need to»; «she found (that)»; «at all» (dos, mejor en diálogo); «the way…» en serie; «for a long moment»; «all at once»; «before she had decided to» y variantes; lecturas de cara; la cara quieta; «held his eyes»; la sonrisa de la madre para las esposas de los ministros; «Lyra read it twice»; «It came out…»; «No X. Y.» (una por capítulo); «never once»; la coletilla con «which» (tres); símiles «like a man»/«as a man»; la metáfora de las sumas para pensar; la vela que se apaga; frases recicladas de capítulos anteriores (el té frío, «held on», «beautifully», la sábana, «a book she was not reading», «like a shell», «the far end of the train»).

## 3. Segundo papel: el revisor (informado)

Ahora sí lees lo planeado, para comprobar fidelidad y continuidad.
- **Lee:** `docs/handoff-v3.0.md` entero; `docs/capitulos/continuidad-transversal.md`; `borradores/guion-tanda-41-50.md` (§0, los capítulos escritos y el siguiente, §5 «Avisos», §7 «Hilos», §8 «Fable 004»); las fichas `borradores/cap-41-ficha-guion.md`, `interludio-2-ficha-guion.md`, `cap-42-ficha-guion.md`; los manuales `docs/capitulos/cap-41.md`, `interludio-2.md`, `cap-42.md`; `docs/fable/004-guion-tanda-41-50.md`; y los originales de referencia de cada capítulo (`referencia/oficial-en/ko-54.md`, `ko-55.md`, `ko-56.md`, `ko-62.md`), solo para comprobar que no hay calco.
- **Comprueba con grep en el texto** (`manuscrito/cap-*.md`, `borradores/cap-*.md` sin fichas, `borradores/extra-year-one-*.md`, `borradores/interludio-*.md` sin fichas) cada nombre, fecha, objeto o «primera vez» que toquen los capítulos. Manda el texto, no el manual.
- **Qué mirar:**
  1. **Fidelidad al guion aprobado:** motor, peldaño, deseo del lector, pantallazo, gancho de cada capítulo; las etiquetas «se queda/cambia/sustituye/nuevo».
  2. **Los criterios de Fable 004:** cada pieza que el lector necesita para una deducción de Lyra está en el texto antes (sobre todo el abuelo Abraxas: retrato dormido y viruela en el 41; la lista de Draco en el 42); Harry hace algo con cada Horrocrux que sabe dónde está, o el texto dice por qué no.
  3. **La cuenta de lo que sabe Lyra** (continuidad §3 y §4): que no olvide lo que sabe (el norte, la Marca, Crouch hijo vivo, la primera capa de Harry, sus dos mentiras) ni sepa lo que no puede saber (Pettigrew en Azkaban, la diadema destruida, quién es el señor de la casita).
  4. **El saber de Harry falla** donde el guion dice (los dementores, el anillo) y acierta donde no depende del regreso.
  5. **Continuidad ya detectada que hay que vigilar:** la diadema se destruyó en **septiembre de 1994**, la primera noche del curso (no en verano); Pettigrew, atrapado el 2 de febrero de 1994; la posdata de Narcissa la llevó Lyra **catorce meses** (33); el retrato de Abraxas es uno de los **cuatro** del despacho (2, 17); Lyra estaba **en la hierba** junto al podio (38); el primer callejón Diagon de Lyra no puede contradecir Madam Malkin’s (16).
  6. **Escalera y racha** (handoff §3 y §4): ningún capítulo plano dos veces seguidas; escena de los dos (como mucho uno de cada cuatro sin ella); ningún beso en esta tanda.

## 4. Tercer papel: aplicar

- **Decide con motivo.** Cada nota del crítico y del revisor se acepta, se acepta en parte o no, siempre con una razón de una línea. Formato de referencia: `docs/notas/cap-41-critica.md` (veredicto, puntuaciones, ranking y una tabla «Nota | Decisión | Motivo»). Escribe `docs/notas/cap-42-critica.md` así, y una sección «Revisión de conjunto 41-42» con lo del revisor, en `docs/notas/revisiones/revision-41-42-codex.md`.
- **Aplica en el texto** (`borradores/cap-NN-*.md`) con el mínimo de cambio que resuelva la nota: la voz del fic manda (frases variadas, densidad de novela, humor que sale del carácter, el lector es listo, no se explica lo que la escena ya mostró).
- **Después de aplicar:** recuento de palabras (`wc -w`), pasada de tics otra vez y cotejo con la oficial.
- **Pon al día, en el mismo paso:**
  - el manual del capítulo (`docs/capitulos/cap-NN.md`): escenas, frases literales que hayan cambiado, quién sabe qué, continuidad fácil de romper;
  - `docs/capitulos/continuidad-transversal.md` («Lo que cambia en el NN»), si cambia algo;
  - si una frase literal cambia y se cita en otro capítulo o manual, cámbiala allí también;
  - `docs/estado-de-trabajo.md`, sección «Ahora mismo», arriba del todo: qué hiciste y el siguiente paso exacto;
  - `docs/notas/autonomo/PARA-EL-AUTOR.md`: qué capítulos quedan listos para subir (título y palabras) y cualquier ⚠.
- **Git:** commits con rutas explícitas, uno por paso (crítica, arreglos, manuales), y `git push -q origin HEAD && git push -q origin HEAD:main` tras cada uno. El repositorio es privado y sigue siéndolo.

## 5. Dónde está cada cosa

| Qué | Dónde |
|---|---|
| Reglas del repositorio | `CLAUDE.md` |
| Lo vigente (motor, reglas, rumbo) | `docs/handoff-v3.0.md` |
| Estado | `docs/estado-de-trabajo.md` («Ahora mismo») |
| Guion de la tanda (aprobado) | `borradores/guion-tanda-41-50.md` |
| Capítulos | `borradores/cap-41-the-sleeve.md`, `interludio-2-the-wrong-night.md` (va entre el 41 y el 42), `cap-42-badges.md` |
| Fichas | `borradores/cap-NN-ficha-guion.md`, `interludio-2-ficha-guion.md` |
| Manuales | `docs/capitulos/cap-NN.md`, `interludio-2.md` |
| Continuidad | `docs/capitulos/continuidad-transversal.md` |
| Encargo del crítico | `docs/critico-v2.0.md` |
| Notas de crítica | `docs/notas/cap-NN-critica.md` |
| Cotejo con la oficial | `docs/notas/cotejo-oficial/ngramas.py` |
| Para el autor | `docs/notas/autonomo/PARA-EL-AUTOR.md` |
