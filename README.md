# SIGC-CUSCO: Sistema Integral de Gestión de Capacitaciones

[![Repositorio](https://img.shields.io/badge/GitHub-SIGC--CUSCO-blue.svg)](https://github.com/frankich99/SIGC-CUSCO)
[![Universidad](https://img.shields.io/badge/UNSAAC-Ingeniería_Informática_y_de_Sistemas-red.svg)](https://www.unsaac.edu.pe/)
[![Curso](https://img.shields.io/badge/Curso-Ingeniería_de_Software_I-orange.svg)](https://www.unsaac.edu.pe/)
[![Documentación](https://img.shields.io/badge/LaTeX-APA_7ma_Edición-brightgreen.svg)](docs/latex/main.pdf)
[![Trello](https://img.shields.io/badge/Trello-SIGC--CUSCO-0079BF.svg)](docs/trello/SIGC-CUSCO.md)

---

## 📌 Descripción del Proyecto

**SIGC-CUSCO** es una plataforma web integral diseñada para centralizar, automatizar y auditar el ciclo completo de capacitación en instituciones públicas (como municipalidades de la región Cusco) y empresas privadas (con foco especial en el sector turismo: hoteles, agencias y restaurantes).

El sistema sustituye el uso desarticulado de hojas de cálculo de Excel, listas físicas de asistencia y diplomas manuales en Word o Canva, garantizando **trazabilidad completa desde la convocatoria e inscripción digital con DNI hasta la emisión masiva de certificados PDF respaldados con código QR y verificación pública**.

---

## 👥 Datos Académicos y Equipo de Trabajo

* **Institución:** Universidad Nacional de San Antonio Abad del Cusco (UNSAAC)
* **Facultad:** Facultad de Ingeniería Eléctrica, Electrónica, Informática y Mecánica
* **Escuela Profesional:** Ingeniería Informática y de Sistemas
* **Asignatura:** Ingeniería de Software I (Semestre 2026-II)
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
6. **Gestión Ágil con Trello:** Tablero Kanban `SIGC-CUSCO` con límites WIP (To Do 5, In Progress 2, Review 1), política de bloqueo, roles (quién prioriza, facilita y construye) y Definition of Done.
7. **Reflexión sobre Control de Versiones con Git:** Sustento de desarrollo colaborativo concurrente, trazabilidad y prevención de fallos.
8. **Trabajo Extra (Benchmarking de Mercado):** Comparativa frente a Moodle, Google Workspace, LMS corporativos (Crehana/Platzi) y portales estatales (OSCE).

---

## 🚀 Documento V2 (Ejercicios de Flujo Ágil, Requerimientos y Diseño)

El documento `docs/v2/v2.pdf` (fuente en `docs/v2/v2.tex`) incluye:

1. **Ejercicio: una revisión saturada.** Justificación con la Ley de Little, acuerdo de *swarming*, límites WIP con su justificación y política de bloqueo.
2. **Ejercicio: coordinar una entrega.** Objetivo de ciclo (Sprint 3), responsabilidades del equipo y dos evidencias de calidad (Definition of Done).
3. Requerimientos (MoSCoW e ISO/IEC 25010).
4. **Plan de entrega del Sprint 3:** historias de usuario con criterios de aceptación (Dado/Cuando/Entonces), Definition of Ready y Done, Ley de Little con números, métricas de flujo y acuerdo de trabajo con Git.
5. Modelado UML, base de datos relacional con script DDL, arquitectura y plan de sprints.

---

## 📂 Estructura del Repositorio

```text
SIGC-CUSCO/
├── README.md                          # Presentación oficial del proyecto para GitHub
├── .github/
│   └── pull_request_template.md       # Plantilla de Pull Request con la Definition of Done
├── docs/                              # Documentación técnica formal
│   ├── latex/                         # Código fuente modular en LaTeX (APA 7ma Edición)
│   │   ├── main.tex                   # Archivo raíz que ensambla todas las secciones
│   │   ├── main.pdf                   # Documento PDF compilado limpio y compacto
│   │   ├── config/
│   │   │   └── packages.tex           # Configuración tipográfica, márgenes y paquetes
│   │   ├── secciones/
│   │   │   ├── 00_portada.tex         # Portada oficial institucional UNSAAC
│   │   │   ├── 01_objetivo_fundamento.tex
│   │   │   ├── 02_stakeholders.tex
│   │   │   ├── 03_vision_sistema.tex
│   │   │   ├── 04_lean_canvas.tex     # Lean Canvas de 9 bloques horizontal (1 página)
│   │   │   ├── 05_gestion_riesgos.tex
│   │   │   ├── 06_arquitectura_modulos.tex
│   │   │   ├── 07_herramienta_trello.tex
│   │   │   ├── 08_reflexion_git.tex
│   │   │   └── 09_benchmarking_soluciones.tex
│   │   └── imagenes/
│   │       └── escudo.png             # Escudo oficial de la UNSAAC en alta resolución
│   ├── trello/
│   │   ├── SIGC-CUSCO.md              # Tablero Trello: columnas, límites WIP, bloqueo, roles y DoD
│   │   └── plantillas-tarjetas.md     # Plantillas de tarjeta: historia, bloqueada y en revisión
│   ├── equipo/
│   │   └── ACUERDOS-DE-TRABAJO.md     # Roles, Daily, límites WIP, bloqueos, flujo Git, DoR y DoD
│   └── v2/
│       ├── v2.tex                     # Documento V2 (ejercicios ágiles, Sprint 3, requerimientos, UML, BD)
│       └── v2.pdf                     # PDF compilado de la V2
└── src/                               # (Próxima fase) Código fuente del desarrollo de software
```

---

## 🛠️ Compilación Rápida del Documento LaTeX

```bash
# Navegar a la carpeta de LaTeX
cd docs/latex

# Compilación con pdflatex (dos pasadas para resolver tabla de contenidos e índices)
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

---

## 🔄 Flujo del Sistema (SIGC-CUSCO)

```text
[INSTITUCIÓN (Municipalidad / Empresa Turística)]
   │
   ▼
[Creación del Curso (Fechas, Vacantes, Modalidad, Docente)]
   │
   ▼
[Inscripción Digital con Validación de DNI]
   │
   ▼
[Control de Asistencia Digital (Marcado QR / Offline)]
   │
   ▼
[Evaluación Académica y Cierre de Actas en Línea]
   │
   ▼
[Emisión Automática de Certificado PDF con Código QR Único]
   │
   ▼
[Verificación Documental Pública + Reporte Gerencial para Auditoría]
```
