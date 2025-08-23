'''
Programación IV
Grupo: 1
Profesor: Andrés Felipe Ramírez Correa
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Listas y Métodos


TALLER 1

1. Realice un algoritmo para sumar los valores numéricos de la
siguiente lista sin ordenarla:
Lista= [2, 8,” hola”, “programación”, 10, “utp”, 85, 82, 100,”
mundo”]
'''

def ListSumAlgorithm(lista : list):
    if not isinstance(lista , list):
        raise TypeError("El argumento de la Fun. ListSumAlgorithm debe ser una lista.\n ")
    suma = 0
    for elemento in lista:
        try:
            suma += float(elemento)
        except (ValueError, TypeError):
            pass
    return suma








Lista= [2, 8, "hola",  "programación", 10, "utp", 85, 82, 100, "mundo"]

print ("2. SUMA ELEMENTOS NUMERICOS DE UNA LISTA \n")
print(f"Lista a sumar: {Lista}")

sum = ListSumAlgorithm(Lista)

print (f"La suma de valores numéricos de la lista es: {sum} ")