# Lectura 39–78 — entrega parcial: dictamen del 39 y lectura del bloque 38–43

## Alcance y conocimiento previo

No conocía versiones anteriores de estos capítulos. Conocía el canon de Harry Potter de forma general; no he cotejado aquí ese recuerdo con fuentes. Las indicaciones del encargo —incluidas las alusiones a cambios y misterios— sí condicionaban mis expectativas. No presento sus datos como descubrimientos míos.

Esta **no es la lectura completa solicitada**. La extensión supera el contexto disponible para leerla y conservarla en esta sesión. He aplicado la cláusula de entrega parcial, dando prioridad al punto 1. Leí completos, primero y en orden, los capítulos 1–5. Después interrumpí ese recorrido y leí completos 38, 39 y 40; los extras de primer año 4, 3 y 2, en ese orden; 41, 42, interludio 2 y 43. La salida conjunta de 42 e interludio 2 se truncó: recuperé el intervalo omitido antes de continuar. No he leído completos 6–37, 44–72 ni los demás extras e interludios; después solo he visto algunos fragmentos devueltos por búsquedas técnicas y por el cotejo de ngramas. La muestra de lectura completa consta de quince archivos y 65.234 palabras según el contador descrito abajo, aproximadamente el 19,4 % del corpus; no representa una lectura de corrido de la novela.

No he leído decisiones.md, revision-39-72.md, numeracion.md, guion-general.md ni guion-tanda-73-84.md. Tampoco críticas anteriores, fichas, manuales, coreano/ o fuentes/. No he abierto los textos de referencia/oficial-en/; la única consulta a ese corpus es la ejecución del script autorizado que se documenta más abajo. No he usado subagentes. No he editado capítulos ni documentos ajenos a este informe.

Base de lectura: main actualizado mediante `git pull --ff-only`, commit `924c9e6d5e8731b111f5c85ab6d53d447d834ed0`. Rama de entrega: `codex/lectura-39-78`. Las citas `archivo:línea` corresponden a esta base. Las etiquetas de capítulo siguen los encabezados de los archivos leídos; no infiero la numeración del lector de capítulos que no he abierto.

## 1. Urgente: ¿se puede publicar el 39?

**Sí, con el alcance limitado de esta revisión: no he encontrado un bloqueo de trama entre el 38 y el 39.** No equivale a certificar su continuidad con todos los capítulos publicados. Antes de publicarlo haría una corrección de expresión y cerraría la discrepancia entre la versión descrita en el encargo y la que hay en main.

La frase «Put it on the bill» está en `borradores/cap-39-never-lied.md:369`. La eliminación de exclamaciones del derrumbe, en cambio, **no está incorporada a este archivo**. Hay cuatro signos: uno en la intervención de Harry de la línea 255 y tres en las de Lyra de las líneas 315 y 323. Si esa eliminación era una decisión cerrada, estos son los cambios concretos; quitar puntuación no obliga a borrar el grito que la narración describe en la línea 257.

| Archivo:línea | Texto actual → propuesto | Motivo |
|---|---|---|
| `borradores/cap-39-never-lied.md:51` | “the bandage had come through his trousers in a long brown stain” → “blood had seeped through his bandage and left a long brown stain on his trousers” | Lo que atraviesa la venda y la tela es la sangre. La expresión actual obliga a resolver una metonimia innecesaria. |
| `borradores/cap-39-never-lied.md:255` | “You could have looked at the *floor!*” → “You could have looked at the *floor*.” | Aplicar la decisión de puntuación también a Harry si abarca todo el derrumbe. Si solo se refería a Lyra, esta intervención puede conservarse. |
| `borradores/cap-39-never-lied.md:315` | “Nobody *came!*” → “Nobody *came*.”; “I am going *home!*” → “I am going *home*.” | El quiebre ya lo sostienen la frase interrumpida, las lágrimas y la pérdida de voz. |
| `borradores/cap-39-never-lied.md:323` | “You *did!*” → “You *did*.” | La acotación inmediata ya dice “It came out in pieces”. |

**Contradicciones con el 38: ninguna confirmada en el cotejo de ambos archivos.** He comprobado estos enlaces concretos:

- La lesión es en la pierna izquierda en `borradores/cap-38-the-cup.md:169`; el 39 mantiene esa pierna y el sangrado en `borradores/cap-39-never-lied.md:51`. La hospitalización del lunes por la noche de `borradores/cap-40-hidden-ink.md:53` cabe después de la escena de la lechucería.
- La acusación de Cedric en `borradores/cap-38-the-cup.md:143` no desaparece: `borradores/cap-39-never-lied.md:5` dice que pide que no arrojen objetos a Harry, no que lo haya perdonado ni que retire la acusación.
- Lyra reconoce el control sobre Crouch y decide callar en `borradores/cap-38-the-cup.md:203` y `borradores/cap-38-the-cup.md:211`. El silencio del domingo en `borradores/cap-39-never-lied.md:5` y la nota posterior en `borradores/cap-40-hidden-ink.md:37` desarrollan esa elección.
- La copa que no cumple lo que Harry esperaba, `borradores/cap-38-the-cup.md:125`, se convierte en la deducción de Lyra en `borradores/cap-39-never-lied.md:79`. No necesita una explicación añadida en el 38.
- La mentira que Harry le reprocha en `borradores/cap-38-the-cup.md:31` sigue siendo una mentira que ella admite y no desvela en `borradores/cap-39-never-lied.md:219`.

