from persona import Persona
from interfaces import Registrable, Agendable


class Doctor(Persona, Registrable, Agendable):
    def __init__(self, nombre: str, documento: int, edad: int, genero: str = "No especificado", especialidad: str = "General"):
        super().__init__(nombre, documento, edad, genero)
        self._especialidad = especialidad

    @property
    def especialidad(self) -> str:
        return self._especialidad

    def registrar(self):
        print(f"Doctor {self.nombre} registrado.")

    def agendar_cita(self, cita):
        self.citas.append(cita)
