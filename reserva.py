"""
reserva.py - Clase que representa una reserva en el sistema.
"""
from datetime import date, datetime
from typing import Any
from cliente import Cliente
from servicio import Servicio
from excepciones import ReservaInvalidaError, DuracionInvalidaError, EstadoReservaError, ParametroObligatorioError

class Reserva:
    """
    Clase que representa una reserva de un servicio por un cliente.
    """
    
    ESTADOS_VALIDOS = ['pendiente', 'confirmada', 'cancelada', 'completada']
    
    def __init__(self, cliente: Cliente, servicio: Servicio, duración: int, fecha: date):
        """
        Inicializa una reserva con validaciones estrictas.
        
        Args:
            cliente: Cliente que realiza la reserva
            servicio: Servicio que se reserva
            duración: Duración de la reserva en horas
            fecha: Fecha de la reserva
            
        Raises:
            ParametroObligatorioError: Si algún parámetro obligatorio está vacío
            ReservaInvalidaError: Si los parámetros no son válidos
            DuracionInvalidaError: Si la duración es inválida
        """
        # Validaciones de parámetros obligatorios
        if not cliente:
            raise ParametroObligatorioError("El cliente es obligatorio")
        
        if not servicio:
            raise ParametroObligatorioError("El servicio es obligatorio")
        
        if not duración:
            raise ParametroObligatorioError("La duración es obligatoria")
        
        if not fecha:
            raise ParametroObligatorioError("La fecha es obligatoria")
        
        # Validaciones de tipo
        if not isinstance(cliente, Cliente):
            raise ReservaInvalidaError("El cliente debe ser una instancia de Cliente")
        
        if not isinstance(servicio, Servicio):
            raise ReservaInvalidaError("El servicio debe ser una instancia de Servicio")
        
        if not isinstance(fecha, date):
            raise ReservaInvalidaError("La fecha debe ser un objeto date válido")
        
        # Validación de duración
        if duración <= 0:
            raise DuracionInvalidaError("La duración debe ser positiva")
        
        # Validación de fecha (no puede ser en el pasado)
        if fecha < date.today():
            raise ReservaInvalidaError("No se pueden hacer reservas en fechas pasadas")
        
        # Asignar valores
        self._cliente = cliente
        self._servicio = servicio
        self._duración = int(duración)
        self._fecha = fecha
        self._estado = 'pendiente'
        self._fecha_creacion = datetime.now()
        self._costo_calculado = None
    
    @property
    def cliente(self) -> Cliente:
        """Cliente que realizó la reserva."""
        return self._cliente
    
    @property
    def servicio(self) -> Servicio:
        """Servicio reservado."""
        return self._servicio
    
    @property
    def duración(self) -> int:
        """Duración de la reserva en horas."""
        return self._duración
    
    @property
    def fecha(self) -> date:
        """Fecha de la reserva."""
        return self._fecha
    
    @property
    def estado(self) -> str:
        """Estado actual de la reserva."""
        return self._estado
    
    @property
    def fecha_creacion(self) -> datetime:
        """Fecha y hora de creación de la reserva."""
        return self._fecha_creacion
    
    def confirmar(self) -> bool:
        """
        Confirma la reserva.
        
        Returns:
            bool: True si la confirmación fue exitosa
            
        Raises:
            EstadoReservaError: Si la reserva no puede ser confirmada
        """
        if self._estado == 'cancelada':
            raise EstadoReservaError("No se puede confirmar una reserva cancelada")
        
        if self._estado == 'completada':
            raise EstadoReservaError("No se puede confirmar una reserva ya completada")
        
        self._estado = 'confirmada'
        return True
    
    def cancelar(self) -> bool:
        """
        Cancela la reserva.
        
        Returns:
            bool: True si la cancelación fue exitosa
            
        Raises:
            EstadoReservaError: Si la reserva no puede ser cancelada
        """
        if self._estado == 'cancelada':
            raise EstadoReservaError("La reserva ya está cancelada")
        
        if self._estado == 'completada':
            raise EstadoReservaError("No se puede cancelar una reserva ya completada")
        
        self._estado = 'cancelada'
        return True
    
    def completar(self) -> bool:
        """
        Marca la reserva como completada.
        
        Returns:
            bool: True si la completitud fue exitosa
            
        Raises:
            EstadoReservaError: Si la reserva no puede ser completada
        """
        if self._estado == 'cancelada':
            raise EstadoReservaError("No se puede completar una reserva cancelada")
        
        if self._estado == 'completada':
            raise EstadoReservaError("La reserva ya está completada")
        
        self._estado = 'completada'
        return True
    
    def calcular_costo(self, **kwargs) -> float:
        """
        Calcula el costo de la reserva usando el servicio correspondiente.
        
        Args:
            **kwargs: Parámetros adicionales para el cálculo del servicio
            
        Returns:
            float: Costo calculado de la reserva
            
        Raises:
            ReservaInvalidaError: Si hay error en el cálculo del costo
        """
        try:
            self._costo_calculado = self._servicio.calcular_costo(self._duración, **kwargs)
            return self._costo_calculado
        except Exception as e:
            raise ReservaInvalidaError(f"Error calculando el costo de la reserva: {str(e)}") from e
    
    def __str__(self) -> str:
        return f"Reserva(Cliente: {self._cliente.nombre}, Servicio: {self._servicio.nombre}, Duración: {self._duración}h, Fecha: {self._fecha}, Estado: {self._estado})"
    
    def to_dict(self) -> dict[str, Any]:
        """
        Convierte la reserva a un diccionario.
        
        Returns:
            dict: Datos de la reserva
        """
        return {
            'cliente': self._cliente.to_dict(),
            'servicio': self._servicio.to_dict(),
            'duración': self._duración,
            'fecha': self._fecha.isoformat(),
            'estado': self._estado,
            'fecha_creacion': self._fecha_creacion.isoformat(),
            'costo_calculado': self._costo_calculado
        }