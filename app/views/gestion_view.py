import tkinter as tk


class GestionView(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Gestión de Tablas")

        self.facultad_button = tk.Button(
            self, text="Gestionar Facultad", command=self.controller.open_facultad_view)
        self.facultad_button.pack()

        self.escuela_button = tk.Button(
            self, text="Gestionar Escuela", command=self.controller.open_escuela_view)
        self.escuela_button.pack()

        self.docente_button = tk.Button(
            self, text="Gestionar Docente", command=self.controller.open_docente_view)
        self.docente_button.pack()

        self.contrato_button = tk.Button(
            self, text="Gestionar Contrato", command=self.controller.open_contrato_view)
        self.contrato_button.pack()

        self.accion_button = tk.Button(
            self, text="Gestionar Accion", command=self.controller.open_accion_view)
        self.accion_button.pack()

        self.licencia_button = tk.Button(
            self, text="Gestionar Licencia", command=self.controller.open_licencia_view)
        self.licencia_button.pack()

        self.geometry("300x300")
