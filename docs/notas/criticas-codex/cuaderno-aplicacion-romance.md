# Cuaderno de aplicación del romance

10 de noviembre de 2026. Punto de recuperación de esta sesión; no sustituye al cuaderno de lector de la otra tarea.

## Estado comprobado antes de escribir

- Carpeta exclusiva: `/Users/eden/.codex/worktrees/revision-romance-inedito/fanfic-hp-malfoy`.
- Rama: `codex/revision-romance-inedito`. No cambiar de rama en la carpeta principal.
- Base de Claude: `593e142c9bc9b2b12aed23032d6572bf41d4b4e3` (`origin/main`); su aplicación narrativa está en `9e8d3ad`.
- HEAD al empezar a aplicar: `3befb7609fb2aefd3e5ae9fa6249c95cbcf48e5d`. Contiene los laboratorios de 24 encuentros, todavía sin aplicar.
- Claude modificó **8 capítulos** de trabajo: 45, 46, 49, 59, 64, 70, 80 y 85. Lectores: 46, 47, 50, 63, 69, 76, 86 y 91.
- Al guardar este punto, ningún capítulo había sido modificado por Codex en esta aplicación.
- El encargo original estaba en la carpeta 8ab9, no en esta. Se recuperó y leyó desde su ruta original. La petición posterior del autor autoriza ahora completar la escritura pendiente. Sigue vigente no hacer merge ni push a main. Publicado: 1–40, intocable.

## Lectura recuperada y límites

La entrega anterior registra lectura completa del tramo 40–72 y, por separado y tras la confirmación del autor, 73–86; los capítulos anteriores y extras ya se leyeron en ese recorrido. En esta reanudación se cotejaron la base, el diff de Claude, CLAUDE.md, el estado, el handoff y la continuidad transversal. Se releyeron completos los ocho capítulos modificados por Claude y el 76 de trabajo, y los quince manuales de los capítulos previstos. El texto actual prevalece sobre sus manuales: algunos conservan frases o números de versiones antiguas.

Antes de cada parche se relee su pasaje con entrada y salida. Una muestra del laboratorio es una alternativa contra `8bd9139`, no un parche automático contra Claude. No se ha hecho una nueva lectura íntegra de todo el libro en esta reanudación. No hay revisión Opus disponible en esta sesión: no atribuirle una crítica nueva.

## Qué pide el autor

Completar la narración dentro de los besos existentes: contacto reconocible, posiciones y respuesta de ambos, nervios, vergüenza, emoción y sensaciones que puedan percibir. No convertir todos los encuentros en grandes escenas ni llenar el beso con una horquilla mientras se elide el contacto. Romance no sexual. La posesividad conserva su ambigüedad; no añadir justificaciones morales ni convertir a Harry en un personaje siempre atento o acertado.

Después de la compactación el autor exigió no modificar sin recuperar el contexto y un cuaderno. Se mantuvieron las escrituras narrativas detenidas durante el cotejo; este archivo fija el punto recuperado.

## Aplicación realizada

| Trabajo | Lector | Pasaje | Precaución |
|---|---|---|---|
| 45 | 46 | B01, Rounds | Conservar sonrisa, altura, «I could go», mano derecha oculta, placa y armadura. Completar el beso elidido. |
| 46 | 47 | B02 y B03, Trophies | Ella sigue de pie, él de rodillas: no pegar la postura antigua del laboratorio. Mandíbula breve y fraude intacto. |
| 48 | 49 | B04, Where the Sea Is | Mentira sin resolver; anillo azul y sesenta intactos. |
| 49 | 50 | B05 y B06, In Fives | Conservar la combinación aplicada por Claude: puños abiertos al moverse ella, costura, «Stay a bit», «Do it properly», latido. No adoptar sin elección los puños cerrados de B06. |
| 57 | 61 | B07, Against the Wind | POV Harry; pacto y muñeca anteriores intactos. Frío y respuesta, sin perdón nuevo. |
| 58 | 62 | B08, Scraps | Cabeza, no boca. Contacto cotidiano breve. |
| 59 | 63 | B09 y B10, In Public | Harry en butaca, ella en alfombra durante el estudio. Cinco minutos de Claude intactos. San Valentín: papel doblado al bolsillo de atrás; no al fender de la muestra antigua. |
| 62 | 67 | B14, The List | Alegría, hoja en bolsillo y «Mine» posterior intactos. No absolver lo de Hopkins. |
| 65 | 70 | B16, The Knight | Alegría de Lyra y fractura de Harry simultáneas. No arreglar la crisis del niño. |
| 66 | 72 | B18, Continuous | Breve rutina anterior al «Mine» de control; no añadir beso a la pelea. |
| 68 | 74 | B19, Ask Me | POV Harry; elección ya escrita, besos como sellos y alegría. No nueva promesa. |
| 69 | 75 | B20, You Were Missed | Narrador «Harry»; ella mantiene ojos abiertos y la mentira sobre Draco. |
| 70 | 76 | B21, Cousins | Conservar completo el diálogo de la tarta de Claude. Solo contacto sobre el plato. |
| 76 | 82 | B23, Where the House Was | Separado del tramo anterior. «No» a la muñeca, brazo izquierdo oculto, calcetín en bolsillo y réplica ritual fallida intactos. |
| 85 | 91 | B24, It’s a Nice One | Separado del tramo anterior. Beso pequeño y silencioso; manos de él en bolsillos. Pub y muerte de Greer intactos. |

