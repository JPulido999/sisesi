import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from app.views.general_options_view import GeneralOptionsView

class EscuelaView(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Gestión de Escuela")
        self.state('zoomed')

        # Frame para los inputs
        self.inputs_frame = ttk.Frame(self)
        self.inputs_frame.pack(padx=10, pady=10)

        # Función para crear Labels con or más claro
        def create_labeled_entry(row, column, label_text):
            label = ttk.Label(self.inputs_frame, text=label_text)
            label.grid(row=row, column=column, padx=5, pady=5, sticky="w")
            
            entry = ttk.Entry(self.inputs_frame)
            entry.grid(row=row, column=column + 1, padx=5, pady=5)
            
            return entry
        
        self.entry_nombre = create_labeled_entry(0, 0, "Nombre")
        self.entry_id_facultad = create_labeled_entry(0, 2, "ID Facultad")

        # Campos obligatorios para habilitar el boton de "CREAR"
        for entry in [self.entry_nombre, self.entry_id_facultad]:
            entry.bind("<KeyRelease>", self.check_fields)

        # CRUD Buttons Frame
        self.buttons_frame = ttk.Frame(self)
        self.buttons_frame.pack(padx=10, pady=10)

        self.create_img = GeneralOptionsView.crear_boton("create.png", 20)
        self.update_img = GeneralOptionsView.crear_boton("update.png", 20)
        self.delete_img = GeneralOptionsView.crear_boton("delete.png", 20)

        self.create_button = ttk.Button(self.buttons_frame, text="Crear", image=self.create_img, compound=tk.TOP, command=self.create_escuela, state=tk.DISABLED)
        self.create_button.grid(row=0, column=0, padx=5, pady=5)

        self.update_button = ttk.Button(self.buttons_frame, text="Actualizar", image=self.update_img, compound=tk.TOP, command=self.update_escuela)
        self.update_button.grid(row=0, column=1, padx=5, pady=5)

        self.delete_button = ttk.Button(self.buttons_frame, text="Eliminar", image=self.delete_img, compound=tk.TOP, command=self.delete_escuela)
        self.delete_button.grid(row=0, column=2, padx=5, pady=5)

        # Frame for Treeview with scrollbar
        self.tree_frame = ttk.Frame(self)
        self.tree_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.tree_scroll = ttk.Scrollbar(self.tree_frame, orient=tk.VERTICAL)
        self.tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.escuela_tree = ttk.Treeview(
            self.tree_frame,
            columns=("ID", "Nombre", "Facultad"),
            show="headings",
            yscrollcommand=self.tree_scroll.set
        )
        self.tree_scroll.config(command=self.escuela_tree.yview)

        self.escuela_tree.heading("ID", text="ID")
        self.escuela_tree.heading("Nombre", text="Nombre")
        self.escuela_tree.heading("Facultad", text="Facultad")
        self.escuela_tree.pack(fill=tk.BOTH, expand=True)

        # Ajustar tamaño de las columnas
        self.escuela_tree.column("ID", width=30)
        self.escuela_tree.column("Nombre", width=150)
        self.escuela_tree.column("Facultad", width=150)

        self.escuela_tree.bind('<<TreeviewSelect>>', self.load_selected_escuela)

        # Frame for search
        self.search_frame = ttk.Frame(self)
        self.search_frame.pack(padx=10, pady=10, fill=tk.X)

        ttk.Label(self.search_frame, text="Buscar por nombre:").pack(side=tk.LEFT, padx=5)
        self.search_entry = ttk.Entry(self.search_frame)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        self.search_button = ttk.Button(self.search_frame, text="Buscar", command=self.search_escuela)
        self.search_button.pack(side=tk.LEFT, padx=5)

    def check_fields(self, *args):
        if all([
            self.entry_nombre.get(),
            self.entry_id_facultad.get()
        ]):
            self.create_button.config(state=tk.NORMAL)
        else:
            self.create_button.config(state=tk.DISABLED)

    def load_selected_escuela(self, event):
        selected_item = self.escuela_tree.selection()
        if selected_item:
            item_values = self.escuela_tree.item(selected_item)["values"]
            self.entry_nombre.delete(0, tk.END)
            self.entry_nombre.insert(0, item_values[1])
            self.entry_id_facultad.delete(0, tk.END)
            self.entry_id_facultad.insert(0, item_values[2])

    def create_escuela(self):
        nombre = self.entry_nombre.get()
        id_facultad = self.entry_id_facultad.get()
        self.controller.create_escuela(nombre, id_facultad)
        self.update_escuela_list()

    def update_escuela(self):
        selected_item = self.escuela_tree.selection()
        if selected_item:
            id_escuela = self.escuela_tree.item(selected_item)["values"][0]
            nombre = self.entry_nombre.get()
            id_facultad = self.entry_id_facultad.get()
            self.controller.update_escuela(id_escuela, nombre, id_facultad)
            self.update_escuela_list()

    def delete_escuela(self):
        selected_item = self.escuela_tree.selection()
        if selected_item:
            id_escuela = self.escuela_tree.item(selected_item)["values"][0]
            self.controller.delete_escuela(id_escuela)
            self.update_escuela_list()

    def update_escuela_list(self):
        # Clear previous entries
        for item in self.escuela_tree.get_children():
            self.escuela_tree.delete(item)

        escuelas = self.controller.list_all_escuela()
        for escuela in escuelas:
            self.escuela_tree.insert("", "end", values=escuela)
            
    def search_escuela(self):
        search_term = self.search_entry.get().strip().lower()
        # Clear previous entries
        for item in self.escuela_tree.get_children():
            self.escuela_tree.delete(item)

        escuelas = self.controller.list_all_escuela()
        filtered_escuelas = [escuela for escuela in escuelas if search_term in escuela[1].lower()]
        
        for escuela in filtered_escuelas:
            self.escuela_tree.insert("", "end", values=escuela)
