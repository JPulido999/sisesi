import sqlite3
import logging
from app.models.database import create_connection

class EscuelaModel:
    @staticmethod
    def create_escuela(nombre, id_facultad):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Escuela (nombre_escuela, id_facultad) VALUES (?, ?)", (nombre, id_facultad))
            conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            logging.error(f"Error al crear escuela: {e}")
        finally:
            conn.close()

    @staticmethod
    def read_escuela(id_escuela):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Escuela WHERE id_escuela = ?", (id_escuela,))
            return cursor.fetchone()
        except sqlite3.Error as e:
            logging.error(f"Error al leer escuela: {e}")
        finally:
            conn.close()

    @staticmethod
    def update_escuela(id_escuela, nombre, id_facultad):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE Escuela SET nombre_escuela = ?, id_facultad = ? WHERE id_escuela = ?", (nombre, id_facultad, id_escuela))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error al actualizar escuela: {e}")
        finally:
            conn.close()

    @staticmethod
    def delete_escuela(id_escuela):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Escuela WHERE id_escuela = ?", (id_escuela,))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error al eliminar escuela: {e}")
        finally:
            conn.close()

    ####################### otros ###################
    
    @staticmethod
    def list_all_escuela():
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Escuela")
            return cursor.fetchall()
        except sqlite3.Error as e:
            logging.error(f"Error al listar las Escuelas: {e}")
        finally:
            conn.close()

    @staticmethod
    def buscar_escuela_por_id(id_escuela):
        return EscuelaModel.read_escuela(id_escuela)

    @staticmethod
    def buscar_escuela_por_nombre(nombre):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Escuela WHERE nombre_escuela = ?", (nombre,))
            return cursor.fetchall()
        except sqlite3.Error as e:
            logging.error(f"Error al buscar escuela por nombre: {e}")
        finally:
            conn.close()
