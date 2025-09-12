'''
Programación IV
Grupo: 1
Profesor: Andrés Felipe Ramírez Correa
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Constructores, Destructores y Métodos


TALLER 3

1. Cree una clase llamada `Libro` con atributos como título, autor, año, editorial y
género. Incluya métodos para mostrar la información del libro, guardar los datos en un
archivo y buscar libros por autor.
'''
from io import *
import os
# Clase Libro
class Libro:
    title: str
    autor: str
    year: str
    editorial: str
    genre: str

    # Constructor
    def __init__(self, title, autor, year, editorial, genre):
        self.title = title
        self.autor = autor
        self.year = year
        self.editorial = editorial
        self.genre = genre
    
    # Para debugging
    def print_Info(self):
        print(f"Titulo: {self.title}, Autor: {self.autor}, Año: {self.year}, Editorial: {self.editorial}, Genero: {self.genre} ")
    
    @staticmethod
    def save_Info(library: 'list[Libro]'):
        ruta_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_archivo = os.path.join(ruta_actual, "libreria.txt")
        #final_library = [book + "\n" for book in library]      # test
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            archivo.write("Titulo|Autor|Año|Editorial|Genero\n")
            #archivo.writelines(final_library)
            for book in library:
                archivo.write(f"{book.title}|{book.autor}|{book.year}|{book.editorial}|{book.genre}\n")


    @staticmethod
    def print_Archive():
        ruta_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_archivo = os.path.join(ruta_actual, "libreria.txt")
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            next(archivo)       # Para saltar encabezado
            lineas = archivo.readlines()
            for linea in lineas:
                print(linea.strip())

    @staticmethod
    def search_By_Autor(key_Autor: str):
        key_Autor= key_Autor.lower().strip()
        ruta_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_archivo = os.path.join(ruta_actual, "libreria.txt")
        with open(ruta_archivo, "r") as archivo:
            next(archivo)  # Saltar encabezado
            for linea in archivo:
                partes = linea.strip().split("|")
                if len(partes) == 5:        # Verificar si se realizo la partición correctamente
                    _, autor_To_Find, *_ = partes  # Desempaquetando lista de partes
                    autor_To_Find = autor_To_Find.lower().strip()
                if key_Autor == autor_To_Find:
                    print(linea)

# Funciones Auxiliares
def insert_Data()-> Libro:
    #title = autor = year = editorial = genre = ""      # Otra manera de definir variables en una sola linea
    '''
    # Segunda manera de definir variables, no necesario porque el scope es toda la fun.
    title: str
    autor: str
    year: str
    editorial: str
    genre: str
    '''
    while True:
        try:
            title = str(input("Titulo: "))
            break        
        except ValueError:
            print("ERROR EN EL TIPO DE DATO")
    while True:
        try:
            autor = str(input("Autor: "))
            break        
        except ValueError:
            print("ERROR EN EL TIPO DE DATO")
    while True:
        try:
            year = str(input("Año: "))
            break        
        except ValueError:
            print("ERROR EN EL TIPO DE DATO")
    while True:
        try:
            editorial = str(input("editorial: "))
            break        
        except ValueError:
            print("ERROR EN EL TIPO DE DATO")
    while True:
        try:
            genre = str(input("Genero: "))
            break        
        except ValueError:
            print("ERROR EN EL TIPO DE DATO")

    x = Libro(title, autor, year, editorial, genre)
    return x

# Scope global por comodidad
Libreria: list[Libro] = []

def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Crear Libro")
        print("2. Actualizar Biblioteca")
        print("3. Mostrar Libros")
        print("4. Buscar Libro")
        print("5. Salir")

        opcion = int(input("Ingrese una opción [1-5]: "))
        match opcion:
            case 1:
                x = insert_Data()
                Libreria.append(x)
                print("--LIBRO CREADO--\n")
            case 2:
                Libro.save_Info(Libreria)
                print("--BIBLIOTECA ACTUALIZADA, CONSULTAR .TXT --\n")
            case 3:
                print("--BIBLIOTECA--\n")
                Libro.print_Archive()
            case 4:
                key = str(input("Autor del Libro: "))
                print("\n--LIBROS ENCONTRADOS--\n")
                Libro.search_By_Autor(key)
                pass
            case 5:
                print("QUE TENGA BUEN DIA.")
                break
            case _:
                print("OPCIÓN NO VALIDA")

# MAIN FUN.
def main():
    menu()

main()
