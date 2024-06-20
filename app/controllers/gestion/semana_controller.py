from app.views.semana_view import SemanaView
from app.models.gestion_model.semana_model import SemanaModel

class SemanaController:
    def __init__(self):
        self.semana_view = None
        self.semana_model = SemanaModel()

    def show_view(self):
        if not self.semana_view or not self.semana_view.winfo_exists():
            self.semana_view = SemanaView(self)
            self.semana_view.update_semana_list()
        self.semana_view.grab_set()

    ################################ LLAMADA A METODOS DE LOS BOTONES ##############################

    def create_semana(self, nombre_semana, contenido_semana, id_unidad):
        self.semana_model.create_semana(nombre_semana, contenido_semana, id_unidad)
        self.semana_view.update_semana_list()

    def read_semana(self, id_semana):
        return self.semana_model.read_semana(id_semana)

    def update_semana(self, id_semana, nombre_semana, contenido_semana, id_unidad):
        self.semana_model.update_semana(id_semana, nombre_semana, contenido_semana, id_unidad)
        self.semana_view.update_semana_list()

    def delete_semana(self, id_semana):
        self.semana_model.delete_semana(id_semana)
        self.semana_view.update_semana_list()

    def list_all_semana(self):
        return self.semana_model.list_all_semanas()
