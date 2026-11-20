# tests/test_simulaciones.py
import unittest
from datetime import date, timedelta
from cliente import Cliente
from reserva_sala import ReservaSala
from alquiler_equipo import AlquilerEquipo
from asesoria_especializada import AsesoriaEspecializada
from reserva import Reserva
from excepciones import *

class TestSistemaGestion(unittest.TestCase):
    """Clase de pruebas para el sistema de gestión."""
    
    def test cliente valido(self):
        """Prueba creación de cliente válido."""
        cliente = Cliente("Juan Pérez", "12345678", "juan@email.com")
        self.assertEqual(cliente.nombre, "Juan Pérez")
        self.assertEqual(cliente.documento, "12345678")
    
    def test cliente invalido(self):
        """Prueba cliente inválido."""
        with self.assertRaises(ClienteInvalidoError):
            Cliente("A", "123", "email_invalido")
    
    def test reserva sala valido(self):
        """Prueba creación de sala válida."""
        sala = ReservaSala("S001", "Sala de Reuniones", 50000, 10)
        self.assertEqual(sala.capacidad, 10)
        costo = sala.calcular_costo(2, impuesto=0.1, descuento=0.05)
        self.assertEqual(costo, 50000 * 2 * 1.1 * 0.95)
    
    def test alquiler equipo valido(self):
        """Prueba creación de equipo válido."""
        equipo = AlquilerEquipo("E001", "Proyector", 25000, "Proyector Epson")
        self.assertEqual(equipo.equipo, "Proyector Epson")
        costo = equipo.calcular_costo(3, daño=True)
        self.assertEqual(costo, 25000 * 3 * 1.5)
    
    def test asoria especializada valida(self):
        """Prueba creación de asesoría válida."""
        asesoria = AsesoriaEspecializada("A001", "Asesoría IA", 75000, "Inteligencia Artificial", 8)
        self.assertEqual(asesoria.temática, "Inteligencia Artificial")
        costo = asesoria.calcular_costo(4, preparacion=True)
        self.assertEqual(costo, 75000 * 4 + 50000)
    
    def test reserva valida(self):
        """Prueba creación de reserva válida."""
        cliente = Cliente("Juan", "12345678", "juan@email.com")
        sala = ReservaSala("S001", "Sala", 50000, 10)
        reserva = Reserva(cliente, sala, 2, date.today() + timedelta(days=1))
        self.assertEqual(reserva.duración, 2)
        self.assertEqual(reserva.estado, "pendiente")
    
    def test reserva invalida(self):
        """Prueba reserva inválida."""
        cliente = Cliente("Juan", "12345678", "juan@email.com")
        sala = ReservaSala("S001", "Sala", 50000, 10)
        with self.assertRaises(DuraciónInvalidaError):
            Reserva(cliente, sala, -1, date.today() + timedelta(days=1))

if __name__ == "__main__":
    unittest.main()