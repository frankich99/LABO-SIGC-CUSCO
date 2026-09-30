# Estructura del Tablero Kanban: SIGC-CUSCO

* **Nombre del Tablero:** `SIGC-CUSCO`
* **Repositorio GitHub:** `https://github.com/frankich99/SIGC-CUSCO`
* **Metodología:** Agile Inception & Lean Thinking
* **Equipo:**
  * Choquenaira Quispe, Noe Franklin (133962)
  * Yaranga Achahui, Aldo (103179)
  * Ccama Enriquez, Carolay (210921)
* **Docente:** Ing. Lisha Sabah Diaz Caceres
* **Curso:** Ingeniería de Software I — UNSAAC

---

## 1. Listas del Tablero (Flujo Kanban)

### 📋 Columna 1: `01. Product Backlog`
* `[SIGC-EP01]` Módulo de Usuarios y Autenticación con Roles (RBAC).
* `[SIGC-EP02]` Módulo de Gestión Multientidad (Municipalidades y Turismo).
* `[SIGC-EP03]` Convocatoria, Catálogo de Cursos e Inscripción con DNI.
* `[SIGC-EP04]` Control de Asistencia Digital en Tiempo Real (Marcado QR / Offline-First).
* `[SIGC-EP05]` Registro Académico de Evaluaciones y Cierre de Actas.
* `[SIGC-EP06]` Motor de Generación Masiva de Certificados PDF con Firma y QR.
* `[SIGC-EP07]` Portal Público de Consulta y Verificación Documental (Hash SHA-256).
* `[SIGC-EP08]` Dashboard Gerencial y Reportes de Impacto para Auditoría (OSCE).

---

### 📝 Columna 2: `02. Sprint Inception (To Do) — WIP Limit: 5`
* `[INCEP-01]` Redacción del Documento de Visión (Plantilla Geoffrey Moore).
* `[INCEP-02]` Mapeo y Caracterización de Stakeholders (Municipalidad y Turismo).
* `[INCEP-03]` Diseño y Validación del Lean Canvas de 9 bloques en formato horizontal.
* `[INCEP-04]` Formulación de la Matriz de Riesgos Iniciales y Planes de Mitigación.
* `[INCEP-05]` Respuestas a las Preguntas de Reflexión sobre Control de Versiones con Git.
* `[INCEP-06]` Benchmarking de Mercado (SIGC-CUSCO vs Moodle vs Google Suite vs LMS Corporativos).

---

### ⏳ Columna 3: `03. In Progress — WIP Limit: 2`
* Tareas de análisis y diseño en desarrollo activo por los miembros del equipo.
* Una tarjeta terminada que espera cupo en Review permanece aquí y sigue contando en el límite.

---

### 🔍 Columna 4: `04. Review / QA — WIP Limit: 1`
* Revisión de formato APA 7ma edición en LaTeX.
* Verificación de compilación limpia con `pdflatex` (sin errores ni advertencias).
* Revisión por pares mediante Pull Request en GitHub (el revisor nunca es el autor).

---

### ✅ Columna 5: `05. Done (Entregables Validados) — Sin límite`
* `[LISTO]` Carátula Oficial UNSAAC con datos del equipo y docente.
* `[LISTO]` Documento de Visión y Alcance formalizado.
* `[LISTO]` Matriz de Stakeholders y Matriz Poder vs Interés.
* `[LISTO]` Lean Canvas de 9 bloques horizontal en una sola página.
* `[LISTO]` Matriz de Riesgos y mitigación técnica (Offline-First y QR).
* `[LISTO]` Tablero Trello sincronizado con GitHub.
* `[LISTO]` Preguntas de reflexión sobre Git.
* `[LISTO]` Estudio de mercado y soluciones similares.
* `[LISTO]` PDF consolidado compilado exitosamente (`main.pdf`).

---

