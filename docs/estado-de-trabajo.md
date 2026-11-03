# Estado de trabajo

**Léelo lo primero** al abrir sesión o tras compactar. Se actualiza en cada paso (escena escrita, crítica aplicada, capítulo cerrado) y va en el mismo commit que el paso.

Última actualización: 3 de noviembre de 2026.

## Ahora mismo

- **EN CURSO (3 de noviembre, sesión de reestructura; cerrojo puesto).** Manda `docs/notas/prompt-sesion-reestructura.md`. Todo va en `docs/notas/reestructura/`. **Lecturas hechas, en texto:** CLAUDE.md, ARRANQUE, handoff, continuidad, del 38 al 50, Int. 2, Y1 5 y 6, del 23 al 37, Int. 1, 16, Y1 1 a 4, 3, 7, 10, 12, 13, 14, 19, 21, 22; lo-que-sabe-harry, ideas-divergencias, poda, Fable 001-004, guion 41-50 (§0, §7, §8), propuesta de Codex, valoración, contexto, revisión integral, crítica de la tanda, edición integral, resúmenes de la oficial 55-111. **Sin leer en texto:** el resto del 1 al 22 (solo continuidad). **Hecho:** paso 1, `auditoria.md`; paso 2, `decisiones.md` en borrador. **Lanzada la consulta a Fable 005** (`docs/fable/005-decisiones-reestructura.md`; primera de dos). **Siguiente paso exacto:** pegar la respuesta de Fable en el dosier, corregir `decisiones.md`, apuntarlo en `docs/fable/REGISTRO.md`, y enseñárselo al autor (puerta 1). No empezar el guion general hasta que conteste. Agentes vivos: Fable 005.

- **3 de noviembre: LEE PRIMERO `docs/notas/prompt-sesion-reestructura.md`, que manda sobre todo lo de abajo.** La rama de Codex (`codex/revision-integral-35-50`, los capítulos 35-50 revisados) está fusionada en la rama de trabajo y en `main`: es la versión vigente. **Publicado hasta el 37.** Decisiones del autor del 3 de noviembre en el handoff (antes del §3). Documentos de Codex copiados a `docs/notas/ideas/codex/`. Valoración de la sesión anterior: `docs/notas/ideas/valoracion-propuesta-identidad-3-nov.md`. **Siguiente paso exacto:** abrir sesión nueva con ese prompt. Agentes vivos: ninguno. Cerrojo: borrado.

- **1 de noviembre de 2026 — revisión integral autorizada por Edén en Codex.** Lectura completa terminada: capítulos 1–50, seis *Year One* y dos interludios (58 textos, unas 224.800 palabras). El autor confirma que del 35 en adelante no está publicado. Encarga corregir continuidad y lógica, reducir atribuciones redundantes de diálogo y sobreexplicaciones, conservando claridad y voz. **Esta revisión va en `codex/revision-integral-35-50`, para comparar antes de incorporar; no se sube a `main` ni a las plataformas.** Lo principal del 1 al 34 se conserva. Trabajo editorial y siguiente paso en `docs/notas/revisiones/edicion-integral-35-50.md`. No hay subagentes activos. Esta entrada prevalece sobre los siguientes pasos históricos de octubre.
- **EDICIÓN Y COMPROBACIONES TERMINADAS; RAMA SUBIDA POR GIT:** revisados los **19 textos** (35–50, interludio 2, Year One 5–6); continuidad, manuales y handoff sincronizados. Revisado el diff del 35–43 y releídos íntegros los textos revisados del 44–50 y los tres extras. Los otros **39 textos permanecen idénticos** al commit base; escenas, citas, comillas y formato comprobados. Recuento: 60.230 → 56.909 palabras; «said», 556 → 420. La edición narrativa está en `ebad71b`, rama `codex/revision-integral-35-50`. Siguiente: el autor sustituye los 19 borradores usando esta rama y decide cuándo incorporarla. Git resolvió el 403 del conector; no hace falta reconectar. No se ha escrito en `main` ni publicado en las plataformas.

