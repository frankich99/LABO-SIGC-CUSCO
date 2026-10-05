# Tablero Trello: SIGC-CUSCO (Lab 03)

* **Proyecto:** Sistema Integral de Gestión de Capacitaciones (SIGC-CUSCO)
* **Curso:** Ingeniería de Software I — UNSAAC
* **Integrantes:**
  * Choquenaira Quispe, Noe Franklin (133962)
  * Yaranga Achahui, Aldo (103179)
  * Ccama Enriquez, Carolay (210921)
* **Docente:** Ing. Lisha Sabah Diaz Caceres

---

## 📋 Lista: Product Backlog (Priorizado)

### 🔴 Prioridad Alta (Must Have)
1. **[HU-10] Asignación de Roles y Permisos (RBAC)**
   * *Descripción:* Como administrador, quiero asignar roles a cada usuario (admin, docente, participante) para que cada uno vea solo lo que le corresponde.
   * *Criterios de Aceptación:*
     - Dado un usuario nuevo, cuando el admin le asigna un rol, entonces sus permisos se actualizan en el acto.

2. **[HU-06] Creación de Capacitaciones**
   * *Descripción:* Como administrador, quiero crear capacitaciones con fechas, cupos y docente asignado para abrir convocatorias.
   * *Criterios de Aceptación:*
     - Dado que se completan los campos obligatorios, cuando se guarda, la capacitación queda en estado "Abierta".

3. **[HU-01] Inscripción con DNI**
   * *Descripción:* Como participante, quiero inscribirme a un curso usando mi DNI para evitar trámites presenciales.
   * *Criterios de Aceptación:*
     - Dado un DNI de 8 dígitos válido y cupos libres, cuando se envía el formulario, queda registrado.
     - Si ya no hay cupos, el sistema bloquea el registro e informa al usuario.

4. **[HU-03] Control de Asistencia QR**
   * *Descripción:* Como docente, quiero registrar asistencia escaneando un código QR para no perder tiempo con listas de papel.
   * *Criterios de Aceptación:*
     - Dado el QR activo de la sesión, cuando el alumno escanea, se guarda fecha y hora de ingreso.

5. **[HU-04] Registro de Notas y Aprobación**
   * *Descripción:* Como docente, quiero ingresar notas de participantes para que el sistema calcule el estado de aprobación automáticamente.
   * *Criterios de Aceptación:*
     - Notas de 0 a 20; con nota mayor o igual a 11 la condición es "Aprobado".

6. **[HU-05] Emisión y Descarga de Certificado PDF**
   * *Descripción:* Como participante, quiero descargar mi certificado en PDF con código QR para acreditar mi capacitación.
   * *Criterios de Aceptación:*
     - Solo disponible para participantes aprobados. Incluye datos completos y código QR de validación.

---

### 🟡 Prioridad Media (Should Have)
7. **[HU-07] Gestión Multientidad**
   * *Descripción:* Como administrador, quiero registrar instituciones (municipalidades y empresas) para gestionar cursos de forma independiente.
8. **[HU-08] Verificación Pública de Certificados**
   * *Descripción:* Como ciudadano, quiero escanear el QR o ingresar el código del certificado para verificar su autenticidad en el portal web.
9. **[HU-09] Reportes para Auditoría**
   * *Descripción:* Como gerente, quiero generar reportes de participantes, asistencia y notas para presentarlos a auditorías (OSCE/OCI).
10. **[HU-02] Confirmación por Correo**
    * *Descripción:* Como participante, quiero recibir un correo al inscribirme para tener constancia de mi registro.

---

### 🟢 Prioridad Baja (Could Have)
11. **[HU-12] Catálogo Público de Cursos**
    * *Descripción:* Como participante, quiero ver la lista de capacitaciones disponibles para elegir dónde inscribirme.
12. **[HU-11] Asistencia en Modo Offline**
    * *Descripción:* Como docente, quiero marcar asistencia sin internet para que se sincronice al recuperar la conexión.
