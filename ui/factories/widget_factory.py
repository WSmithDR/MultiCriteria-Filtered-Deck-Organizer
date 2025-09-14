from typing import Optional, Type
from aqt.qt import QPushButton, QLabel
from ...constants import UIConstants, ButtonWidthType, LabelWordWrap
from ...styles import styles


class WidgetFactory:
    """Factory class for creating styled UI widgets"""
    
    @staticmethod
    def create_styled_input(widget_class: Type, 
                          placeholder_text: Optional[str] = None, 
                          max_height: Optional[int] = None):
        """
        Crea un widget de entrada con estilos comunes
        
        Args:
            widget_class: Clase del widget a crear (QLineEdit, QTextEdit, etc.)
            placeholder_text: Texto de placeholder opcional
            max_height: Altura máxima opcional
            
        Returns:
            Widget configurado con estilos
        """
        widget = widget_class()
        if placeholder_text:
            widget.setPlaceholderText(placeholder_text)
        if max_height:
            widget.setMaximumHeight(max_height)
        widget.setStyleSheet(styles.INPUT)
        return widget
    
    @staticmethod
    def create_styled_button(text: str, 
                           width_type: ButtonWidthType = ButtonWidthType.NORMAL) -> QPushButton:
        """
        Crea un botón con estilos comunes
        
        Args:
            text: Texto del botón
            width_type: Tipo de ancho del botón
            
        Returns:
            Botón configurado con estilos
        """
        button = QPushButton(text)
        button.setStyleSheet(styles.BUTTON)
        
        if width_type == ButtonWidthType.EXTENDED:
            button.setFixedWidth(UIConstants.BUTTON_WIDTH_EXTENDED)
        else:
            button.setFixedWidth(UIConstants.BUTTON_WIDTH)
        
        return button
    
    @staticmethod
    def create_styled_label(text: str, 
                           object_name: Optional[str] = None, 
                           word_wrap: LabelWordWrap = LabelWordWrap.ENABLED) -> QLabel:
        """
        Crea una etiqueta con estilos comunes
        
        Args:
            text: Texto de la etiqueta
            object_name: Nombre del objeto para CSS (opcional)
            word_wrap: Configuración de word wrap
            
        Returns:
            Etiqueta configurada con estilos
        """
        label = QLabel(text)
        label.setStyleSheet(styles.LABEL)
        
        if object_name:
            label.setObjectName(object_name)
        if word_wrap == LabelWordWrap.ENABLED:
            label.setWordWrap(True)
        else:
            label.setWordWrap(False)
        
        return label