No convertiría el 39 en una reconciliación ni haría más noble a Harry para facilitar su publicación. La admisión sobre Ginny y el uso deliberado de la Navidad son parte de su fuerza. La reserva sobre la explicación excesiva del cierre figura en las propuestas opcionales del punto 10; no es una contradicción con el capítulo publicado.

## 2. Como lector: impresión fijada sin consultar la planificación

El comienzo me engancha por una razón concreta: el chantaje de Harry no consigue borrar ni el clasismo ni el amor familiar de Lyra. Su decisión de ocultar información a Lucius tiene una lógica propia. La escena del estudio en el 2 es más convincente que cualquier declaración de que ella es inteligente: obtiene una confesión haciendo creer a su padre que ya sabe la respuesta.

En el bloque 38–43, lo que más me interesa es la distancia entre lo que una persona hace y lo que otra cree que ha hecho. Harry gana y no obtiene lo que esperaba; Lyra vuelve a una familia que la quiere y la utiliza; ambos se atribuyen la muerte de Crouch desde ignorancias distintas. El salto que he dado impide juzgar cuánto de esa fuerza procede de la acumulación de los capítulos intermedios.

El 39 me sostiene sobre todo desde «And you let him» hasta «Who came?». La confesión sobre Ginny impide reducir el conflicto a una familia mala que separa a dos personas inocentes. Cuando Harry usa la Navidad, no me parece un héroe momentáneamente incomprendido: busca hacer daño. Eso funciona. La reacción de Lyra tiene cuerpo de niña desbordada, aunque conserve palabras de la casa en que se ha criado.

El final me convence menos que el centro. No por la persistencia de Harry ni por que Lyra siga queriéndolo: ambas cosas caben. Me pesa que la narración explique sucesivamente qué significa el gesto, cómo viajará a Wiltshire, por qué es una deuda y cuán bien está ejecutado. Cuando ya he entendido la maniobra, sigo recibiendo instrucciones para entenderla. Es una reserva de intensidad y de confianza en el lector, no un fallo demostrado de continuidad.

En el 43 me engancha el cine frustrado y su sustitución por la salida con Sirius. El «Prongs» es un buen golpe concreto. La lista retrospectiva que lo precede, en cambio, se me hace más explicativa: prepara tan explícitamente la herida que deja menos trabajo al incidente. No puedo decir en qué capítulo habría abandonado una novela cuyo tramo central no he leído. En esta muestra no la habría abandonado; sí habría querido menos explicación después de los golpes más claros.

Estas impresiones se recogen antes de consultar cualquier planificación. No constituyen una fase 1 completa ni autorizan conclusiones sobre la costura entre capítulos antiguos y nuevos.

### Cinco mejores momentos de la muestra, no de los 78 capítulos

1. El ajedrez de Navidad: “Your move, Father”, la respuesta que Lyra se da a sí misma y el peón torpe que aparece después. Funciona sin que nadie declare que está acompañándola: `borradores/extra-year-one-2-nobody-asked-you.md:305`, `borradores/extra-year-one-2-nobody-asked-you.md:307`, `borradores/extra-year-one-2-nobody-asked-you.md:339`.
2. “And you let him.” / “Yes.” Harry no encuentra una excepción moral que lo saque del apuro: `borradores/cap-39-never-lied.md:159`, `borradores/cap-39-never-lied.md:161`.
3. “They didn’t come, and they’re mine”. Lyra no necesita idealizar a los suyos para escogerlos. Es el núcleo del capítulo: `borradores/cap-39-never-lied.md:315`.
4. El anillo verde después de la victoria: el objeto asegura que Harry está a salvo cuando la escena demuestra que se ha perdido algo decisivo. Buena inversión del alivio: `borradores/cap-38-the-cup.md:133`, `borradores/cap-38-the-cup.md:151`, `borradores/cap-38-the-cup.md:255`.
5. “Pass the salt, Prongs.” La equivocación de Sirius hace daño sin convertirlo en una persona que quiera hacerlo: `borradores/cap-43-other-plans.md:115`, `borradores/cap-43-other-plans.md:121`.

### Cinco momentos menos logrados de la muestra

