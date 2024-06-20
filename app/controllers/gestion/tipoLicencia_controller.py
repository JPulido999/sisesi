from app.views.tipo_licencia_view import TipoLicenciaView
from app.models.gestion_model.tipoLicencia_model import TipoLicenciaModel

class TipoLicenciaController:
    def __init__(self):
        self.tipo_licencia_view = None
        self.tipo_licencia_model = TipoLicenciaModel()

    def show_view(self):
        if not self.tipo_licencia_view or not self.tipo_licencia_view.winfo_exists():
            self.tipo_licencia_view = TipoLicenciaView(self)
            self.tipo_licencia_view.update_tipo_licencia_list()
        self.tipo_licencia_view.grab_set()

    ################################ LLAMADA A METODOS DE LOS BOTONES ##############################

    def create_tipo_licencia(self, nombre_tipoLicencia):
        self.tipo_licencia_model.create_tipo_licencia(nombre_tipoLicencia)
        self.tipo_licencia_view.update_tipo_licencia_list()

    def read_tipo_licencia(self, id_tipoLicencia):
        return self.tipo_licencia_model.read_tipo_licencia(id_tipoLicencia)

    def update_tipo_licencia(self, id_tipoLicencia, nombre_tipoLicencia):
        self.tipo_licencia_model.update_tipo_licencia(id_tipoLicencia, nombre_tipoLicencia)
        self.tipo_licencia_view.update_tipo_licencia_list()

    def delete_tipo_licencia(self, id_tipoLicencia):
        self.tipo_licencia_model.delete_tipo_licencia(id_tipoLicencia)
        self.tipo_licencia_view.update_tipo_licencia_list()

    def list_all_tipo_licencia(self):
        return self.tipo_licencia_model.list_all_tipo_licencias()
