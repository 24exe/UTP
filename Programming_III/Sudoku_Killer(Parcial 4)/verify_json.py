import json

def verify_sudoku_killer_json(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
        cages = data['cages']

    # 1. Verificar IDs únicos
    ids = [cage['id'] for cage in cages]
    if len(ids) != len(set(ids)):  # Compara la longitud original con el conjunto (sin duplicados).
        return False, "Se encontraron IDs de jaulas duplicados."

    # 2. Verificar la suma total de las jaulas
    total_sum = sum(cage['sum'] for cage in cages)
    if total_sum != 405:  # En Sudoku Killer, la suma total de todas las celdas debe ser 405.
        return False, f"Suma total incorrecta de las jaulas: {total_sum}. Se esperaba: 405."

    # 3. Verificar que no haya celdas repetidas e identificar jaulas con celdas repetidas
    all_cells = []  # Lista para almacenar todas las celdas procesadas.
    repeated_cells = []  # Lista para almacenar celdas repetidas.
    cages_with_repeated_cells = []  # Lista para identificar IDs de jaulas con celdas repetidas.

    for cage in cages:
        for cell in cage['cells']:
            if cell in all_cells:  # Si la celda ya existe, es repetida.
                repeated_cells.append(cell)
                cages_with_repeated_cells.append(cage['id'])
            else:
                all_cells.append(cell)

    if repeated_cells:  # Si se encontraron celdas repetidas, se retorna el error.
        return False, f"Celdas repetidas encontradas: {repeated_cells}. Jaulas con celdas repetidas: {cages_with_repeated_cells}."

    # 4. Verificar que todas las celdas estén presentes e identificar celdas faltantes o adicionales
    expected_cells = [f"{chr(col)}{row}" for col in range(ord('A'), ord('J')) for row in range(1, 10)]
    # Genera todas las celdas esperadas en un Sudoku 9x9, como 'A1', 'B2', etc.
    missing_cells = list(set(expected_cells) - set(all_cells))  # Celdas faltantes.
    extra_cells = list(set(all_cells) - set(expected_cells))  # Celdas adicionales.

    if missing_cells or extra_cells:
        error_message = ""
        if missing_cells:  # Si hay celdas faltantes, las incluye en el mensaje.
            error_message += f"Celdas faltantes: {missing_cells}. "
        if extra_cells:  # Si hay celdas adicionales, las incluye también.
            error_message += f"Celdas adicionales: {extra_cells}."
        return False, error_message

    return True, "Todas las verificaciones pasaron correctamente."

# Ejemplo de uso
json_file = 'output.json'
is_valid, message = verify_sudoku_killer_json(json_file)

if is_valid:
    print("El archivo JSON es válido.")
else:
    print(f"El archivo JSON no es válido: {message}")