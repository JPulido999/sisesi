import sqlite3
import logging
from app.models.database import create_connection

class ReportesModel:

    ####################### CRUD #######################


    ####################### OTROS BÁSICOS #######################

    @staticmethod
    def list_all_licencias_c1(nombreDocente, dniDocente):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            
            query = """
                SELECT d.nombres_docente, d.dni_docente, d.celular_docente, d.correo_docente,
                    l.resolucion_licencia, l.fechaInicio_licencia, l.fechaFin_licencia, l.observacion_licencia,
                    tl.nombre_tipoLicencia
                FROM Licencia l
                INNER JOIN Docente d ON l.id_docente = d.id_docente
                LEFT JOIN Tipo_Licencia tl ON l.id_tipoLicencia = tl.id_tipoLicencia
                WHERE (d.nombres_docente LIKE '%' || ? || '%' AND ? != '')
                OR (d.dni_docente LIKE '%' || ? || '%' AND ? != '')
                OR (? = '' AND ? = '')
            """
            cursor.execute(query, (nombreDocente, nombreDocente, dniDocente, dniDocente, nombreDocente, dniDocente))
            
            return cursor.fetchall()
        except sqlite3.Error as e:
            logging.error(f"Error al listar las licencias: {e}")
            return []
        finally:
            conn.close()


    
    
    @staticmethod
    def buscar_licencia_por_resolucion(resolucion):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM Licencia WHERE resolucion_licencia = ?", (resolucion,))
            return cursor.fetchone()[0]
        except sqlite3.Error as e:
            logging.error(f"Error al buscar licencia por resolucion: {e}")
        finally:
            conn.close()
