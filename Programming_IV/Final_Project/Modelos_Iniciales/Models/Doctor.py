'''
Modulo 1.3: Final_Project.Clinica.Models.Pacientes
Descripción: Este módulo define la clase Pacientes
'''

from datetime import datetime
from Final_Project.Clinica.Models.Persona import Persona
from Final_Project.Clinica.Models.Interfaces import Registrable, Agendable
from Final_Project.Clinica.Models.Pacientes import Paciente

import random
import string


def licencia(longitud: int = 5) -> str:
    """Genera un número de licencia único compuesto por letras mayúsculas y dígitos."""
    caracteres = string.digits
    codigo = "LIC" + "".join(random.choices(caracteres, k=longitud))
    return codigo


class Doctor(Persona, Registrable, Agendable):
    def __init__(self, nombre: str, edad: int, genero: str = "No especificado", especialidad: str = "Medico General"):
        super().__init__(nombre, edad, genero)
        self._especialidad: str = especialidad
        self._numero_licencia: str = licencia()
        self._agenda_doctor: dict[datetime, Paciente] = {}

    @property
    def especialidad(self) -> str:
        return self._especialidad

    @property
    def numero_licencia(self) -> str:
        return self._numero_licencia

    @property
    def agenda_doctor(self) -> dict[datetime, Paciente]:
        return self._agenda_doctor
    
    @especialidad.setter
    def especialidad(self, especialidad: str):
        self._especialidad = especialidad
    
    @numero_licencia.setter
    def numero_licencia(self, numero_licencia: str):
        self._numero_licencia = numero_licencia
    
    def agendar_a_paciente(self, fecha: datetime, paciente: Paciente) -> str:
        """Agrega una cita al diccionario de agenda del doctor."""
        if fecha in self._agenda_doctor:
            return "Error: Ya hay una cita agendada para esa fecha y hora."
        self._agenda_doctor[fecha] = paciente
        return "Cita agendada exitosamente."
    
    def registrar_cita_medica(self) -> str:
        return "Cita médica registrada."