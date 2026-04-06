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
MODULO 3
'''

from Base import ServicioVeterinario, Animal
from Mascotas import *


class ConsultaGeneral(ServicioVeterinario):
    def __init__(self, nombre_servicio: str, direccion: str, telefono: str, duracion_consulta: int, precio: float):
        super().__init__(nombre_servicio, direccion, telefono)
        self.duracion_consulta: int = duracion_consulta  # en minutos
        self.precio: float = precio

    def realizar_consulta(self, animal: Animal) -> str:
        return f"Consulta general realizada para {animal.nombre}. Duración: {self.duracion_consulta} minutos. Precio: ${self.precio}.\n"
    

class Vacunacion(ServicioVeterinario):
    def __init__(self, nombre_servicio: str, direccion: str, telefono: str, precio_vacuna: float):
        super().__init__(nombre_servicio, direccion, telefono)