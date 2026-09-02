import copy
from persona import Persona
from interfaces import Registrable
from MongoDB import ingresar_dato



class Paciente(Persona, Registrable):
    def __init__(self, nombre: str, documento: int, edad: int, genero: str = "No especificado", historial_medico: str = "No se encontro historial medico"):
        super().__init__(nombre, documento, edad, genero)
        self._historial_medico: str = historial_medico

        # Guardar automáticamente en MongoDB
        self.guardar_en_db()


    @property
    def historial_medico(self) -> str:
         return self._historial_medico
        
    @historial_medico.setter
    def historial_medico(self, historial_medico: str):
        self._historial_medico = historial_medico

    def registrar(self) -> str:
        return f"Paciente {self.nombre} registrado"

    def clone(self):
        return copy.deepcopy(self)


    # GUARDAR EN MONGODB
    def guardar_en_db(self):
        data = {
            "id": self._id,
            "nombre": self._nombre,
            "documento": self._documento,
            "edad": self._edad,
            "genero": self._genero,
            "historial_medico": self._historial_medico
        }

        ingresar_dato("Pacientes", data)

    def __str__(self):
        return f"=========Información del Paciente=========\nNombre: {self.nombre}\nDocumento: {self.documento}\nID: {self.id}\nEdad: {self.edad}\nGénero: {self.genero}\nHistorial Médico: {self.historial_medico}\n========================================="
    


if __name__ == "__main__":
    paciente1 = Paciente("Carlos", 11223344, 40, "Masculino", "No alergias conocidas")
    print(paciente1)
    paciente2 = paciente1.clone()
    paciente2.nombre = "Luis"
    paciente2.documento = 44332211
    paciente2.historial_medico = "Alergia a la penicilina"
    paciente2.edad = 35
    print(paciente2)
    print(paciente1.registrar())