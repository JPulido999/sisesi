import tkinter as tk
from PIL import Image, ImageTk
import os
from app.views.general_options_view import GeneralOptionsView

class MainView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("EVALUACIÓN DOCENTE -DGAC")
        self.iconbitmap("C:\\Users\\Admin\\Desktop\\SISESI\\app\\resources\\images\\logo-unsch.ico")

        self.geometry("400x300")

        # Calcular el ancho y el alto de la ventana
        window_width = 400
        window_height = 300
        
        # Obtener las dimensiones de la pantalla
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        # Calcular las coordenadas para centrar la ventana
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        
        # Establecer la geometría de la ventana para que aparezca en el centro
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
        # Llamando funcion crear_boton
        self.gestion_img = GeneralOptionsView.crear_boton("table.png", 50)
        self.administrar_img = GeneralOptionsView.crear_boton("filter.png", 50)
        self.extraerPlan_img = GeneralOptionsView.crear_boton("excel.png", 50)

        # Crear los botones con los iconos
        self.gestion_button = tk.Button(self, text="Gestionar Tablas", image=self.gestion_img, compound=tk.TOP, command=self.controller.open_gestion_view)
        self.gestion_button.pack(pady=10)

        self.administrar_button = tk.Button(self, text="Extraer Datos del sílabo", image=self.administrar_img, compound=tk.TOP, command=self.controller.open_administrar_view)
        self.administrar_button.pack(pady=10)

        self.extraerPlan_button = tk.Button(self, text="Extraer Datos del Plan de Trabajo", image=self.extraerPlan_img, compound=tk.TOP, command=self.controller.open_extraerPlan_view)
        self.extraerPlan_button.pack(pady=10)

if __name__ == "__main__":
    main_view = MainView(None)
    main_view.mainloop()
