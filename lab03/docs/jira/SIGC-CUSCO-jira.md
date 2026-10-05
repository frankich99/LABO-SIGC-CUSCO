# Configuración de Jira Software: SIGC-CUSCO (Lab 03)

* **Proyecto en Jira:** `Sistema Integral de Gestión de Capacitaciones (SIGC-CUSCO)`
* **Clave del Proyecto (Key):** `SIGC`
* **Tipo de Proyecto:** Scrum / Kanban Software Development (Jira Cloud)
* **Curso:** Ingeniería de Software I — UNSAAC
* **Integrantes:**
  * Choquenaira Quispe, Noe Franklin (133962)
  * Yaranga Achahui, Aldo (103179)
  * Ccama Enriquez, Carolay (210921)
* **Docente:** Ing. Lisha Sabah Diaz Caceres

---

## 📌 Configuración de Flujo de Trabajo en Jira (Workflow)

El ciclo de vida de cada *Issue* (Historia de Usuario) en el tablero de Jira sigue el flujo:

```
[ Backlog ] ──► [ To Do ] ──► [ In Progress ] ──► [ In Review / QA ] ──► [ Done ]
```

* **Backlog:** Repositorio priorizado de Historias de Usuario (Product Backlog).
* **To Do:** Historias seleccionadas y comprometidas para el Sprint actual.
* **In Progress:** Tarea en desarrollo activo (WIP Limit: máximo 2 por desarrollador).
* **In Review / QA:** Revisión de código (Pull Request) y validación de criterios de aceptación.
* **Done:** Cumple con la *Definition of Done* (DoD) y criterios de aceptación verificados.

---

## 📋 Product Backlog en Jira (Issues / User Stories)

### 🔴 Prioridad: Highest / High (Must Have)

#### `SIGC-1` | [HU-10] Asignación de Roles y Permisos (RBAC)
* **Tipo de Issue:** Story
* **Prioridad:** Highest
* **Componente:** `Seguridad y Acceso`
* **Descripción:**
  > **Como** administrador,  
  > **quiero** asignar roles a cada usuario (administrador, docente, participante),  
  > **para** que cada uno tenga acceso únicamente a las funciones que le corresponden.
* **Criterios de Aceptación (Gherkin):**
  - **Dado** que un usuario nuevo es registrado en el sistema,  
    **cuando** el administrador le asigna un rol en el panel de control,  
    **entonces** sus permisos de navegación y acciones se actualizan inmediatamente.

---

#### `SIGC-2` | [HU-06] Creación y Configuración de Capacitaciones
* **Tipo de Issue:** Story
* **Prioridad:** Highest
* **Componente:** `Gestión Académica`
* **Descripción:**
  > **Como** administrador,  
  > **quiero** crear una capacitación nueva especificando título, fechas, horas, cupos y docente asignado,  
  > **para** aperturar la convocatoria oficial.
* **Criterios de Aceptación (Gherkin):**
  - **Dado** que el formulario contiene todos los campos obligatorios válidos,  
    **cuando** el administrador guarda el registro,  
    **entonces** el curso pasa a estado "Abierto" y se publica en el catálogo.
  - **Dado** que existen campos vacíos o datos con formato erróneo,  
    **cuando** se intenta guardar,  
    **entonces** el sistema bloquea el guardado y resalta las alertas correspondientes.

---

#### `SIGC-3` | [HU-01] Inscripción de Participantes con DNI
* **Tipo de Issue:** Story
* **Prioridad:** Highest
* **Componente:** `Inscripciones`
* **Descripción:**
  > **Como** participante,  
  > **quiero** inscribirme a una capacitación ingresando mi DNI,  
  > **para** registrarme de forma rápida sin trámites presenciales.
* **Criterios de Aceptación (Gherkin):**
  - **Dado** un DNI válido de 8 dígitos y vacantes disponibles en el curso,  
    **cuando** el participante envía su postulación,  
    **entonces** queda formalmente inscrito y se descuenta un cupo disponible.
  - **Dado** que el curso ya alcanzó el límite de vacantes,  
    **cuando** un participante intenta postular,  
    **entonces** el sistema notifica que no hay cupos y rechaza la solicitud.

---

#### `SIGC-4` | [HU-03] Control de Asistencia mediante Código QR
* **Tipo de Issue:** Story
* **Prioridad:** High
* **Componente:** `Asistencia`
* **Descripción:**
  > **Como** docente,  
  > **quiero** registrar la asistencia de los alumnos mediante un código QR dinámico por sesión,  
  > **para** agilizar el control presencial sin listas físicas en papel.
