import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from app.views.general_options_view import GeneralOptionsView

class AccionView(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Gestión de Acción")

        # Frame para los inputs
        self.inputs_frame = ttk.Frame(self)
        self.inputs_frame.pack(padx=10, pady=10)

        # Función para crear Labels con Entry
        def create_labeled_entry(row, column, label_text):
            label = ttk.Label(self.inputs_frame, text=label_text)
            label.grid(row=row, column=column, padx=5, pady=5, sticky="w")
            
            entry = ttk.Entry(self.inputs_frame)
            entry.grid(row=row, column=column + 1, padx=5, pady=5)
            
            return entry

        # Campos de entrada de datos
        self.entry_dia_accion = create_labeled_entry(0, 0, "Día")
        self.entry_horaInicio_accion = create_labeled_entry(0, 2, "Hora Inicio")
        self.entry_horaFin_accion = create_labeled_entry(0, 4, "Hora Fin")
        self.entry_ambiente_accion = create_labeled_entry(1, 0, "Ambiente")
        self.entry_numAlumnos_accion = create_labeled_entry(1, 2, "Número de Alumnos")
        self.entry_id_tipoActividad = create_labeled_entry(1, 4, "ID Tipo Actividad")
        self.entry_id_semana = create_labeled_entry(2, 0, "ID Semana")
        self.entry_id_docente = create_labeled_entry(2, 2, "ID Docente")

        # Campos obligatorios para habilitar el botón de "CREAR"
        for entry in [
            self.entry_dia_accion,
            self.entry_horaInicio_accion,
            self.entry_horaFin_accion,
            self.entry_ambiente_accion,
            self.entry_numAlumnos_accion,
            self.entry_id_tipoActividad,
            self.entry_id_semana,
            self.entry_id_docente
        ]:
            entry.bind("<KeyRelease>", self.check_fields)

        # CRUD Buttons Frame
        self.buttons_frame = ttk.Frame(self)
        self.buttons_frame.pack(padx=10, pady=10)

        self.create_img = GeneralOptionsView.crear_boton("create.png", 20)
        self.update_img = GeneralOptionsView.crear_boton("update.png", 20)
        self.delete_img = GeneralOptionsView.crear_boton("delete.png", 20)

        self.create_button = ttk.Button(self.buttons_frame, text="Crear", image=self.create_img, compound=tk.TOP, command=self.create_accion, state=tk.DISABLED)
        self.create_button.grid(row=0, column=0, padx=5, pady=5)

        self.update_button = ttk.Button(self.buttons_frame, text="Actualizar", image=self.update_img, compound=tk.TOP, command=self.update_accion)
        self.update_button.grid(row=0, column=1, padx=5, pady=5)

        self.delete_button = ttk.Button(self.buttons_frame, text="Eliminar", image=self.delete_img, compound=tk.TOP, command=self.delete_accion)
        self.delete_button.grid(row=0, column=2, padx=5, pady=5)

        # Frame for Treeview with scrollbar
        self.tree_frame = ttk.Frame(self)
        self.tree_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.tree_scroll = ttk.Scrollbar(self.tree_frame, orient=tk.VERTICAL)
        self.tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.accion_tree = ttk.Treeview(
            self.tree_frame,
            columns=("ID", "Día", "Hora Inicio", "Hora Fin", "Ambiente", "Número de Alumnos", "ID Tipo Actividad", "ID Semana", "ID Docente"),
            show="headings",
            yscrollcommand=self.tree_scroll.set
        )
        self.tree_scroll.config(command=self.accion_tree.yview)

        self.accion_tree.heading("ID", text="ID")
        self.accion_tree.heading("Día", text="Día")
        self.accion_tree.heading("Hora Inicio", text="Hora Inicio")
        self.accion_tree.heading("Hora Fin", text="Hora Fin")
        self.accion_tree.heading("Ambiente", text="Ambiente")
        self.accion_tree.heading("Número de Alumnos", text="Número de Alumnos")
        self.accion_tree.heading("ID Tipo Actividad", text="ID Tipo Actividad")
        self.accion_tree.heading("ID Semana", text="ID Semana")
        self.accion_tree.heading("ID Docente", text="ID Docente")
        self.accion_tree.pack(fill=tk.BOTH, expand=True)

        # Ajustar tamaño de las columnas
        self.accion_tree.column("ID", width=30)
        self.accion_tree.column("Día", width=100)
        self.accion_tree.column("Hora Inicio", width=100)
        self.accion_tree.column("Hora Fin", width=100)
        self.accion_tree.column("Ambiente", width=100)
        self.accion_tree.column("Número de Alumnos", width=100)
        self.accion_tree.column("ID Tipo Actividad", width=100)
        self.accion_tree.column("ID Semana", width=100)
        self.accion_tree.column("ID Docente", width=100)

        # Frame for search
        self.search_frame = ttk.Frame(self)
        self.search_frame.pack(padx=10, pady=10, fill=tk.X)

        ttk.Label(self.search_frame, text="Buscar por día:").pack(side=tk.LEFT, padx=5)
        self.search_entry = ttk.Entry(self.search_frame)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        self.search_button = ttk.Button(self.search_frame, text="Buscar", command=self.search_accion)
        self.search_button.pack(side=tk.LEFT, padx=5)

    def check_fields(self, *args):
        if all([
            self.entry_dia_accion.get(),
            self.entry_horaInicio_accion.get(),
            self.entry_horaFin_accion.get(),
            self.entry_ambiente_accion.get(),
            self.entry_numAlumnos_accion.get(),
            self.entry_id_tipoActividad.get(),
            self.entry_id_semana.get(),
            self.entry_id_docente.get()
        ]):
            self.create_button.config(state=tk.NORMAL)
        else:
            self.create_button.config(state=tk.DISABLED)

    def create_accion(self):
        dia_accion = self.entry_dia_accion.get()
        horaInicio_accion = self.entry_horaInicio_accion.get()
        horaFin_accion = self.entry_horaFin_accion.get()
        ambiente_accion = self.entry_ambiente_accion.get()
        numAlumnos_accion = self.entry_numAlumnos_accion.get()
        id_tipoActividad = self.entry_id_tipoActividad.get()
        id_semana = self.entry_id_semana.get()
        id_docente = self.entry_id_docente.get()

        self.controller.create_accion(
            dia_accion, horaInicio_accion, horaFin_accion, ambiente_accion,
            numAlumnos_accion, id_tipoActividad, id_semana, id_docente
        )
        self.update_accion_list()

    def update_accion(self):
        selected_item = self.accion_tree.selection()
        if selected_item:
            id_accion = self.accion_tree.item(selected_item)["values"][0]
            dia_accion = self.entry_dia_accion.get()
            horaInicio_accion = self.entry_horaInicio_accion.get()
            horaFin_accion = self.entry_horaFin_accion.get()
            ambiente_accion = self.entry_ambiente_accion.get()
            numAlumnos_accion = self.entry_numAlumnos_accion.get()
            id_tipoActividad = self.entry_id_tipoActividad.get()
            id_semana = self.entry_id_semana.get()
            id_docente = self.entry_id_docente.get()
            self.controller.update_accion(
                id_accion, dia_accion, horaInicio_accion, horaFin_accion, ambiente_accion,
                numAlumnos_accion, id_tipoActividad, id_semana, id_docente
            )
            self.update_accion_list()

    def delete_accion(self):
        selected_item = self.accion_tree.selection()
        if selected_item:
            id_accion = self.accion_tree.item(selected_item)["values"][0]
            self.controller.delete_accion(id_accion)
            self.update_accion_list()

    def update_accion_list(self):
        # Clear previous entries
        for item in self.accion_tree.get_children():
            self.accion_tree.delete(item)

        # Fetch updated acciones from controller
        acciones = self.controller.list_all_accion()
        for accion in acciones:
            self.accion_tree.insert("", "end", values=accion)

    def search_accion(self):
        search_term = self.search_entry.get().strip().lower()
        # Clear previous entries
        for item in self.accion_tree.get_children():
            self.accion_tree.delete(item)

        # Fetch acciones matching search term
        acciones = self.controller.list_all_accion()
        filtered_acciones = [accion for accion in acciones if search_term in accion[1].lower()]
        
        for accion in filtered_acciones:
            self.accion_tree.insert("", "end", values=accion)
