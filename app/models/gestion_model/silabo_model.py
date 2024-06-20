import sqlite3
import logging
from app.models.database import create_connection

class SilaboModel:

    ####################### CRUD #######################

    @staticmethod
    def create_silabo(id_asignatura, id_semestre, rutaArchivo_sil):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO Silabo (id_asignatura, id_semestre, rutaArchivo_sil)
                VALUES (?, ?, ?)
            ''', (id_asignatura, id_semestre, rutaArchivo_sil))
            conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            logging.error(f"Error al crear silabo: {e}")
        finally:
            conn.close()

    @staticmethod
    def read_silabo(id_sil):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Silabo WHERE id_sil = ?", (id_sil,))
            return cursor.fetchone()
        except sqlite3.Error as e:
            logging.error(f"Error al leer silabo: {e}")
        finally:
            conn.close()

    @staticmethod
    def update_silabo(id_sil, id_asignatura, id_semestre, rutaArchivo_sil):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE Silabo 
                SET id_asignatura = ?, id_semestre = ?, rutaArchivo_sil = ?
                WHERE id_sil = ?
            ''', (id_asignatura, id_semestre, rutaArchivo_sil, id_sil))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error al actualizar silabo: {e}")
        finally:
            conn.close()

    @staticmethod
    def delete_silabo(id_sil):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Silabo WHERE id_sil = ?", (id_sil,))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error al eliminar silabo: {e}")
        finally:
            conn.close()

    ####################### OTROS BÁSICOS #######################

    @staticmethod
    def list_all_silabos():
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Silabo")
            return cursor.fetchall()
        except sqlite3.Error as e:
            logging.error(f"Error al listar los silabos: {e}")
        finally:
            conn.close()
