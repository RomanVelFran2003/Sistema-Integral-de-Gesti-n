"""
main.py - Programa principal del Sistema Integral de Gestion.
Software FJ
"""

import sys
from datetime import date, timedelta

from cliente import Cliente
from reserva import Reserva
from servicio import Servicio
from reserva_sala import ReservaSala
from alquiler_equipo import AlquilerEquipo
from asesoria_especializada import AsesoriaEspecializada

from excepciones import (
    ClienteInvalidoError,
    ServicioNoDisponibleError,
    ReservaInvalidaError,
    DuracionInvalidaError,
    ParametroObligatorioError,
    EstadoReservaError
)

from logging_config import logger


class SistemaGestion:
    """
    Administra clientes, servicios y reservas del sistema.
    La informacion se conserva en listas durante la ejecucion.
    """

    def __init__(self):
        self.__clientes = []
        self.__servicios = []
        self.__reservas = []

    def registrarCliente(self, cliente: Cliente):
        """Registra un cliente despues de validar su tipo y su identificador."""

        if not isinstance(cliente, Cliente):
            raise ClienteInvalidoError(
                "El objeto proporcionado no es un cliente valido."
            )

        for registrado in self.__clientes:
            if registrado.id == cliente.id:
                raise ValueError("Ya existe un cliente con ese identificador.")

        self.__clientes.append(cliente)
        logger.info("Cliente registrado: %s", cliente)
        return cliente

    def agregarServicio(self, servicio: Servicio):
        """Agrega un servicio valido al sistema."""

        if not isinstance(servicio, Servicio):
            raise ParametroObligatorioError(
                "Debe proporcionar un objeto de tipo Servicio."
            )

        for registrado in self.__servicios:
            if registrado.id_servicio == servicio.id_servicio:
                raise ValueError("Ya existe un servicio con ese identificador.")

        self.__servicios.append(servicio)
        logger.info("Servicio agregado: %s", servicio)
        return servicio

    def crearReserva(self, cliente, servicio, duracion, fecha):
        """Crea una reserva usando un cliente y un servicio registrados."""

        if cliente not in self.__clientes:
            raise ReservaInvalidaError(
                "El cliente no se encuentra registrado en el sistema."
            )

        if servicio not in self.__servicios:
            raise ReservaInvalidaError(
                "El servicio no se encuentra registrado en el sistema."
            )

        reserva = Reserva(cliente, servicio, duracion, fecha)
        self.__reservas.append(reserva)

        logger.info(
            "Reserva creada para el cliente %s y el servicio %s.",
            cliente.id,
            servicio.id_servicio
        )

        return reserva

    def procesarReserva(self, reserva, **kwargs):
        """Calcula el costo y confirma una reserva."""

        if reserva not in self.__reservas:
            raise ReservaInvalidaError(
                "La reserva no pertenece a este sistema."
            )

        return reserva.procesar(**kwargs)

    def mostrarResumen(self):
        """Muestra el resumen de los registros."""

        print("\n========== RESUMEN DEL SISTEMA ==========")
        print("Clientes registrados:", len(self.__clientes))
        print("Servicios registrados:", len(self.__servicios))
        print("Reservas creadas:", len(self.__reservas))

        for reserva in self.__reservas:
            print(reserva)

        print("=========================================")


