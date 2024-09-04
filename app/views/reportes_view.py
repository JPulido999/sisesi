import tkinter as tk
from app.views.general_options_view import GeneralOptionsView

class ReportesView(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Buscar Registros del Docente")

        # Asignar el icono mediante la función estática
        GeneralOptionsView.icono_ventana(self)

        # Llamando función crear_boton
        self.informacion_img = GeneralOptionsView.crear_boton("info.png", 50)
        self.actividades_img = GeneralOptionsView.crear_boton("checklist.png", 50)
        self.contrato_img = GeneralOptionsView.crear_boton("contrato.png", 50)
        self.licencia_img = GeneralOptionsView.crear_boton("licencia.png", 50)

        self.docente_button = tk.Button(
            self, text="Información personal", image=self.informacion_img, compound=tk.TOP, command=self.controller.open_reporteDocente_view)

        self.accion_button = tk.Button(
            self, text="Actividades", image=self.actividades_img, compound=tk.TOP, command=self.controller.open_reporteAccion_view)

        self.contrato_button = tk.Button(
            self, text="Contrato", image=self.contrato_img, compound=tk.TOP, command=self.controller.open_reporteContrato_view)

        self.licencia_button = tk.Button(
            self, text="Licencia", image=self.licencia_img, compound=tk.TOP, command=self.controller.open_reporteLicencia_view)

        # Configuración del tamaño fijo para los botones
        button_width = 20
        button_height = 10

        self.docente_button.config(width=button_width, height=button_height)
        self.accion_button.config(width=button_width, height=button_height)
        self.contrato_button.config(width=button_width, height=button_height)
        self.licencia_button.config(width=button_width, height=button_height)

        # Colocando los botones en una cuadrícula de 2x2
        self.docente_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.accion_button.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        self.contrato_button.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.licencia_button.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        # Configuración de las columnas y filas para que tengan el mismo tamaño
        self.grid_columnconfigure(0, weight=1, uniform="button")
        self.grid_columnconfigure(1, weight=1, uniform="button")
        self.grid_rowconfigure(0, weight=1, uniform="button")
        self.grid_rowconfigure(1, weight=1, uniform="button")

        self.geometry("400x400")
