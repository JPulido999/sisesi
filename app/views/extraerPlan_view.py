import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from app.controllers.extraerPlan_controller import ExtraerPlanController

class ExtraerPlanView(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Extraer Planes de Trabajo")
        self.geometry("600x400")

        self.btn_extraer = tk.Button(self, text="Extraer", command=self.on_extraer_click)
        self.btn_extraer.pack(pady=20)

        self.info_label = tk.Label(self, text="")
        self.info_label.pack(pady=10)

        self.tree = ttk.Treeview(self, columns=("Archivo", "Docente", "Correo", "DNI", "Celular"), show="headings")
        self.tree.heading("Archivo", text="Archivo")
        self.tree.heading("Docente", text="Docente")
        self.tree.heading("Correo", text="Correo")
        self.tree.heading("DNI", text="DNI")
        self.tree.heading("Celular", text="Celular")
        self.tree.pack(expand=True, fill=tk.BOTH)

    def on_extraer_click(self):
        self.controller.process_excel_files()

    def update_info(self, total_files, extracted_data):
        self.info_label.config(text=f"Total de archivos procesados: {total_files}")

        for item in self.tree.get_children():
            self.tree.delete(item)

        for data in extracted_data:
            docente = data['docente']
            self.tree.insert("", "end", values=(data['archivo'], docente["nombre_docente"], docente["correo_docente"], docente["dni_docente"], docente["celular_docente"]))
