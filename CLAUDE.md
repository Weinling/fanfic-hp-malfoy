# Never Owe a Malfoy, Potter

Adaptación al inglés de una fanfic coreana de Harry Potter con un genderbend de Draco: Lyra Malfoy. Se publica en Wattpad y Webnovel. (Título de trabajo anterior: *Harry Potter and His Malfoy Problem*.) El autor es Edén. Habla con él en español; los capítulos se escriben en inglés británico.

**Antes de trabajar en la historia, lee `docs/handoff-v3.0.md`.** Es el documento vigente y corto (unas 3.200 palabras): identidad, motor, reglas de escritura, rumbo, sistema y flujo. El `docs/handoff-v2.0.md` queda de archivo (cómo se llegó aquí) y no hace falta leerlo; los anteriores (v1.1 a v1.7) están superados. Si este archivo y el handoff se contradicen en algo de la historia, manda el handoff; en cómo se trabaja en este repositorio, manda este archivo.

## Mapa

| Ruta | Qué es | ¿Se edita? |
|---|---|---|
| `manuscrito/cap-NN-*.md` | Capítulos publicados (1 a 15; el resto de lo publicado sigue en `borradores/`, ver «Publicación») | Sí, solo para el cotejo con la oficial (ver reglas) |
| `borradores/` | Capítulos sin publicar (el 16, escrito y revisado; el 17 en adelante), guiones, fichas y planes | Sí |
| `docs/handoff-v3.0.md` | Lo vigente: motor, reglas, rumbo y sistema | Sí, al cerrar cada capítulo, solo si cambia algo vigente |
| `docs/handoff-v2.0.md` | Archivo: historia del proyecto hasta el 18 de octubre | No |
| `docs/critico-v2.0.md` | Encargo y rúbrica del crítico | Sí |
| `docs/guia-ilustraciones.md` | Guía para el ilustrador | Pendiente de actualizar |
| `docs/notas/` | Notas de adaptación por capítulo | Sí |
| `coreano/` | Capítulos coreanos originales, `ko-NN.md` (ver `coreano/README.md`) | **No.** Solo consulta |
| `fuentes/` | Archivo de lo importado de claude.ai el 2026-10-08 (ver `fuentes/MANIFIESTO.md`) | **No.** Solo consulta |

## Reglas del repositorio

- **Publicación (autor, 18 de octubre de 2026):** Wattpad, del 1 al 23; hoy sube los *Year One* 1 y 2, mañana el 3 y el 4, y luego uno al día. Webnovel, del 1 al 26 y los cuatro *Year One*; hoy sube el 27 y el 28, y desde mañana uno al día. Sustituye a la entrada siguiente.
- **Publicación (autor, 17 de octubre de 2026, superada):** Wattpad, del 1 al 22; Webnovel, del 1 al 23, *Year One* del 1 al 4 y el 24. El autor actualiza el 1 al 23 y los *Year One* 1 y 2 con las versiones fusionadas (`docs/notas/cotejo-oficial/veredicto-publicado.md`).
- **Publicación (autor, 15 de octubre de 2026, superada):** en Wattpad, del 1 al 21; en Webnovel, 25 entregas (del 1 al 23 más *Year One* 1 y 2, que son las últimas subidas). Todo con el texto anterior al cotejo: el autor subirá los retoques solo tras la revisión de conjunto (`docs/notas/cotejo-oficial/GUIA.md` §8).
- **Cotejo con la traducción inglesa oficial (autor, 15 de octubre de 2026). Sustituye a la regla siguiente.** El original coreano tiene versión inglesa oficial, y el fic no debe parafrasearla tan de cerca. Se retoca también lo publicado: frases, imágenes y orden de los argumentos que calcan la oficial. Los hechos no cambian. Lo que es trama, pantallazos incluidos, se retoca solo un poco, para que quien ya lo ha leído no note que la historia ha cambiado. Si una frase retocada se cita en otro capítulo, la cita se cambia en el mismo paso. Método, orden y lectura al retomar en `docs/notas/cotejo-oficial/GUIA.md`; diagnósticos y notas en la misma carpeta; textos oficiales en `referencia/oficial-en/` (solo para comparar, nunca para copiar). Los cambios se anuncian a los lectores con una nota.
- **Lo publicado no se toca (regla anterior, superada el 15 de octubre por la de arriba).** Decisión del autor (2026-10-11): ni siquiera retoques invisibles. **Excepción** (2026-10-11): el 1, el 2 y el 3 se pueden revisar, solo si enganchan más, mantienen la calidad y no chocan con lo ya leído ni con los capítulos 4 a 23 y el extra *Year One*. Hecho el mismo día: las versiones revisadas pasaron la prueba de continuidad y la crítica, y ya están en `manuscrito/`. El autor las sube a Wattpad y Webnovel con la nota «Chapter 1 revised: same story, faster start». Detalle en `docs/notas/revisiones/decisiones-1-2-3.md`. Del 4 al 15 sigue sin tocarse. Las erratas y los fallos de continuidad que se encuentren en `manuscrito/` se apuntan en `docs/notas/erratas-publicado.md`, y el autor decide si corrige y cuándo (tendría que hacerlo también en Wattpad y Webnovel).
- **Extensión:** el techo de 4.200 palabras es orientativo. Si recortar para llegar a él pierde más de lo que gana, no se recorta (decisión del autor, 2026-10-11).
- **Convenciones de prosa** (handoff §2): comillas y apóstrofos tipográficos (“ ” ’) desde el primer borrador, separador de escena `⁂`, cursivas con `*…*`, Mr/Mrs sin punto.
- **Lecturas:** la sesión principal lee ella misma lo que pide «Lectura obligatoria» tras cada compactación, y la historia entera al empezar cada tanda. El agente `lector` queda para preguntas concretas y largas (decisión del autor, 2026-10-11).
- **Git:** haz commits con rutas explícitas al cerrar cada paso (capítulo escrito, crítica aplicada, handoff actualizado). Haz `push` al cerrar cada paso, sin preguntar (decisión del autor, 2026-10-11). El repositorio es privado y debe seguir siéndolo.
- **Falta por traer:** los capítulos coreanos originales, que van en `coreano/` y los chats que el autor quiera conservar. Pídelos antes de adaptar el capítulo 17.

