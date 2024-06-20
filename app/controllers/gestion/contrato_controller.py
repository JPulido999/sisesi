from app.views.gestion.contrato_view import ContratoView
from app.models.gestion_model.contrato_model import ContratoModel

class ContratoController:
    def __init__(self):
        self.contrato_view = None
        self.contrato_model = ContratoModel()

    def show_view(self):
        if not self.contrato_view or not self.contrato_view.winfo_exists():
            self.contrato_view = ContratoView(self)
            self.contrato_view.update_contrato_list()
        self.contrato_view.grab_set()

    ################################ LLAMADA A METODOS DE LOS BOTONES ##############################

    def create_contrato(self, periodoInicio, periodoFin, id_docente, renacyt, id_condicion, id_regimen, id_categoria):
        self.contrato_model.create_contrato(periodoInicio, periodoFin, id_docente, renacyt, id_condicion, id_regimen, id_categoria)
        self.contrato_view.update_contrato_list()

    def read_contrato(self, id_contrato):
        return self.contrato_model.read_contrato(id_contrato)

    def update_contrato(self, id_contrato, periodoInicio, periodoFin, id_docente, renacyt, id_condicion, id_regimen, id_categoria):
        self.contrato_model.update_contrato(id_contrato, periodoInicio, periodoFin, id_docente, renacyt, id_condicion, id_regimen, id_categoria)
        self.contrato_view.update_contrato_list()

    def delete_contrato(self, id_contrato):
        self.contrato_model.delete_contrato(id_contrato)
        self.contrato_view.update_contrato_list()



    def list_all_contrato(self):
        return self.contrato_model.list_all_contrato()
    
    def buscar_contrato_por_docente(self, id_docente):
        return self.contrato_model.buscar_contrato_por_docente(id_docente)
