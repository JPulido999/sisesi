import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from app.views.general_options_view import GeneralOptionsView

class ContratoView(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Gestión de Contratos")
        self.state('zoomed')

        # Frame para los inputs
        self.inputs_frame = ttk.Frame(self)
        self.inputs_frame.pack(padx=10, pady=10)

        # Función para crear Labels con color más claro
        def create_labeled_entry(row, column, label_text):
            label = ttk.Label(self.inputs_frame, text=label_text)
            label.grid(row=row, column=column, padx=5, pady=5, sticky="w")
            
            entry = ttk.Entry(self.inputs_frame)
            entry.grid(row=row, column=column + 1, padx=5, pady=5)
            
            return entry

        self.entry_periodoInicio = create_labeled_entry(0, 0, "Periodo Inicio")
        self.entry_periodoFin = create_labeled_entry(0, 2, "Periodo Fin")
        self.entry_id_docente = create_labeled_entry(1, 0, "ID Docente")
        self.entry_renacyt = create_labeled_entry(1, 2, "Renacyt")
        self.entry_id_condicion = create_labeled_entry(2, 0, "ID Condición")
        self.entry_id_regimen = create_labeled_entry(2, 2, "ID Régimen")
        self.entry_id_categoria = create_labeled_entry(3, 0, "ID Categoría")

        # CRUD Buttons Frame
        self.buttons_frame = ttk.Frame(self)
        self.buttons_frame.pack(padx=10, pady=10)

        self.create_img=GeneralOptionsView.crear_boton("create.png", 20)
        self.update_img=GeneralOptionsView.crear_boton("update.png", 20)
        self.delete_img=GeneralOptionsView.crear_boton("delete.png", 20)

        self.create_button = ttk.Button(self.buttons_frame, text="Crear", image=self.create_img, compound=tk.TOP, command=self.create_contrato)#, state=tk.DISABLED)
        self.create_button.grid(row=0, column=0, padx=5, pady=5)

        self.update_button = ttk.Button(self.buttons_frame, text="Actualizar", image=self.update_img, compound=tk.TOP, command=self.update_contrato)
        self.update_button.grid(row=0, column=1, padx=5, pady=5)

        self.delete_button = ttk.Button(self.buttons_frame, text="Eliminar", image=self.delete_img, compound=tk.TOP, command=self.delete_contrato)
        self.delete_button.grid(row=0, column=2, padx=5, pady=5)

        # Frame for Treeview with scrollbar
        self.tree_frame = ttk.Frame(self)
        self.tree_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.tree_scroll = ttk.Scrollbar(self.tree_frame, orient=tk.VERTICAL)
        self.tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.contrato_tree = ttk.Treeview(
            self.tree_frame,
            columns=("ID", "Periodo Inicio", "Periodo Fin", "ID Docente", "Renacyt", "ID Condición", "ID Régimen", "ID Categoría"),
            show="headings",
            yscrollcommand=self.tree_scroll.set
        )
        self.tree_scroll.config(command=self.contrato_tree.yview)

        self.contrato_tree.heading("ID", text="ID")
        self.contrato_tree.heading("Periodo Inicio", text="Periodo Inicio")
        self.contrato_tree.heading("Periodo Fin", text="Periodo Fin")
        self.contrato_tree.heading("ID Docente", text="ID Docente")
        self.contrato_tree.heading("Renacyt", text="Renacyt")
        self.contrato_tree.heading("ID Condición", text="ID Condición")
        self.contrato_tree.heading("ID Régimen", text="ID Régimen")
        self.contrato_tree.heading("ID Categoría", text="ID Categoría")
        self.contrato_tree.pack(fill=tk.BOTH, expand=True)

        # Ajustar tamaño de las columnas
        self.contrato_tree.column("ID", width=30)
        self.contrato_tree.column("Periodo Inicio", width=150)
        self.contrato_tree.column("Periodo Fin", width=150)
        self.contrato_tree.column("ID Docente", width=100)
        self.contrato_tree.column("Renacyt", width=100)
        self.contrato_tree.column("ID Condición", width=100)
        self.contrato_tree.column("ID Régimen", width=100)
        self.contrato_tree.column("ID Categoría", width=100)

        self.contrato_tree.bind('<<TreeviewSelect>>', self.load_selected_contrato)

        # Frame for search
        self.search_frame = ttk.Frame(self)
        self.search_frame.pack(padx=10, pady=10, fill=tk.X)

        ttk.Label(self.search_frame, text="Buscar por ID Docente:").pack(side=tk.LEFT, padx=5)
        self.search_entry = ttk.Entry(self.search_frame)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        self.search_button = ttk.Button(self.search_frame, text="Buscar", command=self.search_contrato)
        self.search_button.pack(side=tk.LEFT, padx=5)

    def load_selected_contrato(self, event):
        selected_item = self.contrato_tree.selection()
        if selected_item:
            item_values = self.contrato_tree.item(selected_item)["values"]
            self.entry_periodoInicio.delete(0, tk.END)
            self.entry_periodoInicio.insert(0, item_values[1])
            self.entry_periodoFin.delete(0, tk.END)
            self.entry_periodoFin.insert(0, item_values[2])
            self.entry_id_docente.delete(0, tk.END)
            self.entry_id_docente.insert(0, item_values[3])
            self.entry_renacyt.delete(0, tk.END)
            self.entry_renacyt.insert(0, item_values[4])
            self.entry_id_condicion.delete(0, tk.END)
            self.entry_id_condicion.insert(0, item_values[5])
            self.entry_id_regimen.delete(0, tk.END)
            self.entry_id_regimen.insert(0, item_values[6])
            self.entry_id_categoria.delete(0, tk.END)
            self.entry_id_categoria.insert(0, item_values[7])

    def create_contrato(self):
        periodoInicio = self.entry_periodoInicio.get()
        periodoFin = self.entry_periodoFin.get()
        id_docente = self.entry_id_docente.get()
        renacyt = self.entry_renacyt.get()
        id_condicion = self.entry_id_condicion.get()
        id_regimen = self.entry_id_regimen.get()
        id_categoria = self.entry_id_categoria.get()
        self.controller.create_contrato(periodoInicio, periodoFin, id_docente, renacyt, id_condicion, id_regimen, id_categoria)
        self.update_contrato_list()

    def update_contrato(self):
        selected_item = self.contrato_tree.selection()
        if selected_item:
            id_contrato = self.contrato_tree.item(selected_item)["values"][0]
            periodoInicio = self.entry_periodoInicio.get()
            periodoFin = self.entry_periodoFin.get()
            id_docente = self.entry_id_docente.get()
            renacyt = self.entry_renacyt.get()
            id_condicion = self.entry_id_condicion.get()
            id_regimen = self.entry_id_regimen.get()
            id_categoria = self.entry_id_categoria.get()
            self.controller.update_contrato(id_contrato, periodoInicio, periodoFin, id_docente, renacyt, id_condicion, id_regimen, id_categoria)
            self.update_contrato_list()

    def delete_contrato(self):
        selected_item = self.contrato_tree.selection()
        if selected_item:
            id_contrato = self.contrato_tree.item(selected_item)["values"][0]
            self.controller.delete_contrato(id_contrato)
            self.update_contrato_list()

    def update_contrato_list(self):
        # Clear previous entries
        for item in self.contrato_tree.get_children():
            self.contrato_tree.delete(item)

        contratos = self.controller.list_all_contrato()
        for contrato in contratos:
            self.contrato_tree.insert("", "end", values=contrato)

    def search_contrato(self):
        search_term = self.search_entry.get().strip().lower()
        # Clear previous entries
        for item in self.contrato_tree.get_children():
            self.contrato_tree.delete(item)

        # Fetch contratos matching search term
        contratos = self.controller.list_all_contrato()
        filtered_contratos = [contrato for contrato in contratos if search_term in str(contrato[3]).lower()]
        
        for contrato in filtered_contratos:
            self.contrato_tree.insert("", "end", values=contrato)