1. La explicación del gesto final en `borradores/cap-39-never-lied.md:379` y su calificación en `borradores/cap-39-never-lied.md:381`. La escena ya contiene el egoísmo y el afecto; la glosa los remata varias veces.
2. La lista de pérdidas afectivas de `borradores/cap-43-other-plans.md:75` a `borradores/cap-43-other-plans.md:89`, inmediatamente antes de que una escena muy buena las encarne. Preferiría que el incidente de la sal cargase con más de ese significado. No recomendaría cortar información del Bosque sin haber cotejado §10.
3. El segundo recorrido cómico del boggart: el mayordomo sigue sirviendo después de que ya se ha entendido el contraste entre miedo y vergüenza. La reiteración está en `manuscrito/cap-04-riddikulus.md:235` y `manuscrito/cap-04-riddikulus.md:241`. Es valoración de un capítulo publicado, sin propuesta de modificación.
4. El catálogo de pruebas de `borradores/cap-39-never-lied.md:69` y `borradores/cap-39-never-lied.md:71`. Tiene lógica que Lyra lleve una acusación preparada, pero la acumulación se acerca a una recapitulación para el lector. Mi lectura incompleta impide decidir qué prueba sobra: no he leído todos los acontecimientos evocados.
5. El discurso que recompone la sala común en `borradores/cap-40-hidden-ink.md:147`. Entiendo su función y la mezcla de orgullo y miedo; me convence menos la eficacia casi inmediata sobre toda la sala, `borradores/cap-40-hidden-ink.md:151`, que los cuidados individuales del mismo capítulo. Es una reserva de verosimilitud escénica, no una incoherencia demostrada.

## 3. Las once comprobaciones

