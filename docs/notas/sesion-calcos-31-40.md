# Sesión: reescribir los calcos de la oficial en el 33-40

*24 de octubre de 2026. Encargo del autor tras la revisión (`docs/notas/revisiones/revision-tanda-31-40.md`, §2.2 y §2.8): «reescribe las frases calcadas de la oficial en el 33-40 y sus ecos, con la tabla de cambios, y enséñamelas antes de cerrar». Si se compacta, lee esto después de «Ahora mismo» del estado.*

## Reglas del encargo

- Se cambia la frase, no el gesto ni el hecho. Ninguna línea nueva sale de la oficial (`referencia/oficial-en/`) ni de su orden de argumentos.
- Los ecos se cambian en el mismo paso: en los capítulos, en `borradores/cap-41-arranque-harry-borrador.md` y en los documentos de continuidad que citan la frase (manuales `docs/capitulos/cap-33.md` a `cap-40.md`, `continuidad-transversal.md`, handoff si la cita). Las críticas y las fichas son registro histórico: no se tocan.
- La tabla «frase vieja → nueva → dónde se cita» va en `docs/notas/cotejo-oficial/calcos-31-40.md`.
- **Enseñar al autor antes de cerrar.** Mientras no apruebe: commit y push solo a la rama, no a `main`; el estado dice «pendiente de aprobación».
- Al acabar, cotejo automático: `python3 -I docs/notas/cotejo-oficial/ngramas.py 5 "<capítulos>" "<oficial 36-55>"` y grep de las frases cortas.
- Cerrojo `.autonomo.lock` creado al empezar; borrarlo al cerrar.

## Lista de calcos (de la revisión, con línea al empezar)

| Cap. | Línea | Frase | Oficial |
|---|---|---|---|
| 33 | 99 | «He can sort himself out.» | 36 |
| 33 | 115 | «like a piece on a board» (eco en 39:225) | 36 |
| 33 | 149 | «You might as well tell us now.» | 36 |
| 33 | 239 | «surely a man can have one scar…» | 36 |
| 33 | 253 y título | «Tomorrow still comes» | 36 |
| 34 | 167 | «I accepted because I *wanted* to!» | 40 |
| 34 | 213 | «Can you keep your heart in one piece, girl?» | 40 |
| 35 | 83 | «He’s still my uncle.» | 37 |
| 35 | 231 | «It’s not a task… It’s a spectacle.» | 38 |
| 37 | 15 | «The time has come… to choose.» | 46 |
| 37 | 111-147 | «A man I owe something to» / «Not that» / «A man who lives off the Ministry’s favours… A useful enemy», y el orden del discurso de Lyra | 46 |
| 38 | 121 | «In you, I find— reason to hope.» | 49 |
| 39 | 23 | «Whatever anyone says… you are a Malfoy.» | 46 |
| 39 | 225 | «like a piece on a board» | 36 |
| 39 | 241 | «Don’t push your luck, Potter.» | 46 |
| 39 | 259-261 | «It’s the last time.» / «We’ll see.» | 46 |
| 40 | 25 y 29 | «This is where we end. The time we had was not entirely dull.» (eco en el borrador del 41:17) | 49 |
| 40 | 111 | «Huddled in corners like chickens» | 50 |
| 40 | 115 | «the heir of a house. A *great* house» / «Nobody makes himself small» | 50 |
| 40 | 131 | «It was a short romance.» | 50 |

## Estado

- [ ] Reescritura en los capítulos.
- [ ] Ecos en el borrador del 41 y en los documentos.
- [ ] Cotejo final.
- [ ] Tabla en `docs/notas/cotejo-oficial/calcos-31-40.md`.
- [ ] Enseñado al autor; aprobado; push a `main`; cerrojo borrado.
