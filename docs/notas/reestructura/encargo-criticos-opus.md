# Encargo de los críticos de la reestructura (Opus)

*4 de noviembre de 2026. Dos críticos, cada uno en su sesión y con su tanda. Este documento es común a los dos; el prompt de cada uno está al final.*

## Reglas

- **No editas ningún capítulo.** Escribes solo tu informe y haces commit de ese archivo, con ruta explícita. Otra sesión está escribiendo en `borradores/`: no toques nada más ni hagas `git add .`.
- **Sin subagentes y sin Fable.** La lectura la haces tú, una vez, en orden.
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
