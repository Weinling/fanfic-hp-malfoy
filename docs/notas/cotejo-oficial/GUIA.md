# Guía del cotejo con la traducción oficial

**Para retomar el trabajo tras compactar o en una sesión nueva.** Recoge las reglas del autor, el método y lo que falta. Fecha: 15 de octubre de 2026.

## 1. Qué se busca (autor, 15 de octubre)

- El original coreano tiene traducción inglesa oficial. El fic no debe parafrasearla tan de cerca: se cambian frases, imágenes, chistes y orden de los argumentos que la calcan.
- **Los hechos no cambian.** Los lectores ya han leído hasta el 21 (Wattpad) o el 23 más *Year One* 1 y 2 (Webnovel).
- **Pantallazos y frases de trama:** solo un poco, para que quien ya lo leyó no note otra historia. Ejemplo: «Weather’s bad. I’ll make it quick» pasó a «Rotten weather. I’ll be quick».
- **Mantener la personalidad, el carisma y los momentos emocionales**, y mejorar la historia cuando se pueda. Algunas frases simplemente se quitan. Hay que cuidar mucho los ganchos (el 1, sobre todo).
- **Orden:** primero lo publicado y luego lo no publicado, con más libertad.
- **Citas:** si una frase retocada se cita en otro capítulo, se cambia también allí, en el mismo paso. Lo mismo vale para su manual (`docs/capitulos/`), la continuidad transversal y el handoff.
- **Aviso a los lectores:** el autor publica una nota en la voz de Ash. Ya tiene redactada la primera.
- **Después** el autor comparará la versión editada con la anterior (cuál es mejor, cuánto cambia) y su parecido con la oficial. Para eso están la etiqueta y el script de §4.

## 2. Correspondencia oficial → nuestro capítulo

| Oficial (coreano) | Nuestro | ¿Publicado? | Oficial en el repo |
|---|---|---|---|
| 1 a 6 | 1 a 6 | sí | sí (`cap-01-prologo.md`, `ko-02` a `ko-06`) |
| — | 7 (nuestro) | sí | — |
| 7 a 10 | 8 a 11 | sí | sí (`ko-07` a `ko-10`) |
| — | 12 (nuestro) | sí | — |
| 11 | 13 | sí | **falta** |
| 12 | 14 y el final del 16 | sí | **falta** |
| — | 15 (nuestro) | sí | — |
| 13 | 16 | sí | **falta** |
| 14 | 17 | sí | **falta** (coreano en `coreano/`) |
| 15 | 18 | sí | **falta** (coreano) |
| 16 (parcial) y 17 | 19 | sí | **falta** (coreano) |
| 18 | *Year One* 1 | Webnovel | **falta** (coreano) |
| 19 | 20 | sí | **falta** (coreano) |
| 20 y la primera mitad del 21 | 21 | sí | **falta** (coreano) |
| el resto del 21 y el 22 | 22 | Webnovel | **falta** (coreano) |
| 23 | 23 | Webnovel | **falta** (coreano) |
| 24 | *Year One* 2 | Webnovel | **falta** (coreano) |
| 25, 26 | *Year One* 3, 4 | no | **falta** (coreano) |
| 27 | 24 | no | **falta** (coreano) |
| 28 y la clase de Moody del 30 | 25 | no | **falta** (coreano) |
| 29 | 26 | no | **falta** (coreano) |
| el resto del 30 | 27 | no | **falta** (coreano) |
| 31, 32, 33 | 28, 29, 30 | no | **falta** (coreano) |

Los capítulos que siguen en `borradores/` aunque estén publicados (del 16 al 23 y los *Year One*) cuentan como publicados para este trabajo. `lectura-completa.md` los marca «sin publicar» porque se escribió antes de que el autor diera el estado de publicación; manda esta tabla.

`herramientas/comparar.py` lleva esta misma tabla en `MAPA`. Al añadir una oficial, guárdala con ese nombre (`ko-NN.md`, con la cabecera de los demás) y el script la encuentra solo.

## 3. Orden de trabajo

1. **Publicados, con la oficial que vaya pasando el autor:** 13, 14, 16, 17, 18, 19, *Year One* 1, 20, 21, 22, 23 y *Year One* 2. El 16 necesita la oficial 12 y la 13.
2. **No publicados, con más libertad** (se puede reconstruir una escena, no solo retocar la superficie): *Year One* 3 y 4, y del 24 al 30.
3. **Revisar 7, 12 y 15** (nuestros) solo si un retoque de otro capítulo cambia algo que citan.
4. El 31 sigue en espera hasta terminar.

## 4. Herramientas y referencias

