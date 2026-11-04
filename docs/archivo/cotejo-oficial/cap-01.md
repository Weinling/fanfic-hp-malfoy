# Capítulo 1: cotejo con la traducción oficial

Fecha: 2026-10-15. Texto oficial en `referencia/oficial-en/cap-01-prologo.md`. Coincidencias literales con `python3 -I herramientas/cotejo.py referencia/oficial-en/cap-01-prologo.md manuscrito/cap-01-hostage.md 3`.

**Criterio.** Lo que pasa no se toca: el diario, el Horrocrux, el siete, los refugios, «our hostage», el apretón de manos. Sí se puede cambiar la frase, la imagen y el orden de los argumentos cuando calcan el original. Antes de tocar una línea, hay que buscar si algún capítulo posterior la cita (tabla de semillas en `docs/notas/revisiones/lecciones-draconia-y-plan-1-2-3.md` §2).

Números de línea: `manuscrito/cap-01-hostage.md` tal como está publicado. Ojo: `borradores/cap-01-recorte.md` (12 de octubre, propuesta del autor) ya quita dos de los tres comentarios ajenos de la apertura; si se adopta, solo queda el de la familia.

## Rojo: se reconoce a la primera

| Línea | Nuestro | Oficial | Propuesta |
|---|---|---|---|
| 251 | “You probably don’t know anything useful anyway.” | Idéntico | Quitar la frase; la siguiente (“Your dad’s not going to tell his twelve-year-old his plans”) ya hace el trabajo |
| 169 | “Your dad’s just cost Voldemort one of his seven lives… Your family needs to keep its head down.” | “…one of Voldemort’s seven lives. Your family needs to keep its head down.” | “Your dad’s just lost Voldemort a seventh of his insurance.” El “Seven?” de Lyra sigue funcionando, y la palabra vuelve en la línea 247, cuando Harry la llama a ella “Insurance” |
| 227 | “knives and forks… sit down to dinner on everything you’ve got” | “come to the table with forks and knives, ready to carve up everything you have” | Imagen nueva del mundo de Lyra: “Between the two of them there won’t be a teaspoon left at the Manor with your crest on it.” |
| 293 | La mano como serpiente que ataca, los colmillos | “That hand looked… exactly like a serpent’s fang” | Cambiar la imagen de cierre. Por ejemplo, la mano como un contrato ya firmado con sangre (la tiene en los nudillos) que espera su firma debajo. Siembra el libro de cuentas del 7 |
| 11–19 | Los tres comentarios ajenos: guapa / la familia está en todas partes, “only four of them” / Snape la favorece en Pociones y en el campo | Los mismos tres, en el mismo orden y con el mismo contenido | Mantener el recurso (tres virtudes, voces ajenas), pero con quejas nuevas. Ejemplos: “It isn’t fair. She doesn’t even *try*. She just stands there.” · “My mum says her dad paid for the new greenhouse roof. She says it like it’s a threat.” · “Snape gave her full marks for a Swelling Solution that was *orange*.” |

## Ámbar: misma estructura, otras palabras

- **133–157, el argumento de Harry**: «demuéstralo» → «piensa, idiota, tendría que llevarlo al Ministerio y se enterarían los mortífagos» → «tu padre estaría mejor confesando lo de la Cámara» → «lo peor sería Azkaban» → «tiene amigos en el Wizengamot» → «Voldemort no hará juicio, le matará». Es la misma secuencia del original. Propuesta: reordenarla (que Harry empiece por Voldemort y deje la confesión para el final, como salida que Lyra rechaza) y cambiar “the worst the Ministry could do” (calcada).
- **77**: “Shut up for a minute and listen” ≈ “Shut up and listen”. Basta con otra orden (“Stop talking, Malfoy”) y ajustar la línea 79.
- **93**: “You and your dad are in a lot of trouble” ≈ “You and your father. You’re both in a very difficult position”.
- **223**: “This is blackmail, Malfoy” ≈ “This is a threat, Malfoy”.
- **283–287**: “You’re smarter than I thought” y su remate ≈ “smarter than you look… a very low bar”. Es el mismo chiste.
- **271**: “whoever won, the Malfoys would still be standing in the middle of it” ≈ “she would still be the protagonist of whatever world followed”, en el mismo sitio de la escena.
- **29 y 31**: las gafas (“might even have been called handsome”) y “unpretentious / poor breeding” ≈ “passable… worth a second glance” y “down-to-earth / dirt-poor”.
- **31**: las notas, que se deben a Granger, como en el original.
- **37**: lo de morderse las uñas por la Copa y Crabbe parándola es un detalle muy concreto del original. **No tocar sin más**: el 2 lo cita (línea 177) y el gesto es del personaje. Como mucho, cambiar la forma en que Crabbe la para.

