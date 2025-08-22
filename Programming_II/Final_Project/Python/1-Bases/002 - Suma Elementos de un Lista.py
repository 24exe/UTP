def sum_List(numeros: list[int]) -> int:
   sum: int = 0
   for i in numeros:  # i es el VALOR del elemento
       sum = sum + i  # Correcto: sumas directamente el valor
       '''
       ALTERNATIVA SI SE DESEA USAR EL INDICE EN VEZ DEL VALOR EN LA LISTA: 
       for i in range(len(list)):  # i es el ÍNDICE
        sum = sum + list[i]  # Correcto: usas el índice para acceder al valor
       '''
   return sum

def Gaussian_Sum (list: list[int]) -> int:
    sum: int = 0
    N: int = list[len(list) - 1]    #Primera manera de encontrar el ultimo elemento de una lista.
    '''
    ALTERNATIVA:
    N = list[-1]  ---> Indice NEGATIVO
    
    EJEMPLO:

    lista = [10, 20, 30, 40, 50]
    #         0   1   2   3   4   <- índices positivos
    #        -5  -4  -3  -2  -1   <- índices negativos
    '''
    sum = (N*(N+1))//2  # División entera para obtener int (//)
    return sum


print("¿Quieres ver la suma de los primeros 100 números? Me importa un cu** aquí te va chaval.")

new_List= []

for i in range(1, 101):
    new_List.append(i)

sum_Result = sum_List(new_List)

print(f"El resultado es: {sum_Result}\n")

print("Si te soy honesto conte de esta manera: \n1+2+3+... \nLo cual no es tan cool... \n")

print("Por eso te mostrare como hacerlo con la formula de la suma Gaussiana (deberia ser más rápido): ")

sum_Result = Gaussian_Sum(new_List)

print(f"SUMA GAUSSINA = {sum_Result}")