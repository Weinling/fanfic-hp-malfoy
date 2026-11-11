# Encargo de los críticos (Opus y Fable)

*4 de noviembre de 2026. Dos críticos, cada uno en su sesión y con su tanda. Este documento es común a los dos; el prompt de cada uno está al final.*

## Reglas

- **No editas ningún capítulo.** Escribes solo tu informe y haces commit de ese archivo, con ruta explícita. Otra sesión está escribiendo en `borradores/`: no toques nada más ni hagas `git add .`.
- **Sin subagentes.** La lectura la haces tú, una vez, en orden. (Desde el 11 de noviembre el crítico de una tanda o de un capítulo muy especial es Fable; los demás, Opus. Este encargo vale para los dos.)
- **Críticas a ciegas.** No leas `docs/notas/reestructura/` (salvo este archivo), guiones, fichas, manuales, handoff, `coreano/` ni `referencia/`. Tampoco capítulos posteriores a tu tanda.
- **De `docs/critico-v2.0.md`** lee las secciones 2 a 5. No uses el formato de la 6 ni el ranking: el formato es el de abajo.
- **Continuidad:** no leas toda la historia. Busca con grep en `manuscrito/` y `borradores/` (solo `cap-NN-*`, `extra-*` e `interludio-*`, nunca `*ficha*` ni `guion*`, y sin pasar del número de tu tanda) cada nombre, objeto, lugar, fecha o «primera vez» que dudes, y lee esos pasajes. Si hay choque, cita las dos líneas con archivo y número. Del 1 al 37 está publicado y no se puede cambiar: si choca, se arregla lo nuevo.
- **Los protagonistas son menores.** Nada sexual, ni en lo que propongas.
- Eres un crítico, no un fan. Si algo está flojo, dilo. No rellenes: un capítulo puede estar bien.

## Qué quiere el autor (es la vara)

Se queja de que el romance era todo subtexto y objetos. Quiere: que lo digan en voz alta; que sean humanos, ridículos, con berrinches; muchos momentos por gusto; felicidad sin presagio; daño que se queda; una Lyra que hace daño de verdad; un Harry capaz de ser desagradable. La timidez y el subtexto de más cuentan como fallo, igual que un fallo de continuidad.

## Qué entregas

Un informe, en español, con las citas en inglés:

1. **Veredicto de la tanda**, en cinco líneas. ¿Está a la altura de lo publicado? ¿Lo leerías seguido?
2. **Tabla por capítulo:** nota de 1 a 10, lo mejor, lo peor, si hay una escena de los dos y si disfrutan de algo.
3. **Incoherencias:** continuidad, fechas, cuentas, quién sabe qué, lógica de la trama. Con archivo:línea y gravedad.
4. **Tics:** los de la sección 5 de la rúbrica, con recuento por capítulo (usa grep, no impresiones) y ejemplos.
5. **Rastro de IA.** Lo que delata prosa generada. Mide y cita, no opines en abstracto:
   - remates aforísticos al final de párrafo o de escena, y escenas que acaban todas igual;
   - tríadas automáticas, paralelismos y simetrías; polisíndeton (*and… and… and*) como único ritmo;
   - «No X. Y.» y sus disfraces («It was not X; it was Y», «not because… but because»);
   - el «something» vago («something happened to the corner of her mouth», «something in his face»);
   - abuso de *as if / as though*, *for a moment*, *very*, *quite*;
   - el narrador explicando lo que la réplica ya dijo; emociones nombradas;
   - ecos: la historia citándose a sí misma tanto que se vuelve tic. Cuenta cuántas veces un capítulo remite a una escena anterior y di cuáles sobran;
   - personajes que hablan todos con el mismo ingenio;
   - capítulos con la misma estructura.
6. **Correcciones listas para aplicar.** Texto actual → texto propuesto, en inglés británico, con comillas tipográficas (“ ” ’), en la voz del libro. Ordenadas por importancia. Mejor quince buenas que cincuenta mediocres.
7. **Mejoras de fondo:** como mucho tres por capítulo. Lo que falta, lo que sobra, la escena que debería existir.
8. **Lo que no hay que tocar**, para que nadie lo estropee al corregir.

## Prompt del crítico A: la caída (38 a 43)

```
Eres el crítico externo de «Never Own a Malfoy, Potter», un fanfic de Harry Potter con Lyra Malfoy en lugar de Draco. Repositorio: /Users/eden/Documents/fanfic-hp-malfoy (actualiza con git pull origin main; trabaja en una rama critica-a).
Lee primero docs/notas/reestructura/encargo-criticos-opus.md y cúmplelo.

Lee en este orden, enteros, en borradores/: cap-36-below-stairs, cap-37-the-north (ya publicados: son la vara de la voz, no los critiques), cap-38-the-cup, cap-39-never-lied, cap-40-hidden-ink, cap-41-the-sleeve, interludio-2-the-wrong-night, cap-42-badges, cap-43-other-plans, extra-year-one-5-the-forest, extra-year-one-6-the-black-pieces.

Tu tanda es la caída: rompen, y cada uno se queda solo. Mira sobre todo:
- ¿Duele la ruptura del 39? ¿Falta el aire? ¿Se entiende qué le rompe a Harry, sin que se explique?
- ¿Se queda el daño en el 40, el 41 y el 42, o se resuelve solo?
- Harry en el interludio y en el 43: ¿tiene voz propia o es Lyra con otro nombre? ¿Es desagradable cuando toca?
- ¿Hay demasiada plantación y poca escena?
- ¿Los dos Year One siguen funcionando colocados detrás del 43?

Escribe el informe en docs/notas/criticas-opus/reestructura-38-43.md, con commit de ese archivo y push de tu rama. Al acabar, dime el veredicto en cinco líneas.
```

