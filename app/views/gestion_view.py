import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
from app.views.general_options_view import GeneralOptionsView

class GestionView(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Gestión de Tablas")
        
        # Asignar el icono mediante la función estática
        GeneralOptionsView.icono_ventana(self)

        GeneralOptionsView.views_headers(self)

        # Llamando funcion crear_boton
        self.facultad_img = GeneralOptionsView.crear_boton("table.png", 50)
        self.escuela_img = GeneralOptionsView.crear_boton("table.png", 50)
        self.docente_img = GeneralOptionsView.crear_boton("table.png", 50)
        self.contrato_img = GeneralOptionsView.crear_boton("table.png", 50)
        self.accion_img = GeneralOptionsView.crear_boton("table.png", 50)
        self.licencia_img = GeneralOptionsView.crear_boton("table.png", 50)

        # Botones de gestión
        self.facultad_button = tk.Button(self, text="Gestionar Facultad",image=self.facultad_img, compound=tk.TOP, command=self.controller.open_facultad_view)
        self.escuela_button = tk.Button(self, text="Gestionar Escuela",image=self.escuela_img, compound=tk.TOP, command=self.controller.open_escuela_view)
        self.docente_button = tk.Button(self, text="Gestionar Docente",image=self.docente_img, compound=tk.TOP, command=self.controller.open_docente_view)
        self.contrato_button = tk.Button(self, text="Gestionar Contrato",image=self.contrato_img, compound=tk.TOP, command=self.controller.open_contrato_view)
        self.accion_button = tk.Button(self, text="Gestionar Accion",image=self.accion_img, compound=tk.TOP, command=self.controller.open_accion_view)
        self.licencia_button = tk.Button(self, text="Gestionar Licencia",image=self.licencia_img, compound=tk.TOP, command=self.controller.open_licencia_view)

        # Colocar los botones en una cuadrícula de 3x3
        buttons = [
            self.facultad_button,
            self.escuela_button,
            self.docente_button,
            self.contrato_button,
            self.accion_button,
            self.licencia_button
        ]

        row = 1
        col = 0
        for button in buttons:
            button.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
            col += 1
            if col == 3:
                col = 0
                row += 1

        # Configuración de las columnas y filas para que tengan el mismo tamaño
        for i in range(3):
            self.grid_columnconfigure(i, weight=1, uniform="button")
        for i in range(row+1):
            self.grid_rowconfigure(i, weight=1, uniform="button")
