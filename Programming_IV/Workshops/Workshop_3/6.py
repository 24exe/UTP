
'''
Programación IV
Grupo: 1
Profesor: Andrés Felipe Ramírez Correa
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Constructores, Destructores y Métodos


TALLER 3

6. Implemente una clase `NotaMusical` con atributos como nombre, frecuencia y
duración. Guarde en un archivo las notas mayores a cierta frecuencia. Añada un
método que simule la ejecución de la nota (texto).
'''
from io import *
import os

class NotaMusical():
    notas = []      # Atributo de clase

    def __init__(self, nombre: str, frecuencia: float ,duracion: float):
        self.nombre: str = nombre
        self.frecuencia: float = frecuencia
        self.duracion: float = duracion

        NotaMusical.notas.append(self)

    def reproducir(self):
        print(f"Sonando {self.nombre} a {self.frecuencia}Hz durante {self.duracion}s\n")


    @classmethod
    def guardar_en_archivo(cls, frecuencia_minima: float):
        ruta_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_archivo = os.path.join(ruta_actual, "notas_filtradas.txt")
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            archivo.write(f"Frecuencia Minima: {frecuencia_minima}Hz \n\n")
            archivo.write("Nombre|Frecuencia|Duración\n")
            for nota in NotaMusical.notas:
                if nota.frecuencia > frecuencia_minima:
                    archivo.write(f"{nota.nombre}|{nota.frecuencia}|{nota.duracion}\n")
        print("Revisar 'notas_filtradas.txt'\n")


# Ejemplo de uso
def example():
    n1 = NotaMusical("Do", 261.63, 1)
    n2 = NotaMusical("Re", 278.3, 1)
    n3 = NotaMusical("Si#", 280.4, 0.5)
    n4 = NotaMusical("Sol", 350.8, 3)
    
    n1.reproducir()
    n2.reproducir()
    n3.reproducir()
    n4.reproducir()

    NotaMusical.guardar_en_archivo(280)


# FUN. PRINCIPAL
def main():
    example()

main()
