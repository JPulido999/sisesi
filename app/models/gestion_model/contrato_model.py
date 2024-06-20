import sqlite3
import logging
from app.models.database import create_connection

class ContratoModel:

        ####################### CRUD #######################

    @staticmethod
    def create_contrato(periodoInicio, periodoFin, id_docente, renacyt, id_condicion, id_regimen, id_categoria):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO Contrato (periodoInicio_contrato, periodoFin_contrato, id_docente, renacyt_contrato, id_condicion, id_regimen, id_categoria)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (periodoInicio, periodoFin, id_docente, renacyt, id_condicion, id_regimen, id_categoria))
            conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            logging.error(f"Error al crear contrato: {e}")
        finally:
            conn.close()

    @staticmethod
    def read_contrato(id_contrato):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Contrato WHERE id_contrato = ?", (id_contrato,))
            return cursor.fetchone()
        except sqlite3.Error as e:
            logging.error(f"Error al leer contrato: {e}")
        finally:
            conn.close()

    @staticmethod
    def update_contrato(id_contrato, periodoInicio, periodoFin, id_docente, renacyt, id_condicion, id_regimen, id_categoria):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE Contrato 
                SET periodoInicio_contrato = ?, periodoFin_contrato = ?, id_docente = ?, renacyt_contrato = ?, id_condicion = ?, id_regimen = ?, id_categoria = ?
                WHERE id_contrato = ?
            ''', (periodoInicio, periodoFin, id_docente, renacyt, id_condicion, id_regimen, id_categoria, id_contrato))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error al actualizar contrato: {e}")
        finally:
            conn.close()

    @staticmethod
    def delete_contrato(id_contrato):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Contrato WHERE id_contrato = ?", (id_contrato,))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error al eliminar contrato: {e}")
        finally:
            conn.close()

    ####################### OTROS BÁSICOS #######################
    
    @staticmethod
    def list_all_contrato():
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Contrato")
            return cursor.fetchall()
        except sqlite3.Error as e:
            logging.error(f"Error al listar los contratos: {e}")
        finally:
            conn.close()

    @staticmethod
    def buscar_contrato_por_id(id_contrato):
        return ContratoModel.read_contrato(id_contrato)

    @staticmethod
    def buscar_contrato_por_docente(id_docente):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Contrato WHERE id_docente = ?", (id_docente,))
            return cursor.fetchall()
        except sqlite3.Error as e:
            logging.error(f"Error al buscar contrato por docente: {e}")
        finally:
            conn.close()

    ####################### PERSONALIZADOS #######################

    @staticmethod
    def insert_contrato_desde_excel(contrato_data):
        try:
            """Insertar datos del contrato en la tabla Contrato"""
            sql = '''
            INSERT INTO Contrato (renacyt_contrato, id_condicion, id_regimen, id_categoria, id_docente)
            VALUES (?, ?, ?, ?, ?)
            '''
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute(sql, (contrato_data["renacyt_contrato"], contrato_data["id_condicion"],
                            contrato_data["id_regimen"], contrato_data["id_categoria"], contrato_data["id_docente"]))
            conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            logging.error(f"Error al insertar contrato desde un excel: {e}")
        finally:
            conn.close()