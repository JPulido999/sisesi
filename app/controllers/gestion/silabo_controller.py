from app.views.silabo_view import SilaboView
from app.models.gestion_model.silabo_model import SilaboModel

class SilaboController:
    def __init__(self):
        self.silabo_view = None
        self.silabo_model = SilaboModel()

    def show_view(self):
        if not self.silabo_view or not self.silabo_view.winfo_exists():
            self.silabo_view = SilaboView(self)
            self.silabo_view.update_silabo_list()
        self.silabo_view.grab_set()

    ################################ LLAMADA A METODOS DE LOS BOTONES ##############################

    def create_silabo(self, id_asignatura, id_semestre, rutaArchivo_sil):
        self.silabo_model.create_silabo(id_asignatura, id_semestre, rutaArchivo_sil)
        self.silabo_view.update_silabo_list()

    def read_silabo(self, id_sil):
        return self.silabo_model.read_silabo(id_sil)

    def update_silabo(self, id_sil, id_asignatura, id_semestre, rutaArchivo_sil):
        self.silabo_model.update_silabo(id_sil, id_asignatura, id_semestre, rutaArchivo_sil)
        self.silabo_view.update_silabo_list()

    def delete_silabo(self, id_sil):
        self.silabo_model.delete_silabo(id_sil)
        self.silabo_view.update_silabo_list()

    def list_all_silabo(self):
        return self.silabo_model.list_all_silabos()
