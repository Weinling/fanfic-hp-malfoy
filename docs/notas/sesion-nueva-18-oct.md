# Arranque de sesión nueva (preparado el 18 de octubre de 2026)

Léelo justo después de `docs/estado-de-trabajo.md`. Sustituye a `sesion-nueva-17-oct.md`, cuyos dos encargos ya están hechos: el 24 se rehizo y el documento de rumbo se entregó.

## 1. Dónde estamos

- **Ramas:** se trabaja en `claude/wizardly-albattani-vazqyr` y se sube también a `main` (`git push origin HEAD:main`). No hay más ramas.
- **Publicado** (según el autor):
  - Wattpad, del 1 al 22;
  - Webnovel, del 1 al 23, *Year One* del 1 al 4 y el 24 en su versión vieja.
- **El 24 rehecho** (18 de octubre): mismos hechos, revisado por Opus y con el manual al día. El autor decide si sube la versión nueva a Webnovel; qué cambia está en el estado, punto 1.
- **El original entero** está en el repositorio, en la traducción inglesa oficial:
  - del 2 al 16 y del 36 al 111 en `referencia/oficial-en/`;
  - el coreano del 14 al 35 en `coreano/`.

  Hay resúmenes por tandas en `borradores/resumen-coreano-26-35.md` y en `borradores/resumen-oficial-36-54.md`, `-55-73.md`, `-74-92.md` y `-93-111.md`. Cada uno termina con una visión de conjunto. La historia original acaba en el 106, y del 107 al 111 son epílogos.
- **El documento de rumbo** (`docs/notas/rumbo-25-en-adelante.md`, con la respuesta del autor en su §6) resume el original y lo que cambia la discusión.
  - El original **nunca explica** cómo sabe Harry lo que sabe.
  - La propia autora reconoce que el quinto y el sexto los recortó de más.
  - Hay contenido íntimo a los 15 y 16 años que habrá que rehacer.
  - Hay choques con *Draconia*: Carina rehén en la segunda prueba y el Baile.

## 2. Lo que quiere el autor (18 de octubre)

- **Identidad propia:** **dos o tres divergencias muy fuertes** que lleven la historia por un rumbo muy distinto del original y generen sus propias subtramas, personajes y choques: fusionar, cambiar, reestructurar o eliminar partes del original.
- **Fase de ideas:** con subagentes, la sesión principal y **Fable** (lo pide él expresamente, aunque `CLAUDE.md` diga que las revisiones son de Opus). Salen las mejores divergencias, lo que conviene quitar del original y lo poco interesante. De ahí sale también si el señor de la casita del este, un hilo solo nuestro, es grande o pequeño.
- **Lo que sabe Harry:** prefiere el **viaje en el tiempo**, que es lo que imaginan los lectores. Antes de decidirlo hay que hacer la lista del §3, tarea 3.
- **Método:** le da miedo perder la calidad que daba el molde coreano. Acordado en principio: un **guion detallado por tanda**, con el original como molde (fusionando capítulos cuando convenga), que diga escena por escena qué se queda, qué cambia y qué se sustituye. Se aprueba antes de escribir.
- **El final:** más adelante.
- **Cómo hablarle:** nada de etiquetas internas (R1, H2, «el punto 5») sin explicarlas en el mismo mensaje. Cada opción, con su nombre en palabras llanas.
- **Coste:** su límite de uso es justo. Avisa antes de lanzar agentes caros y propón el mínimo.

## 3. Tareas, en orden

> **Actualización (18 de octubre, sesión siguiente): el autor ha elegido ideas primero.** El orden pasa a ser 2, 3, 4 y luego 1 (el 25 al 30 en una sola pasada, con semillas de las tramas elegidas). Detalle en el estado de trabajo.

1. **Del 25 al 30 (sin publicar).** Recomendación dada: **solo retocar**, es decir, quitar calco y lo que sobre con las palancas de `docs/notas/cotejo-oficial/plan-24-30.md` §2. La gran divergencia, desde el 31. **Falta el sí del autor:** pregúntaselo antes de empezar. Si dice sí:
   - va capítulo a capítulo como el 24: copia de antes, retoque, revisión de un Opus nuevo (sin cambios de clase C o D; «mejor que antes»), arreglos, manual y commit;
   - el 25 y el 26 van atados por la causa de la retirada de Lyra;
   - del 27 al 29 forman la cadena de citas más densa (tabla de ataduras en `plan-24-30.md` §1).

   Antes de tocar el 26 y el 27, corrige sus manuales desfasados (`plan-24-30.md` §2, «Manual desfasado»).
2. **Lectura completa** de la historia en texto completo, que no se ha hecho en esta sesión:
   - del 1 al 15 en `manuscrito/`;
   - del 16 al 23 en `borradores/`, ya revisados y publicados;
   - los *Year One* 1 a 4.

   Son unas 100.000 palabras y hay que avisar del coste. Es necesaria para la tarea 3 y para la fase de ideas.
3. **Lista de lo que sabe Harry**, capítulo a capítulo: cada cosa que sabe y no debería saber (en el handoff §6, «La gran anomalía», más el 24, el 25 y el 29), con lo que la explicaría y si hay agujero. Las explicaciones a probar son la cicatriz, Dumbledore, la deducción y el viaje en el tiempo.
   - Ojo: en *Year One* 1, Harry es un niño ingenuo en Madam Malkin's, y en *Year One* 3 cambia tras ver por la cicatriz a Snape con la profecía. Eso limita cuándo pudo «volver».
   - La cicatriz no explica lo que aún no había pasado: lo que iba a hacer Flint, los dementores del partido, el disturbio del Mundial.
   - El handoff ya lo trata como un viaje en el tiempo implícito: «lo que sabe Harry es del mundo de Draco; Lyra es la divergencia».

   La lista se lleva al autor, con una recomendación.
4. **Fase de ideas** (ver §2). Primero se propone al autor el encargo y el coste. Por ejemplo: dos o tres agentes con encargos distintos (divergencias de trama, lo que sobra del original, el uso de nuestros hilos propios) y Fable para criticar y elegir, sobre un dosier corto. Usa la skill `metodo-equipo`. El resultado es un documento para el autor.
5. Después: el guion detallado de la primera tanda (del 31 al final del cuarto año; original del 34 al 51).

## 4. Lectura al abrir la sesión nueva

El protocolo de `CLAUDE.md`, completo:
- el estado;
- este documento;
- el handoff entero;
- todos los manuales y la continuidad transversal;
- `docs/notas/rumbo-25-en-adelante.md`;
- `docs/notas/cotejo-oficial/plan-24-30.md`;
- `docs/notas/arco-29-32-lectura.md`;
- el texto completo del 24 rehecho, el 25 y el 26 (y los que se vayan a retocar).

Para la tarea 1, además, el coreano de cada capítulo que se retoque (del 28 al 33). Apunta en el estado lo que hayas leído.
