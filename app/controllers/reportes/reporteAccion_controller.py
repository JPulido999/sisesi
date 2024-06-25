from app.views.reportes.reporteAccion_view import ReporteAccionView
from app.models.reportes_model import ReportesModel

class ReporteAccionController:
    def __init__(self):
        self.accion_view = None
        self.accion_model = ReportesModel()

    def show_view(self):
        if not self.accion_view or not self.accion_view.winfo_exists():
            self.accion_view = ReporteAccionView(self)
            self.accion_view.update_accion_list()
        self.accion_view.grab_set()

    ################################ LLAMADA A METODOS DE LOS BOTONES ##############################

    def read_accion(self, id_accion):
        return self.accion_model.read_accion(id_accion)


    def list_all_accion(self):
        return self.accion_model.list_all_acciones()
