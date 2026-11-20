# Sistema Integral de Gestion de Clientes, Servicios y Reservas

## Software FJ

## 1. Descripcion del proyecto

El Sistema Integral de Gestion de Clientes, Servicios y Reservas es una aplicacion desarrollada en Python utilizando el paradigma de programacion orientada a objetos (POO).

Su objetivo es facilitar la administracion de clientes, servicios y reservas de Software FJ, permitiendo registrar informacion, calcular costos, controlar la disponibilidad de los servicios y gestionar los diferentes estados de las reservas.

El sistema utiliza estructuras de datos en memoria, sin necesidad de una base de datos. Ademas, incorpora archivos de registro para almacenar eventos y errores durante la ejecucion.

## 2. Objetivo general

Desarrollar una aplicacion en Python que permita gestionar clientes, servicios y reservas mediante los principios de programacion orientada a objetos, aplicando encapsulamiento, herencia, abstraccion, polimorfismo y manejo de excepciones.

## 3. Caracteristicas principales

- Registro y validacion de clientes.
- Administracion de diferentes tipos de servicios.
- Creacion, confirmacion, cancelacion y finalizacion de reservas.
- Calculo de costos segun el tipo de servicio.
- Aplicacion de impuestos, descuentos y cargos adicionales.
- Validacion de disponibilidad de equipos.
- Manejo de excepciones personalizadas.
- Registro de eventos y errores mediante archivos de log.
- Simulacion de operaciones validas e invalidas.
- Pruebas automaticas utilizando unittest.

## 4. Programacion orientada a objetos

El proyecto aplica los siguientes principios:

### Encapsulamiento

Se utilizan atributos privados y propiedades para proteger la informacion de los clientes y administrar los datos de las entidades.

### Herencia

Las clases Cliente y Servicio heredan de EntidadBase. Las clases ReservaSala, AlquilerEquipo y AsesoriaEspecializada heredan de Servicio.

### Abstraccion

EntidadBase y Servicio son clases abstractas que establecen una estructura comun para las clases derivadas.

### Polimorfismo

Cada tipo de servicio implementa su propia version del metodo calcular_costo(), permitiendo calcular los valores de acuerdo con sus caracteristicas.

## 5. Estructura del proyecto

```text
Sistema-Integral-de-Gestion/
│
├── main.py
├── entidad_base.py
├── cliente.py
├── servicio.py
├── reserva.py
├── reserva_sala.py
├── alquiler_equipo.py
├── asesoria_especializada.py
├── excepciones.py
├── logging_config.py
├── README.md
├── .gitignore
├── .gitattributes
│
├── logs/
│   ├── software_fj_YYYYMMDD.log
│   └── errores_YYYYMMDD.log
│
└── tests/
    └── test_simulaciones.py
```

Los archivos de registro se generan automaticamente durante la ejecucion. La carpeta logs no necesita contener archivos antes de iniciar el programa.

## 6. Requisitos del sistema

- Python 3.9 o superior.
- Visual Studio Code o cualquier editor de codigo.
- Git para administrar el repositorio.
- No requiere instalar bibliotecas externas para ejecutar el programa principal.

## 7. Instalacion y ejecucion

### Paso 1. Descargar el proyecto

Clonar el repositorio desde GitHub:

```bash
git clone https://github.com/RomanVelFran2003/Sistema-Integral-de-Gesti-n.git
```

### Paso 2. Ingresar a la carpeta

```bash
cd Sistema-Integral-de-Gesti-n
```

### Paso 3. Ejecutar el programa

```bash
python main.py
```

En algunos sistemas puede ser necesario utilizar:

```bash
python3 main.py
```

## 8. Ejecucion de pruebas automaticas

Para ejecutar las pruebas unitarias desde la carpeta principal:

```bash
python -m unittest discover -s tests -v
```

Estas pruebas permiten verificar el funcionamiento de las clases, las validaciones, los calculos de costos y el manejo de excepciones.

## 9. Manejo de excepciones y registros

El sistema implementa excepciones personalizadas para controlar errores relacionados con clientes, servicios, reservas, duraciones, estados y calculos de costos.

Tambien utiliza el modulo logging de Python para registrar eventos y errores en archivos independientes dentro de la carpeta logs.

Esto permite identificar problemas durante la ejecucion sin detener innecesariamente el funcionamiento de la aplicacion.

## 10. Alcance del proyecto

La aplicacion permite simular operaciones de gestion de clientes, servicios y reservas. La informacion se conserva en memoria mientras el programa esta en ejecucion.

No utiliza una base de datos ni implementa almacenamiento permanente de clientes, servicios o reservas.

## 11. Autores

Proyecto academico desarrollado para la actividad de programacion en Python.

**Empresa simulada:** Software FJ.

**Tecnologia principal:** Python.

**Paradigma:** Programacion orientada a objetos.
