from aqt.utils import showInfo
from aqt.qt import QDialog, QVBoxLayout, QMessageBox, QScrollArea, QWidget, Qt
from ...constants import UIConstants
from ...styles import styles
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
            self.setWindowTitle(f"{UIConstants.DIALOG_TITLE_EDIT} - {UIConstants.ADDON_NAME}")
        else:
            self.setWindowTitle(f"{UIConstants.DIALOG_TITLE_MAIN} - {UIConstants.ADDON_NAME}")
    
    def setup_ui(self):
        """Configura la interfaz de usuario principal"""
        # Layout principal
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(
            UIConstants.DIALOG_MAIN_MARGIN,
            UIConstants.DIALOG_MAIN_MARGIN,
            UIConstants.DIALOG_MAIN_MARGIN,
            UIConstants.DIALOG_MAIN_MARGIN
        )
        main_layout.setSpacing(UIConstants.DIALOG_MAIN_SPACING)
        
        # Crear un widget contenedor para el formulario
        form_widget = QWidget()
        form_widget.setObjectName(UIConstants.OBJECT_NAME_MAIN_WIDGET)
        form_layout = QVBoxLayout()
        form_layout.setContentsMargins(
            UIConstants.DIALOG_CONTENT_MARGIN,
            UIConstants.DIALOG_CONTENT_MARGIN,
            UIConstants.DIALOG_CONTENT_MARGIN,
            UIConstants.DIALOG_CONTENT_MARGIN
        )  # Padding para el contenedor scrollable
        form_layout.setSpacing(UIConstants.DIALOG_CONTENT_SPACING)
        
        # Agregar secciones del formulario al layout del widget
        for section in self.config_form.get_sections():
            form_layout.addWidget(section)
        
        form_widget.setLayout(form_layout)
        
        # Crear scroll area y configurar el widget contenedor
        scroll_area = QScrollArea()
        scroll_area.setWidget(form_widget)
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)  # Solo scroll vertical
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        
        # Agregar el scroll area al layout principal
        main_layout.addWidget(scroll_area)
        self.setLayout(main_layout)
        
        # Configurar tamaño mínimo
        self.setMinimumWidth(UIConstants.DIALOG_MIN_WIDTH)
        self.setMinimumHeight(UIConstants.DIALOG_MIN_HEIGHT)
        
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
        self.setStyleSheet(styles.DIALOG)
    
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
        self.config_form.actions_section.set_status(UIConstants.STATUS_PROCESSING)
        self.config_form.actions_section.disable_buttons(True)
        
        # Simulación de procesamiento
        showInfo(
            UIConstants.INFO_CONFIG_SAVED.format(
                name=form_data['basic']['name'],
                query=form_data['search']['search_query'],
                groups=len(form_data['grouping']['groups'])
            )
        )
        
        self.config_form.actions_section.set_status(UIConstants.STATUS_CONFIGURATION_COMPLETED)
        self.config_form.actions_section.disable_buttons(False)
        
        # Cerrar el diálogo
        self.accept()
    
    def on_test_clicked(self):
        """Maneja el clic en el botón probar"""
        if not self.validate_form():
            return
        
        form_data = self.get_form_data()
        
        # Aquí iría la lógica para probar la configuración
        self.config_form.actions_section.set_status(UIConstants.STATUS_TESTING_CONFIGURATION)
        
        showInfo(
            UIConstants.INFO_CONFIG_TEST.format(
                name=form_data['basic']['name'],
                query=form_data['search']['search_query'],
                groups=f"{len(form_data['grouping']['groups'])} groups of decks"
            )
        )
        
        self.config_form.actions_section.set_status(UIConstants.STATUS_TEST_COMPLETED)
    
    def on_cancel_clicked(self):
        """Maneja el clic en el botón cancelar"""
        self.reject()
    
    def clear_form(self):
        """Limpia todos los campos del formulario"""
        self.config_form.clear_form()