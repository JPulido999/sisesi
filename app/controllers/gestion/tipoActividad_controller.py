from app.views.tipo_actividad_view import TipoActividadView
from app.models.gestion_model.tipoActividad_model import TipoActividadModel

class TipoActividadController:
    def __init__(self):
        self.tipo_actividad_view = None
        self.tipo_actividad_model = TipoActividadModel()

    def show_view(self):
        if not self.tipo_actividad_view or not self.tipo_actividad_view.winfo_exists():
            self.tipo_actividad_view = TipoActividadView(self)
            self.tipo_actividad_view.update_tipo_actividad_list()
        self.tipo_actividad_view.grab_set()

    ################################ LLAMADA A METODOS DE LOS BOTONES ##############################

    def create_tipo_actividad(self, nombre_tipoActividad, sigla_tipoActividad, id_actividad):
        self.tipo_actividad_model.create_tipo_actividad(nombre_tipoActividad, sigla_tipoActividad, id_actividad)
        self.tipo_actividad_view.update_tipo_actividad_list()

    def read_tipo_actividad(self, id_tipoActividad):
        return self.tipo_actividad_model.read_tipo_actividad(id_tipoActividad)

    def update_tipo_actividad(self, id_tipoActividad, nombre_tipoActividad, sigla_tipoActividad, id_actividad):
        self.tipo_actividad_model.update_tipo_actividad(id_tipoActividad, nombre_tipoActividad, sigla_tipoActividad, id_actividad)
        self.tipo_actividad_view.update_tipo_actividad_list()

    def delete_tipo_actividad(self, id_tipoActividad):
        self.tipo_actividad_model.delete_tipo_actividad(id_tipoActividad)
        self.tipo_actividad_view.update_tipo_actividad_list()

    def list_all_tipo_actividad(self):
        return self.tipo_actividad_model.list_all_tipo_actividades()
