import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from datetime import datetime
import openpyxl
from views.general_options_view import GeneralOptionsView

class ReporteDocenteView(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Consultar Docentes")
        self.state('zoomed')

        # Frame para la búsqueda
        self.search_frame = ttk.Frame(self)
        self.search_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

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
        self.search_button = ttk.Button(self.search_frame, text="Buscar", image=self.search_img,compound=tk.TOP, command=self.search_docente)
        self.search_button.grid(row=0, column=2, rowspan=2, padx=5, pady=5)

        # Botón para exportar a Excel
        self.export_button = ttk.Button(self.search_frame, text="Exportar", image=self.export_img,compound=tk.TOP, command=self.export_to_excel)
        self.export_button.grid(row=0, column=20, rowspan=2, padx=5, pady=5)

        # Frame para la tabla
        self.tree_frame = ttk.Frame(self)
        self.tree_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.tree_scroll = ttk.Scrollbar(self.tree_frame, orient=tk.VERTICAL)
        self.tree_scroll.grid(row=0, column=1, sticky="ns")

        self.docente_tree = ttk.Treeview(
            self.tree_frame,
            columns=("ID", "Nombres", "Apellido Paterno", "Apellido Materno", "Correo", "DNI", "Celular", "Grado Maestro", "Grado Doctor", "Título Profesional", "Título Esp Médico", "Título Esp Odonto", "Grado Bachiller"),
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
        self.docente_tree.heading("Título Esp Médico", text="Título Esp Médico")
        self.docente_tree.heading("Título Esp Odonto", text="Título Esp Odonto")
        self.docente_tree.heading("Grado Bachiller", text="Grado Bachiller")

        self.docente_tree.grid(row=0, column=0, sticky="nsew")

        # Ajustar tamaño de las columnas
        self.docente_tree.column("ID", width=50)
        self.docente_tree.column("Nombres", width=150)
        self.docente_tree.column("Apellido Paterno", width=100)
        self.docente_tree.column("Apellido Materno", width=100)
        self.docente_tree.column("Correo", width=200)
        self.docente_tree.column("DNI", width=80)
        self.docente_tree.column("Celular", width=100)
        self.docente_tree.column("Grado Maestro", width=150)
        self.docente_tree.column("Grado Doctor", width=150)
        self.docente_tree.column("Título Profesional", width=150)
        self.docente_tree.column("Título Esp Médico", width=150)
        self.docente_tree.column("Título Esp Odonto", width=150)
        self.docente_tree.column("Grado Bachiller", width=150)

        # Actualizar lista de docentes al iniciar la ventana
        self.update_docente_list()

    def update_docente_list(self):
        # Limpiar entradas previas
        for item in self.docente_tree.get_children():
            self.docente_tree.delete(item)

        # Obtener las docentes actualizados desde el controlador
        docentes = self.controller.list_all_consulta_docente("", "")
        for docente in docentes:
            self.docente_tree.insert("", "end", values=docente)

    def search_docente(self):
        nombreDocente = self.search_entry_nombre.get().strip().lower()
        dniDocente = self.search_entry_dni.get().strip().lower()

        print(f"Buscando por nombre: {nombreDocente}, DNI: {dniDocente}")

        # Limpiar entradas previas
        for item in self.docente_tree.get_children():
            self.docente_tree.delete(item)

        # Obtener docentes que coincidan con los términos de búsqueda
        docentes = self.controller.list_all_consulta_docente(nombreDocente, dniDocente)
        for docente in docentes:
            self.docente_tree.insert("", "end", values=docente)

    def export_to_excel(self):
        # Crear un nuevo libro de trabajo de Excel
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = "Docentes"

        # Agregar encabezados de columna con formato
        headers = ["ID", "Nombres", "Apellido Paterno", "Apellido Materno", "Correo", "DNI", "Celular", "Grado Maestro", "Grado Doctor", "Título Profesional", "Título Esp Médico", "Título Esp Odonto", "Grado Bachiller"]
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
        for child in self.docente_tree.get_children():
            values = [self.docente_tree.item(child)["values"][0],  # ID
                      self.docente_tree.item(child)["values"][1],  # Nombres
                      self.docente_tree.item(child)["values"][2],  # Apellido Paterno
                      self.docente_tree.item(child)["values"][3],  # Apellido Materno
                      self.docente_tree.item(child)["values"][4],  # Correo
                      self.docente_tree.item(child)["values"][5],  # DNI
                      self.docente_tree.item(child)["values"][6],  # Celular
                      self.docente_tree.item(child)["values"][7],  # Grado Maestro
                      self.docente_tree.item(child)["values"][8],  # Grado Doctor
                      self.docente_tree.item(child)["values"][9],  # Título Profesional
                      self.docente_tree.item(child)["values"][10],  # Título Esp Médico
                      self.docente_tree.item(child)["values"][11],  # Título Esp Odonto
                      self.docente_tree.item(child)["values"][12]]  # Grado Bachiller
            sheet.append(values)

        # Pedir al usuario que seleccione la carpeta para guardar el archivo
        filename = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")],
                                               initialfile="reporte_docentes.xlsx", title="Guardar como...")
        if filename:
            workbook.save(filename)
            messagebox.showinfo("Exportar a Excel", f"Los datos se han exportado correctamente a:\n{filename}")