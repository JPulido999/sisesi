import tkinter as tk
from tkinter import ttk, messagebox
from app.views.general_options_view import GeneralOptionsView

class ReporteContratoView(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Consultar Contratos")

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
        self.search_button = ttk.Button(self.search_frame, text="Buscar", command=self.search_contrato)
        self.search_button.grid(row=0, column=2, rowspan=2, padx=5, pady=5)

        # Frame para la tabla
        self.tree_frame = ttk.Frame(self)
        self.tree_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.tree_scroll = ttk.Scrollbar(self.tree_frame, orient=tk.VERTICAL)
        self.tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.contrato_tree = ttk.Treeview(
            self.tree_frame,
            columns=("Docente", "Dni", "Celular", "Correo", "Renacyt", "FechaInicio", "FechaFin", "Categoria", "Regimen", "Condicion"),
            show="headings",
            yscrollcommand=self.tree_scroll.set
        )
        self.tree_scroll.config(command=self.contrato_tree.yview)

        self.contrato_tree.heading("Docente", text="Docente")
        self.contrato_tree.heading("Dni", text="Dni")
        self.contrato_tree.heading("Celular", text="Celular")
        self.contrato_tree.heading("Correo", text="Correo")
        self.contrato_tree.heading("Renacyt", text="Renacyt")
        self.contrato_tree.heading("FechaInicio", text="Fecha Inicio")
        self.contrato_tree.heading("FechaFin", text="Fecha Fin")
        self.contrato_tree.heading("Categoria", text="Categoria")
        self.contrato_tree.heading("Regimen", text="Regimen")
        self.contrato_tree.heading("Condicion", text="Condicion")

        self.contrato_tree.pack(fill=tk.BOTH, expand=True)

        # Ajustar tamaño de las columnas
        self.contrato_tree.column("Docente", width=250)
        self.contrato_tree.column("Dni", width=60)
        self.contrato_tree.column("Celular", width=70)
        self.contrato_tree.column("Correo", width=200)
        self.contrato_tree.column("Renacyt", width=60)
        self.contrato_tree.column("FechaInicio", width=90)
        self.contrato_tree.column("FechaFin", width=90)
        self.contrato_tree.column("Categoria", width=100)
        self.contrato_tree.column("Regimen", width=100)
        self.contrato_tree.column("Condicion", width=100)

        # Actualizar lista de contratos al iniciar la ventana
        self.update_contrato_list()

    def update_contrato_list(self):
        # Limpiar entradas previas
        for item in self.contrato_tree.get_children():
            self.contrato_tree.delete(item)

        # Obtener las contratos actualizadas desde el controlador
        contratos = self.controller.list_all_consulta_contrato("", "")
        for contrato in contratos:
            self.contrato_tree.insert("", "end", values=contrato)

    def search_contrato(self):
        nombreDocente = self.search_entry_nombre.get().strip().lower()
        dniDocente = self.search_entry_dni.get().strip().lower()

        print(f"Buscando por nombre: {nombreDocente}, DNI: {dniDocente}")  # Agregar esta línea para depuración

        # Limpiar entradas previas
        for item in self.contrato_tree.get_children():
            self.contrato_tree.delete(item)

        # Obtener contratos que coincidan con los términos de búsqueda
        contratos = self.controller.list_all_consulta_contrato(nombreDocente, dniDocente)
        for contrato in contratos:
            self.contrato_tree.insert("", "end", values=contrato)
