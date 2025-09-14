from aqt.qt import QFormLayout, QHBoxLayout, QVBoxLayout
from ...constants import UIConstants


class LayoutFactory:
    """Factory class for creating layouts with standard configurations"""
    
    @staticmethod
    def create_form_layout() -> QFormLayout:
        """
        Crea un QFormLayout con márgenes y espaciado estándar
        
        Returns:
            QFormLayout configurado
        """
        layout = QFormLayout()
        return layout
    
    @staticmethod
    def create_horizontal_layout() -> QHBoxLayout:
        """
        Crea un QHBoxLayout con espaciado estándar
        
        Returns:
            QHBoxLayout configurado
        """
        layout = QHBoxLayout()
        return layout
    
    @staticmethod
    def create_vertical_layout() -> QVBoxLayout:
        """
        Crea un QVBoxLayout con márgenes y espaciado estándar
        
        Returns:
            QVBoxLayout configurado
        """
        layout = QVBoxLayout()
        return layout
    
    @staticmethod
    def create_section_layout() -> QVBoxLayout:
        """
        Crea un QVBoxLayout con márgenes y espaciado específicos para secciones
        
        Returns:
            QVBoxLayout configurado para secciones
        """
        layout = QVBoxLayout()
        layout.setContentsMargins(
            UIConstants.SECTION_MARGIN,
            UIConstants.SECTION_MARGIN,
            UIConstants.SECTION_MARGIN,
            UIConstants.SECTION_MARGIN
        )
        layout.setSpacing(UIConstants.SECTION_SPACING)
        return layout
