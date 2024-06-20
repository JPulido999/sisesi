import tkinter as tk
from tkinter import ttk

class FacultadView(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Gestión de Facultad")

        # Inputs
        self.label_sigla = tk.Label(self, text="Sigla")
        self.label_sigla.pack()
        self.entry_sigla = tk.Entry(self)
        self.entry_sigla.pack()

        self.label_nombre = tk.Label(self, text="Nombre")
        self.label_nombre.pack()
        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.pack()

        # CRUD Buttons
        self.create_button = tk.Button(self, text="Crear Facultad", command=self.create_facultad)
        self.create_button.pack()

        self.update_button = tk.Button(self, text="Actualizar Facultad", command=self.update_facultad)
        self.update_button.pack()

        self.delete_button = tk.Button(self, text="Eliminar Facultad", command=self.delete_facultad)
        self.delete_button.pack()

        # Treeview (Table)
        self.facultad_tree = ttk.Treeview(self, columns=("ID", "Sigla", "Nombre"), show="headings")
        self.facultad_tree.heading("ID", text="ID")
        self.facultad_tree.heading("Sigla", text="Sigla")
        self.facultad_tree.heading("Nombre", text="Nombre")
        self.facultad_tree.pack()

    def create_facultad(self):
        sigla = self.entry_sigla.get()
        nombre = self.entry_nombre.get()
        self.controller.create_facultad(sigla, nombre)
        self.update_facultad_list()

    def update_facultad(self):
        selected = self.facultad_tree.selection()
        if selected:
            id_facultad = self.facultad_tree.item(selected, "values")[0]
            sigla = self.entry_sigla.get()
            nombre = self.entry_nombre.get()
            self.controller.update_facultad(id_facultad, sigla, nombre)
            self.update_facultad_list()

    def delete_facultad(self):
        selected = self.facultad_tree.selection()
        if selected:
            id_facultad = self.facultad_tree.item(selected, "values")[0]
            self.controller.delete_facultad(id_facultad)
            self.update_facultad_list()

    def update_facultad_list(self):
        # Clear previous entries
        for item in self.facultad_tree.get_children():
            self.facultad_tree.delete(item)

        # Fetch updated facultades from controller
        facultades = self.controller.list_all_facultad()
        for facultad in facultades:
            self.facultad_tree.insert("", "end", values=facultad)
