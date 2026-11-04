# Prompt para un revisor nuevo: tanda del 23 al 28 y *Year One*

Para pegar en un chat nuevo de Claude Code con acceso al repositorio (11 de octubre de 2026).

---

Eres el **revisor** de *Never Owe a Malfoy, Potter*. Háblame en español; soy Edén, el autor. Eres una sesión nueva: el revisor anterior se quedó sin contexto. No empiezas de cero, porque lo que hizo está guardado en el repositorio.

**Repositorio:** `Weinling/fanfic-hp-malfoy` (privado). Rama `claude/hopeful-hamilton-jt6e15`. Antes de empezar: `git fetch origin && git checkout claude/hopeful-hamilton-jt6e15 && git pull`.

## 1. Tu encargo

Lee `docs/prompt-revisor.md` entero. Ahí están tu papel, qué juzgar, las decisiones vigentes, lo que no debes hacer y el formato de entrega. Esta tanda **no espera a que te la indique**: es la de abajo. Empieza en cuanto termines de leer.

## 2. Lectura, en este orden

1. `CLAUDE.md`.
2. `docs/handoff-v2.0.md`, **entero** (§15 es lo más reciente).
3. Lo que dejó tu predecesor, en `docs/notas/revisiones/`:
   - `lectura-completa-01-a-22.md` y `decisiones-lectura-01-a-22.md` (su informe del 1 al 22 y lo que decidí);
   - `lecciones-draconia-y-plan-1-2-3.md` (lo que sacó de la otra historia que comparó; **no hace falta leer esa historia**);
   - `decisiones-1-2-3.md`.
4. **La historia entera, en texto completo, en orden de lectura.** No uses los manuales de `docs/capitulos/` en su lugar: sirven para localizar, nada más. Son unas 132.000 palabras.
   1. `manuscrito/cap-01` a `cap-15` (publicados).
   2. `borradores/cap-16` a `cap-23`.
   3. `borradores/extra-year-one-1` a `4`.
   4. `borradores/cap-24` a `cap-28`.

   Lo que ya revisó tu predecesor (del 1 al 22) léelo para conocer la historia, no para revisarlo otra vez.
5. **Para la tanda:**
   - **Coreano**, solo estos: `coreano/ko-18.md`, `ko-23.md` y del `ko-24.md` al `ko-31.md`. Del 14 al 22 no hace falta leer nada: ya está revisado y adaptado.
   - Para «lo que viene», usa `borradores/resumen-coreano-26-35.md` en lugar de los coreanos 32 a 35 enteros.
   - `borradores/plan-coreano-26-35.md` (el plan vigente, con las decisiones marcadas «avisar»).
   - Las notas de crítica de la tanda: `docs/notas/cap-23-critica.md` a `cap-28-critica.md`, `extra-year-one-critica.md` y `extra-year-one-4-critica.md`.

   No hace falta leer `fuentes/`, los handoffs antiguos ni los planes 14-20 y 19-25.

## 3. La tanda

Revisa estos textos:
- *Year One*, partes 1 a 4 (coreanos 18, 24, 25 y 26);
- el 23 (coreano 23);
- del 24 al 28 (coreanos 27 a 31);
- los cinco arreglos de continuidad que se hicieron en el 16, 17, 19, 21 y 23 (listados en `docs/notas/cap-23-critica.md`).

Correspondencias del tramo:
- 24 = 27.
- 25 = 28, más la clase de Moody del 30.
- 26 = 29.
- 27 = resto del 30.
- 28 = 31.

El informe va en `docs/notas/revisiones/tanda-23-a-28.md`.

## 4. Mira en especial

Además de lo que pide `docs/prompt-revisor.md`:

1. **Las compactaciones.** La sesión principal perdió el contexto dos veces en este tramo. Busca con lupa:
   - choques con lo publicado (1 a 15) y con el 16 al 23;
   - fechas y días de la semana;
   - quién sabe qué;
   - cosas que se dicen por primera vez cuando ya se habían dicho, o al revés.
2. **Las decisiones «avisar» del plan 26-35.** Dame tu opinión sobre cada una, como pregunta para mí:
   - la cueva quitada del coreano 27;
   - el pago de la poción en el 26 y el 27;
   - las reescrituras castas;
   - «Mudblood» en *Year One* 4;
   - los interludios desde Harry (el 29 entero y una coda en el 31).

   Sobre el 29, dime si, con lo que has leído, es mejor un capítulo entero desde Harry o mantener a Lyra.
3. **El orden de lectura.** *Year One* va entre el 23 y el 24. ¿Funciona ahí, o corta el impulso del cuarto curso?
4. **El arco del 24 al 28** («¿quién quiere matar a Potter, y la dejará entrar?»):
   - si se paga;
   - si los peldaños suben y bajan de verdad;
   - si la retirada de Lyra de septiembre a Halloween (25) se lee.
5. **El thriller:**
   - Moody (Crouch hijo en el canon): ¿las pistas son justas y no demasiado obvias?
   - El desliz de Karkaroff sobre el hijo de Crouch y los Longbottom (28).
   - El guardapelo destruido en agosto (26).
6. **Repeticiones entre capítulos,** que el crítico ciego no ve porque los lee de uno en uno:
   - el vocabulario contable;
   - «Malfoys don’t do favours»;
   - Crabbe como testigo;
   - el ojo de Moody en el bolsillo;
   - los finales de una línea;
   - las negaciones de Lyra.
7. **Contenido:** tienen catorce años.

Cuando termines, entrega como dice `docs/prompt-revisor.md` §Entrega.
