import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import os
import PyPDF2  # Importar PyPDF2 para trabajar con PDFs
from app.views.general_options_view import GeneralOptionsView

class AdministrarView(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Administrar PDF")
        self.geometry("400x600")  # Ampliar para ajustar nuevos campos
        
        # Asignar el icono mediante la función estática
        GeneralOptionsView.icono_ventana(self)
        
        self.select_pdf_button = tk.Button(self, text="Seleccionar PDF", command=self.select_pdf)
        self.select_pdf_button.pack(pady=10)

        # Agregar un label para mostrar el nombre del archivo seleccionado
        self.selected_pdf_label = tk.Label(self, text="Ningún PDF seleccionado")
        self.selected_pdf_label.pack(pady=5)
        
        self.process_pdf_button = tk.Button(self, text="Extraer datos de PDF", command=self.process_pdf)
        self.process_pdf_button.pack(pady=10)

        # Campos de datos extraídos del PDF
        self.data_frame = tk.Frame(self)
        self.data_frame.pack(pady=10)

        self.labels = {}
        self.entries = {}

        fields = ['Nombre Asignatura', 'Sigla Asignatura', 'Nombre Docente', 'Semestre', 'Créditos Asignatura', 'Aula', 'Horas', 'Días de Clase']
        for field in fields:
            frame = tk.Frame(self.data_frame)
            frame.pack(fill=tk.X, pady=2)
            label = tk.Label(frame, text=field + ":")
            label.pack(side=tk.LEFT, padx=5)
            if field in ['Nombre Asignatura', 'Nombre Docente']:
                entry = ttk.Combobox(frame)
            else:
                entry = tk.Entry(frame)
            entry.pack(side=tk.RIGHT, padx=5, fill=tk.X, expand=True)
            self.labels[field] = label
            self.entries[field] = entry

        # Botón de guardar
        self.save_button = tk.Button(self, text="Guardar", command=self.save_data)
        self.save_button.pack(pady=10)

        self.pdf_path = None

    def select_pdf(self):
        self.pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if self.pdf_path:
            filename = os.path.basename(self.pdf_path)
            self.selected_pdf_label.config(text=f"Archivo seleccionado: {filename}")
            messagebox.showinfo("PDF Seleccionado", f"Archivo seleccionado: {self.pdf_path}")
            self.controller.set_pdf_path(self.pdf_path)

    def process_pdf(self):
        if self.pdf_path:
            extracted_data = self.controller.process_pdf(self.pdf_path)
            # Obtener las listas de asignaturas y docentes
            asignaturas = self.controller.get_asignaturas()
            docentes = self.controller.get_docentes()
            # Mostrar datos extraídos en los campos de entrada
            for field, value in extracted_data.items():
                self.entries[field].delete(0, tk.END)
                if field == 'Nombre Asignatura':
                    self.entries[field]['values'] = asignaturas
                elif field == 'Nombre Docente':
                    self.entries[field]['values'] = docentes
                self.entries[field].insert(0, value)
        else:
            messagebox.showwarning("Advertencia", "Seleccione un PDF primero")

    def save_data(self):
        data = {field: entry.get() for field, entry in self.entries.items()}
        self.controller.save_data(data)
