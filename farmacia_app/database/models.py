from database.connection import create_connection

class Producto:
    def __init__(self, id, nombre, descripcion, precio, stock):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock

    @staticmethod
    def crear_tabla():
        conn = create_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS productos (
                        id SERIAL PRIMARY KEY,
                        nombre VARCHAR(100) NOT NULL,
                        descripcion TEXT,
                        precio NUMERIC(10,2) NOT NULL,
                        stock INTEGER NOT NULL
                    );
                """)
                conn.commit()
                print("Tabla 'productos' creada exitosamente")
            except Exception as e:
                print(f"Error al crear tabla: {e}")
            finally:
                conn.close()