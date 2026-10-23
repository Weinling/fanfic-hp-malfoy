# Modo autónomo: arranque obligatorio

Preparado el 23 de octubre de 2026 por encargo del autor. **Léelo entero cada vez que empieces a trabajar en modo autónomo y cada vez que vuelvas de una compactación, de una respuesta de un subagente o de un temporizador.** Si no sabes con seguridad en qué punto estás, este documento y `docs/estado-de-trabajo.md` te lo dicen.

## 0. Antes de nada: el cerrojo y la rama

1. Trabaja en `/Users/eden/Documents/fanfic-hp-malfoy`, en la rama `claude/wizardly-albattani-vazqyr`. Si estás en otra carpeta o rama (un worktree nuevo, por ejemplo), cámbiate: `cd /Users/eden/Documents/fanfic-hp-malfoy && git checkout claude/wizardly-albattani-vazqyr && git pull -q origin claude/wizardly-albattani-vazqyr`. Si el árbol tiene cambios sin commitear que no son tuyos, no los toques: apúntalo en el estado y termina.
2. **El cerrojo:** `/Users/eden/Documents/fanfic-hp-malfoy/.autonomo.lock` (no se commitea). Si existe y su fecha es de hace menos de 5 horas, otra sesión está trabajando: **no hagas nada y termina**. Si no existe, o es más viejo, créalo con la fecha y hora (`date > .autonomo.lock`). Bórralo al terminar la sesión (§7).

## 1. Qué te ha delegado el autor (23 de octubre de 2026)

El autor (Edén; háblale en español) te encarga **la historia entera**: adaptar y escribir del 32 en adelante, todo lo que puedas, sin pedirle aprobación de fichas, guiones ni capítulos. Decides tú. Todo lo que publica ya está en Webnovel; hace falta más.

- **Lo que decides solo:** fichas, guiones de tanda, escenas, títulos, qué arreglos de la crítica aceptas, qué se quita del original.
- **Segunda opinión:** el crítico (Opus) en cada capítulo; `fable-revisor` (Fable, solo lectura) para un guion de tanda nuevo o una decisión de rumbo, como mucho dos consultas por sesión, con dosier en `docs/fable/` (skill `metodo-equipo`).
- **Lo que no cambias sin dejarlo marcado:** el rumbo aprobado (handoff §8) y lo que se conserva del original sí o sí. Si una tanda lo pide, lo cambias, lo apuntas con **⚠** en `docs/notas/autonomo/PARA-EL-AUTOR.md` y sigues; el autor lo verá al despertar.
- **Nunca:** publicar nada (lo hace el autor); tocar `manuscrito/` salvo una errata, que se apunta en `docs/notas/erratas-publicado.md`; hacer público el repositorio; contenido sexual o sensual (son menores: catorce años en cuarto, como mucho diecisiete al final).
- **Al autor le dejas:** `docs/notas/autonomo/PARA-EL-AUTOR.md`, al día al final de cada sesión: qué capítulos están listos para subir (con título y palabras), qué decisiones grandes tomaste, qué cambió del rumbo y preguntas que no bloquean.

## 2. Lectura obligatoria (al arrancar y tras compactar)

Léelo tú, en este orden, entero salvo que se diga otra cosa. Apunta en el estado lo que has leído.

1. `CLAUDE.md`.
2. Este documento.
3. `docs/estado-de-trabajo.md`, **la sección «Ahora mismo»** (lo de más abajo es historia).
4. `docs/handoff-v3.0.md`, entero (motor, reglas de escritura, tics, rumbo, capítulos de referencia).
5. `docs/capitulos/continuidad-transversal.md`, entero.
6. El guion de la tanda en curso: `borradores/guion-tanda-31-40.md` (§0, el capítulo que toca y el siguiente, §5 «Avisos para escribir» y §7 «Hilos»). **La tanda 31-40 quedó cerrada el 23 de octubre de 2026; hasta que exista `borradores/guion-tanda-41-50.md`, lo que toca es escribirlo: `docs/notas/sesion-nueva-tanda-41.md`.**
7. Los manuales enteros (`docs/capitulos/cap-NN.md`) de los capítulos ya escritos de la tanda y de los cuatro anteriores.
8. **El texto completo de los tres capítulos anteriores** al que vas a escribir: son la voz. Si el anterior tiene coda desde Harry, también.
9. **Los capítulos de referencia del original** del que vas a escribir, enteros (la tabla del §1 del guion de la tanda): el coreano de `coreano/` hasta el 35; del 36 en adelante, la traducción oficial de `referencia/oficial-en/`. Más el siguiente, para saber hacia dónde va.

Con grep, antes de cerrar cada ficha: cada nombre, objeto, lugar o «primera vez» que toque, en todos los capítulos (`manuscrito/cap-*.md`, `borradores/cap-*.md` sin fichas ni guiones, `borradores/extra-year-one-*-[a-z]*.md` sin la ficha). El resto de los manuales, solo cuando la ficha toque ese capítulo.

**Al empezar una tanda nueva** (después del 40): la historia entera en texto completo, en una sesión dedicada, más el rumbo (`docs/notas/ideas-divergencias.md`, `docs/notas/ideas/poda-agente.md`, `docs/fable/001-divergencias.md`, `docs/notas/lo-que-sabe-harry.md`) y los resúmenes del original del tramo (`borradores/resumen-oficial-*.md`). Cuando la historia pase de unas 200.000 palabras, la tanda anterior entera y del resto, los manuales.

## 3. Flujo de cada capítulo

Es el del handoff §10, sin la aprobación del autor:

