from aqt.qt import QGroupBox
from ...constants import ButtonWidthType, LabelWordWrap
from ...styles import styles
from ..factories import WidgetFactory, LayoutFactory
from ...services import ValidationMixin, DataManagementMixin, AbstractSectionInterface

class BaseSection(QGroupBox, ValidationMixin, DataManagementMixin, AbstractSectionInterface):
    """Clase base para todas las secciones del formulario"""
    
    def __init__(self, title: str, parent=None):
        super().__init__(title, parent)
        self._setup_ui()
        self._apply_styles()
    
    def _setup_ui(self):
        """Configura la UI básica de la sección"""
        self.layout = LayoutFactory.create_section_layout()
        self.setLayout(self.layout)
    
    def _apply_styles(self):
        """Aplica estilos CSS a la sección"""
        self.setStyleSheet(styles.GROUPBOX)
    
    # Métodos comunes para configuración de widgets - delegados a WidgetFactory
    def _create_styled_input(self, widget_class, placeholder_text=None, max_height=None):
        """Crea un widget de entrada con estilos comunes"""
        return WidgetFactory.create_styled_input(widget_class, placeholder_text, max_height)
    
    def _create_styled_button(self, text, width_type=ButtonWidthType.NORMAL):
        """Crea un botón con estilos comunes"""
        return WidgetFactory.create_styled_button(text, width_type)
    
    def _create_styled_label(self, text, object_name=None, word_wrap=LabelWordWrap.ENABLED):
        """Crea una etiqueta con estilos comunes"""
        return WidgetFactory.create_styled_label(text, object_name, word_wrap)
    
    # Métodos comunes para configuración de layouts - delegados a LayoutFactory
    def _create_form_layout(self):
        """Crea un QFormLayout con márgenes y espaciado estándar"""
        return LayoutFactory.create_form_layout()
    
    def _create_horizontal_layout(self):
        """Crea un QHBoxLayout con espaciado estándar"""
        return LayoutFactory.create_horizontal_layout()
    
    def _create_vertical_layout(self):
        """Crea un QVBoxLayout con márgenes y espaciado estándar"""
        return LayoutFactory.create_vertical_layout()