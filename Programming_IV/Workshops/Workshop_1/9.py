'''
Programación IV
Grupo: 1
Profesor: Andrés Felipe Ramírez Correa
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Listas y Métodos


TALLER 1

9. Realizar un programa que inicialice una lista con 15 valores
aleatorios y posteriormente muestre en pantalla cada elemento
de la lista junto con su cuadrado y su cubo.
'''

import random


def main():
    print("8. NÚMEROS ALEATORIOS EN UNA LISTA CON SU CUADRADO Y CUBO \n")
    lista = [random.randint(1, 100) for num in range(15)]

    print(f"Lista: {lista}\n")
    for num in lista:
        print(f"{num} -> {num**2} -> {num**3}")


main()