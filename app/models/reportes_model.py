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
    def list_all_contratos_c1(nombreDocente, dniDocente):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            
            query = """
                SELECT d.nombres_docente, d.dni_docente, d.celular_docente, d.correo_docente, 
                    c.renacyt_contrato, c.periodoInicio_contrato, c.periodoFin_contrato,
                    cat.nombre_categoria, reg.nombre_regimen, cond.nombre_condicion
                FROM Contrato c
                INNER JOIN Docente d ON c.id_docente = d.id_docente
                LEFT JOIN Categoria cat ON c.id_categoria = cat.id_categoria
                LEFT JOIN Condicion cond ON c.id_condicion = cond.id_condicion
                LEFT JOIN Regimen reg ON c.id_regimen = reg.id_regimen
                WHERE (d.nombres_docente LIKE '%' || ? || '%' AND ? != '')
                OR (d.dni_docente LIKE '%' || ? || '%' AND ? != '')
                OR (? = '' AND ? = '')
            """
            cursor.execute(query, (nombreDocente, nombreDocente, dniDocente, dniDocente, nombreDocente, dniDocente))
            
            return cursor.fetchall()
        except sqlite3.Error as e:
            logging.error(f"Error al listar los contratos: {e}")
            return []
        finally:
            conn.close()

    @staticmethod
    def list_all_docentes_c1(nombreDocente, dniDocente):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            
            query = """
                SELECT * FROM Docente d
                WHERE (d.nombres_docente LIKE '%' || ? || '%' AND ? != '')
                OR (d.dni_docente LIKE '%' || ? || '%' AND ? != '')
                OR (? = '' AND ? = '')
            """
            cursor.execute(query, (nombreDocente, nombreDocente, dniDocente, dniDocente, nombreDocente, dniDocente))
            
            return cursor.fetchall()
        except sqlite3.Error as e:
            logging.error(f"Error al listar los docentes: {e}")
            return []
        finally:
            conn.close()
    
    @staticmethod
    def list_all_acciones_c1(nombreDocente, dniDocente):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            
            query = """
                SELECT d.nombres_docente,
                    a.dia_accion,a.horaInicio_accion,a.horaFin_accion,a.ambiente_accion,a.numAlumnos_accion,
                    s.nombre_semana,s.contenido_semana,
                    u.numero_unidad,
                    asig.nombre_asignatura,asig.sigla_asignatura,
                    sem.nombre_semestre,
                    pl.nombre_plan,
                    es.nombre_escuela
                FROM Accion a
                JOIN Docente d ON a.id_docente = d.id_docente
                JOIN Semana s ON a.id_semana = s.id_semana
                JOIN Unidad u ON s.id_unidad = u.id_unidad
                JOIN Silabo sil ON u.id_sil = sil.id_sil
                JOIN Asignatura asig ON sil.id_asignatura = asig.id_asignatura
                JOIN Semestre sem ON sil.id_semestre = sem.id_semestre
                JOIN Plan_Estudios pl ON asig.id_plan = pl.id_plan
                JOIN Escuela es ON pl.id_escuela = es.id_escuela
                WHERE (d.nombres_docente LIKE '%' || ? || '%' AND ? != '')
                OR (d.dni_docente LIKE '%' || ? || '%' AND ? != '')
                OR (? = '' AND ? = '')
            """
            cursor.execute(query, (nombreDocente, nombreDocente, dniDocente, dniDocente, nombreDocente, dniDocente))
            
            return cursor.fetchall()
        except sqlite3.Error as e:
            logging.error(f"Error al listar las acciones: {e}")
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
