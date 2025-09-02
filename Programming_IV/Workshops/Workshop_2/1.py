'''
Programación IV
Grupo: 1
Profesor: Andrés Felipe Ramírez Correa
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Archivos, clases y objetos.


TALLER 2


1. Números y dígitos invertidos
- Crear una clase `Numero` donde pueda tener un entero de tres cifras.
- Implemente un método que devuelva la suma de sus dígitos.
- Implemente otro método que escriba en `numeros.txt` el número original y su versión invertida.
- Leer el archivo e imprimir los resultados.


'''
from io import *    # * = "importar todo".
import os           # Para encontrar la ruta del taller.


class Numero:
    value: int
    acumulador: int
    InvertedValue: str


    def InsertData(self):

        while True:
            try:
                numAux = int(input("Ingrese un valor no superior a 999: ").strip())
                if not isinstance(numAux, int):
                    raise TypeError ("EL ARGUMENTO DEBE SER UN NÚMERO ENTERO. ")
                if 0 <= numAux <= 999:
                    self.value = numAux
                    break;
                else:
                    print("ERROR, DIGITE UN NÚMERO DENTRO DEL RANGO (0 - 999)\n")
            except ValueError:
                print("ERROR, DATO INVALIDO")


    def SumOfDigits(self) -> int:
        acumulador = 0
        numAux = self.value
        while numAux != 0:
            acumulador += (numAux % 10)
            numAux //= 10
        self.acumulador = acumulador
        return self.acumulador
    

    def printData(self):
        print(f"La suma de los dígitos de {self.value} es {self.SumOfDigits()}")
   
    def PrintInArchive(self):
        # archivo = open(r"C:\Users\Eduardo Grisales\Desktop\numeros.txt", "w") # Ruta obsoleta
        ruta_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_archivo = os.path.join(ruta_actual, "numeros.txt")
        archivo = open(ruta_archivo, "w", encoding="utf-8")
        archivo.write(f"Número original: {self.value} \n")
        self.InvertedNumber(self.value)
        archivo.write(f"Número invertido: {self.InvertedValue}")
        archivo.close()

    def InvertedNumber(self, num):
        '''
        # Manera de hacerlo pero que se pierden los ceros. EJ: 120 -> 21 en vez de 120 -> 021
        invertido = 0
        while n > 0:
            ultimo = n % 10
            invertido = invertido * 10 + ultimo
            n //= 10
        return invertido
        '''
        numInString = str(num)
        invertedNum = numInString[::-1] # Así conserva los 0s
        self.InvertedValue = invertedNum

    def PrintDataOfDocument(self):
        print("\n---INFORMACIÓN DEL .TXT---\n")
        ruta_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_archivo = os.path.join(ruta_actual, "numeros.txt")
        try:
            with open(ruta_archivo, "r") as archivo:
                lectura = archivo.read()
                print(lectura)
        # Excepciones
        except FileNotFoundError:
            print("El archivo no existe.")



x = Numero()
x.InsertData()
x.printData()
x.PrintInArchive()
x.PrintDataOfDocument()
