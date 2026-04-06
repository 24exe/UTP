"""
EVALUACIÓN NOTA 3 - SUDOKU
CURSO: PROGRAMACIÓN III
PROFESOR: Ramiro Andrés Barrios Valencia
FECHA: 8/11/24
UNIVERSIDAD TÉCNOLOGICA DE PEREIRA

INTEGRANTES DEL GRUPO:
    NOMBRE: Carlos Eduardo Grisales Restrepo
    CÓDIGO: 1055750849
    NOMBRE: Santiago Rodriguez Bedoya 
    CÓDIGO: 1089931033

Objetivo: Encontrar al menos una solución a un tablero de dificultad 
imposible de sudokumania.com.ar.
"""

# Importa el módulo 'copy' para permitir realizar 
# copias profundas de estructuras de datos.
import copy

# Define las columnas del tablero de Sudoku 
# utilizando letras de la 'A' a la 'I'.
Cols = "ABCDEFGHI"

# Define las filas del tablero de Sudoku como 
# un conjunto que contiene los números del 1 al 9.
Rows = set(range(1, 10))



# Fun. encargada de inicializar el tablero
"""
Esta función se utiliza para configurar un tablero de Sudoku vacío, 
donde cada celda inicialmente puede contener cualquier número del 1 al 9. 
La estructura resultante (VarDom) es un diccionario que se usará en 
las siguientes etapas para resolver el Sudoku aplicando restricciones
"""

def clearBoard():
    # Inicializa un diccionario vacío llamado 'VarDom'
    VarDom = {}
    # Recorre cada número en 'Rows' (las filas del tablero)
    
    for row in Rows:
        # Recorre cada letra en 'Cols' (las columnas del tablero)
        for col in Cols:
            # Asigna a cada celda (por ejemplo, 'A1', 'B3', etc.) 
            # un conjunto que contiene los números del 1 al 9
            VarDom[f"{col}{row}"] = Rows.copy()
    # Devuelve el diccionario con todas las celdas inicializadas
    return VarDom
# Llama a la función 'clearBoard' para inicializar el tablero 
# y lo asigna a la variable 'VarDom'
VarDom = clearBoard()


# Fun. encargada de mostrar el contenido del diccionario
"""
Esta función se utilizo para acceder al estado del tablero, aunque no se menciona 
en otras funciones o el resto del código, la usamos para 
depurar manualmente y encontrar fallas en nuestra logica o simplemente ver 
como se encontraba el diccionario de manera visual
"""

def mostrar_diccionario(diccionario):
    # Recorre todos los elementos en el diccionario
    
    for clave, valor in diccionario.items():
        # Imprime la clave (por ejemplo, 'A1', 'B3') 
        # junto con su valor (conjunto de posibles números)
        print(f"{clave}: {valor}")

# Fun. encargada de cargar el tablero
"""
Esta función permite cargar un tablero inicial desde un archivo de texto. 
Cada línea del archivo representa el valor de una celda en el tablero. 
Si la línea contiene un número entre 1 y 9, se fija ese número en la celda correspondiente. 
Si contiene un número mayor o igual a 10, se considera que la celda está vacía y puede 
contener cualquier número del 1 al 9.
"""
def loadBoard(VarDom, fileName):
    # Abre el archivo de texto cuyo nombre se pasa 
    # como argumento ('fileName') en modo lectura
    
    with open(fileName, 'r') as file:
        # Recorre todas las claves del diccionario 'VarDom' (celdas del tablero)
        
        for key in VarDom.keys():
            # Lee una línea del archivo, la convierte a un entero y la almacena en 'value'
            value = int(file.readline())
            # Si el valor leído es menor que 10, asigna ese número 
            # como único posible para la celda
            # De lo contrario, deja la celda sin
            # cambios (mantiene todos los números posibles del 1 al 9)
            VarDom[key] = {value} if value < 10 else VarDom[key]

# Llama a la función 'loadBoard' para cargar un 
# tablero desde el archivo 'board.txt' extraido de Sudoku Mania
loadBoard(VarDom, 'board.txt')

