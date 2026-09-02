from paciente import Paciente
from Final_Project.tests.doctor import Doctor
from cita import Cita

class Clinica:
    def __init__(self):
        self.pacientes: list[Paciente] = []
        self.doctores:list[Doctor] = []
        self.citas: list[Cita] = []

    def agregar_paciente(self, paciente: Paciente):
        self.pacientes.append(paciente)

    def agregar_doctor(self, doctor: Doctor):
        self.doctores.append(doctor)

    def agendar_cita(self, cita: Cita, paciente: Paciente, doctor: Doctor):
        self.citas.append(cita)
        doctor.agendar_cita(cita)