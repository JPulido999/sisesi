import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from app.views.general_options_view import GeneralOptionsView

class LicenciaView(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Gestión de Licencia")

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
        self.entry_resolucion_licencia = create_labeled_entry(0, 0, "Resolución")
        self.entry_fechaInicio_licencia = create_labeled_entry(0, 2, "Fecha Inicio")
        self.entry_fechaFin_licencia = create_labeled_entry(0, 4, "Fecha Fin")
        self.entry_observacion_licencia = create_labeled_entry(1, 0, "Observación")
        self.entry_id_tipoLicencia = create_labeled_entry(1, 2, "ID Tipo Licencia")
        self.entry_id_docente = create_labeled_entry(1, 4, "ID Docente")

        # Campos obligatorios para habilitar el botón de "CREAR"
        for entry in [
            self.entry_id_docente
        ]:
            entry.bind("<KeyRelease>", self.check_fields)

        # CRUD Buttons Frame
        self.buttons_frame = ttk.Frame(self)
        self.buttons_frame.pack(padx=10, pady=10)

        self.create_img = GeneralOptionsView.crear_boton("create.png", 20)
        self.update_img = GeneralOptionsView.crear_boton("update.png", 20)
        self.delete_img = GeneralOptionsView.crear_boton("delete.png", 20)

        self.create_button = ttk.Button(self.buttons_frame, text="Crear", image=self.create_img, compound=tk.TOP, command=self.create_licencia, state=tk.DISABLED)
        self.create_button.grid(row=0, column=0, padx=5, pady=5)

        self.update_button = ttk.Button(self.buttons_frame, text="Actualizar", image=self.update_img, compound=tk.TOP, command=self.update_licencia)
        self.update_button.grid(row=0, column=1, padx=5, pady=5)

        self.delete_button = ttk.Button(self.buttons_frame, text="Eliminar", image=self.delete_img, compound=tk.TOP, command=self.delete_licencia)
        self.delete_button.grid(row=0, column=2, padx=5, pady=5)

        # Frame for Treeview with scrollbar
        self.tree_frame = ttk.Frame(self)
        self.tree_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.tree_scroll = ttk.Scrollbar(self.tree_frame, orient=tk.VERTICAL)
        self.tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.licencia_tree = ttk.Treeview(
            self.tree_frame,
            columns=("ID", "Resolución", "Fecha Inicio", "Fecha Fin", "Observación", "ID Tipo Licencia", "ID Docente"),
            show="headings",
            yscrollcommand=self.tree_scroll.set
        )
        self.tree_scroll.config(command=self.licencia_tree.yview)

        self.licencia_tree.heading("ID", text="ID")
        self.licencia_tree.heading("Resolución", text="Resolución")
        self.licencia_tree.heading("Fecha Inicio", text="Fecha Inicio")
        self.licencia_tree.heading("Fecha Fin", text="Fecha Fin")
        self.licencia_tree.heading("Observación", text="Observación")
        self.licencia_tree.heading("ID Tipo Licencia", text="ID Tipo Licencia")
        self.licencia_tree.heading("ID Docente", text="ID Docente")
        self.licencia_tree.pack(fill=tk.BOTH, expand=True)

        # Ajustar tamaño de las columnas
        self.licencia_tree.column("ID", width=30)
        self.licencia_tree.column("Resolución", width=100)
        self.licencia_tree.column("Fecha Inicio", width=100)
        self.licencia_tree.column("Fecha Fin", width=100)
        self.licencia_tree.column("Observación", width=100)
        self.licencia_tree.column("ID Tipo Licencia", width=100)
        self.licencia_tree.column("ID Docente", width=100)

        # Frame for search
        self.search_frame = ttk.Frame(self)
        self.search_frame.pack(padx=10, pady=10, fill=tk.X)

        ttk.Label(self.search_frame, text="Buscar por resolución:").pack(side=tk.LEFT, padx=5)
        self.search_entry = ttk.Entry(self.search_frame)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        self.search_button = ttk.Button(self.search_frame, text="Buscar", command=self.search_licencia)
        self.search_button.pack(side=tk.LEFT, padx=5)

    def check_fields(self, *args):
        if all([
            self.entry_id_docente.get()
        ]):
            self.create_button.config(state=tk.NORMAL)
        else:
            self.create_button.config(state=tk.DISABLED)

    def create_licencia(self):
        resolucion_licencia = self.entry_resolucion_licencia.get()
        fechaInicio_licencia = self.entry_fechaInicio_licencia.get()
        fechaFin_licencia = self.entry_fechaFin_licencia.get()
        observacion_licencia = self.entry_observacion_licencia.get()
        id_tipoLicencia = self.entry_id_tipoLicencia.get()
        id_docente = self.entry_id_docente.get()

        if self.controller.buscar_licencia_por_resolucion(resolucion_licencia):
            messagebox.showinfo("Advertencia", "La Licencia ya está registrada")
        else:
            self.controller.create_licencia(
                resolucion_licencia, fechaInicio_licencia, fechaFin_licencia,
                observacion_licencia, id_tipoLicencia, id_docente
            )
            self.update_licencia_list()

    def update_licencia(self):
        selected_item = self.licencia_tree.selection()
        if selected_item:
            id_licencia = self.licencia_tree.item(selected_item)["values"][0]
            resolucion_licencia = self.entry_resolucion_licencia.get()
            fechaInicio_licencia = self.entry_fechaInicio_licencia.get()
            fechaFin_licencia = self.entry_fechaFin_licencia.get()
            observacion_licencia = self.entry_observacion_licencia.get()
            id_tipoLicencia = self.entry_id_tipoLicencia.get()
            id_docente = self.entry_id_docente.get()
            self.controller.update_licencia(
                id_licencia, resolucion_licencia, fechaInicio_licencia, fechaFin_licencia,
                observacion_licencia, id_tipoLicencia, id_docente
            )
            self.update_licencia_list()

    def delete_licencia(self):
        selected_item = self.licencia_tree.selection()
        if selected_item:
            id_licencia = self.licencia_tree.item(selected_item)["values"][0]
            self.controller.delete_licencia(id_licencia)
            self.update_licencia_list()

    def update_licencia_list(self):
        # Clear previous entries
        for item in self.licencia_tree.get_children():
            self.licencia_tree.delete(item)

        # Fetch updated licencias from controller
        licencias = self.controller.list_all_licencia()
        for licencia in licencias:
            self.licencia_tree.insert("", "end", values=licencia)

    def search_licencia(self):
        search_term = self.search_entry.get().strip().lower()
        # Clear previous entries
        for item in self.licencia_tree.get_children():
            self.licencia_tree.delete(item)

        # Fetch licencias matching search term
        licencias = self.controller.list_all_licencia()
        filtered_licencias = [licencia for licencia in licencias if search_term in licencia[1].lower()]
        
        for licencia in filtered_licencias:
            self.licencia_tree.insert("", "end", values=licencia)
