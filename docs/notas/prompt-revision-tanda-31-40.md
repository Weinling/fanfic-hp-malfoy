# Prompt de inicio: revisión de la tanda 31-40 y del plan de la 41-50

*24 de octubre de 2026. Para pegar al abrir una sesión nueva.*

---

Eres la sesión principal del proyecto «Never Owe a Malfoy, Potter» (/Users/eden/Documents/fanfic-hp-malfoy): la adaptación al inglés británico de una fanfic coreana de Harry Potter con Lyra Malfoy, genderbend de Draco. Háblale al autor, Edén, en español.

**Esta sesión no escribe capítulos.** Es una sesión de análisis, revisión y crítica: de la tanda 31-40 (escrita en modo autónomo el 23 y 24 de octubre, con el *Interludio 1*) y de lo que tenemos planeado para la 41-50. No toques `manuscrito/` ni los capítulos de `borradores/` sin que el autor apruebe los cambios.

**0. Antes de nada.** Trabaja en la rama `claude/wizardly-albattani-vazqyr` (`git pull -q origin claude/wizardly-albattani-vazqyr`). Crea el cerrojo (`date > .autonomo.lock`) para que la tarea programada nocturna no escriba a la vez, y bórralo al terminar.

**1. Lee, en este orden:**
1. `CLAUDE.md`, `docs/notas/autonomo/ARRANQUE.md` (para saber cómo se ha trabajado; no sigas su flujo de escritura), la sección «Ahora mismo» de `docs/estado-de-trabajo.md`, `docs/handoff-v3.0.md` entero y `docs/capitulos/continuidad-transversal.md`.
2. **La historia entera en texto completo:** `manuscrito/cap-01` a `cap-15`; `borradores/cap-16` a `cap-40` (sin fichas, guiones ni `cap-29-lector.md`); los cuatro `borradores/extra-year-one-*` (sin fichas); y `borradores/interludio-1-the-seventh-lock.md`, que va entre el 32 y el 33. Son unas 200.000 palabras. Si el contexto no da para todo, lee enteros del 24 al 40 y el interludio, y del 1 al 23 y los *Year One*, sus manuales (`docs/capitulos/`). Apunta qué leíste.
3. **Lo que se planeó y se decidió:** `borradores/guion-tanda-31-40.md`; las fichas `borradores/cap-32-ficha-guion.md` a `cap-40-…` e `interludio-1-ficha-guion.md`; las críticas `docs/notas/cap-31-critica.md` a `cap-40-critica.md` (la del 40 trae la valoración del arco) e `interludio-1-critica.md`.
4. **El rumbo y lo que viene:** `docs/notas/ideas-divergencias.md`, `docs/notas/ideas/poda-agente.md`, `docs/fable/001-divergencias.md`, `docs/fable/002-mundo-harry-y-tanda-41.md`, `docs/notas/lo-que-sabe-harry.md`, `docs/notas/sesion-nueva-tanda-41.md` y `borradores/cap-41-arranque-harry-borrador.md`.
5. **El original, para comparar.**
   - **Resúmenes:** `borradores/resumen-coreano-26-35.md` y `borradores/resumen-oficial-36-54.md` (lo que cubre la tanda), `borradores/resumen-oficial-55-73.md` (lo que viene) y las cabeceras y tablas de `-74-92.md` y `-93-111.md` (el resto).
   - **Enteros, solo estos** (bastan para la identidad y las semejanzas; no hace falta leer los 18 de la tanda): `coreano/ko-35.md` (el Baile), `referencia/oficial-en/ko-46.md` (la ruptura), `ko-49.md` (Crouch y la nota), `ko-50.md` (el regreso y el espejo) y, de la tanda nueva, `ko-52.md` y `ko-53.md` (los extras de primero) y `ko-54.md` y `ko-55.md` (el verano de 1995).
   - **Más, si te hace falta** para una comparación concreta: un capítulo entero o el agente `lector` con una pregunta concreta.

**2. Qué tienes que juzgar,** con citas (archivo y frase) y sin calcar nunca la oficial:
1. **¿La tanda 31-40 sigue bien el camino?** Contra el rumbo aprobado (handoff §8 y §7), el motor (§3) y las reglas (§4). ¿Cumple lo prometido (Moody es Moody, Lyra destapa a Crouch, el Baile, la deducción del secreto, la ruptura)? ¿Qué queda flojo?
2. **Identidad frente al original.** ¿En qué se parece todavía (el esqueleto, el orden de los momentos, escenas que conservan su forma) y en qué es ya otra historia? ¿La desviación es demasiado ligera, justa o excesiva? ¿Dónde convendría alejarse más, o volver?
3. **Continuidad y coherencia de la historia entera.** Choques entre capítulos, lo que Lyra olvida que sabe, hilos abandonados, fichas perdidas y deudas sin pagar. Y el saber de Harry: ¿falla lo bastante?
4. **Personajes:** Lyra (¿activa o testigo?), Harry (¿galán, demasiado sabio?), Crabbe, Granger, Weasley, Lucius, Narcissa, Moody. ¿Qué arco está cojo?
5. **El interludio desde Harry y la política de capítulos desde Harry** (Fable 002, D4): ¿funciona?, ¿hacen falta más, y dónde?
6. **Los extras previstos** (*Year One* 5 y 6, originales 52 y 53; *Year Two* 1 y 2, originales 76 y 77) y la idea de extras propios: ¿se hacen?, ¿dónde?, ¿qué tendría que cambiar?
7. **El plan de la 41-50** (`sesion-nueva-tanda-41.md`, Fable 002, el borrador del 41, el recuento de unos 32 capítulos): ¿falta algo, sobra algo, hay que cambiar algo antes de escribir el guion? Revelaciones propias que faltan o que el original explica mal.
8. **Lo que retocarías en lo escrito del 31 al 40, o antes,** por prioridad, con el coste (qué está publicado: Webnovel llega al 30).

**3. Entrega.**
- **Un informe** en `docs/notas/revisiones/revision-tanda-31-40.md`, con: veredicto en una página; los ocho puntos; una lista priorizada de cambios (retoques a lo escrito y cambios al plan); y las decisiones que tiene que tomar el autor, cada una con tu recomendación y explicada sin códigos internos.
- **Si dudas de algo de rumbo**, puedes consultar a `fable-revisor` (como mucho dos veces, con dosier en `docs/fable/003-…`; skill `metodo-equipo`).
- **Al terminar:** commit y push a la rama y a `main`, la línea en «Ahora mismo» del estado, borra el cerrojo, y dale al autor en el chat el resumen y las preguntas.
