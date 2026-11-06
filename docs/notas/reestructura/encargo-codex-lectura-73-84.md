# Encargo de Codex: lectura de la tanda 73-84 (79 a 92 del lector)

*6 de noviembre de 2026. Va después del cuaderno de lector (`encargo-codex-cuaderno-lector.md`).*

**Cuál pegar:**
- **Si el chat antiguo dice que le cabe y conserva la memoria:** el bloque A, en ese chat.
- **Si no:** el bloque B, en un chat nuevo. Se pega A a continuación de B.

## Bloque B: solo en un chat nuevo, antes del bloque A

```
Vas a leer la última tanda de «Never Own a Malfoy, Potter», un fanfic largo de Harry Potter en inglés británico con Lyra Malfoy en lugar de Draco. Se publica por entregas en Wattpad y Webnovel. El autor es Edén. Repositorio: Weinling/fanfic-hp-malfoy, rama main.

No vas a leer toda la novela: son unas 420.000 palabras, y no hace falta. Eres el relevo de otro lector. Para ponerte en su sitio, lee solo esto, en este orden:
1. docs/notas/criticas-codex/cuaderno-lector.md, entero: es lo que recuerda quien leyó del 1 al 78. Trátalo como su memoria, no como verdad: puede equivocarse.
2. docs/notas/criticas-codex/lectura-39-78.md: puntos 2, 4 y 7. El punto 8 no: habla del guion y se lee en la fase 2.
3. docs/notas/reestructura/numeracion.md.
4. En borradores/, enteros, como entrada y sin criticarlos: cap-69-you-were-missed, cap-70-cousins, cap-71-mid-sentence, cap-72-mine.

Del resto de la novela no leas capítulos enteros. Cuando dudes de un nombre, un objeto, una fecha o un «primera vez», usa grep en manuscrito/ y borradores/ (solo cap-*, extra-* e interludio-*) y lee ese pasaje. El repositorio es tu memoria: no tienes que retenerlo, solo saber buscarlo. Di en el informe qué has buscado y qué no.

Di también, al principio del informe, que no has leído la novela entera, y que por eso tu juicio sobre el cansancio acumulado vale menos.
```

## Bloque A: la lectura