## Memoria entre sesiones y compactaciones (decisión del autor, 2026-10-11)

La sesión principal no puede apoyarse solo en el resumen de una compactación ni en el coreano. Tras la compactación del capítulo 20, el crítico cazó cinco choques con capítulos publicados que una lectura completa habría evitado.

- **`docs/estado-de-trabajo.md`.** Se lee **lo primero** al abrir sesión o tras compactar. Dice:
  - en qué capítulo y escena se está;
  - qué está commiteado;
  - qué falta;
  - qué agentes están vivos;
  - qué decide el autor.

  Se actualiza en cada paso, en el mismo commit.
- **`docs/capitulos/`.** Hay un manual por capítulo, con la misma plantilla:
  - escenas y fechas;
  - frases literales que se citan;
  - fichas y libro de cuentas;
  - quién sabe qué;
  - hilos;
  - continuidad fácil de romper;
  - forma del final.

  El manual de cada capítulo nuevo se escribe al cerrarlo, en el mismo paso que el handoff.
- **Lectura obligatoria** (protocolo aligerado por el autor el 18 de octubre de 2026, porque la lectura completa ya costaba unos 370.000 tokens y crece unos 6.000 por capítulo; sustituye al del 11 de octubre):
  - **Al abrir sesión o tras compactar, a mitad de tanda** (no se salta nunca):
    - el estado de trabajo y la nota de sesión, si la hay;
    - el handoff v3.0, **entero**;
    - `docs/capitulos/continuidad-transversal.md` (hitos de la pareja, quién sabe qué y desde cuándo, estado de cada personaje, fichas y deudas), que se actualiza al cerrar cada capítulo;
    - el guion de la tanda en curso;
    - los manuales, enteros, de los capítulos ya escritos de la tanda y de los cuatro anteriores;
    - el texto completo de, como mínimo, los dos capítulos anteriores al que se va a escribir;
    - el coreano que se adapta y los dos siguientes, cuando el guion dice «se queda» o «cambia», y las fichas ya hechas.

    El resto de los manuales se lee cuando la ficha toque algo de ese capítulo: entero el manual, y el pasaje con grep.
  - **Al empezar una tanda:** la historia entera en texto completo, más el handoff, la continuidad y el rumbo. **Sin los manuales**, que repiten el texto. Cuando la historia pase de unas 200.000 palabras (hacia el capítulo 45), se lee entera la tanda anterior y del resto, los manuales.
  - Lo que se lee se apunta en el estado de trabajo.
  - **Antes de cerrar cada ficha:** la sesión principal busca ella misma en el texto (grep) cada nombre, objeto, lugar o «primera vez» que toque la ficha. El agente lector solo se usa para una pregunta concreta y larga (decisión del autor, 2026-10-11).
- **Nunca hay texto que solo exista en el contexto.** Cada escena se commitea al escribirla, y si se compacta a mitad de capítulo, el archivo y el estado de trabajo bastan para seguir.
- **El coreano es fuente de trama, no de continuidad.** La continuidad la dan el manuscrito, los borradores y los manuales.

## Flujo de un capítulo

Es el del handoff v3.0, §10, con este cambio: los capítulos se escriben en `borradores/cap-NN-titulo.md`, una escena por paso, en vez de en un documento de Claude Docs. Cuando el autor publica un capítulo, el archivo pasa a `manuscrito/`.

## Quién hace qué (propuesta, por cerrar con el autor)

Sigue la skill `metodo-equipo`. Reparto inicial:

| Tarea | Quién | Modelo |
|---|---|---|
| Leer material largo y responder una pregunta | agente `lector` | Sonnet |
| Pasadas mecánicas: comillas, `⁂`, recuento de palabras, buscar tics de la lista | subagente | Haiku |
| Ficha, guion y escritura del capítulo | sesión principal | Opus |
| Crítica de cada capítulo con `docs/critico-v2.0.md` | subagente sin acceso al original ni a capítulos futuros | Opus |
| Revisión informada por tandas de capítulos (fidelidad, continuidad, canon, motor a lo largo de varios capítulos) | **chat paralelo que maneja el autor** (prompt en `docs/prompt-revisor.md`; informes en `docs/notas/revisiones/`) | Opus |

Decisión del autor (2026-10-11): todas las revisiones y críticas las hace Opus, no Fable.

**Reutilizar al crítico.** (El revisor ya no es un subagente: lo lleva el autor en otro chat. Cuando llegue un informe nuevo a `docs/notas/revisiones/`, la sesión principal lo lee, decide qué acepta y lo anota.) No se lanza uno nuevo por capítulo: se le pasa el siguiente capítulo al mismo agente, que ya conoce la historia y recuerda su crítica anterior y la nota que recibió. Se usan hasta que se les llene el contexto, sin cambiarlos por arco (decisión del autor, 2026-10-11). Solo entonces se empieza uno nuevo, con un resumen de las notas anteriores (en `docs/notas/`). El crítico nuevo lee **enteros todos los capítulos adaptados** (no resúmenes); no lee el coreano, los planes, las fichas ni los capítulos futuros. El del cuarto año se reinicia al usarlo para el 29 (decisión del autor, 2026-10-11).
