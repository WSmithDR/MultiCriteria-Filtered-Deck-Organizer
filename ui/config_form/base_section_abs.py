from abc import abstractmethod
from aqt.qt import QGroupBox
from ...styles import styles
from ..factories import WidgetFactory, LayoutFactory

class BaseSection(QGroupBox, LayoutFactory, WidgetFactory):
    """Clase base para todas las secciones del formulario"""
    
    def __init__(self, title: str, parent=None):
        super().__init__(title, parent)
        self._setup_ui()
        self._apply_styles()
    
    def _setup_ui(self):
        """Configura la UI básica de la sección"""
        self.layout = self._create_section_layout()
        self.setLayout(self.layout)
    
    def _apply_styles(self):
        """Aplica estilos CSS a la sección"""
        self.setStyleSheet(styles.GROUPBOX)

    @abstractmethod
    def create_widgets(self):
        """Aqui se crean los widgets de la seccion"""
        pass
    
    @abstractmethod
    def setup_layout(self):
        """Aqui es donde se indica cómo se van ubicar los widgets creados en el layout"""
        pass