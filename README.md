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
6. **Gestión Ágil con Trello:** Tablero Kanban `SIGC-CUSCO` con políticas de flujo (Backlog, To Do, In Progress, QA, Done).
7. **Reflexión sobre Control de Versiones con Git:** Sustento de desarrollo colaborativo concurrente, trazabilidad y prevención de fallos.
8. **Trabajo Extra (Benchmarking de Mercado):** Comparativa frente a Moodle, Google Workspace, LMS corporativos (Crehana/Platzi) y portales estatales (OSCE).

---

## 📋 Contenido del Laboratorio 03 (Historias de Usuario y Product Backlog)

1. **Parte 1 — Identificación de Funcionalidades:** Mapeo de 12 requerimientos funcionales aterrizados al SIGC-CUSCO (autenticación RBAC, cursos, inscripción con DNI, control de asistencia QR, evaluaciones, certificados PDF y verificación pública).
2. **Parte 2 — Historias de Usuario:** Redacción de historias en formato estándar (*Como [usuario], quiero [funcionalidad], para [beneficio]*) cubriendo los roles del sistema (Participante, Docente, Administrador, Gerente Municipal y Ciudadano).
3. **Parte 3 — Product Backlog Priorizado:** Ordenamiento ágil aplicando la técnica MoSCoW (*Must Have, Should Have, Could Have*).
4. **Trabajo Extra — Criterios de Aceptación:** Definición de escenarios de validación bajo el formato BDD (*Dado / Cuando / Entonces*) para las historias prioritarias.

---

## 📂 Estructura del Repositorio

```text
SIGC-CUSCO/
├── README.md                          # Presentación oficial del proyecto para GitHub
├── lab03/                             # Laboratorio 03: Elicitación de Requerimientos
│   ├── Lab 3 ING. DE SOFTWARE.pdf     # Guía oficial del laboratorio
│   └── docs/
│       ├── latex/                     # Informe técnico modular en LaTeX
│       │   ├── main.tex               # Documento principal
│       │   ├── main.pdf               # Documento PDF compilado
│       │   ├── config/packages.tex    # Paquetes y estilos
│       │   ├── secciones/             # Portada, objetivos, historias, backlog, criterios
│       │   └── imagenes/              # Escudo oficial UNSAAC
│       └── trello/
│           └── SIGC-CUSCO-lab03.md    # Tarjetas para tablero Kanban / Backlog
├── docs/                              # Documentación del Laboratorio 02 y arquitectura
│   ├── latex/                         # Fuente LaTeX del Lab 02
│   ├── trello/                        # Tablero Trello inicial
│   └── v2/                            # Especificación técnica v2
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
