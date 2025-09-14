from aqt.utils import showInfo
from aqt.qt import QDialog, QVBoxLayout, QMessageBox
from ...constants import GeneralConstants, UIConstants
from ..config_form import ConfigForm

class ConfigDialog(QDialog):
    """Diálogo principal de configuración para mazos filtrados - maneja ventana y eventos"""
    
    def __init__(self, parent=None, edit_data=None):
        super().__init__(parent)
        self.edit_data = edit_data
        self.config_form = ConfigForm()
        self.setup_ui()
        self.setup_connections()
        self.apply_styles()
        
        # Si estamos en modo edición, cargar los datos
        if self.edit_data:
            self.load_edit_data()
            self.setWindowTitle(f"{UIConstants.DIALOG_TITLE_EDIT} - {GeneralConstants.ADDON_NAME}")
        else:
            self.setWindowTitle(GeneralConstants.ADDON_NAME)
    
    def setup_ui(self):
        """Configura la interfaz de usuario principal"""
        # Layout principal
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)
        
        # Agregar secciones del formulario al layout
        for section in self.config_form.get_sections():
            main_layout.addWidget(section)
        
        self.setLayout(main_layout)
        
        # Configurar tamaño mínimo
        self.setMinimumWidth(600)
        self.setMinimumHeight(700)
        
        # Centrar la ventana
        if self.parent():
            self.move(
                self.parent().x() + (self.parent().width() - self.width()) // 2,
                self.parent().y() + (self.parent().height() - self.height()) // 2
            )
    
    def setup_connections(self):
        """Configura las conexiones de señales y slots"""
        self.config_form.setup_connections(
            self.on_create_clicked,
            self.on_test_clicked,
            self.on_cancel_clicked
        )
    
    def apply_styles(self):
        """Aplica estilos generales al diálogo"""
        self.setStyleSheet("""
            QDialog {
                background-color: #ffffff;
            }
        """)
    
    def load_edit_data(self):
        """Carga los datos para edición"""
        self.config_form.load_edit_data(self.edit_data)
    
    def validate_form(self) -> bool:
        """Valida todo el formulario"""
        errors = self.config_form.get_validation_errors()
        
        if errors:
            error_message = "Por favor corrija los siguientes errores:\n\n" + "\n".join(f"• {error}" for error in errors)
            QMessageBox.warning(self, "Errores de Validación", error_message)
            return False
        
        return True
    
    def get_form_data(self) -> dict:
        """Retorna todos los datos del formulario"""
        return self.config_form.get_form_data()
    
    def on_create_clicked(self):
        """Maneja el clic en el botón crear/actualizar"""
        if not self.validate_form():
            return
        
        # Obtener datos del formulario
        form_data = self.get_form_data()
        
        # Aquí iría la lógica para crear/actualizar los mazos filtrados
        # Por ahora, solo mostramos un mensaje
        self.config_form.actions_section.set_status("Procesando...")
        self.config_form.actions_section.disable_buttons(True)
        
        # Simulación de procesamiento
        showInfo(
            f"Configuración '{form_data['basic']['name']}' guardada exitosamente.\n"
            f"Query: {form_data['search']['search_query']}\n"
            f"Grupos configurados: {len(form_data['grouping']['groups'])}"
        )
        
        self.config_form.actions_section.set_status("Configuración completada")
        self.config_form.actions_section.disable_buttons(False)
        
        # Cerrar el diálogo
        self.accept()
    
    def on_test_clicked(self):
        """Maneja el clic en el botón probar"""
        if not self.validate_form():
            return
        
        form_data = self.get_form_data()
        
        # Aquí iría la lógica para probar la configuración
        self.config_form.actions_section.set_status("Probando configuración...")
        
        showInfo(
            f"Prueba de configuración '{form_data['basic']['name']}'.\n"
            f"La consulta buscaría: {form_data['search']['search_query']}\n"
            f"Se crearían {len(form_data['grouping']['groups'])} grupos de mazos."
        )
        
        self.config_form.actions_section.set_status("Prueba completada")
    
    def on_cancel_clicked(self):
        """Maneja el clic en el botón cancelar"""
        self.reject()
    
    def clear_form(self):
        """Limpia todos los campos del formulario"""
        self.config_form.clear_form()