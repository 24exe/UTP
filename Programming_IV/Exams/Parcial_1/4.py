'''
Programación IV
Grupo: 1
Profesor: Andrés Felipe Ramírez Correa
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Nombre: Rafael Urrea Gaviria
Codigo: 1004737606


Parcial 1

4. Diseñe un programa que reciba un numero entero de 4 cifras, diga si el
primer número es múltiplo del cuarto número y debe mostrar la suma del
segundo número y el tercero (no requiere implementar el paradigma
orientado a objetos), este punto se debe hacer usando operaciones
aritméticas para descomponer el numero de 4 cifras.
'''
def solicitar_numero_4_cifras() -> int:
    while True:
        try:
            entrada = int(input("Ingrese un número entero de 4 cifras: ").strip())
        except ValueError:
            print("ERROR: Debe ingresar un entero.")
            continue
        if 1000 <= entrada <= 9999:
            return entrada
        else:
            print("ERROR: El número debe tener 4 cifras.")

def descomponer_numero(numero: int) -> tuple[int, int, int, int]:
    d1 = numero // 1000
    d2 = (numero // 100) % 10
    d3 = (numero // 10) % 10
    d4 = numero % 10
    return d1, d2, d3, d4

def es_multiplo(primer: int, cuarto: int) -> str:
    if cuarto == 0:
        return f"El cuarto digito es 0; no se puede verificar múltiplo (división por cero)."
    if primer % cuarto == 0:
        return f"El primer digito {primer} es mltiplo del cuarto digito {cuarto}."
    else:
        return f"El primer digito {primer} no es multiplo del cuarto digito {cuarto}."

def mostrar_resultados(numero: int, d1: int, d2: int, d3: int, d4: int):
    print("\n--- RESULTADOS ---")
    print(f"Número ingresado: {numero}")
    print(f"Digitos -> 1: {d1}  2: {d2}  3: {d3}  4: {d4}")
    print(es_multiplo(d1, d4))
    suma = d2 + d3
    print(f"La suma del segundo digito ({d2}) y el tercero ({d3}) es: {suma}")
    print("------------------\n")

def main():
    while True:
        numero = solicitar_numero_4_cifras()
        d1, d2, d3, d4 = descomponer_numero(numero)
        mostrar_resultados(numero, d1, d2, d3, d4)
        while True:
            respuesta = input("¿Desea procesar otro número? (s/n): ").strip().lower()
            if respuesta == "s":
                break 
            elif respuesta == "n":
                return
            else:
                print("SOLO RESPONDA s (sí) o n (no).")
main()