- **EN CURSO (28 de octubre, sesión de la tanda 41-50, con el autor en el chat; cerrojo creado a las 21:51): el guion de la tanda 41-50.** Prompt: `docs/notas/prompt-tanda-41-50.md`.
  - **Hecho:** las decisiones 2 a 9 del autor (todas como se recomendaban) apuntadas en el handoff §7, §8 y §10, en `docs/notas/sesion-nueva-tanda-41.md` y en la continuidad (e249dde). **Guion escrito**: `borradores/guion-tanda-41-50.md` (2c4ee23). Fable 004: «aceptable con cambios», todos aplicados al guion (§8) y al handoff §8 (la diadema, ya destruida por Harry) (5372d6e). PARA-EL-AUTOR al día. Agentes vivos: ninguno.
  - **Lecturas hechas:** `CLAUDE.md`, el arranque, el prompt de la tanda, el handoff entero, la continuidad entera, la nota de sesión, la revisión 31-40 entera, el texto completo del 24 al 40 y del *Interludio 1*; del 1 al 23 y los *Year One*, **solo la continuidad transversal y grep** (el contexto no daba para los manuales enteros); Fable 001, 002 y 003; `lo-que-sabe-harry.md`, `ideas-divergencias.md`, `poda-agente.md`; el borrador del arranque desde Harry; el guion 31-40 (formato, §0, cap. 31, §3 a §7); los resúmenes de la oficial del 52 al 73 y las tablas del 74 al 92.
  - **Guion APROBADO por el autor (29 de octubre, en el chat).** Escritos y subidos: **41, *The Sleeve*** (~3.060; criticado y cerrado); ***Interlude: The Wrong Night*** (Interludio 2, entre el 41 y el 42; ~3.730; criticado y cerrado; la diadema pasa a **septiembre de 1994**, cambiado en handoff, guion y PARA-EL-AUTOR); **42, *Badges*** (~2.930; ficha, manual y continuidad hechos; **sin crítica**).
- **30 de octubre, por decisión del autor:** la crítica, la revisión y los arreglos del 42 (y la revisión de conjunto del 41, el interludio 2 y el 42) los hace **Codex**, con el encargo `docs/notas/encargo-codex-critica-y-revision.md` (§0 trae el prompt para pegar). El crítico Claude de esta sesión muere con ella.
- **30 de octubre, al final: LA TANDA 41-50 ESTÁ ESCRITA ENTERA** (por decisión del autor, sin crítica del 42 en adelante). Escritos, con ficha corta, manual y continuidad: 42 *Badges*, *Year One* 5 *The Forest* y 6 *The Black Pieces*, 43 *Prefects*, 44 *Rounds*, 45 *Lines*, 46 *Where the Sea Is*, 47 *Pretext*, 48 *Him, and Now You*, 49 *The Button Warmer*, 50 *The East Cottage*. Handoff §1 y §9 al día. **La crítica y la revisión las hace Codex** con `docs/notas/encargo-codex-critica-y-revision.md` (dos sesiones: A, el crítico a ciegas; B, el revisor que decide y aplica; los prompts en el §0). **30 de octubre, último momento:** dos críticos Opus (Claude) **han criticado a ciegas** el 42 a 50 y los *Year One* 5 y 6, en `docs/notas/criticas-opus/` (con `tanda-41-50.md`; todo commiteado; nada aplicado). Con ellos, Codex puede saltarse la sesión A del encargo y hacer solo la B (leer esas críticas como de otra persona, decidir y aplicar). **Siguiente paso exacto:** que Codex haga la revisión (sesión B, y la A si faltan críticas); después (Claude), el guion de la tanda 51-56 con lectura de tanda nueva (la tanda 41-50 entera en texto, y del resto los manuales) y consulta a Fable. Agentes vivos: ninguno. Cerrojo: borrado.

- **HECHO Y APROBADO POR EL AUTOR (24 de octubre): reescritos los calcos de la oficial en el 33-40 y sus ecos** (tabla en `docs/notas/cotejo-oficial/calcos-31-40.md`; el 33 se llama ahora *The Corner Table*). Aprobado; subido a la rama y a `main`. Lo siguiente sigue siendo el guion de la tanda 41-50, cuando el autor tome las decisiones del §4 de la revisión (`docs/notas/revisiones/revision-tanda-31-40.md`). **Si se compacta, lee `docs/notas/sesion-calcos-31-40.md`**: reglas, lista de frases con su línea y casillas de estado. Hasta que el autor apruebe, commit y push solo a la rama. Cerrojo creado.

- **HECHO (24 de octubre, sesión de revisión, sin tocar capítulos): revisión de la tanda 31-40 y del plan de la 41-50**, en `docs/notas/revisiones/revision-tanda-31-40.md` (leída la historia entera en texto, lo planeado, el rumbo, los resúmenes y los originales que pedía el encargo; consulta a Fable 003, «aceptable con cambios»). Lo principal: una docena de frases del 33 al 40 calcan la oficial (reescribir antes de publicar); el 41 debería abrir desde Lyra en la Mansión y cobrar el coste de Crouch; la tanda 41-50, hasta la Navidad del quinto, con un pago a mitad; faltan en el plan Draco en Hogwarts, Sirius y su muerte sabida, Pettigrew, el mapa, Snape y el Ministerio en el colegio. **Nueve decisiones para el autor en el §4 del informe.** El guion 41-50 espera a que las tome. Script de cotejo con la oficial: `docs/notas/cotejo-oficial/ngramas.py`.

- **HECHO (24 de octubre, con el autor):** decisiones de Fable 002 (handoff §7 y §10; dos líneas en el 39) y el ***Interludio 1*, «The Seventh Lock»**, desde Harry, entre el 32 y el 33 (`borradores/interludio-1-the-seventh-lock.md`; ficha, crítica y manual `docs/capitulos/interludio-1.md`); el relato del baúl del 33, recortado. El siguiente paso exacto no cambia (abajo).

