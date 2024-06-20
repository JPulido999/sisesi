import sqlite3
import logging
from app.models.database import create_connection

class SemestreModel:

    ####################### CRUD #######################

    @staticmethod
    def create_semestre(nombre_semestre, duracion_semestre, fechaInicio_semestre, fechaFin_semestre, estado_semestre):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO Semestre (nombre_semestre, duracion_semestre, fechaInicio_semestre, fechaFin_semestre, estado_semestre)
                VALUES (?, ?, ?, ?, ?)
            ''', (nombre_semestre, duracion_semestre, fechaInicio_semestre, fechaFin_semestre, estado_semestre))
            conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            logging.error(f"Error al crear semestre: {e}")
        finally:
            conn.close()

    @staticmethod
    def read_semestre(id_semestre):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Semestre WHERE id_semestre = ?", (id_semestre,))
            return cursor.fetchone()
        except sqlite3.Error as e:
            logging.error(f"Error al leer semestre: {e}")
        finally:
            conn.close()

    @staticmethod
    def update_semestre(id_semestre, nombre_semestre, duracion_semestre, fechaInicio_semestre, fechaFin_semestre, estado_semestre):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE Semestre 
                SET nombre_semestre = ?, duracion_semestre = ?, fechaInicio_semestre = ?, fechaFin_semestre = ?, estado_semestre = ?
                WHERE id_semestre = ?
            ''', (nombre_semestre, duracion_semestre, fechaInicio_semestre, fechaFin_semestre, estado_semestre, id_semestre))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error al actualizar semestre: {e}")
        finally:
            conn.close()

    @staticmethod
    def delete_semestre(id_semestre):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Semestre WHERE id_semestre = ?", (id_semestre,))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error al eliminar semestre: {e}")
        finally:
            conn.close()

    ####################### OTROS BÁSICOS #######################
    
    @staticmethod
    def list_all_semestres():
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Semestre")
            return cursor.fetchall()
        except sqlite3.Error as e:
            logging.error(f"Error al listar los semestres: {e}")
        finally:
            conn.close()
