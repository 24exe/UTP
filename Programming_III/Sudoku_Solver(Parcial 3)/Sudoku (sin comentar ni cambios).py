import copy

Cols = "ABCDEFGHI"
Rows = set(range(1, 10))

def clearBoard():
    VarDom = {}
    for row in Rows:
        for col in Cols:
            VarDom[f"{col}{row}"] = Rows.copy()
    return VarDom

VarDom = clearBoard()

def mostrar_diccionario(diccionario):
    for clave, valor in diccionario.items():
        print(f"{clave}: {valor}")

def loadBoard(VarDom, fileName):
    with open(fileName, 'r') as file:
        for key in VarDom.keys():
            value = int(file.readline())
            VarDom[key] = {value} if value < 10 else VarDom[key]

loadBoard(VarDom, 'board.txt')

def hiddenTwin(VarDom, VarsList):
    anyChange = False
    for var1 in VarsList:
        if len(VarDom[var1]) == 1:
            value1 = list(VarDom[var1])[0]
            for var2 in VarsList:
                if var1 != var2:
                    oldValue = VarDom[var2].copy()
                    VarDom[var2].discard(value1)
                    if oldValue != VarDom[var2]:
                        anyChange = True
    return anyChange

def hiddenSingle(Vars, constraint):
    anyChange = False
    varsEquals = {}
    for var1 in constraint:
        if len(Vars[var1]) > 1:
            for var2 in constraint:
                if var1 != var2 and Vars[var1] == Vars[var2]:
                    if tuple(Vars[var1]) in varsEquals:
                        Set_aux = set(varsEquals[tuple(Vars[var1])].copy())
                        Set_aux.add(var1)
                        Set_aux.add(var2)
                        varsEquals[tuple(Vars[var1])] = list(Set_aux)
                    else:
                        varsEquals[tuple(Vars[var1])] = [var1, var2]

    for domVar in varsEquals:
        if len(domVar) == len(varsEquals[domVar]):
            for var in constraint:
                if var not in varsEquals[domVar]:
                    for value in domVar:
                        oldValue = Vars[var].copy()
                        Vars[var].discard(value)
                        if oldValue != Vars[var]:
                            anyChange = True
    return anyChange

def ForwardChecking(VarDom, Varlist):
    for var1 in Varlist:
        dom = set(range(1, 9))
        for var2 in Varlist:
            if var1 != var2:
                dom.difference(VarDom[var2])
        if len(dom) == 1:
            VarDom[var1] = dom
            return True

def defineRows():
    Cols = "ABCDEFGHI"
    Rows = set(range(1, 10))

    allRows = []
    for row in Rows:
        varsRow = []
        for col in Cols:
            varsRow.append(f"{col}{row}")
        allRows.append(varsRow)
    return allRows

def defineCols():
    Cols = "ABCDEFGHI"
    Rows = set(range(1, 10))
    allCols = []
    for col in Cols:
        varsCol = []
        for row in Rows:
            varsCol.append(f"{col}{row}")
        allCols.append(varsCol)
    return allCols

def defineBoxes():
    Cols = "ABCDEFGHI"
    Rows = set(range(1, 10))
    allBoxes = []
    for row_start in range(1, 10, 3):
        for col_start in range(0, 9, 3):
            varsBox = []
            for i in range(3):
                for j in range(3):
                    row = row_start + i
                    col = Cols.index(Cols[col_start]) + j
                    varsBox.append(f"{Cols[col]}{row}")
            allBoxes.append(varsBox)
    return allBoxes

def basicConstraints(VarDom):
    constraints = defineRows() + defineCols() + defineBoxes()
    anyChange = True
    while anyChange:
        anyChange = False
        for varsList in constraints:
            anyChange = hiddenTwin(VarDom, varsList) if not anyChange else True
            anyChange = hiddenSingle(VarDom, varsList) if not anyChange else True
            anyChange = ForwardChecking(VarDom, varsList) if not anyChange else True
    return VarDom

def is_solved(VarDom):
    for key, value in VarDom.items():
        if len(value) != 1 and len(value) != 0:
            return False
    return True

def is_local_consistent(VarDom):
    for key, value in VarDom.items():
        if len(VarDom[key]) == 0:
            return False
    return True  

def can_delete(board, position, values):
    test = copy.deepcopy(board)
    valList = list(values)
    contador = 0
    for val in valList:
        test[position] = {val}
        test = basicConstraints(test)
        if is_local_consistent(basicConstraints(test)):
            contador += 1
        test = copy.deepcopy(board)
      
    return contador == 1

def delete_value(board, position, values):
    if can_delete(board, position, values):
        oldBoard = copy.deepcopy(board)
        valList = list(values)
        for val in valList:
            board[position] = {val}
            board = basicConstraints(board)
            if is_local_consistent(board):
                return board
            else:
                board = copy.deepcopy(oldBoard)
    return board

def backtraking(VarDom):
    VarDom = basicConstraints(VarDom)
    while not is_solved(VarDom):
        for i in range(2, 9):
            for key, value in VarDom.items():
                if len(value) == i:
                    VarDom = delete_value(VarDom, key, value)
            if is_solved(VarDom):
                break
    return VarDom

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

VarDom = backtraking(VarDom)

mostrar_tablero(VarDom)