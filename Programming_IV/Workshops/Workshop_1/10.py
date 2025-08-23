'''
Programación IV
Grupo: 1
Profesor: Andrés Felipe Ramírez Correa
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Listas y Métodos


TALLER 1

10. Elabore un programa para ingresar la siguiente lista.
Lista= [“casa”, “programación”, “utp”, “universidad”, “utp, “casa”,
“casa”,” thj”, “vbh”, “456”, “987”]

    a. Borre los elementos repetidos que tengamos en la lista
    b. Borre las cadenas que NO contengan vocales.
    c. Ordene la lista en orden alfabético respecto al primer
    elemento de la cadena.
'''

Lista = ["casa", "programación", "utp", "universidad", "utp", "casa", "casa", "thj", "vbh", "456", "987"]
print(f"Lista original: {Lista}")

# a. Borrar elementos repetidos (manteniendo el orden)
lista_sin_repetidos = list(dict.fromkeys(Lista))

# b. Borrar cadenas que NO contengan vocales
vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
lista_con_vocales = [palabra for palabra in lista_sin_repetidos if any(v in palabra for v in vocales)]

# c. Ordenar alfabéticamente por el primer carácter
lista_ordenada = sorted(lista_con_vocales, key=lambda x: x[0].lower())

print("\nLista sin repetidos:")
print(lista_sin_repetidos)
print("\nLista con vocales:")
print(lista_con_vocales)
print("\nLista final ordenada:")
print(lista_ordenada)