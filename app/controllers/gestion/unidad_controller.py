from app.views.unidad_view import UnidadView
from app.models.gestion_model.unidad_model import UnidadModel

class UnidadController:
    def __init__(self):
        self.unidad_view = None
        self.unidad_model = UnidadModel()

    def show_view(self):
        if not self.unidad_view or not self.unidad_view.winfo_exists():
            self.unidad_view = UnidadView(self)
            self.unidad_view.update_unidad_list()
        self.unidad_view.grab_set()

    ################################ LLAMADA A METODOS DE LOS BOTONES ##############################

    def create_unidad(self, numero_unidad, id_sil):
        self.unidad_model.create_unidad(numero_unidad, id_sil)
        self.unidad_view.update_unidad_list()

    def read_unidad(self, id_unidad):
        return self.unidad_model.read_unidad(id_unidad)

    def update_unidad(self, id_unidad, numero_unidad, id_sil):
        self.unidad_model.update_unidad(id_unidad, numero_unidad, id_sil)
        self.unidad_view.update_unidad_list()

    def delete_unidad(self, id_unidad):
        self.unidad_model.delete_unidad(id_unidad)
        self.unidad_view.update_unidad_list()

    def list_all_unidad(self):
        return self.unidad_model.list_all_unidades()
