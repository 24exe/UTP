'''
Programación IV
Grupo: 1
Profesor: Andrés Felipe Ramírez Correa
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Archivos, clases y objetos.


TALLER 2


4. Registro de clientes
- Crea una clase `Cliente` con al menos 5 atributos (id, nombre, edad, ciudad, saldo).
- Implemente un método que guarde los clientes en `clientes.txt`.
- Otro método que lea el archivo y muestre solo los clientes con saldo negativo.
'''

from io import *
import os


class Cliente:
    ContadorClientes: int = 0
    ID: int
    Name: str
    Age: int
    City: str
    Saldo: float

    def InsertData(self):
        while True:
            try:
                nameAux = str(input("Digite su nombre completo (con apellidos): "))
                self.Name = nameAux
                break
            except ValueError:
                print ("ERROR, TIPO DE DATO INVALIDO \n")

        print(f"Se le asigno la siguiente ID: {Cliente.ContadorClientes + 1}\n")
        Cliente.ContadorClientes += 1
        self.ID = Cliente.ContadorClientes

        while True:
            try:
                ageAux = int(input("Digite su edad: "))
                if ageAux >= 18:
                    self.Age = ageAux
                    break
                else:
                    print("TIENE QUE TENER MAS DE 18 PARA SER CLIENTE, PIENSE CUAL ES SU EDAD DE NUEVO. \n")
            except ValueError:
                print ("ERROR, TIPO DE DATO INVALIDO \n")
        
        while True:
            try:
                cityAux = str(input("Digite su ciudad de residencia: "))
                self.City = cityAux
                break
            except ValueError:
                print ("ERROR, TIPO DE DATO INVALIDO \n")
        while True:
            try:
                saldoAux = float(input("Digite el saldo de su cuenta: "))
                self.Saldo = saldoAux
                break
            except ValueError:
                print ("ERROR, EL TIPO DE DATO DEBE SER DE TIPO NÚMERICO \n")

    @staticmethod
    def SaveResults(lista_usuarios: list):
        ruta_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_archivo = os.path.join(ruta_actual, "clientes.txt")
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            for usuario in lista_usuarios:
                archivo.write(f"ID: {usuario.ID}, Nombre: {usuario.Name}, Edad: {usuario.Age}, Ciudad: {usuario.City}, Saldo: {usuario.Saldo}\n")
            archivo.close()
        print("Usuarios en el archivo 'clientes.txt'")

    @staticmethod
    def MostrarClientesConSaldoNegativo():
        ruta_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_archivo = os.path.join(ruta_actual, "clientes.txt")
        with open(ruta_archivo, "r") as archivo:
            for linea in archivo:
                partes = linea.split("Saldo:")
                if len(partes) > 1: # Verificación de que el split funciono para
                    saldo = float(partes[1].strip())
                    if saldo < 0: 
                        print(linea)
            archivo.close()
        


n: int
while True:
    try:    
        num = int(input("¿Cuantos USERS desea Ingresar?: "))
        n = num
        break
    except (ValueError, TypeError):
        print("ERROR DE INSERCIÓN EN EL NÚMERO DE USUARIOS, SE DARA UN TAMAÑO DE 3 POR DEFECTO. \n")
        n = 3
        break

usuarios: list[Cliente] = []
for i in range(n):
    print(f"Usuario {i+1}: \n")
    user = Cliente()
    user.InsertData()
    usuarios.append(user)
    print("\n")

Cliente.SaveResults(usuarios)
print("Clientes con saldo negativo:")
Cliente.MostrarClientesConSaldoNegativo()