Son **18 encuentros en 15 capítulos modificados por Codex**. Comprobado por diff contra `593e142`: los ocho de Claude y los quince de Codex comparten seis, por lo que el conjunto comprende **17 capítulos distintos**. Lectores modificados por Codex: **46, 47, 49, 50, 61, 62, 63, 67, 70, 72, 74, 75, 76, 82 y 91**. A estos se añaden el 69 y el 86, intervenidos solo por Claude.

## No aplicar

- B11 (60), B12 (61), B13 (primer beso del 62), B15 (64), B17 (escalera del 65): cinco reservas; el autor no ha decidido retirarlas. No borrar ni desarrollar ahora.
- B22 (71): beso en la frente tras inmovilizarla; ya cumple su función de control. No añadir recompensa romántica.
- No tocar 40 ni anteriores, ni reescribir el resto de escenas por estilo.
- Mantener las intervenciones de Claude en 64 y 80 aunque Codex no añada prosa allí.

## Avance

- [x] Reconstruir y registrar contexto antes de modificar capítulos.
- [x] Aplicar 45–49 y comprobar contra Claude.
- [x] Aplicar 57–70, conservando cinco reservas.
- [x] Aplicar por separado 76 y 85.
- [x] Leer en frío los cambios, comprobar posiciones, secretos, puntos, tics y crecimiento.
- [x] Registrar recuento real y preparar entrega con rutas explícitas. El commit de aplicación y su rama se comprueban en el historial de git; el cerrojo propio se retira al terminar.

Al entregar, distinguir aplicación narrativa local de fusión/publicación. No afirmar que los capítulos están en main ni que recibieron una nueva crítica externa.

## Comprobación de la aplicación

Se revisaron los pasajes aplicados con su contexto y el diff completo. Los retoques finales corrigieron la continuidad de las manos en *Ask Me*, hicieron perceptible el latido contra la mejilla en *In Fives* y quitaron una torpeza añadida de San Valentín para no repetir en todos los encuentros el beso que empieza mal. En *Cousins* se deja la pluma junto al papel antes de inclinarse; no se adopta el tenedor de la muestra antigua.

Comparación literal contra la base: cinco reservas conservadas; capítulos 40, 60, 61, 64, 71 y 80 sin cambios en esta aplicación; primer beso del 62 y escalera del 65 intactos; cinco minutos y coda del papel del 59 intactos; diálogo completo del examen del 70 intacto; negativa de la colina y su salida intactas; pub y todo el domingo del 85 intactos. Ningún otro capítulo aparece en el diff de Codex. Las cuentas y secretos se cotejaron en la lectura: no se añadieron visitas, declaraciones ni información compartida.

`git diff --check` pasó. Las comillas de los capítulos están equilibradas y las líneas añadidas no introducen comillas rectas ni apóstrofos rectos dentro de palabras. Cotejo mecánico con `herramientas/ngramas.py` contra 92 archivos de referencia, sin usarlos para escribir: dos coincidencias nuevas de cinco palabras, ambas giros corrientes («before he could say anything» y «when she opened her eyes»). No justifican cambiar expresiones naturales.

La ampliación neta es de unas **1.560 palabras** distribuidas entre quince capítulos. *In Public* crece más (+307, hasta unas 4.530 contando título): se conserva el espacio de Ron, de los Patronus y de los cinco minutos. No se recorta la vida del grupo para cumplir una cifra. Los otros tres desarrollos grandes crecen aproximadamente +124 (*Rounds*), +238 (*In Fives*) y +192 (*Against the Wind*). Los dos posteriores al 73 añaden +52 y +28 palabras: no se convierten en nuevas reconciliaciones.

La revisión de esta aplicación es propia, sin puntuaciones ni nueva crítica Opus. Las alternativas de los laboratorios siguen siendo documentos de comparación contra su base antigua; para conocer lo aplicado, leer los capítulos de esta rama y este cuaderno. El estado compartido y el cuaderno de lector de la otra tarea no se han modificado. Claude puede reflejar los hechos de la versión adoptada en manuales cuando el autor la integre.

## Entrega y subida

La aplicación narrativa está guardada en el commit **`da87893`**, en `codex/revision-romance-inedito`. El árbol quedó limpio tras ese commit. La revisión automática de aprobación rechazó `git push -q origin HEAD`: indicó que no veía autorización para enviar el contenido privado al remoto y que la subida chocaba con la prohibición previa de publicar/subir. Se comprobó después, sin escribir, que `origin` es `https://github.com/Weinling/fanfic-hp-malfoy.git`. Se solicitó autorización explícita para subir solo esta rama. **No se ha reintentado; no afirmar que está subida.** Main no se ha modificado ni se ha fusionado la entrega. El siguiente paso, si el autor autoriza, es subir únicamente la rama y verificar el resultado.
