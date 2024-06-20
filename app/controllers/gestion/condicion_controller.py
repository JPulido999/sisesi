from app.views.condicion_view import CondicionView
from app.models.gestion_model.condicion_model import CondicionModel

class CondicionController:
    def __init__(self):
        self.condicion_view = None
        self.condicion_model = CondicionModel()

    def show_view(self):
        if not self.condicion_view or not self.condicion_view.winfo_exists():
            self.condicion_view = CondicionView(self)
            self.condicion_view.update_condicion_list()
        self.condicion_view.grab_set()

    ################################ LLAMADA A METODOS DE LOS BOTONES ##############################

    def create_condicion(self, nombre_condicion):
        self.condicion_model.create_condicion(nombre_condicion)
        self.condicion_view.update_condicion_list()

    def read_condicion(self, id_condicion):
        return self.condicion_model.read_condicion(id_condicion)

    def update_condicion(self, id_condicion, nombre_condicion):
        self.condicion_model.update_condicion(id_condicion, nombre_condicion)
        self.condicion_view.update_condicion_list()

    def delete_condicion(self, id_condicion):
        self.condicion_model.delete_condicion(id_condicion)
        self.condicion_view.update_condicion_list()

    def list_all_condicion(self):
        return self.condicion_model.list_all_condiciones()