# Fun./Restricción encargada de que cada número sea unico
"""
AllDifferent implementa una restricción: 
en una fila, columna o cuadro 3x3, cada número debe ser único.

Si una celda tiene un único valor determinado, esta función 
elimina ese valor de los posibles valores de las celdas relacionadas.

Si se eliminan valores de las celdas relacionadas, 
la función devuelve True para indicar que el tablero ha cambiado 
y que puede ser necesario aplicar más restricciones.
"""
def AllDifferent(VarDom, VarsList):
    # Inicializa una variable booleana para rastrear 
    # si se han realizado cambios en el dominio
    anyChange = False

    # Recorre cada variable (celda) en la lista 'VarsList'
    for var1 in VarsList:
        # Verifica si la celda tiene un único valor posible
        if len(VarDom[var1]) == 1:
            # Obtiene ese valor único de la celda
            value1 = list(VarDom[var1])[0]
            
            # Recorre nuevamente todas las celdas en 'VarsList'
            for var2 in VarsList:
                # Asegura que no se compare la misma celda consigo misma
                if var1 != var2:
                    # Guarda una copia del dominio actual de la celda 'var2'
                    oldValue = VarDom[var2].copy()
                    
                    # Elimina 'value1' del conjunto de posibles valores de 'var2'
                    VarDom[var2].discard(value1)
                    
                    # Si el dominio de 'var2' cambió, marca 'anyChange' como verdadero
                    if oldValue != VarDom[var2]:
                        anyChange = True
                        
    # Devuelve 'True' si se realizaron cambios en alguna celda, 'False' en caso contrario
    return anyChange

# Fun./Restricción entifica pares de celdas que comparten el mismo conjunto de 
# valores posibles y elimina esos valores de las celdas no involucradas
"""
La función hiddenTwin implementa una restricción:

Hidden Twins se refiere a un par de celdas en una fila, columna o cuadrante 
que comparten exactamente el mismo conjunto de posibles valores, 
y no hay otras celdas en ese conjunto que tengan esos mismos valores.

Una vez identificados, se puede eliminar esos valores de las demás celdas en ese grupo, 
lo que reduce las posibilidades y ayuda a avanzar en la solución del Sudoku.
"""
def hiddenTwin(Vars, constraint):
    # Inicializa una variable booleana para rastrear si se realizaron cambios en el dominio
    anyChange = False

    # Crea un diccionario para almacenar pares de celdas que 
    # comparten el mismo conjunto de valores posibles
    varsEquals = {}
    
    # Recorre cada celda (var1) en la lista 'constraint'
    for var1 in constraint:
        # Solo se considera la celda si tiene más de un valor posible
        if len(Vars[var1]) > 1:
            # Compara 'var1' con todas las demás celdas en 'constraint'
            
            for var2 in constraint:
                # Asegura que no se compare la celda consigo misma 
                # y que ambas tengan los mismos valores posibles
                if var1 != var2 and Vars[var1] == Vars[var2]:
                    # Si ya se encontró un par con este conjunto de valores, lo actualiza
                    
                    if tuple(Vars[var1]) in varsEquals:
                        Set_aux = set(varsEquals[tuple(Vars[var1])].copy())
                        Set_aux.add(var1)
                        Set_aux.add(var2)
                        varsEquals[tuple(Vars[var1])] = list(Set_aux)
                    else:
                        # Si no, crea un nuevo par en 'varsEquals' 
                        # con las celdas que comparten el mismo conjunto
                        varsEquals[tuple(Vars[var1])] = [var1, var2]

    # Recorre los conjuntos de valores encontrados en 'varsEquals'
    for domVar in varsEquals:
        # Verifica si el número de celdas encontradas es 
        # igual al número de valores en 'domVar'
        if len(domVar) == len(varsEquals[domVar]):
            # Recorre todas las celdas en la lista 'constraint'
            for var in constraint:
                # Si la celda no forma parte del par 'hidden twin', 
                # elimina esos valores de su dominio
                if var not in varsEquals[domVar]:
                    for value in domVar:
                        # Guarda una copia del dominio actual antes de modificarlo
                        oldValue = Vars[var].copy()
                        # Elimina el valor del dominio de la celda
                        Vars[var].discard(value)
                        # Si hubo un cambio en el dominio, marca 'anyChange' como True
                        if oldValue != Vars[var]:
                            anyChange = True
    
    # Devuelve 'True' si se realizaron cambios en alguna celda, 'False' en caso contrario
    return anyChange

