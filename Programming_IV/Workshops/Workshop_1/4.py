'''
Programación IV
Grupo: 1
Profesor: Andrés Felipe Ramírez Correa
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Listas y Métodos


TALLER 1

4. Escriba un programa que pida al usuario la cantidad que desea
de la lista, luego el usuario debe ingresar valores numéricos
enteros hasta llenar la lista, luego de ingresarlos se debe
imprimir en pantalla cada número ingresado por el usuario y al
lado debe aparecer ese mismo número al cuadrado y al lado ese
mismo número al cubo, ejemplo:
L = [2,3]


Salida:
2 - 4 - 8
3 - 9 - 27
'''
print ("4. CUADRADO Y CUBO DE CADA ELEMENTO DE UNA LISTA \n")
cantidad = int(input("Ingrese la cantidad de números que desea en la lista: "))
L = []
for i in range(cantidad):
    num = int(input(f"Ingrese el número {i+1}: "))
    L.append(num)

for num in L:
    print(f"{num} - {num**2} - {num**3}")


