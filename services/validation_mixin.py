from abc import abstractmethod
from typing import List


class ValidationMixin:
    """Mixin class that provides validation functionality"""
    
    @abstractmethod
    def validate(self) -> List[str]:
        """
        Valida los datos de la sección
        
        Returns:
            Lista de mensajes de error. Vacía si la validación es exitosa
        """
        pass
    
    def is_valid(self) -> bool:
        """
        Verifica si los datos son válidos
        
        Returns:
            True si no hay errores de validación, False en caso contrario
        """
        return len(self.validate()) == 0
    
    def get_validation_errors(self) -> List[str]:
        """
        Retorna la lista de errores de validación
        
        Returns:
            Lista de mensajes de error
        """
        return self.validate()
