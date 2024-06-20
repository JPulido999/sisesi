from app.views.gestion.facultad_view import FacultadView
from app.models.gestion_model.facultad_model import FacultadModel

class FacultadController:

    def __init__(self):
        self.facultad_view = None
        self.facultad_model = FacultadModel()

    def show_view(self):
        if not self.facultad_view or not self.facultad_view.winfo_exists():
            self.facultad_view = FacultadView(self)
            self.facultad_view.update_facultad_list()  # Llama a update_facultad_list() aquí

        self.facultad_view.grab_set()

    ################################ LLAMADA A METODOS DE LOS BOTONES ##############################

    def create_facultad(self, sigla, nombre):
        self.facultad_model.create_facultad(sigla, nombre)
        self.facultad_view.update_facultad_list()

    def read_facultad(self, id_facultad):
        return self.facultad_model.read_facultad(id_facultad)
    
    def update_facultad(self, id_facultad, sigla, nombre):
        self.facultad_model.update_facultad(id_facultad, sigla, nombre)
        self.facultad_view.update_facultad_list()

    def delete_facultad(self, id_facultad):
        self.facultad_model.delete_facultad(id_facultad)
        self.facultad_view.update_facultad_list()

    ############################################

    def list_all_facultad(self):
        return self.facultad_model.list_all_facultad()
    
    def buscar_facultad_por_nombre(self, nombre):
        return self.facultad_model.buscar_facultad_por_nombre(nombre)
