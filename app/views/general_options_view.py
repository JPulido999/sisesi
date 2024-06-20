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