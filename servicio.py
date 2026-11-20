"""
servicio.py - Clase abstracta para servicios.
"""
from abc import ABC, abstractmethod
from typing import Any
from entidad_base import EntidadBase
from excepciones import ParametroObligatorioError, CalculoCostoError

class Servicio(EntidadBase, ABC):
    """
    Clase abstracta para servicios del sistema.
    """
    
    def __init__(self, id_servicio: str, nombre: str, costo_base: float):
        """
        Inicializa un servicio con validaciones.
        
        Args:
            id_servicio: ID único del servicio
            nombre: Nombre del servicio
            costo_base: Costo base del servicio
            
        Raises:
            ParametroObligatorioError: Si algún parámetro obligatorio está vacío
            CalculoCostoError: Si el costo base es inválido
        """
        if not id_servicio or not id_servicio.strip():
            raise ParametroObligatorioError("El ID del servicio es obligatorio")
        
        if not nombre or not nombre.strip():
            raise ParametroObligatorioError("El nombre del servicio es obligatorio")
        
        if costo_base < 0:
            raise CalculoCostoError("El costo base no puede ser negativo")
        
        self._id_servicio = id_servicio.strip()
        self._nombre = nombre.strip()
        self._costo_base = float(costo_base)
    
    @property
    def id_servicio(self) -> str:
        """ID del servicio."""
        return self._id_servicio
    
    @property
    def nombre(self) -> str:
        """Nombre del servicio."""
        return self._nombre
    
    @property
    def costo_base(self) -> float:
        """Costo base del servicio."""
        return self._costo_base
    
    @abstractmethod
    def calcular_costo(self, duracion: int, **kwargs) -> float:
        """
        Calcula el costo del servicio.
        
        Args:
            duración: Duración del servicio en horas
            **kwargs: Parámetros adicionales específicos de cada servicio
            
        Returns:
            float: Costo calculado
            
        Raises:
            CalculoCostoError: Si la duración es inválida
        """
        if duracion <= 0:
            raise CalculoCostoError("La duración debe ser positiva")
        
        return self._costo_base * duracion
    
    def __str__(self) -> str:
        return f"Servicio(ID: {self._id_servicio}, Nombre: {self._nombre}, Costo base: ${self._costo_base:,.2f})"
    
    def to_dict(self) -> dict[str, Any]:
        """
        Convierte el servicio a un diccionario.
        
        Returns:
            dict: Datos del servicio
        """
        return {
            'id_servicio': self._id_servicio,
            'nombre': self._nombre,
            'costo_base': self._costo_base
        }