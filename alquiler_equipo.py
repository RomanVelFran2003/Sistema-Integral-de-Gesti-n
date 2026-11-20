"""
alquiler_equipo.py - Servicio de alquiler de equipos.
"""
from servicio import Servicio
from excepciones import CalculoCostoError, ParametroObligatorioError

class AlquilerEquipo(Servicio):
    """
    Servicio de alquiler de equipos con gestión de estado.
    """
    
    def __init__(self, id_servicio: str, nombre: str, costo_base: float, equipo: str, estado: str = 'disponible'):
        """
        Inicializa un servicio de alquiler de equipo.
        
        Args:
            id_servicio: ID del servicio
            nombre: Nombre del servicio
            costo_base: Costo base por hora de alquiler
            equipo: Descripción del equipo
            estado: Estado del equipo ('disponible', 'no disponible', 'mantenimiento')
            
        Raises:
            ParametroObligatorioError: Si el equipo no se especifica
            CalculoCostoError: Si el estado no es válido
        """
        super().__init__(id_servicio, nombre, costo_base)
        
        if not equipo or not equipo.strip():
            raise ParametroObligatorioError("La descripción del equipo es obligatoria")
        
        estados_validos = ['disponible', 'no disponible', 'mantenimiento']
        if estado not in estados_validos:
            raise CalculoCostoError(f"Estado inválido. Debe ser uno de: {estados_validos}")
        
        self._equipo = equipo.strip()
        self._estado = estado
    
    @property
    def equipo(self) -> str:
        """Descripción del equipo."""
        return self._equipo
    
    @property
    def estado(self) -> str:
        """Estado actual del equipo."""
        return self._estado
    
    def cambiar_estado(self, nuevo_estado: str) -> None:
        """
        Cambia el estado del equipo.
        
        Args:
            nuevo_estado: Nuevo estado del equipo
            
        Raises:
            CalculoCostoError: Si el estado no es válido
        """
        estados_validos = ['disponible', 'no disponible', 'mantenimiento']
        if nuevo_estado not in estados_validos:
            raise CalculoCostoError(f"Estado inválido. Debe ser uno de: {estados_validos}")
        
        self._estado = nuevo_estado
    
    def calcular_costo(self, duracion: int, daño: bool = False, limpieza: bool = False) -> float:
        """
        Calcula el costo del alquiler de equipo con recargos adicionales.
        
        Args:
            duración: Duración en horas
            daño: Si hubo daños al equipo
            limpieza: Si requiere limpieza adicional
            
        Returns:
            float: Costo calculado
            
        Raises:
            CalculoCostoError: Si la duración es inválida
        """
        # Llamar al método del padre para validación básica
        super().calcular_costo(dacion)
        
        costo_base = self._costo_base * duracion
        
        # Recargos adicionales
        if daño:
            costo_base *= 1.5  # 50% de recargo por daños
        if limpieza:
            costo_base += 25000  # Recargo fijo por limpieza
        
        return round(costo_base, 2)
    
    def __str__(self) -> str:
        return f"AlquilerEquipo(ID: {self._id_servicio}, Equipo: {self._equipo}, Estado: {self._estado}, Costo base: ${self._costo_base:,.2f})"
    
    def to_dict(self) -> dict[str, Any]:
        """
        Convierte el servicio a un diccionario.
        
        Returns:
            dict: Datos del servicio
        """
        datos = super().to_dict()
        datos['equipo'] = self._equipo
        datos['estado'] = self._estado
        datos['tipo'] = 'AlquilerEquipo'
        return datos