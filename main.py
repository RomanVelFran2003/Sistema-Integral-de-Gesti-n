"""
main.py - Script principal del sistema Software FJ.
Ejecuta simulaciones completas del sistema.
"""
import sys
from datetime import date, timedelta
from cliente import Cliente
from servicio import Servicio
from reserva_sala import ReservaSala
from alquiler_equipo import AlquilerEquipo
from asesoria_especializada import AsesoriaEspecializada
from reserva import Reserva
from excepciones import (
    ClienteInvalidoError, ServicioNoDisponibleError, ReservaInvalidaError,
    DuracionInvalidaError, ParametroObligatorioError, EstadoReservaError,
    CalculoCostoError
)
from logging_config import logger

class SistemaGestion:
    """
    Clase principal que gestiona el sistema de Software FJ.
    """
    
    def __init__(self):
        """ inicializa el sistema con listas vacías."""
        self.__client = []
        self.__servicios = []
        self.__reservas = []
        logger.info(" Sistema Software FJ iniciado")
    
    def registrarCliente(self, nombre: str, documento: str, contacto: str) -> bool:
        """
        Registra un nuevo cliente en el sistema.
        
        Returns:
            bool: True si el registro fue exitoso
        """
        try:
            cliente = Cliente(nome, documento, contacto)
            self.__client.append(cliente)
            logger.info(f"Cliente registrado: {cliente}")
            return True
        except (ClienteInvalidoError, ParametroObligatorioError) as e:
            logger.error(f"Error registrando cliente: {str(e)}")
            return False
        except Exception as e:
            logger.critical(f"Error inesperado registrando cliente: {str(e)}")
            return False
    
    def agregarServicio(self, servicio) -> bool:
        """
        Agrega un servicio al sistema.
        
        Returns:
            bool: True si la agregación fue exitosa
        """
        try:
            self.__servicios.append(servicio)
            logger.info(f"Servicio agregado: {servicio}")
            return True
        except Exception as e:
            logger.error(f"Error agregando servicio: {str(e)}")
            return False
    
    def crearReserva(self, cliente: Cliente, servicio: Servicio, duración: int, fecha: date) -> bool:
        """
        Crea una nueva reserva.
        
        Returns:
            bool: True si la reserva fue exitosa
        """
        try:
            reserva = Reserva(cliente, servicio, duración, fecha)
            self.__reservas.append(reserva)
            logger.info(f"Reserva creada: {reserva}")
            return True
        except (ReservaInvalidaError, DuracionInvalidaError, ParametroObligatorioError) as e:
            logger.error(f"Error creando reserva: {str(e)}")
            return False
        except Exception as e:
            logger.critical(f"Error inesperado creando reserva: {str(e)}")
            return False
    
    def ejecutar_simulaciones(self):
        """ Ejecuta las simulaciones obligatorias del sistema."""
        logger.info("=== INICIANDO SIMULACIONES OBLIGATORIAS ===")
        
        # Simulaciones válidas
        self._simulacion1_ClienteValido()
        self._simulacion2_ReservaValida()
        self._simulacion3_SalaValida()
        self._simulacion4_EquipoValido()
        self._simulacion5_AsesoriaValida()
        
        # Simulaciones inválidas
        self._simulacion6_ClienteSinDocumento()
        self._simulacion7_ClienteDatosIncorrectos()
        self._simulacion8_ServicioInexistente()
        self._simulacion9_DurationInvalida()
        self._simulacion10_ReservaIncorrecta()
        
        # Simulaciones extra para robustez
        self._simulaciones_extras()
        
        logger.info("=== SIMULACIONES COMPLETADAS ===")
    
    def _simulacion1_ClienteValido(self):
        """Simulación 1: Cliente válido."""
        logger.info(" Simulación 1: Cliente válido")
        try:
            exito = self.registrarCliente("Juan Pérez", "12345678", "juan.perez@email.com")
            if exito:
                logger.info(" Simulación 1 exitosa: cliente registrado correctamente")
            else:
                logger.error(" Simulación 1 fallida: no se pudo registrar el cliente")
        except Exception as e:
            logger.error(f" Error en simulación 1: {str(e)}")
    
    def _simulacion2_ReservaValida(self):
        """Simulación 2: Reserva válida."""
        logger.info(" Simulación 2: Reserva válida")
        try:
            if self.__client and self.__servicios:
                cliente = self.__client[0]
                servicio = self.__servicios[0]
                exito = self.crearReserva(cliente, servicio, 2, date.today() + timedelta(days=1))
                if exito:
                    logger.info(" Simulación 2 exitosa: reserva creada correctamente")
                else:
                    logger.error(" Simulación 2 fallida: no se pudo crear la reserva")
            else:
                logger.warning(" No hay clientes o servicios disponibles para la simulación 2")
        except Exception as e:
            logger.error(f" Error en simulación 2: {str(e)}")
    
    def _simulacion3_SalaValida(self):
        """Simulación 3: Sala válida."""
        logger.info(" Simulación 3: Sala válida")
        try:
            sala = ReservaSala("SALA001", "Sala de Reuniones Principal", 50000, 20)
            exito = self.agregarServicio(sala)
            if exito:
                logger.info(" Simulación 3 exitosa: sala agregada correctamente")
            else:
                logger.error(" Simulación 3 fallida: no se pudo agregar la sala")
        except Exception as e:
            logger.error(f" Error en simulación 3: {str(e)}")
    
    def _simulacion4_EquipoValido(self):
        """Simulación 4: Equipo válido."""
        logger.info(" Simulación 4: Equipo válido")
        try:
            equipo = AlquilerEquipo("EQ001", "Proyector Epson", 25000, "Proyector Epson PowerLite")
            exito = self.agregarServicio(equipo)
            if exito:
                logger.info(" Simulación 4 exitosa: equipo agregado correctamente")
            else:
                logger.error(" Simulación 4 fallida: no se pudo agregar el equipo")
        except Exception as e:
            logger.error(f" Error en simulación 4: {str(e)}")
    
    def _simulacion5_AsesoriaValida(self):
        """Simulación 5: Asesoría válida."""
        logger.info(" Simulación 5: Asesoría válida")
        try:
            asesoria = AsesoriaEspecializada("ASE001", "Asesoría en IA", 75000, "Inteligencia Artificial", 8)
            exito = self.agregarServicio(asesoria)
            if exito:
                logger.info(" Simulación 5 exitosa: asesoría agregada correctamente")
            else:
                logger.error(" Simulación 5 fallida: no se pudo agregar la asesoría")
        except Exception as e:
            logger.error(f" Error en simulación 5: {str(e)}")
    
    def _simulacion6_ClienteSinDocumento(self):
        """Simulación 6: Cliente sin documento."""
        logger.info(" Simulación 6: Cliente sin documento")
        try:
            exito = self.registrarCliente("María García", "", "maria.garcia@email.com")
            if not exito:
                logger.info(" Simulación 6 exitosa: se detectó correctamente el error de documento faltante")
            else:
                logger.error(" Simulación 6 fallida: no se detectó el error de documento faltante")
        except Exception as e:
            logger.error(f" Error inesperado en simulación 6: {str(e)}")
    
    def _simulacion7_ClienteDatosIncorrectos(self):
        """Simulación 7: Cliente con datos incorrectos."""
        logger.info(" Simulación 7: Cliente con datos incorrectos")
        try:
            exito = self.registrarCliente("Carlos", "123", "email_no_valido")
            if not exito:
                logger.info(" Simulación 7 exitosa: se detectaron correctamente los datos incorrectos")
            else:
                logger.error(" Simulación 7 fallida: no se detectaron los datos incorrectos")
        except Exception as e:
            logger.error(f" Error inesperado en simulación 7: {str(e)}")
    
    def _simulacion8_ServicioInexistente(self):
        """Simulación 8: Servicio inexistente."""
        logger.info(" Simulación 8: Servicio inexistente")
        try:
            if self.__client:
                cliente = self.__client[0]
                # Intentar crear reserva con un servicio que no existe
                servicio_ficticio = ReservaSala("FICTICIO", "Servicio Ficticio", 10000, 10)
                exito = self.crearReserva(cliente, servicio_ficticio, 1, date.today() + timedelta(days=1))
                if not exito:
                    logger.info(" Simulación 8 exitosa: se detectó correctamente el servicio inexistente")
                else:
                    logger.error(" Simulación 8 fallida: no se detectó el servicio inexistente")
            else:
                logger.warning(" No hay clientes disponibles para la simulación 8")
        except Exception as e:
            logger.error(f" Error inesperado en simulación 8: {str(e)}")
    
    def _simulacion9_DurationInvalida(self):
        """Simulación 9: Duración inválida."""
        logger.info(" Simulación 9: Duración inválida")
        try:
            if self.__client and self.__servicios:
                cliente = self.__client[0]
                servicio = self.__servicios[0]
                exito = self.crearReserva(cliente, servicio, -5, date.today() + timedelta(days=1))
                if not exito:
                    logger.info(" Simulación 9 exitosa: se detectó correctamente la duración inválida")
                else:
                    logger.error(" Simulación 9 fallida: no se detectó la duración inválida")
            else:
                logger.warning(" No hay clientes o servicios disponibles para la simulación 9")
        except Exception as e:
            logger.error(f" Error inesperado en simulación 9: {str(e)}")
    
    def _simulacion10_ReservaIncorrecta(self):
        """Simulación 10: Reserva incorrecta."""
        logger.info(" Simulación 10: Reserva incorrecta")
        try:
            if self.__client:
                cliente = self.__client[0]
                # Intentar crear reserva con fecha pasada
                servicio = ReservaSala("SALA002", "Sala de Prueba", 30000, 10)
                exito = self.crearReserva(cliente, servicio, 2, date.today() - timedelta(days=1))
                if not exito:
                    logger.info(" Simulación 10 exitosa: se detectó correctamente la fecha pasada")
                else:
                    logger.error(" Simulación 10 fallida: no se detectó la fecha pasada")
            else:
                logger.warning(" No hay clientes disponibles para la simulación 10")
        except Exception as e:
            logger.error(f" Error inesperado en simulación 10: {str(e)}")
    
    def _simulaciones_extras(self):
        """Simulaciones extras para demostrar robustez."""
        logger.info("=== SIMULACIONES EXTRAS ===")
        
        # Extra 1: Encadenamiento de excepciones
        self._extra1_EncadenamientoExcepciones()
        
        # Extra 2: Operación que falla pero continúa
        self._extra2_OperacionFallidaContinua()
        
        # Extra 3: Múltiples errores consecutivos
        self._extra3_MultiplesErrores()
        
        # Extra 4: Validación de límites
        self._extra4_ValidacionLimites()
        
        # Extra 5: Operación compleja exitosa
        self._extra5_OperacionComplejaExitosa()
    
    def _extra1_EncadenamientoExcepciones(self):
        """Extra 1: Demostrar encadenamiento de excepciones."""
        logger.info(" Extra 1: Encadenamiento de excepciones")
        try:
            # Intentar crear un cliente con datos que causan múltiples errores
            cliente = Cliente("A", "123", "email")  # Múltiples errores
        except Exception as e:
            logger.info(f" Excepción encadenada detectada: {type(e).__name__}: {str(e)}")
            if e.__cause__:
                logger.info(f" Causa original: {type(e.__cause__).__name__}: {str(e.__cause__)}")
    
    def _extra2_OperacionFallidaContinua(self):
        """Extra 2: Operación fallida que no detiene el sistema."""
        logger.info(" Extra 2: Operación fallida que continúa")
        try:
            # Intentar una operación que fallará
            cliente_invalido = Cliente("", "", "")
        except Exception as e:
            logger.warning(f" Error controlado: {str(e)}")
            logger.info(" El sistema continúa funcionando después del error")
    
    def _extra3_MultiplesErrores(self):
        """Extra 3: Múltiples errores consecutivos."""
        logger.info(" Extra 3: Múltiples errores consecutivos")
        errores = 0
        
        # Primero error
        try:
            cliente = Cliente("Test", "123", "email_invalido")
        except Exception as e:
            logger.error(f" Error 1: {str(e)}")
            errores += 1
        
        # Segundo error
        try:
            servicio = ReservaSala("S", "Sala", -1000, 0)
        except Exception as e:
            logger.error(f" Error 2: {str(e)}")
            errores += 1
        
        # Tercer error
        try:
            reserva = Reserva(None, None, 0, None)
        except Exception as e:
            logger.error(f" Error 3: {str(e)}")
            errores += 1
        
        logger.info(f" Total de errores manejados: {errores}")
        logger.info(" El sistema sigue funcionando después de múltiples errores")
    
    def _extra4_ValidacionLimites(self):
        """Extra 4: Validación de límites."""
        logger.info(" Extra 4: Validación de límites")
        try:
            # Probar con valores en los límites
            cliente_limite = Cliente("A" * 100, "12345678", "test@email.com")
            logger.info(" Cliente con nombre largo aceptado correctamente")
        except Exception as e:
            logger.error(f" Error inesperado con límites: {str(e)}")
    
    def _extra5_OperacionComplejaExitosa(self):
        """Extra 5: Operación compleja exitosa."""
        logger.info(" Extra 5: Operación compleja exitosa")
        try:
            # Crear cliente
            cliente = Cliente("Ana López", "87654321", "ana.lopez@email.com")
            self.__client.append(cliente)
            
            # Crear servicio
            servicio = ReservaSala("SALA003", "Sala Ejecutiva", 75000, 15)
            self.__servicios.append(servicio)
            
            # Crear reserva
            reserva = Reserva(cliente, servicio, 3, date.today() + timedelta(days=2))
            self.__reservas.append(reserva)
            
            # Calcular costo con parámetros
            costo = reserva.calcular_costo(impuesto=0.16, descuento=0.10, personas=10)
            
            logger.info(f" Operación compleja exitosa. Costo final: ${costo:,.2f}")
            
        except Exception as e:
            logger.error(f" Error en operación compleja: {str(e)}")

def main():
    """Función principal del sistema."""
    logger.info("=== INICIO DEL SISTEMA SOFTWARE FJ ===")
    
    sistema = SistemaGestion()
    sistema.ejecutar_simulaciones()
    
    logger.info("=== SISTEMA FINALIZADO CORRECTAMENTE ===")
    return 0

if __name__ == "__main__":
    sys.exit(main())