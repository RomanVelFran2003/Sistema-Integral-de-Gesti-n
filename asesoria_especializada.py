"""
asesoria_especializada.py - Servicio de asesorías especializadas.
"""
from servicio import Servicio
from excepciones import CalculoCostoError, ParametroObligatorioError

class AsesoriaEspecializada(Servicio):
    """
    Servicio de asesorías especializadas con temáticas específicas.
    """
    
    def __init__(self, id_servicio: str, nombre: str, costo_base: float, temática: str, duración_maxima: int):
        """
        Inicializa un servicio de asesoría especializada.
        
        Args:
            id_servicio: ID del servicio
            nombre: Nombre del servicio
            costo_base: Costo base por hora
            temática: Temática de la asesoría
            duración_maxima: Duración máxima en horas
            
        Raises:
            ParametroObligatorioError: Si la temática no se especifica
            CalculoCostoError: Si la duración máxima es inválida
        """
        super().__init__(id_servicio, nombre, costo_base)
        
        if not temática or not temática.strip():
            raise ParametroObligatorioError("La temática de la asesoría es obligatoria")
        
        if duración_maxima <= 0:
            raise CalculoCostoError("La duración máxima debe ser positiva")
        
        self._temática = temática.strip()
        self._duración_maxima = int(duración_maxima)
    
    @property
    def temática(self) -> str:
        """Temática de la asesoría."""
        return self._temática
    
    @property
    def duración_maxima(self) -> int:
        """Duración máxima de la asesoría en horas."""
        return self._duración_maxima
    
    def calcular_costo(self, duracion: int, preparacion: bool = False, material: bool = False) -> float:
        """
        Calcula el costo de la asesoría con recargos adicionales.
        
        Args:
            duración: Duración en horas
            preparacion: Si requiere preparación previa
            material: Si incluye material de apoyo
            
        Returns:
            float: Costo calculado
            
        Raises:
            CalculoCostoError: Si la duración es inválida o excede el máximo
        """
        # Llamar al método del padre para validación básica
        super().calcular_costo(dacion)
        
        if duracion > self._duración_maxima:
            raise CalculoCostoError(f"La duración ({daccion}h) excede el máximo permitido ({self._duración_maxima}h)")
        
        costo_base = self._costo_base * duracion
        
        # Recargos adicionales
        if preparacion:
            costo_base += 50000  # Recargo fijo por preparación
        if material:
            costo_base += 30000  # Recargo por material
        
        return round(costo_base, 2)
    
    def __str__(self) -> str:
        return f"AsesoriaEspecializada(ID: {self._id_servicio}, Temática: {self._temática}, Duración máxima: {self._duración_maxima}h, Costo base: ${self._costo_base:,.2f})"
    
    def to_dict(self) -> dict[str, Any]:
        """
        Convierte el servicio a un diccionario.
        
        Returns:
            dict: Datos del servicio
        """
        datos = super().to_dict()
        datos['temática'] = self._temática
        datos['duración_maxima'] = self._duración_maxima
        datos['tipo'] = 'AsesoriaEspecializada'
        return datos