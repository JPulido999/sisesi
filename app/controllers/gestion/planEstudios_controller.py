from app.views.plan_estudios_view import PlanEstudiosView
from app.models.gestion_model.planEstudios_model import PlanEstudiosModel

class PlanEstudiosController:
    def __init__(self):
        self.plan_estudios_view = None
        self.plan_estudios_model = PlanEstudiosModel()

    def show_view(self):
        if not self.plan_estudios_view or not self.plan_estudios_view.winfo_exists():
            self.plan_estudios_view = PlanEstudiosView(self)
            self.plan_estudios_view.update_plan_estudios_list()
        self.plan_estudios_view.grab_set()

    ################################ LLAMADA A METODOS DE LOS BOTONES ##############################

    def create_plan_estudios(self, nombre_plan, id_escuela):
        self.plan_estudios_model.create_plan_estudios(nombre_plan, id_escuela)
        self.plan_estudios_view.update_plan_estudios_list()

    def read_plan_estudios(self, id_plan):
        return self.plan_estudios_model.read_plan_estudios(id_plan)

    def update_plan_estudios(self, id_plan, nombre_plan, id_escuela):
        self.plan_estudios_model.update_plan_estudios(id_plan, nombre_plan, id_escuela)
        self.plan_estudios_view.update_plan_estudios_list()

    def delete_plan_estudios(self, id_plan):
        self.plan_estudios_model.delete_plan_estudios(id_plan)
        self.plan_estudios_view.update_plan_estudios_list()

    def list_all_plan_estudios(self):
        return self.plan_estudios_model.list_all_planes_estudios()
