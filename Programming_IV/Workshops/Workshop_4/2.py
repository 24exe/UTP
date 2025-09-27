'''
Programación IV
Grupo: 1
Profesor: Andrés Felipe Ramírez Correa
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Herencia simple y polimorfismo.


TALLER 4
2. Haciendo uso el siguiente diagrama:

    Implemente:
        • Crea al menos un objeto de cada subclase y añádelos a una lista llamada vehículos.
        • Realiza una función llamada catalogar() que reciba la lista de vehículos y los recorra
            mostrando el nombre de su clase y sus atributos.
        • Modifica la función catalogar() para que reciba un argumento optativo ruedas,
            haciendo que muestre únicamente los que su número de ruedas concuerde con el
            valor del argumento. También debe mostrar un mensaje "Se han encontrado {}
            vehículos con {} ruedas:" únicamente si se envía el argumento ruedas. Ponla a
            prueba con 0, 2 y 4 ruedas como valor.
'''

class Vehiculo:

    def __init__(self, ruedas: int, color: str = "No Especificado"):
        self.ruedas: int = ruedas
        self.color: str = color

#----------------------------------------------------------------------

class Coche(Vehiculo):

    def __init__(self, velocidad: int, cc: int, color: str = "No Especificado"):
        ruedas: int = 4
        super().__init__(ruedas, color)
        self.velocidad: int = velocidad
        self.cc: int = cc
        lista_vehiculos.append(self)

    def __str__(self):
        return f"Tipo: {self.__class__.__name__}, Ruedas: 4, Color: {self.color}, CC: {self.cc}, Velocidad: {self.velocidad} Km/h"

#----------------------------------------------------------------------

class Camioneta(Coche):

    def __init__(self, velocidad: int, cc: int, carga: float, color: str = "No Especificado"):
        super().__init__(velocidad, cc, color)
        self.carga: float = carga

    def __str__(self):
        return super().__str__() + f", Carga: {self.carga} Toneladas"

#----------------------------------------------------------------------

class Bicicleta(Vehiculo):

    def __init__(self, color: str = "No Especificado", tipo: str = "No Especificado"):
        ruedas: int = 2
        super().__init__(ruedas, color)
        self.tipo: str = tipo
        lista_vehiculos.append(self)

    def __str__(self):
        return f"Tipo: {self.__class__.__name__}, Ruedas: 2, Color: {self.color}, Tipo de Bicicleta: {self.tipo}"
    
#----------------------------------------------------------------------

class Motocicleta(Bicicleta):

    def __init__(self, velocidad: int, cc: int, tipo: str = "No Especificado", color: str = "No Especificado"):
        super().__init__(color, tipo)
        self.velocidad: int = velocidad
        self.cc: int = cc
    
    def __str__(self):
        return super().__str__() + f", CC: {self.cc}, Velocidad: {self.velocidad} Km/h"

#----------------------------------------------------------------------

# AVISO: no use @classmethod ni @staticmethod ya que en el enunciado decia "función" y no "método", por ende lo tomo como una función.

'''
Primera versión de la función catalogar sin el parámetro opcional de ruedas.

def catalogar(lista_vehiculos: list[Vehiculo]):
    for vehiculo in lista_vehiculos:
        print(vehiculo)
'''

def catalogar(lista_vehiculos: list[Vehiculo], ruedas: int | None = None):
    if ruedas is not None:
        print(f"Se han encontrado {sum(1 for vehiculo in lista_vehiculos if vehiculo.ruedas == ruedas)} vehículos con {ruedas} ruedas:\n")
    else:
        print("Mostrando todos los vehículos:\n")
    for vehiculo in lista_vehiculos:
        if ruedas is None or vehiculo.ruedas == ruedas:
            print(vehiculo)
    print() 

#----------------------------------------------------------------------

lista_vehiculos: list[Vehiculo] = []

#----------------------------------------------------------------------

def ejemplo_de_uso():
    coche1 = Coche(180, 1600, "Rojo")
    coche2 = Coche(200, 2000, "Azul")
    camioneta1 = Camioneta(150, 2500, 2.5, "Blanco")
    bicicleta1 = Bicicleta("Verde", "Montaña")
    motocicleta1 = Motocicleta(120, 600, "Deportiva", "Negro")
    
    catalogar(lista_vehiculos)
    print("\n--- Filtrado por ruedas ---")
    catalogar(lista_vehiculos, 0)
    catalogar(lista_vehiculos, 2)
    catalogar(lista_vehiculos, 4)
    catalogar(lista_vehiculos) # Sin filtro
    print("\n--- Fin del ejemplo de uso ---")


ejemplo_de_uso()