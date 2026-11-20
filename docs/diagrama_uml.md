classDiagram
    class EntidadBase {
        <<abstract>>
        +__str__() str
        +to_dict() dict
    }

    class Client {
        -__nombre: str
        -__documento: str
        -__contacto: str
        -__id: int
        +nombre: str
        +documento: str
        +contacto: str
        +id: int
        +__str__() str
        +to_dict() dict
    }

    class Servicio {
        <<abstract>>
        -_id_servicio: str
        -_nombre: str
        -_costo_base: float
        +id_servicio: str
        +nombre: str
        +costo_base: float
        +calcular_costo(duración: int, **kwargs) float
        +__str__() str
        +to_dict() dict
    }

    class ReservaSala {
        -_capacidad: int
        +capacidad: int
        +calcular_costo(duración: int, impuesto: float, descuento: float, personas: int) float
        +__str__() str
        +to_dict() dict
    }

    class AlquilerEquipo {
        -_equipo: str
        -_estado: str
        +equipo: str
        +estado: str
        +cambiar_estado(nuevo_estado: str)
        +calcular_costo(duración: int, daño: bool, limpieza: bool) float
        +__str__() str
        +to_dict() dict
    }

    class AsesoriaEspecializada {
        -_temática: str
        -_duración_maxima: int
        +temática: str
        +duración_maxima: int
        +calcular_costo(duración: int, preparacion: bool, material: bool) float
        +__str__() str
        +to_dict() dict
    }

    class Reserva {
        -_cliente: Client
        -_servicio: Servicio
        -_duración: int
        -_fecha: date
        -_estado: str
        -_fecha_creacion: datetime
        -_costo_calculado: float
        +cliente: Client
        +servicio: Servicio
        +duración: int
        +fecha: date
        +estado: str
        +fecha_creacion: datetime
        +confirmar() bool
        +cancelar() bool
        +completar() bool
        +calcular_costo(**kwargs) float
        +__str__() str
        +to_dict() dict
    }

    class ClienteInvalidoError
    class ServicioNoDisponibleError
    class ReservaInvalidaError
    class DuraciónInvalidaError
    class ParametroObligatorioError
    class EstadoReservaError
    class CalculoCostoError

    EntidadBase <|-- Client
    EntidadBase <|-- Servicio
    Servicio <|-- ReservaSala
    Servicio <|-- AlquilerEquipo
    Servicio <|-- AsesoriaEspecializada
    Reserva o-- Client
    Reserva o-- Servicio