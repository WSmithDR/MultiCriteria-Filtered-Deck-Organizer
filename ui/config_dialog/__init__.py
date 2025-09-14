from aqt.utils import showInfo
from aqt.qt import QDialog, QVBoxLayout, QMessageBox
from ...constants import GeneralConstants
from .basic_config_section import BasicConfigSection
from .search_section import SearchSection
from .grouping_section import GroupingSection
from .actions_section import ActionsSection

class ConfigDialog(QDialog):
    """Diálogo principal de configuración para mazos filtrados"""
    
    def __init__(self, parent=None, edit_data=None):
        super().__init__(parent)
        self.edit_data = edit_data
        self.setup_ui()
        self.setup_connections()
        self.apply_styles()
        
        # Si estamos en modo edición, cargar los datos
        if self.edit_data:
            self.load_edit_data()
            self.setWindowTitle(f"Editar Configuración - {GeneralConstants.ADDON_NAME}")
        else:
            self.setWindowTitle(GeneralConstants.ADDON_NAME)
    
    def setup_ui(self):
        """Configura la interfaz de usuario principal"""
        # Crear secciones
        self.basic_section = BasicConfigSection()
        self.search_section = SearchSection()
        self.grouping_section = GroupingSection()
        self.actions_section = ActionsSection()
        
        # Layout principal
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)
        
        # Agregar secciones al layout
        main_layout.addWidget(self.basic_section)
        main_layout.addWidget(self.search_section)
        main_layout.addWidget(self.grouping_section)
        main_layout.addWidget(self.actions_section)
        
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
        self.actions_section.connect_create_action(self.on_create_clicked)
        self.actions_section.connect_test_action(self.on_test_clicked)
        self.actions_section.connect_cancel_action(self.on_cancel_clicked)
    
    def apply_styles(self):
        """Aplica estilos generales al diálogo"""
        self.setStyleSheet("""
            QDialog {
                background-color: #ffffff;
            }
        """)
    
    def load_edit_data(self):
        """Carga los datos para edición"""
        if not self.edit_data:
            return
            
        # Cargar datos en cada sección
        if 'basic' in self.edit_data:
            self.basic_section.set_data(self.edit_data['basic'])
        
        if 'search' in self.edit_data:
            self.search_section.set_data(self.edit_data['search'])
        
        if 'grouping' in self.edit_data:
            self.grouping_section.set_data(self.edit_data['grouping'])
        
        # Cambiar texto del botón para modo edición
        self.actions_section.set_create_button_text("Actualizar Configuración")
    
    def validate_form(self) -> bool:
        """Valida todo el formulario"""
        errors = []
        
        # Validar cada sección
        if not self.basic_section.is_valid():
            errors.extend(self.basic_section.get_validation_errors())
        
        if not self.search_section.is_valid():
            errors.extend(self.search_section.get_validation_errors())
        
        if not self.grouping_section.is_valid():
            errors.extend(self.grouping_section.get_validation_errors())
        
        if errors:
            error_message = "Por favor corrija los siguientes errores:\n\n" + "\n".join(f"• {error}" for error in errors)
            QMessageBox.warning(self, "Errores de Validación", error_message)
            return False
        
        return True
    
    def get_form_data(self) -> dict:
        """Retorna todos los datos del formulario"""
        return {
            'basic': self.basic_section.get_data(),
            'search': self.search_section.get_data(),
            'grouping': self.grouping_section.get_data()
        }
    
    def on_create_clicked(self):
        """Maneja el clic en el botón crear/actualizar"""
        if not self.validate_form():
            return
        
        # Obtener datos del formulario
        form_data = self.get_form_data()
        
        # Aquí iría la lógica para crear/actualizar los mazos filtrados
        # Por ahora, solo mostramos un mensaje
        self.actions_section.set_status("Procesando...")
        self.actions_section.disable_buttons(True)
        
        # Simulación de procesamiento
        showInfo(
            f"Configuración '{form_data['basic']['name']}' guardada exitosamente.\n"
            f"Query: {form_data['search']['search_query']}\n"
            f"Grupos configurados: {len(form_data['grouping']['groups'])}"
        )
        
        self.actions_section.set_status("Configuración completada")
        self.actions_section.disable_buttons(False)
        
        # Cerrar el diálogo
        self.accept()
    
    def on_test_clicked(self):
        """Maneja el clic en el botón probar"""
        if not self.validate_form():
            return
        
        form_data = self.get_form_data()
        
        # Aquí iría la lógica para probar la configuración
        self.actions_section.set_status("Probando configuración...")
        
        showInfo(
            f"Prueba de configuración '{form_data['basic']['name']}'.\n"
            f"La consulta buscaría: {form_data['search']['search_query']}\n"
            f"Se crearían {len(form_data['grouping']['groups'])} grupos de mazos."
        )
        
        self.actions_section.set_status("Prueba completada")
    
    def on_cancel_clicked(self):
        """Maneja el clic en el botón cancelar"""
        self.reject()
    
    def clear_form(self):
        """Limpia todos los campos del formulario"""
        self.basic_section.clear_data()
        self.search_section.clear_data()
        self.grouping_section.clear_data()
        self.actions_section.clear_data()