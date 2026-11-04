# Encargo del crítico externo (Codex)

> **Nota (4 de noviembre de 2026):** tras la limpieza, lo que aquí se cita de `docs/fable/`, `docs/notas/ideas/`, `docs/handoff-v3.0.md`, `ARRANQUE.md` y los resúmenes está en `docs/archivo/` o en `referencia/resumenes/`. Este documento es histórico; manda `CLAUDE.md`.

*3 de noviembre de 2026. El autor trabaja con límites estrictos y sin Fable: la crítica de los capítulos la hace Codex, fuera de esta sesión. Sustituye al crítico Opus del ARRANQUE §5. Claude le pasa al autor el prompt de abajo con los huecos rellenos.*

## Cómo trabaja

- **Acceso:** por git, como en la revisión del 1 de noviembre, que funcionó así. Hace `git pull` de `main` en su copia y no escribe en esa rama.
- **Qué lee para cada capítulo:** `docs/critico-v2.0.md`, el capítulo y los **cinco anteriores** en orden de lectura. Nada más.
- **La continuidad no exige leerlo todo:** busca con grep en `manuscrito/`, `borradores/cap-*`, `borradores/extra-*` y `borradores/interludio-*` cada nombre, objeto, lugar, fecha o «primera vez» que toque el capítulo, y lee solo esos pasajes. Si choca, cita las dos líneas.
- **Por tanda:** al cerrar cada tanda lee la tanda entera, una vez.
- **Lectura de toda la historia:** solo si el autor lo pide.
- **Qué no lee:** guiones, fichas, handoff, manuales, `docs/notas/reestructura/` y capítulos futuros. La crítica es a ciegas.
- **Dónde escribe:** `docs/notas/criticas-codex/cap-NN.md`, en la rama `codex/critica`. No toca capítulos.

## Prompt para pegar

```
Eres el crítico externo de «Never Own a Malfoy, Potter». Repositorio: Weinling/fanfic-hp-malfoy.
Actualiza tu copia con `git pull origin main`. Trabaja en la rama codex/critica. No edites ningún capítulo.

Critica: [CAPÍTULO, RUTA]
Lee docs/critico-v2.0.md, ese capítulo y los cinco anteriores en orden de lectura: [RUTAS].
No leas guiones, fichas, handoff, manuales ni docs/notas/reestructura/.
Para la continuidad, no leas toda la historia: busca con grep cada nombre, objeto, lugar, fecha o «primera vez» del capítulo en manuscrito/ y borradores/ (solo capítulos, extras e interludios), lee esos pasajes y cita las dos líneas si hay choque.

Además del encargo normal:
- Penaliza la falta de romance y la timidez igual que un fallo de continuidad. Señala cada sitio donde el texto sugiere lo que debería decir.
- Señala si el capítulo no tiene una escena de los dos, o si los dos no disfrutan de nada.
- Los protagonistas son menores: nada sexual.

Escribe en docs/notas/criticas-codex/[cap-NN].md, con commit y push a codex/critica.
Formato: veredicto en tres líneas; lo que funciona; los problemas por gravedad, con cita y arreglo concreto; continuidad; ranking acumulado.
```
