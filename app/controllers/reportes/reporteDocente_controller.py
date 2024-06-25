from app.views.reportes.reporteDocente_view import ReporteDocenteView
from app.models.reportes_model import ReportesModel


class ReporteDocenteController:

    def __init__(self):
        self.docente_view = None
        self.docente_model = ReportesModel()

    def show_view(self):
        if not self.docente_view or not self.docente_view.winfo_exists():
            self.docente_view = ReporteDocenteView(self)
            self.docente_view.update_docente_list()
        self.docente_view.grab_set()

    ################################ LLAMADA A METODOS DE LOS BOTONES ##############################

    def read_docente(self, id_docente):
        return self.docente_model.read_docente(id_docente)

    ############################################

    def list_all_docente(self):
        return self.docente_model.list_all_docente()
    
    def buscar_docente_por_nombre(self, nombres):
        return self.docente_model.buscar_docente_por_nombre(nombres)
    
    def buscar_docente_por_dni(self, dni):
        return self.docente_model.buscar_docente_por_dni(dni)
    
    ############################################



