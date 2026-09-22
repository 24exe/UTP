import random


# ============================================================
# CONTEXTO DEL PROBLEMA
# ============================================================
# Tenemos un tablero de ajedrez de 8x8.
#
# Queremos colocar 8 reinas de manera que ninguna pueda
# atacar a otra.
#
# Para simplificar:
#
#     Cada fila tendrá exactamente una reina.
#
# Por lo tanto, solo necesitamos decidir la columna
# de cada reina.
#
# Ejemplo:
#
#     [0, 4, 7, 5, 2, 6, 1, 3]
#
# significa:
#
#     Reina de la fila 0 -> columna 0
#     Reina de la fila 1 -> columna 4
#     Reina de la fila 2 -> columna 7
#     ...
# ============================================================


N = 8


# ============================================================
# FUNCIÓN PARA SABER SI DOS REINAS ESTÁN EN CONFLICTO
# ============================================================

def are_in_conflict(row1, col1, row2, col2):

    # Mismo columna
    if col1 == col2:
        return True

    # Misma diagonal
    #
    # Dos posiciones están en la misma diagonal cuando
    # la diferencia de filas es igual a la diferencia
    # de columnas.
    if abs(row1 - row2) == abs(col1 - col2):
        return True

    return False


# ============================================================
# CONTAR CONFLICTOS
# ============================================================
# board[row] = columna donde está la reina de esa fila.
#
# Esta función cuenta cuántos conflictos tiene una reina
# específica.
# ============================================================

def count_conflicts(board, row):

    conflicts = 0

    col = board[row]

    for other_row in range(N):

        # No comparamos la reina consigo misma.
        if other_row == row:
            continue

        other_col = board[other_row]

        if are_in_conflict(
            row,
            col,
            other_row,
            other_col
        ):
            conflicts += 1

    return conflicts


# ============================================================
# CONTAR TODOS LOS CONFLICTOS
# ============================================================

def total_conflicts(board):

    conflicts = 0

    for row in range(N):

        # Solo contamos conflictos con las filas posteriores
        # para no contar dos veces el mismo conflicto.
        for other_row in range(row + 1, N):

            if are_in_conflict(
                row,
                board[row],
                other_row,
                board[other_row]
            ):
                conflicts += 1

    return conflicts


# ============================================================
# MIN-CONFLICTS
# ============================================================

def min_conflicts(max_steps=10000):

    # --------------------------------------------------------
    # 1. CREAR UNA SOLUCIÓN INICIAL
    # --------------------------------------------------------
    # Colocamos una reina aleatoriamente en cada fila.
    #
    # Esta solución probablemente tendrá conflictos.
    # --------------------------------------------------------

    board = [
        random.randint(0, N - 1)
        for _ in range(N)
    ]

    print("Configuración inicial:")
    print(board)

    print(
        "Conflictos iniciales:",
        total_conflicts(board)
    )


    # --------------------------------------------------------
    # 2. REPETIR HASTA ENCONTRAR UNA SOLUCIÓN
    # --------------------------------------------------------

    for step in range(max_steps):

        # Si no existen conflictos,
        # encontramos una solución válida.
        if total_conflicts(board) == 0:

            print("\n¡Solución encontrada!")
            print("Pasos:", step)
            print("Tablero:", board)

            return board


        # ----------------------------------------------------
        # 3. BUSCAR REINAS QUE TENGAN CONFLICTOS
        # ----------------------------------------------------

        conflicted_rows = []

        for row in range(N):

            if count_conflicts(board, row) > 0:
                conflicted_rows.append(row)


        # ----------------------------------------------------
        # 4. ELEGIR UNA REINA CONFLICTIVA
        # ----------------------------------------------------

        row = random.choice(conflicted_rows)


        # ----------------------------------------------------
        # 5. PROBAR TODAS LAS COLUMNAS
        # ----------------------------------------------------
        # Queremos saber:
        #
        # "¿En qué columna tendría esta reina
        #    la menor cantidad de conflictos?"
        # ----------------------------------------------------

        best_columns = []
        minimum_conflicts = float("inf")

        for column in range(N):

            # Movemos temporalmente la reina.
            board[row] = column

            conflicts = count_conflicts(
                board,
                row
            )

            # Encontramos una columna mejor.
            if conflicts < minimum_conflicts:

                minimum_conflicts = conflicts
                best_columns = [column]

            # Si otra columna tiene exactamente
            # el mismo número mínimo de conflictos,
            # también la guardamos.
            elif conflicts == minimum_conflicts:

                best_columns.append(column)


        # ----------------------------------------------------
        # 6. ELEGIR UNA DE LAS MEJORES OPCIONES
        # ----------------------------------------------------

        board[row] = random.choice(best_columns)


    # Si llegamos aquí, no encontramos una solución
    # dentro del número máximo de pasos.
    print("\nNo se encontró solución.")
    return None


# ============================================================
# EJECUTAR EL ALGORITMO
# ============================================================

solution = min_conflicts()


# ============================================================
# MOSTRAR EL TABLERO
# ============================================================

if solution:

    print("\nRepresentación del tablero:\n")

    for row in range(N):

        for column in range(N):

            if solution[row] == column:
                print("♛", end=" ")

            else:
                print(".", end=" ")

        print()