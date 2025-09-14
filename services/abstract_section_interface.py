from abc import abstractmethod


class AbstractSectionInterface:
    """Abstract interface that all sections must implement"""
    
    @abstractmethod
    def create_widgets(self):
        """Crea los widgets para la sección"""
        pass
    
    @abstractmethod
    def setup_layout(self):
        """Configura el layout de la sección"""
        pass
