'''
Programación IV
Grupo: 1
Profesor: Andrés Felipe Ramírez Correa
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Listas y Métodos


TALLER 1

5. Realice un programa que almacene una cantidad de cadenas
dictaminadas por el usuario, en pantalla se debe mostrar la
cadena que más caracteres contenga y la cadena que menos
caracteres contenga.

Ejemplo:
Lista= [“oso”, “casa”, “murciélago”, “ventana”, “programación”]
Cadena mayor = programación.
Cadena menor = oso
'''
num_Cadenas = 0

def maxFinder(Lista : list):
    longitud_final = 0
    elemento_final = ""
    for elem in Lista:
         longitud_elemento = len(elem)
         if longitud_elemento > longitud_final:
            longitud_final = longitud_elemento
            elemento_final = elem
    return elemento_final

def minFinder (Lista : list): 
    longitud_final = 1000000000000000000000000000000000000000000000000000
    elemento_final = ""
    for elem in Lista:
         longitud_elemento = len(elem)
         if longitud_elemento < longitud_final:
            longitud_final = longitud_elemento
            elemento_final = elem
    return elemento_final
     


print("5. CADENA MAYOR Y MENOR \n")
while True:
        try:
            n = int(input("¿Cuantas cadenas desea ingresar?: ").strip())
            if n > 0:
                num_Cadenas = n
                break
            else:
                print("ERROR, DIGITE UN NÚMERO ENTERO POSITIVO. EJ: 4.\n")
        except ValueError:
            print("ERROR, DIGITE UN TIPO DE DATO ENTERO POSITIVO. EJ: 3.\n")
lista = []
for i in range(n):
    cadena = input(f"Ingrese la cadena #{i+1}: ")
    lista.append(cadena)

# Metodos "sencillos" (aburridos para este ejercicio)

#cadena_mayor = max(lista, key=len)
#cadena_menor = min(lista, key=len)

# Metodo con Fun.
cadena_mayor = maxFinder(lista)
cadena_menor = minFinder(lista)
print(f"Cadena mayor = {cadena_mayor}.")
print(f"Cadena menor = {cadena_menor}.")


