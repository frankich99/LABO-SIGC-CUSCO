# Acuerdos de Trabajo del Equipo SIGC-CUSCO

Documento vivo del equipo. Se revisa al cierre de cada ciclo.

## 1. Equipo y roles

| Pregunta | Rol | Integrante |
|---|---|---|
| Prioriza | Product Owner | Yaranga Achahui, Aldo (103179) |
| Facilita | Scrum Master / Facilitadora | Ccama Enriquez, Carolay (210921) |
| Construye | Tech Lead / Desarrollo | Choquenaira Quispe, Noe Franklin (133962) |

En un equipo de tres personas todos construyen y revisan; el rol define quién decide y quién responde.

## 2. Ritmo del equipo

- **Daily Standup:** 15 minutos como máximo, presencial o virtual. Cada integrante responde: qué terminé, qué haré y qué me bloquea. Los primeros 5 minutos se dedican a las tarjetas bloqueadas.
- **Planificación del ciclo:** se define el objetivo del ciclo y se eligen las historias que lo cumplen, con estimación en puntos.
- **Demostración y retrospectiva:** al cierre del ciclo se muestra la función utilizable y se revisan las métricas de flujo (tiempo de ciclo, tiempo bloqueado, saturación de Review).

## 3. Tablero y límites WIP

| Columna | Límite |
|---|---|
| Backlog | Sin límite |
| To Do | 5 |
| In Progress | 2 |
| Review / QA | 1 |
| Done | Sin límite |

- Con Review llena no se inicia trabajo nuevo: se ayuda a terminar la revisión (*swarming*).
- Una tarjeta terminada que espera cupo en Review se queda en In Progress y sigue contando.

## 4. Tarjetas bloqueadas

1. Etiqueta `BLOQUEADA` de inmediato, con causa, dependencia y responsable de destrabarla.
2. Sigue en su columna y cuenta en el WIP.
3. Se trata en los primeros 5 minutos del siguiente Daily.
4. A las 24 horas sin resolver: se escala al docente o al responsable de la dependencia y se activa el plan alterno.
5. La persona asignada apoya otra tarjeta; no inicia trabajo nuevo.
6. Al resolverse, se retira la etiqueta y se anota la duración.

## 5. Flujo de trabajo con Git

- Cada integrante trabaja en su **propia rama** (por ejemplo `rama-aldobaz`, `ramaFRANKI`).
- La rama `main` solo recibe trabajo revisado, mediante **Pull Request**.
- **Commits:** un mensaje claro por cambio, con prefijo `docs:`, `feat:`, `fix:` o `test:`.
- **Pull Request:** se abre con la plantilla de `.github/pull_request_template.md`.
- **Revisión:** la aprueban los dos integrantes que no son autores (autor ≠ revisor).
- Antes de empezar a trabajar en el día: `git pull` de tu rama, para no partir de una versión vieja.

## 6. Definition of Ready y Definition of Done

**Ready (para entrar a To Do):** criterios de aceptación escritos, requisito vinculado, estimación en puntos y dependencias externas identificadas.

**Done (para entrar a Done):**

1. Demostración funcional validada por el Product Owner.
2. Pull Request aprobado por los dos integrantes que no son autores, con el linter sin advertencias y el SQL sin errores.
3. Enlace del Pull Request registrado en la tarjeta.

## 7. Plantillas

- Pull Request: `.github/pull_request_template.md`
- Tarjetas de Trello: `docs/trello/plantillas-tarjetas.md`
