import tkinter as tk
from tkinter import ttk, messagebox
from app.views.general_options_view import GeneralOptionsView

class ReporteDocenteView(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Consultar Docentes")

        # Frame para la búsqueda
        self.search_frame = ttk.Frame(self)
        self.search_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Etiqueta y entrada para buscar por nombre del docente
        ttk.Label(self.search_frame, text="Nombre del Docente:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.search_entry_nombre = ttk.Entry(self.search_frame)
        self.search_entry_nombre.grid(row=0, column=1, padx=5, pady=5)

        # Etiqueta y entrada para buscar por DNI del docente
        ttk.Label(self.search_frame, text="DNI del Docente:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.search_entry_dni = ttk.Entry(self.search_frame)
        self.search_entry_dni.grid(row=1, column=1, padx=5, pady=5)

        # Botón de búsqueda
        self.search_button = ttk.Button(self.search_frame, text="Buscar", command=self.search_docente)
        self.search_button.grid(row=0, column=2, rowspan=2, padx=5, pady=5)

        # Frame para la tabla
        self.tree_frame = ttk.Frame(self)
        self.tree_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.tree_scroll = ttk.Scrollbar(self.tree_frame, orient=tk.VERTICAL)
        self.tree_scroll.grid(row=0, column=1, sticky="ns")

        self.docente_tree = ttk.Treeview(
            self.tree_frame,
            columns=("ID", "Nombres", "Apellido Paterno", "Apellido Materno", "Correo", "DNI", "Celular", "Grado Maestro", "Grado Doctor", "Título Profesional", "Título Esp Médico", "Título Esp Odonto", "Grado Bachiller"),
            show="headings",
            yscrollcommand=self.tree_scroll.set
        )
        self.tree_scroll.config(command=self.docente_tree.yview)

        self.docente_tree.heading("ID", text="ID")
        self.docente_tree.heading("Nombres", text="Nombres")
        self.docente_tree.heading("Apellido Paterno", text="Apellido Paterno")
        self.docente_tree.heading("Apellido Materno", text="Apellido Materno")
        self.docente_tree.heading("Correo", text="Correo")
        self.docente_tree.heading("DNI", text="DNI")
        self.docente_tree.heading("Celular", text="Celular")
        self.docente_tree.heading("Grado Maestro", text="Grado Maestro")
        self.docente_tree.heading("Grado Doctor", text="Grado Doctor")
        self.docente_tree.heading("Título Profesional", text="Título Profesional")
        self.docente_tree.heading("Título Esp Médico", text="Título Esp Médico")
        self.docente_tree.heading("Título Esp Odonto", text="Título Esp Odonto")
        self.docente_tree.heading("Grado Bachiller", text="Grado Bachiller")

        self.docente_tree.grid(row=0, column=0, sticky="nsew")

        # Ajustar tamaño de las columnas
        self.docente_tree.column("ID", width=50)
        self.docente_tree.column("Nombres", width=150)
        self.docente_tree.column("Apellido Paterno", width=100)
        self.docente_tree.column("Apellido Materno", width=100)
        self.docente_tree.column("Correo", width=200)
        self.docente_tree.column("DNI", width=80)
        self.docente_tree.column("Celular", width=100)
        self.docente_tree.column("Grado Maestro", width=150)
        self.docente_tree.column("Grado Doctor", width=150)
        self.docente_tree.column("Título Profesional", width=150)
        self.docente_tree.column("Título Esp Médico", width=150)
        self.docente_tree.column("Título Esp Odonto", width=150)
        self.docente_tree.column("Grado Bachiller", width=150)

        # Actualizar lista de docentes al iniciar la ventana
        self.update_docente_list()

    def update_docente_list(self):
        # Limpiar entradas previas
        for item in self.docente_tree.get_children():
            self.docente_tree.delete(item)

        # Obtener las docentes actualizados desde el controlador
        docentes = self.controller.list_all_consulta_docente("", "")
        for docente in docentes:
            self.docente_tree.insert("", "end", values=docente)

    def search_docente(self):
        nombreDocente = self.search_entry_nombre.get().strip().lower()
        dniDocente = self.search_entry_dni.get().strip().lower()

        print(f"Buscando por nombre: {nombreDocente}, DNI: {dniDocente}")  # Agregar esta línea para depuración

        # Limpiar entradas previas
        for item in self.docente_tree.get_children():
            self.docente_tree.delete(item)

        # Obtener docentes que coincidan con los términos de búsqueda
        docentes = self.controller.list_all_consulta_docente(nombreDocente, dniDocente)
        for docente in docentes:
            self.docente_tree.insert("", "end", values=docente)