| Comprobación | Veredicto y alcance |
|---|---|
| 1. Capítulos nuevos, costuras, amistad constante, energía | **No comprobada como prueba a ciegas.** Me faltan los tramos y he visto los sufijos de los archivos en el inventario técnico; ya no sería honesto fingir que identifico los seis capítulos solo por la lectura. En 40–43 sí hay continuidad local: receta en `borradores/cap-40-hidden-ink.md:247`, envío compartido en `borradores/cap-41-the-sleeve.md:133` y ocio sin misión en `borradores/cap-43-other-plans.md:33`. Eso no demuestra que enero–junio tenga vida de grupo sostenida. |
| 2. Diggory después de «Two Hours» y expedición al Ministerio | **Pendiente.** No he leído ni ese capítulo ni la expedición. No puedo medir el peso del hueco ni prescribir el lugar mínimo de una escena sin conocer las transiciones. La petición de Cedric de que no agredan a Harry en `borradores/cap-39-never-lied.md:5` solo evita una falsa equivalencia entre enfado y hostilidad ilimitada; no establece la futura lealtad. |
| 3. Qué sabe Ron desde «Bothy», sobre todo 67, 68 y 71 | **Pendiente.** No he leído esos capítulos. No confundo ver que Harry está afectado con conocer la información específica que el encargo sitúa en «Bothy». |
| 4. Goyle: vida propia, cocina, Hopkins, Draco y paquete | **Base local compatible; arco sin verificar.** La rapidez de Goyle con la varita ya existe en `borradores/extra-year-one-4-what-scared-actually-is.md:271`; no es simplemente una acompañante inerte. La receta de `borradores/cap-40-hidden-ink.md:247` y el intento imperfecto de `borradores/cap-41-the-sleeve.md:133` hacen de la cocina algo aprendido, no una competencia súbita perfecta. Pero ambos resultados siguen llegando a Lyra como cuidado. No puedo certificar una vida independiente, ni Hopkins, ni el paquete del 62, ni la compatibilidad con el 37. |
| 5. Crabbe y Nott respecto a 29 y 32 | **No comprobada la relación; sí existe una base de sutileza en Crabbe.** Ofrece quedarse y acepta la negativa en `borradores/extra-year-one-2-nobody-asked-you.md:165` y `borradores/extra-year-one-2-nobody-asked-you.md:169`. Su consuelo también llega sin declaración en `borradores/extra-year-one-4-what-scared-actually-is.md:411`. No he leído 29 ni 32 ni las escenas de Nott; esos cuidados no prueban por sí solos el arco solicitado. |
| 6. Cannons y diferencia entre los dos Patronus públicos | **Pendiente.** No he leído completos 53, 59, 60b y 70 ni «Two Hours». El zorro del interludio, `borradores/interludio-2-the-wrong-night.md:95`, establece una carga personal, pero no basta para explicar cuándo Harry decide exponerla ante otros. No invento esa explicación. |
| 7. Martes y jueves, incorporaciones, Draco, Umbridge y Lyra | **Pendiente.** La lista que recibe Draco en `borradores/cap-42-badges.md:71` establece un riesgo concreto para su futuro en Hogwarts. No permite juzgar la logística ni las tolerancias del grupo que todavía no he leído. |
| 8. «Who came?» después del 39 actual | **Coherente en los ecos leídos; comprobación incompleta.** En el 39, Harry escoge el punto vulnerable, `borradores/cap-39-never-lied.md:293`, y Lyra reconoce su uso, `borradores/cap-39-never-lied.md:323`. En el 40 su intento de disculpa nombra Navidad y ella lo corta, `borradores/cap-40-hidden-ink.md:113` y `borradores/cap-40-hidden-ink.md:115`. En el 42 ensaya respuestas, `borradores/cap-42-badges.md:51`: no contradice que se haya quebrado y haya respondido; imagina respuestas mejores. El interludio reconoce la intención de herir y la ironía de que él sí acudió, `borradores/interludio-2-the-wrong-night.md:63` y `borradores/interludio-2-the-wrong-night.md:65`. El 43 mantiene su responsabilidad y recuerda el episodio de los once años, `borradores/cap-43-other-plans.md:71`, compatible con el llanto que él provocó en `borradores/extra-year-one-4-what-scared-actually-is.md:315`. **No he leído la confidencia ante el espejo ni los ecos de 56 y 65.** No certifico el recorrido completo de la revelación. |
| 9. Mesa de Oclumancia y calendario de 55–72 | **Pendiente.** No he leído completos 60, 60b, 65 y 66 ni reconstruido 1996. Solo he hecho una comprobación auxiliar de calendario del bloque leído: el 31 de julio de 1995 fue lunes, compatible con el cumpleaños y la noche equivocada de `borradores/interludio-2-the-wrong-night.md:57` y `borradores/interludio-2-the-wrong-night.md:81`. El 16 de agosto fue miércoles, compatible con la excursión nocturna del interludio y el jueves posterior del cine, `borradores/interludio-2-the-wrong-night.md:175`, `borradores/cap-43-other-plans.md:95` y `borradores/cap-43-other-plans.md:103`. No sustituyo con esto la auditoría solicitada de 1996. |
| 10. Pistas del Bosque frente a decisiones §10 | **No cotejada.** He leído la mención del Bosque en `borradores/cap-43-other-plans.md:57` y el recuerdo que termina en la luz verde y la nada en `borradores/interludio-2-the-wrong-night.md:209` y `borradores/interludio-2-the-wrong-night.md:211`. Sin §10 ni los otros capítulos no puedo decidir si las pistas son justas, excesivas o incompatibles con la solución. |
| 11. Harry gris; Lyra niña que se rompe | **Cumplido en el centro del 39; reserva sobre su cierre.** Harry admite que permitió lo de Ginny por control y por obtener medios para destruir Horrocruxes, `borradores/cap-39-never-lied.md:171`; pide una mentira que lo proteja, `borradores/cap-39-never-lied.md:255`; usa una confidencia para herir, `borradores/cap-39-never-lied.md:299`; y ofrece conservar el vínculo gestionando la información que ella entregue a su familia, `borradores/cap-39-never-lied.md:327`. No es noble sin coste. Lyra sabe de dónde viene y aun así no puede controlar el llanto, `borradores/cap-39-never-lied.md:309` y `borradores/cap-39-never-lied.md:317`. Mi reserva es la admiración por la eficacia de él en `borradores/cap-39-never-lied.md:381`: puede volver elegante demasiado pronto lo que acaba de ser cruel. Es una lectura posible del efecto, no prueba de que el narrador lo absuelva. El interludio y el 43 conservan expresamente su culpa. |

## 4. Incoherencias por gravedad

**No he confirmado ninguna incoherencia grave en la muestra.** Esto no es una lista de absoluciones para los capítulos no leídos. Los dos asuntos que sí corregiría son de alcance menor:

| Gravedad | Dos referencias | Diagnóstico y reparación |
|---|---|---|
| Menor: alcance ambiguo de una afirmación | `borradores/cap-39-never-lied.md:13`: Lyra usa la varita para separar las capas de la carta de Lucius. `borradores/cap-40-hidden-ink.md:33`: “she had never once used it for anything until now”. | La segunda frase puede entenderse como que nunca había usado ese recurso, ni siquiera para leer; literalmente acaba de hacerlo. Es probable que se quiera decir que nunca lo había usado para ocultar un mensaje propio. Basta precisarlo en el 40. No hace falta cambiar el 39 ni inventar otra magia. |
| Edición: discrepancia de versión | El encargo dice que se retiraron las exclamaciones del derrumbe. `borradores/cap-39-never-lied.md:315` conserva dos y `borradores/cap-39-never-lied.md:323` conserva una. | No es una contradicción interna de la ficción. Sí exige no dar por revisado un estado del texto que el archivo no contiene. El punto 1 da los cambios exactos y distingue la intervención de Harry. |

### Asuntos que afectan a lo publicado

No propongo modificar nada del 1 al 38 ni los extras anteriores. El enlace 38–39 está cotejado en el punto 1. Dos cruces adicionales resisten:

