from aqt.qt import QLineEdit
from .base_section_abs import BaseSection
from ...constants.ui import UIConstants

class BasicConfigSection(BaseSection):
    """Sección para la configuración básica (nombre de la configuración)"""
    
    def __init__(self, parent=None):
        super().__init__(UIConstants.SECTION_BASIC_CONFIG, parent)
        self.name_input = None
        self.create_widgets()
        self.setup_layout()
    
    def create_widgets(self):
        """Crea los widgets para la sección de configuración básica"""
        self.name_input = self._create_styled_input(
            QLineEdit,
            UIConstants.PLACEHOLDER_CONFIG_NAME
        )
        
        # Etiqueta de descripción
        self.description_label = self._create_styled_label(
            UIConstants.LABEL_CONFIG_DESCRIPTION,
            UIConstants.OBJECT_NAME_DESCRIPTION_LABEL
        )
    
    def setup_layout(self):
        """Configura el layout de la sección"""
        # Usamos QFormLayout para mejor organización
        form_layout = self._create_form_layout()
        form_layout.addRow(UIConstants.LABEL_NAME, self.name_input)
        
        # Agregamos el form layout y la descripción al layout principal
        self.layout.addLayout(form_layout)
        self.layout.addWidget(self.description_label)
    