import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from app.views.general_options_view import GeneralOptionsView

class DocenteView(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Gestión de Docente")

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

        
        self.entry_nombres = create_labeled_entry(0, 0, "Nombres")
        self.entry_apellido_paterno = create_labeled_entry(0, 2, "Apellido Paterno")
        self.entry_apellido_materno = create_labeled_entry(0, 4, "Apellido Materno")
        self.entry_correo = create_labeled_entry(1, 0, "Correo")
        self.entry_dni = create_labeled_entry(1, 2, "DNI")
        self.entry_celular = create_labeled_entry(1, 4, "Celular")
        self.entry_grado_maestro = create_labeled_entry(2, 0, "Grado Maestro")
        self.entry_grado_doctor = create_labeled_entry(2, 2, "Grado Doctor")
        self.entry_titulo_profesional = create_labeled_entry(2, 4, "Título Profesional")
        self.entry_titulo_esp_medico = create_labeled_entry(3, 0, "Título Esp. Médico")
        self.entry_titulo_esp_odonto = create_labeled_entry(3, 2, "Título Esp. Odonto")
        self.entry_grado_bachiller = create_labeled_entry(3, 4, "Grado Bachiller")




        #Campos obligatorios para habilitar el boton de "CREAR"
        for entry in [
            self.entry_nombres,
            self.entry_apellido_paterno,
            self.entry_apellido_materno,
            self.entry_correo,
            self.entry_dni,
            self.entry_celular,
            self.entry_grado_maestro,
            self.entry_grado_doctor,
            self.entry_titulo_profesional,
            self.entry_titulo_esp_medico,
            self.entry_titulo_esp_odonto,
            self.entry_grado_bachiller
        ]:
            entry.bind("<KeyRelease>", self.check_fields)

        # CRUD Buttons Frame
        self.buttons_frame = ttk.Frame(self)
        self.buttons_frame.pack(padx=10, pady=10)

        self.create_img=GeneralOptionsView.crear_boton("create.png", 20)
        self.update_img=GeneralOptionsView.crear_boton("update.png", 20)
        self.delete_img=GeneralOptionsView.crear_boton("delete.png", 20)

        self.create_button = ttk.Button(self.buttons_frame, text="Crear", image=self.create_img, compound=tk.TOP, command=self.create_docente, state=tk.DISABLED)
        self.create_button.grid(row=0, column=0, padx=5, pady=5)

        self.update_button = ttk.Button(self.buttons_frame, text="Actualizar", image=self.update_img, compound=tk.TOP, command=self.update_docente)
        self.update_button.grid(row=0, column=1, padx=5, pady=5)

        self.delete_button = ttk.Button(self.buttons_frame, text="Eliminar", image=self.delete_img, compound=tk.TOP, command=self.delete_docente)
        self.delete_button.grid(row=0, column=2, padx=5, pady=5)

        # Frame for Treeview with scrollbar
        self.tree_frame = ttk.Frame(self)
        self.tree_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.tree_scroll = ttk.Scrollbar(self.tree_frame, orient=tk.VERTICAL)
        self.tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.docente_tree = ttk.Treeview(
            self.tree_frame,
            columns=("ID", "Nombres", "Apellido Paterno", "Apellido Materno", "Correo", "DNI", "Celular", "Grado Maestro", "Grado Doctor", "Título Profesional", "Título Esp. Médico", "Título Esp. Odonto", "Grado Bachiller"),
            show="headings",
            yscrollcommand=self.tree_scroll.set
        )
        self.tree_scroll.config(command=self.docente_tree.yview)

        self.docente_tree.heading("ID", text="ID")
        self.docente_tree.heading("Nombres", text="Nombres")
        self.docente_tree.heading("Apellido Paterno", text="Apellido Paterno")
        self.docente_tree.heading("Apellido Materno", text="Apellido Materno")
        self.docente_tree.heading("Correo", text="Correo")
        self.docente_tree.heading("DNI", text="DNI")
        self.docente_tree.heading("Celular", text="Celular")
        self.docente_tree.heading("Grado Maestro", text="Grado Maestro")
        self.docente_tree.heading("Grado Doctor", text="Grado Doctor")
        self.docente_tree.heading("Título Profesional", text="Título Profesional")
        self.docente_tree.heading("Título Esp. Médico", text="Título Esp. Médico")
        self.docente_tree.heading("Título Esp. Odonto", text="Título Esp. Odonto")
        self.docente_tree.heading("Grado Bachiller", text="Grado Bachiller")
        self.docente_tree.pack(fill=tk.BOTH, expand=True)

        # Ajustar tamaño de las columnas
        self.docente_tree.column("ID", width=30)
        self.docente_tree.column("Nombres", width=150)
        self.docente_tree.column("Apellido Paterno", width=150)
        self.docente_tree.column("Apellido Materno", width=150)
        self.docente_tree.column("Correo", width=150)
        self.docente_tree.column("DNI", width=60)
        self.docente_tree.column("Celular", width=70)
        self.docente_tree.column("Grado Maestro", width=150)
        self.docente_tree.column("Grado Doctor", width=150)
        self.docente_tree.column("Título Profesional", width=150)
        self.docente_tree.column("Título Esp. Médico", width=150)
        self.docente_tree.column("Título Esp. Odonto", width=150)
        self.docente_tree.column("Grado Bachiller", width=150)

    def check_fields(self, *args):
        if all([
            self.entry_nombres.get(),
            self.entry_apellido_paterno.get(),
            self.entry_apellido_materno.get(),
            self.entry_correo.get(),
            self.entry_dni.get(),
            self.entry_celular.get(),
            self.entry_grado_maestro.get(),
            self.entry_grado_doctor.get(),
            self.entry_titulo_profesional.get(),
            self.entry_titulo_esp_medico.get(),
            self.entry_titulo_esp_odonto.get(),
            self.entry_grado_bachiller.get()
        ]):
            self.create_button.config(state=tk.NORMAL)
        else:
            self.create_button.config(state=tk.DISABLED)

    def create_docente(self):
        nombres = self.entry_nombres.get()
        apellido_paterno = self.entry_apellido_paterno.get()
        apellido_materno = self.entry_apellido_materno.get()
        correo = self.entry_correo.get()
        dni = self.entry_dni.get()
        celular = self.entry_celular.get()
        grado_maestro = self.entry_grado_maestro.get()
        grado_doctor = self.entry_grado_doctor.get()
        titulo_profesional = self.entry_titulo_profesional.get()
        titulo_esp_medico = self.entry_titulo_esp_medico.get()
        titulo_esp_odonto = self.entry_titulo_esp_odonto.get()
        grado_bachiller = self.entry_grado_bachiller.get()

        if self.controller.buscar_docente_por_dni(dni):
            messagebox.showinfo("Advertencia", "El Docente ya está registrado")
        else:
            self.controller.create_docente(
                nombres, apellido_paterno, apellido_materno, correo, dni, celular,
                grado_maestro, grado_doctor, titulo_profesional, titulo_esp_medico,
                titulo_esp_odonto, grado_bachiller
            )
            self.update_docente_list()

    def update_docente(self):
        selected_item = self.docente_tree.selection()
        if selected_item:
            id_docente = self.docente_tree.item(selected_item)["values"][0]
            nombres = self.entry_nombres.get()
            apellido_paterno = self.entry_apellido_paterno.get()
            apellido_materno = self.entry_apellido_materno.get()
            correo = self.entry_correo.get()
            dni = self.entry_dni.get()
            celular = self.entry_celular.get()
            grado_maestro = self.entry_grado_maestro.get()
            grado_doctor = self.entry_grado_doctor.get()
            titulo_profesional = self.entry_titulo_profesional.get()
            titulo_esp_medico = self.entry_titulo_esp_medico.get()
            titulo_esp_odonto = self.entry_titulo_esp_odonto.get()
            grado_bachiller = self.entry_grado_bachiller.get()
            self.controller.update_docente(
                id_docente, nombres, apellido_paterno, apellido_materno, correo, dni,
                celular, grado_maestro, grado_doctor, titulo_profesional, titulo_esp_medico,
                titulo_esp_odonto, grado_bachiller
            )
            self.update_docente_list()

    def delete_docente(self):
        selected_item = self.docente_tree.selection()
        if selected_item:
            id_docente = self.docente_tree.item(selected_item)["values"][0]
            self.controller.delete_docente(id_docente)
            self.update_docente_list()

    def update_docente_list(self):
        # Clear previous entries
        for item in self.docente_tree.get_children():
            self.docente_tree.delete(item)

        # Fetch updated docentes from controller
        docentes = self.controller.list_all_docente()
        for docente in docentes:
            self.docente_tree.insert("", "end", values=docente)
