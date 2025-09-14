from enum import Enum

class GroupingCombination(Enum):
    """Formas de combinar múltiples criterios de agrupamiento"""
    SINGLE = "single"  # Solo un criterio
    NESTED = "nested"  # Agrupamiento jerárquico
    PARALLEL = "parallel"  # Múltiples grupos independientes

