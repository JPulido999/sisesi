import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from app.views.general_options_view import GeneralOptionsView

class ExtraerPlanView(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Extraer Planes de Trabajo")
        self.geometry("600x400")

        # Asignar el icono mediante la función estática
        GeneralOptionsView.icono_ventana(self)

        self.extraer_img = GeneralOptionsView.crear_boton("extract-folder.png", 50)

        self.btn_extraer = tk.Button(self, text="Extraer", image=self.extraer_img, compound=tk.TOP, command=self.on_extraer_click)
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

        # Ajustar tamaño de las columnas
        self.tree.column("Archivo", width=150)
        self.tree.column("Docente", width=150)
        self.tree.column("Correo", width=100)
        self.tree.column("DNI", width=80)
        self.tree.column("Celular", width=100)

    def on_extraer_click(self):
        self.controller.process_excel_files()

    def update_info(self, total_files, extracted_data):
        self.info_label.config(text=f"Total de archivos procesados: {total_files}")

        for item in self.tree.get_children():
            self.tree.delete(item)

        for data in extracted_data:
            docente = data['docente']
            self.tree.insert("", "end", values=(data['archivo'], docente["nombre_docente"], docente["correo_docente"], docente["dni_docente"], docente["celular_docente"]))
