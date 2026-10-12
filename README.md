# SIGC-CUSCO: Sistema Integral de Gestión de Capacitaciones

[![Repositorio](https://img.shields.io/badge/GitHub-SIGC--CUSCO-blue.svg)](https://github.com/frankich99/SIGC-CUSCO)
[![Universidad](https://img.shields.io/badge/UNSAAC-Ingeniería_Informática_y_de_Sistemas-red.svg)](https://www.unsaac.edu.pe/)
[![Curso](https://img.shields.io/badge/Curso-Ingeniería_de_Software_I-orange.svg)](https://www.unsaac.edu.pe/)
[![Documentación Lab 03](https://img.shields.io/badge/LaTeX-Lab_03_PDF-brightgreen.svg)](lab03/docs/latex/main.pdf)
[![Documentación Lab 04](https://img.shields.io/badge/LaTeX-Lab_04_PDF-purple.svg)](lab04/Lab_04_Informe_SIGC_CUSCO.pdf)

---

## 📌 Descripción del Proyecto

**SIGC-CUSCO** es una plataforma web integral diseñada para centralizar, automatizar y auditar el ciclo completo de capacitación en instituciones públicas (como municipalidades de la región Cusco) y empresas privadas (con foco especial en el sector turismo: hoteles, agencias y restaurantes).

El sistema sustituye el uso desarticulado de hojas de cálculo de Excel, listas físicas de asistencia y diplomas manuales en Word o Canva, garantizando **trazabilidad completa desde la convocatoria e inscripción digital con DNI hasta la emisión masiva de certificados PDF respaldados con código QR y verificación pública**.

---

## 👥 Datos Académicos y Equipo de Trabajo

* **Institución:** Universidad Nacional de San Antonio Abad del Cusco (UNSAAC)
* **Facultad:** Facultad de Ingeniería Eléctrica, Electrónica, Informática y Mecánica
* **Escuela Profesional:** Ingeniería Informática y de Sistemas
* **Asignatura:** Ingeniería de Software I
* **Docente:** Ing. Lisha Sabah Diaz Caceres

### Integrantes:
* **Choquenaira Quispe, Noe Franklin** — 133962 — [GitHub: @frankich99](https://github.com/frankich99)
* **Yaranga Achahui, Aldo** — 103179
* **Ccama Enriquez, Carolay** — 210921

---

## 🚀 Contenido del Laboratorio 02 (Agile Inception)

1. **Identificación y Matriz de Stakeholders:** Caracterización de Municipalidades (OSCE/SIGA), Empresas Turísticas (Atención al cliente), Participantes, Capacitadores y Administradores TI.
2. **Definición de la Visión (Geoffrey Moore):** Declaración canónica, matriz de alcance (*Es / No Es / Hace / No Hace*) y objetivos SMART.
3. **Lean Canvas Refinado (9 Bloques):** Modelado ágil de negocio en orientación horizontal ajustado a una sola página (`docs/latex/secciones/04_lean_canvas.tex`).
4. **Matriz de Riesgos Iniciales:** Mitigación técnica para brecha digital, conectividad *Offline-First* y autenticidad documental (hash SHA-256 + QR público).
5. **Arquitectura y Flujo del Sistema:** 8 módulos funcionales, diccionario de datos y flujo operativo.
6. **Gestión Ágil con Jira Software:** Configuración del proyecto de desarrollo con políticas de flujo (Backlog, To Do, In Progress, QA, Done).
7. **Reflexión sobre Control de Versiones con Git:** Sustento de desarrollo colaborativo concurrente, trazabilidad y prevención de fallos.
8. **Trabajo Extra (Benchmarking de Mercado):** Comparativa frente a Moodle, Google Workspace, LMS corporativos (Crehana/Platzi) y portales estatales (OSCE).

---

## 📋 Contenido del Laboratorio 03 (Historias de Usuario y Product Backlog)

1. **Parte 1 — Identificación de Funcionalidades:** Mapeo de 12 requerimientos funcionales aterrizados al SIGC-CUSCO (autenticación RBAC, cursos, inscripción con DNI, control de asistencia QR, evaluaciones, certificados PDF y verificación pública).
2. **Parte 2 — Historias de Usuario:** Redacción de historias en formato estándar (*Como [usuario], quiero [funcionalidad], para [beneficio]*) cubriendo los roles del sistema (Participante, Docente, Administrador, Gerente Municipal y Ciudadano).
3. **Parte 3 — Product Backlog Priorizado (Jira Software):** Ordenamiento ágil aplicando la técnica MoSCoW (*Must Have, Should Have, Could Have*) y estructuración en Jira (`lab03/docs/jira/SIGC-CUSCO-jira.md`).
4. **Archivo de Importación Automática para Jira:** Archivo `.csv` estructurado listo para carga masiva (`lab03/docs/jira/jira_import_sigc_cusco.csv`).
5. **Trabajo Extra — Criterios de Aceptación:** Definición de escenarios de validación bajo el formato BDD (*Dado / Cuando / Entonces*) para las historias prioritarias.

---

## 🎨 Contenido del Laboratorio 04 (Modelado del Sistema: UML y Prototipos)

1. **Parte 1 — Diagrama de Casos de Uso (UML):**
   * Modelado completo de fronteras del sistema, actores principales (*Participante*, *Docente*, *Administrador*, *Sistema Central/RENIEC*) y 11 casos de uso centrales con relaciones `<<include>>` y `<<extend>>`.
   * Formato editable nativo en **Draw.io**: [`lab04/diagramas/casos_de_uso.drawio`](lab04/diagramas/casos_de_uso.drawio).
2. **Parte 2 — Diagrama de Clases (UML):**
   * Modelo del dominio tipado con atributos, métodos de negocio, visibilidad y multiplicidades (`User`, `Course`, `Enrollment`, `AttendanceRecord`, `CertificateService`, `UserRole`, `CourseStatus`).
   * Formato editable nativo en **Draw.io**: [`lab04/diagramas/clases.drawio`](lab04/diagramas/clases.drawio).
3. **Parte 3 — Prototipos y Capturas del Sistema en Ejecución:**
   * **Login:** Prototipo interactivo y captura real del login en Laravel 13 e Inertia Vue 3 (`localhost:8000/login`).
   * **Alertas:** Centro de notificaciones con códigos de urgencia (cierre de actas, inasistencia crítica al 25% y diplomas emitidos).
   * **Reportes:** Dashboard analítico e interfaz de validación pública de diplomas con código, nota y hash SHA-256 verificado (`localhost:8000/certificates`).
4. **Trabajo Extra — Experiencia de Usuario (UX) y Validación con Usuarios:**
   * Aplicación de heurísticas de usabilidad de Jakob Nielsen en el software real.
   * Evidencias de interfaces reales: Dashboard autenticado, portal de convocatorias y ficha de curso con control de vacantes en tiempo real.
   * Protocolo de evaluación con usuarios representativos y consolidación en la escala **SUS (System Usability Scale: 86.5/100 - Grado A)**.
5. **Informe Técnico Final en LaTeX:**
   * Código fuente modular en [`lab04/latex/`](lab04/latex/).
   * Documento compilado con formato sobrio oficial de la UNSAAC: [`lab04/Lab_04_Informe_SIGC_CUSCO.pdf`](lab04/Lab_04_Informe_SIGC_CUSCO.pdf).

---

## 📂 Estructura General del Repositorio

```text
LABO-SIGC-CUSCO/
├── README.md                          # Presentación oficial del repositorio y los laboratorios
│
├── lab04/                             # Laboratorio 04: Modelado UML y Prototipos
│   ├── Lab_04_Informe_SIGC_CUSCO.pdf  # Informe técnico oficial compilado (PDF)
│   ├── diagramas/                     # Modelos nativos editables en Draw.io y PlantUML
│   │   ├── casos_de_uso.drawio        # Diagrama de Casos de Uso editable
│   │   ├── clases.drawio              # Diagrama de Clases editable
│   │   ├── casos_de_uso.puml          # Código fuente PlantUML
│   │   └── clases.puml                # Código fuente PlantUML
│   └── latex/                         # Código fuente modular en LaTeX
│       ├── main.tex                   # Documento principal LaTeX
│       ├── config/packages.tex        # Configuración formal institucional
│       ├── secciones/                 # Portada, Casos de Uso, Clases, Prototipos, UX
│       └── imagenes/                  # Capturas reales del sistema en localhost y diagramas
│
├── lab03/                             # Laboratorio 03: Elicitación de Requerimientos
│   ├── Lab 3 ING. DE SOFTWARE.pdf     # Guía oficial del laboratorio
│   ├── jira_import_sigc_cusco.csv     # Plantilla CSV para importación masiva en Jira
│   └── docs/
│       ├── latex/                     # Informe técnico modular en LaTeX
│       │   ├── main.tex               # Documento principal
│       │   ├── main.pdf               # Documento PDF compilado
│       │   └── secciones/             # Secciones del Lab 03
│       └── jira/                      # Backlog e historias en Jira
│
└── docs/                              # Documentación del Laboratorio 02 (Agile Inception)
    ├── latex/                         # Fuente LaTeX del Lab 02
    └── v2/                            # Especificación técnica v2
```

---

## 🛠️ Compilación de Documentos LaTeX

Para compilar el informe técnico del **Laboratorio 04**:

```bash
# Navegar al directorio de LaTeX del Lab 04
cd lab04/latex

# Compilar con pdflatex (dos pasadas para actualizar tabla de contenidos y referencias cruzadas)
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

---

## 🔄 Flujo Operativo del Sistema (SIGC-CUSCO)

```text
[INSTITUCIÓN (Municipalidad / DIRCETUR / Empresa)]
   │
   ▼
[Creación del Curso y Asignación Docente (Capacidad, Horas, Fechas)]
   │
   ▼
[Inscripción Digital con Validación de Identidad por DNI]
   │
   ▼
[Control de Asistencia Digital con Token QR Dinámico]
   │
   ▼
[Registro de Notas y Cierre Formal de Acta Académica]
   │
   ▼
[Emisión Masiva de Certificados Digitales con Hash Criptográfico SHA-256]
   │
   ▼
[Verificación Pública con QR/Código + Analítica de Reportes]
```