- “I’ve never lied to you” se cuestiona expresamente por la mentira de la introducción del libro en `borradores/cap-39-never-lied.md:183`. El engaño está comprobado en `manuscrito/cap-05-manners.md:39` y `manuscrito/cap-05-manners.md:53`. El 39 no lo olvida ni necesita retocar el 5.
- La supuesta indiferencia de Lyra hacia necesitar ayuda, `borradores/cap-39-never-lied.md:333`, no se debe tomar como una nueva verdad objetiva que invalida `manuscrito/cap-05-manners.md:243`. Es una afirmación defensiva que hace mientras no consigue dominar el llanto. Corregirla para volverla factual le quitaría voz.

Tampoco considero contradictorias las culpas por Crouch: Lyra cree que habría vivido si ella hubiera avisado el sábado, `borradores/cap-41-the-sleeve.md:31`; el lector ve después que Harry demoró ocho horas la entrega de la nota, `borradores/interludio-2-the-wrong-night.md:21`. Son responsabilidades y contrafácticos distintos. Suprimir el segundo dato para proteger a Harry sí debilitaría el diseño.

## 5. Crítica de los capítulos señalados

La nota del 39 es provisional respecto a su colocación dentro de la novela; evalúa el capítulo completo y su enlace con el 38.

| Capítulo del lector | Nota | Lo mejor | Lo peor | Qué sobra | Qué falta |
|---|---|---|---|---|---|
| 39, Never Lied | 8/10 | La confesión sobre Ginny, la elección consciente de la familia y la crueldad de «Who came?». Tres conflictos que no se resuelven con una explicación amable. | El cierre explica su propia inteligencia más de lo que necesita; puede dar demasiado pronto al daño una forma admirable. | Parte de la glosa de `borradores/cap-39-never-lied.md:379`, la repetición valorativa de `borradores/cap-39-never-lied.md:381` y el subrayado final de los búhos en `borradores/cap-39-never-lied.md:399`. | No le añadiría una escena ni otra confesión. Le falta, en algunos párrafos finales, dejar actuar al gesto sin traducirlo después. |

**Sin crítica completa ni nota**, porque no los he leído: 45 Trials; 46 Rounds; 52 Lanterns; 53 Nobody; 55 Two Hours; 56 Him, and Now You; 63 In Public; 65 Three; 67 The List; 71 Bothy; 73 Through a Door; 77 Mid-Sentence; 78 Mine. Sus números y títulos proceden del encargo, no de una comprobación mía de sus encabezados.

## 6. ¿Cumple lo que se propone?

**No hay cotejo con revision-39-72.md ni decisiones §10.** No he abierto esos documentos y no atribuyo al autor objetivos que no haya leído. Respecto a los objetivos explícitos del encargo:

- El 39 preserva la responsabilidad de Harry y la pertenencia familiar de Lyra; no la convierte en alguien que solo necesitaba descubrir que sus padres eran malos.
- En el bloque 40–43, los amigos hacen cosas reconocibles fuera de una investigación: escribir, cocinar, comprar una escoba, preparar una salida. Ron y Hermione eligen su propio jueves, `borradores/cap-43-other-plans.md:39`; Sirius cambia el día de Harry con una salida real, `borradores/cap-43-other-plans.md:103`. Son acciones útiles para el objetivo de vida compartida.
- No puedo determinar si eso ocupa la línea principal durante todo el curso o si son islas. Tampoco si el misterio del Bosque cumple su promesa.

## 7. Editorial, voz, tics y cotejos

### Juicio editorial limitado

No puedo responder si la novela sostiene 78 capítulos, qué capítulo entero sobra, cómo se reparten todos los puntos de vista ni qué misterios llevan demasiado tiempo pendientes. El bloque leído sí articula tres movimientos diferentes: revelación y ruptura en el 39, consecuencias públicas y domésticas en 40–42, y respuesta de Harry en el interludio y el 43. No se limita a repetir la discusión en siete habitaciones.

Hay, sin embargo, repetición de su explicación: lo que Harry hizo en la lechucería vuelve a formularse en `borradores/interludio-2-the-wrong-night.md:63` y `borradores/cap-43-other-plans.md:71`. El cambio de punto de vista justifica volver al hecho; sería menos convincente volver siempre a demostrar que él sabía dónde herir. El dato nuevo del interludio —que él acudía a jugar— sí cambia la lectura y merece su espacio.