## 2. Etiquetas por Color (Labels)
* 🟢 **Verde:** `Módulo de Certificados y QR`
* 🔵 **Azul:** `Capacitaciones e Inscripciones`
* 🟠 **Naranja:** `Asistencia y Evaluaciones`
* 🔴 **Rojo:** `Seguridad y Gestión de Riesgos`
* 🟣 **Púrpura:** `Documentación y Agile Inception`
* 🟡 **Amarillo:** `Administración e Infraestructura`
* ⚫ **Negro:** `BLOQUEADA` (se agrega solo mientras la tarjeta esté bloqueada)

---

## 3. Políticas de Flujo: WIP y Bloqueo

### 3.1 Límites WIP

| Columna | Límite | Justificación |
|---|---|---|
| Product Backlog | Sin límite | Lista priorizada por el Product Owner; no es trabajo en curso. |
| To Do | 5 | Reserva de trabajo listo equivalente a un ciclo; más tarjetas envejecen sin ejecutarse. |
| In Progress | 2 | Equipo de 3 integrantes: siempre queda una persona libre para revisar, facilitar o apoyar. |
| Review / QA | 1 | Un solo revisor activo; obliga a terminar la revisión antes de aceptar más trabajo. |
| Done | Sin límite | Solo ingresan tarjetas que cumplen la Definition of Done. |

**Regla ante saturación (Review llena):** no se inicia trabajo nuevo (por ejemplo, el módulo de recordatorios). Quien tenga capacidad libre ayuda a terminar la revisión pendiente mediante *swarming* (prueba y corrección en pareja). Principio: *"Stop starting, start finishing"*.

### 3.2 Política de tarjeta bloqueada

1. **Marcar de inmediato:** quien detecta el bloqueo agrega la etiqueta `BLOQUEADA` y escribe en la tarjeta la causa, la dependencia externa, quién puede destrabarla y la fecha y hora.
2. **Sigue contando en el WIP:** la tarjeta permanece en su columna y ocupa su cupo, para que el costo del bloqueo se mantenga visible.
3. **Tratar en el siguiente Daily Standup:** la facilitadora la pone primera en la agenda (primeros 5 minutos) y se acuerda una acción con responsable.
4. **Escalar a las 24 horas:** si sigue bloqueada, se escala al docente o al responsable de la dependencia y se activa un plan alterno (por ejemplo, validar el DNI por formato y unicidad mientras no llegue el token de RENIEC).
5. **Nadie queda ocioso:** la persona asignada apoya por *swarming* a otra tarjeta; no inicia elementos nuevos.
6. **Cierre:** al resolverse se retira la etiqueta y se anota cuánto duró el bloqueo, para revisarlo en la retrospectiva.

---

## 4. Objetivo de Ciclo y Responsabilidades

**Objetivo del Sprint 3:** que un participante en Cusco pueda inscribirse en línea a un curso municipal o turístico validando su DNI, y obtenga en pantalla su credencial digital con código QR para el control de asistencia.

| Pregunta | Rol | Responsable | Responsabilidades concretas |
|---|---|---|---|
| Prioriza | Product Owner | Yaranga Achahui, Aldo (103179) | Ordena el backlog, define los criterios de aceptación y decide si una tarjeta pasa a Done tras la demostración. |
| Facilita | Scrum Master / Facilitadora | Ccama Enriquez, Carolay (210921) | Vigila los límites WIP, dirige el Daily Standup, gestiona los bloqueos y remueve impedimentos. |
| Construye | Tech Lead / Desarrollo | Choquenaira Quispe, Noe Franklin (133962) | Diseña la arquitectura y el esquema de datos, construye los servicios y responde por la calidad técnica. |

En un equipo de tres personas todos construyen y revisan; el rol define quién decide y quién responde. Regla: **autor ≠ revisor**.

---

## 5. Definition of Done (Calidad)

Una tarjeta pasa a `05. Done` solo si cumple las dos evidencias:

1. **Demostración funcional en vivo:** se ingresa un DNI en el navegador, el sistema valida que haya vacantes, guarda la inscripción y muestra el código QR. La valida el Product Owner.
2. **Calidad del software:** Pull Request en GitHub aprobado por los dos integrantes que no son autores, con 0 advertencias del linter y el script SQL ejecutado sin errores de integridad. La facilitadora registra el enlace del PR en la tarjeta.
