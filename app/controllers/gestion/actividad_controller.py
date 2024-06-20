from app.views.actividad_view import ActividadView
from app.models.gestion_model.actividad_model import ActividadModel

class ActividadController:
    def __init__(self):
        self.actividad_view = None
        self.actividad_model = ActividadModel()

    def show_view(self):
        if not self.actividad_view or not self.actividad_view.winfo_exists():
            self.actividad_view = ActividadView(self)
            self.actividad_view.update_actividad_list()
        self.actividad_view.grab_set()

    ################################ LLAMADA A METODOS DE LOS BOTONES ##############################

    def create_actividad(self, nombre_actividad, id_categoriaActividad):
        self.actividad_model.create_actividad(nombre_actividad, id_categoriaActividad)
        self.actividad_view.update_actividad_list()

    def read_actividad(self, id_actividad):
        return self.actividad_model.read_actividad(id_actividad)

    def update_actividad(self, id_actividad, nombre_actividad, id_categoriaActividad):
        self.actividad_model.update_actividad(id_actividad, nombre_actividad, id_categoriaActividad)
        self.actividad_view.update_actividad_list()

    def delete_actividad(self, id_actividad):
        self.actividad_model.delete_actividad(id_actividad)
        self.actividad_view.update_actividad_list()

    def list_all_actividad(self):
        return self.actividad_model.list_all_actividades()
