import sqlite3
import logging
from app.models.database import create_connection

class TipoLicenciaModel:

    ####################### CRUD #######################

    @staticmethod
    def create_tipo_licencia(nombre_tipoLicencia):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO Tipo_Licencia (nombre_tipoLicencia)
                VALUES (?)
            ''', (nombre_tipoLicencia,))
            conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            logging.error(f"Error al crear tipo de licencia: {e}")
        finally:
            conn.close()

    @staticmethod
    def read_tipo_licencia(id_tipoLicencia):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Tipo_Licencia WHERE id_tipoLicencia = ?", (id_tipoLicencia,))
            return cursor.fetchone()
        except sqlite3.Error as e:
            logging.error(f"Error al leer tipo de licencia: {e}")
        finally:
            conn.close()

    @staticmethod
    def update_tipo_licencia(id_tipoLicencia, nombre_tipoLicencia):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE Tipo_Licencia 
                SET nombre_tipoLicencia = ?
                WHERE id_tipoLicencia = ?
            ''', (nombre_tipoLicencia, id_tipoLicencia))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error al actualizar tipo de licencia: {e}")
        finally:
            conn.close()

    @staticmethod
    def delete_tipo_licencia(id_tipoLicencia):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Tipo_Licencia WHERE id_tipoLicencia = ?", (id_tipoLicencia,))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error al eliminar tipo de licencia: {e}")
        finally:
            conn.close()

    ####################### OTROS BÁSICOS #######################
    
    @staticmethod
    def list_all_tipo_licencias():
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Tipo_Licencia")
            return cursor.fetchall()
        except sqlite3.Error as e:
            logging.error(f"Error al listar los tipos de licencia: {e}")
        finally:
            conn.close()
