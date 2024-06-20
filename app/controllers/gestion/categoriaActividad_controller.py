from app.views.categoria_actividad_view import CategoriaActividadView
from app.models.gestion_model.categoria_actividad_model import CategoriaActividadModel

class CategoriaActividadController:
    def __init__(self):
        self.categoria_actividad_view = None
        self.categoria_actividad_model = CategoriaActividadModel()

    def show_view(self):
        if not self.categoria_actividad_view or not self.categoria_actividad_view.winfo_exists():
            self.categoria_actividad_view = CategoriaActividadView(self)
            self.categoria_actividad_view.update_categoria_actividad_list()
        self.categoria_actividad_view.grab_set()

    ################################ LLAMADA A METODOS DE LOS BOTONES ##############################

    def create_categoria_actividad(self, nombre_catAct, descripcion_catAct):
        self.categoria_actividad_model.create_categoria_actividad(nombre_catAct, descripcion_catAct)
        self.categoria_actividad_view.update_categoria_actividad_list()

    def read_categoria_actividad(self, id_catAct):
        return self.categoria_actividad_model.read_categoria_actividad(id_catAct)

    def update_categoria_actividad(self, id_catAct, nombre_catAct, descripcion_catAct):
        self.categoria_actividad_model.update_categoria_actividad(id_catAct, nombre_catAct, descripcion_catAct)
        self.categoria_actividad_view.update_categoria_actividad_list()

    def delete_categoria_actividad(self, id_catAct):
        self.categoria_actividad_model.delete_categoria_actividad(id_catAct)
        self.categoria_actividad_view.update_categoria_actividad_list()

    def list_all_categoria_actividad(self):
        return self.categoria_actividad_model.list_all_categoria_actividad()
