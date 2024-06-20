import logging
import sqlite3


def create_connection():
    conn = sqlite3.connect('sisesi.db')
    return conn


def create_tables():
    try:
        conn = create_connection()
        cursor = conn.cursor()

        # Crear la tabla Accion
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Accion (
                id_accion INTEGER PRIMARY KEY,
                dia_accion VARCHAR(50),
                horaInicio_accion VARCHAR(50),
                horaFin_accion VARCHAR(50),
                ambiente_accion VARCHAR(50),
                numAlumnos_accion INTEGER,
                id_tipoActividad INTEGER,
                id_semana INTEGER,
                id_docente INTEGER,
                FOREIGN KEY (id_tipoActividad) REFERENCES Tipo_Actividad(id_tipoActividad),
                FOREIGN KEY (id_semana) REFERENCES Semana(id_semana),
                FOREIGN KEY (id_docente) REFERENCES Docente(id_docente)
            )
        ''')

        # Crear la tabla Categoria_Actividad
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Categoria_Actividad (
                id_categoriaActividad INTEGER PRIMARY KEY,
                nombre_categoriaActividad VARCHAR(50)
            )
        ''')

        # Crear la tabla Actividad
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Actividad (
                id_actividad INTEGER PRIMARY KEY,
                nombre_actividad VARCHAR(50),
                id_categoriaActividad INTEGER,
                FOREIGN KEY (id_categoriaActividad) REFERENCES Categoria_Actividad(id_categoriaActividad)
            )
        ''')

        # Crear la tabla Asignatura
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Asignatura (
                id_asignatura INTEGER PRIMARY KEY,
                nombre_asignatura VARCHAR(50),
                sigla_asignatura VARCHAR(10),
                creditos_asignatura INTEGER,
                horasTs_asignatura INTEGER,
                horasPs_asignatura INTEGER,
                horasLs_asignatura INTEGER,
                id_plan INTEGER,
                id_departamento INTEGER,
                FOREIGN KEY (id_plan) REFERENCES Plan_Estudios(id_plan),
                FOREIGN KEY (id_departamento) REFERENCES Departamento_Academico(id_departamento)
            )
        ''')

        # Crear la tabla Categoria
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Categoria (
                id_categoria INTEGER PRIMARY KEY,
                nombre_categoria VARCHAR(50)
            )
        ''')

        # Crear la tabla Condicion
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Condicion (
                id_condicion INTEGER PRIMARY KEY,
                nombre_condicion VARCHAR(50)
            )
        ''')

        # Crear la tabla Contrato
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Contrato (
                id_contrato INTEGER PRIMARY KEY,
                periodoInicio_contrato DATETIME,
                periodoFin_contrato DATETIME,
                id_docente INTEGER,
                renacyt_contrato CHAR(18),
                id_condicion INTEGER,
                id_regimen INTEGER,
                id_categoria INTEGER,
                FOREIGN KEY (id_docente) REFERENCES Docente(id_docente),
                FOREIGN KEY (id_condicion) REFERENCES Condicion(id_condicion),
                FOREIGN KEY (id_regimen) REFERENCES Regimen(id_regimen),
                FOREIGN KEY (id_categoria) REFERENCES Categoria(id_categoria)
            )
        ''')

        # Crear la tabla Departamento_Academico
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Departamento_Academico (
                id_departamento INTEGER PRIMARY KEY,
                nombre_departamento VARCHAR(50)
            )
        ''')

        # Crear la tabla Docente
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Docente (
                id_docente INTEGER PRIMARY KEY,
                nombres_docente VARCHAR(50),
                apellidoPaterno_docente VARCHAR(50),
                apellidoMaterno_docente VARCHAR(50),
                correo_docente VARCHAR(50),
                dni_docente VARCHAR(10),
                celular_docente VARCHAR(15),
                gradoMaestro_docente VARCHAR(50),
                gradoDoctor_docente VARCHAR(50),
                tituloProfesional_docente VARCHAR(50),
                tituloEspMedico_docente VARCHAR(50),
                tituloEspOdonto_docente VARCHAR(50),
                gradoBachiller_docente VARCHAR(50)
            )
        ''')

        # Crear la tabla Escuela
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Escuela (
                id_escuela INTEGER PRIMARY KEY,
                nombre_escuela VARCHAR(50),
                id_facultad INTEGER,
                FOREIGN KEY (id_facultad) REFERENCES Facultad(id_facultad)
            )
        ''')

        # Crear la tabla Facultad
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Facultad (
                id_facultad INTEGER PRIMARY KEY,
                sigla_facultad VARCHAR(10),
                nombre_facultad VARCHAR(50)
            )
        ''')

        # Crear la tabla Licencia
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Licencia (
                id_licencia INTEGER PRIMARY KEY,
                resolucion_licencia VARCHAR(50) NULL,
                fechaInicio_licencia DATE NULL,
                fechaFin_licencia DATE NULL,
                observacion_licencia TEXT NULL,
                id_tipoLicencia INTEGER NULL,
                id_docente INTEGER NOT NULL,
                FOREIGN KEY (id_docente) REFERENCES Docente(id_docente),
                FOREIGN KEY (id_tipoLicencia) REFERENCES Tipo_Licencia(id_tipoLicencia)
            )
            ''')
        
        # Crear la tabla Plan_Estudios
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Plan_Estudios (
                id_plan INTEGER PRIMARY KEY,
                nombre_plan VARCHAR(50),
                id_escuela INTEGER,
                FOREIGN KEY (id_escuela) REFERENCES Escuela(id_escuela)
            )
        ''')

        # Crear la tabla Regimen
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Regimen (
                id_regimen INTEGER PRIMARY KEY,
                nombre_regimen VARCHAR(50)
            )
        ''')

        # Crear la tabla Semana
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Semana (
                id_semana INTEGER PRIMARY KEY,
                nombre_semana VARCHAR(50),
                contenido_semana TEXT,
                id_unidad INTEGER,
                FOREIGN KEY (id_unidad) REFERENCES Unidad(id_unidad)
            )
        ''')

        # Crear la tabla Semestre
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Semestre (
                id_semestre INTEGER PRIMARY KEY,
                nombre_semestre VARCHAR(50),
                duracion_semestre VARCHAR(50),
                fechaInicio_semestre DATE,
                fechaFin_semestre DATE,
                estado_semestre VARCHAR(50)
            )
        ''')

        # Crear la tabla Silabo
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Silabo (
                id_sil INTEGER PRIMARY KEY,
                id_asignatura INTEGER,
                id_semestre INTEGER,
                rutaArchivo_sil VARCHAR(50),
                FOREIGN KEY (id_asignatura) REFERENCES Asignatura(id_asignatura),
                FOREIGN KEY (id_semestre) REFERENCES Semestre(id_semestre)
            )
        ''')

        # Crear la tabla Tipo_Actividad
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Tipo_Actividad (
                id_tipoActividad INTEGER PRIMARY KEY,
                nombre_tipoActividad VARCHAR(50),
                sigla_tipoActividad VARCHAR(10),
                id_actividad INTEGER,
                FOREIGN KEY (id_actividad) REFERENCES Actividad(id_actividad)
            )
        ''')

        # Crear la tabla Tipo_Licencia
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Tipo_Licencia (
                id_tipoLicencia INTEGER PRIMARY KEY,
                nombre_tipoLicencia VARCHAR(50) NULL
            )
            ''')

        # Crear la tabla Unidad
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Unidad (
                id_unidad INTEGER PRIMARY KEY,
                numero_unidad VARCHAR(50),
                id_sil INTEGER,
                FOREIGN KEY (id_sil) REFERENCES Silabo(id_sil)
            )
        ''')

        # Llamada a la función para insertar datos básicos
        insert_basic_data(cursor)

        conn.commit()
    except sqlite3.Error as e:
        logging.error(f"Error al crear las tablas: {e}")
    finally:
        conn.close()


