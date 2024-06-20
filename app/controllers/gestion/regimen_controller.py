from app.views.regimen_view import RegimenView
from app.models.gestion_model.regimen_model import RegimenModel

class RegimenController:
    def __init__(self):
        self.regimen_view = None
        self.regimen_model = RegimenModel()

    def show_view(self):
        if not self.regimen_view or not self.regimen_view.winfo_exists():
            self.regimen_view = RegimenView(self)
            self.regimen_view.update_regimen_list()
        self.regimen_view.grab_set()

    ################################ LLAMADA A METODOS DE LOS BOTONES ##############################

    def create_regimen(self, nombre_regimen):
        self.regimen_model.create_regimen(nombre_regimen)
        self.regimen_view.update_regimen_list()

    def read_regimen(self, id_regimen):
        return self.regimen_model.read_regimen(id_regimen)

    def update_regimen(self, id_regimen, nombre_regimen):
        self.regimen_model.update_regimen(id_regimen, nombre_regimen)
        self.regimen_view.update_regimen_list()

    def delete_regimen(self, id_regimen):
        self.regimen_model.delete_regimen(id_regimen)
        self.regimen_view.update_regimen_list()

    def list_all_regimen(self):
        return self.regimen_model.list_all_regimenes()
