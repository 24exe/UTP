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
MODULO 2
'''

from Base import Animal


class Perro(Animal):
    def __init__(self, nombre: str, edad: int, peso: float, dueño: str, raza: str, vacunado: bool = False):
        super().__init__(nombre, edad, peso, dueño)
        self.raza: str = raza
        self.vacunado: bool = vacunado

    def vacunar(self):
        if not self.vacunado:
            self.vacunado = True
            return f"{self.nombre} ha sido vacunado.\n"
        else:
            return f"{self.nombre} ya está vacunado.\n"

    def ladrar(self):
        return "¡Guau Guau!\n"
    
    def __str__(self):
        return super().__str__()
    
class Gato(Animal):
    def __init__(self, nombre: str, edad: int, peso: float, dueño: str, raza: str, esterilizado: bool = False):
        super().__init__(nombre, edad, peso, dueño)
        self.raza: str = raza
        self.esterilizado: bool = esterilizado

    def esterilizar(self):
        if not self.esterilizado:
            self.esterilizado = True
            return f"{self.nombre} ha sido esterilizado"
        else:
            return f"{self.nombre} ya esta esterilizado"
        
    def maullar(self):
        return "¡Miau Miau!\n"
    