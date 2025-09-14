from .base_section_abs import BaseSection
from ...constants.ui import UIConstants

class ActionsSection(BaseSection):
    """Sección para los botones de acción del formulario"""
    
    def __init__(self, parent=None):
        super().__init__(UIConstants.SECTION_ACTIONS, parent)
        self.create_button = None
        self.cancel_button = None
        self.status_label = None
        self.create_widgets()
        self.setup_layout()
    
    def create_widgets(self):
        """Crea los widgets para la sección de acciones"""
        # Botón principal para crear mazos
        self.create_button = self._create_styled_button(
            UIConstants.BUTTON_CREATE_FILTERED_DECKS,
            'extended'
        )
        
        # Botón para cancelar
        self.cancel_button = self._create_styled_button(
            UIConstants.BUTTON_CANCEL,
            'normal'
        )
        self.cancel_button.setObjectName(UIConstants.OBJECT_NAME_SECONDARY)
        
        # Etiqueta de estado
        self.status_label = self._create_styled_label(
            UIConstants.STATUS_READY,
            UIConstants.OBJECT_NAME_STATUS_LABEL
        )
    
    def setup_layout(self):
        """Configura el layout de la sección"""
        # Layout horizontal para botones
        button_layout = self._create_horizontal_layout()
        button_layout.addWidget(self.create_button)
        button_layout.addWidget(self.cancel_button)
        #button_layout.addStretch()
        
        # Agregar botones y etiqueta de estado al layout principal
        self.layout.addLayout(button_layout)
        self.layout.addWidget(self.status_label)
    
    def connect_create_action(self, handler):
        """Conecta el botón de crear con el handler proporcionado"""
        if self.create_button:
            self.create_button.clicked.connect(handler)
    
    def connect_test_action(self, handler):
        """Conecta el botón de prueba con el handler proporcionado"""
        # Nota: Actualmente no hay botón de prueba, pero el método está definido para compatibilidad
        pass
    
    def connect_cancel_action(self, handler):
        """Conecta el botón de cancelar con el handler proporcionado"""
        if self.cancel_button:
            self.cancel_button.clicked.connect(handler)
    
    def set_create_button_text(self, text: str):
        """Establece el texto del botón de crear"""
        if self.create_button:
            self.create_button.setText(text)
    
    def clear_data(self):
        """Limpia los datos de la sección (no aplica para acciones)"""
        pass