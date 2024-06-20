from app.views.gestion.docente_view import DocenteView
from app.models.gestion_model.docente_model import DocenteModel

class DocenteController:

    def __init__(self):
        self.docente_view = None
        self.docente_model = DocenteModel()

    def show_view(self):
        if not self.docente_view or not self.docente_view.winfo_exists():
            self.docente_view = DocenteView(self)
            self.docente_view.update_docente_list()
        self.docente_view.grab_set()

    ################################ LLAMADA A METODOS DE LOS BOTONES ##############################

    def create_docente(self, nombres, apellido_paterno, apellido_materno, correo, dni, celular, grado_maestro, grado_doctor, titulo_profesional, titulo_esp_medico, titulo_esp_odonto, grado_bachiller):
        self.docente_model.create_docente(nombres, apellido_paterno, apellido_materno, correo, dni, celular, grado_maestro, grado_doctor, titulo_profesional, titulo_esp_medico, titulo_esp_odonto, grado_bachiller)
        self.docente_view.update_docente_list()

    def read_docente(self, id_docente):
        return self.docente_model.read_docente(id_docente)

    def update_docente(self, id_docente, nombres, apellido_paterno, apellido_materno, correo, dni, celular, grado_maestro, grado_doctor, titulo_profesional, titulo_esp_medico, titulo_esp_odonto, grado_bachiller):
        self.docente_model.update_docente(id_docente, nombres, apellido_paterno, apellido_materno, correo, dni, celular, grado_maestro, grado_doctor, titulo_profesional, titulo_esp_medico, titulo_esp_odonto, grado_bachiller)
        self.docente_view.update_docente_list()

    def delete_docente(self, id_docente):
        self.docente_model.delete_docente(id_docente)
        self.docente_view.update_docente_list()

    ############################################

    def list_all_docente(self):
        return self.docente_model.list_all_docente()
    
    def buscar_docente_por_nombre(self, nombres):
        return self.docente_model.buscar_docente_por_nombre(nombres)
    
    def buscar_docente_por_dni(self, dni):
        return self.docente_model.buscar_docente_por_dni(dni)
    
    ############################################



