import tkinter as tk
from tkinter import ttk

class EscuelaView(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Gestión de Escuela")

        # Inputs
        self.label_nombre = tk.Label(self, text="Nombre")
        self.label_nombre.pack()
        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.pack()

        self.label_id_facultad = tk.Label(self, text="ID Facultad")
        self.label_id_facultad.pack()
        self.entry_id_facultad = tk.Entry(self)
        self.entry_id_facultad.pack()

        # CRUD Buttons
        self.create_button = tk.Button(self, text="Crear Escuela", command=self.create_escuela)
        self.create_button.pack()

        self.update_button = tk.Button(self, text="Actualizar Escuela", command=self.update_escuela)
        self.update_button.pack()

        self.delete_button = tk.Button(self, text="Eliminar Escuela", command=self.delete_escuela)
        self.delete_button.pack()

        # Treeview (Table)
        self.escuela_tree = ttk.Treeview(self, columns=("ID", "Nombre", "Facultad"), show="headings")
        self.escuela_tree.heading("ID", text="ID")
        self.escuela_tree.heading("Nombre", text="Nombre")
        self.escuela_tree.heading("Facultad", text="Facultad")
        self.escuela_tree.pack()

    def create_escuela(self):
        nombre = self.entry_nombre.get()
        id_facultad = self.entry_id_facultad.get()
        self.controller.create_escuela(nombre, id_facultad)
        self.update_escuela_list()

    def update_escuela(self):
        selected = self.escuela_tree.selection()
        if selected:
            id_escuela = self.escuela_tree.item(selected, "values")[0]
            nombre = self.entry_nombre.get()
            id_facultad = self.entry_id_facultad.get()
            self.controller.update_escuela(id_escuela, nombre, id_facultad)
            self.update_escuela_list()

    def delete_escuela(self):
        selected = self.escuela_tree.selection()
        if selected:
            id_escuela = self.escuela_tree.item(selected, "values")[0]
            self.controller.delete_escuela(id_escuela)
            self.update_escuela_list()

    def update_escuela_list(self):
        # Clear previous entries
        for item in self.escuela_tree.get_children():
            self.escuela_tree.delete(item)

        escuelas = self.controller.list_all_escuela()
        for escuela in escuelas:
            self.escuela_tree.insert("", "end", values=escuela)
