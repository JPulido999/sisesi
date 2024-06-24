import sqlite3
import logging
from app.models.database import create_connection

class LicenciaModel:

    ####################### CRUD #######################

    @staticmethod
    def create_licencia(resolucion_licencia, fechaInicio_licencia, fechaFin_licencia, observacion_licencia, id_tipoLicencia, id_docente):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO Licencia (resolucion_licencia, fechaInicio_licencia, fechaFin_licencia, observacion_licencia, id_tipoLicencia, id_docente)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (resolucion_licencia, fechaInicio_licencia, fechaFin_licencia, observacion_licencia, id_tipoLicencia, id_docente))
            conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            logging.error(f"Error al crear licencia: {e}")
        finally:
            conn.close()

    @staticmethod
    def read_licencia(id_licencia):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Licencia WHERE id_licencia = ?", (id_licencia,))
            return cursor.fetchone()
        except sqlite3.Error as e:
            logging.error(f"Error al leer licencia: {e}")
        finally:
            conn.close()

    @staticmethod
    def update_licencia(id_licencia, resolucion_licencia, fechaInicio_licencia, fechaFin_licencia, observacion_licencia, id_tipoLicencia, id_docente):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE Licencia 
                SET resolucion_licencia = ?, fechaInicio_licencia = ?, fechaFin_licencia = ?, observacion_licencia = ?, id_tipoLicencia = ?, id_docente = ?
                WHERE id_licencia = ?
            ''', (resolucion_licencia, fechaInicio_licencia, fechaFin_licencia, observacion_licencia, id_tipoLicencia, id_docente, id_licencia))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error al actualizar licencia: {e}")
        finally:
            conn.close()

    @staticmethod
    def delete_licencia(id_licencia):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Licencia WHERE id_licencia = ?", (id_licencia,))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error al eliminar licencia: {e}")
        finally:
            conn.close()

    ####################### OTROS BÁSICOS #######################

    @staticmethod
    def list_all_licencias():
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Licencia")
            return cursor.fetchall()
        except sqlite3.Error as e:
            logging.error(f"Error al listar las licencias: {e}")
        finally:
            conn.close()
    
    
    @staticmethod
    def buscar_licencia_por_resolucion(resolucion):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM Licencia WHERE resolucion_licencia = ?", (resolucion,))
            return cursor.fetchone()[0]
        except sqlite3.Error as e:
            logging.error(f"Error al buscar licencia por resolucion: {e}")
        finally:
            conn.close()
