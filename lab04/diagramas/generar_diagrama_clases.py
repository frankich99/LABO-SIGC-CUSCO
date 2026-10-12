import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Configuración de lienzo
fig, ax = plt.subplots(figsize=(15, 10.5), dpi=300)
ax.set_xlim(0, 1500)
ax.set_ylim(0, 1050)
ax.axis('off')

# Paleta de colores UML profesional
COLOR_HEADER_MAIN = '#0284c7'
COLOR_HEADER_DOC = '#0369a1'
COLOR_HEADER_CERT = '#059669'
COLOR_HEADER_ALERT = '#d97706'
COLOR_HEADER_ENUM = '#475569'
COLOR_BG = '#ffffff'
COLOR_BORDER = '#0284c7'
COLOR_TEXT = '#0f172a'
COLOR_MUTED = '#475569'

def draw_uml_class(x, y, w, h, title, attributes, methods, header_color=COLOR_HEADER_MAIN):
    # Caja principal
    rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=2,rounding_size=6",
                                  facecolor=COLOR_BG, edgecolor=COLOR_BORDER, linewidth=1.5)
    ax.add_patch(rect)
    
    # Encabezado
    h_header = 28
    hdr = patches.FancyBboxPatch((x, y + h - h_header), w, h_header,
                                 boxstyle="round,pad=2,rounding_size=6",
                                 facecolor=header_color, edgecolor=COLOR_BORDER, linewidth=1.5)
    ax.add_patch(hdr)
    ax.text(x + w/2, y + h - h_header/2 - 2, title, color='#ffffff',
            fontsize=9.5, fontweight='bold', ha='center', va='center', family='sans-serif')
    
    # Atributos
    curr_y = y + h - h_header - 14
    for attr in attributes:
        ax.text(x + 10, curr_y, attr, color=COLOR_TEXT, fontsize=7.5, va='center', family='sans-serif')
        curr_y -= 14
        
    # Línea divisoria
    ax.plot([x, x + w], [curr_y + 6, curr_y + 6], color='#cbd5e1', linewidth=1)
    curr_y -= 6
    
    # Métodos
    for m in methods:
        ax.text(x + 10, curr_y, m, color=COLOR_MUTED, fontsize=7.5, va='center', family='sans-serif')
        curr_y -= 14

# 1. Superclase Usuario
draw_uml_class(570, 830, 360, 180, "Usuario <<Abstract>>", [
    "- id : int",
    "- dni : string [8]",
    "- nombres : string",
    "- apellidos : string",
    "- email : string",
    "- passwordHash : string",
    "- rol : RolUsuario"
], [
    "+ iniciarSesion(pass) : boolean",
    "+ recuperarPassword() : void",
    "+ getNombreCompleto() : string"
])

# 2. Participante
draw_uml_class(260, 580, 260, 140, "Participante", [
    "- entidadProcedencia : string",
    "- telefono : string"
], [
    "+ inscribirse(cursoId) : Inscripcion",
    "+ marcarAsistenciaQR(token) : bool",
    "+ descargarCertificado() : Certificado"
], COLOR_HEADER_DOC)

# 3. Docente
draw_uml_class(620, 580, 260, 140, "Docente", [
    "- especialidad : string",
    "- gradoAcademico : string",
    "- firmaDigitalPath : string"
], [
    "+ iniciarSesionClase() : SesionClase",
    "+ generarQR(sesionId) : string",
    "+ registrarNota(actaId, nota) : void",
    "+ cerrarActaFinal() : void"
], COLOR_HEADER_DOC)

# 4. Administrador
draw_uml_class(980, 580, 250, 140, "Administrador", [
    "- cargoOficina : string"
], [
    "+ registrarInstitucion() : Institucion",
    "+ crearCapacitacion() : Capacitacion",
    "+ asignarDocente(cursoId, docId) : void",
    "+ emitirReporteAuditoria() : Reporte"
], COLOR_HEADER_DOC)

# 5. Institución
draw_uml_class(40, 310, 220, 130, "Institucion", [
    "- id : int",
    "- ruc : string [11]",
    "- razonSocial : string",
    "- logoUrl : string"
], [
    "+ listarCursos() : List<Capacitacion>"
])

# 6. Capacitación
draw_uml_class(340, 270, 310, 200, "Capacitacion", [
    "- id : int",
    "- codigo : string",
    "- titulo : string",
    "- horasAcademicas : int",
    "- fechaInicio : date",
    "- fechaFin : date",
    "- cuposTotales : int",
    "- cuposDisponibles : int",
    "- estado : EstadoCurso"
], [
    "+ hayVacantes() : boolean",
    "+ descontarCupo() : void",
    "+ calcularPorcentajeAsistencia() : float",
    "+ calcularTasaAprobacion() : float"
])

