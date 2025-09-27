'''
Programación IV
Grupo: 1
Profesor: Andrés Felipe Ramírez Correa
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Herencia simple y polimorfismo.


TALLER 4

    Realice un programa en el que podamos observar los atributos de las clases
    inspiradas en el siguiente gráfico, se debe implementar herencia simple y se
    deben guardar la información de cada vehículo en uno o varios archivos para
    poder listarlos cuando se necesiten, el programa también debe contar con los
    siguientes métodos:

        - Métodos Vehículo:
            a. Debe mostrar información dependiendo del vehículo (camión, moto,
            automóvil) de cuantos años aproximadamente le pueden durar las llantas esto
            también sujeto a tres tipos de marcas.
            b. tipo de combustible que se recomienda usar para el vehículo que se elija (ACPM, Extra, Corriente).

        - Métodos Coche:
        a. Mostrar que tiempo se tomaría cada vehículo en llegar desde Pereira a
        diferentes lugares en Colombia (mínimo 5 lugares).
        b. debe mostrar cuanto gastaría al mes en combustible cada automóvil
        suponiendo que cada uno hace viajes de 1000 km mensuales, ustedes pueden
        consultar precios actuales para parametrizar el combustible.
'''


from io import *
import os

#----------------------------------------------------------------------

class Vehiculo:

    def __init__(self, color: str, ruedas: int, marca_de_llantas: str):
        self.color: str = color
        self.ruedas: int = ruedas
        self.marca_de_llantas: str = marca_de_llantas 

    def __str__(self):
        return f"Color: {self.color}, Ruedas: {self.ruedas}, Marca de Llantas: {self.marca_de_llantas} "
    
    def duracion_llantas(self):
        """ Duración estimada de las llantas en Km."""

        marca_de_llantas: dict = {# Marca : Kilometros de esa marca
            "Michellin" : 50000,
            "Goodyear": 40000,
            "Barum": 30000
        }
        return marca_de_llantas.get(self.marca_de_llantas, 25000) # Si no esta en el diccionario, retorna 25000 Km de duración (predeterminada)
    def combustible_recomendado(self):
        """ Recomendación general (se redefine en subclases)"""

        return "Combustible Estandar"
    
#----------------------------------------------------------------------

class Coche(Vehiculo):

    def __init__(self, color: str, marca_de_llantas: str, cc: int, vel_max: int):
        ruedas: int = 4
        super().__init__(color, ruedas, marca_de_llantas)
        
        self.cc: int = cc
        self.vel_max: int = vel_max
        self.combustible: str = self.combustible_recomendado()
        lista_vehiculos.append(self)

    def combustible_recomendado(self)-> str:
        """ Retorna el combustible correspondiente a cada cilindrada"""
        if self.cc >= 2000:
            return "Extra"
        return "Corriente"
    
    def tiempo_de_viaje(self, ciudad: str):
        """ Retorna el tiempo estimado de viaje desde Pereira a la ciudad dada una velocidad máxima."""
        if ciudad in ciudades:
            destino_distancia = ciudades.get(ciudad)
            return f"Tiempo de viaje desde Pereira hasta {ciudad} a max. velocidad: {destino_distancia / self.vel_max} h\n"
        return "-- DESTINO NO ENCONTRADO --\n"
    
    def __str__(self):
        return super().__str__() + f"Tipo: Coche, CC: {self.cc}, Velocidad Máxima: {self.vel_max}"

#----------------------------------------------------------------------

class Moto(Vehiculo):

    def __init__(self, color: str, marca_de_llantas: str, cc: int, vel_max: int):
        ruedas: int = 2
        super().__init__(color, ruedas, marca_de_llantas)
        
        self.cc: int = cc
        self.vel_max: int = vel_max
        self.combustible: str = self.combustible_recomendado()
        lista_vehiculos.append(self)

    def combustible_recomendado(self)-> str:
        """ Retorna el combustible correspondiente a cada cilindrada"""
        if self.cc >= 200:
            return "Extra"
        return "Corriente"
    
    def tiempo_de_viaje(self, ciudad: str):
        """ Retorna el tiempo estimado de viaje desde Pereira a la ciudad dada una velocidad máxima."""
        if ciudad in ciudades:
            destino_distancia = ciudades.get(ciudad)
            return f"Tiempo de viaje desde Pereira hasta {ciudad} a max. velocidad: {destino_distancia / self.vel_max} h\n"
        return "-- DESTINO NO ENCONTRADO --\n"
    
    def __str__(self):
        return super().__str__() + f"Tipo: Moto, CC: {self.cc}, Velocidad Máxima: {self.vel_max}"

