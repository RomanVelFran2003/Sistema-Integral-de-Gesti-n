"""
reserva_sala.py - Servicio de reserva de salas.
"""
from servicio import Servicio
from excepciones import CalculoCostoError, ParametroObligatorioError

class ReservaSala(Servicio):
    """
    Servicio de reserva de salas con capacidades específicas.
    """
    
    def __init__(self, id_servicio: str, nombre: str, costo_base: float, capacidad: int):
        """
        Inicializa un servicio de reserva de sala.
        
        Args:
            id_servicio: ID del servicio
            nombre: Nombre del servicio
            costo_base: Costo base por hora
            capacidad: Capacidad máxima de la sala
            
        Raises:
            CalculoCostoError: Si la capacidad es inválida
        """
        super().__init__(id_servicio, nombre, costo_base)
        
        if capacidad <= 0:
            raise CalculoCostoError("La capacidad debe ser positiva")
        
        self._capacidad = int(capacidad)
    
    @property
    def capacidad(self) -> int:
        """Capacidad de la sala."""
        return self._capacidad
    
    def calcular_costo(self, duracion: int, impuesto: float = 0.1, descuento: float = 0.0, personas: int = 1) -> float:
        """
        Calcula el costo de la reserva de sala con impuestos y descuentos.
        
        Args:
            duración: Duración en horas
            impuesto: Porcentaje de impuesto (0.1 = 10%)
            descuento: Porcentaje de descuento (0.05 = 5%)
            personas: Número de personas (para validación de capacidad)
            
        Returns:
            float: Costo calculado
            
        Raises:
            CalculoCostoError: Si la duración es inválida o personas exceden capacidad
        """
        # Llamar al método del padre para validación básica
        super().calcular_costo(duracion)
        
        if personas > self._capacidad:
            raise CalculoCostoError(f"El número de personas ({personas}) excede la capacidad de la sala ({self._capacidad})")
        
        costo_base = self._costo_base * duracion
        costo_con_impuesto = costo_base * (1 + impuesto)
        costo_final = costo_con_impuesto * (1 - descuento)
        
        return round(costo_final, 2)
    
    def __str__(self) -> str:
        return f"ReservaSala(ID: {self._id_servicio}, Nombre: {self._nombre}, Capacidad: {self._capacidad}, Costo base: ${self._costo_base:,.2f})"
    
    def to_dict(self) -> dict[str, Any]:
        """
        Convierte el servicio a un diccionario.
        
        Returns:
            dict: Datos del servicio
        """
        datos = super().to_dict()
        datos['capacidad'] = self._capacidad
        datos['tipo'] = 'ReservaSala'
        return datos