"""
reserva.py - Clase que representa las reservas del sistema Software FJ.
"""

from datetime import date, datetime
from typing import Any

from cliente import Cliente
from servicio import Servicio
from excepciones import (
    ReservaInvalidaError,
    DuracionInvalidaError,
    EstadoReservaError,
    ParametroObligatorioError
)
from logging_config import logger


class Reserva:
    """
    Representa una reserva realizada por un cliente para un servicio.
    """

    ESTADOS_VALIDOS = [
        "pendiente",
        "confirmada",
        "cancelada",
        "completada"
    ]

    def __init__(
        self,
        cliente: Cliente,
        servicio: Servicio,
        duracion: int,
        fecha: date
    ):
        # Validar cliente
        if cliente is None:
            raise ParametroObligatorioError(
                "El cliente es obligatorio."
            )

        if not isinstance(cliente, Cliente):
            raise ReservaInvalidaError(
                "El cliente debe ser una instancia de Cliente."
            )

        # Validar servicio
        if servicio is None:
            raise ParametroObligatorioError(
                "El servicio es obligatorio."
            )

        if not isinstance(servicio, Servicio):
            raise ReservaInvalidaError(
                "El servicio debe ser una instancia de Servicio."
            )

        # Validar duración
        if duracion is None:
            raise ParametroObligatorioError(
                "La duración de la reserva es obligatoria."
            )

        if (
            isinstance(duracion, bool)
            or not isinstance(duracion, int)
            or duracion <= 0
        ):
            raise DuracionInvalidaError(
                "La duración debe ser un número entero mayor que cero."
            )

        # Validar fecha
        if fecha is None:
            raise ParametroObligatorioError(
                "La fecha de la reserva es obligatoria."
            )

        if not isinstance(fecha, date) or isinstance(fecha, datetime):
            raise ReservaInvalidaError(
                "La fecha debe ser un objeto de tipo date."
            )

        if fecha < date.today():
            raise ReservaInvalidaError(
                "No se pueden crear reservas con fechas pasadas."
            )

        # Inicializar atributos
        self._cliente = cliente
        self._servicio = servicio
        self._duracion = duracion
        self._fecha = fecha
        self._estado = "pendiente"
        self._fecha_creacion = datetime.now()
        self._costo_calculado = None

        logger.info(
            "Reserva creada para el cliente %s y servicio %s.",
            cliente.id,
            servicio.id_servicio
        )

    @property
    def cliente(self) -> Cliente:
        return self._cliente

    @property
    def servicio(self) -> Servicio:
        return self._servicio

    @property
    def duracion(self) -> int:
        return self._duracion

    @property
    def duración(self) -> int:
        """Propiedad compatible con el nombre utilizado anteriormente."""
        return self._duracion

    @property
    def fecha(self) -> date:
        return self._fecha

    @property
    def estado(self) -> str:
        return self._estado

    @property
    def fecha_creacion(self) -> datetime:
        return self._fecha_creacion

    @property
    def costo_calculado(self) -> float:
        return self._costo_calculado

    def confirmar(self) -> bool:
        """
        Confirma una reserva pendiente.
        """

        if self._estado != "pendiente":
            raise EstadoReservaError(
                "Solo se pueden confirmar reservas pendientes."
            )

        self._estado = "confirmada"

        logger.info("Reserva confirmada correctamente.")

        return True

    def cancelar(self) -> bool:
        """
        Cancela una reserva pendiente o confirmada.
        """

        if self._estado not in ["pendiente", "confirmada"]:
            raise EstadoReservaError(
                "No se puede cancelar una reserva cancelada o completada."
            )

        self._estado = "cancelada"

        logger.info("Reserva cancelada correctamente.")

        return True

    def completar(self) -> bool:
        """
        Marca como completada una reserva confirmada.
        """

        if self._estado != "confirmada":
            raise EstadoReservaError(
                "Solo se pueden completar reservas confirmadas."
            )

        self._estado = "completada"

        logger.info("Reserva completada correctamente.")

        return True

    def calcular_costo(self, **kwargs) -> float:
        """
        Calcula el costo utilizando el método del servicio correspondiente.
        """

        if self._estado == "cancelada":
            raise EstadoReservaError(
                "No se puede calcular el costo de una reserva cancelada."
            )

        try:
            costo = self._servicio.calcular_costo(
                self._duracion,
                **kwargs
            )

            self._costo_calculado = costo

            logger.info(
                "Costo de reserva calculado: $%.2f",
                costo
            )

            return costo

        except Exception as error:
            logger.exception(
                "Error al calcular el costo de la reserva."
            )

            raise ReservaInvalidaError(
                "No fue posible calcular el costo de la reserva."
            ) from error

    def procesar(self, **kwargs) -> float:
        """
        Procesa una reserva pendiente:
        calcula el costo y la confirma si el cálculo es exitoso.
        """

        if self._estado != "pendiente":
            raise EstadoReservaError(
                "Solo se pueden procesar reservas pendientes."
            )

        costo = self.calcular_costo(**kwargs)
        self.confirmar()

        logger.info(
            "Reserva procesada correctamente. Costo: $%.2f",
            costo
        )

        return costo

    def __str__(self) -> str:
        return (
            f"Reserva | Cliente: {self._cliente.nombre} | "
            f"Servicio: {self._servicio.nombre} | "
            f"Duración: {self._duracion} horas | "
            f"Fecha: {self._fecha} | "
            f"Estado: {self._estado}"
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "cliente": self._cliente.to_dict(),
            "servicio": self._servicio.to_dict(),
            "duracion": self._duracion,
            "fecha": self._fecha.isoformat(),
            "estado": self._estado,
            "fecha_creacion": self._fecha_creacion.isoformat(),
            "costo_calculado": self._costo_calculado
        }
