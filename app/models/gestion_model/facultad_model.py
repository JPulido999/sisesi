import sqlite3
import logging
from app.models.database import create_connection

class FacultadModel:
    @staticmethod
    def create_facultad(sigla, nombre):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Facultad (sigla_facultad, nombre_facultad) VALUES (?, ?)", (sigla, nombre))
            conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            logging.error(f"Error al crear facultad: {e}")
        finally:
            conn.close()

    @staticmethod
    def read_facultad(id_facultad):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Facultad WHERE id_facultad = ?", (id_facultad,))
            return cursor.fetchone()
        except sqlite3.Error as e:
            logging.error(f"Error al leer facultad: {e}")
        finally:
            conn.close()

    @staticmethod
    def update_facultad(id_facultad, sigla, nombre):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE Facultad SET sigla_facultad = ?, nombre_facultad = ? WHERE id_facultad = ?", (sigla, nombre, id_facultad))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error al actualizar facultad: {e}")
        finally:
            conn.close()

    @staticmethod
    def delete_facultad(id_facultad):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Facultad WHERE id_facultad = ?", (id_facultad,))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error al eliminar facultad: {e}")
        finally:
            conn.close()

    ####################### otros ###################
    
    @staticmethod
    def list_all_facultad():
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Facultad")
            return cursor.fetchall()
        except sqlite3.Error as e:
            logging.error(f"Error al listar las facultades: {e}")
        finally:
            conn.close()

    @staticmethod
    def buscar_facultad_por_id(id_facultad):
        return FacultadModel.read_facultad(id_facultad)

    @staticmethod
    def buscar_facultad_por_nombre(nombre):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Facultad WHERE nombre_facultad = ?", (nombre,))
            return cursor.fetchall()
        except sqlite3.Error as e:
            logging.error(f"Error al buscar facultad por nombre: {e}")
        finally:
            conn.close()
