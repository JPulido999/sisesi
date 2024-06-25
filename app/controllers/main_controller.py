from app.views.main_view import MainView
from app.controllers.gestion_controller import GestionController
from app.controllers.administrar_controller import AdministrarController
from app.controllers.extraerPlan_controller import ExtraerPlanController
from app.controllers.reportes_controller import ReportesController

class MainController:
    def __init__(self):
        self.main_view = MainView(self)
        self.gestion_controller = None
        self.administrar_controller = None
        self.extraerPlan_controller = None
        self.reportes_controller = None

    def run(self):
        self.main_view.mainloop()


    ################################ LLAMADA A CONTROLES DE LOS BOTONES ##############################
        

    def open_gestion_view(self):
        if not self.gestion_controller:
            self.gestion_controller = GestionController()
        self.gestion_controller.show_view()

    def open_administrar_view(self):
        if not self.administrar_controller:
            self.administrar_controller = AdministrarController()
        self.administrar_controller.show_view()

    def open_extraerPlan_view(self):
        if not self.extraerPlan_controller:
            self.extraerPlan_controller = ExtraerPlanController()
        self.extraerPlan_controller.show_view()
    
    def open_reportes_view(self):
        if not self.reportes_controller:
            self.reportes_controller = ReportesController()
        self.reportes_controller.show_view()
