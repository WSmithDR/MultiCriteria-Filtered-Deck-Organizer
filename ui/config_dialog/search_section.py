from typing import Dict, Any
from aqt.qt import QLineEdit, QLabel, QTextEdit, QFormLayout, QVBoxLayout, Qt
from .base_section import BaseSection
from ...constants import UIConstants

class SearchSection(BaseSection):
    """Sección para la consulta de búsqueda de tarjetas"""
    
    def __init__(self, parent=None):
        super().__init__("Búsqueda - WHERE", parent)
        self.search_input = None
        self.example_label = None
        self.create_widgets()
        self.setup_layout()
    
    def create_widgets(self):
        """Crea los widgets para la sección de búsqueda"""
        # Campo de texto para la búsqueda
        self.search_input = QTextEdit()
        self.search_input.setPlaceholderText(
            "Ej: deck:Current OR tag:important is:due"
        )
        self.search_input.setMaximumHeight(100)
        self.search_input.setStyleSheet(UIConstants.INPUT_STYLE)
        
        # Etiqueta de ejemplos
        self.example_label = QLabel(
            "<b>Ejemplos:</b><br>"
            "• <code>deck:Spanish</code> - Mazo específico<br>"
            "• <code>is:due</code> - Tarjetas pendientes<br>"
            "• <code>tag:important</code> - Por etiqueta<br>"
            "• <code>Front:*vocabulary*</code> - Por contenido<br>"
            "• <code>is:rated</code> - Tarjetas calificadas"
        )
        self.example_label.setWordWrap(True)
        self.example_label.setStyleSheet(
            "color: #666666; font-size: 11px; padding: 5px; "
            "background-color: #f5f5f5; border-radius: 3px;"
        )
        self.example_label.setTextFormat(Qt.TextFormat.RichText)
        self.example_label.setOpenExternalLinks(False)
    
    def setup_layout(self):
        """Configura el layout de la sección"""
        # Layout principal
        main_layout = QVBoxLayout()
        
        # Form layout para el campo de búsqueda
        form_layout = QFormLayout()
        form_layout.addRow("Consulta de búsqueda:", self.search_input)
        
        main_layout.addLayout(form_layout)
        main_layout.addWidget(self.example_label)
        
        # Agregar al layout de la sección
        self.layout.addLayout(main_layout)
    
    def get_data(self) -> Dict[str, Any]:
        """Retorna los datos de la sección"""
        return {
            "search_query": self.search_input.toPlainText().strip()
        }
    
    def set_data(self, data: Dict[str, Any]):
        """Establece los datos de la sección (para edición)"""
        if "search_query" in data:
            self.search_input.setText(str(data["search_query"]))
    
    def clear_data(self):
        """Limpia los datos de la sección"""
        self.search_input.clear()
    
    def is_valid(self) -> bool:
        """Valida que la consulta no esté vacía"""
        query = self.search_input.toPlainText().strip()
        return len(query) > 0
    
    def get_validation_errors(self) -> list:
        """Retorna errores de validación"""
        errors = []
        if not self.is_valid():
            errors.append("La consulta de búsqueda es obligatoria")
        return errors