def ejecutar_simulaciones():
    """Ejecuta operaciones validas e invalidas para demostrar el sistema."""

    sistema = SistemaGestion()
    fecha_reserva = date.today() + timedelta(days=3)

    print("\n==========================================")
    print(" SISTEMA INTEGRAL DE GESTION - SOFTWARE FJ")
    print("==========================================")

    # SIMULACION 1: Registrar un cliente valido.
    print("\nSIMULACION 1: Registro de cliente valido")

    cliente = Cliente(
        "Carlos Perez",
        "12345678",
        "carlos@gmail.com"
    )

    sistema.registrarCliente(cliente)
    print("Resultado: cliente registrado correctamente.")

    # SIMULACION 2: Intentar crear un cliente con datos invalidos.
    print("\nSIMULACION 2: Registro de cliente invalido")

    try:
        Cliente(
            "",
            "123",
            "correo_incorrecto"
        )
    except (ClienteInvalidoError, ParametroObligatorioError, ValueError) as error:
        logger.warning("No fue posible crear el cliente: %s", error)
        print("Resultado: se rechazo el cliente por datos invalidos.")

    # SIMULACION 3: Crear y registrar una reserva de sala.
    print("\nSIMULACION 3: Registro de servicio de sala")

    sala = ReservaSala(
        "S001",
        "Sala de reuniones",
        80000,
        10
    )

    sistema.agregarServicio(sala)
    print("Resultado: servicio de sala registrado.")

    # SIMULACION 4: Crear y registrar un servicio de alquiler de equipo.
    print("\nSIMULACION 4: Registro de alquiler de equipo")

    equipo = AlquilerEquipo(
        "S002",
        "Proyector multimedia",
        50000,
        "Proyector",
        "disponible"
    )

    sistema.agregarServicio(equipo)
    print("Resultado: equipo registrado correctamente.")

    # SIMULACION 5: Crear y registrar una asesoria especializada.
    print("\nSIMULACION 5: Registro de asesoria especializada")

    asesoria = AsesoriaEspecializada(
        "S003",
        "Asesoria tecnologica",
        60000,
        "Tecnologia",
        4
    )

    sistema.agregarServicio(asesoria)
    print("Resultado: asesoria registrada correctamente.")

    # SIMULACION 6: Intentar registrar un servicio duplicado.
    print("\nSIMULACION 6: Registro de servicio duplicado")

    try:
        sistema.agregarServicio(sala)
    except ValueError as error:
        logger.warning("Registro duplicado: %s", error)
        print("Resultado: se rechazo el servicio duplicado.")

    # SIMULACION 7: Crear y procesar una reserva de sala.
    print("\nSIMULACION 7: Reserva de sala")

    reserva_sala = sistema.crearReserva(
        cliente,
        sala,
        2,
        fecha_reserva
    )

    costo_sala = sistema.procesarReserva(
        reserva_sala,
        personas=5,
        impuesto=0.19,
        descuento=0.10
    )

    print("Resultado: reserva procesada correctamente.")
    print("Costo de la reserva de sala: $", costo_sala)

    # SIMULACION 8: Crear y procesar una reserva de equipo.
    print("\nSIMULACION 8: Reserva de equipo")

    reserva_equipo = sistema.crearReserva(
        cliente,
        equipo,
        3,
        fecha_reserva
    )

    costo_equipo = sistema.procesarReserva(
        reserva_equipo,
        daño=False,
        limpieza=True
    )

    print("Resultado: reserva de equipo procesada.")
    print("Costo del alquiler: $", costo_equipo)

    # SIMULACION 9: Crear y procesar una asesoria.
    print("\nSIMULACION 9: Reserva de asesoria")

    reserva_asesoria = sistema.crearReserva(
        cliente,
        asesoria,
        2,
        fecha_reserva
    )

    costo_asesoria = sistema.procesarReserva(
        reserva_asesoria,
        preparacion=True,
        material=True
    )

    print("Resultado: asesoria procesada correctamente.")
    print("Costo de la asesoria: $", costo_asesoria)

    # SIMULACION 10: Intentar crear una reserva con duracion invalida.
    print("\nSIMULACION 10: Duracion invalida")

    try:
        sistema.crearReserva(
            cliente,
            sala,
            0,
            fecha_reserva
        )
    except (DuracionInvalidaError, ReservaInvalidaError, ValueError) as error:
        logger.warning("Reserva rechazada: %s", error)
        print("Resultado: se rechazo la duracion invalida.")

    # SIMULACION 11: Intentar crear una reserva con fecha pasada.
    print("\nSIMULACION 11: Fecha de reserva vencida")

    try:
        sistema.crearReserva(
            cliente,
            sala,
            1,
            date.today() - timedelta(days=1)
        )
    except (ReservaInvalidaError, ValueError) as error:
        logger.warning("Fecha de reserva rechazada: %s", error)
        print("Resultado: se rechazo la fecha pasada.")

    # SIMULACION 12: Intentar reservar un servicio no registrado.
    print("\nSIMULACION 12: Servicio no registrado")

    try:
        servicio_externo = ReservaSala(
            "S999",
            "Sala externa",
            70000,
            8
        )

        sistema.crearReserva(
            cliente,
            servicio_externo,
            1,
            fecha_reserva
        )
    except (ReservaInvalidaError, ValueError) as error:
        logger.warning("Servicio rechazado: %s", error)
        print("Resultado: se rechazo el servicio no registrado.")

    # SIMULACION 13: Intentar reservar un equipo en mantenimiento.
    print("\nSIMULACION 13: Equipo no disponible")

    equipo.cambiar_estado("mantenimiento")

    reserva_mantenimiento = sistema.crearReserva(
        cliente,
        equipo,
        1,
        fecha_reserva
    )

    try:
        sistema.procesarReserva(reserva_mantenimiento)
    except ServicioNoDisponibleError as error:
        logger.warning("Servicio rechazado: %s", error)
        print("Resultado: no se pudo reservar el equipo.")
    except ReservaInvalidaError as error:
        logger.error("No se pudo procesar la reserva: %s", error)
        print("Resultado: no se pudo reservar el equipo.")

    # SIMULACION 14: Demostrar el manejo de excepciones.
    print("\nSIMULACION 14: Manejo de excepciones")

    try:
        print("Verificando el estado de una reserva...")
        if reserva_sala.estado != "confirmada":
            raise EstadoReservaError(
                "La reserva de sala no se encuentra confirmada."
            )

    except EstadoReservaError as error:
        logger.error("Error de estado: %s", error)
        print("Se detecto un problema con el estado de la reserva.")

    else:
        print("La reserva se encuentra confirmada correctamente.")

    finally:
        print("Verificacion de estado finalizada.")

    # Mostrar el resumen de las operaciones.
    sistema.mostrarResumen()

    logger.info("Finalizaron las simulaciones del sistema.")