# Fun./Restricción que detecta en que celdas queda un unico valor posible
"""
La función hiddenSingle detecta celdas en las que solo queda un valor posible 
(después de eliminar los valores que ya están en otras celdas del mismo conjunto)
y asigna ese valor a la celda.
"""
def hiddenSingle(VarDom, Varlist):
    # Recorre cada celda (var1) en la lista de variables 'Varlist'
    for var1 in Varlist:
        # Inicializa un conjunto de posibles valores (del 1 al 9) para la celda var1
        dom = set(range(1, 9))

        # Recorre cada otra celda (var2) en 'Varlist'
        for var2 in Varlist:
            # Asegura que no se compare la celda consigo misma
            if var1 != var2:
                # Elimina de 'dom' los valores que están en el dominio de 'var2'
                dom.difference(VarDom[var2])

        # Si solo queda un valor posible en 'dom', asigna ese valor a var1
        if len(dom) == 1:
            VarDom[var1] = dom
            # Devuelve True para indicar que se hizo un cambio
            return True
    # Devuelve False si no se realizó ningún cambio
    return False

# Fun. encargada de definir todas las filas del tablero
"""
La función defineRows genera una lista de todas las filas del tablero de Sudoku, 
donde cada fila es representada por una lista de celdas (en formato "ColumnaFila"). 
Cada celda es identificada por su combinación de columna y fila.
"""
"""
Salida de la Fun.:
[['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1'],
 ['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2'],
 ['A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3', 'I3'],
 ['A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4', 'I4'],
 ['A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5', 'I5'],
 ['A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6', 'I6'],
 ['A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7', 'I7'],
 ['A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8', 'I8'],
 ['A9', 'B9', 'C9', 'D9', 'E9', 'F9', 'G9', 'H9', 'I9']]
"""
def defineRows(Cols, Rows):
    # Inicializa una lista vacía llamada 'allRows' para almacenar todas las filas
    allRows = []

    # Recorre cada fila en 'Rows'
    for row in Rows:
        # Crea una lista vacía llamada 'varsRow' para almacenar 
        # las variables (celdas) de la fila actual
        varsRow = []
        # Recorre cada columna en 'Cols'
        
        for col in Cols:
            # Añade a 'varsRow' la referencia a la celda en 
            # formato "ColumnaFila" (por ejemplo "A1", "B3")
            varsRow.append(f"{col}{row}")
        
        # Añade la fila completa ('varsRow') a 'allRows'
        allRows.append(varsRow)
    
    # Devuelve la lista completa de filas
    return allRows

# Fun. encargada de definir las columnas del tablero
"""
La función defineCols genera una lista de todas las columnas del tablero de Sudoku, 
donde cada columna es representada por una lista de celdas (en formato "ColumnaFila"). 
Cada celda es identificada por su combinación de columna y fila.
"""
"""
Salida de la Fun.:
[['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9'],
 ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9'],
 ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'],
 ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9'],
 ['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9'],
 ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9'],
 ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9'],
 ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9'],
 ['I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9']]
"""
def defineCols(Cols, Rows):
    # Inicializa una lista vacía llamada 'allCols' para almacenar todas las columnas
    allCols = []
    # Recorre cada columna en 'Cols'
    for col in Cols:
        # Crea una lista vacía llamada 'varsCol' 
        # para almacenar las variables (celdas) de la columna actual
        varsCol = []

        # Recorre cada fila en 'Rows'
        for row in Rows:
            # Añade a 'varsCol' la referencia a la celda en 
            # formato "ColumnaFila" (por ejemplo "A1", "A2")
            varsCol.append(f"{col}{row}")
        
        # Añade la columna completa ('varsCol') a 'allCols'
        allCols.append(varsCol)
    
    # Devuelve la lista completa de columnas
    return allCols

