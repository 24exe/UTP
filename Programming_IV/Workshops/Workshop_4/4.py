'''
Programación IV
Grupo: 1
Profesor: Andrés Felipe Ramírez Correa
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Herencia simple y polimorfismo.


TALLER 4

4. Crea una clase base Transporte con atributos capacidad y tarifa.
Subclases: Bus, Taxi y Metro, cada una sobrescribe un método
calcular_pasaje(km) que determine el costo según la distancia recorrida.
Ejemplo:
Bus: tarifa fija + (100 * km)
Taxi: (500 * km)
Metro: tarifa fija sin importar los km
Crea varios transportes y muestra el costo de un trayecto de 10 km para cada uno
usando polimorfismo.
'''

class Transporte:
    def __init__(self, capacidad: int, tarifa: float):
        self.capacidad: int = capacidad
        self.tarifa: float = tarifa

    def calcular_pasaje(self, km: float) -> float:
        pass

class Bus(Transporte):
    def __init__(self, capacidad: int, tarifa: float):
        super().__init__(capacidad, tarifa)

    def calcular_pasaje(self, km: float) -> float:
        return self.tarifa + (100 * km)

class Taxi(Transporte):
    def __init__(self, capacidad: int, tarifa: float):
        super().__init__(capacidad, tarifa)

    def calcular_pasaje(self, km: float) -> float:
        return 500 * km

class Metro(Transporte):
    def __init__(self, capacidad: int, tarifa: float):
        super().__init__(capacidad, tarifa)

    def calcular_pasaje(self, km: float) -> float:
        return self.tarifa 


def ejemplo_de_uso():
    transporte1 = Bus(50, 2000)
    transporte2 = Taxi(4, 0)
    transporte3 = Metro(200, 2500)

    lista_transporte = [transporte1, transporte2, transporte3]

    for transporte in lista_transporte:
        print(f"Transporte: {transporte.__class__.__name__}, Costo por 10 km: {transporte.calcular_pasaje(10)}")


ejemplo_de_uso()