# INSERCIONES ###########################################################3
def insert_basic_data(cursor):
    # Inserciones básicas: Datos de las facultades y escuelas
    facultades_escuelas = [
        ("Ciencias Agrarias", "C. Agrarias", "Agronomía"),
        ("Ciencias Agrarias", "C. Agrarias", "Ingeniería Agrícola"),
        ("Ciencias Agrarias", "C. Agrarias", "Ingeniería Agroforestal"),
        ("Ciencias Agrarias", "C. Agrarias", "Medicina Veterinaria"),
        ("Ciencias Biológicas", "C. Biológicas", "Biología"),
        ("Ciencias de la Educación", "C. de la Educación", "Educación Física"),
        ("Ciencias de la Educación", "C. de la Educación", "Educación Inicial"),
        ("Ciencias de la Educación", "C. de la Educación", "Educación Primaria"),
        ("Ciencias de la Educación", "C. de la Educación", "Educación Secundaria"),
        ("Ciencias de la Salud", "C. de la Salud", "Enfermería"),
        ("Ciencias de la Salud", "C. de la Salud", "Farmacia y Bioquímica"),
        ("Ciencias de la Salud", "C. de la Salud", "Medicina Humana"),
        ("Ciencias de la Salud", "C. de la Salud", "Obstetricia"),
        ("Ciencias Económicas, Administrativas y Contables",
         "FACEAC", "Administración de Empresas"),
        ("Ciencias Económicas, Administrativas y Contables",
         "FACEAC", "Contabilidad y Auditoría"),
        ("Ciencias Económicas, Administrativas y Contables", "FACEAC", "Economía"),
        ("Ciencias Sociales", "C. Sociales", "Antropología Social"),
        ("Ciencias Sociales", "C. Sociales", "Arqueología e Historia"),
        ("Ciencias Sociales", "C. Sociales", "Ciencias de la Comunicación"),
        ("Ciencias Sociales", "C. Sociales", "Trabajo Social"),
        ("Derecho y Ciencias Políticas", "Derecho", "Derecho"),
        ("Ingeniería de Minas, Geología y Civil",
         "FIMGC", "Ciencias Físico-Matemáticas"),
        ("Ingeniería de Minas, Geología y Civil", "FIMGC", "Ingeniería Civil"),
        ("Ingeniería de Minas, Geología y Civil", "FIMGC", "Ingeniería de Minas"),
        ("Ingeniería de Minas, Geología y Civil",
         "FIMGC", "Ingeniería de Sistemas"),
        ("Ingeniería de Minas, Geología y Civil",
         "FIMGC", "Ingeniería Informática"),
        ("Ingeniería Química y Metalurgia", "FIQM", "Ingeniería Agroindustrial"),
        ("Ingeniería Química y Metalurgia", "FIQM",
         "Ingeniería en Industrias Alimentarias"),
        ("Ingeniería Química y Metalurgia", "FIQM", "Ingeniería Química")
    ]

    # Insertar datos en las tablas Facultad y Escuela
    for facultad, sigla, escuela in facultades_escuelas:
        # Verificar si la facultad ya existe
        cursor.execute(
            "SELECT id_facultad FROM Facultad WHERE nombre_facultad = ?", (facultad,))
        facultad_id = cursor.fetchone()
        if not facultad_id:
            # Si la facultad no existe, la insertamos
            cursor.execute(
                "INSERT INTO Facultad (nombre_facultad, sigla_facultad) VALUES (?, ?)", (facultad, sigla))
            facultad_id = cursor.lastrowid
        else:
            facultad_id = facultad_id[0]

        # Verificar si la escuela ya existe
        cursor.execute(
            "SELECT id_escuela FROM Escuela WHERE nombre_escuela = ?", (escuela,))
        escuela_id = cursor.fetchone()
        if not escuela_id:
            # Si la Escuela no existe, la insertamos
            cursor.execute(
                "INSERT INTO Escuela (nombre_escuela, id_facultad) VALUES (?, ?)", (escuela, facultad_id))
            escuela_id = cursor.lastrowid
        else:
            escuela_id = escuela_id[0]

    # Inserción de datos en la tabla Condicion
    condiciones = ["NOMBRADO", "CONTRATADO"]
    for condicion in condiciones:
        cursor.execute(
            "SELECT id_condicion FROM Condicion WHERE nombre_condicion = ?", (condicion,))
        condicion_id = cursor.fetchone()
        if not condicion_id:
            cursor.execute(
                "INSERT INTO Condicion (nombre_condicion) VALUES (?)", (condicion,))

    # Inserción de datos en la tabla Categoria
    categorias = ["Ordinario Principal", "Ordinario Asociado",
                  "Ordinario Auxiliar", "Extraordinario"]
    for categoria in categorias:
        cursor.execute(
            "SELECT id_categoria FROM Categoria WHERE nombre_categoria = ?", (categoria,))
        categoria_id = cursor.fetchone()
        if not categoria_id:
            cursor.execute(
                "INSERT INTO Categoria (nombre_categoria) VALUES (?)", (categoria,))

    # Inserción de datos en la tabla Regimen
    regimenes = ["Tiempo Completo", "Tiempo Parcial", "Dedicación Exclusiva",
                 "DC A1", "DC A2", "DC A3", "DC B1", "DC B2", "DC B3", "DC C1", "DC C2", "DC C3"]
    for regimen in regimenes:
        cursor.execute(
            "SELECT id_regimen FROM Regimen WHERE nombre_regimen = ?", (regimen,))
        regimen_id = cursor.fetchone()
        if not regimen_id:
            cursor.execute(
                "INSERT INTO Regimen (nombre_regimen) VALUES (?)", (regimen,))

    # Inserción de datos en la Departamento Académico
    departamentos = ["Agronomía y Zootecnia", "Ciencias Biológicas", "Educación y Ciencias Humanas", "Lenguas y Literatura", "Ciencias Económicas y Administrativas",
                     "Ciencias Histórico-Sociales", "Ciencias Jurídicas", "Enfermería", "Medicina Humana", "Obstetricia", "Ingeniería de Minas y Civil", "Matemática y Física", "Ingeniería Química"]
    for departamento in departamentos:
        cursor.execute(
            "SELECT id_departamento FROM Departamento_Academico WHERE nombre_departamento = ?", (departamento,))
        departamento_id = cursor.fetchone()
        if not departamento_id:
            cursor.execute(
                "INSERT INTO Departamento_Academico (nombre_departamento) VALUES (?)", (departamento,))

    # Inserción de datos en la Semestre
    semestres = ["2024-0", "2024-I", "2024-II"]
    for semestre in semestres:
        cursor.execute(
            "SELECT id_semestre FROM Semestre WHERE nombre_semestre = ?", (semestre,))
        semestre_id = cursor.fetchone()
        if not semestre_id:
            cursor.execute(
                "INSERT INTO Semestre (nombre_semestre) VALUES (?)", (semestre,))

    # Definir las categorías de actividades
    categorias_actividades = [
        ("Actividades Lectivas", [
            "Actividades de Docencia Lectiva",
            "Actividades de Investigación Lectiva"
        ]),
        ("Actividades No Lectivas", [
            "Actividades de Proyección Social",
            "Actividades de Investigación No Lectiva",
            "Actividades de Tutoría",
            "Actividades de Docencia No Lectiva",
            "Actividades de Gestión"
        ])
    ]

    # Insertar categorías de actividades en Categoria_Actividad y obtener los IDs
    categoria_actividad_ids = {}
    for nombre_categoria, actividades in categorias_actividades:
        cursor.execute(
            "SELECT id_categoriaActividad FROM Categoria_Actividad WHERE nombre_categoriaActividad = ?", (nombre_categoria,))
        categoria_actividad_id = cursor.fetchone()
        if not categoria_actividad_id:
            cursor.execute(
                "INSERT INTO Categoria_Actividad (nombre_categoriaActividad) VALUES (?)", (nombre_categoria,))
            categoria_actividad_id = cursor.lastrowid
        else:
            categoria_actividad_id = categoria_actividad_id[0]
        categoria_actividad_ids[nombre_categoria] = categoria_actividad_id

        # Insertar las actividades asociadas a esta categoría en la tabla Actividad
        for actividad in actividades:
            cursor.execute(
                "SELECT id_actividad FROM Actividad WHERE nombre_actividad = ?", (actividad,))
            actividad_id = cursor.fetchone()
            if not actividad_id:
                cursor.execute("INSERT INTO Actividad (nombre_actividad, id_categoriaActividad) VALUES (?, ?)", (
                    actividad, categoria_actividad_id))

    # Definir los tipos de actividades y asociarlos a las actividades específicas
    tipos_actividades = {
        "Actividades de Docencia Lectiva": [
            ("TP", "Teoría Presencial"),
            ("PP", "Práctica Presencial"),
            ("PLP", "Práctica Laboratorio Presencial"),
            ("PCL", "Práctica Clínica"),
            ("PEC", "Práctica en Comunidad"),
            ("TV", "Teoría Virtual"),
            ("PV", "Práctica Virtual")
        ],
        "Actividades de Investigación Lectiva": [
            ("LIN", "Labores de Investigación")
        ],
        "Actividades de Proyección Social": [
            ("SPS", "Sesión de Proyección Social"),
            ("APS", "Actividad de Proyección Social")
        ],
        "Actividades de Investigación No Lectiva": [
            ("SII", "Sesión de Instituto de Investigación")
        ],
        "Actividades de Tutoría": [
            ("AAA", "Atención a Alumnos")
        ],
        "Actividades de Docencia No Lectiva": [
            ("PCE", "Preparación de Clases y Evaluaciones")
        ],
        "Actividades de Gestión": [
            ("LAD", "Labores Administrativas"),
            ("SCU", "Sesión de Consejo Universitario"),
            ("SCF", "Sesión de Consejo de Facultad"),
            ("SDP", "Sesión de Departamento"),
            ("SEF", "Sesión de Escuela"),
            ("CP", "Comisiones Permanentes")
        ]
    }

    # Insertar los tipos de actividades en Tipo_Actividad y asociarlos a las actividades correspondientes
    for actividad, tipos in tipos_actividades.items():
        cursor.execute(
            "SELECT id_actividad FROM Actividad WHERE nombre_actividad = ?", (actividad,))
        actividad_id = cursor.fetchone()[0]

        for tipo in tipos:
            cursor.execute(
                "SELECT id_tipoActividad FROM Tipo_Actividad WHERE nombre_tipoActividad = ? AND sigla_tipoActividad = ?", (tipo[1], tipo[0]))
            tipo_id = cursor.fetchone()
            if not tipo_id:
                cursor.execute(
                    "INSERT INTO Tipo_Actividad (id_actividad, nombre_tipoActividad, sigla_tipoActividad) VALUES (?, ?, ?)", (actividad_id, tipo[1], tipo[0]))

    # Inserción de datos en la tabla Tipo_Licencia
    tipos_licencias = ["Año sabático", "Licencia por estudio"]
    for tipo_licencia in tipos_licencias:
        cursor.execute(
            "SELECT id_tipoLicencia FROM Tipo_Licencia WHERE nombre_tipoLicencia = ?", (tipo_licencia,))
        semestre_id = cursor.fetchone()
        if not semestre_id:
            cursor.execute(
                "INSERT INTO Tipo_Licencia (nombre_tipoLicencia) VALUES (?)", (tipo_licencia,))
            
    # Asegurarse de que los cambios se guarden en la base de datos
    cursor.connection.commit()