# Fun. encargada de definir los subespacios 3x3
"""
La función defineBoxes genera una lista de todos los cuadros 3x3 
del tablero de Sudoku. Cada cuadro está representado por una lista de celdas, 
y cada celda se identifica mediante su combinación de columna y fila.
"""
"""
Salida de la Fun.:
[['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3'],
 ['D1', 'E1', 'F1', 'D2', 'E2', 'F2', 'D3', 'E3', 'F3'],
 ['G1', 'H1', 'I1', 'G2', 'H2', 'I2', 'G3', 'H3', 'I3'],
 ['A4', 'B4', 'C4', 'A5', 'B5', 'C5', 'A6', 'B6', 'C6'],
 ['D4', 'E4', 'F4', 'D5', 'E5', 'F5', 'D6', 'E6', 'F6'],
 ['G4', 'H4', 'I4', 'G5', 'H5', 'I5', 'G6', 'H6', 'I6'],
 ['A7', 'B7', 'C7', 'A8', 'B8', 'C8', 'A9', 'B9', 'C9'],
 ['D7', 'E7', 'F7', 'D8', 'E8', 'F8', 'D9', 'E9', 'F9'],
 ['G7', 'H7', 'I7', 'G8', 'H8', 'I8', 'G9', 'H9', 'I9']]
"""
def defineBoxes(Cols, Rows):
    # Inicializa una lista vacía llamada 'allBoxes' 
    # para almacenar los cuadros (cajas) 3x3
    
    allBoxes = []
    # Itera sobre las filas en pasos de 3 
    # (para cubrir las tres secciones horizontales de cuadros 3x3)
    
    for row_start in range(1, 10, 3):
        # Itera sobre las columnas en pasos de 3 
        # (para cubrir las tres secciones verticales de cuadros 3x3)
        
        for col_start in range(0, 9, 3):
            # Inicializa una lista vacía llamada 'varsBox' para almacenar 
            # las celdas de la caja actual
            varsBox = []
            # Itera sobre 3 filas dentro de un cuadro 3x3
            
            for i in range(3):
                # Itera sobre 3 columnas dentro de un cuadro 3x3
                
                for j in range(3):
                    # Calcula la fila correspondiente sumando 'i' a 'row_start'
                    row = row_start + i
                    # Calcula la columna correspondiente usando 'col_start' y 'j'
                    col = Cols.index(Cols[col_start]) + j
                    # Añade la referencia de la celda en formato "ColumnaFila" al cuadro actual
                    varsBox.append(f"{Cols[col]}{row}")
            # Añade el cuadro completo ('varsBox') a 'allBoxes'
            allBoxes.append(varsBox)
    # Devuelve la lista completa de cuadros 3x3
    return allBoxes

# Fun./Restricción que aplica iterativamente restricciones de filas, columnas y cuadros
"""
La función basicConstraints aplica iterativamente el de restricciones básicas 
previamente definidas (AllDifferent, hiddenTwin, y hiddenSingle) sobre 
el dominio de las variables del Sudoku. 

Este proceso se repite hasta que no se producen más cambios en los dominios de las celdas, 
asegurando que el tablero se ajuste lo más posible a las restricciones del Sudoku.
"""
def basicConstraints(VarDom):
    # Define una lista de restricciones combinadas: filas, columnas y cuadros
    constraints = defineRows(Cols, Rows) + defineCols(Cols, Rows) + defineBoxes(Cols, Rows)
   
    # Inicializa la variable 'anyChange' en True para comenzar el ciclo de restricciones
    anyChange = True
    
    # Mientras haya cambios en las restricciones, sigue aplicándolas
    while anyChange:
        # Establece 'anyChange' en False al inicio de cada ciclo, se actualizará si hay cambios
        anyChange = False
        
        # Recorre cada conjunto de variables de las restricciones (filas, columnas, cuadros)
        for varsList in constraints:
            # Aplica la restricción AllDifferent y si hay algún cambio, 
            # marca anyChange como True
            anyChange = AllDifferent(VarDom, varsList) if not anyChange else True
            # Aplica la restricción hiddenTwin y si hay algún cambio, 
            # marca anyChange como True
            anyChange = hiddenTwin(VarDom, varsList) if not anyChange else True
            # Aplica la restricción hiddenSingle y si hay algún cambio, 
            # marca anyChange como True
            anyChange = hiddenSingle(VarDom, varsList) if not anyChange else True
    # Devuelve el dominio de variables actualizado después de aplicar las restricciones
    return VarDom


