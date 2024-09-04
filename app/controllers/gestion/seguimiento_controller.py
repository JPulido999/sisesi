from app.views.gestion.accion_view import AccionView
from app.models.gestion_model.accion_model import AccionModel

class AccionController:
    def __init__(self):
        self.accion_view = None
        self.accion_model = AccionModel()

    def show_view(self):
        if not self.accion_view or not self.accion_view.winfo_exists():
            self.accion_view = AccionView(self)
            self.accion_view.update_accion_list()
        self.accion_view.grab_set()

    ################################ LLAMADA A METODOS DE LOS BOTONES ##############################

    def create_accion(self, dia_accion, horaInicio_accion, horaFin_accion, ambiente_accion, numAlumnos_accion, id_tipoActividad, id_semana, id_docente):
        self.accion_model.create_accion(dia_accion, horaInicio_accion, horaFin_accion, ambiente_accion, numAlumnos_accion, id_tipoActividad, id_semana, id_docente)
        self.accion_view.update_accion_list()

    def read_accion(self, id_accion):
        return self.accion_model.read_accion(id_accion)

    def update_accion(self, id_accion, dia_accion, horaInicio_accion, horaFin_accion, ambiente_accion, numAlumnos_accion, id_tipoActividad, id_semana, id_docente):
        self.accion_model.update_accion(id_accion, dia_accion, horaInicio_accion, horaFin_accion, ambiente_accion, numAlumnos_accion, id_tipoActividad, id_semana, id_docente)
        self.accion_view.update_accion_list()

    def delete_accion(self, id_accion):
        self.accion_model.delete_accion(id_accion)
        self.accion_view.update_accion_list()

    def list_all_accion(self):
        return self.accion_model.list_all_acciones()
