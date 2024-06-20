import sqlite3
import logging
from app.models.database import create_connection

class CondicionModel:

    ####################### CRUD #######################

    @staticmethod
    def create_condicion(nombre_condicion):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO Condicion (nombre_condicion)
                VALUES (?)
            ''', (nombre_condicion,))
            conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            logging.error(f"Error al crear condición: {e}")
        finally:
            conn.close()

    @staticmethod
    def read_condicion(id_condicion):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Condicion WHERE id_condicion = ?", (id_condicion,))
            return cursor.fetchone()
        except sqlite3.Error as e:
            logging.error(f"Error al leer condición: {e}")
        finally:
            conn.close()

    @staticmethod
    def update_condicion(id_condicion, nombre_condicion):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE Condicion 
                SET nombre_condicion = ?
                WHERE id_condicion = ?
            ''', (nombre_condicion, id_condicion))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error al actualizar condición: {e}")
        finally:
            conn.close()

    @staticmethod
    def delete_condicion(id_condicion):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Condicion WHERE id_condicion = ?", (id_condicion,))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error al eliminar condición: {e}")
        finally:
            conn.close()

    ####################### OTROS BÁSICOS #######################
    
    @staticmethod
    def list_all_condiciones():
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Condicion")
            return cursor.fetchall()
        except sqlite3.Error as e:
            logging.error(f"Error al listar las condiciones: {e}")
        finally:
            conn.close()