# 7. Inscripción
draw_uml_class(750, 270, 290, 190, "Inscripcion", [
    "- id : int",
    "- fechaInscripcion : datetime",
    "- estado : EstadoInscripcion",
    "- notaFinal : float [0..20]",
    "- porcentajeAsistencia : float"
], [
    "+ registrarNotaFinal(nota) : void",
    "+ cumpleRequisitosCert() : boolean",
    "+ emitirCodigoCertificado() : string"
])

# 8. Sesión de Clase
draw_uml_class(240, 30, 280, 170, "SesionClase", [
    "- id : int",
    "- numeroSesion : int",
    "- fecha : date",
    "- horaInicio : time",
    "- horaFin : time",
    "- tokenQR : string",
    "- expiracionToken : datetime"
], [
    "+ generarTokenQR() : string",
    "+ validarVigencia(token) : boolean"
])

# 9. Asistencia
draw_uml_class(620, 30, 270, 160, "Asistencia", [
    "- id : int",
    "- fechaHoraMarcado : datetime",
    "- estado : EstadoAsistencia",
    "- metodo : string [QR / Manual]",
    "- ipMarcacion : string"
], [
    "+ registrarMarcacion() : boolean",
    "+ validarTolerancia() : boolean"
])

# 10. Certificado
draw_uml_class(1140, 270, 320, 180, "Certificado", [
    "- id : int",
    "- codigoVerificacion : string",
    "- hashSHA256 : string",
    "- fechaEmision : datetime",
    "- pdfUrl : string"
], [
    "+ generarHashCriptografico() : string",
    "+ verificarFirma() : boolean",
    "+ validarAutenticidad(hash) : boolean"
], COLOR_HEADER_CERT)

# 11. AlertaNotificación
draw_uml_class(1140, 830, 320, 160, "AlertaNotificacion", [
    "- id : int",
    "- tipo : TipoAlertaEnum",
    "- titulo : string",
    "- mensaje : string",
    "- fechaCreacion : datetime",
    "- leida : boolean"
], [
    "+ marcarComoLeida() : void",
    "+ dispararNotificacion() : void"
], COLOR_HEADER_ALERT)

# 12. Cuadro de Enumeraciones
enum_box = patches.FancyBboxPatch((1000, 30), 460, 140, boxstyle="round,pad=2,rounding_size=6",
                                 facecolor='#f8fafc', edgecolor='#64748b', linewidth=1.2)
ax.add_patch(enum_box)
hdr_e = patches.FancyBboxPatch((1000, 145), 460, 25, boxstyle="round,pad=2,rounding_size=6",
                              facecolor=COLOR_HEADER_ENUM, edgecolor='#64748b', linewidth=1.2)
ax.add_patch(hdr_e)
ax.text(1230, 157, "<<Enumeraciones del Sistema>>", color='#ffffff',
        fontsize=9, fontweight='bold', ha='center', va='center')
ax.text(1020, 125, "• RolUsuario: ADMIN, DOCENTE, PARTICIPANTE", color=COLOR_TEXT, fontsize=7.5)
ax.text(1020, 105, "• EstadoCurso: BORRADOR, ABIERTO, EN_CURSO, CONCLUIDO, CANCELADO", color=COLOR_TEXT, fontsize=7.5)
ax.text(1020, 85, "• EstadoInscripcion: INSCRITO, EN_PROCESO, APROBADO, DESAPROBADO", color=COLOR_TEXT, fontsize=7.5)
ax.text(1020, 65, "• TipoAlerta: PLAZO_ACTA, ASISTENCIA_RIESGO, CERTIFICADO_EMITIDO", color=COLOR_TEXT, fontsize=7.5)
ax.text(1020, 45, "• EstadoAsistencia: PRESENTE, TARDANZA, FALTA, JUSTIFICADO", color=COLOR_TEXT, fontsize=7.5)

# ================= RELACIONES Y FLECHAS =================

# Herencia (Triángulo blanco hacia Usuario)
triangle = patches.Polygon([[750, 830], [740, 805], [760, 805]], closed=True,
                           facecolor='#ffffff', edgecolor='#334155', linewidth=1.5)
ax.add_patch(triangle)
ax.plot([750, 750], [805, 780], color='#334155', linewidth=1.5)

# Ramas de herencia
ax.plot([390, 1105], [780, 780], color='#334155', linewidth=1.5)
ax.plot([390, 390], [780, 720], color='#334155', linewidth=1.5)
ax.plot([750, 750], [780, 720], color='#334155', linewidth=1.5)
ax.plot([1105, 1105], [780, 720], color='#334155', linewidth=1.5)

