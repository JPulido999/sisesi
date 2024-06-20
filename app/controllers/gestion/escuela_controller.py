from app.views.gestion.escuela_view import EscuelaView
from app.models.gestion_model.escuela_model import EscuelaModel

class EscuelaController:

    def __init__(self):
        self.escuela_view = None
        self.escuela_model = EscuelaModel()

    def show_view(self):
        if not self.escuela_view or not self.escuela_view.winfo_exists():
            self.escuela_view = EscuelaView(self)
            self.escuela_view.update_escuela_list()
        self.escuela_view.grab_set()

    ################################ LLAMADA A METODOS DE LOS BOTONES ##############################

    def create_escuela(self, nombre, id_facultad):
        self.escuela_model.create_escuela(nombre, id_facultad)
        self.escuela_view.update_escuela_list()

    def read_escuela(self, id_escuela):
        return self.escuela_model.read_escuela(id_escuela)

    def update_escuela(self, id_escuela, nombre, id_facultad):
        self.escuela_model.update_escuela(id_escuela, nombre, id_facultad)
        self.escuela_view.update_escuela_list()

    def delete_escuela(self, id_escuela):
        self.escuela_model.delete_escuela(id_escuela)
        self.escuela_view.update_escuela_list()



    def list_all_escuela(self):
        return self.escuela_model.list_all_escuela()
    
    def buscar_escuela_por_nombre(self, nombre):
        return self.escuela_model.buscar_escuela_por_nombre(nombre)
