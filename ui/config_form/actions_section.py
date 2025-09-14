from typing import Dict, Any
from aqt.qt import QPushButton, QHBoxLayout, QLabel
from .base_section import BaseSection
from ...constants.ui import UIConstants
from ...styles import styles

class ActionsSection(BaseSection):
    """Sección para los botones de acción del formulario"""
    
    def __init__(self, parent=None):
        super().__init__(UIConstants.SECTION_ACTIONS, parent)
        self.create_button = None
        self.test_button = None
        self.cancel_button = None
        self.status_label = None
        self.create_widgets()
        self.setup_layout()
    
    def create_widgets(self):
        """Crea los widgets para la sección de acciones"""
        # Botón principal para crear mazos
        self.create_button = QPushButton(UIConstants.BUTTON_CREATE_FILTERED_DECKS)
        self.create_button.setStyleSheet(styles.BUTTON)
        self.create_button.setFixedWidth(UIConstants.BUTTON_WIDTH + 40)
        
        # Botón para probar la configuración
        self.test_button = QPushButton(UIConstants.BUTTON_TEST_CONFIGURATION)
        self.test_button.setStyleSheet(styles.BUTTON)
        self.test_button.setFixedWidth(UIConstants.BUTTON_WIDTH + 40)
        
        # Botón para cancelar
        self.cancel_button = QPushButton(UIConstants.BUTTON_CANCEL)
        self.cancel_button.setObjectName("secondary")
        self.cancel_button.setStyleSheet(styles.BUTTON)
        self.cancel_button.setFixedWidth(UIConstants.BUTTON_WIDTH)
        
        # Etiqueta de estado
        self.status_label = QLabel(UIConstants.STATUS_READY)
        self.status_label.setStyleSheet("color: #666666; font-style: italic;")
    
    def setup_layout(self):
        """Configura el layout de la sección"""
        # Layout horizontal para botones
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.create_button)
        button_layout.addWidget(self.test_button)
        button_layout.addWidget(self.cancel_button)
        button_layout.addStretch()
        
        # Agregar botones y etiqueta de estado al layout principal
        self.layout.addLayout(button_layout)
        self.layout.addWidget(self.status_label)
    
    def get_data(self) -> Dict[str, Any]:
        """Retorna los datos de la sección (en este caso, vacío)"""
        return {}
    
    def set_data(self, data: Dict[str, Any]):
        """Establece los datos de la sección (para edición)"""
        pass  # No hay datos que establecer en esta sección
    
    def clear_data(self):
        """Limpia los datos de la sección"""
        self.set_status("✅ Listo para crear mazos filtrados")
    
    def set_status(self, message: str, is_error: bool = False):
        """Establece el mensaje de estado"""
        self.status_label.setText(message)
        if is_error:
            self.status_label.setStyleSheet("color: #d32f2f; font-weight: bold;")
        else:
            self.status_label.setStyleSheet("color: #666666; font-style: italic;")
    
    def connect_create_action(self, callback):
        """Conecta el botón de crear a una función callback"""
        self.create_button.clicked.connect(callback)
    
    def connect_test_action(self, callback):
        """Conecta el botón de probar a una función callback"""
        self.test_button.clicked.connect(callback)
    
    def connect_cancel_action(self, callback):
        """Conecta el botón de cancelar a una función callback"""
        self.cancel_button.clicked.connect(callback)
    
    def set_create_button_text(self, text: str):
        """Cambia el texto del botón de crear (para modo edición)"""
        self.create_button.setText(text)
    
    def disable_buttons(self, disabled: bool = True):
        """Habilita o deshabilita todos los botones"""
        self.create_button.setDisabled(disabled)
        self.test_button.setDisabled(disabled)
        self.cancel_button.setDisabled(disabled)
