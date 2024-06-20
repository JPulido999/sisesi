import sqlite3
import logging
from app.models.database import create_connection

class RegimenModel:

    ####################### CRUD #######################

    @staticmethod
    def create_regimen(nombre_regimen):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO Regimen (nombre_regimen)
                VALUES (?)
            ''', (nombre_regimen,))
            conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            logging.error(f"Error al crear régimen: {e}")
        finally:
            conn.close()

    @staticmethod
    def read_regimen(id_regimen):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Regimen WHERE id_regimen = ?", (id_regimen,))
            return cursor.fetchone()
        except sqlite3.Error as e:
            logging.error(f"Error al leer régimen: {e}")
        finally:
            conn.close()

    @staticmethod
    def update_regimen(id_regimen, nombre_regimen):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE Regimen 
                SET nombre_regimen = ?
                WHERE id_regimen = ?
            ''', (nombre_regimen, id_regimen))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error al actualizar régimen: {e}")
        finally:
            conn.close()

    @staticmethod
    def delete_regimen(id_regimen):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Regimen WHERE id_regimen = ?", (id_regimen,))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error al eliminar régimen: {e}")
        finally:
            conn.close()

    ####################### OTROS BÁSICOS #######################
    
    @staticmethod
    def list_all_regimenes():
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Regimen")
            return cursor.fetchall()
        except sqlite3.Error as e:
            logging.error(f"Error al listar los regímenes: {e}")
        finally:
            conn.close()