* **Criterios de Aceptación (Gherkin):**
  - **Dado** que el docente proyecta o genera el código QR de la sesión activa,  
    **cuando** el participante escanea el código desde su dispositivo,  
    **entonces** el sistema registra su asistencia con marca temporal (fecha y hora).
  - **Dado** que un participante ya registró su presencia en esa sesión,  
    **cuando** intenta escanear el código por segunda vez,  
    **entonces** el sistema indica que la asistencia ya fue computada.

---

#### `SIGC-5` | [HU-04] Registro de Evaluaciones y Cálculo de Aprobación
* **Tipo de Issue:** Story
* **Prioridad:** High
* **Componente:** `Evaluaciones`
* **Descripción:**
  > **Como** docente,  
  > **quiero** registrar las calificaciones finales de los participantes,  
  > **para** que el sistema calcule automáticamente la condición de aprobado o desaprobado.
* **Criterios de Aceptación (Gherkin):**
  - **Dado** que el docente ingresa notas en la escala vigesimal (0 a 20),  
    **cuando** cierra el acta de notas,  
    **entonces** aquellos con nota $\ge 11$ son clasificados como "Aprobado".

---

#### `SIGC-6` | [HU-05] Generación y Descarga de Certificados Digitales en PDF
* **Tipo de Issue:** Story
* **Prioridad:** High
* **Componente:** `Certificación`
* **Descripción:**
  > **Como** participante,  
  > **quiero** descargar mi certificado oficial en PDF con código QR y firma digital,  
  > **para** acreditar mi capacitación ante entidades laborales.
* **Criterios de Aceptación (Gherkin):**
  - **Dado** que el participante cuenta con condición "Aprobado",  
    **cuando** solicita su certificado en la plataforma,  
    **entonces** se genera un documento PDF con sus nombres, horas académicas y QR de validación.
  - **Dado** que el participante figura como desaprobado o no completó asistencias mínimas,  
    **cuando** intenta acceder al certificado,  
    **entonces** el sistema le informa que no cumple con los requisitos normativos.

---

### 🟡 Prioridad: Medium (Should Have)

#### `SIGC-7` | [HU-07] Gestión Multientidad (Municipalidades y Turismo)
* **Tipo de Issue:** Story
* **Prioridad:** Medium
* **Componente:** `Institucional`
* **Descripción:**
  > **Como** administrador,  
  > **quiero** dar de alta distintas instituciones (municipalidades distritales y empresas del sector turismo),  
  > **para** que cada entidad administre sus eventos y padrones con aislamiento e independencia.

#### `SIGC-8` | [HU-08] Portal Web de Verificación Pública de Certificados
* **Tipo de Issue:** Story
* **Prioridad:** Medium
* **Componente:** `Certificación y Auditoría`
* **Descripción:**
  > **Como** ciudadano o empleador,  
  > **quiero** escanear el código QR del certificado o ingresar su código único en el portal público,  
  > **para** corroborar de forma inmediata que el documento no ha sido adulterado.

#### `SIGC-9` | [HU-09] Dashboard Gerencial y Reportes para Auditoría
* **Tipo de Issue:** Story
* **Prioridad:** Medium
* **Componente:** `Reportes`
* **Descripción:**
  > **Como** gerente municipal,  
  > **quiero** exportar reportes de asistencia, inscritos y calificaciones en formato Excel/PDF,  
  > **para** sustentar las horas formativas ante órganos de control y auditorías (OSCE/OCI).

#### `SIGC-10` | [HU-02] Notificación de Confirmación de Inscripción por Correo
* **Tipo de Issue:** Story
* **Prioridad:** Medium
* **Componente:** `Notificaciones`
* **Descripción:**
  > **Como** participante,  
  > **quiero** recibir un mensaje automático de confirmación por correo electrónico al inscribirme,  
  > **para** tener el comprobante de mi registro con la información del aula y horarios.

---

### 🟢 Prioridad: Low (Could Have)

#### `SIGC-11` | [HU-12] Catálogo Público de Capacitaciones Disponibles
* **Tipo de Issue:** Story
* **Prioridad:** Low
* **Componente:** `Portal Web`
* **Descripción:**
  > **Como** participante o ciudadano,  
  > **quiero** navegar por una cartelera pública con los cursos activos y sus temarios,  
  > **para** elegir el programa de mi interés antes de iniciar sesión.

#### `SIGC-12` | [HU-11] Marcado de Asistencia en Modo Offline-First
* **Tipo de Issue:** Story
* **Prioridad:** Low
* **Componente:** `Asistencia`
* **Descripción:**
  > **Como** docente,  
  > **quiero** registrar la asistencia en auditorios sin señal de internet,  
  > **para** que los datos se almacenen en caché local y se sincronicen cuando vuelva la red.
