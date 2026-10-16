# Beats rehechos (16 de octubre de 2026): informe para revisión externa

Encargo del autor: cambiar cómo se desarrollan las situaciones (beats), no solo las frases, para que la historia deje de calcar el esqueleto del original coreano. Condiciones:
- no se cambian los hechos;
- las frases icónicas, solo un poco;
- quien ya leyó lo publicado no debe notar otra historia.

Palanca casi siempre: que Lyra mueva la escena en vez de reaccionar, o abrir en otro punto y contar lo anterior de recuerdo.

## Tres versiones de cada capítulo

| Versión | Dónde está |
|---|---|
| **Original publicado** (lo que leen Wattpad 1-21 y Webnovel 1-23 + *Year One*) | `git show 888ff27:<ruta>` |
| **Revisado** (cotejo de frases, antes de tocar beats) | `git show eee1bdc^:<ruta>` |
| **Nuevo** (beats rehechos) | la rama actual |

Los *Year One* 1 y 2 no tenían versión revisada: original = revisado.

## Qué cambió y cuánto

Parecido de texto entre versiones (1,00 = idéntico; mide palabras y orden).

| Cap. | Rev.→nuevo | Orig.→nuevo | Qué cambia en la estructura |
|---|---|---|---|
| 1 | 0,70 | 0,67 | Arranca en escena (la noticia en la sala común); Lyra deduce ella lo del caldero; intenta comprar el diario |
| 2 | 0,70 | 0,64 | Arranca en el lago; Lyra farolea con su padre («I saw you put it in her cauldron») |
| 3 | 0,88 | 0,77 | Arranca con la varita en el botón del guardia; Lyra se ofrece a sujetar a Potter |
| 4 | 0,69 | 0,62 | La clase arranca con el pulpo atado; Lyra pide la revancha y acaba ella con el boggart (tercer *Riddikulus*); la charla sobre el que no se nombra, después, con la servilleta al cuello |
| 5 | 0,80 | 0,64 | Arranca en la clase («How?»); el prefacio falso como contraamenaza; el hipogrifo empieza con Harry en el aire; en la enfermería, primero los dedos y luego la amenaza en frío |
| 8 | 0,76 | 0,71 | La discusión, en la cola de Filch; la tarde como búsqueda; de noche, la cara de Harry («*Just missed him*») lleva a Lyra a deducir el cómplice |
| 10 | 0,92 | 0,84 | El *Impervius* deducido desde el aire; Lyra le agarra la túnica antes del segundo intento, que falla igual; encuentra ella la Snitch |
| 11 | 0,82 | 0,71 | Lyra abre acusando a Snape de ser el cómplice; la enfermería contada desde el lago; el perro como prueba del aviso del tren |
| 13 | 0,86 | 0,60 | Arranca a mitad de la confidencia; Lyra ve las huellas de Harry en la nieve y espera a propósito; adivina al animago antes de la transformación |
| 14 | 0,92 | 0,63 | Black saca lo del chocolate; la pregunta a Black abre la explicación del vínculo; el «Hands off» cae sobre una oferta de Lyra (lo que sabe de los Black) |
| 18 | 0,72 | 0,62 | Lyra entiende la táctica de Diggory y la usa (30-0) hasta que él saca a Potter; Mrs Norris abre la escena de la escalera; los anillos, esa noche |
| 19 | 0,96 | 0,69 | Lyra ve el dedo de la rata y se lo calla; cobra su silencio a Lupin; llega a la discusión a cobrar la deuda de Harry |
| 20 | 0,93 | 0,68 | Arranca en el cajón; Lyra lanza a Buckbeak en picado contra el lobo; ante Pettigrew, la elección se ve en escena |
| 21 | 0,93 | 0,60 | Arranca ya en el pasado; Lyra ve el anillo de Harry desde el principio y se lo calla; es ella quien entiende la persecución |
| 22 | 0,93 | 0,77 | Lyra se lanza al oír lo del neutralizador y Harry la sujeta; marca ella el «Now» del patronus; se adelanta a Dumbledore |
| 23 | 0,85 | 0,53 | Arranca con las lechuzas y la carta; la final, contada por el marcador que Lyra calcula; en el claustro se adelanta ella («I heard. We’re not going out») |
| *Year One* 1 | 0,66 | 0,66 | La Selección empieza dentro del Sombrero; el sapo naranja en escena; la clase de vuelo, reescrita en su narración |
| *Year One* 2 | 0,41 | 0,41 | Abre con Lyra huyendo en la nieve; Harry después; Lyra de noche con el recuerdo |

Sin cambios de estructura: 6, 7, 9, 12, 15, 16 (salvo una línea) y 17.

## Cómo se revisó

- Cada capítulo pasó por un revisor Opus que no era a ciegas. Comparó contra lo publicado y contra la versión anterior, clasificó cada cambio de la A a la D y buscó citas rotas en los capítulos posteriores.
- El bucle 19-22 lo revisó un revisor nuevo, que leyó los cuatro juntos.
- Hallazgos corregidos: una pregunta duplicada (14), un marcador que no sumaba (18), «ten days» → «days» (20), dos cambios de clase C devueltos a B (el lobo vuelve a atacar a Lyra en el 20; Dumbledore vuelve a deducir en el 22).
- Veredicto de todos: «mejor que lo publicado, publicable».

**Falta.** No se ha hecho una comparación a ciegas entre revisado y nuevo. Es la que decide si el cambio de beats mejora la versión revisada. Pregunta sugerida para el crítico: por capítulo, ¿cuál de las tres versiones es mejor en gancho, claridad, agencia de Lyra, voz, lógica y emoción? ¿El nuevo pierde algo del revisado que convenga recuperar?

**Volver atrás.** Cualquier capítulo se puede devolver a la versión revisada sin tocar el resto: `git show eee1bdc^:<ruta> > <ruta>`. Después hay que comprobar las citas de los capítulos vecinos; los manuales dicen cuáles son.
