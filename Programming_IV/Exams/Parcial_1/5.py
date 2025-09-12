'''
Programación IV
Grupo: 1
Profesor: Andrés Felipe Ramírez Correa
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Nombre: Rafael Urrea Gaviria
Codigo: 1004737606

Parcial 1

5. Implementar el algoritmo de cifrado y descifrado cesar haciendo uso de
POO, archivos y listas.
Para este algoritmo se deja documentación en la sección de “Parcial I”.
'''

from io import *
import os

class Cesar:
    def __init__(self, llave: int):
        self.llave = llave % 26
        self.alf_lower = [chr(c) for c in range(ord('a'), ord('z') + 1)]
        self.alf_upper = [chr(c) for c in range(ord('A'), ord('Z') + 1)]

    def cifrar(self, texto: str) -> str:
        resultado = []
        for ch in texto:
            if ch in self.alf_lower:
                i = self.alf_lower.index(ch)
                resultado.append(self.alf_lower[(i + self.llave) % 26])
            elif ch in self.alf_upper:
                i = self.alf_upper.index(ch)
                resultado.append(self.alf_upper[(i + self.llave) % 26])
            else:
                resultado.append(ch)
        return "".join(resultado)

    def descifrar(self, texto: str) -> str:
        resultado = []
        for ch in texto:
            if ch in self.alf_lower:
                i = self.alf_lower.index(ch)
                resultado.append(self.alf_lower[(i - self.llave) % 26])
            elif ch in self.alf_upper:
                i = self.alf_upper.index(ch)
                resultado.append(self.alf_upper[(i - self.llave) % 26])
            else:
                resultado.append(ch)
        return "".join(resultado)

def solicitar_llave() -> int:
    while True:
        try:
            k = int(input("Ingrese la llave: ").strip())
            return k
        except ValueError:
            print("ERROR: ingrese un número entero.")

def solicitar_texto(prompt: str) -> str:
    while True:
        try:
            txt = input(f"{prompt}: ").rstrip("\n")
            if txt == "":
                print("ERROR: no puede estar vacío.")
                continue
            return txt
        except Exception:
            print("ERROR EN EL TIPO DE DATO")

def guardar_registro(original: str, cifrado: str, nombre_archivo: str = "cifrado_registro.txt") -> None:
    try:
        ruta = os.path.dirname(os.path.abspath(__file__))
    except NameError:
        ruta = os.getcwd()
    ruta_archivo = os.path.join(ruta, nombre_archivo)
    try:
        with open(ruta_archivo, "a", encoding="utf-8") as f:
            f.write(f"{original}|{cifrado}\n")
        print(f"Guardado en archivo: {ruta_archivo}")
    except Exception as e:
        print(f"ERROR AL GUARDAR: {e}")

def mostrar_menu():
    print("\n--- MENU CIFRADO CÉSAR ---")
    print("1. Cifrar palabra")
    print("2. Descifrar palabra")
    print("3. Salir")

def menu():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Seleccion opción [1-3]: ").strip())
        except ValueError:
            print("ERROR: opción invalida.")
            continue

        if opcion == 1:
            llave = solicitar_llave()
            texto = solicitar_texto("Ingrese la palabra o frase a cifrar")
            cesar = Cesar(llave)
            cifrado = cesar.cifrar(texto)
            print("\n--- TEXTO CIFRADO ---")
            print(cifrado)
            print("---------------------\n")
            guardar_registro(texto, cifrado)

        elif opcion == 2:
            llave = solicitar_llave()
            texto = solicitar_texto("Ingrese la palabra cifrada para descifrar")
            cesar = Cesar(llave)
            descifrado = cesar.descifrar(texto)
            print("\n--- TEXTO DESCIFRADO ---")
            print(descifrado)
            print("------------------------\n")

        elif opcion == 3:
            print("SALIENDO...")
            break
        else:
            print("OPCION NO VALIDA")

def main():
    menu()

if __name__ == "__main__":
    main()
