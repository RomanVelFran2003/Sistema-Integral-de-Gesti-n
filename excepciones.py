"""
excepciones.py - Excepciones personalizadas para el sistema.
"""

class ClienteInvalidoError(Exception):
    """Excepción para clientes inválidos."""
    pass

class ServicioNoDisponibleError(Exception):
    """Excepción para servicios no disponibles."""
    pass

class ReservaInvalidaError(Exception):
    """Excepción para reservas inválidas."""
    pass

class DuracionInvalidaError(Exception):
    """Excepción para duraciones inválidas."""
    pass

class ParametroObligatorioError(Exception):
    """Excepción para parámetros obligatorios faltantes."""
    pass

class EstadoReservaError(Exception):
    """Excepción para errores en el estado de la reserva."""
    pass

class CalculoCostoError(Exception):
    """Excepción para errores en el cálculo de costos."""
    pass

class ArchivoError(Exception):
    """Excepción para errores de archivo."""
    pass