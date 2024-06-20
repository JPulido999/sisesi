from app.views.licencia_view import LicenciaView
from app.models.gestion_model.licencia_model import LicenciaModel

class LicenciaController:
    def __init__(self):
        self.licencia_view = None
        self.licencia_model = LicenciaModel()

    def show_view(self):
        if not self.licencia_view or not self.licencia_view.winfo_exists():
            self.licencia_view = LicenciaView(self)
            self.licencia_view.update_licencia_list()
        self.licencia_view.grab_set()

    ################################ LLAMADA A METODOS DE LOS BOTONES ##############################

    def create_licencia(self, resolucion_licencia, fechaInicio_licencia, fechaFin_licencia, observacion_licencia, id_tipoLicencia, id_docente):
        self.licencia_model.create_licencia(resolucion_licencia, fechaInicio_licencia, fechaFin_licencia, observacion_licencia, id_tipoLicencia, id_docente)
        self.licencia_view.update_licencia_list()

    def read_licencia(self, id_licencia):
        return self.licencia_model.read_licencia(id_licencia)

    def update_licencia(self, id_licencia, resolucion_licencia, fechaInicio_licencia, fechaFin_licencia, observacion_licencia, id_tipoLicencia, id_docente):
        self.licencia_model.update_licencia(id_licencia, resolucion_licencia, fechaInicio_licencia, fechaFin_licencia, observacion_licencia, id_tipoLicencia, id_docente)
        self.licencia_view.update_licencia_list()

    def delete_licencia(self, id_licencia):
        self.licencia_model.delete_licencia(id_licencia)
        self.licencia_view.update_licencia_list()

    def list_all_licencia(self):
        return self.licencia_model.list_all_licencias()
