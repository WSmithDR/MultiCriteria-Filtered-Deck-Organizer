from typing import Dict, Any
from aqt.qt import QTextEdit, QFormLayout, QVBoxLayout, Qt
from .base_section import BaseSection
from ...constants.ui import UIConstants

class SearchSection(BaseSection):
    """Sección para la consulta de búsqueda de tarjetas"""
    
    def __init__(self, parent=None):
        super().__init__(UIConstants.SECTION_SEARCH, parent)
        self.search_input = None
        self.example_label = None
        self.create_widgets()
        self.setup_layout()
    
    def create_widgets(self):
        """Crea los widgets para la sección de búsqueda"""
        # Campo de texto para la búsqueda
        self.search_input = self._create_styled_input(
            QTextEdit,
            UIConstants.PLACEHOLDER_SEARCH_EXAMPLE,
            UIConstants.TEXT_EDIT_MAX_HEIGHT
        )
        
        # Etiqueta de ejemplos
        self.example_label = self._create_styled_label(
            UIConstants.SEARCH_EXAMPLES_TITLE +
            UIConstants.SEARCH_EXAMPLE_DECK +
            UIConstants.SEARCH_EXAMPLE_DUE +
            UIConstants.SEARCH_EXAMPLE_TAG +
            UIConstants.SEARCH_EXAMPLE_CONTENT +
            UIConstants.SEARCH_EXAMPLE_RATED,
            UIConstants.OBJECT_NAME_EXAMPLE_LABEL
        )
        self.example_label.setTextFormat(Qt.TextFormat.RichText)
        self.example_label.setOpenExternalLinks(False)
    
    def setup_layout(self):
        """Configura el layout de la sección"""
        # Layout principal
        main_layout = self._create_vertical_layout()
        
        # Form layout para el campo de búsqueda
        form_layout = self._create_form_layout()
        form_layout.addRow(UIConstants.LABEL_SEARCH_QUERY, self.search_input)
        
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
