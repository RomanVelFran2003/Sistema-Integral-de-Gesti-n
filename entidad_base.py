"""
entidad_base.py - Clase abstracta base para todas las entidades del sistema.
"""
from abc import ABC, abstractmethod
from typing import Any

class EntidadBase(ABC):
    """
    Clase abstracta que define la interfaz para todas las entidades del sistema.
    """
    
    @abstractmethod
    def __str__(self) -> str:
        """
        Representación en cadena de la entidad.
        
        Returns:
            str: Representación de la entidad
        """
        pass
    
    @abstractmethod
    def to_dict(self) -> dict[str, Any]:
        """
        Convierte la entidad a un diccionario.
        
        Returns:
            dict: Datos de la entidad
        """
        pass