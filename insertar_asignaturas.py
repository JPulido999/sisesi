import pandas as pd
import sqlite3
import os

# Conexión a la base de datos SQLite
conn = sqlite3.connect('sisesi.db')
cursor = conn.cursor()

# Ruta al directorio que contiene los archivos Excel
ruta_directorio = 'C:\\Users\\Admin\\Downloads\\RECURSOS SIIGE\\ASIGNATURAS'

# Recorre todos los archivos Excel en el directorio
for archivo in os.listdir(ruta_directorio):
    if archivo.endswith('.xlsx') or archivo.endswith('.xls'):
        # Cargar el archivo Excel
        archivo_excel = pd.ExcelFile(os.path.join(ruta_directorio, archivo))
        
        # Recorre todas las hojas en el archivo Excel
        for hoja in archivo_excel.sheet_names:
            # Leer la hoja en un DataFrame
            df = archivo_excel.parse(hoja)
            
            # Suponiendo que el DataFrame tiene columnas 'nombre_asignatura', 'codigo_asignatura', etc.
            for index, row in df.iterrows():
                codigo = row['Código']
                ciclo = row['Ciclo']                
                nombre = row['Nombre']
                plan_estudio_nombre = row['Plan de Estudios']
                
                # Buscar el id del plan de estudios por su nombre
                cursor.execute('''
                    SELECT id_plan FROM Plan_Estudios WHERE denominacion_plan = ?
                ''', (plan_estudio_nombre,))
                resultado = cursor.fetchone()
                
                if resultado:
                    id_plan = resultado[0]
                    
                    # Inserta los datos en la base de datos
                    cursor.execute('''
                        INSERT INTO Asignatura (nombre_asignatura, sigla_asignatura, id_plan)
                        VALUES (?, ?, ?)
                    ''', (nombre, codigo, id_plan))
                else:
                    print(f"Plan de estudios '{plan_estudio_nombre}' no encontrado para la asignatura '{nombre}'.")

# Guardar (commit) los cambios en la base de datos
conn.commit()

# Cerrar la conexión
conn.close()
