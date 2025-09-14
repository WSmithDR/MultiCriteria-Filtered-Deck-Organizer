from typing import Dict, Any
from aqt.qt import QGroupBox, QVBoxLayout
from ...constants import UIConstants

class BaseSection(QGroupBox):
    """Clase base para todas las secciones del formulario"""
    
    def __init__(self, title: str, parent=None):
        super().__init__(title, parent)
        self._setup_ui()
        self._apply_styles()
    
    def _setup_ui(self):
        """Configura la UI básica de la sección"""
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(
            UIConstants.SECTION_MARGIN,
            UIConstants.SECTION_MARGIN,
            UIConstants.SECTION_MARGIN,
            UIConstants.SECTION_MARGIN
        )
        self.layout.setSpacing(UIConstants.SECTION_SPACING)
        self.setLayout(self.layout)
    
    def _apply_styles(self):
        """Aplica estilos CSS a la sección"""
        self.setStyleSheet(UIConstants.SECTION_STYLE)
    
    # Métodos abstractos implementados manualmente
    def create_widgets(self):
        """Crea los widgets para la sección. Debe ser implementado por subclases."""
        raise NotImplementedError("Subclasses must implement create_widgets()")
    
    def setup_layout(self):
        """Configura el layout de la sección. Debe ser implementado por subclases."""
        raise NotImplementedError("Subclasses must implement setup_layout()")
    
    def get_data(self) -> Dict[str, Any]:
        """Retorna los datos de la sección. Debe ser implementado por subclases."""
        raise NotImplementedError("Subclasses must implement get_data()")
    
    def set_data(self, data: Dict[str, Any]):
        """Establece los datos de la sección. Debe ser implementado por subclases."""
        raise NotImplementedError("Subclasses must implement set_data()")
    
    def validate(self) -> list:
        """Valida los datos de la sección. Debe ser implementado por subclases."""
        raise NotImplementedError("Subclasses must implement validate()")
    
    def clear_data(self):
        """Limpia los datos de la sección. Debe ser implementado por subclases."""
        raise NotImplementedError("Subclasses must implement clear_data()")
    
    def is_valid(self) -> bool:
        """Valida los datos de la sección. Por defecto retorna True"""
        return True
    
    def get_validation_errors(self) -> list:
        """Retorna una lista de errores de validación"""
        return []
