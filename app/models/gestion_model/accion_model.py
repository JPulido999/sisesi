import sqlite3
import logging
from app.models.database import create_connection

class AccionModel:

        ####################### CRUD #######################
        
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
