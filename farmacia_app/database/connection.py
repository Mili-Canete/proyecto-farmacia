import psycopg2
from psycopg2 import OperationalError

def create_connection():
    try:
        conn = psycopg2.connect(
            database="farmacia_db",
            user="postgres",
            password="admin",
            host="localhost",
            port="5432"
        )
        return conn
    except OperationalError as e:
        print(f"Error al conectar a PostgreSQL: {e}")
        return None