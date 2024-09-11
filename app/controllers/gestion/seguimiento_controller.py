from app.views.gestion.seguimiento_view import SeguimientoView
from app.models.gestion_model.seguimiento_model import SeguimientoModel

class SeguimientoController:
    def __init__(self):
        self.seguimiento_view = None
        self.seguimiento_model = SeguimientoModel()

    def show_view(self):
        if not self.seguimiento_view or not self.seguimiento_view.winfo_exists():
            self.seguimiento_view = SeguimientoView(self)
            self.seguimiento_view.update_seguimiento_list()
        self.seguimiento_view.grab_set()

    ################################ LLAMADA A METODOS DE LOS BOTONES ##############################

    def create_seguimiento(self, dia_accion, horaInicio_accion, horaFin_accion, ambiente_accion, numAlumnos_accion, id_tipoActividad, id_semana, id_docente):
        self.seguimiento_model.create_accion(dia_accion, horaInicio_accion, horaFin_accion, ambiente_accion, numAlumnos_accion, id_tipoActividad, id_semana, id_docente)
        self.seguimiento_view.update_seguimiento_list()

    def read_seguimiento(self, id_accion):
        return self.seguimiento_model.read_seguimiento(id_accion)

    def update_seguimiento(self, id_accion, dia_accion, horaInicio_accion, horaFin_accion, ambiente_accion, numAlumnos_accion, id_tipoActividad, id_semana, id_docente):
        self.seguimiento_model.update_seguimiento(id_accion, dia_accion, horaInicio_accion, horaFin_accion, ambiente_accion, numAlumnos_accion, id_tipoActividad, id_semana, id_docente)
        self.seguimiento_view.update_seguimiento_list()

    def delete_seguimiento(self, id_accion):
        self.seguimiento_model.delete_seguimiento(id_accion)
        self.seguimiento_view.update_seguimiento_list()

    def list_all_seguimiento(self):
        return self.seguimiento_model.list_all_seguimientos()
