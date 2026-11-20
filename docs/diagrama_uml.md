classDiagram
    class EntidadBase {
        <<abstract>>
        +__str__() str
        +to_dict() dict
    }

    class Cliente {
        -__nombre: str
        -__documento: str
        -__contacto: str
        -__id: int
        +nombre: str
        +documento: str
        +contacto: str
        +id: int
        +to_dict() dict
        +__str__() str
    }

    class Servicio {
        <<abstract>>
        -_id_servicio: str
        -_nombre: str
        -_costo_base: float
        +calcular_costo(duracion, kwargs) float
        +to_dict() dict
        +__str__() str
    }

    class ReservaSala {
        -capacidad: int
        +calcular_costo(duracion, kwargs) float
        +to_dict() dict
    }

    class AlquilerEquipo {
        -equipo: str
        -estado: str
        +cambiar_estado(estado) void
        +calcular_costo(duracion, kwargs) float
        +to_dict() dict
    }

    class AsesoriaEspecializada {
        -tematica: str
        -duracion_maxima: int
        +calcular_costo(duracion, kwargs) float
        +to_dict() dict
    }

    class Reserva {
        -_cliente: Cliente
        -_servicio: Servicio
        -_duracion: int
        -_fecha: date
        -_estado: str
        -_costo_calculado: float
        +confirmar() void
        +cancelar() void
        +completar() void
        +calcular_costo(kwargs) float
        +procesar(kwargs) float
        +to_dict() dict
        +__str__() str
    }

    class SistemaGestion {
        -__clientes: list
        -__servicios: list
        -__reservas: list
        +registrarCliente(cliente) Cliente
        +agregarServicio(servicio) Servicio
        +crearReserva(cliente, servicio, duracion, fecha) Reserva
        +procesarReserva(reserva, kwargs) float
        +mostrarResumen() void
    }

    class ClienteInvalidoError
    class ServicioNoDisponibleError
    class ReservaInvalidaError
    class DuracionInvalidaError
    class ParametroObligatorioError
    class EstadoReservaError
    class CalculoCostoError
    class ArchivoError

    EntidadBase <|-- Cliente
    EntidadBase <|-- Servicio

    Servicio <|-- ReservaSala
    Servicio <|-- AlquilerEquipo
    Servicio <|-- AsesoriaEspecializada

    Cliente "1" <-- "0..*" Reserva : pertenece a
    Servicio "1" <-- "0..*" Reserva : utiliza

    SistemaGestion "1" o-- "0..*" Cliente : administra
    SistemaGestion "1" o-- "0..*" Servicio : administra
    SistemaGestion "1" o-- "0..*" Reserva : administra

    Exception <|-- ClienteInvalidoError
    Exception <|-- ServicioNoDisponibleError
    Exception <|-- ReservaInvalidaError
    Exception <|-- DuracionInvalidaError
    Exception <|-- ParametroObligatorioError
    Exception <|-- EstadoReservaError
    Exception <|-- CalculoCostoError
    Exception <|-- ArchivoError
