import tkinter as tk
from PIL import Image, ImageTk
import os      
    
class GeneralOptionsView():

    @staticmethod
    def crear_boton(nombre, tamano):
        # Obtener la ruta del directorio de imágenes
        image_dir = os.path.join("app", "resources", "images")

        # Construir la ruta completa a la imagen del botón
        boton_icon_path = os.path.join(image_dir, nombre)

        # Cargar la imagen
        boton_icon = Image.open(boton_icon_path)

        # Redimensionar la imagen según sea necesario
        boton_icon = boton_icon.resize((tamano,tamano))

        # Convertir la imagen en un formato compatible con tkinter
        boton_img = ImageTk.PhotoImage(boton_icon)

        return boton_img
    
    @staticmethod
    def views_headers(window_instance):
        # Calcular el ancho y el alto de la ventana
        window_width = 400
        window_height = 500
        
        # Obtener las dimensiones de la pantalla
        screen_width = window_instance.winfo_screenwidth()
        screen_height = window_instance.winfo_screenheight()
        
        # Calcular las coordenadas para centrar la ventana
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        
        # Establecer la geometría de la ventana para que aparezca en el centro
        window_instance.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Cabecera con imagen
        image_path = "C:\\Users\\Admin\\Desktop\\SISESI\\app\\resources\\images\\logodga.jpg"
        header_image = Image.open(image_path)
        header_image = header_image.resize((403, 80), Image.LANCZOS)
        header_photo = ImageTk.PhotoImage(header_image)
        header_label = tk.Label(window_instance, image=header_photo)
        header_label.image = header_photo  # Mantener una referencia a la imagen
        header_label.grid(row=0, column=0, columnspan=3, pady=10)

        # Ajustar la geometría de la ventana
        window_instance.geometry(f"{window_width}x{window_height}")