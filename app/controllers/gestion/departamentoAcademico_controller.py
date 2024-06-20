from app.views.departamento_academico_view import DepartamentoAcademicoView
from app.models.gestion_model.departamento_academico_model import DepartamentoAcademicoModel

class DepartamentoAcademicoController:
    def __init__(self):
        self.departamento_academico_view = None
        self.departamento_academico_model = DepartamentoAcademicoModel()

    def show_view(self):
        if not self.departamento_academico_view or not self.departamento_academico_view.winfo_exists():
            self.departamento_academico_view = DepartamentoAcademicoView(self)
            self.departamento_academico_view.update_departamento_academico_list()
        self.departamento_academico_view.grab_set()

    ################################ LLAMADA A METODOS DE LOS BOTONES ##############################

    def create_departamento_academico(self, nombre_departamento):
        self.departamento_academico_model.create_departamento_academico(nombre_departamento)
        self.departamento_academico_view.update_departamento_academico_list()

    def read_departamento_academico(self, id_departamento):
        return self.departamento_academico_model.read_departamento_academico(id_departamento)

    def update_departamento_academico(self, id_departamento, nombre_departamento):
        self.departamento_academico_model.update_departamento_academico(id_departamento, nombre_departamento)
        self.departamento_academico_view.update_departamento_academico_list()

    def delete_departamento_academico(self, id_departamento):
        self.departamento_academico_model.delete_departamento_academico(id_departamento)
        self.departamento_academico_view.update_departamento_academico_list()

    def list_all_departamento_academico(self):
        return self.departamento_academico_model.list_all_departamentos_academicos()
