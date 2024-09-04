import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from app.views.general_options_view import GeneralOptionsView

class SeguimientoView(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Gestión de Seguimiento")
        self.state('zoomed')

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
        self.entry_dia_seguimiento = create_labeled_entry(0, 0, "Día")
        self.entry_hora_seguimiento = create_labeled_entry(0, 2, "Hora")
        self.entry_obs1_seguimiento = create_labeled_entry(0, 4, "Puntualidad Docente")
        self.entry_obs2_seguimiento = create_labeled_entry(1, 0, "Ambiente Adecuado")
        self.entry_obs3_seguimiento = create_labeled_entry(1, 2, "Asistencia ALumnos")
        self.entry_obs4_seguimiento = create_labeled_entry(1, 4, "Observacion4")
        self.entry_obs5_seguimiento = create_labeled_entry(2, 0, "Observacion5")
        self.entry_comentarios_seguimiento = create_labeled_entry(2, 2, "Comentarios")
        self.entry_id_accion = create_labeled_entry(2, 4, "ID Accion")

        # Campos obligatorios para habilitar el botón de "CREAR"
        for entry in [
            self.entry_dia_seguimiento,
            self.entry_hora_seguimiento,
            self.entry_obs1_seguimiento,
            self.entry_obs2_seguimiento,
            self.entry_obs3_seguimiento,
            self.entry_obs4_seguimiento,
            self.entry_obs5_seguimiento,
            self.entry_comentarios_seguimiento,
            self.entry_id_accion
        ]:
            entry.bind("<KeyRelease>", self.check_fields)

        # CRUD Buttons Frame
        self.buttons_frame = ttk.Frame(self)
        self.buttons_frame.pack(padx=10, pady=10)

        self.create_img = GeneralOptionsView.crear_boton("create.png", 20)
        self.update_img = GeneralOptionsView.crear_boton("update.png", 20)
        self.delete_img = GeneralOptionsView.crear_boton("delete.png", 20)

        self.create_button = ttk.Button(self.buttons_frame, text="Crear", image=self.create_img, compound=tk.TOP, command=self.create_seguimiento, state=tk.DISABLED)
        self.create_button.grid(row=0, column=0, padx=5, pady=5)

        self.update_button = ttk.Button(self.buttons_frame, text="Actualizar", image=self.update_img, compound=tk.TOP, command=self.update_seguimiento)
        self.update_button.grid(row=0, column=1, padx=5, pady=5)

        self.delete_button = ttk.Button(self.buttons_frame, text="Eliminar", image=self.delete_img, compound=tk.TOP, command=self.delete_seguimiento)
        self.delete_button.grid(row=0, column=2, padx=5, pady=5)

        # Frame for Treeview with scrollbar
        self.tree_frame = ttk.Frame(self)
        self.tree_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.tree_scroll = ttk.Scrollbar(self.tree_frame, orient=tk.VERTICAL)
        self.tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.seguimiento_tree = ttk.Treeview(
            self.tree_frame,
            columns=("ID", "Día", "Hora", "Puntualidad Docente", "Ambiente Adecuado", "Asistencia Alumnos", "Observacion4", "Observacion5", "Comentarios", "ID Accion"),
            show="headings",
            yscrollcommand=self.tree_scroll.set
        )
        self.tree_scroll.config(command=self.seguimiento_tree.yview)

        self.seguimiento_tree.heading("ID", text="ID")
        self.seguimiento_tree.heading("Día", text="Día")
        self.seguimiento_tree.heading("Hora", text="Hora")
        self.seguimiento_tree.heading("Puntualidad Docente", text="Hora Fin")
        self.seguimiento_tree.heading("Ambiente Adecuado", text="Ambiente")
        self.seguimiento_tree.heading("Asistencia Alumnos", text="Número de Alumnos")
        self.seguimiento_tree.heading("Observacion4", text="ID Tipo Actividad")
        self.seguimiento_tree.heading("Observacion5", text="ID Semana")
        self.seguimiento_tree.heading("ID Accion", text="ID Docente")
        self.seguimiento_tree.pack(fill=tk.BOTH, expand=True)

        # Ajustar tamaño de las columnas
        self.seguimiento_tree.column("ID", width=30)
        self.seguimiento_tree.column("Día", width=100)
        self.seguimiento_tree.column("Hora ", width=100)
        self.seguimiento_tree.column("Puntualidad Docente", width=100)
        self.seguimiento_tree.column("Ambiente Adecuado", width=100)
        self.seguimiento_tree.column("Asistencia Alumnos", width=100)
        self.seguimiento_tree.column("Observacion4", width=100)
        self.seguimiento_tree.column("Observacion5", width=100)
        self.seguimiento_tree.column("ID Accion", width=100)
        self.seguimiento_tree.bind('<<TreeviewSelect>>', self.load_selected_seguimiento)

        # Frame for search
        self.search_frame = ttk.Frame(self)
        self.search_frame.pack(padx=10, pady=10, fill=tk.X)

        ttk.Label(self.search_frame, text="Buscar por día:").pack(side=tk.LEFT, padx=5)
        self.search_entry = ttk.Entry(self.search_frame)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        self.search_button = ttk.Button(self.search_frame, text="Buscar", command=self.search_seguimiento)
        self.search_button.pack(side=tk.LEFT, padx=5)

    def check_fields(self, *args):
        if all([
            self.entry_dia_seguimiento.get(),
            self.entry_hora_seguimiento.get(),
            self.entry_obs1_seguimiento.get(),
            self.entry_obs2_seguimiento.get(),
            self.entry_obs3_seguimiento.get(),
            self.entry_obs4_seguimiento.get(),
            self.entry_obs5_seguimiento.get(),
            self.entry_comentarios_seguimiento.get(),
            self.entry_id_accion.get()
        ]):
            self.create_button.config(state=tk.NORMAL)
        else:
            self.create_button.config(state=tk.DISABLED)

    def load_selected_seguimiento(self, event):
        selected_item = self.seguimiento_tree.selection()
        if selected_item:
            item_values = self.seguimiento_tree.item(selected_item)["values"]
            self.entry_dia_seguimiento.delete(0, tk.END)
            self.entry_dia_seguimiento.insert(0, item_values[1])
            self.entry_hora_seguimiento.delete(0, tk.END)
            self.entry_hora_seguimiento.insert(0, item_values[2])
            self.entry_obs1_seguimiento.delete(0, tk.END)
            self.entry_obs1_seguimiento.insert(0, item_values[3])
            self.entry_obs2_seguimiento.delete(0, tk.END)
            self.entry_obs2_seguimiento.insert(0, item_values[4])
            self.entry_obs3_seguimiento.delete(0, tk.END)
            self.entry_obs3_seguimiento.insert(0, item_values[5])
            self.entry_obs4_seguimiento.delete(0, tk.END)
            self.entry_obs4_seguimiento.insert(0, item_values[6])
            self.entry_obs5_seguimiento.delete(0, tk.END)
            self.entry_obs5_seguimiento.insert(0, item_values[7])
            self.entry_comentarios_seguimiento.delete(0, tk.END)
            self.entry_comentarios_seguimiento.insert(0, item_values[8])
            self.entry_id_accion.delete(0, tk.END)
            self.entry_id_accion.insert(0, item_values[9])

    def create_seguimiento(self):
        dia_seguimiento = self.entry_dia_seguimiento.get()
        hora_seguimiento = self.entry_hora_seguimiento.get()
        obs1_seguimiento = self.entry_obs1_seguimiento.get()
        obs2_seguimiento = self.entry_obs2_seguimiento.get()
        obs3_seguimiento = self.entry_obs3_seguimiento.get()
        obs4_seguimiento = self.entry_obs4_seguimiento.get()
        obs5_seguimiento = self.entry_obs5_seguimiento.get()
        comentarios_seguimiento = self.entry_comentarios_seguimiento.get()
        id_accion = self.entry_id_accion.get()

        self.controller.create_seguimiento(
            dia_seguimiento, hora_seguimiento, obs1_seguimiento, obs2_seguimiento,
            obs3_seguimiento, obs4_seguimiento, obs5_seguimiento, comentarios_seguimiento, id_accion
        )
        self.update_seguimiento_list()

    def update_seguimiento(self):
        selected_item = self.seguimiento_tree.selection()
        if selected_item:
            id_seguimiento = self.seguimiento_tree.item(selected_item)["values"][0]
            dia_seguimiento = self.entry_dia_seguimiento.get()
            hora_seguimiento = self.entry_hora_seguimiento.get()
            obs1_seguimiento = self.entry_obs1_seguimiento.get()
            obs2_seguimiento = self.entry_obs2_seguimiento.get()
            obs3_seguimiento = self.entry_obs3_seguimiento.get()
            obs4_seguimiento = self.entry_obs4_seguimiento.get()
            obs5_seguimiento = self.entry_obs5_seguimiento.get()
            comentarios_seguimiento = self.entry_comentarios_seguimiento.get()
            id_accion = self.entry_id_accion.get()
            self.controller.update_seguimiento(
                id_seguimiento, dia_seguimiento, hora_seguimiento, obs1_seguimiento, obs2_seguimiento,
                obs3_seguimiento, obs4_seguimiento, obs5_seguimiento, comentarios_seguimiento, id_accion
            )
            self.update_seguimiento_list()

    def delete_seguimiento(self):
        selected_item = self.seguimiento_tree.selection()
        if selected_item:
            id_seguimiento = self.seguimiento_tree.item(selected_item)["values"][0]
            self.controller.delete_seguimiento(id_seguimiento)
            self.update_seguimiento_list()

    def update_seguimiento_list(self):
        # Clear previous entries
        for item in self.seguimiento_tree.get_children():
            self.seguimiento_tree.delete(item)

        # Fetch updated seguimientoes from controller
        seguimientos = self.controller.list_all_seguimiento()
        for seguimiento in seguimientos:
            self.seguimiento_tree.insert("", "end", values=seguimiento)

    def search_seguimiento(self):
        search_term = self.search_entry.get().strip().lower()
        # Clear previous entries
        for item in self.seguimiento_tree.get_children():
            self.seguimiento_tree.delete(item)

        # Fetch seguimientoes matching search term
        seguimientos = self.controller.list_all_seguimiento()
        filtered_seguimientoes = [seguimiento for seguimiento in seguimientos if search_term in seguimiento[1].lower()]
        
        for seguimiento in filtered_seguimientoes:
            self.seguimiento_tree.insert("", "end", values=seguimiento)
