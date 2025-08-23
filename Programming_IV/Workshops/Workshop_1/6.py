'''
Programación IV
Grupo: 1
Profesor: Andrés Felipe Ramírez Correa
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Listas y Métodos


TALLER 1

6. Realice un programa en el que el usuario ingrese un valor
entero, luego debe mostrar en pantalla las cadenas cuya longitud
sea igual al número ingresado, puede usar la lista del ejercicio 5
o 7.
'''

def main():
    print("6. CONCORDANCIA CADENA INGRESADA \n")
    longitud = 0
    lista_cadenas = ["oso", "casa", "murciélago", "ventana", "programación"]
    while True:
        try:
            n = int(input("Ingrese la longitud de la cadena a buscar (número): ").strip())
            if n > 0:
                longitud = n
                break
            else:
                print("ERROR, DIGITE UN NÚMERO ENTERO POSITIVO. EJ: 4.\n")
        except ValueError:
            print("ERROR, DIGITE UN TIPO DE DATO ENTERO POSITIVO. EJ: 3.\n")
    coinciden = [cad for cad in lista_cadenas if len(cad) == longitud]
    if coinciden:
        print("Cadenas encontradas:\n" + "\n".join(coinciden)) 
    else:
        print(f"No hay cadenas con longitud {longitud}.")


main()