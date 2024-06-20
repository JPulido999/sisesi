from app.views.semestre_view import SemestreView
from app.models.gestion_model.semestre_model import SemestreModel

class SemestreController:
    def __init__(self):
        self.semestre_view = None
        self.semestre_model = SemestreModel()

    def show_view(self):
        if not self.semestre_view or not self.semestre_view.winfo_exists():
            self.semestre_view = SemestreView(self)
            self.semestre_view.update_semestre_list()
        self.semestre_view.grab_set()

    ################################ LLAMADA A METODOS DE LOS BOTONES ##############################

    def create_semestre(self, nombre_semestre, duracion_semestre, fechaInicio_semestre, fechaFin_semestre, estado_semestre):
        self.semestre_model.create_semestre(nombre_semestre, duracion_semestre, fechaInicio_semestre, fechaFin_semestre, estado_semestre)
        self.semestre_view.update_semestre_list()

    def read_semestre(self, id_semestre):
        return self.semestre_model.read_semestre(id_semestre)

    def update_semestre(self, id_semestre, nombre_semestre, duracion_semestre, fechaInicio_semestre, fechaFin_semestre, estado_semestre):
        self.semestre_model.update_semestre(id_semestre, nombre_semestre, duracion_semestre, fechaInicio_semestre, fechaFin_semestre, estado_semestre)
        self.semestre_view.update_semestre_list()

    def delete_semestre(self, id_semestre):
        self.semestre_model.delete_semestre(id_semestre)
        self.semestre_view.update_semestre_list()

    def list_all_semestre(self):
        return self.semestre_model.list_all_semestres()
