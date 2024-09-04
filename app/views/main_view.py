import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
from app.views.general_options_view import GeneralOptionsView

class MainView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("EVALUACIÓN DOCENTE -DGAC")
        
        # Asignar el icono mediante la función estática
        GeneralOptionsView.icono_ventana(self)

        GeneralOptionsView.views_headers(self)

        # Llamando funcion crear_boton
        self.gestion_img = GeneralOptionsView.crear_boton("database-table.png", 50)
        self.administrar_img = GeneralOptionsView.crear_boton("filter.png", 50)
        self.extraerPlan_img = GeneralOptionsView.crear_boton("excel.png", 50)
        self.reportes_img = GeneralOptionsView.crear_boton("report.png", 50)

        # Crear los botones con los iconos
        self.gestion_button = tk.Button(self, text="Gestionar Tablas", image=self.gestion_img, compound=tk.TOP, command=self.controller.open_gestion_view)
        self.administrar_button = tk.Button(self, text="Extraer Datos del Sílabo", image=self.administrar_img, compound=tk.TOP, command=self.controller.open_administrar_view)
        self.extraerPlan_button = tk.Button(self, text="Extraer Datos del Plan de Trabajo", image=self.extraerPlan_img, compound=tk.TOP, command=self.controller.open_extraerPlan_view)
        self.reportes_button = tk.Button(self, text="Generar Reportes", image=self.reportes_img, compound=tk.TOP, command=self.controller.open_reportes_view)

        # Configuración del tamaño fijo para los botones
        button_width = 20
        button_height = 10

        self.gestion_button.config(width=button_width, height=button_height)
        self.administrar_button.config(width=button_width, height=button_height)
        self.extraerPlan_button.config(width=button_width, height=button_height)
        self.reportes_button.config(width=button_width, height=button_height)

        # Colocando los botones en una cuadrícula de 2x2
        self.gestion_button.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.administrar_button.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        self.extraerPlan_button.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        self.reportes_button.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

        # Configuración de las columnas y filas para que tengan el mismo tamaño
        self.grid_columnconfigure(0, weight=1, uniform="button")
        self.grid_columnconfigure(1, weight=1, uniform="button")
        self.grid_rowconfigure(1, weight=1, uniform="button")
        self.grid_rowconfigure(2, weight=1, uniform="button")

if __name__ == "__main__":
    main_view = MainView(None)
    main_view.mainloop()