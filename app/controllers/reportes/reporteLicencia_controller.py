from app.views.reportes.reporteLicencia_view import ReporteLicenciaView
from app.models.reportes_model import ReportesModel

class ReporteLicenciaController:
    def __init__(self):
        self.licencia_view = None
        self.licencia_model = ReportesModel()

    def show_view(self):
        if not self.licencia_view or not self.licencia_view.winfo_exists():
            self.licencia_view = ReporteLicenciaView(self)
            self.licencia_view.update_licencia_list()
        self.licencia_view.grab_set()

    ################################ LLAMADA A METODOS DE LOS BOTONES ##############################
    def read_licencia(self, id_licencia):
        return self.licencia_model.read_licencia(id_licencia)

    ############################################

    def list_all_consulta_licencia(self, nombreDocente, dniDocente):
        return self.licencia_model.list_all_licencias_c1(nombreDocente, dniDocente)

    
    
    def buscar_licencia_por_resolucion(self, resolucion):
        return self.licencia_model.buscar_licencia_por_resolucion(resolucion)