import tkinter as tk
from tkinter import ttk
from app.views.general_options_view import GeneralOptionsView  # Assuming this import is necessary

class ReporteAccionView(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Consultar Acciones")

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
        self.search_button = ttk.Button(self.search_frame, text="Buscar", command=self.search_accion)
        self.search_button.grid(row=0, column=2, rowspan=2, padx=5, pady=5)

        # Frame para la tabla
        self.tree_frame = ttk.Frame(self)
        self.tree_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.tree_scroll = ttk.Scrollbar(self.tree_frame, orient=tk.VERTICAL)
        self.tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.accion_tree = ttk.Treeview(
            self.tree_frame,
            columns=("Docente", "Día", "Hora Inicio", "Hora Fin", "Ambiente", "N° de Alumnos", "Semana",
                     "Contenido", "Unidad", "Asignatura", "Sigla",
                     "Semestre", "Plan", "Escuela"),
            show="headings",
            yscrollcommand=self.tree_scroll.set
        )
        self.tree_scroll.config(command=self.accion_tree.yview)

        self.accion_tree.heading("Docente", text="Docente")
        self.accion_tree.heading("Día", text="Día")
        self.accion_tree.heading("Hora Inicio", text="Hora Inicio")
        self.accion_tree.heading("Hora Fin", text="Hora Fin")
        self.accion_tree.heading("Ambiente", text="Ambiente")
        self.accion_tree.heading("N° de Alumnos", text="N° de Alumnos")
        self.accion_tree.heading("Semana", text="Semana")
        self.accion_tree.heading("Contenido", text="Contenido")
        self.accion_tree.heading("Unidad", text="Unidad")
        self.accion_tree.heading("Asignatura", text="Asignatura")
        self.accion_tree.heading("Sigla", text="Sigla")
        self.accion_tree.heading("Semestre", text="Semestre")
        self.accion_tree.heading("Plan", text="Plan")
        self.accion_tree.heading("Escuela", text="Escuela")

        self.accion_tree.pack(fill=tk.BOTH, expand=True)

        # Ajustar tamaño de las columnas
        self.accion_tree.column("Docente", width=200)
        self.accion_tree.column("Día", width=90)
        self.accion_tree.column("Hora Inicio", width=50)
        self.accion_tree.column("Hora Fin", width=50)
        self.accion_tree.column("Ambiente", width=50)
        self.accion_tree.column("N° de Alumnos", width=50)
        self.accion_tree.column("Semana", width=50)
        self.accion_tree.column("Contenido", width=200)
        self.accion_tree.column("Unidad", width=50)
        self.accion_tree.column("Asignatura", width=110)
        self.accion_tree.column("Sigla", width=50)
        self.accion_tree.column("Semestre", width=50)
        self.accion_tree.column("Plan", width=50)
        self.accion_tree.column("Escuela", width=100)

        # Actualizar lista de acciones al iniciar la ventana
        self.update_accion_list()

    def update_accion_list(self):
        # Limpiar entradas previas
        for item in self.accion_tree.get_children():
            self.accion_tree.delete(item)

        # Obtener las acciones actualizadas desde el controlador
        acciones = self.controller.list_all_consulta_accion("", "")
        for accion in acciones:
            self.accion_tree.insert("", "end", values=accion)

    def search_accion(self):
        nombreDocente = self.search_entry_nombre.get().strip().lower()
        dniDocente = self.search_entry_dni.get().strip().lower()

        print(f"Buscando por nombre: {nombreDocente}, DNI: {dniDocente}")  # Agregar esta línea para depuración

        # Limpiar entradas previas
        for item in self.accion_tree.get_children():
            self.accion_tree.delete(item)

        # Obtener acciones que coincidan con los términos de búsqueda
        acciones = self.controller.list_all_consulta_accion(nombreDocente, dniDocente)
        for accion in acciones:
            self.accion_tree.insert("", "end", values=accion)
