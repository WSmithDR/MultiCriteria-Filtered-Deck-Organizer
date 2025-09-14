from typing import Dict, Any
from aqt.qt import QLineEdit, QFormLayout
from .base_section import BaseSection
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
    
    def get_data(self) -> Dict[str, Any]:
        """Retorna los datos de la sección"""
        return {
            "name": self.name_input.text().strip()
        }
    
    def set_data(self, data: Dict[str, Any]):
        """Establece los datos de la sección (para edición)"""
        if "name" in data:
            self.name_input.setText(str(data["name"]))
    
    def clear_data(self):
        """Limpia los datos de la sección"""
        self.name_input.clear()
    
    def validate(self) -> list:
        """Valida los datos de la sección"""
        errors = []
        name = self.name_input.text().strip()
        if len(name) == 0:
            errors.append("El nombre de la configuración es obligatorio")
        return errors
