
from database.connection import create_connection
from utils.logger import setup_logger

logger = setup_logger(__name__)


class ProductoService:
    @staticmethod
    def obtener_por_id(producto_id):
        try:
            if not isinstance(producto_id, int) or producto_id <= 0:
                logger.error(f"ID inválido recibido: {producto_id}")
                raise ValueError("ID debe ser entero positivo")

            conn = create_connection()
            if not conn:
                logger.critical("Conexión a DB fallida")
                return None

            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM productos WHERE id = %s", (producto_id,))
                resultado = cursor.fetchone()

                if not resultado:
                    logger.warning(f"Producto no encontrado (ID: {producto_id})")
                    return None

                logger.info(f"Producto recuperado (ID: {producto_id})")
                return resultado

        except Exception as e:
            logger.exception(f"Error inesperado: {str(e)}")
            return None
        finally:
            if conn:
                conn.close()