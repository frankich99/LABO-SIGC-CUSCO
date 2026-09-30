# Plantillas de Tarjetas para el Tablero SIGC-CUSCO

Copia y pega estas plantillas en la descripción de la tarjeta de Trello.

---

## 1. Tarjeta de historia de usuario

**Título:** `[US-XX] Nombre corto de la historia`

```text
HISTORIA
Como <rol>, quiero <acción> para <beneficio>.

REQUISITO: RF-__ / RNF-__
PUNTOS: __
RESPONSABLE: <nombre>
RAMA DE GIT: <nombre de la rama>

CRITERIOS DE ACEPTACIÓN
- Dado <contexto>, cuando <acción>, entonces <resultado esperado>.
- Dado <contexto>, cuando <acción>, entonces <resultado esperado>.

DEFINITION OF READY (antes de pasar a To Do)
[ ] Criterios de aceptación escritos
[ ] Requisito vinculado
[ ] Estimación en puntos
[ ] Dependencias externas identificadas

DEFINITION OF DONE (antes de pasar a Done)
[ ] Evidencia 1: demostración funcional validada por el Product Owner
[ ] Evidencia 2: Pull Request aprobado por dos integrantes que no son autores
[ ] Linter sin advertencias
[ ] SQL ejecutado sin errores (si aplica)
[ ] Enlace del Pull Request: <pegar aquí>
```

---

## 2. Tarjeta bloqueada

Al bloquearse una tarjeta, agrega la etiqueta negra `BLOQUEADA` y pega este bloque al inicio de la descripción.

```text
🚫 BLOQUEADA
Desde: <fecha y hora>
Causa: <qué está impidiendo avanzar>
Dependencia externa: <persona, entidad o recurso>
Quién puede destrabarla: <nombre>
Acción acordada en el Daily: <qué se hará y quién>
Plan alterno: <qué se hará si pasan 24 horas sin resolver>
Resuelta el: <fecha y hora>   Duración: <horas>
```

Recuerda: la tarjeta bloqueada sigue en su columna y sigue contando en el límite WIP.

---

## 3. Tarjeta en revisión (Review / QA)

```text
REVISIÓN
Autor: <nombre>
Revisor asignado: <nombre distinto del autor>
Enlace del Pull Request: <pegar aquí>
Inicio de la revisión: <fecha y hora>

LISTA DEL REVISOR
[ ] Probé cada criterio de aceptación
[ ] Revisé el código o el documento
[ ] El linter no reporta advertencias
[ ] El documento LaTeX compila sin errores (si aplica)
[ ] Resultado: APROBADO / DEVUELTO con observaciones

Observaciones:
- 
```

Si la columna Review está llena, nadie inicia trabajo nuevo: se ayuda a terminar la revisión en pareja (*swarming*).
