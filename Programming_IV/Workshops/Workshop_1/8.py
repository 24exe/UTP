'''
Programación IV
Grupo: 1
Profesor: Andrés Felipe Ramírez Correa
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Listas y Métodos


TALLER 1

8. Realizar un programa que haga conteo de todos los caracteres
que no sean vocales en una lista de 10 cadenas.
'''

# Lista de 10 cadenas
cadenas = ["Programación", "Python", "Universidad", "Estudiante", "Código", "Profesor", "Taller", "Grupo", "Métodos", "Listas"]

vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
conteo = 0

for cadena in cadenas:
    for caracter in cadena:
        if caracter not in vocales:
            conteo += 1


print("8. CONTEO VOCALES \n")

print("Cantidad de caracteres que no son vocales:", conteo)

