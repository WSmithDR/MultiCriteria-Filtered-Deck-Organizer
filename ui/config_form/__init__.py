from .basic_config_section import BasicConfigSection
from .search_section import SearchSection
from .grouping_section import GroupingSection
from .actions_section import ActionsSection


class ConfigForm:
    """Formulario de configuración para mazos filtrados - maneja datos, validación y secciones"""
    
    def __init__(self):
        self.setup_sections()
    
    def setup_sections(self):
        """Inicializa todas las secciones del formulario"""
        self.basic_section = BasicConfigSection()
        self.search_section = SearchSection()
        self.grouping_section = GroupingSection()
        self.actions_section = ActionsSection()
    
    def get_sections(self):
        """Retorna todas las secciones del formulario"""
        return [
            self.basic_section,
            self.search_section,
            self.grouping_section,
            self.actions_section
        ]
    
    def load_edit_data(self, edit_data):
        """Carga los datos para edición en todas las secciones"""
        if not edit_data:
            return
            
        # Cargar datos en cada sección
        if 'basic' in edit_data:
            self.basic_section.set_data(edit_data['basic'])
        
        if 'search' in edit_data:
            self.search_section.set_data(edit_data['search'])
        
        if 'grouping' in edit_data:
            self.grouping_section.set_data(edit_data['grouping'])
        
        # Cambiar texto del botón para modo edición
        self.actions_section.set_create_button_text("Actualizar Configuración")
    
    def validate_form(self) -> bool:
        """Valida todo el formulario y retorna True si es válido"""
        errors = []
        
        # Validar cada sección
        if not self.basic_section.is_valid():
            errors.extend(self.basic_section.get_validation_errors())
        
        if not self.search_section.is_valid():
            errors.extend(self.search_section.get_validation_errors())
        
        if not self.grouping_section.is_valid():
            errors.extend(self.grouping_section.get_validation_errors())
        
        return errors
    
    def get_validation_errors(self) -> list:
        """Retorna la lista de errores de validación"""
        return self.validate_form()
    
    def get_form_data(self) -> dict:
        """Retorna todos los datos del formulario"""
        return {
            'basic': self.basic_section.get_data(),
            'search': self.search_section.get_data(),
            'grouping': self.grouping_section.get_data()
        }
    
    def clear_form(self):
        """Limpia todos los campos del formulario"""
        self.basic_section.clear_data()
        self.search_section.clear_data()
        self.grouping_section.clear_data()
        self.actions_section.clear_data()
    
    def setup_connections(self, create_handler, test_handler, cancel_handler):
        """Configura las conexiones de señales y slots"""
        self.actions_section.connect_create_action(create_handler)
        self.actions_section.connect_test_action(test_handler)
        self.actions_section.connect_cancel_action(cancel_handler)
