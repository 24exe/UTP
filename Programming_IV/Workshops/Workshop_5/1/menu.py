'''
Programación IV
Grupo: 1
Profesor: Andrés Felipe Ramírez Correa
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Herencia múltiple.


TALLER 5

Para el siguiente grafico diseñe un algoritmo implementando herencia
múltiple:
    a. Para cada clase debe diseñar al menos 6 atributos.
    b. Para las clases profesor debe realizar un método en donde se pueda
    calcular el sueldo mensual dependiendo de las horas que trabaja y del
    tipo de profesor que sea
    c. Debe de crear un método para calcular la antigüedad de todas las
    entidades en el diseño.
    d. Dependiendo de cada tipo de profesor debe diseñar al menos tres
    materias acordes con el rango de cada uno y se deben visualizar en
    pantalla por medio de un método.
    e. Guarde la información que crea necesaria en un archivo para este
    programa.
'''





'''
MODULO 4
'''

from unittest import case
from ProfesorAyudante import Profesor_Ayudante
from AlumnoYProfesor import Estudiante, Profesor
from datetime import * 
import json
import os
from io import *

Lista_Personal_Universitario: list[Estudiante | Profesor | Profesor_Ayudante] = []

def guardar_en_archivo_json():
    ruta_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo = os.path.join(ruta_actual, "datos_personal_universitario.json")
    with open(ruta_archivo, "w") as archivo:
        json.dump([objeto.__dict__ for objeto in Lista_Personal_Universitario], archivo)

def cargar_desde_archivo_json():
    ruta_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo = os.path.join(ruta_actual, "datos_personal_universitario.json")
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, "r") as archivo:
            datos = json.load(archivo)
            for item in datos:
                if 'carrera' in item:
                    objeto = Estudiante(**item)
                elif 'tipo' in item:
                    objeto = Profesor(**item)
                else:
                    objeto = Profesor_Ayudante(**item)
                Lista_Personal_Universitario.append(objeto)

def input_int(mensaje: str) -> int:
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: Ingresa un numero entero valido.")

def input_str(mensaje: str) -> str:
    while True:
        try:
            return str(input(mensaje))
        except ValueError:
            print("Error: Ingresa un texto valido.")

def buscar_personal_universitario(documento: str) -> Estudiante | Profesor | Profesor_Ayudante:
    for Persona in Lista_Personal_Universitario:
        if Persona.documento == documento:
            print(Persona)
            return Persona
    print("No se encontró la persona con el documento proporcionado.")


def menu():
    cargar_desde_archivo_json()
    while True:
        print("\n--- Menu de Gestion Universitaria ---")
        print("1. Menu Estudiante")
        print("2. Menu Profesor")
        print("3. Menu Profesor Ayudante")
        print("4. Mostrar Personal Universitario")
        print("5. Guardar")
        print("6. Cargar")
        print("7. Salir")
        opcion = input_int("Seleccione una opcion: ")



def menu_estudiante():    
    while True:
        print("\n--- Menu Estudiante ---")
        print("1. Agregar Estudiante")
        print("2. Agregar Materia")
        print("3. Cancelar Materia")
        print("4. Volver al Menu Principal")
        opcion = input_int("Seleccione una opcion: ")
        match opcion:
            case 1:
                nombre = input_str("Ingrese el nombre del estudiante: ")
                edad = input_int("Ingrese la edad del estudiante: ")
                genero = input_str("Ingrese el genero del estudiante: ")
                documento = input_str("Ingrese el documento del estudiante: ")
                direccion = input_str("Ingrese la direccion del estudiante: ")
                telefono = input_str("Ingrese el telefono del estudiante: ")
                fecha_ingreso = input_str("Ingrese la fecha de ingreso (YYYY-MM-DD): ")
                carrera = input_str("Ingrese la carrera del estudiante: ")
                semestre = input_int("Ingrese el semestre del estudiante: ")
                
                estudiante = Estudiante(nombre, edad, genero, documento, direccion, telefono, fecha_ingreso, carrera, semestre)
                Lista_Personal_Universitario.append(estudiante)
                pass
            case 2:
                # Lógica para agregar materia
                pass
            case 3:
                # Lógica para cancelar materia
                pass
            case 4:
                break
        opcion = input_int("Seleccione una opcion: ")
 
'''
        if opcion == 1:

            print("Estudiante agregado exitosamente.")
            inscribir = input_str("Desea inscribir materias ahora? (S/N) ")
            if inscribir.lower() == 's':
                num_materias = input_int("¿Cuántas materias desea inscribir? ")
                for _ in range(num_materias):
                    materia = input_str("Ingrese el nombre de la materia: ")
                    estudiante.inscribir_materia(materia)
                print("Materias inscritas exitosamente.")
            else :
                print("No se inscribieron materias.")


        if opcion == 2:
            nombre = input_str("Ingrese el nombre del profesor: ")
            edad = input_int("Ingrese la edad del profesor: ")
            id_profesor = input_str("Ingrese el ID del profesor: ")
            tipo = input_str("Ingrese el tipo de profesor (Titular/Adjunto): ")
            horas_trabajadas = input_int("Ingrese las horas trabajadas: ")
            fecha_ingreso = input_str("Ingrese la fecha de ingreso (YYYY-MM-DD): ")
            profesor = Profesor(nombre, edad, id_profesor, tipo, horas_trabajadas, fecha_ingreso)
            Lista_Personal_Universitario.append(profesor)
            print("Profesor agregado exitosamente.")

        if opcion == 3:
            nombre = input_str("Ingrese el nombre del profesor ayudante: ")
            edad = input_int("Ingrese la edad del profesor ayudante: ")
            id_profesor_ayudante = input_str("Ingrese el ID del profesor ayudante: ")
            horas_trabajadas = input_int("Ingrese las horas trabajadas: ")
            fecha_ingreso = input_str("Ingrese la fecha de ingreso (YYYY-MM-DD): ")
            profesor_ayudante = Profesor_Ayudante(nombre, edad, id_profesor_ayudante, horas_trabajadas, fecha_ingreso)
            Lista_Personal_Universitario.append(profesor_ayudante)
'''