En esta muestra se distinguen las voces. Draco reclama cosas concretas y no comprende todo lo que repite, `borradores/cap-41-the-sleeve.md:5`; Lucius convierte afecto y utilidad en una sola conversación, `borradores/cap-41-the-sleeve.md:105`; Crabbe corrige con pocas palabras el entusiasmo de Goyle en la nota conjunta, `borradores/cap-41-the-sleeve.md:133`; Sirius pregunta por la película como alguien que está disfrutando de verdad, `borradores/cap-43-other-plans.md:107`. Harry y Lyra comparten deliberadamente el idioma de cuentas y condiciones. Lo que a veces los acerca demasiado no es el diálogo, sino una narración igualmente aficionada a explicar cada gesto con una comparación y rematarlo con otra frase.

No he hecho una auditoría completa de calcos, léxico británico, canon o anacronismos. La película del hombre vestido de murciélago en `borradores/cap-43-other-plans.md:35` no está identificada por título en el texto; no he verificado cartelera ni existencia de esa sala concreta en 1995. No la marco como anacronismo basándome solo en mi recuerdo. El calendario de 1996 queda pendiente.

### Recuento de tics

Procesamiento automático de **88 archivos**: 78 capítulos numerados, ocho extras y dos interludios. El bloque de archivos 39–72 tiene 40 capítulos y corresponde al tramo 39–78 del encargo. Los seis intercalados identificados por sufijo son 44b, 50b, 50c, 51b, 60b y 65b; no he cotejado esta identificación con numeracion.md.

Para contar palabras se excluyeron las líneas que empiezan por `#` y se utilizó `\b[A-Za-z]+(?:[’'][A-Za-z]+)*\b`. Se conservan diálogos, cursivas y cartas. Las expresiones se cuentan sin distinguir mayúsculas. «Perros» suma las palabras dog(s), puppy/puppies, hound(s) y terrier(s): **son menciones léxicas, no animales distintos ni todas las comparaciones caninas posibles**.

| Expresión | Publicado 1–38: 157.478 palabras | Archivos 39–72: 145.846 palabras | Corpus: 336.419 palabras |
|---|---:|---:|---:|
| eleven | 36 | 93 | 144 |
| léxico de perros definido arriba | 51 | 28 | 92 |
| he/she wanted it/that [clearly] understood | 0 | 4 | 4 |
| he wanted that understood, literal | 0 | 2 | 2 |
| there was | 236 | 485 | 795 |
| there were | 52 | 90 | 158 |
| as you would, cadena literal | 1 | 8 | 10 |
| it, palabra completa | 4.366 | 4.950 | 10.300 |
| It al comienzo de párrafo, incluidas comillas/cursivas iniciales | 318 | 354 | 753 |

«Eleven» pasa de **2,29 a 6,38 menciones por 10.000 palabras**, unas 2,8 veces más. «There was/were» pasa de **18,29 a 39,42**, unas 2,2 veces más. Es la diferencia más clara de estas construcciones frecuentes. «It» inicial pasa de **20,19 a 24,27 párrafos por 10.000 palabras**: aumenta, pero bastante menos. No he contado todos los comienzos de frase con «It»; el dato de la tabla es estrictamente de párrafos.

Los perros bajan de **3,24 a 1,92 menciones por 10.000 palabras**. Por tanto, este recuento no sostiene que el nuevo bloque tenga una intensificación general de perros. Puede haber acumulaciones locales o comparaciones no incluidas en el patrón. Tampoco «as you would» significa siempre la misma construcción: `borradores/cap-28-credit.md:107` contiene “as dreary as you would think so”, una comparación dentro del diálogo. No convertiría diez coincidencias literales en diez fallos de voz.

La familia estrecha de «wanted…understood» aparece en `borradores/cap-39-never-lied.md:383`, `borradores/cap-44b-trials.md:227`, `borradores/cap-49-in-fives.md:81` y `borradores/cap-64-the-date.md:7`. Dos son literalmente «He wanted that understood». No he contado como equivalentes todas las fórmulas sobre querer dejar algo claro. En el 39 hay cinco «eleven»; el dato por sí solo no obliga a eliminar ninguno: en ese capítulo la edad es parte de la acusación.

Los seis intercalados suman 19.238 palabras, 11 «eleven», 97 «there was/were» y 55 párrafos con «It» inicial. Esto da **50,42 «there was/were» por 10.000 palabras**, por encima de la media del bloque revisado. Es un dato para una futura lectura comparada, **no una demostración de costura**, y mucho menos de autoría automática.

Sobre los finales: tomando únicamente el último párrafo de cada uno de los siete archivos del bloque 38–43 más interludio 2, uno tiene una formulación claramente sentenciosa, “She did not leave gaps”, `borradores/cap-43-other-plans.md:229`. Los otros seis terminan en acción, imagen o recuerdo concreto. Esta clasificación es interpretativa y no mide los 341 finales de escena del corpus. En cambio, la autocita del bloque sí es visible: `borradores/cap-40-hidden-ink.md:25` reaparece en `borradores/cap-43-other-plans.md:65`; «Who came?» vuelve en el 42, el interludio y el 43. A veces aporta perspectiva; el riesgo es que cada repetición vuelva acompañada de su explicación.