# Fun. que comprueba si el Sudoku está resuelto.
"""
Esta función determina si un Sudoku está completo. 
Revisa cada celda para asegurar que tenga un único número. 
Si todas las celdas están llenas correctamente, el Sudoku está resuelto.
"""
def is_solved(VarDom):
    #VarDom: Un diccionario que representa el dominio de cada variable.
    for key, value in VarDom.items():
        # Itera sobre cada celda del Sudoku y su conjunto de posibles valores.
        # Si una celda tiene más de un valor posible o no tiene ningún valor,
        # significa que el Sudoku aún no está completamente resuelto.
        if len(value) != 1 and len(value) != 0:
            # Si se encuentra una celda con múltiples o ningún valor posible,
            # la función concluye que el Sudoku no está resuelto y retorna False.
            return False

    # Si se han examinado todas las celdas y cada una tiene un único valor,
    # la función concluye que el Sudoku está resuelto y retorna True.   
    return True
  #True si el Sudoku está resuelto, False en caso contrario.


# Fun. que comprueba si el Sudoku es consistente.
"""
Esta función verifica si el Sudoku es localmente consistente.

Un Sudoku es localmente consistente si ninguna celda tiene un dominio vacío. 
En otras palabras, si cada celda tiene al menos un valor posible.
"""
def is_local_consistent(VarDom):
    for key, value in VarDom.items():
    #Itera sobre todas las claves (celdas) y valores (conjuntos de posibles valores) 
    # del diccionario VarDom.
        if len(VarDom[key]) == 0:
            # Verifica si el conjunto de posibles valores para la celda actual está vacío.
            # Si el conjunto está vacío, significa que no hay ningún número que 
            # pueda colocarse en esa celda, lo que indica una inconsistencia en el Sudoku.
            return False
    return True
    # Si se llega a este punto, significa que se han revisado 
    # todas las celdas y ninguna tiene un conjunto vacío de posibles valores. 
    # Por lo tanto, el Sudoku es localmente consistente y la función devuelve True.

#Fun./Restricción determina si un valor puede ser eliminado de una celda sin 
# violar las restricciones basicas
"""
La función can_delete verifica si es posible eliminar un valor 
específico de una celda en un tablero de Sudoku sin que esto lleve a un estado inconsistente. 
Para ello, crea una copia del tablero, asigna el valor a la celda en la copia, 
aplica las restricciones básicas del Sudoku (filas, columnas y regiones) y verifica 
si el tablero modificado sigue siendo localmente consistente. Si solo un valor de todos 
los posibles mantiene la consistencia, entonces eliminar ese valor no es seguro, 
y la función devuelve False. Si múltiples valores o ninguno mantienen la consistencia, 
la función devuelve True, indicando que el valor puede ser eliminado sin problemas.
"""
def can_delete(board, position, values):
    # board: El estado actual del tablero de Sudoku.
    # position: La posición de la celda a verificar.
    # values: Los posibles valores para la celda en la posición dada.
    test = copy.deepcopy(board) 
    # Crea una copia del tablero original para realizar pruebas sin modificar el original.
    valList = list(values)  
    # Convierte el conjunto de valores posibles en una lista para iterar sobre ellos.
    contador = 0 
    # Inicializa un contador para llevar la cuenta de los valores que mantienen la consistencia.
    
    for val in valList:
        test[position] = {val}  
        # Asigna el valor actual a la celda en la copia del tablero.

        test = basicConstraints(test) 
        # Aplica las restricciones básicas del Sudoku al tablero modificado.
        if is_local_consistent(basicConstraints(test)): 
        # Verifica si el tablero sigue siendo localmente consistente.
            contador += 1  # Si es consistente, incrementa el contador.
        test = copy.deepcopy(board) 
        # Restaura el tablero a su estado original para la siguiente iteración.

     # Devuelve True si solo un valor mantiene la consistencia, False en caso contrario.  
    return contador == 1

