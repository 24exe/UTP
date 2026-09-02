'''
Modulo 1.2: Final_Project.Clinica.Models.Cita
Descripción: Este módulo define la clase Base Cita
'''
from datetime import datetime

class Cita:
    def __init__(self, doctor: str, doctor_id: str, paciente: str , paciente_id: str, fecha: str|datetime = "No especificada"):
        self._nombre_Doctor: str = doctor
        self._id_doctor: str = doctor_id
        self._nombre_Paciente: str = paciente
        self._id_paciente: str = paciente_id
        self._fecha: str = fecha
    
    # Getters
    @property
    def nombre_doctor(self) -> str:
        return self._nombre_Doctor
    
    @property
    def id_doctor(self) -> str:
        return self._id_doctor
    
    @property
    def nombre_paciente(self) -> str:
        return self._nombre_Paciente
    
    @property
    def id_paciente(self) -> str:
        return self._id_paciente
    
    @property
    def fecha(self) -> str:
        return self._fecha
    
    # Setters
    @nombre_doctor.setter
    def nombre_doctor(self, nombre_doctor: str):
        self._nombre_Doctor = nombre_doctor
    
    @id_doctor.setter
    def id_doctor(self, id_doctor: str):
        self._id_doctor = id_doctor
    
    @nombre_paciente.setter
    def nombre_paciente(self, nombre_paciente: str):
        self._nombre_Paciente = nombre_paciente

    @id_paciente.setter
    def id_paciente(self, id_paciente: str):
        self._id_paciente = id_paciente
    
    @fecha.setter
    def fecha(self, fecha: str):
        self._fecha = fecha


    def __str__(self):
        return f"---Información de la Cita Médica ---\nDoctor: {self.nombre_doctor}\nID: {self.id_doctor}\nPaciente: {self.nombre_paciente}\nID: {self.id_paciente}\nFecha: {self.fecha}"
    

if __name__ == "__main__":
    cita_ejemplo = Cita("Dr. Juan Perez", "LIC12345", "Ana Gomez", "PAC67890")
    print(cita_ejemplo)