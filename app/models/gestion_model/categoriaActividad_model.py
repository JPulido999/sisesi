import sqlite3
import logging
from app.models.database import create_connection

class CategoriaActividadModel:

    ####################### CRUD #######################

    @staticmethod
    def create_categoria_actividad(nombre_categoriaActividad):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO Categoria_Actividad (nombre_categoriaActividad)
                VALUES (?)
            ''', (nombre_categoriaActividad,))
            conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            logging.error(f"Error al crear categoría de actividad: {e}")
        finally:
            conn.close()

    @staticmethod
    def read_categoria_actividad(id_categoriaActividad):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Categoria_Actividad WHERE id_categoriaActividad = ?", (id_categoriaActividad,))
            return cursor.fetchone()
        except sqlite3.Error as e:
            logging.error(f"Error al leer categoría de actividad: {e}")
        finally:
            conn.close()

    @staticmethod
    def update_categoria_actividad(id_categoriaActividad, nombre_categoriaActividad):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE Categoria_Actividad 
                SET nombre_categoriaActividad = ?
                WHERE id_categoriaActividad = ?
            ''', (nombre_categoriaActividad, id_categoriaActividad))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error al actualizar categoría de actividad: {e}")
        finally:
            conn.close()

    @staticmethod
    def delete_categoria_actividad(id_categoriaActividad):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Categoria_Actividad WHERE id_categoriaActividad = ?", (id_categoriaActividad,))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error al eliminar categoría de actividad: {e}")
        finally:
            conn.close()

    ####################### OTROS BÁSICOS #######################

    @staticmethod
    def list_all_categoria_actividades():
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Categoria_Actividad")
            return cursor.fetchall()
        except sqlite3.Error as e:
            logging.error(f"Error al listar las categorías de actividades: {e}")
        finally:
            conn.close()
