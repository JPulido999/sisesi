import sqlite3
import logging
from app.models.database import create_connection

class AccionModel:

    ####################### CRUD #######################
    @staticmethod
    def create_accion(dia_accion, horaInicio_accion, horaFin_accion, ambiente_accion, numAlumnos_accion, id_tipoActividad, id_semana, id_docente):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO Accion (dia_accion, horaInicio_accion, horaFin_accion, ambiente_accion, numAlumnos_accion, id_tipoActividad, id_semana, id_docente)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (dia_accion, horaInicio_accion, horaFin_accion, ambiente_accion, numAlumnos_accion, id_tipoActividad, id_semana, id_docente))
            conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            logging.error(f"Error al crear acción: {e}")
        finally:
            conn.close()

    @staticmethod
    def read_accion(id_accion):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Accion WHERE id_accion = ?", (id_accion,))
            return cursor.fetchone()
        except sqlite3.Error as e:
            logging.error(f"Error al leer acción: {e}")
        finally:
            conn.close()

    @staticmethod
    def update_accion(id_accion, dia_accion, horaInicio_accion, horaFin_accion, ambiente_accion, numAlumnos_accion, id_tipoActividad, id_semana, id_docente):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE Accion 
                SET dia_accion = ?, horaInicio_accion = ?, horaFin_accion = ?, ambiente_accion = ?, numAlumnos_accion = ?, id_tipoActividad = ?, id_semana = ?, id_docente = ?
                WHERE id_accion = ?
            ''', (dia_accion, horaInicio_accion, horaFin_accion, ambiente_accion, numAlumnos_accion, id_tipoActividad, id_semana, id_docente, id_accion))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error al actualizar acción: {e}")
        finally:
            conn.close()

    @staticmethod
    def delete_accion(id_accion):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Accion WHERE id_accion = ?", (id_accion,))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error al eliminar acción: {e}")
        finally:
            conn.close()

    ####################### OTROS BÁSICOS #######################

    @staticmethod
    def list_all_acciones():
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Accion")
            return cursor.fetchall()
        except sqlite3.Error as e:
            logging.error(f"Error al listar las acciones: {e}")
        finally:
            conn.close()
    


    ####################### ESPECIALES #######################
        
    @staticmethod
    def insert_accion_desde_excel(accion_data):
        try:
            """Insertar datos de acción en la tabla Accion"""
            sql = '''
            INSERT INTO Accion (dia_accion, horaInicio_accion, horaFin_accion,
                                ambiente_accion, numAlumnos_accion, id_tipoActividad,
                                id_semana, id_docente)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            '''
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute(sql, (accion_data["dia_accion"], accion_data["horaInicio_accion"],
                                accion_data["horaFin_accion"], accion_data["ambiente_accion"],
                                accion_data["numAlumnos_accion"], accion_data["id_tipoActividad"],
                                accion_data["id_semana"], accion_data["id_docente"]))
            conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            logging.error(f"Error al insertar acción desde un excel: {e}")
        finally:
            conn.close()
