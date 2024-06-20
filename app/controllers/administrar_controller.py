import sqlite3
import re
import PyPDF2
from app.views.administrar_view import AdministrarView

def create_connection():
    conn = sqlite3.connect('sisesi.db')
    return conn

class AdministrarController:
    def __init__(self):
        self.pdf_path = None
        self.view = None

    def set_pdf_path(self, path):
        self.pdf_path = path

    def process_pdf(self, pdf_path):
        # Extraer datos del PDF
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()

        # Usar expresiones regulares para extraer información específica
        nombre_asignatura = re.search(r'Nombre de la asignatura: (.+)', text)
        sigla_asignatura = re.search(r'Sigla: (.+)', text)
        nombre_docente = re.search(r'Docente: (.+)', text)
        semestre = re.search(r'Semestre: (.+)', text)
        creditos_asignatura = re.search(r'Créditos: (\d+)', text)
        aula = re.search(r'Aula: (.+)', text)
        horas = re.search(r'Horas: (.+)', text)
        dias_clase = re.search(r'Días de clase: (.+)', text)

        # Extraer los valores de los grupos de las expresiones regulares
        extracted_data = {
            'Nombre Asignatura': nombre_asignatura.group(1) if nombre_asignatura else "",
            'Sigla Asignatura': sigla_asignatura.group(1) if sigla_asignatura else "",
            'Nombre Docente': nombre_docente.group(1) if nombre_docente else "",
            'Semestre': semestre.group(1) if semestre else "",
            'Créditos Asignatura': int(creditos_asignatura.group(1)) if creditos_asignatura else 0,
            'Aula': aula.group(1) if aula else "",
            'Horas': horas.group(1) if horas else "",
            'Días de Clase': dias_clase.group(1) if dias_clase else ""
        }

        return extracted_data

    def get_asignaturas(self):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT nombre_asignatura FROM Asignatura")
        results = cursor.fetchall()
        conn.close()
        return [row[0] for row in results]

    def get_docentes(self):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT nombres_docente FROM Docente")
        results = cursor.fetchall()
        conn.close()
        return [row[0] for row in results]

    def save_data(self, data):
        conn = create_connection()
        cursor = conn.cursor()

        # Obtener IDs de las asignaturas y docentes seleccionados
        cursor.execute("SELECT id_asignatura FROM Asignatura WHERE nombre_asignatura = ?", (data['Nombre Asignatura'],))
        id_asignatura = cursor.fetchone()[0]

        cursor.execute("SELECT id_docente FROM Docente WHERE nombres_docente = ?", (data['Nombre Docente'],))
        id_docente = cursor.fetchone()[0]

        # SQL de Inserción
        cursor.execute("INSERT INTO Silabo (id_asignatura, id_docente, diaT_sil, ambienteT_sil, horaT_sil) VALUES (?, ?, ?, ?, ?)",
                       (id_asignatura, id_docente, data['Días de Clase'], data['Aula'], data['Horas']))

        conn.commit()
        conn.close()

        print("Datos almacenados correctamente")

    def show_view(self):
        self.view = AdministrarView(self)
        self.view.mainloop()
