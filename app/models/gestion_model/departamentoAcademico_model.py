import sqlite3
import logging
from app.models.database import create_connection

class DepartamentoAcademicoModel:

    ####################### CRUD #######################

    @staticmethod
    def create_departamento_academico(nombre_departamento):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO Departamento_Academico (nombre_departamento)
                VALUES (?)
            ''', (nombre_departamento,))
            conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            logging.error(f"Error al crear departamento académico: {e}")
        finally:
            conn.close()

    @staticmethod
    def read_departamento_academico(id_departamento):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Departamento_Academico WHERE id_departamento = ?", (id_departamento,))
            return cursor.fetchone()
        except sqlite3.Error as e:
            logging.error(f"Error al leer departamento académico: {e}")
        finally:
            conn.close()

    @staticmethod
    def update_departamento_academico(id_departamento, nombre_departamento):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE Departamento_Academico 
                SET nombre_departamento = ?
                WHERE id_departamento = ?
            ''', (nombre_departamento, id_departamento))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error al actualizar departamento académico: {e}")
        finally:
            conn.close()

    @staticmethod
    def delete_departamento_academico(id_departamento):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Departamento_Academico WHERE id_departamento = ?", (id_departamento,))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error al eliminar departamento académico: {e}")
        finally:
            conn.close()

    ####################### OTROS BÁSICOS #######################
    
    @staticmethod
    def list_all_departamentos_academicos():
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Departamento_Academico")
            return cursor.fetchall()
        except sqlite3.Error as e:
            logging.error(f"Error al listar los departamentos académicos: {e}")
        finally:
            conn.close()
