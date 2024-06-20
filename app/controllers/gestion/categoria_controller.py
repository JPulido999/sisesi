from app.views.categoria_view import CategoriaView
from app.models.gestion_model.categoria_model import CategoriaModel

class CategoriaController:
    def __init__(self):
        self.categoria_view = None
        self.categoria_model = CategoriaModel()

    def show_view(self):
        if not self.categoria_view or not self.categoria_view.winfo_exists():
            self.categoria_view = CategoriaView(self)
            self.categoria_view.update_categoria_list()
        self.categoria_view.grab_set()

    ################################ LLAMADA A METODOS DE LOS BOTONES ##############################

    def create_categoria(self, nombre_categoria):
        self.categoria_model.create_categoria(nombre_categoria)
        self.categoria_view.update_categoria_list()

    def read_categoria(self, id_categoria):
        return self.categoria_model.read_categoria(id_categoria)

    def update_categoria(self, id_categoria, nombre_categoria):
        self.categoria_model.update_categoria(id_categoria, nombre_categoria)
        self.categoria_view.update_categoria_list()

    def delete_categoria(self, id_categoria):
        self.categoria_model.delete_categoria(id_categoria)
        self.categoria_view.update_categoria_list()

    def list_all_categoria(self):
        return self.categoria_model.list_all_categorias()