- **Commit 888ff27** («Capítulo 1: el manuscrito pasa a ser el texto publicado»): es el texto publicado antes de cualquier retoque, para todos los capítulos (el 1 ya con el arranque recortado que se publicó). Contra él se compara todo. La etiqueta `antes-del-cotejo` solo existe en local, porque el proxy no deja subir etiquetas; si falta, se usa el hash: `git tag antes-del-cotejo 888ff27`.
- **`python3 -I herramientas/cotejo.py OFICIAL CAPITULO [n=4]`** lista los tramos de palabras compartidos, de más largo a más corto. Normaliza Carina/Lyra a «malfoy» y «dad» a «father». Para buscar calcos claros, usa `n=6`; para pulir, `n=4` o `5`.
- **`python3 -I herramientas/comparar.py [caps…] [--base REV]`** da, por capítulo:
  - el parecido con la versión de 888ff27 (difflib, de 0 a 1);
  - las palabras cambiadas;
  - los tramos de 6 o más palabras compartidos con la oficial, antes y ahora.

  Es lo que el autor pidió para comparar. Datos al cerrar el 11: parecido entre 0,77 (el 6) y 0,94 (el 8), y tramos con la oficial de 3 a 19 por capítulo bajados a 0 o 1.

## 5. Método por capítulo

1. **Guardar la oficial** que pegue el autor en `referencia/oficial-en/ko-NN.md`, con la cabecera «Traducción inglesa oficial — coreano NN (nuestro capítulo X)» y «Pegado por el autor el AAAA-MM-DD. Solo para cotejo.». Commit.
2. **Leer las dos versiones enteras**, la oficial y la nuestra, y pasar `cotejo.py` con `n=4` y `n=6`.
3. **Hacer la lista de lo que calca:**
   - réplicas casi literales;
   - imágenes y comparaciones;
   - chistes;
   - el orden de los argumentos dentro de un diálogo;
   - el arranque y el cierre de escena.

   Hay que marcar cuáles son pantallazos o anclas (`lectura-completa.md` las tiene apuntadas por capítulo).
4. **Grep de cada ancla** en `manuscrito/`, `borradores/` (capítulos), `docs/capitulos/`, `docs/capitulos/continuidad-transversal.md` y `docs/handoff-v2.0.md` antes de cambiarla. Si se cita en un capítulo posterior, el cambio va con la cita ajustada.
5. **Aplicar los cambios con un script de Python** que haga `assert s.count(old) == 1` antes de cada sustitución. Nada de reescrituras a mano de bloques grandes en lo publicado. Convenciones del §2 del handoff: “ ” ’, ⁂, `*…*`, Mr/Mrs sin punto. Ojo a los tics del §4.
6. **Volver a pasar `cotejo.py`** y dejarlo en 0 o 1 tramo de 6 palabras. Lo que quede ha de ser canon o una fórmula neutra.
7. **Releer las escenas tocadas**: voz, ritmo, que el gancho y la emoción sigan ahí.
8. **Commit del capítulo** (rutas explícitas, «Capítulo N: retoques del cotejo con la oficial»), con sus citas en otros capítulos. Push.
9. **Notas:**
   - en `docs/notas/cotejo-oficial/`, una tabla de anclas cambiadas y lo más visible, siguiendo el modelo de `caps-02-11.md`;
   - actualizar el manual del capítulo (citas literales);
   - si toca, la continuidad transversal y el handoff;
   - el estado de trabajo.

   Commit y push.

En los **no publicados** el paso 5 puede ser una reescritura de escena, pero hay que mantener lo que ya fija la continuidad (manuales, continuidad transversal) y lo que planean el 31 en adelante.

## 6. Lectura obligatoria al retomar tras compactar

Hay que cumplir el protocolo de `CLAUDE.md`; para este trabajo, en concreto:

1. `docs/estado-de-trabajo.md`;
2. esta guía;
3. `docs/notas/cotejo-oficial/caps-02-11.md` (el modelo y las anclas ya cambiadas);
4. la entrada de `lectura-completa.md` de cada capítulo que se vaya a tocar, más sus conclusiones;
5. el handoff entero y todos los manuales, enteros, como manda `CLAUDE.md`;
6. para cada capítulo:
   - su texto entero y la oficial entera;
   - el manual de los capítulos que lo citan;
   - el coreano si está en `coreano/` y la oficial no ha llegado.

## 7. Avisos

- **Números de línea viejos:** los «(l. NN)» de los manuales del 1 al 11 apuntan al texto anterior al cotejo y ya no casan. Hay que buscar por frase, no por línea.
- **Documentos históricos:** las notas de revisión (`docs/notas/revisiones/`), las del crítico (`docs/critico-v2.0.md`, `docs/notas/critico-*`) y `borradores/cap-29-lector.md` citan frases antiguas. Se dejan como están; no se corrigen.
- **El crítico del 29** está vivo y conoce el texto antiguo. Si se le pasa el 31, hay que avisarle de que del 1 al 11 (y lo que siga) hay frases retocadas, y darle la tabla de anclas.
- `referencia/oficial-en/ko-03.md` está cortado a mitad de escena (acaba en «and said carefully,»). El 3 se cotejó con lo que hay; si el autor pasa el resto, conviene repasar el final del 3.
- **Pendiente de pedir al autor:** la oficial de los coreanos 11 al 33. Lo urgente es del 11 al 24, que cubre lo publicado.
