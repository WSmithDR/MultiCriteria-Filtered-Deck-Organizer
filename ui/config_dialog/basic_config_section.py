from typing import Dict, Any
from aqt.qt import QLineEdit, QLabel, QFormLayout
from .base_section import BaseSection
from ...constants import UIConstants

class BasicConfigSection(BaseSection):
    """Sección para la configuración básica (nombre de la configuración)"""
    
    def __init__(self, parent=None):
        super().__init__("Configuración Básica", parent)
        self.name_input = None
        self.create_widgets()
        self.setup_layout()
    
    def create_widgets(self):
        """Crea los widgets para la sección de configuración básica"""
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Ingrese el nombre de la configuración...")
        self.name_input.setStyleSheet(UIConstants.INPUT_STYLE)
        
        # Etiqueta de descripción
        description_label = QLabel(
            "Nombre que identificará esta configuración de mazos filtrados"
        )
        description_label.setWordWrap(True)
        description_label.setStyleSheet("color: #666666; font-size: 12px;")
        
        self.description_label = description_label
    
    def setup_layout(self):
        """Configura el layout de la sección"""
        # Usamos QFormLayout para mejor organización
        form_layout = QFormLayout()
        form_layout.addRow("Nombre:", self.name_input)
        
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
    
    def is_valid(self) -> bool:
        """Valida que el nombre no esté vacío"""
        name = self.name_input.text().strip()
        return len(name) > 0
    
    def get_validation_errors(self) -> list:
        """Retorna errores de validación"""
        errors = []
        if not self.is_valid():
            errors.append("El nombre de la configuración es obligatorio")
        return errors
