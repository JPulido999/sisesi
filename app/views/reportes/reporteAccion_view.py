import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from datetime import datetime
import openpyxl
from app.views.general_options_view import GeneralOptionsView

class ReporteAccionView(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Consultar Acciones")
        self.state('zoomed')

        # Frame para la búsqueda
        self.search_frame = ttk.Frame(self)
        self.search_frame.pack(padx=10, pady=10, fill=tk.X)

        # Etiqueta y entrada para buscar por nombre del docente
        ttk.Label(self.search_frame, text="Nombre del Docente:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.search_entry_nombre = ttk.Entry(self.search_frame)
        self.search_entry_nombre.grid(row=0, column=1, padx=5, pady=5)

        # Etiqueta y entrada para buscar por DNI del docente
        ttk.Label(self.search_frame, text="DNI del Docente:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.search_entry_dni = ttk.Entry(self.search_frame)
        self.search_entry_dni.grid(row=1, column=1, padx=5, pady=5)

        self.search_img=GeneralOptionsView.crear_boton("search.png", 20)
        self.export_img=GeneralOptionsView.crear_boton("excel.png", 20)
    
        # Botón de búsqueda
        self.search_button = ttk.Button(self.search_frame, text="Buscar", image=self.search_img,compound=tk.TOP, command=self.search_accion)
        self.search_button.grid(row=0, column=2, rowspan=2, padx=5, pady=5)

        # Botón para exportar a Excel
        self.export_button = ttk.Button(self.search_frame, text="Exportar", image=self.export_img,compound=tk.TOP, command=self.export_to_excel)
        self.export_button.grid(row=0, column=20, rowspan=2, padx=5, pady=5)

        # Frame para la tabla
        self.tree_frame = ttk.Frame(self)
        self.tree_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.tree_scroll = ttk.Scrollbar(self.tree_frame, orient=tk.VERTICAL)
        self.tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.accion_tree = ttk.Treeview(
            self.tree_frame,
            columns=("Docente", "Día", "H. Inicio", "H. Fin", "Ambiente", "N° Alumnos", "Semana",
                     "Contenido", "Unidad", "Asignatura", "Sigla", "Semestre", "Plan", "Escuela"),
            show="headings",
            yscrollcommand=self.tree_scroll.set 
        )
        self.tree_scroll.config(command=self.accion_tree.yview)

        self.accion_tree.heading("Docente", text="Docente")
        self.accion_tree.heading("Día", text="Día")
        self.accion_tree.heading("H. Inicio", text="H. Inicio")
        self.accion_tree.heading("H. Fin", text="H. Fin")
        self.accion_tree.heading("Ambiente", text="Ambiente")
        self.accion_tree.heading("N° Alumnos", text="N° Alumnos")
        self.accion_tree.heading("Semana", text="Semana")
        self.accion_tree.heading("Contenido", text="Contenido")
        self.accion_tree.heading("Unidad", text="Unidad")
        self.accion_tree.heading("Asignatura", text="Asignatura")
        self.accion_tree.heading("Sigla", text="Sigla")
        self.accion_tree.heading("Semestre", text="Semestre")
        self.accion_tree.heading("Plan", text="Plan")
        self.accion_tree.heading("Escuela", text="Escuela")

        self.accion_tree.pack(fill=tk.BOTH, expand=True)

        # Ajustar tamaño de las columnas
        self.accion_tree.column("Docente", width=180)
        self.accion_tree.column("Día", width=90)
        self.accion_tree.column("H. Inicio", width=50)
        self.accion_tree.column("H. Fin", width=50)
        self.accion_tree.column("Ambiente", width=50)
        self.accion_tree.column("N° Alumnos", width=50)
        self.accion_tree.column("Semana", width=70)
        self.accion_tree.column("Contenido", width=200)
        self.accion_tree.column("Unidad", width=50)
        self.accion_tree.column("Asignatura", width=110)
        self.accion_tree.column("Sigla", width=50)
        self.accion_tree.column("Semestre", width=50)
        self.accion_tree.column("Plan", width=80)
        self.accion_tree.column("Escuela", width=100)

        # Actualizar lista de acciones al iniciar la ventana
        self.update_accion_list()

    def update_accion_list(self):
        # Limpiar entradas previas
        for item in self.accion_tree.get_children():
            self.accion_tree.delete(item)

        # Obtener las acciones actualizadas desde el controlador
        acciones = self.controller.list_all_consulta_accion("", "")
        for accion in acciones:
            self.accion_tree.insert("", "end", values=accion)

    def search_accion(self):
        nombreDocente = self.search_entry_nombre.get().strip().lower()
        dniDocente = self.search_entry_dni.get().strip().lower()

        print(f"Buscando por nombre: {nombreDocente}, DNI: {dniDocente}")

        # Limpiar entradas previas
        for item in self.accion_tree.get_children():
            self.accion_tree.delete(item)

        # Obtener acciones que coincidan con los términos de búsqueda
        acciones = self.controller.list_all_consulta_accion(nombreDocente, dniDocente)
        for accion in acciones:
            self.accion_tree.insert("", "end", values=accion)

    def export_to_excel(self):
        # Crear un nuevo libro de trabajo de Excel
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = "Acciones"

        # Agregar encabezados de columna con formato
        headers = ["Docente", "Día", "H. Inicio", "H. Fin", "Ambiente", "N° Alumnos", "Semana",
                   "Contenido", "Unidad", "Asignatura", "Sigla", "Semestre", "Plan", "Escuela"]
        sheet.append(headers)
        for col in sheet.columns:
            max_length = 0
            column = col[0].column_letter
            for cell in col:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(cell.value)
                except:
                    pass
            adjusted_width = (max_length + 2) * 1.2
            sheet.column_dimensions[column].width = adjusted_width

        # Obtener datos del Treeview y añadir a la hoja
        for child in self.accion_tree.get_children():
            values = [self.accion_tree.item(child)["values"][0],  # Docente
                      self.accion_tree.item(child)["values"][1],  # Día
                      self.accion_tree.item(child)["values"][2],  # H. Inicio
                      self.accion_tree.item(child)["values"][3],  # H. Fin
                      self.accion_tree.item(child)["values"][4],  # Ambiente
                      self.accion_tree.item(child)["values"][5],  # N° Alumnos
                      self.accion_tree.item(child)["values"][6],  # Semana
                      self.accion_tree.item(child)["values"][7],  # Contenido
                      self.accion_tree.item(child)["values"][8],  # Unidad
                      self.accion_tree.item(child)["values"][9],  # Asignatura
                      self.accion_tree.item(child)["values"][10],  # Sigla
                      self.accion_tree.item(child)["values"][11],  # Semestre
                      self.accion_tree.item(child)["values"][12],  # Plan
                      self.accion_tree.item(child)["values"][13]]  # Escuela
            sheet.append(values)

        # Pedir al usuario que seleccione la carpeta para guardar el archivo
        filename = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")],
                                               initialfile="reporte_acciones.xlsx", title="Guardar como...")
        if filename:
            workbook.save(filename)
            messagebox.showinfo("Exportar a Excel", f"Los datos se han exportado correctamente a:\n{filename}")