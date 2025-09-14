from abc import abstractmethod
from typing import Dict, Any


class DataManagementMixin:
    """Mixin class that provides data management functionality"""
    
    @abstractmethod
    def get_data(self) -> Dict[str, Any]:
        """
        Retorna los datos de la sección
        
        Returns:
            Diccionario con los datos de la sección
        """
        pass
    
    @abstractmethod
    def set_data(self, data: Dict[str, Any]):
        """
        Establece los datos de la sección
        
        Args:
            data: Diccionario con los datos a establecer
        """
        pass
    
    @abstractmethod
    def clear_data(self):
        """Limpia los datos de la sección"""
        pass
