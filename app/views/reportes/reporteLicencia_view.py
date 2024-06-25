import tkinter as tk
from tkinter import ttk, messagebox
from app.views.general_options_view import GeneralOptionsView

class ReporteLicenciaView(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Consultar Licencias")

        # Frame para la búsqueda
        self.search_frame = ttk.Frame(self)
        self.search_frame.pack(padx=10, pady=10, fill=tk.X)

        # Etiqueta y entrada para buscar por nombre del docente
        ttk.Label(self.search_frame, text="Nombre del Docente:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.search_entry_nombre = ttk.Entry(self.search_frame)
        self.search_entry_nombre.grid(row=0, column=1, padx=5, pady=5)

        # Etiqueta y entrada para buscar por DNI del docente
        ttk.Label(self.search_frame, text="DNI del Docente:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.search_entry_dni = ttk.Entry(self.search_frame)
        self.search_entry_dni.grid(row=1, column=1, padx=5, pady=5)

        # Botón de búsqueda
        self.search_button = ttk.Button(self.search_frame, text="Buscar", command=self.search_licencia)
        self.search_button.grid(row=0, column=2, rowspan=2, padx=5, pady=5)

        # Frame para la tabla
        self.tree_frame = ttk.Frame(self)
        self.tree_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.tree_scroll = ttk.Scrollbar(self.tree_frame, orient=tk.VERTICAL)
        self.tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.licencia_tree = ttk.Treeview(
            self.tree_frame,
            columns=("Docente", "Dni", "Celular", "Correo", "Resolucion", "FechaInicio", "FechaFin", "Observacion", "Licencia"),
            show="headings",
            yscrollcommand=self.tree_scroll.set
        )
        self.tree_scroll.config(command=self.licencia_tree.yview)

        self.licencia_tree.heading("Docente", text="Docente")
        self.licencia_tree.heading("Dni", text="Dni")
        self.licencia_tree.heading("Celular", text="Celular")
        self.licencia_tree.heading("Correo", text="Correo")
        self.licencia_tree.heading("Resolucion", text="Resolución")
        self.licencia_tree.heading("FechaInicio", text="Fecha Inicio")
        self.licencia_tree.heading("FechaFin", text="Fecha Fin")
        self.licencia_tree.heading("Observacion", text="Observacion")
        self.licencia_tree.heading("Licencia", text="Licencia")

        self.licencia_tree.pack(fill=tk.BOTH, expand=True)

        # Ajustar tamaño de las columnas
        self.licencia_tree.column("Docente", width=250)
        self.licencia_tree.column("Dni", width=60)
        self.licencia_tree.column("Celular", width=70)
        self.licencia_tree.column("Correo", width=200)
        self.licencia_tree.column("Resolucion", width=250)
        self.licencia_tree.column("FechaInicio", width=80)
        self.licencia_tree.column("FechaFin", width=80)
        self.licencia_tree.column("Observacion", width=150)
        self.licencia_tree.column("Licencia", width=100)

        # Actualizar lista de licencias al iniciar la ventana
        self.update_licencia_list()

    def update_licencia_list(self):
        # Limpiar entradas previas
        for item in self.licencia_tree.get_children():
            self.licencia_tree.delete(item)

        # Obtener las licencias actualizadas desde el controlador
        licencias = self.controller.list_all_consulta_licencia("", "")
        for licencia in licencias:
            self.licencia_tree.insert("", "end", values=licencia)

    def search_licencia(self):
        nombreDocente = self.search_entry_nombre.get().strip().lower()
        dniDocente = self.search_entry_dni.get().strip().lower()

        print(f"Buscando por nombre: {nombreDocente}, DNI: {dniDocente}")  # Agregar esta línea para depuración

        # Limpiar entradas previas
        for item in self.licencia_tree.get_children():
            self.licencia_tree.delete(item)

        # Obtener licencias que coincidan con los términos de búsqueda
        licencias = self.controller.list_all_consulta_licencia(nombreDocente, dniDocente)
        for licencia in licencias:
            self.licencia_tree.insert("", "end", values=licencia)