- **MODO AUTÓNOMO ACTIVO (23 de octubre).** Lee primero `docs/notas/autonomo/ARRANQUE.md`. **SIGUIENTE PASO EXACTO: el guion de la tanda 41-50** (el verano de 1995 y el quinto), siguiendo `docs/notas/sesion-nueva-tanda-41.md`: lectura de tanda nueva (ARRANQUE §2: la historia entera, unas 196.000 palabras, más el rumbo y los resúmenes de la oficial del tramo), decidir qué capítulos del original cubre, escribir `borradores/guion-tanda-41-50.md` con el formato del de la tanda anterior, y consultar a `fable-revisor` con dosier en `docs/fable/`. Después, la ficha del 41. Agentes vivos: ninguno (el crítico de la sesión murió con ella; el siguiente se lanza nuevo según el §5, leyendo completo desde el 24 hasta el 40, o desde el 31 si el contexto no da: decidirlo y apuntarlo).

- **HECHO (sesión autónoma del 23 de octubre, de las 20:37 a las 22:00 por el reloj de la máquina): del 32 al 40, escritos, criticados y cerrados. La tanda 31-40 y el cuarto curso están terminados.** «Plain Silver» (32), «Tomorrow Still Comes» (33), «Sneakoscope» (34), «Spectacle» (35), «Below Stairs» (36), «The North» (37), «The Cup» (38), «Never Lied» (39), «Hidden Ink» (40), en `borradores/cap-3N-*.md` y `cap-40-hidden-ink.md`; fichas `borradores/cap-NN-ficha-guion.md`; críticas y decisiones `docs/notas/cap-NN-critica.md` (la del 40 trae la valoración del arco y qué vigilar en la tanda siguiente); manuales `docs/capitulos/cap-NN.md`; continuidad transversal, handoff (§1, §3, §8, §9) y `docs/notas/lo-que-sabe-harry.md` al día. Todo subido a la rama y a `main`. Lecturas hechas en la sesión: CLAUDE.md, el arranque, el estado, el handoff entero, la continuidad, el guion de la tanda entero, los manuales del 27 al 31, el texto del 29 al 31, el coreano 35, la oficial 36 a 40 y 43 a 51, `lo-que-sabe-harry.md` y la ficha del 31. Para el autor: `docs/notas/autonomo/PARA-EL-AUTOR.md`.

- (Superado:) La primera nota del modo autónomo decía «Siguiente paso exacto: la ficha del 32». Hecho. Temporizador: la tarea programada «Never Owe: sesión autónoma nocturna» arranca una sesión nueva cada noche a la 1:07 y a las 4:07.

- **HECHO (23 de octubre): el 31, «Whether I Do», cerrado** (`borradores/cap-31-whether-i-do.md`, ~4.080 palabras). Criticado por el crítico vivo (`docs/notas/cap-31-critica.md`; ranking: junto al 30) y arreglos aplicados; nota enviada. **Cambio sobre la ficha aprobada:** el «Krum, is it?» de Moody se quitó (lo de Krum ya era público, así que no probaba nada) y la escena del barco acaba en Karkaroff. Manual (`docs/capitulos/cap-31.md`), continuidad y handoff al día. **Siguiente: la ficha del 32**, leyendo entero el coreano 35 como capítulo de referencia (la regla nueva) y el guion de la tanda. El crítico sigue vivo y espera el 32.
- **Regla nueva (23 de octubre), ya en el handoff §1 y en `CLAUDE.md`:** desde el 31, la ficha de cada capítulo se hace leyendo enteros sus uno o dos capítulos de referencia del original (el coreano hasta el 35; del 36 en adelante, la traducción oficial de `referencia/oficial-en/`, del mismo autor, como guía de trama y escenas, nunca para la frase) y readaptándolos. La ficha cierra con lo que se quita del original y por qué.
- **Publicación (23 de octubre):** en Webnovel está todo hasta el 30 y los cuatro *Year One*. El autor subió por error el *Year One* 4 antiguo como «actualización» y lo sustituye por el texto bueno, con una nota de disculpa. Hace falta el 31 y los siguientes.
- **La nota `sesion-nueva-31.md` queda cumplida** (ficha del 31 hecha y aprobada; crítico nuevo lanzado). Siguiente tras el 31: la ficha del 32, con el coreano 35 entero como referencia.