**Rastro de prosa generada:** no hay base para atribuir un origen a partir de estos datos. En la muestra encuentro una tendencia a explicar y rematar lo ya expresado, especialmente en el cierre del 39. Es un problema editorial describible sin convertir un contador o una intuición de estilo en detector de procedencia.

### Comillas, separadores y tratamientos

Script de solo lectura sobre los 88 archivos: **6.433 comillas dobles de apertura y 6.433 de cierre**, con balance también comprobado por archivo; **cero comillas dobles rectas y cero apóstrofos ASCII**; **341 separadores ⁂**, todos solos en su línea; **cero separadores alternativos de línea formados por tres o más guiones o asteriscos**; **cero Mr. o Mrs.** con punto. No se ha verificado con un parser el emparejamiento semántico de cada intervención: igualdad de cantidades no demuestra por sí sola que todas las comillas estén bien colocadas. No hay incidencia detectada por estos controles.

### Ngramas frente a referencia/oficial-en/

He ejecutado **el script existente sin modificarlo**, con 40 archivos propios y los 92 `.md` presentes en referencia/oficial-en/, primero para N=5 y después para N=8. No he leído los textos oficiales. Las salidas se capturaron en memoria; no se generaron archivos de trabajo. Reproducción del cotejo:

```python
from pathlib import Path
import re, subprocess
ours = sorted(p for p in Path('borradores').glob('cap-*.md')
              if 39 <= int(re.match(r'cap-(\d+)', p.name).group(1)) <= 72)
refs = sorted(Path('referencia/oficial-en').glob('*.md'))
for n in (5, 8):
    subprocess.run(['python3', '-I', 'herramientas/ngramas.py', str(n),
                    ','.join(map(str, ours)), ','.join(map(str, refs))], check=True)
```

Con N=5: **221 tramos devueltos en el bloque completo**. En el 39, 14; son expresiones corrientes como “the rest of your life” o la réplica “I’ve never lied to you”. En los seis intercalados:

| Archivo | Tramos devueltos, N=5 |
|---|---:|
| cap-44b-trials.md | 9 |
| cap-50b-lanterns.md | 0 |
| cap-50c-nobody.md | 8 |
| cap-51b-two-hours.md | 9 |
| cap-60b-three.md | 3 |
| cap-65b-bothy.md | 5 |
| **Total** | **34** |

Entre ellos hay términos o fórmulas de la historia, como “defence against the dark arts” y “I must not tell lies”. El contador incluso convierte O.W.L.s en la secuencia “the o w l s”: no son cinco palabras ordinarias. No trataría la cifra bruta como porcentaje de texto copiado.

Con N=8 aparecen tres resultados: “he stood at the top of the stairs” en `borradores/cap-51-four-hours.md:263`, atribuido por el script a ko-72.md; “when he spoke again his voice had dropped” en `borradores/cap-60-furniture.md:163`, a ko-81.md; y “and there was nothing to be done about it” en `borradores/cap-68-ask-me.md:71`, a ko-78.md. Son construcciones narrativas comunes, sin singularidad suficiente por sí solas para proponer una reparación. **Ninguno pertenece a los seis intercalados.** Las atribuciones oficiales son las que devuelve el programa, sin comprobación manual de su contexto ni de su línea.

Límites importantes del instrumento: elimina puntuación y puede cruzar frases; filtra ventanas según una lista de palabras; guarda un solo archivo de referencia por ngrama; y prolonga una coincidencia si las ventanas siguientes existen en el diccionario, sin exigir que procedan de un mismo pasaje o archivo. Por eso una secuencia larga que salga con N=5 no queda automáticamente confirmada como una cita continua de esa longitud. De hecho, el tramo de ocho palabras aparente del 71, “felt for the first time in his life”, aparece al prolongar ventanas con N=5, pero no sale con N=8. No lo he elevado a coincidencia continua verificada ni he abierto la referencia para resolverlo.

**Resultado: no ha aparecido una coincidencia que por sí sola justifique una alarma textual.** No es una certificación de originalidad ni cubre traducciones, paráfrasis o frases de dos a cuatro palabras. La cabecera del script recomienda buscar también estas últimas; ese cotejo adicional contra las referencias **no está hecho**.

## 8. Guion 73–84

**No leído; no hay dictamen sobre qué se sostiene o qué falla en ese guion.** No utilizo el nombre del archivo ni el encargo para fingir que conozco sus escenas. Solo puedo señalar obligaciones ya existentes en el bloque leído:

- La culpa de Harry incluye decisiones propias y tiempos perdidos. La demora de la nota no puede desaparecer del balance si después se pretende juzgar la de Lyra: `borradores/interludio-2-the-wrong-night.md:21` frente a `borradores/cap-41-the-sleeve.md:31`.
- El acercamiento no equivale a perdón. El 40 evita una disculpa completa, `borradores/cap-40-hidden-ink.md:113`, y el 42 conserva su enfado, `borradores/cap-42-badges.md:53`.
- Hermione ha observado el procedimiento de la carta y la evasiva de Harry, `borradores/interludio-2-the-wrong-night.md:13` y `borradores/interludio-2-the-wrong-night.md:17`. Su inteligencia ya tiene un punto de apoyo concreto.
- La tarea que recibe Draco es materialmente peligrosa y Lyra decide no quitarle el papel: `borradores/cap-42-badges.md:71`, `borradores/cap-42-badges.md:185`. No es solo color familiar.

Es posible que 44–72 ya desarrollen o paguen estas obligaciones. No las doy por pendientes al llegar al 78 sin haber leído ese tramo.

## 9. Ideas que mejoran lo comprobado

No añadiría material al 39. Probaría una versión con menos glosa al final: conservar deuda, egoísmo y decisión, pero dejar que parte del significado recaiga en que ella sale de la torre y él no consigue convertir el último intento en una broma. El punto 10 propone recortes concretos.

Para revisar el conjunto más adelante, una pregunta útil es si cada regreso a «Who came?» añade **información o conducta**. El interludio sí añade que Harry era el visitante; el 42 añade cómo Lyra ensaya otras respuestas. Cuando solo vuelva a nombrarse la misma culpa, ese sería un lugar razonable para recortar antes de sacrificar escenas de grupo. No recomiendo insertar una escena de Cedric en una fecha que no he verificado.

## 10. Correcciones concretas: diez propuestas, no quince

No completo artificialmente quince con cinco sustituciones que no puedo justificar. Las cuatro primeras recogen los ajustes del punto urgente; la quinta aclara el alcance del encantamiento del 40. Las cinco restantes son **opciones de poda**, no condiciones para publicar. Conviene leerlas juntas antes de adoptarlas: su efecto acumulado es un cierre más seco.

| Prioridad | Archivo:línea | Texto actual → propuesto |
|---|---|---|
| 1. Expresión | `borradores/cap-39-never-lied.md:51` | “the bandage had come through his trousers in a long brown stain” → “blood had seeped through his bandage and left a long brown stain on his trousers” |
| 2. Cierre de versión | `borradores/cap-39-never-lied.md:315` | “Nobody *came!*” → “Nobody *came*.”; “I am going *home!*” → “I am going *home*.” |
| 3. Cierre de versión | `borradores/cap-39-never-lied.md:323` | “You *did!*” → “You *did*.” |
| 4. Cierre de versión, según alcance de la decisión | `borradores/cap-39-never-lied.md:255` | “You could have looked at the *floor!*” → “You could have looked at the *floor*.” |
| 5. Precisión de continuidad | `borradores/cap-40-hidden-ink.md:33` | “she had never once used it for anything until now” → “she had never used it to hide a message of her own until now” |
| 6. Evitar la fórmula de énfasis | `borradores/cap-39-never-lied.md:383` | “She wanted it clearly understood that nothing was forgiven.” → “She had forgiven him nothing.” |
| 7. Quitar una repetición inmediata | `borradores/cap-39-never-lied.md:373` | “She had taken him apart, in order, under headings, with her nose running, and he was still standing there, on one leg.” → “She had taken him apart, in order, under headings, and he was still standing there, on one leg.” Ya figura la misma imagen en `borradores/cap-39-never-lied.md:371`. |
| 8. Reducir la glosa del cierre | `borradores/cap-39-never-lied.md:379` | Sustituir el párrafo que empieza “She knew what this was” y termina “as hard as he could” por: “She was going down those stairs, and he wanted her to stay. He could not keep her, so he meant her to take this home. It would sit at her father’s table. There was no parcel it could be sent back in.” Conserva la maniobra sin explicarla de tantas formas. |
| 9. Confiar en el efecto de la escena | `borradores/cap-39-never-lied.md:381` | “It was very well done.” → suprimir. Lyra ya ha usado la misma valoración, con intención hiriente, en `borradores/cap-39-never-lied.md:323`. Aquí la reiteración puede concederle una elegancia que el resto del capítulo no necesita garantizar. |
| 10. Acabar con menos subrayado | `borradores/cap-39-never-lied.md:399` | “He had tried to make it a joke. She heard him try. It came out on no breath at all, and there was not an owl in that tower that could have taken it for one.” → “He had tried to make it a joke. It came out on no breath at all.” La salida de Lyra sigue siendo el cierre de la escena. |

No se ha aplicado ninguna de estas propuestas al manuscrito. Quedan sin entregar la lectura completa, la mayor parte de las once comprobaciones, trece críticas de capítulo, el cotejo con la planificación, la revisión del guion y cinco correcciones adicionales justificadas. El dictamen urgente del 39 y los controles automáticos anteriores sí están hechos con el alcance indicado.
