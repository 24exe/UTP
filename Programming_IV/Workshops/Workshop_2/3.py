'''
Programación IV
Grupo: 1
Profesor: Andrés Felipe Ramírez Correa
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Archivos, clases y objetos.


TALLER 2


3. Cadenas clasificadas por vocales
- Crea una clase `Cadena` con un atributo texto.
- Genere una lista de 15 cadenas.
- Implemente un método que ordene primero las cadenas que empiezan con vocal y luego las demás.
- Guarde la lista ordenada en `cadenas.txt`.
'''

from io import *
import os



class Cadena:
    texto: str

    def InsertData(self):
        while True:
            try:
                textoAux = str(input("Digite una cadena (no mayor a 20 caracteres): ").strip())
                self.texto = textoAux
                break;
            except ValueError:
                print("ERROR, DATO INVALIDO")
    @staticmethod
    def SortCadenas(lista_de_cadenas: list):
        vocales = "aeiouAEIOU"
        # Listas por comprensión para almacenar ambos
        empieza_vocal = [cadena for cadena in lista_de_cadenas if cadena.texto and cadena.texto[0] in vocales]
        no_vocal = [cadena for cadena in lista_de_cadenas if cadena.texto and cadena.texto[0] not in vocales]
        ordenadas = empieza_vocal + no_vocal

        ruta_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_archivo = os.path.join(ruta_actual, "cadenas.txt")
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            for cadena in ordenadas:
                archivo.write(f"{cadena.texto}\n")
        archivo.close()
        print("Lista ordenada guardada en cadenas.txt")


lista_cadenas: list[Cadena] = []
for i in range(15):
    print(f"Cadena {i+1}: \n")
    cadena = Cadena()
    cadena.InsertData()
    lista_cadenas.append(cadena)
    print("\n")

Cadena.SortCadenas(lista_cadenas)