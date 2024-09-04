import sqlite3
import logging
from app.models.database import create_connection

class SeguimientoModel:

    ####################### CRUD #######################
    @staticmethod
    def create_seguimiento(dia_seguimiento, hora_seguimiento, obs1_seguimiento, obs2_seguimiento, obs3_seguimiento, obs4_seguimiento, obs5_seguimiento, comentarios_seguimiento, id_accion):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO Seguimiento (dia_seguimiento, hora_seguimiento, obs1_seguimiento, obs2_seguimiento, obs3_seguimiento, obs4_seguimiento, obs5_seguimiento, comentarios_seguimiento, id_accion)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (dia_seguimiento, hora_seguimiento, obs1_seguimiento, obs2_seguimiento, obs3_seguimiento, obs4_seguimiento, obs5_seguimiento, comentarios_seguimiento, id_accion))
            conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            logging.error(f"Error al crear seguimiento: {e}")
        finally:
            conn.close()

    @staticmethod
    def read_seguimiento(id_seguimiento):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Seguimiento WHERE id_seguimiento = ?", (id_seguimiento,))
            return cursor.fetchone()
        except sqlite3.Error as e:
            logging.error(f"Error al leer seguimiento: {e}")
        finally:
            conn.close()

    @staticmethod
    def update_seguimiento(dia_seguimiento, hora_seguimiento, obs1_seguimiento, obs2_seguimiento, obs3_seguimiento, obs4_seguimiento, obs5_seguimiento, comentarios_seguimiento, id_accion):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE Seguimiento 
                SET dia_seguimiento = ?, hora_seguimiento = ?, obs1_seguimiento = ?, obs2_seguimiento = ?, obs3_seguimiento = ?, obs4_seguimiento = ?, obs5_seguimiento = ?, comentarios_seguimiento = ?, id_accion = ?
                WHERE id_seguimiento = ?
            ''', (dia_seguimiento, hora_seguimiento, obs1_seguimiento, obs2_seguimiento, obs3_seguimiento, obs4_seguimiento, obs5_seguimiento, comentarios_seguimiento, id_accion))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error al actualizar seguimiento: {e}")
        finally:
            conn.close()

    @staticmethod
    def delete_seguimiento(id_seguimiento):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Seguimiento WHERE id_seguimiento = ?", (id_seguimiento,))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error al eliminar seguimiento: {e}")
        finally:
            conn.close()

    ####################### OTROS BÁSICOS #######################

    @staticmethod
    def list_all_seguimientos():
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Seguimiento")
            return cursor.fetchall()
        except sqlite3.Error as e:
            logging.error(f"Error al listar las seguimientoes: {e}")
        finally:
            conn.close()
    


    ####################### ESPECIALES #######################
        
    @staticmethod
    def insert_seguimiento_desde_excel(seguimiento_data):
        try:
            """Insertar datos de acción en la tabla seguimiento"""
            sql = '''
            INSERT INTO Seguimiento (dia_seguimiento, horaInicio_seguimiento, horaFin_seguimiento,
                                ambiente_seguimiento, numAlumnos_seguimiento, id_tipoActividad,
                                id_semana, id_docente)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            '''
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute(sql, (seguimiento_data["dia_seguimiento"], seguimiento_data["horaInicio_seguimiento"],
                                seguimiento_data["horaFin_seguimiento"], seguimiento_data["ambiente_seguimiento"],
                                seguimiento_data["numAlumnos_seguimiento"], seguimiento_data["id_tipoActividad"],
                                seguimiento_data["id_semana"], seguimiento_data["id_docente"]))
            conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            logging.error(f"Error al insertar acción desde un excel: {e}")
        finally:
            conn.close()
