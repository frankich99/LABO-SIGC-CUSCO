# Sistema Integral de Gestión de Capacitaciones (SIGC)

[![Versión](https://img.shields.io/badge/versión-SIGC__V0.1-blue.svg)](https://github.com/)
[![Universidad](https://img.shields.io/badge/UNSAAC-Ingeniería_de_Sistemas-red.svg)](https://www.unsaac.edu.pe/)
[![Curso](https://img.shields.io/badge/Curso-Ingeniería_de_Software_I-orange.svg)](https://www.unsaac.edu.pe/)
[![Documentación](https://img.shields.io/badge/LaTeX-APA_7ma_Edición-brightgreen.svg)](docs/latex/main.pdf)
[![Gestión](https://img.shields.io/badge/Metodología-Agile_Inception_%26_Trello-0079BF.svg)](docs/trello/estructura_trello.md)

---

## 📌 Descripción del Proyecto

El **Sistema Integral de Gestión de Capacitaciones (SIGC)** es una plataforma de software concebida para centralizar, automatizar, gestionar y auditar todo el ciclo formativo en instituciones públicas (como municipalidades de la región Cusco) y entidades privadas (con especial énfasis en empresas del sector turismo: hoteles, agencias y gastronomía).

El sistema sustituye el uso desarticulado de hojas de cálculo de Excel, listas impresas de asistencia y diplomas manuales en Word o Canva, garantizando **trazabilidad completa desde la convocatoria e inscripción digital hasta la emisión instantánea de certificados digitales infalsificables respaldados con código QR y validación pública**.

---

## 👥 Integrantes del Equipo (Grupo de Trabajo)

* **Choquenaira Quispe, Noe Franklin** — *Código: 133962* — [GitHub: @frankich99](https://github.com/frankich99)
* **Yaranga Achahui, Aldo** — *Código: 103179*
* **Ccama Enriquez, Carolay** — *Código: 210921*

**Institución:** Universidad Nacional de San Antonio Abad del Cusco (UNSAAC)  
**Facultad:** Facultad de Ingeniería Eléctrica, Electrónica, Informática y Mecánica  
**Escuela Profesional:** Ingeniería Informática y de Sistemas  
**Asignatura:** Ingeniería de Software I (Semestre 2026-II)  
**Docente:** _____________________________________________

---

## 🚀 Entregables del Laboratorio 2 (Agile Inception)

En cumplimiento riguroso de la **Guía de Laboratorio 02: Agile Inception**, este repositorio alberga la documentación técnica formal:

1. **Identificación y Matriz de Stakeholders:** Caracterización de Municipalidades (OSCE/SIGA), Empresas Turísticas (Atención al cliente), Participantes, Capacitadores y Administradores TI.
2. **Definición de la Visión (Geoffrey Moore):** Posicionamiento claro del producto, frontera de alcance (*Es / No Es / Hace / No Hace*) y objetivos SMART.
3. **Lean Canvas Refinado (9 Bloques):** Modelado ágil de negocio en orientación horizontal (`docs/latex/secciones/04_lean_canvas.tex`).
4. **Matriz de Riesgos Iniciales:** Mitigación de brecha digital, conectividad offline, y prevención de falsificación documental vía SHA-256 + QR.
5. **Gestión Ágil con Trello:** Tablero Kanban con políticas de flujo (Backlog, To Do, In Progress, QA, Done).
6. **Reflexión sobre Control de Versiones con Git:** Sustento de desarrollo colaborativo concurrente, trazabilidad y prevención de conflictos.
7. **Trabajo Extra (Benchmarking de Mercado):** Comparativa frente a Moodle, Google Workspace, LMS corporativos (Crehana/Platzi) y portales estatales (OSCE).

---

## 📂 Estructura del Repositorio

```text
SIGC_V0.1/
├── README.md                          # Presentación oficial y documentación del proyecto
├── docs/                              # Documentación técnica formal
│   ├── latex/                         # Código fuente completo en LaTeX (APA 7ma Edición)
│   │   ├── main.tex                   # Archivo raíz que ensambla todas las secciones
│   │   ├── main.pdf                   # Documento PDF compilado (27 páginas con carátula)
│   │   ├── config/
│   │   │   └── packages.tex           # Configuración tipográfica, márgenes y paquetes
│   │   ├── secciones/
│   │   │   ├── 00_portada.tex         # Portada oficial institucional UNSAAC
│   │   │   ├── 01_objetivo_fundamento.tex
│   │   │   ├── 02_stakeholders.tex
│   │   │   ├── 03_vision_sistema.tex
│   │   │   ├── 04_lean_canvas.tex     # Lean Canvas de 9 bloques en formato horizontal
│   │   │   ├── 05_gestion_riesgos.tex
│   │   │   ├── 06_arquitectura_modulos.tex
│   │   │   ├── 07_herramienta_trello.tex
│   │   │   ├── 08_reflexion_git.tex
│   │   │   └── 09_benchmarking_soluciones.tex
│   │   └── imagenes/
│   │       └── escudo.png             # Escudo oficial de la UNSAAC en alta resolución
│   └── trello/
│       └── estructura_trello.md       # Configuración detallada de listas, etiquetas y tareas
└── src/                               # (Próxima fase) Código fuente de la implementación web
```

---

## 🛠️ Cómo Compilar el Documento LaTeX

El documento está optimizado para compilar de forma ultra rápida sin requerir dependencias externas complejas:

```bash
# Navegar a la carpeta de LaTeX
cd docs/latex

# Compilación con pdflatex (dos pasadas para resolver referencias y tabla de contenidos)
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

El resultado se genera directamente como `main.pdf`.

---

## 🔄 Flujo del Sistema (Ciclo Formativo SIGC)

```text
[INSTITUCIÓN (Municipalidad / Empresa Turística)]
   │
   ▼
[Creación del Curso (Fechas, Vacantes, Modalidad, Capacitador)]
   │
   ▼
[Publicación e Inscripción Digital con Validación de DNI]
   │
   ▼
[Control de Asistencia Digital (Marcado QR o Lista Rápida)]
   │
   ▼
[Evaluación Académica y Cierre de Actas en Línea]
   │
   ▼
[Emisión Automática de Certificado PDF con Código QR Único]
   │
   ▼
[Verificación Documental Pública + Reporte Gerencial de Impacto]
```

---

## 📋 Tablero de Trello

El seguimiento visual del proyecto se realiza en Trello bajo la siguiente convención:
* **Backlog:** Épicas de desarrollo (Usuarios, Cursos, Asistencia, Certificados, Reportes).
* **Sprint Inception (To Do):** Tareas del Laboratorio 2 completadas y validadas.
* **WIP Limit:** Máximo 3 tareas simultáneas en proceso.
* **Definition of Done:** Documento en LaTeX sin errores de compilación, aprobado por revisión de pares en GitHub.

---

## 📄 Licencia y Derechos

Desarrollado con fines estrictamente académicos para el curso de **Ingeniería de Software I** en la **Universidad Nacional de San Antonio Abad del Cusco (UNSAAC)**, Semestre 2026-II.
