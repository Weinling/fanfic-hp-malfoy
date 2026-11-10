# Never Own a Malfoy, Potter

Adaptación al inglés británico de una fanfic coreana de Harry Potter con Lyra Malfoy en lugar de Draco. Se publica en Wattpad y Webnovel. (Antes *Never Owe a Malfoy, Potter*: el cambio nace en el 39 y el autor lo anuncia al publicar ese capítulo.) El autor es Edén. Habla con él en español; los capítulos van en inglés británico.

## Al empezar, tras compactar

Lee, en este orden:
1. `docs/estado-de-trabajo.md`: una página, con el siguiente paso exacto.
2. `docs/handoff-v4.0.md`: identidad, motor, reglas y flujo.
3. `docs/capitulos/continuidad-transversal.md`: hitos, quién sabe qué, cada capítulo.
4. El guion de la tanda en curso, el capítulo que toca y lo que pida su ficha.

**Antes de crear o rehacer un capítulo** (autor, 4 de noviembre): además, los manuales que toque y los tres capítulos anteriores en texto, y grep de cada nombre, objeto, lugar o «primera vez». No se escribe a ciegas, y se dice con honestidad lo que no se ha leído. La historia entera no es obligatoria.

## Mapa

| Ruta | Qué es | ¿Se edita? |
|---|---|---|
| `manuscrito/` | Capítulos 1 a 15, publicados | No |
| `borradores/` | Capítulos del 16 en adelante, extras, interludios y el guion de la tanda en curso. Nada más. **Los archivos llevan número de trabajo; el título, el del lector:** `docs/notas/reestructura/numeracion.md` | Del 43 en adelante |
| `docs/estado-de-trabajo.md` | Dónde estamos | Sí, en cada paso, y corto |
| `docs/handoff-v4.0.md` | Lo vigente | Sí |
| `docs/capitulos/` | Continuidad y un manual por capítulo | Sí, al cerrar cada capítulo |
| `docs/critico-v2.0.md` | Rúbrica y tics | Sí |
| `docs/notas/reestructura/` | Decisiones, guion general, encargos de crítica, poda | Sí |
| `docs/notas/criticas-opus/` | Críticas de la tanda en curso | Las escribe el crítico |
| `docs/notas/lo-que-sabe-harry.md` | Fondo del secreto | Sí |
| `docs/notas/erratas-publicado.md` | Erratas de lo publicado | Sí |
| `docs/guia-ilustraciones.md` | Guía para el ilustrador | Pendiente |
| `docs/archivo/` | Todo lo superado: handoffs, fichas, guiones cerrados, sesiones, críticas antiguas, cotejo. **No se lee salvo que haga falta para algo concreto; nada de ahí manda** | No |
| `coreano/`, `fuentes/`, `referencia/` | Original y resúmenes (`referencia/resumenes/`). Solo consulta | No |
| `herramientas/` | Scripts (`ngramas.py` para el cotejo con la oficial) | Sí |

## Reglas

- **Publicación (autor, 10 de noviembre de 2026):** publicado hasta el 42 inclusive. **Del 1 al 42 no se toca;** una errata se apunta en `erratas-publicado.md`. Del 43 en adelante se puede cambiar a fondo. Lo nuevo no puede contradecir lo publicado. Publicar lo hace el autor.
- **Son menores:** nada sexual ni sensual, nunca.
- **Prosa:** comillas y apóstrofos tipográficos (“ ” ’), separador `⁂`, cursivas `*…*`, Mr/Mrs sin punto. Extensión orientativa: 3.000 a 4.200 palabras; si recortar pierde más de lo que gana, no se recorta.
- **Vamos por nuestro camino (autor, 5 de noviembre).** El lector no conoce el original y no hay que debérselo. No se leen capítulos de referencia. Se rescata de él solo lo que escribiríamos peor: lista en `docs/notas/reestructura/decisiones.md`, §9. Se coge la idea, nunca la frase; los guiones no citan frases de la oficial. Al escribir no se tiene delante. Cotejo final: `herramientas/ngramas.py`.
- **Manual de Babel (autor, 5 de noviembre):** `~/Downloads/BABEL_manual-narrativo_y_handoff/sources/manual-narrativo/`, unas 300.000 palabras de técnicas. No se lee entero: se mira una técnica concreta si puede mejorar una escena, y se decide si vale la pena. Nunca es obligatorio.
- **Crítica (autor, 4 de noviembre):** cada capítulo nuevo o rehecho lo revisa un crítico Opus como subagente antes de cerrarlo, reutilizando al que ya tenga el contexto mientras le quepa. Sin Fable. Encargo en `docs/notas/reestructura/encargo-criticos-opus.md`. Los críticos son a ciegas: no leen guiones, fichas, manuales ni el rumbo. Otros subagentes grandes, preguntando.
- **Git:** commits con rutas explícitas al cerrar cada paso, y push a la rama y a `main` sin preguntar (`git push -q origin HEAD && git push -q origin HEAD:main`). Mensajes en español. El repositorio es privado y debe seguir siéndolo.
- **Cerrojo:** `date > .autonomo.lock` al trabajar (no se commitea). Si existe y tiene menos de 5 horas, para y avisa. Bórralo al terminar.
- **No acumular:** lo que quede superado va a `docs/archivo/` en el mismo paso. Un solo documento vigente por tema. El estado no es un diario.
- **Nunca hay texto que solo exista en el contexto.** Si se compacta a mitad de capítulo, el archivo y el estado bastan para seguir.
