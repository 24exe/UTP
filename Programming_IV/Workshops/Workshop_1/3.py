'''
Programación IV
Grupo: 1
Profesor: Andrés Felipe Ramírez Correa
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Listas y Métodos


TALLER 1

3. Escribir un programa que almacene las asignaturas de un curso
en una lista, pida al usuario las 4 notas de cada materia y en
pantalla mostrar el promedio que ha sacado en cada materia y si
alguna materia queda por debajo de la nota 3 debe salir en
pantalla “asignatura perdida”, luego se deben calcular el
promedio general de todas las materias si el promedio está por
debajo de 3 debe imprimir “semestre perdido”, si esta entre 3 y 4
debe imprimir “buen trabajo”, si el promedio esta entre 4 y 5
debe imprimir “felicidades serás becado”.

Salida de datos:

Matemáticas -- nota1: 2, nota2: 2, nota3: 2, nota 4: 2
Promedio de Matemáticas: 2 -- asignatura perdida

Inglés -- nota1: 3, nota2: 3, nota3: 3, nota 4: 3
Promedio de Inglés: 3 -- asignatura ganada

Promedio general: 2.5 -- “Semestre perdido”
'''

def prom_Semestre_Algorithm(promedio_materias : list, materias : int):
    conteo = 0
    for i in promedio_materias:
        conteo += i
    return conteo / materias


def main():
    # Se que es código spaguetti.
    asignaturas = []        #n
    notas_Asignaturas = []  #4
    prom_Asignaturas = []   #n
    num_Materias = 0        #n
    mensaje_Asignatura = [] #n
    print ("3. PROGRAMA DE ASIGNATURAS, NOTAS Y PROMEDIOS \n")

    print("--- SOFTWARE ACADEMICO, BIENVENIDO ALUMNO --- \n")


    # ----------------------- CONTEO MATERIAS -----------------------
    while True:
        try:
            n = int(input("¿Cuantas materias tiene?: ").strip())
            if n > 0:
                num_Materias = n
                break
            else:
                print("ERROR, DIGITE UN NÚMERO ENTERO POSITIVO. EJ: 4.\n")
        except ValueError:
            print("ERROR, DIGITE UN TIPO DE DATO ENTERO POSITIVO. EJ: 3.\n")
    

    # ----------------------- NOMBRE MATERIAS -----------------------
    for i in range(num_Materias):
        materia = str(input(f"Digite la materia N°{i + 1}: "))
        asignaturas.append(materia)
    #print(asignaturas)
    

    # ----------------------- NOTAS POR MATERIA -----------------------
    for materia in asignaturas:
        print (f"Digite las notas para la asignatura de {materia}: ")
        notas_Provisional = []
        for i in range(4):
            while True:
                try:
                    nota = float(input(f"Digite la nota N° {i+1} de {materia}: ").strip().replace(",", "."))
                    if 0 <= nota <= 5:
                        notas_Provisional.append(nota)
                        break
                    else:
                        print("ERROR, DIGITE UN NÚMERO ENTRE 0 Y 5. EJ: 3,5\n")
                except ValueError:
                     print("ERROR, DIGITE UN TIPO DE DATO ENTERO POSITIVO. EJ: 2.\n")

        # Se usa el metodo copy junto a append para copiar cada elemento de la lista provisional en la principal
        notas_Asignaturas.append(notas_Provisional.copy())

        #print(notas_Asignaturas)


    # ----------------------- PROMEDIOS -----------------------
    for materia in notas_Asignaturas:
        conteo = 0
        for nota in materia:
            conteo += nota
        promedio = conteo / 4
        if promedio < 3:
            mensaje = "Asignatura Perdida"
        else:
            mensaje = "Asignatura Ganada"    
        mensaje_Asignatura.append(mensaje)
        prom_Asignaturas.append(promedio)
    #print (prom_Asignaturas)
    #print (mensaje_Asignatura)



    # ----------------------- PROMEDIO SEMESTRE -----------------------
    
    prom_Semestre = prom_Semestre_Algorithm(prom_Asignaturas, num_Materias)
    #print (prom_Semestre)


    # ----------------------- MENSAJE FINAL -----------------------

    print("===== BOLETÍN ACADÉMICO =====\n")

    # enumerate crea pares (indice, valor) dentro del elemento del bucle.
    for idx, materia in enumerate(asignaturas):
        notas = notas_Asignaturas[idx]

        # lista por comprensión junto con .join
        notas_str = ", ".join([f"nota {i+1}: {notas[i]}" for i in range(4)])
        print(f"{materia} -- {notas_str}")
        print(f"Promedio de {materia}: {prom_Asignaturas[idx]} -- {mensaje_Asignatura[idx]}\n")

    print(f"Promedio general: {prom_Semestre}", end=" -- ")
    if prom_Semestre < 3:
        print("Semestre perdido </3 ")
    elif 3 <= prom_Semestre < 4:
        print("Buen trabajo :) ")
    elif 4 <= prom_Semestre <= 5:
        print("¡Felicitaciones serás becado! :D ")
main()


