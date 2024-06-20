import sqlite3
import logging
from app.models.database import create_connection

class SemanaModel:

    ####################### CRUD #######################

    @staticmethod
    def create_semana(nombre_semana, contenido_semana, id_unidad):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO Semana (nombre_semana, contenido_semana, id_unidad)
                VALUES (?, ?, ?)
            ''', (nombre_semana, contenido_semana, id_unidad))
            conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            logging.error(f"Error al crear semana: {e}")
        finally:
            conn.close()

    @staticmethod
    def read_semana(id_semana):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Semana WHERE id_semana = ?", (id_semana,))
            return cursor.fetchone()
        except sqlite3.Error as e:
            logging.error(f"Error al leer semana: {e}")
        finally:
            conn.close()

    @staticmethod
    def update_semana(id_semana, nombre_semana, contenido_semana, id_unidad):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE Semana 
                SET nombre_semana = ?, contenido_semana = ?, id_unidad = ?
                WHERE id_semana = ?
            ''', (nombre_semana, contenido_semana, id_unidad, id_semana))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error al actualizar semana: {e}")
        finally:
            conn.close()

    @staticmethod
    def delete_semana(id_semana):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Semana WHERE id_semana = ?", (id_semana,))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error al eliminar semana: {e}")
        finally:
            conn.close()

    ####################### OTROS BÁSICOS #######################

    @staticmethod
    def list_all_semanas():
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Semana")
            return cursor.fetchall()
        except sqlite3.Error as e:
            logging.error(f"Error al listar las semanas: {e}")
        finally:
            conn.close()
