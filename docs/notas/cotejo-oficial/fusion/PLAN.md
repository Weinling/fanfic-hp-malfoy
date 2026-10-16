# Fusión de versiones (16-17 de octubre de 2026)

**Aprobado por el autor:** «Sí a todo». Tras la fusión habrá una revisión final, y luego el autor publica.

## Contexto

Hay tres versiones de cada capítulo tocado:
- **publicada**: `888ff27`;
- **revisada**: `eee1bdc^`, que es `f1a12e7` (solo cambió frases);
- **nueva**: los beats rehechos, la rama actual antes de esta fusión (`HEAD` en `informe-beats.md`).

Tres revisores Opus las compararon a ciegas. Después aplicaron el criterio del autor: **Lyra no puede ser Mary Sue; más competente no significa mejor personaje; tiene 13 años y sus torpezas y encantos se conservan. Lo mismo vale para Harry: no debe parecer infalible**. Los informes, con las listas de fusión citadas, están en esta carpeta:
- `informe-1-caps-01-08.md`: caps. 1, 2, 3, 4, 5 y 8. Las fases 2, 2b y 3 están al final.
- `informe-2-caps-10-18-Y1.md`: caps. 10, 11, 13, 14 y 18, y *Year One* 1 y 2. Las fases 2 y 3 y el criterio Mary Sue están al final.
- `informe-3-caps-19-23.md`: caps. 19 a 23. La §7 trata el criterio Mary Sue, la §8 la fase 2, la §9 la fase 3 con las listas de fusión y la **§10 tiene el veredicto final**.
- `clave-letras.json`: qué letra (A o B) era la publicada y cuál la nueva en cada capítulo. Los informes se refieren a las versiones por letra y por «REVISADO».

## Base de cada capítulo

| Base | Capítulos |
|---|---|
| **Revisado** (restaurar con `git show f1a12e7:<ruta> > <ruta>`) | 4, 5, 8, 10, 11, 13, 18, 19, 20, 21 y 22 |
| **Nueva** (la actual) | 1, 2, 3, 14 y 23, y *Year One* 1 y 2 |

Sobre la base de cada capítulo se injerta lo que diga la lista de fusión de su informe, sacado de la otra versión o de la publicada.

## Qué se salva de la nueva aunque la base sea el revisado

Lo que no es Mary Sue, sino defectos de Lyra en acción:
- **20:** la tentación del *Incarcerous* ante Pettigrew, y que vaya a Potter.
- **22:** la escoba que se le escapa hacia Pettigrew cuando oye lo del neutralizador, y Harry la sujeta.
- **19:** «expected to be paid»; dejarlo suave, según el informe 3.
- **11:** «paid her for it in advance», adaptado.
- Las imágenes propias que señalan los informes.

## Qué se le quita a Lyra (Mary Sue)

- **4:** gana ella al boggart.
- **5:** usa el prefacio como arma y deja de llorar al tercer dedo.
- **8:** la deducción de más.
- **10:** las torpezas perdidas.
- **13:** ve las huellas y adivina al animago.
- **18:** el contraataque y el 30-0.
- **20:** el picado contra el lobo.
- **21:** «That *will* be you» y el anillo visto en la primera página.
- **22:** el «Now» del patronus (suavizar) y la confesión a Dumbledore (quitar).
- **23:** «He’ll go now» (suavizar: que lo entienda después de la captura, como una derrota).

## Arreglos fijos, además de las listas

1. **Fallos del bucle que arrastra el revisado del 21:** el orden de Granger (que coincida con el 19) y el anillo que parpadea en la escalinata. Las frases exactas están en el informe 3.
2. **Fallos que tienen todas las versiones:**
   - el anillo durante el patronus: cuando Lyra ve la luz desde la escalinata, debería estar rosa o parpadeando;
   - la frase de Lupin «the two men who could swear to it» (19);
   - el regreso de Dumbledore («the whole business finished»; 20 y 22).
3. **Citas cruzadas que hay que reajustar a la base elegida:**
   - **6:** «cold fury». Volver a «fury» si el 5 vuelve a la amenaza llorando.
   - **14:** «at the bottom of the stairs». Volver a «in that corridor» si el 8 vuelve al pasillo.
   - **20:** «Days in a drawer». Con el 18 revisado, los anillos aparecen el lunes anterior al partido: volver a «Ten days».
   - **16:** el eco de la oferta de los Black. Se queda, porque el 14 mantiene la base nueva.
   - **25:** «in February». Se queda.
   - **Erratas antiguas:**
     - el «rat of a traitor» del 11 y el 13 dice «in Hogsmeade», pero fue en el castillo;
     - el 19 dice que Lyra tendió la mano en mayo, pero en el 1 la tiende Potter. Comprobar.
4. **Publicar juntos:**
   - el 3 con el 11, el 13 y el 14 (el consejo del perro);
   - el 8 con el 11 y el 13;
   - el 9 con el 10;
   - el 14 con el 16.

## Orden de trabajo

1. Restaurar el revisado en los 11 capítulos de base revisada. Commit.
2. Por bloques, aplicar las listas de fusión de cada informe:
   - **bloque A:** 1, 2, 3, 4, 5 y 8;
   - **bloque B:** 10, 11, 13, 14 y 18, y *Year One* 1 y 2;
   - **bloque C:** 19 a 23, juntos por el bucle.

   Cada bloque se cierra con un commit.
3. Citas cruzadas y erratas (punto 3 de arriba). Commit.
4. Revisión final por un Opus nuevo: misma historia que la publicada, sin Mary Sue, bucle coherente y citas. Aplicar lo que encuentre.
5. Manuales, continuidad, handoff y `veredicto-publicado.md` (qué subir y en qué orden). Commit.
6. Avisar al autor: puede publicar.

## Lectura al retomar tras una compactación (para este encargo)

1. `docs/estado-de-trabajo.md`.
2. Este plan.
3. El informe del bloque en curso, entero.
4. Las dos versiones del capítulo en el que se trabaja (base e injertos).

El protocolo completo de `CLAUDE.md` (handoff entero y todos los manuales) se reserva para escribir capítulos nuevos. Para esta fusión no hace falta: los informes ya llevan las citas cruzadas.