# Fun. intenta asignar un valor a una celda y aplicar restricciones, 
# devolviendo el tablero actualizado si es consistente, 
# o restaurándolo si causa inconsistencias.
"""
La función delete_value intenta asignar un valor a una celda específica del tablero, 
aplicando las restricciones del Sudoku. Si el valor no causa inconsistencias locales, 
devuelve el tablero actualizado. Si provoca problemas, restaura el estado anterior del tablero.
"""
def delete_value(board, position, values):
    # Si se puede eliminar el valor en la posición indicada, continúa con el proceso
    if can_delete(board, position, values):
        # Se hace una copia profunda del tablero actual para mantener el estado original
        oldBoard = copy.deepcopy(board)
        
        # Convierte el conjunto de valores a una lista para iterar sobre ellos
        valList = list(values)
        
        # Itera sobre la lista de valores para intentar eliminarlos del dominio de la celda
        for val in valList:
            # Asigna el valor actual de la lista al dominio de la celda en la posición indicada
            board[position] = {val}
            
            # Aplica las restricciones básicas para actualizar el tablero con 
            # las nuevas asignaciones
            board = basicConstraints(board)
            
            # Si el tablero es consistente localmente (sin conflictos), 
            # devuelve el tablero actualizado
            if is_local_consistent(board):
                return board
            else:
                # Si no es consistente, restaura el tablero al estado anterior
                board = copy.deepcopy(oldBoard)
    
    # Si no se puede eliminar el valor o no hay consistencia, retorna el tablero original sin cambios
    return board


# Fun. que implementa un backtracking no cronologico
"""
La función backtraking utiliza una estrategia de prueba y error para explorar 
diferentes posibilidades de asignación de valores a las celdas del Sudoku. 
Si una elección lleva a un callejón sin salida, se retrocede y se prueba otra opción. 
Este proceso continúa hasta que se encuentra una solución válida o se determina 
que no existe solución.
Aplica las restricciones básicas y utiliza un enfoque de backtracking para intentar 
resolver el Sudoku, eliminando valores de celdas hasta que el tablero esté resuelto.
"""
def backtraking(VarDom):
    # Aplica las restricciones básicas al tablero para reducir el dominio de las celdas
    VarDom = basicConstraints(VarDom)

    # Mientras el tablero no esté resuelto, sigue buscando una solución
    while not is_solved(VarDom):
        # Recorre el dominio de las celdas intentando hacer eliminaciones con backtracking
        for i in range(2, 9):
            # Recorre todas las celdas del tablero
            for key, value in VarDom.items():
                # Si el dominio de una celda tiene exactamente 'i' valores, intenta eliminar valores
                if len(value) == i:
                    VarDom = delete_value(VarDom, key, value)
            
            # Si el tablero se resuelve durante el proceso, termina el ciclo
            if is_solved(VarDom):
                break
    
    # Devuelve el tablero con la solución encontrada (o sin cambios si no se resolvió)
    return VarDom



# Fun. que sirve para mostrar el tablero
"""
Esta función toma un diccionario que representa el 
estado actual del Sudoku y lo muestra en un formato legible, 
destacando las celdas resueltas y las que aún tienen múltiples posibilidades.
"""
def mostrar_tablero(diccionario):
    tablero = [[' ' for _ in range(9)] for _ in range(9)]

    for clave, valor in diccionario.items():
        fila = int(clave[1]) - 1
        columna = ord(clave[0]) - ord('A')
        tablero[fila][columna] = valor.pop() if len(valor) == 1 else "*"

    print("Sudoku resuelto!!!")
    for i in range(9):
        if i % 3 == 0:
            print("+-------+-------+-------+")
        for j in range(9):
            if j % 3 == 0:
                print("|", end=" ")
            print(tablero[i][j], end=" ")
        print("|")
    print("+-------+-------+-------+")


# Se llama a la función 'backtraking' con el tablero actual ('VarDom'),
# la cual intenta resolver el Sudoku aplicando restricciones y eliminando valores.
# El tablero actualizado o modificado se guarda nuevamente en 'VarDom'.
VarDom = backtraking(VarDom)

# Se llama a la función 'mostrar_tablero' con el tablero resuelto o modificado ('VarDom'),
# para imprimir el estado final del tablero de Sudoku en formato visual en la consola.
mostrar_tablero(VarDom)