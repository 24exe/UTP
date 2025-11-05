from libreria import Libreria
from libros import Libro
import os
import json


def menu():
    Libreria_1 = Libreria()
    while True:
        print("\n--Menú de la Librería--")
        print("1. Agregar libro")
        print("2. Mostrar libros")
        print("3. Filtrar libros por autor")
        print("4. Guardar libros en archivo JSON")
        print("5. Cargar libros desde archivo JSON")
        print("6. Salir")
        
        opcion = input_int("Ingrese una opción [1-6]: ")

        match opcion:
            case 1:
                titulo = input_str("Ingrese el título del libro: ")
                autor = input_str("Ingrese el autor del libro: ")
                year = input_int("Ingrese el año de publicación: ")
                editorial = input_str("Ingrese la editorial del libro: ")
                genero = input_str("Ingrese el género del libro: ")
                libro = Libro(titulo, autor, year, editorial, genero)
                Libreria_1.agregar_libro(libro)
            case 2:
                Libreria_1.mostrar_libros()
            case 3:
                if Libreria_1.comprobar_vacio():
                    print("\nNo hay libros en la librería.")
                    continue
                autor = input_str("Ingrese el autor del libro: ")
                Libreria_1.buscar_por_autor(autor)
            case 4:
                Libreria_1.guardar_en_archivo_json()
            case 5:
                Libreria_1.cargar_desde_archivo_json()
            case 6:
                print("\nSaliendo del programa...")
                return 

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


if __name__ == "__main__":
    menu()