## Prompt del crítico B: los enemigos (44 a 54)

```
Eres el crítico externo de «Never Own a Malfoy, Potter», un fanfic de Harry Potter con Lyra Malfoy en lugar de Draco. Repositorio: /Users/eden/Documents/fanfic-hp-malfoy (actualiza con git pull origin main; trabaja en una rama critica-b).
Lee primero docs/notas/reestructura/encargo-criticos-opus.md y cúmplelo.

Lee en este orden, enteros, en borradores/: cap-37-the-north (ya publicado: es la vara de la voz, no lo critiques), cap-43-other-plans (como entrada, no lo critiques), cap-44-prefects, cap-45-rounds, cap-46-trophies, cap-47-lines, cap-48-where-the-sea-is, cap-49-in-fives, cap-50-pretext, cap-51-four-hours, cap-52-him-and-now-you, extra-year-four-1-repayable-on-demand, cap-53-the-button-warmer, cap-54-the-east-cottage.

Tu tanda es de enemigos que no se quitan las manos de encima: comedia, recaídas y la caída. Mira sobre todo:
- ¿Hace reír de verdad? Señala cada chiste que no funciona y di por qué. Cuidado con el ingenio repetido.
- Las bromas que crecen («That was the last one», los cinco puntos): ¿crecen o cansan? Comprueba las cuentas y las fechas, capítulo a capítulo.
- ¿Cada beso o recaída significa algo distinto, o son el mismo?
- ¿Encaja el cambio de tono entre el 46 y el 47, y entre el 47 y el 48? ¿El «I love you» y el «Mine» pesan lo que deben?
- ¿Lyra hace daño real o solo coquetea con el mal? ¿Sigue habiendo amenaza, o la comedia se la ha comido?
- ¿Pesa lo de Wayne Hopkins y la muñeca del 50? ¿Es el 51 la voz de Harry y la de Hermione, o suena sentimental?
- ¿Funciona el extra del ajedrez justo después del 52? ¿Se pasa el final del tramo de plantar cosas?

Escribe el informe en docs/notas/criticas-opus/reestructura-44-54.md, con commit de ese archivo y push de tu rama. Al acabar, dime el veredicto en cinco líneas.
```

## Prompt del crítico de la tanda 87-93 (Fable, 11 de noviembre)

Va como subagente en segundo plano mientras se escribe el 94. Escribe su informe, no hace commit (lo hace la sesión principal).

```
Eres el crítico externo de «Never Own a Malfoy, Potter», un fanfic de Harry Potter en inglés británico con Lyra Malfoy en lugar de Draco. Repositorio: /Users/eden/Documents/fanfic-hp-malfoy. Ignora todo archivo cuyo nombre acabe en « 2.md».
Lee primero docs/notas/reestructura/encargo-criticos-opus.md y cúmplelo, salvo dos cosas: no haces commit (otra sesión escribe a la vez en borradores/ y lo hará ella) y la vara de la voz son el 36 y el 37.

Lee en este orden, enteros, en borradores/:
- Como vara de la voz, sin criticarlos: cap-36-below-stairs, cap-37-the-north.
- Como entrada, sin criticarlos: cap-85-its-a-nice-one, cap-86-twenty-three.
- Tu tanda: cap-87-what-i-found, cap-88-clauses, cap-89-when-it-falls-due, cap-90-sit-on-you, cap-91-under-owing, cap-92-tea, cap-93-not-yet.
Los títulos llevan el número del lector (cap-93 es el «Chapter 99»); cita siempre por archivo:línea.

La tanda va del 19 de diciembre de 1996 al 15 de febrero de 1997: tras el baño, él le ha abierto el brazo y ella sigue sin poder hablar porque la Marca oye. Mira sobre todo:
- ¿Duele Greer desde fuera de Lyra (87, 91) y sin que nadie la perdone? ¿Supervivencia se confunde en algún sitio con reparación?
- Las reglas del oído: lo que se dice en voz alta, lo que va en papel y se quema, y lo que solo se puede decir. ¿Alguna escena las dobla porque le conviene? ¿Se entiende sin que se explique?
- Dumbledore (87, 93): ¿se lee como oscuro, o el texto le limpia? Harry: ¿sigue siendo gris o se ha vuelto noble? ¿Lyra se rompe delante de los demás o se vuelve demasiado adulta?
- El 91 desde Crabbe: ¿voz propia o Lyra con otro nombre? ¿Pesa su decisión?
- El 92 y el 93: ¿la Amortentia y la novena cláusula funcionan como consentimiento y no como gesto bonito? ¿La espera del 93 se sostiene o se estira? ¿El 93 paga sin beso?
- Las cuentas: veintitrés y veintidós, fechas, el sexto del bombón, los siete minutos y los once.
- Extensión: los siete pasan de 4.200 palabras (de 4.600 a 5.350). Di qué escena o párrafo cortarías en cada uno, si alguno, y qué se perdería.
- Repetición entre capítulos: arranques, finales con gesto mudo, objetos que vuelven con su historia entera, «It» en los golpes.

Escribe el informe en docs/notas/criticas-opus/tanda-87-93.md, con el formato del encargo. Al acabar, responde con el veredicto en cinco líneas y las tres correcciones que más importan.
```
