'''
Programación IV
Grupo: 1
Profesor: Andrés Felipe Ramírez Correa
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Archivos, clases y objetos.


TALLER 2


5. Clasificación de objetos electrónicos
- Crea una clase `Electrodomestico` con atributos: nombre, marca, consumo (en
watts).
- Implemente un método que clasifique los objetos como “bajo consumo” (<500W) o
“alto consumo” (>=500W).
- Guarda el inventario en `electrodomesticos.txt`.
'''
from io import *
import os

class Electrodomestico:
    marca: str
    nombre: str
    consumo: int


    def InsertData(self):
        while True:
            try:
                nameAux = str(input("Digite el nombre del electrodomestico: "))
                self.nombre = nameAux
                break
            except ValueError:
                print ("ERROR, TIPO DE DATO INVALIDO \n")
        while True:
            try:
                marcaAux = str(input("Digite la marca del electrodomestico: "))
                self.marca = nameAux
                break
            except ValueError:
                print ("ERROR, TIPO DE DATO INVALIDO \n")
        while True:
            try:
                consumoAux = int(input("Digite el consumo del electrodomestico(en Watts): "))
                if consumoAux > 0:
                    self.consumo = consumoAux
                    break
                else:
                    print("TIENE QUE INGRESAR UN NÚMERO ENTERO POSITIVO. \n")
            except ValueError:
                print ("ERROR, TIPO DE DATO INVALIDO \n")
    
    @staticmethod
    def Clasificacion(lista_electrodomesticos: list):
        bajo_consumo: list = []
        alto_consumo: list = []
        ruta_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_archivo = os.path.join(ruta_actual, "electrodomesticos.txt")
        with open(ruta_archivo, "r") as archivo:
            for linea in archivo:
                partes = linea.split("Consumo:")
                if len(partes) > 1: # Verificación de que el split funciono
                    consumo = int(partes[1].strip())
                    if consumo >= 500: 
                        alto_consumo.append(linea)
                    else:
                        bajo_consumo.append(linea)
        print("Aparatos de alto consumo: \n")
        for aparato in alto_consumo:
            print(aparato)
        print("Aparatos de bajo consumo: \n")
        for aparato in bajo_consumo:
            print(aparato)

    @staticmethod
    def Inventario(lista_electrodomesticos: list):
        ruta_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_archivo = os.path.join(ruta_actual, "electrodomesticos.txt")
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            for aparato in lista_electrodomesticos:
                archivo.write(f"Nombre: {aparato.nombre}, Marca: {aparato.marca} , Consumo: {aparato.consumo}\n")
        archivo.close()
        print("Inventario creado en 'electrodomesticos.txt'")


n: int
while True:
    try:    
        num = int(input("¿Cuantos electrodomesticos desea Ingresar?: "))
        n = num
        break
    except (ValueError, TypeError):
        print("ERROR DE INSERCIÓN EN EL NÚMERO DE ELECTRODOMESTICOS, SE DARA UN TAMAÑO DE 2 POR DEFECTO. \n")
        n = 2
        break

electrodomesticos: list[Electrodomestico] = []
for i in range(n):
    print(f"Electrodomestico {i+1}: \n")
    aparato = Electrodomestico()
    aparato.InsertData()
    electrodomesticos.append(aparato)
    print("\n")
Electrodomestico.Inventario(electrodomesticos)
Electrodomestico.Clasificacion(electrodomesticos)