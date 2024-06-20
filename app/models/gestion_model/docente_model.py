import sqlite3
import logging
from app.models.database import create_connection

class DocenteModel:
    @staticmethod
    def create_docente(nombres, apellido_paterno, apellido_materno, correo, dni, celular, grado_maestro, grado_doctor, titulo_profesional, titulo_esp_medico, titulo_esp_odonto, grado_bachiller):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Docente (
                    nombres_docente, apellidoPaterno_docente, apellidoMaterno_docente, correo_docente,
                    dni_docente, celular_docente, gradoMaestro_docente, gradoDoctor_docente,
                    tituloProfesional_docente, tituloEspMedico_docente, tituloEspOdonto_docente, gradoBachiller_docente
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (nombres, apellido_paterno, apellido_materno, correo, dni, celular, grado_maestro, grado_doctor, titulo_profesional, titulo_esp_medico, titulo_esp_odonto, grado_bachiller))
            conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            logging.error(f"Error al crear docente: {e}")
        finally:
            conn.close()

    @staticmethod
    def read_docente(id_docente):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Docente WHERE id_docente = ?", (id_docente,))
            return cursor.fetchone()
        except sqlite3.Error as e:
            logging.error(f"Error al leer docente: {e}")
        finally:
            conn.close()

    @staticmethod
    def update_docente(id_docente, nombres, apellido_paterno, apellido_materno, correo, dni, celular, grado_maestro, grado_doctor, titulo_profesional, titulo_esp_medico, titulo_esp_odonto, grado_bachiller):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE Docente SET 
                    nombres_docente = ?, apellidoPaterno_docente = ?, apellidoMaterno_docente = ?, correo_docente = ?,
                    dni_docente = ?, celular_docente = ?, gradoMaestro_docente = ?, gradoDoctor_docente = ?,
                    tituloProfesional_docente = ?, tituloEspMedico_docente = ?, tituloEspOdonto_docente = ?, gradoBachiller_docente = ?
                WHERE id_docente = ?
            """, (nombres, apellido_paterno, apellido_materno, correo, dni, celular, grado_maestro, grado_doctor, titulo_profesional, titulo_esp_medico, titulo_esp_odonto, grado_bachiller, id_docente))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error al actualizar docente: {e}")
        finally:
            conn.close()

    @staticmethod
    def delete_docente(id_docente):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Docente WHERE id_docente = ?", (id_docente,))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error al eliminar docente: {e}")
        finally:
            conn.close()

    ####################### otros ###################
    @staticmethod
    def list_all_docente():
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Docente")
            return cursor.fetchall()
        except sqlite3.Error as e:
            logging.error(f"Error al listar los Docentes: {e}")
        finally:
            conn.close()

    @staticmethod
    def buscar_docente_por_id(id_docente):
        return DocenteModel.read_docente(id_docente)

    @staticmethod
    def buscar_docente_por_nombre(nombres):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Docente WHERE nombres_docente = ?", (nombres,))
            return cursor.fetchall()
        except sqlite3.Error as e:
            logging.error(f"Error al buscar docente por nombre: {e}")
        finally:
            conn.close()
    
    @staticmethod
    def buscar_docente_por_dni(dni):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM Docente WHERE dni_docente = ?", (dni,))
            return cursor.fetchone()[0]
        except sqlite3.Error as e:
            logging.error(f"Error al buscar docente por dni: {e}")
        finally:
            conn.close()

    ############################################

    @staticmethod
    def insert_docente_desde_excel(docente_data):
        try:
            sql = '''
            INSERT INTO Docente (nombres_docente, correo_docente, dni_docente, celular_docente, gradoBachiller_docente, 
                                tituloProfesional_docente, gradoMaestro_docente, gradoDoctor_docente, 
                                tituloEspMedico_docente, tituloEspOdonto_docente)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            '''
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute(sql, (docente_data["nombre_docente"], docente_data["correo_docente"], docente_data["dni_docente"],
                            docente_data["celular_docente"], docente_data["gradoBachiller_docente"],
                            docente_data["tituloProfesional_docente"], docente_data["gradoMaestro_docente"],
                            docente_data["gradoDoctor_docente"], docente_data["tituloSegEspMedico_docente"],
                            docente_data["tituloSegEspOdontologo_docente"]))
            conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            logging.error(f"Error al insertar docente desde un excel: {e}")
        finally:
            conn.close()