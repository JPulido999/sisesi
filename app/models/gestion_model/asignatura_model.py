import sqlite3
import logging
from app.models.database import create_connection

class AsignaturaModel:

    ####################### CRUD #######################

    @staticmethod
    def create_asignatura(nombre_asignatura, codigo_asignatura, id_tipoAsignatura, id_planEstudios):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO Asignatura (nombre_asignatura, codigo_asignatura, id_tipoAsignatura, id_planEstudios)
                VALUES (?, ?, ?, ?)
            ''', (nombre_asignatura, codigo_asignatura, id_tipoAsignatura, id_planEstudios))
            conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            logging.error(f"Error al crear asignatura: {e}")
        finally:
            conn.close()

    @staticmethod
    def read_asignatura(id_asignatura):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Asignatura WHERE id_asignatura = ?", (id_asignatura,))
            return cursor.fetchone()
        except sqlite3.Error as e:
            logging.error(f"Error al leer asignatura: {e}")
        finally:
            conn.close()

    @staticmethod
    def update_asignatura(id_asignatura, nombre_asignatura, codigo_asignatura, id_tipoAsignatura, id_planEstudios):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE Asignatura 
                SET nombre_asignatura = ?, codigo_asignatura = ?, id_tipoAsignatura = ?, id_planEstudios = ?
                WHERE id_asignatura = ?
            ''', (nombre_asignatura, codigo_asignatura, id_tipoAsignatura, id_planEstudios, id_asignatura))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error al actualizar asignatura: {e}")
        finally:
            conn.close()

    @staticmethod
    def delete_asignatura(id_asignatura):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Asignatura WHERE id_asignatura = ?", (id_asignatura,))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error al eliminar asignatura: {e}")
        finally:
            conn.close()

    ####################### OTROS BÁSICOS #######################

    @staticmethod
    def list_all_asignaturas():
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Asignatura")
            return cursor.fetchall()
        except sqlite3.Error as e:
            logging.error(f"Error al listar las asignaturas: {e}")
        finally:
            conn.close()
