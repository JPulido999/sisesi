from app.views.asignatura_view import AsignaturaView
from app.models.gestion_model.asignatura_model import AsignaturaModel

class AsignaturaController:
    def __init__(self):
        self.asignatura_view = None
        self.asignatura_model = AsignaturaModel()

    def show_view(self):
        if not self.asignatura_view or not self.asignatura_view.winfo_exists():
            self.asignatura_view = AsignaturaView(self)
            self.asignatura_view.update_asignatura_list()
        self.asignatura_view.grab_set()

    ################################ LLAMADA A METODOS DE LOS BOTONES ##############################

    def create_asignatura(self, nombre_asignatura, sigla_asignatura, creditos_asignatura, horasTs_asignatura, horasPs_asignatura, horasLs_asignatura, id_plan, id_departamento):
        self.asignatura_model.create_asignatura(nombre_asignatura, sigla_asignatura, creditos_asignatura, horasTs_asignatura, horasPs_asignatura, horasLs_asignatura, id_plan, id_departamento)
        self.asignatura_view.update_asignatura_list()

    def read_asignatura(self, id_asignatura):
        return self.asignatura_model.read_asignatura(id_asignatura)

    def update_asignatura(self, id_asignatura, nombre_asignatura, sigla_asignatura, creditos_asignatura, horasTs_asignatura, horasPs_asignatura, horasLs_asignatura, id_plan, id_departamento):
        self.asignatura_model.update_asignatura(id_asignatura, nombre_asignatura, sigla_asignatura, creditos_asignatura, horasTs_asignatura, horasPs_asignatura, horasLs_asignatura, id_plan, id_departamento)
        self.asignatura_view.update_asignatura_list()

    def delete_asignatura(self, id_asignatura):
        self.asignatura_model.delete_asignatura(id_asignatura)
        self.asignatura_view.update_asignatura_list()

    def list_all_asignatura(self):
        return self.asignatura_model.list_all_asignaturas()