```
Ahora lee la tanda nueva. Haz git pull --ff-only y trabaja en main. Si .autonomo.lock tiene menos de cinco horas, no toques git: escribe el informe y avísame.

SITUACIÓN
- Publicado: del 1 al 38, que no se puede tocar. El 39, con el autor. Del 40 en adelante se puede cambiar a fondo.
- Tu informe del 1 al 78 se aplicó. No todo: docs/notas/reestructura/decisiones.md y los manuales dicen qué cambió, y puedes verlo con git log.
- Si eres el lector anterior: no te fíes de tu memoria de los capítulos 60b, 62, 64, 65b, 71 y 72. Han cambiado. El grupo de Diggory tiene ahora una escena al principio de cap-64-the-date.md. Léela antes de empezar, y dime si el hueco de enero a junio sigue pesando.
- La tanda son catorce capítulos, un interludio y un extra, unas 85.000 palabras. Termina el 19 de diciembre de 1996.
- Los títulos llevan el número del lector. Los archivos, el de trabajo: cap-86-twenty-three.md es el capítulo 92. Cita por archivo:línea.
- Son menores. Nada sexual ni sensual, tampoco en lo que propongas.

CÓMO TRABAJAR
Fase 1, a ciegas. Lee cada capítulo entero, en orden, una vez, sin notas, sin subagentes y sin docs/. No abras coreano/, fuentes/ ni referencia/. En esta fase solo puedes usar grep si eres relevo y te falta un dato.

ORDEN DE LECTURA, en borradores/: cap-73, cap-74, cap-75, interludio-3-the-cobb, cap-76 a cap-81, extra-year-four-3-out-of-your-depth, cap-82 a cap-86.

Fase 2. Escribe lo que sentiste antes de leer nada más. Luego lee docs/notas/reestructura/decisiones.md (§5, §6, §8, §9 y §10) y docs/archivo/guiones/guion-tanda-73-84.md, y compara. No leas docs/notas/criticas-opus/.

No edites capítulos. Escribes dos cosas: el informe y el cuaderno.

TU PRIORIDAD
Coherencia, que sea disfrutable y de alta calidad, y que cumpla lo que se propone. Las ideas, después.

LO QUE NADIE HA REVISADO BIEN
Después de la crítica se hicieron dos pasadas a mano, y nadie las ha leído en frío: tics del 71 al 86, y frase larga del 80 al 86. Son unas 150 reescrituras de párrafo. Busca dónde se ha roto la voz, dónde un párrafo unido suena peor que los trozos, y dónde una frase larga estropea un golpe. También si el 85 y el 86 siguen distinguiendo el clímax del pasillo.

LO QUE QUIERO QUE COMPRUEBES (números de archivo)
1. Las reglas de la Marca (78): oye, no ve, no duerme, el viento la tapa. ¿Se cumplen en todos los capítulos? ¿Alguna escena las dobla porque le conviene? ¿Se entiende por qué Lyra no le escribe a Harry, y cuándo se entiende?
2. El 81. Harry sabe que ella corrió por el castillo, y ella le dice lo contrario al oído de Riddle. ¿Es un malentendido romántico barato o se sostiene? Ese era tu miedo.
3. La lealtad de lo publicado: ¿Sirius, en el interludio, y Lupin, en el 73, encajan con lo que eran? Si el «Prongs» del 72 duele más o menos ahora.
4. Bones, en el 75: ¿queda a su altura? ¿Es creíble la jugada de las cuatro casas? ¿Y que Susan y Hopkins lleguen a Lyra en el 84?
5. Goyle: ¿tiene vida propia antes de morir, o la tienda llega tarde? ¿Pagan el 84 y el 85 lo sembrado? ¿El «No» y la muerte son consecuencia o trampa del autor?
6. Lo que cubre la muerte de Goyle: Snape, Pomfrey, Mrs Goyle y Dumbledore. ¿Se investigaría más? ¿Hay alguien hecho tonto?
7. El grupo en sexto: que lo lleve Neville, «Not you», Hopkins diciendo no. ¿Tiene consecuencias reales fuera de la pareja?
8. Ron: Ron narrador en el 83, ¿tiene voz propia y hace reír? Ron y Hermione, ¿se responde a la mentira? Ginny, ¿vida propia o confidente? Su hora perdida, ¿le pesa de verdad?
9. Harry gris: la tortura planeada, «Please come» en público, Moody, el cuaderno negro, la fuente. ¿Lo pierdes como lector? ¿Dónde se le limpia? «Move!» y «Sec—»: ¿absuelven al surco lo que debe ser suyo?
10. Lyra se rompe, y no solo en privado. ¿Dónde se pasa, y dónde se vuelve demasiado adulta?
11. Riddle y la rata: que parezca que oyó el cuarto y solo tenga papeles. ¿Se sostiene? ¿Dice algo que un papel no podría darle?
12. El final del 86: ¿se entiende lo del ojo sin explicarlo?
13. Cuentas: el calendario de junio a diciembre de 1996, veinticuatro y veintitrés, los días contados, y quién sabe qué al final.

EDITORIAL
¿Cuál es el capítulo más flojo? ¿Qué se alarga? ¿La tanda abusa de lo mismo: silencios, objetos que vuelven con su historia entera, brazos que suben, gestos mudos al final? Voces, calcos del español, léxico no británico, anacronismos, errores de canon. Rastro de prosa generada: mide, no opines en abstracto.

COTEJO
Pasa herramientas/ngramas.py con estos capítulos contra referencia/oficial-en/ sin leer esos textos, y comprueba con un script comillas tipográficas, ⁂ y Mr/Mrs sin punto.

EL INFORME
En docs/notas/criticas-codex/lectura-73-84.md, en español, con citas en inglés y archivo:línea.
1. Como lector: dónde te enganchaste, dónde te aburriste, dónde lo habrías dejado, cinco mejores momentos y cinco peores.
2. Las trece comprobaciones, una por una, con veredicto.
3. Las dos pasadas: qué han estropeado, con texto actual → propuesto.
4. Incoherencias por gravedad, citando las dos líneas.
5. Tabla por capítulo: nota, lo mejor, lo peor, qué sobra y qué falta.
6. Editorial y tics, medidos.
7. Qué le exige esto al tramo siguiente: de diciembre de 1996 a julio de 1997.
8. Las quince correcciones más importantes, texto actual → propuesto, en inglés británico con comillas tipográficas. Nada del 1 al 38.

EL CUADERNO
Al acabar, actualiza docs/notas/criticas-codex/cuaderno-lector.md para quien te releve: añade lo que esta tanda ha prometido, cumplido y roto, con las mismas reglas de siempre, y [PLAN] en lo que sepas por la fase 2. Que no pase de 4.000 palabras: si hace falta, recorta lo que ya esté pagado.

Commit solo de esos dos archivos, con rutas explícitas, y push de main. Dame las rutas y el veredicto en cinco líneas.

Di con honestidad lo que no hayas leído o comprobado. Si te falta contexto antes de terminar, para, dilo y entrega lo que tengas; no sigas leyendo a medias.
```