# Institucion 1 -- 0..* Capacitacion
ax.plot([260, 340], [380, 380], color='#334155', linewidth=1.5)
ax.text(270, 390, "1", fontsize=8.5, fontweight='bold', color=COLOR_TEXT)
ax.text(315, 390, "0..*", fontsize=8.5, fontweight='bold', color=COLOR_TEXT)
ax.text(285, 365, "promueve >", fontsize=7.5, color=COLOR_MUTED)

# Docente 1 -- 0..* Capacitacion
ax.plot([700, 700, 520, 520], [580, 520, 520, 470], color='#334155', linewidth=1.5)
ax.text(708, 560, "1", fontsize=8.5, fontweight='bold', color=COLOR_TEXT)
ax.text(528, 485, "0..*", fontsize=8.5, fontweight='bold', color=COLOR_TEXT)
ax.text(590, 528, "dicta >", fontsize=7.5, color=COLOR_MUTED)

# Capacitacion 1 -- 0..* Inscripcion
ax.plot([650, 750], [370, 370], color='#334155', linewidth=1.5)
ax.text(660, 380, "1", fontsize=8.5, fontweight='bold', color=COLOR_TEXT)
ax.text(725, 380, "0..*", fontsize=8.5, fontweight='bold', color=COLOR_TEXT)
ax.text(685, 355, "registra >", fontsize=7.5, color=COLOR_MUTED)

# Participante 1 -- 0..* Inscripcion
ax.plot([390, 390, 830, 830], [580, 500, 500, 460], color='#334155', linewidth=1.5)
ax.text(400, 560, "1", fontsize=8.5, fontweight='bold', color=COLOR_TEXT)
ax.text(840, 475, "0..*", fontsize=8.5, fontweight='bold', color=COLOR_TEXT)
ax.text(580, 506, "realiza >", fontsize=7.5, color=COLOR_MUTED)

# Capacitacion 1 -- 1..* SesionClase
ax.plot([450, 450, 380, 380], [270, 230, 230, 200], color='#334155', linewidth=1.5)
ax.text(458, 250, "1", fontsize=8.5, fontweight='bold', color=COLOR_TEXT)
ax.text(390, 210, "1..*", fontsize=8.5, fontweight='bold', color=COLOR_TEXT)
ax.text(410, 236, "programa >", fontsize=7.5, color=COLOR_MUTED)

# SesionClase 1 -- 0..* Asistencia
ax.plot([520, 620], [115, 115], color='#334155', linewidth=1.5)
ax.text(530, 125, "1", fontsize=8.5, fontweight='bold', color=COLOR_TEXT)
ax.text(595, 125, "0..*", fontsize=8.5, fontweight='bold', color=COLOR_TEXT)
ax.text(550, 100, "controla >", fontsize=7.5, color=COLOR_MUTED)

# Inscripcion 1 -- 0..* Asistencia
ax.plot([800, 800, 780, 780], [270, 230, 230, 190], color='#334155', linewidth=1.5)
ax.text(808, 250, "1", fontsize=8.5, fontweight='bold', color=COLOR_TEXT)
ax.text(788, 205, "0..*", fontsize=8.5, fontweight='bold', color=COLOR_TEXT)

# Inscripcion 1 -- 0..1 Certificado
ax.plot([1040, 1140], [360, 360], color='#334155', linewidth=1.5)
ax.text(1050, 370, "1", fontsize=8.5, fontweight='bold', color=COLOR_TEXT)
ax.text(1110, 370, "0..1", fontsize=8.5, fontweight='bold', color=COLOR_TEXT)
ax.text(1070, 345, "origina >", fontsize=7.5, color=COLOR_MUTED)

# Usuario 1 -- 0..* AlertaNotificacion
ax.plot([930, 1140], [910, 910], color='#334155', linewidth=1.5)
ax.text(940, 920, "1", fontsize=8.5, fontweight='bold', color=COLOR_TEXT)
ax.text(1110, 920, "0..*", fontsize=8.5, fontweight='bold', color=COLOR_TEXT)
ax.text(1010, 895, "recibe >", fontsize=7.5, color=COLOR_MUTED)

# Guardar figura en alta resolución
plt.tight_layout()
plt.savefig('latex/imagenes/diagrama_clases.png', dpi=300, bbox_inches='tight')
plt.savefig('diagramas/diagrama_clases.png', dpi=300, bbox_inches='tight')
print("Diagrama de clases generado exitosamente.")
