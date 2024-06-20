import sqlite3
import logging
from app.models.database import create_connection

class UnidadModel:

    ####################### CRUD #######################

    @staticmethod
    def create_unidad(numero_unidad, id_sil):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO Unidad (numero_unidad, id_sil)
                VALUES (?, ?)
            ''', (numero_unidad, id_sil))
            conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            logging.error(f"Error al crear unidad: {e}")
        finally:
            conn.close()

    @staticmethod
    def read_unidad(id_unidad):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Unidad WHERE id_unidad = ?", (id_unidad,))
            return cursor.fetchone()
        except sqlite3.Error as e:
            logging.error(f"Error al leer unidad: {e}")
        finally:
            conn.close()

    @staticmethod
    def update_unidad(id_unidad, numero_unidad, id_sil):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE Unidad 
                SET numero_unidad = ?, id_sil = ?
                WHERE id_unidad = ?
            ''', (numero_unidad, id_sil, id_unidad))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error al actualizar unidad: {e}")
        finally:
            conn.close()

    @staticmethod
    def delete_unidad(id_unidad):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Unidad WHERE id_unidad = ?", (id_unidad,))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error al eliminar unidad: {e}")
        finally:
            conn.close()

    ####################### OTROS BÁSICOS #######################

    @staticmethod
    def list_all_unidades():
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Unidad")
            return cursor.fetchall()
        except sqlite3.Error as e:
            logging.error(f"Error al listar las unidades: {e}")
        finally:
            conn.close()
