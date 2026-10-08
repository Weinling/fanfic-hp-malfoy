# Harry Potter and His Malfoy Problem

Adaptación al inglés de una fanfic coreana de Harry Potter con un genderbend de Draco: Lyra Malfoy. Se publica en Wattpad. El autor es Edén. Habla con él en español; los capítulos se escriben en inglés británico.

**Antes de trabajar en la historia, lee `docs/handoff-v2.0.md`.** Es el documento vigente: motor, reglas de escritura, personajes, continuidad, plan y flujo. Los handoffs anteriores (v1.1 a v1.7) están superados. Si este archivo y el handoff se contradicen en algo de la historia, manda el handoff; en cómo se trabaja en este repositorio, manda este archivo.

## Mapa

| Ruta | Qué es | ¿Se edita? |
|---|---|---|
| `manuscrito/cap-NN-*.md` | Capítulos 1 a 16, versión publicada | Solo retoques invisibles (handoff §9) |
| `borradores/` | Capítulos en curso (el 17 en adelante), guiones y fichas de capítulo | Sí |
| `docs/handoff-v2.0.md` | Motor y reglas | Sí, al cerrar cada capítulo |
| `docs/critico-v2.0.md` | Encargo y rúbrica del crítico | Sí |
| `docs/guia-ilustraciones.md` | Guía para el ilustrador | Pendiente de actualizar |
| `docs/notas/` | Notas de adaptación por capítulo | Sí |
| `fuentes/` | Archivo de lo importado de claude.ai el 2026-10-08 (ver `fuentes/MANIFIESTO.md`) | **No.** Solo consulta |

## Reglas del repositorio

- **Lo publicado no se reescribe.** En `manuscrito/` solo se corrigen erratas, continuidad y canon de categoría A, sin cambiar hechos.
- **Convenciones de prosa** (handoff §2): comillas y apóstrofos tipográficos (“ ” ’) desde el primer borrador, separador de escena `⁂`, cursivas con `*…*`, Mr/Mrs sin punto.
- **Lecturas largas** (varios capítulos, el handoff entero): encárgaselas al agente `lector` con una pregunta concreta. No cargues el manuscrito entero en la sesión principal.
- **Git:** haz commits con rutas explícitas al cerrar cada paso (capítulo escrito, crítica aplicada, handoff actualizado). Haz `push` solo cuando el autor lo pida. El repositorio es privado y debe seguir siéndolo.
- **Falta por traer:** los capítulos coreanos originales (el handoff los da por adjuntos y aquí no están) y los chats que el autor quiera conservar. Pídelos antes de adaptar el capítulo 17.

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
| Lecturas de conjunto de un arco; juicio sobre planes grandes | agente `fable-revisor` | Fable (solo lee) |
