from abc import ABC, abstractmethod

class Registrable(ABC):
    @abstractmethod
    def registrar(self) -> str:
        pass



class Agendable(ABC):
    @abstractmethod
    def agendar_cita(self, cita):
        pass
