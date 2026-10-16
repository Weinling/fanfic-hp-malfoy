# Revisión final 2: capítulos 15 a 23 (texto fusionado frente a 888ff27)

Leídos enteros del 11 al 23, junto con los diffs completos del 16 al 23 frente a 888ff27, y repasadas con grep las citas del 24 al 30 y de *Year One* 3 y 4.

**Aviso previo.** El 16 y el 17 no tienen «como mucho una línea» cambiada. Llevan los retoques del cotejo (commits 913fa89, 0caa955, ea0918e, 408d7e5 y cc6cfaf, todos posteriores a 888ff27): unas 30 y 47 líneas, sobre todo en el diálogo de Harry y Sirius, el recuerdo de Madam Malkin y la escena de Draco. Los he revisado. No hay nada de tipo C ni D, y no rompen ninguna cita (cap. 1, *Year One* 1 y el 24 siguen cuadrando). El 15 no tiene ningún cambio.

---

## Hallazgos, de más a menos grave

### 1. Cap. 21, l. 266: la reacción de Potter va pegada a la frase equivocada (D, bucle 19→21)
> “She saw Malfoy take another step at him. *You must have so much to talk about.* And then, from the outside, she saw … Potter shutting it again so hard that his teeth met.”

- **El problema.** En el 19 (l. 205-211), los dientes, el gesto en la comisura y el «She decided it was guilt» vienen después de «So you take *Granger*», y luego «She took another step». En cambio, «You must have so much to talk about» va dirigida a Granger (l. 237), y Lyra no da ningún paso hacia Potter. El «It had not been guilt» del 21 remite justo a aquel momento. Al cambiar la cita para cuadrar el orden, se ha descolgado el gesto.
- **El orden correcto.** Según el 19, el gesto va antes de que Granger intervenga.
- **Arreglo.**
  - Borrar l. 266-270 («She saw Malfoy take another step…» hasta «Beside her, under the cloak, Harry said nothing.»).
  - Ponerlas justo después de l. 244 («Malfoy reached them and started to shout.»), con la cita de antes: «She saw Malfoy take another step at him. *So you take Granger.* And then, from the outside…» (el resto igual, hasta «…Harry said nothing.»).
  - En l. 246, cambiar «It all came out of her, everything from the last two months:» por «Then the rest came out of her, everything from the last two months:».
  - El párrafo «She held on to him with all her weight… It did not stop her seeing.» enlaza bien con «Then Granger raised her voice, and Malfoy reached for the word, and—».

### 2. Anillos: el destello rosa del 20 choca con el final del 21 (D, bucle 20↔21/22)
- **Dónde.**
  - Cap. 20, l. 95: «As it went, the ring flashed pink, once, and was red again before she could be sure of it.» Este destello lo ha añadido la fusión.
  - Cap. 21, l. 494: «“Coincidence,” Harry agreed, and put both rings in his pocket.»
  - La ficha del 22 dice además «Los anillos, en el bolsillo de Harry».
- **Por qué falla.** El anillo solo informa de quien lo lleva puesto. A partir del final del 21, el Harry futuro no lo lleva, así que darle la mano a Lyra en el patronus no puede volver rosa el anillo de Malfoy.
- **El resto del esquema sí cuadra sin el destello.**
  - En el cuarto, el anillo parpadea rojo y rosa: el Harry futuro lo lleva puesto y está bajo la capa con Lyra.
  - En la escalinata está rojo fijo: Harry ya se lo ha guardado.
  - Si Harry siguiera con el anillo puesto, la escalinata debería seguir parpadeando.
- **Arreglo mínimo (20, l. 95).** Borrar la segunda frase y la tercera, y que quede «Then, beyond the trees, a light went up, white for an instant and then, unmistakably, silver, and it ran out over the water and was gone.».
- **Alternativa, si se quiere conservar el destello.** En el 21, l. 494, «“Coincidence,” Harry agreed. He put hers in his pocket and his own back on his finger. “Come on. I’ve got a Patronus to cast.”». Pero entonces el «steady, bloody red» de la escalinata (20, l. 91) necesita explicación. No lo recomiendo.
- **Problema previo, menor.** El morado al aterrizar (20, l. 149), «*On guard*», ya estaba en lo publicado. Con los anillos en el bolsillo, solo lo explica el Potter inconsciente, que no está «on guard». Lo tapa la coartada de Zonko’s; lo dejaría.

### 3. Cap. 22, l. 355: Dumbledore no puede haber hablado ya con Snape (D)
> “We came back as fast as we could, in time to be told by Severus that the whole business was finished.”