#----------------------------------------------------------------------

class Camion(Vehiculo):
    def __init__(self, color: str, marca_de_llantas: str, toneladas: int, vel_max: int):
        ruedas: int = 6
        super().__init__(color, ruedas, marca_de_llantas)
        
        self.toneladas: int = toneladas
        self.vel_max: int = vel_max
        self.combustible: str = self.combustible_recomendado()
        lista_vehiculos.append(self)

    def combustible_recomendado(self)-> str:
        """ Retorna el combustible correspondiente a cada tonelada"""
        if self.toneladas >= 10:
            return "ACPM"
        return "Extra"
    
    def tiempo_de_viaje(self, ciudad: str):
        """ Retorna el tiempo estimado de viaje desde Pereira a la ciudad dada una velocidad máxima."""
        if ciudad in ciudades:
            destino_distancia = ciudades.get(ciudad)
            return f"Tiempo de viaje desde Pereira hasta {ciudad} a max. velocidad: {destino_distancia / self.vel_max} h\n"
        return "-- DESTINO NO ENCONTRADO --\n"
    
    def __str__(self):
        return super().__str__() + f"Tipo: Camión, Toneladas: {self.toneladas}, Velocidad Máxima: {self.vel_max}"
#----------------------------------------------------------------------

def guardar_vehiculos_en_archivo():
    """ Guarda la información de los vehículos en un archivo de texto."""
    ruta_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo = os.path.join(ruta_actual, "vehiculos.txt")
    with open(ruta_archivo, "w", encoding="utf-8") as f:
        for vehiculo in lista_vehiculos:
            f.write(str(vehiculo) + "\n")






#----------------------------------------------------------------------
ciudades: dict = {
    "Medellin": 241,
    "Cali": 209,
    "Bogotá": 307,
    "Cartagena": 943,
    "Manizales": 53,
}

lista_vehiculos: list[Coche] = []


def ejemplo_de_uso():
    coche1 = Coche("Rojo", "Michellin", 1600, 180)
    coche2 = Coche("Azul", "Goodyear", 2000, 200)
    coche3 = Coche("Verde", "Barum", 1400, 160)

    print(coche1)
    print(f"Combustible recomendado: {coche1.combustible_recomendado()}")
    print(f"Duración estimada de llantas: {coche1.duracion_llantas()} Km")
    print(coche1.tiempo_de_viaje("Medellin"))
    print(coche2)
    print(f"Combustible recomendado: {coche2.combustible_recomendado()}")
    print(f"Duración estimada de llantas: {coche2.duracion_llantas()} Km")
    print(coche2.tiempo_de_viaje("Cali"))
    print(coche3)
    print(f"Combustible recomendado: {coche3.combustible_recomendado()}")
    print(f"Duración estimada de llantas: {coche3.duracion_llantas()} Km")
    print(coche3.tiempo_de_viaje("Bogotá"))

    moto1 = Moto("Negro", "Michellin", 150, 160)
    moto2 = Moto("Blanco", "Goodyear", 250, 180)
    print(moto1)
    print(f"Combustible recomendado: {moto1.combustible_recomendado()}")
    print(f"Duración estimada de llantas: {moto1.duracion_llantas()} Km")
    print(moto1.tiempo_de_viaje("Manizales"))
    print(moto2)
    print(f"Combustible recomendado: {moto2.combustible_recomendado()}")
    print(f"Duración estimada de llantas: {moto2.duracion_llantas()} Km")
    print(moto2.tiempo_de_viaje("Cartagena"))

    camion1 = Camion("Amarillo", "Barum", 8, 120)
    camion2 = Camion("Gris", "Michellin", 12, 100)
    print(camion1)
    print(f"Combustible recomendado: {camion1.combustible_recomendado()}")
    print(f"Duración estimada de llantas: {camion1.duracion_llantas()} Km")
    print(camion1.tiempo_de_viaje("Medellin"))
    print(camion2)
    print(f"Combustible recomendado: {camion2.combustible_recomendado()}")
    print(f"Duración estimada de llantas: {camion2.duracion_llantas()} Km")
    print(camion2.tiempo_de_viaje("Cali"))

    guardar_vehiculos_en_archivo()



ejemplo_de_uso()