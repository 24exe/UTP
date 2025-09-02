'''
Programación IV
Grupo: 1
Profesor: Andrés Felipe Ramírez Correa
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Archivos, clases y objetos.


TALLER 2


6. Animales y edades
- Crea una clase `Animal` con atributos: especie, nombre, edad.
- Genere una lista de animales.
- Implementa un método que calcule el promedio de edades.
- Guarda y lee el archivo `animales.txt` mostrando los animales que superan la edad promedio.
'''
from io import *
import os

class Animal:
    numAnimales: int = 0
    especie: str
    nombre: str
    edad: int


    def InsertData(self):
        while True:
            try:
                espAux = str(input("¿A qué especie pertenece el animal?: "))
                self.especie = espAux
                break
            except ValueError:
                print("ERROR, TIPO DE DATO INGRESADO INCORRECTO. \n")
        while True:
            try:
                nameAux = str(input("¿Cual es el nombre del animal?: "))
                self.nombre = nameAux
                break
            except ValueError:
                print("ERROR, TIPO DE DATO INCORRECTO")
        while True:
            try:
                edadAux = int(input("Edad del animal: "))
                if edadAux > 0:
                    self.edad = edadAux
                    break
                else:
                    print("ERROR, LA EDAD DEBE SER UN NÚMERO ENTERO POSITIVO")
            except ValueError:
                print("ERROR, INGRESE UN TIPO DE DATO NÚMERICO ENTERO POSITIVO")


    @staticmethod
    def PromAges(lista_animales: list)-> float:
        SumOfAges: int  = 0
        lista_edades:list[int] = []
        for animal in lista_animales:
            SumOfAges += animal.edad
        return SumOfAges / Animal.numAnimales
    

    @staticmethod
    def SaveInfo(lista_animales: list, promedio):
        animalsOverAverageAge = []
        ruta_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_archivo = os.path.join(ruta_actual, "animales.txt")

        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            archivo.write("----ANIMALES---\n\n")
            for animal in lista_animales:
                archivo.write(f"Especie: {animal.especie}, Nombre: {animal.nombre}, Edad: {animal.edad}\n")
            archivo.close()

        # Se lee el archivo para procesar los animales que sobrepasan la edad promedio.
        with open(ruta_archivo, "r") as archivo:
            for linea in archivo:
                partes = linea.split("Edad:")
                if len(partes) > 1:
                    try:
                        edad = int(partes[1].strip().replace(",", ""))
                        if edad > promedio:
                            animalsOverAverageAge.append(linea.strip())
                    except ValueError:
                        pass
        print("Animales que superan la edad promedio:\n")
        for animal in animalsOverAverageAge:
            print(animal)


#------------------------------------------

n: int
while True:
    try:    
        num = int(input("¿Cuantos animales desea Ingresar?: "))
        n = num
        break
    except (ValueError, TypeError):
        print("ERROR DE INSERCIÓN EN EL NÚMERO DE ANIMALES, SE DARA UN TAMAÑO DE 5 POR DEFECTO. \n")
        n = 5
        break

animales: list[Animal] = []
for i in range(n):
    print(f"Animal {i+1}: \n")
    animal = Animal()
    animal.InsertData()
    Animal.numAnimales += 1
    animales.append(animal)
    print("\n")

promedioEdad = Animal.PromAges(animales)
print(f"Número de animales {Animal.numAnimales}")
print(f"Edad promedio: {promedioEdad}\n")
Animal.SaveInfo(animales, promedioEdad)