- **HECHO (19 de octubre): el *Year One* 4 rehecho, «What Scared Actually Is»** (`borradores/extra-year-one-4-what-scared-actually-is.md`, ~6.100 palabras; ficha aprobada con las cuatro recomendaciones; escrito escena a escena; pasada de tics hecha; manual, continuidad, `lo-que-sabe-harry.md` y handoff al día). El archivo se renombró desde `extra-year-one-4-two-words.md`; la versión publicada en Webnovel: `git show 9746d09:borradores/extra-year-one-4-two-words.md`. **Sin crítica todavía.** El autor retiene el 4 en Wattpad (el 20 sube solo el 3) y lo sustituirá en Webnovel con la nota *Year One, Part 4 revised: same corridor, a different fear.* **Pendiente del autor:** si se queda con 6.100 palabras o se recorta; si el crítico nuevo lee también este (además del *Year One* 2 y el 31), avisando antes del coste. Análisis previo: `docs/notas/year-one-4-rehacer.md`.
- **CRÍTICA HECHA (19 de octubre): los *Year One* 2 y 4 rehechos**, por el crítico nuevo (Opus; vivo, se reutiliza para el 31; ya tiene la nota). Crítica y decisiones: `docs/notas/extra-year-one-2-y-4-rehechos-critica.md`. Arreglos aplicados en los dos y en sus manuales. El 4 entra en el grupo de cabeza del ranking; el 2 sube a la mitad alta. Ahora: el 2, ~5.420 palabras; el 4, ~6.000. El autor sube los dos a Webnovel con nota cuando quiera (el 2: *Year One, Part 2 revised: same fir tree, a different Christmas*; el 4: *Year One, Part 4 revised: same corridor, a different fear*).
- **FICHA DEL 31 HECHA (19 de octubre), espera la aprobación del autor:** `borradores/cap-31-ficha-guion.md` (con la historia entera leída hoy; cinco decisiones en «Para decidir»). No se escribe hasta que la apruebe. Leído para ella, además de la historia entera: el guion de la tanda (§0, cap. 31 y 32, §3 a §7), los coreanos 34 y 35, el resumen de la oficial del 36 y la ficha del 30 como formato. La lectura completa de hoy sirve para el 31 si no se compacta; si se compacta, el protocolo corto de esa nota.
- **SESIÓN NUEVA (preparado el 19 de octubre): lee `docs/notas/sesion-nueva-31.md` justo después de este estado.** Dice qué leer (el protocolo corto, unos 60.000 tokens; la historia entera no) y qué hacer: la ficha del 31, que aprueba el autor; luego escribirlo; el crítico nuevo, avisando antes del coste, para el 31 y el *Year One* 2. Todo lo de abajo está hecho y subido.
- **HECHO (18 de octubre): el *Year One* 2, rehecho y escrito** (`borradores/extra-year-one-2-nobody-asked-you.md`, ~5.520 palabras; ficha aprobada; manual y continuidad al día). Sin crítica todavía: se decide con el autor si lo lee el crítico nuevo del 31. La versión publicada en Webnovel: `git show a87b54e:borradores/extra-year-one-2-nobody-asked-you.md`. El autor lo sube a Wattpad, y en Webnovel sustituye al publicado, con una nota.
- **Después: la ficha del 31** (guion de la tanda aprobado; handoff v3.0, §9). Antes de lanzar el crítico nuevo, avisar al autor del coste.
- **HECHO hoy, tras la aprobación del guion:** guion marcado como aprobado; §18 del handoff v2.0; la silla que cruje en el palco del 24 (manual y continuidad al día; hay que volver a subirlo en Webnovel); **handoff v3.0** (corto, solo lo vigente) y **protocolo de lectura aligerado** en `CLAUDE.md`, ambos por encargo del autor.
- (Superado por `sesion-nueva-31.md`:) **Si se compacta ahora:** seguir el protocolo nuevo de `CLAUDE.md` («a mitad de tanda»): este estado, el handoff v3.0, la continuidad transversal, el guion de la tanda, los manuales del 27 al 30 y el texto completo del 29 y el 30. Para el *Year One* 2: su ficha, el texto actual del *Year One* 2 y el del 1 y el 3, y sus manuales.

