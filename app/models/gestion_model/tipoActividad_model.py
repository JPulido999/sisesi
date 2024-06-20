import sqlite3
import logging
from app.models.database import create_connection

class TipoActividadModel:

    ####################### CRUD #######################

    @staticmethod
    def create_tipo_actividad(nombre_tipoActividad, sigla_tipoActividad, id_actividad):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO Tipo_Actividad (nombre_tipoActividad, sigla_tipoActividad, id_actividad)
                VALUES (?, ?, ?)
            ''', (nombre_tipoActividad, sigla_tipoActividad, id_actividad))
            conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            logging.error(f"Error al crear tipo de actividad: {e}")
        finally:
            conn.close()

    @staticmethod
    def read_tipo_actividad(id_tipoActividad):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Tipo_Actividad WHERE id_tipoActividad = ?", (id_tipoActividad,))
            return cursor.fetchone()
        except sqlite3.Error as e:
            logging.error(f"Error al leer tipo de actividad: {e}")
        finally:
            conn.close()

    @staticmethod
    def update_tipo_actividad(id_tipoActividad, nombre_tipoActividad, sigla_tipoActividad, id_actividad):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE Tipo_Actividad 
                SET nombre_tipoActividad = ?, sigla_tipoActividad = ?, id_actividad = ?
                WHERE id_tipoActividad = ?
            ''', (nombre_tipoActividad, sigla_tipoActividad, id_actividad, id_tipoActividad))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error al actualizar tipo de actividad: {e}")
        finally:
            conn.close()

    @staticmethod
    def delete_tipo_actividad(id_tipoActividad):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Tipo_Actividad WHERE id_tipoActividad = ?", (id_tipoActividad,))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error al eliminar tipo de actividad: {e}")
        finally:
            conn.close()

    ####################### OTROS BÁSICOS #######################
    
    @staticmethod
    def list_all_tipo_actividades():
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Tipo_Actividad")
            return cursor.fetchall()
        except sqlite3.Error as e:
            logging.error(f"Error al listar los tipos de actividad: {e}")
        finally:
            conn.close()