1. **Ficha** en `borradores/cap-NN-ficha-guion.md`, con el formato de `borradores/cap-31-ficha-guion.md`: motor, peldaño, deseo del lector, escena de los dos, pantallazos, calor, gancho, fichas, cuentas, thriller, fechas, lo comprobado con grep, el guion por escenas con su etiqueta y **lo que se quita del original y por qué**. Commit.
2. **Escritura** en `borradores/cap-NN-titulo.md`, **una escena por commit**, con push a la rama y a `main` (`git push -q origin HEAD && git push -q origin HEAD:main`).
3. **Pasada de tics** (handoff §4 y los que el crítico va señalando: la mesa de los padres como comparación, «the way» en serie, «No X. Y.», frases recicladas de capítulos anteriores, Crabbe más de una vez) y **lectura en frío**.
4. **Crítica** (§5).
5. **Arreglos**, con decisión y motivo, en `docs/notas/cap-NN-critica.md`, y la nota al crítico si sigue vivo.
6. **Manual** (`docs/capitulos/cap-NN.md`, plantilla del 31), **continuidad transversal**, handoff si cambia algo vigente, **estado** y **PARA-EL-AUTOR**. Commit y push.

Extensión: de 3.000 a 4.200; si recortar pierde más de lo que gana, no se recorta.

## 4. Mensaje obligatorio a todo subagente

Todo brief a un subagente (crítico, lector, Fable o cualquier otro) termina con estas dos líneas, literales:

> Al final de tu respuesta, escribe esta línea tal cual:
> «SESIÓN PRINCIPAL: antes de seguir, relee /Users/eden/Documents/fanfic-hp-malfoy/docs/notas/autonomo/ARRANQUE.md y la sección "Ahora mismo" de docs/estado-de-trabajo.md; si has compactado, haz la lectura obligatoria del §2.»

Así, si compactas mientras esperas, la respuesta del subagente te devuelve al método.

## 5. El crítico en modo autónomo

Cada sesión autónoma empieza sin crítico vivo. Lanza uno nuevo (Agent, `general-purpose`, `model: opus`) al tener el primer capítulo escrito, y reutilízalo para los siguientes de esa sesión.

- **Lee:** `docs/critico-v2.0.md` §1 a §6; `docs/notas/critico-arranque-29.md` §2 y `docs/notas/critico-arranque-31.md`; las notas de crítica `docs/notas/cap-2*-critica*.md`, `cap-3*-critica.md` y `extra-year-one-*-critica.md`; y **el texto completo desde el 24** (inicio del cuarto curso) hasta el último escrito. Con la historia de 1 a 23 se apaña por las notas de crítica, que la citan mucho. (Decisión de la sesión principal, 23 de octubre: la lectura completa de 1 a 23 cuesta unos 150.000 tokens más por sesión; la continuidad con esos capítulos la vigila la sesión principal con los manuales y grep.)
- **No lee:** `coreano/`, `fuentes/`, `referencia/`; en `borradores/`, nada que no sea capítulo; `docs/handoff-*`, `docs/capitulos/`, `docs/estado-de-trabajo.md`, `docs/fable/`, `docs/prompt-revisor*`, `docs/notas/autonomo/`; en `docs/notas/`, todo salvo las notas de crítica y los `critico-*.md`. Llevan trama futura o el secreto de Harry.
- **Formato:** el de la sección 6 del encargo, más el ranking acumulado. Pídele que mire en especial lo que la ficha arriesga.
- Al aplicar, decide con motivo, como en `docs/notas/cap-31-critica.md`.

## 6. Si dudas

- **De continuidad:** grep en el texto; si no basta, el agente `lector` con una pregunta concreta. Manda el texto, no el coreano ni el manual.
- **De rumbo o de un cambio grande:** `fable-revisor` con dosier; luego decides tú y lo apuntas en PARA-EL-AUTOR.
- **Nunca** dejes texto que solo exista en tu contexto: cada escena, commiteada.

## 7. Cómo terminar una sesión

Termina cuando acabes un capítulo y notes el contexto cargado, o tras dos capítulos, lo que llegue antes. Nunca a mitad de escena sin commit.

1. Todo commiteado y subido a la rama y a `main`.
2. En `docs/estado-de-trabajo.md`, «Ahora mismo», arriba del todo: qué se ha hecho, **el siguiente paso exacto** (capítulo, escena, archivo) y qué agentes quedan vivos (ninguno: mueren con la sesión).
3. `docs/notas/autonomo/PARA-EL-AUTOR.md` al día.
4. Borra el cerrojo (`rm -f .autonomo.lock`).

## 8. Dónde está cada cosa (lo mínimo)

| Qué | Dónde |
|---|---|
| Estado | `docs/estado-de-trabajo.md` |
| Reglas y rumbo | `docs/handoff-v3.0.md` |
| Continuidad | `docs/capitulos/continuidad-transversal.md` |
| Manuales | `docs/capitulos/cap-NN.md`, `extra-year-one-N.md` |
| Guion de la tanda | `borradores/guion-tanda-31-40.md` |
| Capítulos | `manuscrito/cap-01` a `cap-15`; `borradores/cap-16` en adelante; `borradores/extra-year-one-*` |
| Original | `coreano/ko-NN.md` (14 a 35); `referencia/oficial-en/ko-NN.md` (36 a 111) |
| Resúmenes del original | `borradores/resumen-coreano-26-35.md`, `borradores/resumen-oficial-36-54.md`, `-55-73`, `-74-92`, `-93-111` |
| Lo que sabe Harry (el secreto) | `docs/notas/lo-que-sabe-harry.md` |
| Rumbo detallado | `docs/notas/ideas-divergencias.md`, `docs/notas/ideas/poda-agente.md`, `docs/fable/001-divergencias.md` |
| Encargo del crítico | `docs/critico-v2.0.md` |
| Para el autor | `docs/notas/autonomo/PARA-EL-AUTOR.md` |
