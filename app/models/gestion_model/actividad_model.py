import sqlite3
import logging
from app.models.database import create_connection

class ActividadModel:

    ####################### CRUD #######################

    @staticmethod
    def create_actividad(nombre_actividad, id_categoriaActividad):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO Actividad (nombre_actividad, id_categoriaActividad)
                VALUES (?, ?)
            ''', (nombre_actividad, id_categoriaActividad))
            conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            logging.error(f"Error al crear actividad: {e}")
        finally:
            conn.close()

    @staticmethod
    def read_actividad(id_actividad):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Actividad WHERE id_actividad = ?", (id_actividad,))
            return cursor.fetchone()
        except sqlite3.Error as e:
            logging.error(f"Error al leer actividad: {e}")
        finally:
            conn.close()

    @staticmethod
    def update_actividad(id_actividad, nombre_actividad, id_categoriaActividad):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE Actividad 
                SET nombre_actividad = ?, id_categoriaActividad = ?
                WHERE id_actividad = ?
            ''', (nombre_actividad, id_categoriaActividad, id_actividad))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error al actualizar actividad: {e}")
        finally:
            conn.close()

    @staticmethod
    def delete_actividad(id_actividad):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Actividad WHERE id_actividad = ?", (id_actividad,))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error al eliminar actividad: {e}")
        finally:
            conn.close()

    ####################### OTROS BÁSICOS #######################
    
    @staticmethod
    def list_all_actividades():
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Actividad")
            return cursor.fetchall()
        except sqlite3.Error as e:
            logging.error(f"Error al listar las actividades: {e}")
        finally:
            conn.close()
