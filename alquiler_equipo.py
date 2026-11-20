"""
alquiler_equipo.py - Servicio de alquiler de equipos de Software FJ.
"""

from typing import Any

from servicio import Servicio
from excepciones import (
    CalculoCostoError,
    ParametroObligatorioError,
    ServicioNoDisponibleError
)


class AlquilerEquipo(Servicio):
    """
    Servicio para alquilar equipos tecnológicos.
    """

    ESTADOS_VALIDOS = [
        "disponible",
        "no disponible",
        "mantenimiento"
    ]

    def __init__(
        self,
        id_servicio: str,
        nombre: str,
        costo_base: float,
        equipo: str,
        estado: str = "disponible"
    ):
        super().__init__(id_servicio, nombre, costo_base)

        if not isinstance(equipo, str) or not equipo.strip():
            raise ParametroObligatorioError(
                "El nombre del equipo es obligatorio."
            )

        if not isinstance(estado, str):
            raise CalculoCostoError(
                "El estado del equipo debe ser texto."
            )

        estado_limpio = estado.strip().lower()

        if estado_limpio not in self.ESTADOS_VALIDOS:
            raise CalculoCostoError(
                "El estado del equipo no es válido."
            )

        self._equipo = equipo.strip()
        self._estado = estado_limpio

    @property
    def equipo(self) -> str:
        return self._equipo

    @property
    def estado(self) -> str:
        return self._estado

    def cambiar_estado(self, nuevo_estado: str) -> None:
        """
        Cambia el estado de disponibilidad del equipo.
        """

        if not isinstance(nuevo_estado, str):
            raise CalculoCostoError(
                "El nuevo estado debe ser texto."
            )

        estado_limpio = nuevo_estado.strip().lower()

        if estado_limpio not in self.ESTADOS_VALIDOS:
            raise CalculoCostoError(
                "El nuevo estado no es válido."
            )

        self._estado = estado_limpio

    def calcular_costo(
        self,
        duracion: int,
        daño: bool = False,
        limpieza: bool = False
    ) -> float:
        """
        Calcula el costo del alquiler del equipo.
        Aplica recargos por daños y limpieza.
        """

        # Validar duración
        super().calcular_costo(duracion)

        # Comprobar disponibilidad
        if self._estado != "disponible":
            raise ServicioNoDisponibleError(
                f"El equipo {self._equipo} no está disponible."
            )

        # Validar parámetros adicionales
        if not isinstance(daño, bool):
            raise CalculoCostoError(
                "El parámetro daño debe ser verdadero o falso."
            )

        if not isinstance(limpieza, bool):
            raise CalculoCostoError(
                "El parámetro limpieza debe ser verdadero o falso."
            )

        costo = self._costo_base * duracion

        if daño:
            costo *= 1.5

        if limpieza:
            costo += 25000

        return round(costo, 2)

    def __str__(self) -> str:
        return (
            f"{super().__str__()} | "
            f"Equipo: {self._equipo} | "
            f"Estado: {self._estado}"
        )

    def to_dict(self) -> dict[str, Any]:
        datos = super().to_dict()
        datos["equipo"] = self._equipo
        datos["estado"] = self._estado
        datos["tipo"] = "Alquiler de equipo"

        return datos
