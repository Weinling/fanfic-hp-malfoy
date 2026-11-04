# Prompt de inicio: la tanda 41-50 (el verano de 1995 y el quinto, hasta Navidad)

*28 de octubre de 2026. Para pegar al abrir la sesión que hace la tanda nueva.*

---

Eres la sesión principal del proyecto «Never Owe a Malfoy, Potter» (/Users/eden/Documents/fanfic-hp-malfoy): la adaptación al inglés británico de una fanfic coreana de Harry Potter con Lyra Malfoy, genderbend de Draco. Háblale al autor, Edén, en español. **Esta sesión hace la tanda 41-50:** primero el guion de la tanda, y después los capítulos.

## 0. Antes de nada

- Rama `claude/wizardly-albattani-vazqyr` (`git pull -q origin claude/wizardly-albattani-vazqyr`).
- Cerrojo: `date > .autonomo.lock` (si existe y tiene menos de 5 horas, para y avísame). Bórralo al terminar.
- Lee `docs/notas/autonomo/ARRANQUE.md` entero: su flujo por capítulo (§3), el mensaje a los subagentes (§4), el crítico (§5) y cómo terminar (§7) mandan en esta sesión.

## 1. Las decisiones del autor que faltaban

Son las del §4 de `docs/notas/revisiones/revision-tanda-31-40.md`; la 1, los calcos, ya está hecha y aprobada. **Respuestas del autor:**

> Acepto las recomendaciones del informe en las decisiones 2 a 9, salvo lo que diga aquí: ______

Las recomendaciones, por si las cambia:
- **2.** El 41 abre desde Lyra en la Mansión, cobrando la Marca del andén. El borrador desde Harry (`borradores/cap-41-arranque-harry-borrador.md`) pasa al 42 o al 43.
- **3.** La tanda acaba en la Navidad del quinto, cuando Lyra descubre quién es el señor de la casita.
- **4.** Pettigrew está en Azkaban sin registro, y la fuga del quinto lo suelta. Tiene que hacer algo antes del Ministerio; si no se le encuentra función, que siga con Dumbledore.
- **5.** Moody se lleva el mapa, así que Harry pasa el verano y el otoño sin él.
- **6.** Los Horrocruxes son los del canon, pero movidos desde 1995 por la red de los Malfoy: Harry va adonde recuerda y no los encuentra; la pista está en casa de Lyra.
- **7.** El «never felt better» de Abraxas es una cura: Voldemort le curó la viruela de dragón, y eso lo tiene atado.
- **8.** Draco entra en Slytherin.
- **9.** Los *Year Two* se rehacen sobre lo nuestro, en la tanda 51-60.

**Lo primero es apuntar estas decisiones:** en el handoff (§7, §8 y §10), en `docs/notas/sesion-nueva-tanda-41.md` y en la continuidad, si tocan algo. Commit.

## 2. Lectura de tanda nueva (ARRANQUE §2)

La historia ya ronda las 200.000 palabras (el umbral de `CLAUDE.md`).

1. **Lo de siempre:** `CLAUDE.md`, la sección «Ahora mismo» del estado, `docs/handoff-v3.0.md` entero y `docs/capitulos/continuidad-transversal.md`.
2. **Texto completo:**
   - del 24 al 40 y `borradores/interludio-1-the-seventh-lock.md`, que va entre el 32 y el 33 (el 33 se llama ahora *The Corner Table*);
   - del 1 al 23 y los cuatro *Year One*: enteros si caben, y si no, sus manuales (`docs/capitulos/`).

   Apunta qué leíste.
3. **Lo planeado y decidido:**
   - `docs/notas/sesion-nueva-tanda-41.md`;
   - `docs/notas/revisiones/revision-tanda-31-40.md`, sobre todo el §2.7, «lo que falta» (Draco en Hogwarts; Sirius y su muerte sabida; dónde está Voldemort; cómo tuvo cuerpo sin cementerio; Pettigrew; la culpa de Crouch y el silencio del norte; qué del quinto del canon sigue pasando, con Cedric vivo y enemigo; Snape; la Oclumancia de Lyra; el pago a mitad de tanda), además del §3 y el §4;
   - `docs/fable/002-mundo-harry-y-tanda-41.md` y `docs/fable/003-revision-tanda-31-40-y-plan-41.md`;
   - `docs/notas/lo-que-sabe-harry.md`, `docs/notas/ideas-divergencias.md`, `docs/notas/ideas/poda-agente.md` y `docs/fable/001-divergencias.md`;
   - el borrador del 41 desde Harry;
   - `borradores/guion-tanda-31-40.md`, como formato.
4. **El original del tramo:**
   - `borradores/resumen-oficial-36-54.md` (del 52 al 54);
   - `borradores/resumen-oficial-55-73.md`, entero;
   - las cabeceras y tablas de `-74-92.md` y `-93-111.md`.

   Los capítulos originales enteros se leen al hacer la ficha de cada capítulo (regla de los capítulos de referencia).

## 3. El guion de la tanda

- **Escribe** `borradores/guion-tanda-41-50.md` con el formato del de la tanda 31-40:
  - la tanda en una página;
  - el calendario;
  - capítulo a capítulo, con etiquetas y la tabla de referencias del original;
  - lo que cae;
  - los avisos para escribir;
  - los hilos.
- **Tiene que recoger:**
  - las decisiones de Fable 002 (el tablero de Harry, que lo formula Lyra en el quinto; los fragmentos del bosque; un capítulo desde Harry por tanda, como *Interlude*; Hermione antes que Ron);
  - los cuatro huecos de Fable 002 (la cuenta de Horrocruxes y el anillo de Gaunt; el anillo de Lyra devuelto; la mentira del 37; Narcissa en el andén);
  - lo que falta según la revisión;
  - los *Year One* 5 y 6 (originales 52 y 53) en la primera pausa del verano sin gancho;
  - como mucho dos o tres capítulos propios, sin capítulo de referencia;
  - un pago a mitad de tanda;
  - y el recuento: del quinto salen unos 15 o 16 capítulos, y la historia entera, unos 34 a 36 más los extras.
- **Consulta a `fable-revisor`** con dosier `docs/fable/004-guion-tanda-41-50.md` (skill `metodo-equipo`) y aplica lo que aceptes, con motivo.
- **Si estoy en el chat,** enséñame el guion en una página con las decisiones grandes antes de escribir el 41. Si no estoy (sesión nocturna), sigue en modo autónomo, como dice el arranque, y apúntalo con ⚠ en `docs/notas/autonomo/PARA-EL-AUTOR.md`.

## 4. Los capítulos

- **El flujo** es el del ARRANQUE §3: ficha leyendo enteros sus capítulos de referencia del original; escritura escena a escena con commit y push; pasada de tics (la lista viva del crítico, al final de `docs/notas/cap-40-critica.md`); crítica; arreglos; manual; continuidad; estado; y PARA-EL-AUTOR.
- **El crítico es nuevo** (ARRANQUE §5): lee completo desde el 31, con el interludio, más las notas de crítica. Se reutiliza para toda la tanda.
- **Los capítulos desde Harry** se publican como *Interlude: …*, sin número, y no rompen la numeración.
- **Para hacia las 00:45,** o antes si notas el contexto cargado. Deja el estado con el siguiente paso exacto y borra el cerrojo.
