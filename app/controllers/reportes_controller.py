from app.views.reportes_view import ReportesView

from app.controllers.reportes.reporteDocente_controller import ReporteDocenteController
from app.controllers.reportes.reporteContrato_controller import ReporteContratoController
from app.controllers.reportes.reporteAccion_controller import ReporteAccionController
from app.controllers.reportes.reporteLicencia_controller import ReporteLicenciaController

class ReportesController:

    def __init__(self):
        self.reportes_view = None

        self.reporteDocente_controller = None   # Inicializar el controlador de docente
        self.reporteContrato_controller = None   # Inicializar el controlador de contrato
        self.reporteAccion_controller = None   # Inicializar el controlador de contrato
        self.reporteLicencia_controller = None   # Inicializar el controlador de contrato

    def show_view(self):
        if not self.reportes_view or not self.reportes_view.winfo_exists():
            self.reportes_view = ReportesView(self)
        self.reportes_view.grab_set()


    ################################ LLAMADA A CONTROLES DE LOS BOTONES ##############################

    def open_reporteDocente_view(self):
        if not self.reporteDocente_controller:
            self.reporteDocente_controller = ReporteDocenteController()
        self.reporteDocente_controller.show_view()
    
    def open_reporteContrato_view(self):
        if not self.reporteContrato_controller:
            self.reporteContrato_controller = ReporteContratoController()
        self.reporteContrato_controller.show_view()

    def open_reporteAccion_view(self):
        if not self.reporteAccion_controller:
            self.reporteAccion_controller = ReporteAccionController()
        self.reporteAccion_controller.show_view()
        
    def open_reporteLicencia_view(self):
        if not self.reporteLicencia_controller:
            self.reporteLicencia_controller = ReporteLicenciaController()
        self.reporteLicencia_controller.show_view()
