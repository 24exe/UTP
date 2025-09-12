'''
Programación IV
Grupo: 1
Profesor: Andrés Felipe Ramírez Correa
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Constructores, Destructores y Métodos


TALLER 3

8. Cree una clase “Triangulo” donde me calcule área, perímetro y un método que me
diga que tipo de triangulo es.
'''

import math

class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimetro() / 2  # semiperímetro
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def tipo(self):
        if self.a == self.b == self.c:
            return "Equilátero"
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return "Isósceles"
        else:
            return "Escaleno"


def ejemplo_de_uso():
    # Ejemplo de uso
    t = Triangulo(3, 4, 5)
    print("Perímetro:", t.perimetro())
    print("Área:", t.area())
    print("Tipo:", t.tipo())

def main():
    ejemplo_de_uso()

main()

