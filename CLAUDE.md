# Never Owe a Malfoy, Potter

Adaptación al inglés de una fanfic coreana de Harry Potter con un genderbend de Draco: Lyra Malfoy. Se publica en Wattpad y Webnovel. (Título de trabajo anterior: *Harry Potter and His Malfoy Problem*.) El autor es Edén. Habla con él en español; los capítulos se escriben en inglés británico.

**Antes de trabajar en la historia, lee `docs/handoff-v2.0.md`.** Es el documento vigente: motor, reglas de escritura, personajes, continuidad, plan y flujo. Los handoffs anteriores (v1.1 a v1.7) están superados. Si este archivo y el handoff se contradicen en algo de la historia, manda el handoff; en cómo se trabaja en este repositorio, manda este archivo.

## Mapa

| Ruta | Qué es | ¿Se edita? |
|---|---|---|
| `manuscrito/cap-NN-*.md` | Capítulos publicados (1 a 15) | **No.** Las erratas van a `docs/notas/erratas-publicado.md` |
| `borradores/` | Capítulos sin publicar (el 16, escrito y revisado; el 17 en adelante), guiones, fichas y planes | Sí |
| `docs/handoff-v2.0.md` | Motor y reglas | Sí, al cerrar cada capítulo |
| `docs/critico-v2.0.md` | Encargo y rúbrica del crítico | Sí |
| `docs/guia-ilustraciones.md` | Guía para el ilustrador | Pendiente de actualizar |
| `docs/notas/` | Notas de adaptación por capítulo | Sí |
| `coreano/` | Capítulos coreanos originales, `ko-NN.md` (ver `coreano/README.md`) | **No.** Solo consulta |
| `fuentes/` | Archivo de lo importado de claude.ai el 2026-10-08 (ver `fuentes/MANIFIESTO.md`) | **No.** Solo consulta |

## Reglas del repositorio

- **Lo publicado no se toca.** Decisión del autor (2026-10-11): ni siquiera retoques invisibles. **Excepción** (2026-10-11): el 1, el 2 y el 3 se pueden revisar, solo si enganchan más, mantienen la calidad y no chocan con lo ya leído ni con los capítulos 4 a 23 y el extra *Year One*. Hecho el mismo día: las versiones revisadas pasaron la prueba de continuidad y la crítica, y ya están en `manuscrito/`. El autor las sube a Wattpad y Webnovel con la nota «Chapter 1 revised: same story, faster start». Detalle en `docs/notas/revisiones/decisiones-1-2-3.md`. Del 4 al 15 sigue sin tocarse. Las erratas y los fallos de continuidad que se encuentren en `manuscrito/` se apuntan en `docs/notas/erratas-publicado.md`, y el autor decide si corrige y cuándo (tendría que hacerlo también en Wattpad y Webnovel).
- **Extensión:** el techo de 4.200 palabras es orientativo. Si recortar para llegar a él pierde más de lo que gana, no se recorta (decisión del autor, 2026-10-11).
- **Convenciones de prosa** (handoff §2): comillas y apóstrofos tipográficos (“ ” ’) desde el primer borrador, separador de escena `⁂`, cursivas con `*…*`, Mr/Mrs sin punto.
- **Lecturas largas** (varios capítulos, el handoff entero): encárgaselas al agente `lector` con una pregunta concreta. No cargues el manuscrito entero en la sesión principal.
- **Git:** haz commits con rutas explícitas al cerrar cada paso (capítulo escrito, crítica aplicada, handoff actualizado). Haz `push` al cerrar cada paso, sin preguntar (decisión del autor, 2026-10-11). El repositorio es privado y debe seguir siéndolo.
- **Falta por traer:** los capítulos coreanos originales, que van en `coreano/` y los chats que el autor quiera conservar. Pídelos antes de adaptar el capítulo 17.

## Flujo de un capítulo

Es el del handoff §8, con este cambio: los capítulos se escriben en `borradores/cap-NN-titulo.md`, una escena por paso, en vez de en un documento de Claude Docs. Cuando el autor publica un capítulo, el archivo pasa a `manuscrito/`.

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

**Reutilizar al crítico.** (El revisor ya no es un subagente: lo lleva el autor en otro chat. Cuando llegue un informe nuevo a `docs/notas/revisiones/`, la sesión principal lo lee, decide qué acepta y lo anota.) No se lanza uno nuevo por capítulo: se le pasa el siguiente capítulo al mismo agente, que ya conoce la historia y recuerda su crítica anterior y la nota que recibió. Se usan hasta que se les llene el contexto, sin cambiarlos por arco (decisión del autor, 2026-10-11). Solo entonces se empieza uno nuevo, con un resumen de las notas anteriores (en `docs/notas/`).