## Verde: es nuestro o es trama

Madam Malkin’s y el tren (se paga en el 16), Dobby y el calcetín, Borgin’s y “Not that one”, la pregunta del siete y la pausa, el cuarto de debajo de la escalera, “Act like you, then”, Northumberland, “then you, at least” (frase guía del capítulo; viene de “If that’s not possible, then at least you do”, pero la vacilación y la cara de doce años son nuestras).

## Coste estimado

Unas 15 intervenciones en un capítulo de 4.700 palabras, en torno a un 8 % del texto, sin cambiar hechos. Lo más delicado es la apertura (11–19), porque es lo que lee todo lector nuevo.

## Aplicado (15 de octubre de 2026)

Base: el texto **publicado** que pasó el autor (el arranque recortado de `borradores/cap-01-recorte.md` más el resto). `manuscrito/cap-01-hostage.md` no coincidía con él y se ha igualado antes de retocar (commit aparte).

- **Apertura:** la única cita ajena que quedaba («How are they everywhere?») pasa a «They’re like dry rot, the Malfoys. You find them in the walls». Las gafas se cambian por «Somebody who had never heard him open his mouth». La teoría de las notas pasa a ser Granger («the theory was Granger»). La uña: Crabbe le coge la muñeca y le baja la mano a la mesa; sigue cuadrando con el 2.
- **«Shut up for a minute and listen»** → «Malfoy. Stop talking for one minute».
- **«You and your dad are in a lot of trouble»** → «has done something very stupid, and you’re going to have to help him live through it».
- **El argumento**, reordenado. Fuera «Think, you idiot» y «the worst the Ministry could do». Ahora va: la Ministry es lo fácil → confesar lo de la Cámara sería mejor → Voldemort no hace juicios → Lyra saca el Wizengamot → «And none of them are going to be in the room».
- **«One of his seven lives»** → «a seventh of his insurance». Lyra salta igual en «A *seventh*», y la palabra vuelve cuando Harry la llama «Insurance» («she did not care for the company»). En el 4, «one of seven lives gone» pasa a «one piece of seven gone».
- **«Your family needs to keep its head down»** → «So your family wants to go very quiet». «Your family needs to stay out of it» → «So you lot stay out of it». **«Then you, at least» se queda.**
- **«This is blackmail, Malfoy. Just so you know»** → «I’m blackmailing you, by the way. In case that wasn’t clear».
- **Los cuchillos y tenedores** → «there won’t be a teaspoon left at the Manor with your name on it». «Your family’s finished» → «that’s the end of the Malfoys».
- **Fuera «You probably don’t know anything useful anyway».**
- **«Whoever won, the Malfoys would still be standing»** → «Wars… were things that happened to other families, and the Malfoys sent flowers afterwards».
- **«I’ll be on your side»** → «Whatever *it* is».
- **«Smarter than I thought… the nicest thing»** → «I thought there’d be hexes» / «The night is young».
- **La serpiente** → la sangre de los nudillos como tinta, un contrato ya firmado que espera su nombre.

El script ya solo encuentra coincidencias de nombres y fórmulas neutras («the Chamber of Secrets», «Board of Governors»).
