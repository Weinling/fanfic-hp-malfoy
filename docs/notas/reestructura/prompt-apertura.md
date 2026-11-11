# Prompt de apertura

*10 de noviembre de 2026, retocado el 11. Se pega al empezar una sesión nueva que tenga que conocer el rumbo (guiones, decisiones). Para seguir escribiendo capítulos basta con lo que pide `CLAUDE.md`. Sustituye al del 5 de noviembre (en `docs/archivo/sesiones/`).*

```
Sigues el trabajo de «Never Own a Malfoy, Potter». Trabajas en español con el autor, Edén; los capítulos van en inglés británico. Esta sesión no tiene una tarea cerrada de antemano: tienes que conocer la historia y su rumbo lo bastante para escribir guiones y también para discutir ideas, decisiones, tramas, personajes y cambios en los capítulos sin publicar.

PONTE AL DÍA

0. Comprueba que estás en main, haz git pull y pon el cerrojo. Lee CLAUDE.md y sigue sus reglas. La memoria del proyecto carga sola.

1. El núcleo, entero y en este orden:
   - docs/estado-de-trabajo.md
   - docs/handoff-v4.0.md
   - docs/notas/reestructura/decisiones.md (todo; §5 a §12 son el rumbo vigente)
   - docs/notas/reestructura/guion-general.md
   - docs/notas/lo-que-sabe-harry.md
   - docs/notas/reestructura/numeracion.md
   - docs/capitulos/arcos.md, entero: la historia por arcos.
   - docs/capitulos/continuidad-transversal.md, entera: es el mapa de cada capítulo, de quién sabe qué y de las fichas. Si choca con el texto, manda el texto.
   - docs/critico-v2.0.md, secciones 2 a 5 (rúbrica y tics)

2. Las lecturas externas, por sus conclusiones:
   - docs/notas/criticas-codex/lectura-73-84.md, §7 (lo que la última tanda le exige al tramo 4; resumido en decisiones §11)
   - docs/notas/criticas-codex/cuaderno-lector.md
   - docs/notas/criticas-codex/cuaderno-aplicacion-romance.md y critica-independiente-romance-10-nov.md (qué se cambió en el romance y por qué)
   - docs/archivo/guiones/guion-tanda-73-84.md: solo el Voto y las notas «Para el tramo 4» (búscalas con grep)

3. docs/capitulos/arcos.md, entero, y los capítulos de su «Lectura obligatoria», tabla 1 (unas 41.000 palabras), completos.
   Los archivos llevan número de trabajo: cap-72-mine.md es el 78 del lector. Del resto, el manual (docs/capitulos/cap-NN.md) y grep cuando haga falta. Antes de opinar sobre un capítulo concreto o de tocarlo, léelo entero, y di con honestidad lo que no has leído. Para preguntas puntuales sobre capítulos que no has leído puedes usar un subagente lector.

No leas la historia entera. No abras coreano/, referencia/ ni fuentes/. No leas el original.

LO QUE DEBES TENER CLARO
- Publicado hasta el 42: del 1 al 42 no se toca; una errata se apunta en erratas-publicado.md. Del 43 en adelante se puede cambiar a fondo, sin contradecir lo publicado.
- Los informes de Codex son criterio, no órdenes. Mandan las decisiones del autor.
- Harry es gris: actúa, desea y se equivoca; nada de nobleza que no se haya ganado. Lyra es una cría y se rompe delante de los demás. La amistad va en la línea principal, y los amigos tienen vida propia.
- La posesividad se narra ambigua: ni se explica, ni se justifica, ni se aclara si es inocente. Menos besos, y los que queden, con tierra física. Nada de segundas explicaciones.
- Si dejas algo fuera por un límite tuyo, dilo al entregar cada escena, con una línea final: «Fuera por mi límite:» y lo que quedó fuera, o «Nada». No lo disfraces de problema de voz ni lo presentes como regla del autor.
- La crítica va por tandas y a ciegas, en segundo plano mientras se escribe lo siguiente: Fable para una tanda o un capítulo muy especial, Opus para lo demás (`CLAUDE.md`).
- Comprueba la rama antes de cada commit: Codex trabaja en su propia carpeta y alguna vez ha cambiado la de aquí.

PENDIENTE
- Decidir si se retiran cinco besos en reserva: trabajo 60, 61, primer beso del 62, 64 y el de la escalera del 65.
- La tanda 87-98 está escrita hasta donde diga el estado; su guion, en borradores/guion-tanda-87-98.md. El guion de la tanda siguiente se escribe con Fable.
- Sigue en pie la decisión §7 (el otro Harry perdió), con lo que añade el §10.

AL TERMINAR DE LEER, UN MENSAJE CORTO
a) En diez líneas: dónde está la historia y adónde va.
b) De tres a cinco agujeros, tensiones o riesgos que hayas visto, con archivo:línea.
c) Lo que no has leído.
Después espera. Pregunta solo lo que sea de verdad del autor. Sé breve y di lo que piensas.
```
