import tkinter as tk
from tkinter import ttk

class ContratoView(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Gestión de Contratos")

        # Inputs
        self.label_periodoInicio = tk.Label(self, text="Periodo Inicio")
        self.label_periodoInicio.pack()
        self.entry_periodoInicio = tk.Entry(self)
        self.entry_periodoInicio.pack()

        self.label_periodoFin = tk.Label(self, text="Periodo Fin")
        self.label_periodoFin.pack()
        self.entry_periodoFin = tk.Entry(self)
        self.entry_periodoFin.pack()

        self.label_id_docente = tk.Label(self, text="ID Docente")
        self.label_id_docente.pack()
        self.entry_id_docente = tk.Entry(self)
        self.entry_id_docente.pack()

        self.label_renacyt = tk.Label(self, text="Renacyt")
        self.label_renacyt.pack()
        self.entry_renacyt = tk.Entry(self)
        self.entry_renacyt.pack()

        self.label_id_condicion = tk.Label(self, text="ID Condición")
        self.label_id_condicion.pack()
        self.entry_id_condicion = tk.Entry(self)
        self.entry_id_condicion.pack()

        self.label_id_regimen = tk.Label(self, text="ID Régimen")
        self.label_id_regimen.pack()
        self.entry_id_regimen = tk.Entry(self)
        self.entry_id_regimen.pack()

        self.label_id_categoria = tk.Label(self, text="ID Categoría")
        self.label_id_categoria.pack()
        self.entry_id_categoria = tk.Entry(self)
        self.entry_id_categoria.pack()

        # CRUD Buttons
        self.create_button = tk.Button(self, text="Crear Contrato", command=self.create_contrato)
        self.create_button.pack()

        self.update_button = tk.Button(self, text="Actualizar Contrato", command=self.update_contrato)
        self.update_button.pack()

        self.delete_button = tk.Button(self, text="Eliminar Contrato", command=self.delete_contrato)
        self.delete_button.pack()

        # Treeview (Table)
        self.contrato_tree = ttk.Treeview(self, columns=("ID", "Periodo Inicio", "Periodo Fin", "ID Docente", "Renacyt", "ID Condición", "ID Régimen", "ID Categoría"), show="headings")
        self.contrato_tree.heading("ID", text="ID", anchor=tk.CENTER)
        self.contrato_tree.column("ID", width=50, anchor=tk.CENTER)

        self.contrato_tree.heading("Periodo Inicio", text="Periodo Inicio", anchor=tk.CENTER)
        self.contrato_tree.column("Periodo Inicio", width=150, anchor=tk.CENTER)

        self.contrato_tree.heading("Periodo Fin", text="Periodo Fin", anchor=tk.CENTER)
        self.contrato_tree.column("Periodo Fin", width=150, anchor=tk.CENTER)

        self.contrato_tree.heading("ID Docente", text="ID Docente", anchor=tk.CENTER)
        self.contrato_tree.column("ID Docente", width=100, anchor=tk.CENTER)

        self.contrato_tree.heading("Renacyt", text="Renacyt", anchor=tk.CENTER)
        self.contrato_tree.column("Renacyt", width=150, anchor=tk.CENTER)

        self.contrato_tree.heading("ID Condición", text="ID Condición", anchor=tk.CENTER)
        self.contrato_tree.column("ID Condición", width=100, anchor=tk.CENTER)

        self.contrato_tree.heading("ID Régimen", text="ID Régimen", anchor=tk.CENTER)
        self.contrato_tree.column("ID Régimen", width=100, anchor=tk.CENTER)

        self.contrato_tree.heading("ID Categoría", text="ID Categoría", anchor=tk.CENTER)
        self.contrato_tree.column("ID Categoría", width=100, anchor=tk.CENTER)

        self.contrato_tree.pack()

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
        selected = self.contrato_tree.selection()
        if selected:
            id_contrato = self.contrato_tree.item(selected, "values")[0]
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
        selected = self.contrato_tree.selection()
        if selected:
            id_contrato = self.contrato_tree.item(selected, "values")[0]
            self.controller.delete_contrato(id_contrato)
            self.update_contrato_list()

    def update_contrato_list(self):
        # Clear previous entries
        for item in self.contrato_tree.get_children():
            self.contrato_tree.delete(item)

        contratos = self.controller.list_all_contrato()
        for contrato in contratos:
            self.contrato_tree.insert("", "end", values=contrato)
