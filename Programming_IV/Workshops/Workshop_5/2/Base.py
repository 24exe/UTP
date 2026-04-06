'''
Programación IV
Grupo: 1
Profesor: Andrés Felipe Ramírez Correa
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Herencia múltiple.


TALLER 5

2. Diseñe y modele un problema de cotidianidad con herencia múltiple,
implementando las siguientes características:
a. Debe tener al menos dos clases principales.
b. Debe tener al menos 5 subclases.
c. Las clases principales deben tener cada una al menos 5 atributos.
d. Entre todas las clases principales y subclases deben diseñar al menos 7
métodos.
e. Se debe crear una lista para almacenar los objetos creados para probar
las clases y subclases.

f. Guarde la información que crea necesaria en un archivo para este
programa.
'''

'''
MODULO 1
'''
from datetime import *

class Animal():
    def __init__(self, nombre: str, edad: int, peso: float, dueño: str):
        self.nombre: str = nombre
        self.edad: int = edad
        self.peso: float = peso
        self.dueño: str = dueño
    def __str__(self):
        print("=========================================\n")
        print(f"Nombre: {Animal.nombre}")
        print(f"Edad: {Animal.edad}")


class ServicioVeterinario():
    def __init__(self, nombre_servicio: str, direccion: str, telefono: str):
        self.nombre_servicio: str = nombre_servicio
        self.direccion: str = direccion
        self.telefono: str = telefono
    
    def convertir_a_fecha(self, fecha: date | str) -> date:
        '''
        Convierte una cadena en formato "YYYY-MM-DD" a un objeto date.
        Si ya es un objeto date, lo retorna tal cual.
        '''
        if isinstance(fecha, str):
            return datetime.strptime(fecha.strip(), "%Y-%m-%d").date()
        return fecha

    def agendar_cita(self, animal: Animal, fecha: date | str) -> str:
        return f"Cita agendada para {animal.nombre} el día {fecha} en {self.nombre_servicio}.\n"
    


