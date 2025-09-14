from typing import Dict, Any
from aqt.qt import QGroupBox, QVBoxLayout, QPushButton, QLabel, QFormLayout, QHBoxLayout
from ...constants import UIConstants,ButtonWidthType, LabelWordWrap
from ...styles import styles

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
        self.setStyleSheet(styles.GROUPBOX)
    
    # Métodos comunes para configuración de widgets
    def _create_styled_input(self, widget_class, placeholder_text=None, max_height=None):
        """Crea un widget de entrada con estilos comunes"""
        widget = widget_class()
        if placeholder_text:
            widget.setPlaceholderText(placeholder_text)
        if max_height:
            widget.setMaximumHeight(max_height)
        widget.setStyleSheet(styles.INPUT)
        return widget
    
    def _create_styled_button(self, text, width_type=ButtonWidthType.NORMAL):
        """Crea un botón con estilos comunes"""
        button = QPushButton(text)
        button.setStyleSheet(styles.BUTTON)
        
        if width_type == ButtonWidthType.EXTENDED:
            button.setFixedWidth(UIConstants.BUTTON_WIDTH_EXTENDED)
        else:
            button.setFixedWidth(UIConstants.BUTTON_WIDTH)
        
        return button
    
    def _create_styled_label(self, text, object_name=None, word_wrap=LabelWordWrap.ENABLED):
        """Crea una etiqueta con estilos comunes"""
        label = QLabel(text)
        label.setStyleSheet(styles.LABEL)
        
        if object_name:
            label.setObjectName(object_name)
        if word_wrap == LabelWordWrap.ENABLED:
            label.setWordWrap(True)
        else:
            label.setWordWrap(False)
        
        return label
    
    def _create_form_layout(self):
        """Crea un QFormLayout con márgenes y espaciado estándar"""
        layout = QFormLayout()
        return layout
    
    def _create_horizontal_layout(self):
        """Crea un QHBoxLayout con espaciado estándar"""
        layout = QHBoxLayout()
        return layout
    
    def _create_vertical_layout(self):
        """Crea un QVBoxLayout con márgenes y espaciado estándar"""
        layout = QVBoxLayout()
        return layout
    
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
