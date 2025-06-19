
from utils.logger import setup_logger
from database.models import Producto
from services.producto_service import ProductoService

logger = setup_logger(__name__)


def main():
    logger.info("Iniciando aplicación...")

    try:
        producto = ProductoService.obtener_por_id(1)
        if producto:
            logger.debug(f"Datos obtenidos: {producto}")
    except Exception as e:
        logger.critical(f"Error fatal: {str(e)}", exc_info=True)
        raise


if __name__ == "__main__":
    main()