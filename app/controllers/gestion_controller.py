from app.views.gestion_view import GestionView

from app.controllers.gestion.facultad_controller import FacultadController
from app.controllers.gestion.escuela_controller import EscuelaController
from app.controllers.gestion.docente_controller import DocenteController
from app.controllers.gestion.contrato_controller import ContratoController
from app.controllers.gestion.accion_controller import AccionController
from app.controllers.gestion.licencia_controller import LicenciaController

class GestionController:

    def __init__(self):
        self.gestion_view = None
        self.facultad_controller = None  # Inicializar el controlador de facultad
        self.escuela_controller = None   # Inicializar el controlador de escuela
        self.docente_controller = None   # Inicializar el controlador de docente
        self.contrato_controller = None   # Inicializar el controlador de contrato
        self.accion_controller = None   # Inicializar el controlador de contrato
        self.licencia_controller = None   # Inicializar el controlador de contrato

    def show_view(self):
        if not self.gestion_view or not self.gestion_view.winfo_exists():
            self.gestion_view = GestionView(self)
        self.gestion_view.grab_set()


    ################################ LLAMADA A CONTROLES DE LOS BOTONES ##############################

    def open_facultad_view(self):
        if not self.facultad_controller:
            self.facultad_controller = FacultadController()
        self.facultad_controller.show_view()

    def open_escuela_view(self):
        if not self.escuela_controller:
            self.escuela_controller = EscuelaController()
        self.escuela_controller.show_view()

    def open_docente_view(self):
        if not self.docente_controller:
            self.docente_controller = DocenteController()
        self.docente_controller.show_view()
    
    def open_contrato_view(self):
        if not self.contrato_controller:
            self.contrato_controller = ContratoController()
        self.contrato_controller.show_view()

    def open_accion_view(self):
        if not self.accion_controller:
            self.accion_controller = AccionController()
        self.accion_controller.show_view()
        
    def open_licencia_view(self):
        if not self.licencia_controller:
            self.licencia_controller = LicenciaController()
        self.licencia_controller.show_view()
