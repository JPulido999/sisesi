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
                horaInicio_accion TIME,
                horaFin_accion TIME,
                ambiente_accion VARCHAR(50),
                numAlumnos_accion INTEGER,
                id_tipoActividad INTEGER,
                id_asignatura INTEGER,
                id_docente INTEGER,
                FOREIGN KEY (id_tipoActividad) REFERENCES Tipo_Actividad(id_tipoActividad),
                FOREIGN KEY (id_asignatura) REFERENCES Asignatura(id_asignatura),
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
                ciclo_asignatura VARCHAR(10),
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
                periodoInicio_contrato DATE,
                periodoFin_contrato DATE,
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
                genero_docente VARCHAR(15),
                pais_docente VARCHAR(50),
                correo_docente VARCHAR(50),
                dni_docente VARCHAR(10),
                celular_docente VARCHAR(15),
                gradoBachiller_docente VARCHAR(70),
                tituloProfesional_docente VARCHAR(70),
                gradoMaestro_docente VARCHAR(70),
                gradoDoctor_docente VARCHAR(70),
                tituloEspMedico_docente VARCHAR(50)
            )
        ''')

        # Crear la tabla Escuela
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Escuela (
                id_escuela INTEGER PRIMARY KEY,
                nombre_escuela VARCHAR(50),
                codigo_escuela VARCHAR(5),
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
                denominacion_plan VARCHAR(50),
                resolucion_plan VARCHAR (50),
                fecha_plan DATE,
                enfoque_plan VARCHAR(50),
                observacion_plan TEXT,
                rutaArchivo_plan VARCHAR(100),
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

        # Crear la tabla Semestre
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Semestre (
                id_semestre INTEGER PRIMARY KEY,
                nombre_semestre VARCHAR(50),
                duracion_semestre VARCHAR(50),
                fechaInicio_semestre DATE,
                fechaFin_semestre DATE
            )
        ''')

        # Crear la tabla Silabo
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Silabo (
                id_sil INTEGER PRIMARY KEY,
                id_asignatura INTEGER,
                id_semestre INTEGER,
                rutaArchivo_sil VARCHAR(100),
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
        ("Ciencias Agrarias", "C. Agrarias", "Agronomía", "P01"),
        ("Ciencias Agrarias", "C. Agrarias", "Ingeniería Agrícola", "P28"),
        ("Ciencias Agrarias", "C. Agrarias", "Ingeniería Agroforestal", "P36"),
        ("Ciencias Agrarias", "C. Agrarias", "Medicina Veterinaria", "P31"),
        ("Ciencias Biológicas", "C. Biológicas", "Biología", ""),
        ("Ciencias Biológicas", "C. Biológicas", "Biología - Microbiología", "P02"),
        ("Ciencias Biológicas", "C. Biológicas", "Biología - Biotecnología", "P03"),
        ("Ciencias Biológicas", "C. Biológicas", "Biología - Ecología y Recursos Naturales", "P04"),
        ("Ciencias de la Educación", "C. de la Educación", "Educación Inicial", "P05"),
        ("Ciencias de la Educación", "C. de la Educación", "Educación Primaria", "P06"),
        ("Ciencias de la Educación", "C. de la Educación", "Educación Secundaria - Lengua Española y Literatura", "P07"),
        ("Ciencias de la Educación", "C. de la Educación", "Educación Secundaria - Inglés y Lengua Española", "P08"),
        ("Ciencias de la Educación", "C. de la Educación", "Educación Secundaria - Ciencias Sociales, Filosofía y Psicología", "P09"),
        ("Ciencias de la Educación", "C. de la Educación", "Educación Secundaria - Matemática, Física e Informática", "P10"),
        ("Ciencias de la Educación", "C. de la Educación", "Educación Física", ""),
        ("Ciencias de la Educación", "C. de la Educación", "Educación Física - Entrenamiento Deportivo", "P11"),
        ("Ciencias de la Educación", "C. de la Educación", "Educación Física - Gestión Deportiva", "P12"),
        ("Ciencias de la Educación", "C. de la Educación", "Educación Física - Promoción de la Salud Social", "P13"),
        ("Ciencias de la Salud", "C. de la Salud", "Enfermería", "P22"),
        ("Ciencias de la Salud", "C. de la Salud", "Farmacia y Bioquímica", "P27"),
        ("Ciencias de la Salud", "C. de la Salud", "Medicina Humana", "P37"),
        ("Ciencias de la Salud", "C. de la Salud", "Obstetricia", "P25"),
        ("Ciencias Económicas, Administrativas y Contables", "FACEAC", "Administración de Empresas", "P14"),
        ("Ciencias Económicas, Administrativas y Contables", "FACEAC", "Contabilidad y Auditoría", "P15"),
        ("Ciencias Económicas, Administrativas y Contables", "FACEAC", "Economía", "P16"),
        ("Ciencias Sociales", "C. Sociales", "Antropología Social", "P17"),
        ("Ciencias Sociales", "C. Sociales", "Arqueología e Historia", ""),
        ("Ciencias Sociales", "C. Sociales", "Arqueología e Historia - Arqueología", "P18"),
        ("Ciencias Sociales", "C. Sociales", "Arqueología e Historia - Historia", "P19"),
        ("Ciencias Sociales", "C. Sociales", "Ciencias de la Comunicación", "P30"),
        ("Ciencias Sociales", "C. Sociales", "Trabajo Social", "P20"),
        ("Derecho y Ciencias Políticas", "Derecho", "Derecho", "P21"),
        ("Ingeniería de Minas, Geología y Civil", "FIMGC", "Ciencias Físico-Matemáticas", ""),
        ("Ingeniería de Minas, Geología y Civil", "FIMGC", "Ciencias Físico-Matemáticas - Matemática", "P32"),
        ("Ingeniería de Minas, Geología y Civil", "FIMGC", "Ciencias Físico-Matemáticas - Física", "P33"),
        ("Ingeniería de Minas, Geología y Civil", "FIMGC", "Ciencias Físico-Matemáticas - Estadística", "P34"),
        ("Ingeniería de Minas, Geología y Civil", "FIMGC", "Ingeniería Civil", "P24"),
        ("Ingeniería de Minas, Geología y Civil", "FIMGC", "Ingeniería de Minas", "P23"),
        ("Ingeniería de Minas, Geología y Civil", "FIMGC", "Ingeniería de Sistemas", "P35"),
        ("Ingeniería de Minas, Geología y Civil", "FIMGC", "Ingeniería Informática", ""),
        ("Ingeniería Química y Metalurgia", "FIQM", "Ingeniería Agroindustrial", "P29"),
        ("Ingeniería Química y Metalurgia", "FIQM", "Ingeniería en Industrias Alimentarias", "P26"),
        ("Ingeniería Química y Metalurgia", "FIQM", "Ingeniería Química", "P38")
    ]

    # Insertar datos en las tablas Facultad y Escuela
    for facultad, sigla, escuela, codigo in facultades_escuelas:
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
                "INSERT INTO Escuela (nombre_escuela, codigo_escuela, id_facultad) VALUES (?, ?, ?)", (escuela, codigo, facultad_id))
            escuela_id = cursor.lastrowid
        else:
            escuela_id = escuela_id[0]

    # Inserciones básicas: Datos de las facultades y escuelas
    escuelas_planes = {
        "Agronomía": [
            ('2015-08-24', "Nº 401-2015-UNSCH-CU", "Currículo 2004 revisado - Agronomía", "Objetivos", 
            "No figura DEPART. ACADEMICO/ No figura HL (HP y HL están unidos en HP, además la suma de horas figura como 12, debe ser 13)/En el curso LE141, TH registra 4 debe ser 5 / Cursos de ACTIVIDADES CO CURRICULARES difieren en los cursos que no suman créditos. / En ÁREA ACADÉMICA DE HIDROLOGÍA agrega el curso SU556 Manejo de cuencas, en la Resolución no figura / (CURRÍCULO ENVIADO POR LA EPA NO ES EL ACTUALIZADO)","docs/planes/2004/01 Agronomía Currículo 2004 Revisado.pdf"),
            ('', "", "CURRÍCULO-2018 - Agronomía", "","","docs/planes/2018/PROGRAMA_P01_CURRÍCULO AGRONOMÍA.pdf") 
        ],
        "Ingeniería Agrícola": [
            ('2016-07-22', "455-2016-UNSCH-CU", "Currículo 2004 Revisado - Agrícola", "Objetivos", "Ninguna", "docs/planes/2004/21 Ingeniería Agrícola Currículo 2004 Revisado.pdf"),
            ('', "", "CURRÍCULO 2018 - Agrícola", "","","docs/planes/2018/PROGRAMA_P28_CURRÍCULO INGENIERÍA AGRÍCOLA.pdf")
        ],
        "Ingeniería Agroforestal": [
            ('2015-08-24', "Nº 402-2015-UNSCH-CU", "Currículo 2009 revisado - Agroforestal", "Objetivos", "Ninguna", "docs/planes/2004/28 Ingeniería Agroforestal Currículo 2009 Revisado.pdf"),
            ('', "", "CURRÍCULO 2018 - Agroforestal", "","","docs/planes/2018/PROGRAMA_P36_CURRÍCULO INGENIERÍA AGROFORESTAL.pdf")
        ],
        "Medicina Veterinaria": [
            ('2016-02-23', "121-2016-UNSCH-R", "Currículo 2004 Revisado - Veterinaria", "Objetivos", "Ninguna", "docs/planes/2004/24 Medicina Veterinaria Currículo 2004 Revisado.pdf"),
            ('', "", "CURRÍCULO 2018 - Veterinaria", "","","docs/planes/2018/PROGRAMA_P31_CURRÍCULO MEDICINA VETERINARIA.pdf")
        ],
        "Educación Inicial": [
            ('2015-09-21', "N° 532-2015-UNSCH-CU", "Currículo 2004 - revisado - Inicial", "Objetivos", "Ninguna", "docs/planes/2004/03 Educación Inicial Currículo 2004 Revisado.pdf"),
            ('', "", "CURRÍCULO 2018 - Inicial", "","","docs/planes/2018/PROGRAMA_P05_CURRÍCULO EDUCACIÓN INICIAL.pdf")
        ],
        "Educación Primaria": [
            ('2016-06-30', "RCU N° 379-2016-UNSCH-CU", "Currículo 2004 Reajustado revisado - Primaria", "Objetivos", "Ninguna", "docs/planes/2004/04 Educación Primaria Currículo 2004 Revisado.pdf"),
            ('', "", "CURRÍCULO 2018 - Primaria", "","","docs/planes/2018/PROGRAMA_P06_CURRÍCULO EDUCACIÓN PRIMARIA.pdf")
        ],
        "Educación Secundaria - Ciencias Sociales, Filosofía y Psicología": [
            ('', "", "Revisado 2004 - Turismo", "Objetivos", "Ninguna", "docs/planes/2004/05 Educación Secundaria 2004 Revisado.pdf"),
            ('', "", "CURRÍCULO 2018 - Turismo", "","","docs/planes/2018/PROGRAMA_P09_CURRÍCULO EDUCACIÓN SECUNDARIA_CIENCIAS SOCIALES Y FILOSOFÍA.pdf")
        ],
        "Educación Secundaria - Inglés y Lengua Española": [
            ('', "", "Revisado 2004 - Inglés", "Objetivos", "Ninguna", "docs/planes/2004/05 Educación Secundaria 2004 Revisado.pdf"),
            ('', "", "CURRÍCULO 2018 - Inglés", "","","docs/planes/2018/PROGRAMA_P08_CURRÍCULO EDUCACIÓN SECUNDARIA_INGLÉS Y LENGUA ESPAÑOLA.pdf")
        ],
        "Educación Secundaria - Matemática, Física e Informática": [
            ('2020-02-12', "153-2020-UNSCH-R", "Currículo 2004 - Reajustado y Adecuado a la Ley 30220 - Matemática (ES)", "Competencias", 
            "Incongruente, el currículo que maneja la OGA es distinto a los que se encuentran en la Secretaría General.", "docs/planes/2004/05 Educación Secundaria 2004 Revisado.pdf"),
            ('', "", "CURRÍCULO 2018 - Matemática (ES)", "","","docs/planes/2018/PROGRAMA_P10_CURRÍCULO EDUCACIÓN SECUNDARIA_MATEMÁTICA, FÍSICA E INFORMÁTICA.pdf")
        ],
        "Educación Secundaria - Lengua Española y Literatura": [
            ('2020-02-12', "153-2020-UNSCH-R", "Currículo 2004 - Adecuado a la Ley 30220 - Lengua y Literatura", "Competencias", 
            "Incongruente, el currículo que maneja la OGA es distinto a los que se encuentran en la Secretaría General.", "docs/planes/2004/05 Educación Secundaria 2004 Revisado.pdf"),
            ('', "", "CURRÍCULO 2018 - Lengua y Literatura", "", "","docs/planes/2018/PROGRAMA_P07_CURRÍCULO EDUCACIÓN SECUNDARIA_LENGUA ESPAÑOLA Y LITERATURA.pdf")
        ],
        "Educación Física": [
            ('2015-09-21', "533-2015-UNSCH-CU", "Currículo 2004 - Revisado - Ed. Física", "Objetivos", "Ninguna", "docs/planes/2004/06 Educación Física Currículo 2004 Revisado.pdf")
        ],
        "Educación Física - Entrenamiento Deportivo": [
            ('', "", "CURRÍCULO 2018 - Entrenamiento Deportivo", "","","docs/planes/2018/PROGRAMA_P11_P12_P13_CURRÍCULO EDUCACIÓN FÍSICA.pdf")
        ],
        "Educación Física - Gestión Deportiva": [
            ('', "", "CURRÍCULO 2018 - Gestión Deportiva", "","","docs/planes/2018/PROGRAMA_P11_P12_P13_CURRÍCULO EDUCACIÓN FÍSICA.pdf")
        ],
        "Educación Física - Promoción de la Salud Social": [
            ('', "", "CURRÍCULO 2018 - Promoción de la Salud Social", "","","docs/planes/2018/PROGRAMA_P11_P12_P13_CURRÍCULO EDUCACIÓN FÍSICA.pdf")
        ],

        "Administración de Empresas": [
            ('', "", "Currículo 2004 - Administración", "Objetivos", "Ninguna", "docs/planes/2004/07 Administración de Empresas Currículo 2004.pdf"),
            ('', "", "CURRÍCULO 2018 - Administración", "","","docs/planes/2018/PROGRAMA_P14_CURRÍCULO ADMINISTRACIÓN DE EMPRESAS.pdf")
        ],
        "Contabilidad y Auditoría": [
            ('2016-01-12', "N° 055-2016-UNSCH-CU", "Currículo 2004 - Revisado - Contabilidad", "Objetivos", "Ninguna", "docs/planes/2004/08 Contabilidad y Auditoría Currículo 2004 Revisado.pdf"),
            ('', "", "CURRÍCULO 2018 - Contabilidad", "","","docs/planes/2018/PROGRAMA_P15_CURRÍCULO CONTABILIDAD Y AUDITORÍA.pdf")
        ],
        "Economía": [
            ('2016-01-14', "N° 067-2016-UNSCH-CU", "Currículo 2004 - Revisado - Economía", "Objetivos", "Ninguna", "docs/planes/2004/09 Economía Currículo 2004 Revisado.pdf"),
            ('', "", "CURRÍCULO 2018 - Economía", "","","docs/planes/2018/PROGRAMA_P16_CURRÍCULO ECONOMÍA.pdf")
        ],
        "Antropología Social": [
            ('2016-01-27', "N° 056-2016-UNSCH-R", "Currículo 2004- Revisado - Antropología", "Objetivos", "Ninguna", "docs/planes/2004/10 Antropología Social Currículo 2004 Revisado.pdf"),
            ('', "", "CURRÍCULO 2018 - Antropología", "","","docs/planes/2018/PROGRAMA_P17_CURRÍCULO ANTROPOLOGÍA SOCIAL.pdf")
        ],
        "Ciencias de la Comunicación": [
            ('2016-07-11', "393-2016-UNSCH-CU", "Currículo estudios 2004 Revisado - Comunicación", "Objetivos", 
            "En el curso PRACTICA PREPROFESIONAL la sigla figura como PPCC-542, debe ser PP-542", "docs/planes/2004/23 Ciencias de la Comunicación Currículo 2004 Revisado.pdf"),
            ('', "", "CURRÍCULO 2018 - Comunicación", "","","docs/planes/2018PROGRAMA_P30_CURRÍCULO CIENCIAS DE LA COMUNICACIÓN.pdf")
        ],
        "Trabajo Social": [
            ('2016-02-23', "120-2016-UNSCH-R", "CURRÍCULO 2004 - Revisado - Trabajo Social", "Objetivos", "Falta consignar la malla curricular en DIGITAL", "docs/planes/2004/12 Trabajo Social Currículo 2004 Revisado.pdf"),
            ('', "", "CURRÍCULO 2018 - Trabajo Social", "","","docs/planes/2018/PROGRAMA_P20_CURRÍCULO TRABAJO SOCIAL.pdf")
        ],
        "Arqueología e Historia": [
            ('2011-07-18', "N° 550-2011-UNSCH-CU", "Currículo 2004- Reajustado - Arqueología", "Objetivos", "Ninguna", "docs/planes/2004/11 Arqueología e Historia Currículo 2004 Reajustado.pdf"),
        ],
        "Arqueología e Historia - Arqueología": [
            ('', "", "CURRÍCULO 2018 - Arqueología", "","","docs/planes/2018/PROGRAMA_P18_CURRÍCULO ARQUEOLOGÍA E HISTORIA_ARQUEOLOGÍA.pdf")
        ],
        "Arqueología e Historia - Historia": [
            ('', "", "CURRÍCULO 2018 - Historia", "","","docs/planes/2018/PROGRAMA_P19_CURRÍCULO ARQUEOLOGÍA E HISTORIA_HISTORIA.pdf")
        ],
        "Derecho": [
            ('2016-01-12', "N° 057-2016-UNSCH-CU", "Currículo 2004 - Revisado - Derecho", "Objetivos", "Ninguna", "docs/planes/2004/13 Derecho Currículo 2004 Revisado.pdf"),
            ('', "", "CURRÍCULO 2018 - Derecho", "","","docs/planes/2018/PROGRAMA_P21_CURRÍCULO DERECHO.pdf")
        ],
        "Ingeniería de Minas": [
            ('2016-07-22', "453-2016-UNSCH-CU", "Currículo 2004 Revisado - Minas", "Objetivos", "Ninguna", "docs/planes/2004/15 Ingeniería de Minas Currículo 2004 Revisado.pdf"),
            ('', "", "CURRÍCULO 2018 - Minas", "","","docs/planes/2018/PROGRAMA_P23_CURRÍCULO INGENIERÍA DE MINAS.pdf")
        ],
        "Ingeniería Civil": [
            ('2016-08-10', "N° 473-2016-UNSCH-CU", "Currículo 2004 - Revisado - Civil", "Objetivos", 
            "No coincide el contenido (índice) en lo físico y digital. En el digital no se encuentra la malla curricular. Y algunos puntos donde especifica la revisión no coincide con el currículo DIGITAL entregado por la escuela.", "docs/planes/2004/16 Ingeniería Civil Currículo 2004 Revisado.pdf"),
            ('', "", "CURRÍCULO 2018 - Civil", "","","docs/planes/2018/PROGRAMA_P24_CURRÍCULO INGENIERÍA CIVIL.pdf")
        ],
        "Ingeniería de Sistemas": [
            ('2016-07-22', "456-2016-UNSCH-CU", "Currículo de estudios 2005 Revisado - Sistemas", "Objetivos", "Ninguna", "docs/planes/2004/27 Ingeniería de Sistemas Curriculo 2005 Revisado.pdf"),
            ('', "", "CURRÍCULO 2018 - Sistemas", "","","docs/planes/2018/PROGRAMA_P35_CURRÍCULO INGENIERÍA DE SISTEMAS.pdf")
        ],
        "Ciencias Físico-Matemáticas": [
            ('2019-02-28', "236-2019-UNSCH-R", "CURRÍCULO 1998 Matemáticas-Reajustado - Físico-Matemáticas", "Objetivos", "Ninguna", "docs/planes/2004/26 Ciencias Fisico Matematicas Curriculo 1998 Revisado.pdf")
        ],
        "Ciencias Físico-Matemáticas - Matemática": [
            ('', "", "CURRÍCULO 2018 - Matemática", "", "","docs/planes/2018/PROGRAMA_P32_CURRÍCULO MATEMÁTICA.pdf")
        ],
        "Ciencias Físico-Matemáticas - Física": [
            ('', "", "CURRÍCULO 2018 - Física", "", "","docs/planes/2018/PROGRAMA_P33_CURRÍCULO FÍSICA.pdf")
        ],
        "Ciencias Físico-Matemáticas - Estadística": [
            ('', "", "CURRÍCULO 2018 - Estadística", "", "","docs/planes/2018PROGRAMA_P34_CURRÍCULO ESTADÍSTICA.pdf")
        ],
        "Ingeniería Química": [
            ('2020-07-30', "N° 249-2020-UNSCH-CU", "Currículo 2004 - Revisado - Química", "Competencias", "Ninguna", "docs/planes/2004/17 Ingeniería Química Currículo 2004 Revisado.pdf"),
            ('', "", "CURRÍCULO 2018 - Química", "","","docs/planes/2018/PROGRAMA_P38_CURRÍCULO INGENIERÍA QUÍMICA.pdf")
        ],
        "Ingeniería en Industrias Alimentarias": [
            ('2015-11-03', "N° 670-2015-UNSCH-CU", "Currículo 2004 - Revisado - Alimentarias", "Objetivos", 
            "No coincide el contenido (índice) y no registra el cuadro de Departamento académico en cada semestre. La malla curricular está elaborada con diferentes formatos.", "docs/planes/2004/19 Ingeniería en Industrias Alimentarias Currículo 2004 Revisado.pdf"),
            ('', "", "CURRÍCULO 2018 - Alimentarias", "","","docs/planes/2018/PROGRAMA_P26_CURRÍCULO INGENIERÍA EN INDÚSTRIAS ALIMENTARIAS.pdf")
        ],
        "Ingeniería Agroindustrial": [
            ('2016-01-20', "Nº 102-2016-UNSCH-CU", "Currículo 2004 - Reajustado - Agroindustrial", "Objetivos", 
            "No figura en DIGITAL la malla curricular / El cuadro de equivalencias de la escuela NO figura en el currículo FISICO", "docs/planes/2004/22 Ingeniería Agroindustrial Currículo 2004 Revisado.pdf"),
            ('', "", "CURRÍCULO 2018 - Agroindustrial", "","","docs/planes/2018/PROGRAMA_P29_CURRÍCULO INGENIERÍA AGROINDUSTRIAL.pdf")
        ],
        "Enfermería": [
            ('2015-08-24', "Nº 403-2015-UNSCH-CU", "Currículo 2004 - Revisado - Enfermería", "Competencias", "Ninguna", "docs/planes/2004/14 Enfermería Currículo 2004 Revisado.pdf"),
            ('', "", "CURRÍCULO 2018 - Enfermería", "","","docs/planes/2018/PROGRAMA_P22_CURRÍCULO ENFERMERÍA.pdf")
        ],
        "Obstetricia": [
            ('2019-02-06', "N° 157-2019-UNSCH-R", "Currículo 2004 - Actualizado - Obstetricia", "Competencias", 
            "Incongruente, el currículo que maneja la OGA es CURRÍCULO 2004 REAJUSTADO, debe ser CURRÍCULO 2004 ACTUALIZADO, según resolución aprobado el 06/02/2019.", "docs/planes/2004/18 Obstetricia Currículo 2004 Revisado.pdf"),
            ('', "", "CURRÍCULO 2018 - Obstetricia", "","","docs/planes/2018/PROGRAMA_P25_CURRÍCULO OBSTETRICIA.pdf")
        ],
        "Farmacia y Bioquímica": [
            ('2016-01-12', "Nº 056-2016-UNSCH-CU", "Currículo 2004 - Revisado - Farmacia", "Objetivos", 
            "No figura los departamentos académicos en la Distribución de asignaturas, en el currículo que nos facilitó la escuela.", "docs/planes/2004/20 Farmacia y Bioquímica Currículo 2004 revisado.pdf"),
            ('', "", "CURRÍCULO 2018 - Farmacia", "","","docs/planes/2018/PROGRAMA_P27_CURRÍCULO FARMACIA Y BIOQUÍMICA.pdf")
        ],
        "Medicina Humana": [
            ('2020-05-19', "171-2020-UNSCH-CU", "Currículo 2012 - Reajustado - Medicina", "Competencias", "Ninguna", "docs/planes/2004/29 Medicina Humana Currículo 2012 Reajustado.pdf"),
            ('', "", "CURRÍCULO 2018 - Medicina", "","","docs/planes/2018/PROGRAMA_P37_CURRÍCULO MEDICINA HUMANA.pdf")
        ],
        "Biología": [
            ('2016-07-22', "N° 454-2016-UNSCH-CU", "Currículo 2004 - Revisado - Biología", "Objetivos", "Ninguna", "docs/planes/2004/02 Biología Currículo 2004 Revisado.pdf")
        ],
        "Biología - Microbiología": [
            ('', "", "CURRÍCULO 2018 - Microbiología", "","","docs/planes/2018/PROGRAMA_P02_CURRÍCULO MICROBIOLOGÍA.pdf")
        ],
        "Biología - Biotecnología": [
            ('', "", "CURRÍCULO 2018 - Biotecnología", "","","docs/planes/2018/PROGRAMA_P03_CURRÍCULO BIOTECNOLOGÍA.pdf")
        ],
        "Biología - Ecología y Recursos Naturales": [
            ('', "", "CURRÍCULO 2018 - Ecología", "","","docs/planes/2018/PROGRAMA_P04_CURRÍCULO ECOLOGÍA Y RECURSOS NATURALES.PDF")
        ]
    } 

    for escuelax, planes in escuelas_planes.items():
        try:
            cursor.execute("SELECT id_escuela FROM Escuela WHERE nombre_escuela = ?", (escuelax,))
            escuelax_id = cursor.fetchone()

            if escuelax_id:
                escuelax_id = escuelax_id[0]
            else:
                # Manejar el caso en que la escuela no se encuentra
                print(f"Escuela '{escuelax}' no encontrada.")
                continue

            for plan in planes:
                cursor.execute("SELECT id_plan FROM Plan_Estudios WHERE denominacion_plan = ?", (plan[2],))
                plan_id = cursor.fetchone()

                if not plan_id:
                    cursor.execute(
                        "INSERT INTO Plan_Estudios (fecha_plan, resolucion_plan, denominacion_plan, enfoque_plan, observacion_plan, rutaArchivo_plan, id_escuela) VALUES (?, ?, ?, ?, ?, ?, ?)",
                        (plan[0], plan[1], plan[2], plan[3], plan[4], plan[5], escuelax_id)
                    )
                    print(f"Plan '{plan[2]}' insertado para la escuela '{escuelax}'.")
                else:
                    print(f"Plan '{plan[2]}' ya existe para la escuela '{escuelax}'.")
        except sqlite3.Error as e:
            print(f"Error al procesar la escuela '{escuelax}': {e}")

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
                 "DC A1", "DC A2", "DC A3", "DC B1", "DC B2", "DC B3"]
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
    semestres = [("2024-I", "17 semanas", '2023-09-19', '2024-04-03'), ("2024-0", "8 semanas", '', ''), ("2024-II", "17 semanas", '2023-06-03', '2024-11-28'), ("2025-I", "17 semanas", '', ''), ("2025-II", "17 semanas", '', '')]
    for semestre in semestres:
        cursor.execute(
            "SELECT id_semestre FROM Semestre WHERE nombre_semestre = ?", (semestre[0],))
        semestre_id = cursor.fetchone()
        if not semestre_id:
            # Reemplazar valores vacíos con NULL para fechas
            fecha_inicio = semestre[2] if semestre[2] else None
            fecha_fin = semestre[3] if semestre[3] else None

            cursor.execute(
                "INSERT INTO Semestre (nombre_semestre, duracion_semestre, fechaInicio_semestre, fechaFin_semestre) VALUES (?,?,?,?)",
                (semestre[0], semestre[1], fecha_inicio, fecha_fin)
            )

    # Definir las categorías de actividades
    categorias_actividades = [
        ("Actividades Lectivas", [
            "Actividades de Docencia Lectiva"
        ]),
        ("Actividades No Lectivas", [
            "Actividades de RSPEC",
            "Actividades de Investigación e Innovación",
            "Actividades de Tutoría",
            "Actividades de Gestión",
            "Actividades de Docencia No Lectiva"
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
            ("PCP", "Práctica Clínica Presencial"),
            ("PCI", "Práctica en Comunidad o Institución"),
        ],
        "Actividades de RSPEC": [
            ("ARS", "Actividad de Responsabilidad Social"),
            ("APS", "Actividad de Proyección Social"),
            ("AEC", "Actividad de Extensión Cultural")
        ],
        "Actividades de Investigación e Innovación": [
            ("SIII", "Sesión de Instituto de Investigación e Innovación"),
            ("AIN", "Actividades de Investigación")
        ],
        "Actividades de Tutoría": [
            ("TI", "Tutoría Individual"),
            ("TG", "Tutoría Grupal")
        ],
        "Actividades de Gestión": [
            ("LAD", "Labores Administrativas"),
            ("SCU", "Sesión de Consejo Universitario"),
            ("SCF", "Sesión de Consejo de Facultad"),
            ("SDP", "Sesión de Departamento Académico"),
            ("SEF", "Sesión de Escuela Profesional"),
            ("CP", "Comisiones Permanentes")
        ],
        "Actividades de Docencia No Lectiva": [
            ("PCE", "Preparación de Clases y Evaluaciones")
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
    tipos_licencias = ["Licencia por año sabático", "Licencia por estudio"]
    for tipo_licencia in tipos_licencias:
        cursor.execute(
            "SELECT id_tipoLicencia FROM Tipo_Licencia WHERE nombre_tipoLicencia = ?", (tipo_licencia,))
        semestre_id = cursor.fetchone()
        if not semestre_id:
            cursor.execute(
                "INSERT INTO Tipo_Licencia (nombre_tipoLicencia) VALUES (?)", (tipo_licencia,))

    # Asegurarse de que los cambios se guarden en la base de datos
    cursor.connection.commit()
