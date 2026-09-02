'''
Modulo 1.2: Final_Project.Clinica.Models.Interfaces
Descripción: Este módulo define las Clases Base Agendable y Registrable
'''

from abc import ABC, abstractmethod

class Registrable(ABC):
    @abstractmethod
    def registrar_cita_medica(self) -> str:
        pass
    @abstractmethod
    def editar_cita_medica(self) -> str:
        pass
    @abstractmethod
    def eliminar_cita_medica(self) -> str:
        pass


class Agendable(ABC):
    @abstractmethod
    def agendar_a_paciente(self, cita):
        pass