- **El problema.** En ese momento Snape sigue con la comitiva en el bosque. Harry lo dice («Snape’s bringing him now»), Dumbledore se sorprende («Severus is?»), y en el 20 Dumbledore aparece en el vestíbulo cuando llega la comitiva. Además, Snape no volvió con Dumbledore: volvió solo y fue a la orilla. Lo publicado decía otra cosa («by the time we hurried back, the two of you had finished»).
- **Arreglo.** «“Severus and I were each called to the Ministry this evening, by letter, and the Ministry, when we arrived, had called neither of us. Peter’s work, I imagine. I came back as fast as I could, and before I have so much as reached my office, here is Peter, caught, by two third-years.” He inclined his head. “I have a high opinion of you both. Not quite that high. A Time-Turner seemed the likelier explanation.”»

### 4. Cap. 19, l. 139: Lupin se contradice con la atadura (D, frente al 14 y a la l. 135)
> “And the only other man who could swear to it would be kissed before he got to the end of the first sentence.”

- **El problema.** Sirius no puede jurarlo. En el 14 está atado («What he can’t do is point»), y el propio Lupin acaba de decir «Sirius can’t say a word» (l. 135). Dumbledore está atado igual. Es nuevo de la fusión; lo publicado hablaba del juramento.
- **Arreglo.** «And the only other men who know it can’t so much as point, and one of them would be kissed before anybody thought to ask.»

### 5. Cap. 21, l. 454: el sitio está al revés (D, error del injerto)
> “Somewhere above them Malfoy had it on…”

- **El problema.** El injerto ha trasladado el momento al dormitorio, pero ha dejado el «above» de cuando Malfoy estaba en la escalinata. Lyra está en el pasillo de las mazmorras, y el dormitorio queda más abajo: «She went on down to the girls’ dormitories, lower still» (l. 400). El 20 lo confirma: las oye «through the ceiling, in the common room».
- **Arreglo.** «Somewhere below them, behind her bed-hangings, Malfoy had it on, and was turning it this way and that, trying to make it tell her something.»

### 6. Cap. 21, l. 7-8: falta un salto de párrafo (E)
- **El problema.** «…set in a gold ring that spun on its own axis.» y «“Closer.”» van en líneas seguidas, sin línea en blanco, así que en Markdown se funden en un solo párrafo.
- **Arreglo.** Meter una línea en blanco entre las dos.

### 7. Cap. 21, l. 220: frase del injerto confusa (E)
> “At the bottom of the other one, he had not looked like somebody who had just run down four flights.”

- **El problema.** El «he» no tiene antecedente, y el Potter de la ventana no estaba «at the bottom of the other one», sino al fondo del pasillo.
- **Arreglo.** «She went down the opposite staircase. The Potter at the window, she remembered now, had not looked like somebody who had just run down four flights, and she had not stopped to wonder about it. Of course he had not: that Potter had been standing there with Granger all along, and the one who ran was this one.»

### 8. Cap. 20, l. 157: el hocico no coincide con lo que Lyra copió (D leve)
> “the snout a shade too short”

- **El problema.** En el 11 y el 12 el hocico es «a shade narrower». El nuevo «a shade» hace eco directo de aquella frase, y así el cambio de «narrower» a «short» se nota más. Lo publicado ya decía «too short», pero sin eco.
- **Arreglo.** «the snout a shade too narrow, the eyes a shade too far forward».

### 9. Cap. 22, l. 33: hora imposible (E leve, ya estaba en lo publicado)
> “not even in the ground-floor corridor three hours ago”

- **El problema.** Por el reloj, el beso fue hace una hora: Malfoy se va al toque de queda y el reloj del 22 da las 20:45 y las 21:00. Por el tiempo que ha vivido Lyra, fueron unas cuatro. Tres no cuadra con ninguno.
- **Arreglo.** «not even in the ground-floor corridor that evening».

### 10. Citas en capítulos sin publicar (D leve, no afectan a la subida)
- **25, l. 139.** Dice «*whoever drinks it need never know*», pero el 19, el 20 y el 22 dicen «Whoever drank it need never know». Cambiar a «*whoever drank it need never know*».
- **25, l. 95, y 26, l. 235.** Citan «*Especially next year, if students come from other schools.*», con coma. En el 23 (y en el 24 y en el 25, l. 173) va con punto. Cambiar a «*Especially next year. If students come from other schools.*».
- **El resto cuadra.** «Very kind. But no need», «nine o’clock», el filete de Buckbeak (28), el pañuelo y la pluma de azúcar (30), «In the company of their sweetheart» (24), «Stand aside» y el «Shut up, Malfoy» de *Year One* 4.

