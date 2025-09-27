'''
Programación IV
Grupo: 1
Profesor: Andrés Felipe Ramírez Correa
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Herencia simple y polimorfismo.


TALLER 4

3. Define una clase base Figura con un método area().
Implementa subclases Rectangulo, Triangulo y Circulo que sobrescriban el método
area() con la fórmula correspondiente.
Crea objetos de cada clase y guarda sus áreas en una lista. Luego recórrela
mostrando qué tipo de figura es y cuánto mide su área.
'''
from math import pi

class Figura:
    lista_figuras = []
    def area(self):
        pass

    @classmethod
    def mostrar_areas(cls):
        for figura_actual in cls.lista_figuras:
            print(f"Figura: {figura_actual.__class__.__name__}, Área: {figura_actual.area()}")


class Rectangulo(Figura): 
    def __init__(self, base: float, altura: float):
        self.base: float = base
        self.altura: float = altura
        Figura.lista_figuras.append(self)

    def area(self) -> float:
        return self.base * self.altura


class Triangulo(Figura):
    def __init__(self, base: float, altura: float):
        self.base: float = base
        self.altura: float = altura
        Figura.lista_figuras.append(self)

    def area(self) -> float:
        return (self.base * self.altura) / 2 


class Circulo(Figura):
    radio: float

    def __init__(self, radio: float):
        self.radio: float = radio
        Figura.lista_figuras.append(self)

    def area(self) -> float:
        return pi * (self.radio ** 2)
    

def ejemplo_de_uso():
    r1 = Rectangulo(4, 5)
    r2 = Rectangulo(6, 7)
    t1 = Triangulo(4, 5)
    t2 = Triangulo(6, 7)
    c1 = Circulo(3)
    c2 = Circulo(4)

    Figura.mostrar_areas()

ejemplo_de_uso()