- **GUION DE LA TANDA REPASADO (18 de octubre, sesión nueva, protocolo completo). Espera la aprobación del autor.** Leída la historia entera en texto completo (ver «Lecturas hechas»). Repaso hecho contra el texto: los tres fallos del §6 resueltos y diez correcciones más, cada una en su escena con la marca **[Repaso]** y juntas en el §6 del guion; hilos sin tocar en el §7. La más grande: la teoría de Harry sobre Moody pasa de la multijugos al Imperius, porque Harry tuvo el mapa con los nombres de verdad hasta después del Cáliz. **No se escribe nada del 31 hasta que el autor lo apruebe.** Errata corregida en el 28 (una comilla de más), que sube hoy a Webnovel. Publicación confirmada con el autor y puesta en `CLAUDE.md`. Siguiente, con el guion aprobado: el §3, puntos 3 a 6, de `sesion-nueva-guion-31.md` (handoff §18, la silla del 24 si se aprueba, la ficha del 31 y el crítico nuevo, avisando antes del coste).
- (Anterior:) **SESIÓN NUEVA (preparado el 18 de octubre, al final): lee `docs/notas/sesion-nueva-guion-31.md` justo después de este estado.** El guion de la tanda se escribió sin la historia entera en contexto (solo el 29 y el 30 en texto completo) y ya tiene tres fallos encontrados (§6 del guion). Decisión del autor: una sesión nueva lee la historia entera, repasa el guion y se lo lleva para aprobar. El autor dice que está publicado hasta el 26: hay que confirmarlo y poner al día `CLAUDE.md`.
- (Anterior:) **Guion de la primera tanda (del 31 al 40, original 34 a 51): ESCRITO (18 de octubre), en `borradores/guion-tanda-31-40.md`. Espera la aprobación del autor y sus respuestas a las nueve decisiones del §4.** No se escribe nada del 31 hasta entonces. El autor dio por buena, para este guion, la lectura de la historia entera del 18 de octubre; el resto del protocolo está hecho (ver «Lecturas hechas»).
- **Retoque del 30: HECHO y cerrado (18 de octubre).** La nota `docs/notas/sesion-nueva-30.md` queda cumplida salvo su §4. **Siguiente:** (1) avisado el autor de lo que puede subir: del 25 al 30, retocados y cerrados, nunca publicados (Webnovel llega al 24; Wattpad, al 22), y el 24 rehecho si aún no lo ha cambiado en Webnovel; (2) preparar el **guion detallado de la primera tanda**, del 31 al final del cuarto (original 34 a 51), escena por escena, para que lo apruebe el autor antes de escribir. **Antes del 31 vuelve el protocolo completo de lectura**; preguntar al autor si basta la lectura de la historia entera del 18 de octubre.
- (Anterior:) **SESIÓN NUEVA (preparado el 18 de octubre, al final): lee `docs/notas/sesion-nueva-30.md` justo después de este estado.** Es el retoque del 30, con una lectura reducida que ha autorizado el autor. La nota anterior (`sesion-nueva-18-oct.md`) ya está cumplida.
- (Anterior:) **lee `docs/notas/sesion-nueva-18-oct.md`**, ya cumplida. Dice dónde estamos, qué quiere el autor, las tareas en orden y qué leer. Lo de abajo es el detalle del 17 y el 18 de octubre.
  - **Abierta ya (18 de octubre):** lectura del §4 hecha (ver «Lecturas hechas en esta sesión», al final).
  - **DECIDIDO por el autor (18 de octubre): ideas primero.** Del 25 al 30 no se toca nada todavía. Nuevo orden:
    1. lectura completa del 1 al 23 y los *Year One* 1 a 4 (unas 121.000 palabras), por la sesión principal;
    2. lista de lo que sabe Harry;
    3. fase de ideas (se le propone antes el encargo y el coste);
    4. después, el 25 al 30 retocados **en una sola pasada**: fuera el calco y lo que sobre, sin cambiar hechos, más unas pocas líneas de lectura inocente que preparen las tramas elegidas.
  - **Revisión de esos retoques:** propuesto un Opus nuevo por grupo (25 y 26; 27 a 29; 30), tres en vez de seis.
  - **HECHO (18 de octubre):**
    - la lectura completa del 1 al 23 y los *Year One* 1 a 4, en texto completo, por la sesión principal;
    - la lista de lo que sabe Harry, en `docs/notas/lo-que-sabe-harry.md`, con tabla, recomendación y agujeros.

    Recomendado: **viaje en el tiempo con la cicatriz como puerta**. Llega en el pasillo de *Year One* 3 (invierno de 1992); antes es un niño sin pasado. **DECIDIDO por el autor (18 de octubre): A**, Harry viene de un mundo sin Lyra, el del canon. Las opciones eran:
    - **A,** un mundo sin Lyra (recomendada);
    - **B,** su propia vida, repetida.
  - **Fase de ideas, aprobada por el autor en su versión mínima (18 de octubre) y en marcha:**
    1. dos agentes Opus en paralelo, uno de divergencias candidatas (`docs/notas/ideas/divergencias-agente.md`) y otro de poda del original (`docs/notas/ideas/poda-agente.md`);
    2. la sesión principal junta los dos informes con sus propias ideas en un dosier (`docs/fable/001-divergencias.md`);
    3. una consulta a Fable como revisor (solo lectura);
    4. documento final para el autor en `docs/notas/ideas-divergencias.md`.

    **HECHA (18 de octubre).** Informes de los dos agentes, ideas de la sesión, dosier y respuesta de Fable (001, «aceptable con cambios») y documento final `docs/notas/ideas-divergencias.md`. **APROBADO por el autor (18 de octubre): las seis recomendaciones.** En marcha: los retoques del 25 al 30 en una sola pasada, con las semillas (25: la lámpara de la casita; 26: la nota de Regulus; 28: la letra vieja; 29: Lucius de niño; 30: la Copa; 24, opcional: la silla que cruje).
    - Orden: el 25 y el 26 juntos, luego del 27 al 29 y por último el 30. En cada grupo: copia de antes en el scratchpad, retoque, revisión de un Opus nuevo, arreglos, manuales y commit.
    - **25 y 26: retocados (936b719)**, con las semillas de la lámpara y de la nota de Regulus. Copias de antes: `scratchpad/25-antes-retoque.md` y `26-antes-retoque.md` (o `git show 12c5270:borradores/…`). **Cerrados:** revisión de un Opus nuevo (`docs/notas/cotejo-oficial/revision-25-26-retoque.md`: los dos, mejor que antes; ni C ni D), arreglos aplicados (todos menos la pulla a Smith, que se queda), manuales del 25 y el 26 y continuidad al día. El anillo se deja de poner a las nueve «desde finales de agosto», ya no «desde septiembre».
    - **27 a 29: retocados (13156be)** con las semillas de la letra vieja (28), «nothing she wanted him to have» y Lucius de niño (29). Copias de antes en el scratchpad (`27-`, `28-`, `29-antes-retoque.md`) o en `git show c8e993b:borradores/…`. **Cerrados:** revisión de un Opus nuevo (`docs/notas/cotejo-oficial/revision-27-29-retoque.md`: los tres, mejor que antes; dos de clase C, arreglados: el mapa, que Lyra ya conoce desde el 27, y una sola visita al barco vista por Ron), todos los arreglos aplicados y los manuales del 27 al 29 y la continuidad al día. **Solo falta el 30** (ver `docs/notas/sesion-nueva-30.md`).
    - **30: retocado (sesión nueva del 18 de octubre, lectura reducida).** Copia de antes: `scratchpad/30-antes-retoque.md` (o `git show 75749af:borradores/cap-30-which-one.md`). Cambios: el desayuno en el otro orden (Goyle y el *Profeta* delante de la cuarta pregunta de Crabbe; la escena termina en «You’re not even pretending any more… Are you?», sin «Pretending what?»; la cuchara de Parkinson sigue); la Saeta sin el «Did you lend him yours?» de Goyle; **semilla de la Copa** en la tienda: Bagman grita «one step nearer the Triwizard Cup!» y Potter vuelve la cabeza «as people do when somebody across a crowded room says a name they know»; Lyra lo achaca a ser campeón. **La túnica de gala de Narcissa no entra** (no aprobada expresamente; el final queda intacto; su sitio, el 31 o el 32, cuando lleguen las túnicas). **Cerrado:** revisión de un Opus nuevo (`docs/notas/cotejo-oficial/revision-30-retoque.md`: mejor que antes; ni C ni D), todos los arreglos aplicados (la bisagra «Crabbe had watched all of this…», menos «moment», la voz de Bagman, «rolled over», «one shoe on»), manual del 30 y continuidad al día. **El tramo del 24 al 30 está terminado.**
    - (Lo que había antes:) **del 27 al 29**, juntos. Antes: leer los coreanos 30 (resto), 31 y 32, el texto del 27 al 29 y su tabla de ataduras (`plan-24-30.md` §1). Semillas: la letra vieja de la carta lacrada (28) y Lucius de niño en la carta de Draco (29). Opcional en el 27: Moody hablando desde dentro del Imperius (con la decisión de que Moody es Moody, que diga algo que solo sabe quien lo ha sufrido de verdad, compatible con un auror auténtico).
  1. **HECHO (18 de octubre): el 24 rehecho** (`borradores/cap-24-replay.md`, ~3.930 palabras; commits 79aee8e y fc9bf88). Revisado por un Opus nuevo (calco 9 → 7; ningún D; todas las ataduras en pie) y con sus arreglos aplicados. Manual `docs/capitulos/cap-24.md` al día. La versión publicada: `git show 798a357:borradores/cap-24-replay.md`.
     - **Para Webnovel:** cambia el modo, no los hechos. Abre Draco con el póster; Draco sospecha que sus omniculares son los de tienda, no la cree y se lleva también el póster; el verano del anillo va después; **Lyra abre ella los ojos** en el casi beso (se acuerda de la capa de su padre) y la voz de Narcissa llega después. El autor decide si sube esta versión.
     - **Ramas (resuelto):** `main` avanzado hasta la rama de trabajo; el autor borró `claude/hopeful-hamilton-jt6e15`. Se trabaja en `claude/wizardly-albattani-vazqyr` y se sube también a `main`.
  2. **Del 25 al 30 (sin publicar):** recomendado al autor **solo retocar** (quitar calco y lo que sobre, con las palancas de `plan-24-30.md`), sin trama divergente grande; la gran divergencia, desde el 31. El autor lo planteó como pregunta. **Contestado el 18 de octubre: retoques sí, pero después de la fase de ideas y en una sola pasada** (ver arriba).
  3. **Rumbo (lo que el autor dijo el 18 de octubre):**
     - **No entendió R1, R2 y R3** ni los hilos H1, H2 y H3 del documento de rumbo; ya se le explicaron en el chat.
     - **Lo que quiere:** **dos o tres divergencias muy fuertes** que lleven la historia por un rumbo muy distinto del original y generen sus propias subtramas, personajes y choques (fusionar, cambiar, reestructurar o eliminar partes del original). Eso dará la identidad propia.
     - **El final:** queda para más adelante.
     - **Método:** lista de ideas hecha con subagentes, **la sesión principal y Fable** (el autor lo pide expresamente, aunque en `CLAUDE.md` las revisiones son de Opus): las mejores divergencias, lo que conviene quitar del original y lo poco interesante. De ahí sale también si el señor de la casita del este (hilo solo nuestro; no existe en el original) es grande o pequeño.
     - **Su miedo:** perder la calidad que daba el molde del coreano, del que se fusionaban capítulos. Se le propuso un **guion detallado por tanda**: el original como molde, más qué se queda, qué cambia y qué se sustituye, escena por escena. Se aprueba antes de escribir.
  4. **Lo que sabe Harry (hilo clave del motor).**
     - **El autor creía que el original lo explicaba con viajes en el tiempo; no es así.** Grep en los coreanos 14 a 35 y en la oficial del 2 al 111: no hay regresión ni viaje en el tiempo. El giratiempo del 21 y el 22 es el de Hermione, el del canon. El original solo da la cicatriz o el Horrocrux (oficial 90) y nunca lo explica del todo.
     - **El autor prefiere el viaje en el tiempo** («todos imaginan que es eso») y pregunta si la cicatriz sola explicaría todo sin agujero.
     - **Respuesta dada:** la cicatriz no explica lo que aún no había pasado (Flint, los dementores del partido, el disturbio del Mundial). El handoff ya lo trata como un viaje en el tiempo implícito: «lo que sabe Harry es del mundo de Draco; Lyra es la divergencia».
     - **Pendiente:**
       - leer enteros los *Year One* 1 a 4 (en el 1, Harry es un niño ingenuo en Madam Malkin's y eso limita cuándo pudo «volver»);
       - hacer la **lista de todo lo que Harry ha sabido**, capítulo a capítulo, con lo que lo explicaría (cicatriz, Dumbledore, viaje en el tiempo, deducción) y si hay agujero;
       - llevarla al autor.
  5. **Lecturas.**
     - **Hechas en esta sesión:**
       - el protocolo completo: el estado, la nota de sesión, el handoff entero, todos los manuales (1 a 30 y *Year One* 1 a 4) y la continuidad transversal;
       - los coreanos 27 a 29;
       - del 22 al 30 en texto completo;
       - `plan-24-30.md`, `arco-29-32-lectura.md` y `resumen-coreano-26-35.md`;
       - la oficial del 36 al 54, entera;
       - las visiones de conjunto de los cuatro `borradores/resumen-oficial-*.md`.
     - **Pendiente antes de la fase de ideas:** la historia entera en texto completo (del 1 al 21, revisados y publicados, y los *Year One*). El autor lo pregunta y lo da por necesario.
  6. **La oficial completa del 36 al 111** (unas 245.000 palabras; extracción del autor, comprobada) está en `referencia/oficial-en/ko-36.md` … `ko-111.md`. Los resúmenes completos están en `borradores/resumen-oficial-36-54.md`, `-55-73.md`, `-74-92.md` y `-93-111.md`. La primera extracción venía incompleta y ya está sustituida. Herramienta: `herramientas/partir_oficial.py`.
  7. **Ramas:** resuelto (ver el punto 1).
  8. **Agentes vivos:** ninguno.
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
- **Sesión del *Year One* 4 (19 de octubre), en contexto limpio, la historia entera por decisión del autor.** Leído entero por la sesión principal, sin agentes y sin manuales: `CLAUDE.md`, este estado, `sesion-nueva-31.md`, el handoff v3.0, `lo-que-sabe-harry.md`, la ficha, el manual y la crítica antiguos del *Year One* 4, el coreano 26; **la historia entera en texto completo**: `manuscrito/cap-01` a `cap-15`, `borradores/cap-16` a `cap-30` y los *Year One* 1 a 4; la continuidad transversal; la ficha del *Year One* 2; del guion de la tanda, el §0 y el capítulo 40. Con grep, en toda la historia: boggart, el llanto, la cara fría, la muñeca, Leg-Locker, *Flipendo*, Cruciatus, los invernaderos.
- **Sesión nueva del guion (18 de octubre, la que sigue a `sesion-nueva-guion-31.md`), en contexto limpio, protocolo completo** (unos 370.000 tokens; el autor lo aprobó sabiendo el coste). Leído entero y en orden por la sesión principal, sin agentes:
  - `CLAUDE.md`, este estado y `docs/notas/sesion-nueva-guion-31.md`;
  - el handoff entero (`docs/handoff-v2.0.md`, §1 a §17);
  - todos los manuales de `docs/capitulos/` (1 a 30 y *Year One* 1 a 4) y `continuidad-transversal.md`;
  - **la historia entera en texto completo:** `manuscrito/cap-01` a `cap-15`, `borradores/cap-16` a `cap-23`, `borradores/extra-year-one-1` a `4` y `borradores/cap-24` a `cap-30`;
  - los coreanos 34 y 35;
  - `borradores/resumen-oficial-36-54.md`, del 36 al 51 (y por encima del 52 al 54);
  - el rumbo: `ideas-divergencias.md`, `ideas/poda-agente.md`, `docs/fable/001-divergencias.md` y `lo-que-sabe-harry.md`;
  - `borradores/guion-tanda-31-40.md`.

  Con grep, en toda la historia: Winky, Jorkins, Percy, el baúl, la petaca, Crouch, la multijugos, el mapa, «Write on Sundays», la bufanda, la ventana de Snape, la capa al final del 30 y las comillas descuadradas.
- **Misma sesión, para el guion de la tanda (18 de octubre):** el autor autoriza a no releer la historia entera (basta la del 18 de octubre). Leído entero por la sesión principal: el handoff (§1 a §17), todos los manuales de `docs/capitulos/` (1 a 30 y *Year One* 1 a 4) y la continuidad transversal; los coreanos 34 y 35; `borradores/resumen-oficial-36-54.md` (del 36 al 51); `docs/notas/ideas-divergencias.md`, `ideas/poda-agente.md`, `ideas/divergencias-agente.md`, `ideas/ideas-sesion.md`, `docs/fable/001-divergencias.md` y `lo-que-sabe-harry.md`. Con grep, el 24 (la silla que cruje no está puesta), el 25 al 29 (el baúl, la petaca, Dobby) y `plan-coreano-26-35.md`.
- **Sesión nueva del 30 (18 de octubre), lectura reducida autorizada por el autor** (`docs/notas/sesion-nueva-30.md` §2), leído entero por la sesión principal: `CLAUDE.md`, este estado, `sesion-nueva-30.md`; del handoff, §2, §4, §16 y §17; los manuales del 29 y del 30 y la continuidad transversal; de `plan-24-30.md`, §1 (tabla de calco, ataduras y lo que necesita el 31) y el apartado del cap. 30 en §2; el texto completo del 29 y del 30; el coreano 33. Con grep, `ideas-divergencias.md` (la semilla de la Copa y la túnica). **No leído:** el resto del handoff y de los manuales. Para el 31 vuelve el protocolo completo.
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
- **Sesión nueva del 18 de octubre (la que sigue a `sesion-nueva-18-oct.md`), en contexto limpio.** Leído entero por la sesión principal lo que pide su §4:
  - `CLAUDE.md`, este estado y `docs/notas/sesion-nueva-18-oct.md`;
  - el handoff entero (`docs/handoff-v2.0.md`, §1 a §15);
  - todos los manuales de `docs/capitulos/` (1 a 30 y *Year One* 1 a 4) y `continuidad-transversal.md`;
  - `docs/notas/rumbo-25-en-adelante.md` (con la respuesta del autor, §6), `docs/notas/cotejo-oficial/plan-24-30.md` entero y `docs/notas/arco-29-32-lectura.md`;
  - el texto completo del 24 rehecho, el 25 y el 26.

  **Después, en la misma sesión:** la historia entera del 1 al 23 y los *Year One* 1 a 4, en texto completo y en orden (unas 121.000 palabras). **Sin leer todavía:** los coreanos 28 a 33 y el 27 al 30 en texto completo (se leen antes de retocarlos). Hecha al autor la pregunta del 25 al 30; se espera respuesta antes de tocar ningún capítulo.

## Texto que solo existe en contexto

Ninguno. Todo está commiteado y subido.

## Agentes vivos

- **Crítico:** el del cuarto año (criticó del 24 al 28) está retirado. El del 29 (Opus, arrancado con `docs/notas/critico-arranque-29.md`) criticó el 29 y el 30, pero era de una sesión anterior y ya no se le puede reutilizar. **Para el 31 hace falta uno nuevo**, que lea enteros todos los capítulos adaptados, con un resumen de las notas anteriores (`CLAUDE.md`). Antes de lanzarlo, avisar al autor del coste. El anterior (17 a 23, *Year One*, revisión del 1 al 3) está retirado.
- **Fase de ideas:** terminada.
- Ningún agente vivo.
- **Revisor:** es el chat paralelo del autor. Sus informes llegan a `docs/notas/revisiones/`.

## Decisiones pendientes del autor

- En qué capítulo obtiene Lyra alguna pieza de lo que sabe Harry (en el 29 no: la copa de Hufflepuff no se nombra).
- La publicación la lleva el autor (consejos: titular los extras «Year One, Part N»; en Webnovel la numeración automática se adelanta cuatro respecto a la interna).
