import sqlite3
import logging
from app.models.database import create_connection

class PlanEstudiosModel:

    ####################### CRUD #######################

    @staticmethod
    def create_plan_estudios(nombre_plan, id_escuela):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO Plan_Estudios (nombre_plan, id_escuela)
                VALUES (?, ?)
            ''', (nombre_plan, id_escuela))
            conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            logging.error(f"Error al crear plan de estudios: {e}")
        finally:
            conn.close()

    @staticmethod
    def read_plan_estudios(id_plan):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Plan_Estudios WHERE id_plan = ?", (id_plan,))
            return cursor.fetchone()
        except sqlite3.Error as e:
            logging.error(f"Error al leer plan de estudios: {e}")
        finally:
            conn.close()

    @staticmethod
    def update_plan_estudios(id_plan, nombre_plan, id_escuela):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE Plan_Estudios 
                SET nombre_plan = ?, id_escuela = ?
                WHERE id_plan = ?
            ''', (nombre_plan, id_escuela, id_plan))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error al actualizar plan de estudios: {e}")
        finally:
            conn.close()

    @staticmethod
    def delete_plan_estudios(id_plan):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Plan_Estudios WHERE id_plan = ?", (id_plan,))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error al eliminar plan de estudios: {e}")
        finally:
            conn.close()

    ####################### OTROS BÁSICOS #######################
    
    @staticmethod
    def list_all_planes_estudios():
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Plan_Estudios")
            return cursor.fetchall()
        except sqlite3.Error as e:
            logging.error(f"Error al listar los planes de estudios: {e}")
        finally:
            conn.close()
