'''
Programación IV
Grupo: 1
Profesor: Andrés Felipe Ramírez Correa
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Listas y Métodos


TALLER 1

7. Realizar un programa que pida al usuario un carácter, luego se
debe mostrar las cadenas que contengan dicho carácter y debe
mostrar si dichas cadenas son pares o impares.
Lista= [“oso”, “casa”, “murciélago”, “ventana”, “programación”,”
objetos”, “listas”, “métodos”, “utp”]

'''
def Cadenas_Con_Caracter(caracter: str, lista : list):
    coincidencias =[] 
    resultado = []
    for cadena in lista:
        if caracter in cadena:
            coincidencias.append(cadena)


    # verifica si la lista tiene al menos 1 elemento para ser "True", en caso de no tener es "False"
    if coincidencias:
        for cadena in coincidencias:
            longitud = len(cadena)
            paridad = "par" if longitud % 2 == 0 else "impar"
            resultado.append(f"{cadena} -> longitud {longitud} ({paridad})")
        return "Cadenas encontradas:\n" + "\n".join(resultado)
    else:
        return f"No hay cadenas que contengan el carácter '{caracter}'."
     


def main():
     print("7. CONCORDANCIA DE CARACTERES \n")
     caracter = ' '
     Lista= ["oso", "casa", "murciélago", "ventana", "programación", "objetos", "listas", "métodos", "utp"]
     while True:
        try:
            c = str(input("Ingrese el caracter a buscar: ").strip())
            if len(c) == 1:
                caracter = c
                break
            else:
                print("ERROR, DIGITE UN SOLO CARACTER. EJ: a\n")
        except ValueError:
                print("ERROR, DIGITE UN TIPO DE DATO CHAR. EJ: B.\n")
     print(Cadenas_Con_Caracter(caracter, Lista))


main()