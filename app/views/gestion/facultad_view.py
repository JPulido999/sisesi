import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from app.views.general_options_view import GeneralOptionsView

class FacultadView(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Gestión de Facultad")
        self.state('zoomed')

        # Frame para los inputs
        self.inputs_frame = ttk.Frame(self)
        self.inputs_frame.pack(padx=10, pady=10)

        # Función para crear Labels con entrada de texto
        def create_labeled_entry(row, column, label_text):
            label = ttk.Label(self.inputs_frame, text=label_text)
            label.grid(row=row, column=column, padx=5, pady=5, sticky="w")
            
            entry = ttk.Entry(self.inputs_frame)
            entry.grid(row=row, column=column + 1, padx=5, pady=5)
            
            return entry

        self.entry_sigla = create_labeled_entry(0, 0, "Sigla")
        self.entry_nombre = create_labeled_entry(0, 2, "Nombre")

        # CRUD Buttons Frame
        self.buttons_frame = ttk.Frame(self)
        self.buttons_frame.pack(padx=10, pady=10)

        self.create_img = GeneralOptionsView.crear_boton("create.png", 20)
        self.update_img = GeneralOptionsView.crear_boton("update.png", 20)
        self.delete_img = GeneralOptionsView.crear_boton("delete.png", 20)

        self.create_button = ttk.Button(self.buttons_frame, text="Crear", image=self.create_img, compound=tk.TOP, command=self.create_facultad)
        self.create_button.grid(row=0, column=0, padx=5, pady=5)

        self.update_button = ttk.Button(self.buttons_frame, text="Actualizar", image=self.update_img, compound=tk.TOP, command=self.update_facultad)
        self.update_button.grid(row=0, column=1, padx=5, pady=5)

        self.delete_button = ttk.Button(self.buttons_frame, text="Eliminar", image=self.delete_img, compound=tk.TOP, command=self.delete_facultad)
        self.delete_button.grid(row=0, column=2, padx=5, pady=5)

        # Frame for Treeview with scrollbar
        self.tree_frame = ttk.Frame(self)
        self.tree_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.tree_scroll = ttk.Scrollbar(self.tree_frame, orient=tk.VERTICAL)
        self.tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.facultad_tree = ttk.Treeview(
            self.tree_frame,
            columns=("ID", "Sigla", "Nombre"),
            show="headings",
            yscrollcommand=self.tree_scroll.set
        )
        self.tree_scroll.config(command=self.facultad_tree.yview)

        self.facultad_tree.heading("ID", text="ID")
        self.facultad_tree.heading("Sigla", text="Sigla")
        self.facultad_tree.heading("Nombre", text="Nombre")
        self.facultad_tree.pack(fill=tk.BOTH, expand=True)

        # Ajustar tamaño de las columnas
        self.facultad_tree.column("ID", width=50)
        self.facultad_tree.column("Sigla", width=150)
        self.facultad_tree.column("Nombre", width=300)

        self.facultad_tree.bind('<<TreeviewSelect>>', self.load_selected_facultad)

        # Frame for search
        self.search_frame = ttk.Frame(self)
        self.search_frame.pack(padx=10, pady=10, fill=tk.X)

        ttk.Label(self.search_frame, text="Buscar por sigla:").pack(side=tk.LEFT, padx=5)
        self.search_entry = ttk.Entry(self.search_frame)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        self.search_button = ttk.Button(self.search_frame, text="Buscar", command=self.search_facultad)
        self.search_button.pack(side=tk.LEFT, padx=5)

    def load_selected_facultad(self, event):
        selected_item = self.facultad_tree.selection()
        if selected_item:
            item_values = self.facultad_tree.item(selected_item)["values"]
            self.entry_sigla.delete(0, tk.END)
            self.entry_sigla.insert(0, item_values[1])
            self.entry_nombre.delete(0, tk.END)
            self.entry_nombre.insert(0, item_values[2])

    def create_facultad(self):
        sigla = self.entry_sigla.get()
        nombre = self.entry_nombre.get()

        if self.controller.buscar_facultad_por_nombre(nombre):
            messagebox.showinfo("Advertencia", "La Facultad ya está registrada")
        else:
            self.controller.create_facultad(sigla, nombre)
            self.update_facultad_list()

    def update_facultad(self):
        selected_item = self.facultad_tree.selection()
        if selected_item:
            id_facultad = self.facultad_tree.item(selected_item)["values"][0]
            sigla = self.entry_sigla.get()
            nombre = self.entry_nombre.get()
            self.controller.update_facultad(id_facultad, sigla, nombre)
            self.update_facultad_list()

    def delete_facultad(self):
        selected_item = self.facultad_tree.selection()
        if selected_item:
            id_facultad = self.facultad_tree.item(selected_item)["values"][0]
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

    def search_facultad(self):
        search_term = self.search_entry.get().strip().lower()
        # Clear previous entries
        for item in self.facultad_tree.get_children():
            self.facultad_tree.delete(item)

        # Fetch facultades matching search term
        facultades = self.controller.list_all_facultad()
        filtered_facultades = [facultad for facultad in facultades if search_term in facultad[1].lower()]
        
        for facultad in filtered_facultades:
            self.facultad_tree.insert("", "end", values=facultad)
