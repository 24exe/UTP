'''
Programación IV
Grupo: 1
Profesor: Andrés Felipe Ramírez Correa
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Listas y Métodos


TALLER 1

2. Dada la siguiente lista: palabras = ["Hola", "mundo", "esto", "es",
"Python"] Una todas las palabras de la lista en una sola cadena separadas
por espacio o algún carácter especial.
'''


def UnirCadenas(palabras: list) -> str:
    inicio = 0
    CadenaUnica: str = ""
    for elemento in palabras:
        if inicio == 0:
            CadenaUnica = elemento
            inicio += 1
        else:
            CadenaUnica = CadenaUnica +  " " + elemento
    return CadenaUnica




palabras = ["Hola", "mundo", "esto", "es","Python"]

print ("2. CONCATENACIÓN DE ELEMENTOS DE UNA LISTA \n")
print(f"Lista a concatenar: {palabras}")

cadena = UnirCadenas(palabras)

print (f"Union: {cadena}")