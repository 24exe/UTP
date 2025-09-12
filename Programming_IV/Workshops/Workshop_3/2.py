'''
Programación IV
Grupo: 1
Profesor: Andrés Felipe Ramírez Correa
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Constructores, Destructores y Métodos


TALLER 3

2. Diseñe una clase `Estudiante` con atributos como nombre, código, carrera, edad y
promedio. Implemente métodos para calcular si el estudiante aprueba (promedio >=
3.0), y guardar los datos en un archivo.
'''
from io import *
import os
# Clase Estudiante
class Estudiante:
    nombre: str
    int: str
    carrera: str
    edad: str
    promedio: float 

    def __init__(self, nombre, codigo, carrera, edad, promedio):
        self.nombre = nombre
        self.codigo = codigo
        self.carrera = carrera
        self.edad = edad
        self.promedio = promedio
    
    def aprueba(self):
        if self.promedio >= 3.0:
            print("APROBADO\n")
        else:
            print("REPROBADO")
    
    @staticmethod
    def guardar_Datos(estudiantes:'list[Estudiante]'):
        ruta_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_archivo = os.path.join(ruta_actual, "Lista_Estudiantes.txt")
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            for estudiante in estudiantes:
                archivo.write(f"{estudiante.nombre}|{estudiante.codigo}|{estudiante.carrera}|{estudiante.edad}|{estudiante.promedio}|")
                if estudiante.promedio >= 3:
                    archivo.write("APROBADO\n")
                else:
                    archivo.write("REPROBADO\n")

def insert_Data()-> Estudiante:
    while True:
        try:
            nombre = str(input("Nombre: "))
            break        
        except ValueError:
            print("ERROR EN EL TIPO DE DATO")
    while True:
        try:
            codigo = int(input("Código: "))
            if codigo in codigos_usados:
                print("ERROR, CÓDIGO YA USADO\n")
            else:
                codigos_usados.add(codigo)
                break        
        except ValueError:
            print("ERROR EN EL TIPO DE DATO")
    while True:
        try:
            carrera = str(input("Carrera: "))
            break        
        except ValueError:
            print("ERROR EN EL TIPO DE DATO")
    while True:
        try:
            edad = str(input("Edad: "))
            break        
        except ValueError:
            print("ERROR EN EL TIPO DE DATO")
    while True:
        try:
            promedio = float(input("Promedio: "))
            break        
        except ValueError:
            print("ERROR EN EL TIPO DE DATO")

    x = Estudiante(nombre, codigo, carrera, edad, promedio)
    return x

Estudiantes: list[Estudiante] = []
codigos_usados = set()

def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Crear Estudiante")
        print("2. Guardar en Archivo")
        print("3. Salir")

        opcion = int(input("Ingrese una opción [1-3]: "))
        match opcion:
            case 1:
                x = insert_Data()
                Estudiantes.append(x)
                x.aprueba()
                print("--ESTUDIANTE CREADO--\n")
            case 2:
                print("--LISTA DE ESTUDIANTES ACTUALIZADA--\n")
                Estudiante.guardar_Datos(Estudiantes)
                print("--REVISAR 'Lista_Estudiantes.txt'--\n")
            case 3:
                print("QUE TENGA BUEN DIA")
                break
            case _:
                print("OPCION NO VALIDA")


# FUN. PRINCIPAL
def main():
    menu()

main()