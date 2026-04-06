# Archivo: main.py

import os
from sudoku import KillerSudokuSolver
from convert_to_json import convert_to_json
from verify_json import verify_sudoku_killer_json
from sudoku import KillerSudokuSolver

def main():
    try:
        # Paso 1: Convertir el archivo de texto a JSON
        print('Convirtiendo el archivo de texto a JSON...')
        convert_to_json('input.txt', 'output.json')
        print('Archivo convertido exitosamente.')

        # Paso 2: Verificar el archivo JSON generado
        print('Verificando el archivo JSON...')
        is_valid = verify_sudoku_killer_json('output.json')

        if not is_valid:
            print('El archivo JSON contiene inconsistencias. Corrige los errores y vuelve a intentarlo.')
            return
        print('El archivo JSON es válido.')

        # Paso 3: Resolver el Sudoku Killer
        print('Resolviendo el Sudoku Killer...')
        solver = KillerSudokuSolver('output.json')
        solver.solver(log=True) # Llama al método de resolución con logging activado

        # Paso 4: Mostrar el tablero resuelto
        print('Tablero resuelto:')
        solver.print_board2()
    except Exception as e:
        print(f'Ocurrió un error: {e}')

if __name__ == "__main__":
    main()
