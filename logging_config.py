"""
logging_config.py - Configuración del sistema de logging profesional.
"""
import logging
import os
from datetime import datetime

def configurar_logging() -> logging.Logger:
    """
    Configura el sistema de logging con múltiples niveles y salidas.
    
    Returns:
        logging.Logger: Logger configurado
    """
    # Crear directorio de logs si no existe
    log_dir = 'logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # Configurar logger principal
    logger = logging.getLogger('SoftwareFJ')
    logger.setLevel(logging.DEBUG)  # Capturar todos los niveles
    
    # Evitar duplicación de handlers
    if logger.handlers:
        logger.handlers.clear()
    
    # Formato detallado
    formato_detallado = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Handler para archivo principal (todos los niveles)
    archivo_principal = logging.FileHandler(
        f'logs/software_fj_{datetime.now().strftime("%Y%m%d")}.log',
        encoding='utf-8'
    )
    archivo_principal.setLevel(logging.DEBUG)
    archivo_principal.setFormatter(formato_detallado)
    
    # Handler para errores (solo ERROR y CRITICAL)
    archivo_errores = logging.FileHandler(
        f'logs/software_fj_errores_{datetime.now().strftime("%Y%m%d")}.log',
        encoding='utf-8'
    )
    archivo_errores.setLevel(logging.ERROR)
    archivo_errores.setFormatter(formato_detallado)
    
    # Handler para consola (desarrollo)
    consola = logging.StreamHandler()
    consola.setLevel(logging.INFO)
    consola.setFormatter(formato_detallado)
    
    # Agregar handlers al logger
    logger.addHandler(archivo_principal)
    logger.addHandler(archivo_errores)
    logger.addHandler(consola)
    
    return logger

# Logger global para el sistema
logger = configurar_logging()