### 11. Cap. 23, l. 207: Harry se acerca a lo infalible (B, leve, opcional)
> “He had not been looking for it at all. He had been waiting for sixty.”

- **El problema.** Da a entender que Harry tenía la Snitch a voluntad toda la tarde. Lo publicado ya lo insinuaba («as if he had been waiting for exactly that number»), pero ahora el narrador lo afirma. La parte que humilla a Lyra («a Seeker herself, and seen none of it») está bien.
- **Arreglo, si se quiere suavizar.** «He had not been chasing it at all, only keeping it from Diggory; and at sixty there had been no more room to wait.»

### 12. Detalles opcionales, ya en lo publicado o casi invisibles
- **18, l. 97-109.** Con el silbido añadido, Derrick «went for him again» y en la línea siguiente Hooch pita a Bole. Se entiende, pero chirría un poco. Opcional: «…and went for him again; and Bole, not to be left out, went after him too.»
- **21, l. 172 (ya publicado).** Que Harry esté «honestly surprised» y «counting on nobody… except Hermione» choca con el 12, donde leyó el título del ensayo de Lyra y dijo «Good». Opcional: «“Did you?” Harry did not sound surprised so much as rueful.»
- **21, l. 72 (ya publicado).** «Lyra had worn that cloak all the way down to the lake»: en el 20 la llevó metida en la túnica. Opcional: «had carried that cloak».
- **21, l. 418.** En el 20 Malfoy le habla al anillo antes de sacarlo del cajón; aquí, después. Opcional: «and looked at the ring lying there, and spoke to it».
- **«Ten days in a drawer» (20).** Del lunes de los anillos (18) al miércoles del 19 («four days» después del sábado) van nueve días. «Ten» vale como redondeo. Si se quiere exacto: «Nine days in a drawer».

---

## Comprobaciones sin problemas
- **Mismo relato que lo publicado (criterio A).** No hay reinterpretaciones de tipo C fuera de las ya citadas.
- **Añadidos de tipo B que encajan.** El silbido de Lyra en el 18, la tentación del *Incarcerous* en el 20 y el respiro bajo la capa en el 22 (que explican por qué Pettigrew no está atado y por qué lo atan Lyra y Harry), la carta falsa del Ministerio (19, 20, 21 y 22 coherentes en lo esencial) y el nuevo arranque del 23 (la escoba llega por lechuza en el desayuno).
- **Mary Sue (criterio B).** Lyra conserva o gana torpezas y orgullo que le sale caro:
  - Derrick no le hace caso.
  - Pierde contra Diggory.
  - Buckbeak no se impresiona.
  - Grita y cae al suelo ante el lobo.
  - Se cae del hipogrifo.
  - Cierra los ojos «for mechanics».
  - Se ve salir «like a cork».
  - El Obliviate que Harry le baja de la mano.
  - El zorro que se cae.
  - Dumbledore la supera a ella, no al revés.
  - No ve la jugada de Harry en la final.

  Harry tampoco sale infalible: no entiende lo de «we», está «hazy», no sabe lo del anillo y no prevé lo de la poción. Hay una sola reserva, el punto 11.
- **Orden de la pelea (19 frente a 21).** Fuera del punto 1, coincide: gritos, cuello de la túnica, Potter mira a Granger, Granger carraspea, levanta la voz, la palabra, «Shut up, Malfoy», «Go to bed… Tomorrow I’ll tell you everything».
- **Objetos.** La capa y el mapa (las dos copias, el lavado y el olor a jabón), la cadena del giratiempo, las escobas (Cleansweep del cobertizo, la de Harry en el sauce, la de Lyra al otro lado del campo) y el lazo del pelo cuadran.
- **Snape y el Ministerio.** Encaja con el 19 (avisado desde el lunes, se fue esa tarde) y con lo que dice Lupin en el 21.
- **Horas.** Cuadran la llegada a la hora de la cena, el «ten to curfew», el «an hour or so from now» y el reloj de las 20:45 y las 21:00. Solo falla el punto 9.

---

## Veredicto por capítulo
- **15:** publicable tal cual (sin cambios).
- **16:** publicable tal cual. Lleva retoques del cotejo, sin problemas.
- **17:** publicable tal cual. Lleva retoques del cotejo, sin problemas.
- **18:** publicable tal cual (el punto 12 es opcional).
- **19:** publicable con el arreglo 4.
- **20:** publicable con los arreglos 2 y 8 (y el 12, opcional).
- **21:** publicable con los arreglos 1, 5, 6 y 7. El 1 es imprescindible: quien relea el 19 y el 21 seguidos lo notará.
- **22:** publicable con el arreglo 3 (y el 9, recomendable).
- **23:** publicable tal cual (el punto 11 es opcional).