def main():
    """Punto de entrada del programa."""

    try:
        ejecutar_simulaciones()

    except Exception as error:
        logger.exception("Error inesperado durante la ejecucion: %s", error)
        print("Ocurrio un error inesperado. Revise los archivos de logs.")

    else:
        print("\nEl programa finalizo las simulaciones.")

    finally:
        print("Gracias por utilizar el sistema Software FJ.")

    return 0


if __name__ == "__main__":
    sys.exit(main())

11.
"""
test_simulaciones.py - Pruebas automaticas del sistema Software FJ.
"""

import unittest
from datetime import date, timedelta

from cliente import Cliente
from reserva import Reserva
from reserva_sala import ReservaSala
from alquiler_equipo import AlquilerEquipo
from asesoria_especializada import AsesoriaEspecializada

from excepciones import (
    ClienteInvalidoError,
    ServicioNoDisponibleError,
    ReservaInvalidaError,
    DuracionInvalidaError,
    ParametroObligatorioError,
    EstadoReservaError
)


class TestCliente(unittest.TestCase):

    def test_cliente_valido(self):
        cliente = Cliente(
            "Carlos Perez",
            "12345678",
            "carlos@gmail.com"
        )

        self.assertEqual(cliente.nombre, "Carlos Perez")
        self.assertEqual(cliente.documento, "12345678")
        self.assertEqual(cliente.contacto, "carlos@gmail.com")

    def test_cliente_nombre_invalido(self):
        with self.assertRaises(
            (ClienteInvalidoError, ParametroObligatorioError)
        ):
            Cliente("", "12345678", "carlos@gmail.com")

    def test_cliente_documento_invalido(self):
        with self.assertRaises(
            (ClienteInvalidoError, ParametroObligatorioError)
        ):
            Cliente("Carlos Perez", "123", "carlos@gmail.com")

    def test_cliente_correo_invalido(self):
        with self.assertRaises(
            (ClienteInvalidoError, ParametroObligatorioError)
        ):
            Cliente("Carlos Perez", "12345678", "correo_incorrecto")


