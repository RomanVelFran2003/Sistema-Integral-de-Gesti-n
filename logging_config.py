9.
"""
logging_config.py - Configuración del sistema de registros (logs).
"""

import logging
from datetime import datetime
from pathlib import Path


def configurar_logging() -> logging.Logger:
    """
    Configura los registros generales, errores y mensajes de consola.
    """

    # Crear la carpeta logs dentro del proyecto.
    directorio_logs = Path(__file__).resolve().parent / "logs"
    directorio_logs.mkdir(parents=True, exist_ok=True)

    # Obtener el logger principal.
    logger = logging.getLogger("SoftwareFJ")
    logger.setLevel(logging.DEBUG)
    logger.propagate = False

    # Evitar que se dupliquen los registros al configurar nuevamente.
    for handler in logger.handlers[:]:
        handler.close()
        logger.removeHandler(handler)

    fecha = datetime.now().strftime("%Y%m%d")

    formato = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Archivo para todos los eventos.
    archivo_general = logging.FileHandler(
        directorio_logs / f"software_fj_{fecha}.log",
        encoding="utf-8"
    )
    archivo_general.setLevel(logging.INFO)
    archivo_general.setFormatter(formato)

    # Archivo exclusivo para errores.
    archivo_errores = logging.FileHandler(
        directorio_logs / f"errores_{fecha}.log",
        encoding="utf-8"
    )
    archivo_errores.setLevel(logging.ERROR)
    archivo_errores.setFormatter(formato)

    # Mostrar los registros también en la consola.
    consola = logging.StreamHandler()
    consola.setLevel(logging.INFO)
    consola.setFormatter(formato)

    logger.addHandler(archivo_general)
    logger.addHandler(archivo_errores)
    logger.addHandler(consola)

    return logger


# Logger disponible para los demás módulos.
logger = configurar_logging()