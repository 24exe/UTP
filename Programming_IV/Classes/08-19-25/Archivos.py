'''
Programación IV

Archivo 2

Grupo: 1
Profesor: Andrés Felipe Ramírez Correa
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Archivos

'''

# El * significa que importa todo lo de esa libreria, en estos ejemplos no afecta mucho
# la funcionalidad.
from io import *


while True:
    opcion = int((input('''Bienvenido al Menú!
                        1. Escribir
                        2. Leer
                        3. Borrar
                        4. Añadir
                        5. Salir
                        Opción: ''')))
    
    '''
    A diferencia del Switch, Match Case es mas eficiente por qué esta basado
    internamente en una tabla Hash, por ende su acceso es instantaneo O(1) a
    diferencia del Switch que tiene un acceso O(n) (n siendo los casos) para el
    caso que se desea.
    '''
    match opcion:
        case 1:
            archivo = open(r"C:\Users\Eduardo Grisales\Desktop\archivo.txt", "w")
            mensaje = input("ingrese los datos: ")
            archivo.write(f"{mensaje}\n")
            archivo.close()
        case 2:
            archivo = open(r"C:\Users\Eduardo Grisales\Desktop\archivo.txt", "r")
            lectura = archivo.read()
            print(lectura)
            archivo.close()
        case 3:
            archivo = open(r"C:\Users\Eduardo Grisales\Desktop\archivo.txt", "w")
            archivo.close()
        case 4:
            archivo = open(r"C:\Users\Eduardo Grisales\Desktop\archivo.txt", "a")
            mensaje = input("ingrese los datos: ")
            archivo.write(f"{mensaje}\n")
            archivo.close()
        case 5:
            print("adios")
            break
