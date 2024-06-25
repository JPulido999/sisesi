from app.views.reportes.reporteContrato_view import ReporteContratoView
from app.models.reportes_model import ReportesModel

class ReporteContratoController:
    def __init__(self):
        self.contrato_view = None
        self.contrato_model = ReportesModel()

    def show_view(self):
        if not self.contrato_view or not self.contrato_view.winfo_exists():
            self.contrato_view = ReporteContratoView(self)
            self.contrato_view.update_contrato_list()
        self.contrato_view.grab_set()

    ################################ LLAMADA A METODOS DE LOS BOTONES ##############################

    def read_contrato(self, id_contrato):
        return self.contrato_model.read_contrato(id_contrato)




    def list_all_contrato(self):
        return self.contrato_model.list_all_contrato()
    
    def buscar_contrato_por_docente(self, id_docente):
        return self.contrato_model.buscar_contrato_por_docente(id_docente)