class TestServicios(unittest.TestCase):

    def test_reserva_sala_costo(self):
        sala = ReservaSala(
            "S001",
            "Sala de reuniones",
            80000,
            10
        )

        costo = sala.calcular_costo(
            2,
            personas=5,
            impuesto=0.19,
            descuento=0.10
        )

        esperado = 80000 * 2 * 1.19 * 0.90
        self.assertAlmostEqual(costo, esperado, places=2)

    def test_reserva_sala_exceso_personas(self):
        sala = ReservaSala(
            "S001",
            "Sala de reuniones",
            80000,
            10
        )

        with self.assertRaises(Exception):
            sala.calcular_costo(2, personas=15)

    def test_alquiler_equipo_costo(self):
        equipo = AlquilerEquipo(
            "S002",
            "Proyector multimedia",
            50000,
            "Proyector",
            "disponible"
        )

        costo = equipo.calcular_costo(
            2,
            daño=False,
            limpieza=True
        )

        self.assertEqual(costo, 125000)

    def test_equipo_no_disponible(self):
        equipo = AlquilerEquipo(
            "S002",
            "Proyector multimedia",
            50000,
            "Proyector",
            "mantenimiento"
        )

        with self.assertRaises(ServicioNoDisponibleError):
            equipo.calcular_costo(1)

    def test_asesoria_costo(self):
        asesoria = AsesoriaEspecializada(
            "S003",
            "Asesoria tecnologica",
            60000,
            "Tecnologia",
            4
        )

        costo = asesoria.calcular_costo(
            2,
            preparacion=True,
            material=True
        )

        self.assertEqual(costo, 200000)

    def test_asesoria_supera_duracion_maxima(self):
        asesoria = AsesoriaEspecializada(
            "S003",
            "Asesoria tecnologica",
            60000,
            "Tecnologia",
            4
        )

        with self.assertRaises(Exception):
            asesoria.calcular_costo(5)


class TestReserva(unittest.TestCase):

    def setUp(self):
        self.cliente = Cliente(
            "Carlos Perez",
            "12345678",
            "carlos@gmail.com"
        )

        self.sala = ReservaSala(
            "S001",
            "Sala de reuniones",
            80000,
            10
        )

        self.fecha = date.today() + timedelta(days=3)

    def test_crear_reserva_valida(self):
        reserva = Reserva(
            self.cliente,
            self.sala,
            2,
            self.fecha
        )

        self.assertEqual(reserva.estado, "pendiente")
        self.assertEqual(reserva.duracion, 2)

    def test_duracion_invalida(self):
        with self.assertRaises(DuracionInvalidaError):
            Reserva(
                self.cliente,
                self.sala,
                0,
                self.fecha
            )

    def test_fecha_pasada(self):
        with self.assertRaises(ReservaInvalidaError):
            Reserva(
                self.cliente,
                self.sala,
                2,
                date.today() - timedelta(days=1)
            )

    def test_procesar_reserva(self):
        reserva = Reserva(
            self.cliente,
            self.sala,
            2,
            self.fecha
        )

        costo = reserva.procesar(
            personas=5,
            impuesto=0.19,
            descuento=0.10
        )

        self.assertAlmostEqual(costo, 171360, places=2)
        self.assertEqual(reserva.estado, "confirmada")

    def test_cancelar_reserva(self):
        reserva = Reserva(
            self.cliente,
            self.sala,
            2,
            self.fecha
        )

        reserva.cancelar()

        self.assertEqual(reserva.estado, "cancelada")

    def test_completar_reserva(self):
        reserva = Reserva(
            self.cliente,
            self.sala,
            2,
            self.fecha
        )

        reserva.confirmar()
        reserva.completar()

        self.assertEqual(reserva.estado, "completada")

    def test_encadenamiento_excepcion(self):
        reserva = Reserva(
            self.cliente,
            self.sala,
            2,
            self.fecha
        )

        with self.assertRaises(ReservaInvalidaError) as contexto:
            reserva.calcular_costo(personas=15)

        self.assertIsNotNone(contexto.exception.__cause__)


if __name__ == "__main__":
    unittest.main()