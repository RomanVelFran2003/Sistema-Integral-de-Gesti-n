"""
cliente.py - Clase que representa a un cliente del sistema.
"""
from typing import Any
from entidad_base import EntidadBase
from excepciones import ClienteInvalidoError, ParametroObligatorioError
import re

class Cliente(EntidadBase):
    """
    Clase que representa a un cliente del sistema con validaciones robustas.
    """
    
    def __init__(self, nombre: str, documento: str, contacto: str, cliente_id: int = None):
        """
        Inicializa un cliente con validaciones estrictas.
        
        Args:
            nombre: Nombre completo del cliente
            documento: Número de documento de identidad
            contacto: Correo electrónico de contacto
            cliente_id: ID único del cliente (opcional)
            
        Raises:
            ParametroObligatorioError: Si algún parámetro obligatorio está vacío
            ClienteInvalidoError: Si los datos no cumplen con el formato correcto
        """
        # Validaciones de parámetros obligatorios
        if not nombre or not nombre.strip():
            raise ParametroObligatorioError("El nombre es obligatorio")
        
        if not documento or not documento.strip():
            raise ParametroObligatorioError("El documento es obligatorio")
        
        if not contacto or not contacto.strip():
            raise ParametroObligatorioError("El contacto es obligatorio")
        
        # Validaciones de formato
        nombre_limpio = nombre.strip()
        if len(nombre_limpio) < 2:
            raise ClienteInvalidoError("El nombre debe tener al menos 2 caracteres")
        
        documento_limpio = documento.strip()
        if not documento_limpio.isdigit():
            raise ClienteInvalidoError("El documento debe contener solo números")
        
        if len(documento_limpio) < 7 or len(documento_limpio) > 10:
            raise ClienteInvalidoError("El documento debe tener entre 7 y 10 dígitos")
        
        contacto_limpio = contacto.strip()
        patron_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(patron_email, contacto_limpio):
            raise ClienteInvalidoError("El contacto debe ser un correo electrónico válido")
        
        # Asignar valores
        self.__nombre = nombre_limpio
        self.__documento = documento_limpio
        self.__contacto = contacto_limpio
        self.__id = cliente_id if cliente_id else hash(documento_limpio)  # Generar ID si no se proporciona
    
    @property
    def nombre(self) -> str:
        """Nombre del cliente."""
        return self.__nombre
    
    @property
    def documento(self) -> str:
        """Documento de identidad del cliente."""
        return self.__documento
    
    @property
    def contacto(self) -> str:
        """Correo electrónico de contacto."""
        return self.__contacto
    
    @property
    def id(self) -> int:
        """ID único del cliente."""
        return self.__id
    
    def __str__(self) -> str:
        return f"Cliente(ID: {self.__id}, Nombre: {self.__nombre}, Documento: {self.__documento}, Contacto: {self.__contacto})"
    
    def to_dict(self) -> dict[str, Any]:
        """
        Convierte el cliente a un diccionario.
        
        Returns:
            dict: Datos del cliente
        """
        return {
            'id': self.__id,
            'nombre': self.__nombre,
            'documento': self.__documento,
            'contacto': self.__contacto
        }