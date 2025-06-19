import logging
import os
from logging.handlers import RotatingFileHandler


def setup_logger(name):
    # Crea directorio de logs si no existe
    os.makedirs('logs', exist_ok=True)

    # Configuración básica
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  # Captura todos los niveles

    # Formato de los mensajes
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Handler para archivo (rotativo)
    file_handler = RotatingFileHandler(
        'logs/app.log',
        maxBytes=1024 * 1024,  # 1MB
        backupCount=3
    )
    file_handler.setFormatter(formatter)

    # Handler para consola
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Añadir handlers al logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger