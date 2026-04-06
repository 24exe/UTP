import json

# Propósito: Esta función toma un archivo de texto que contiene información
# sobre las jaulas de un Sudoku Killer en un formato personalizado y lo
# convierte en un archivo JSON con una estructura más estandarizada.

def convert_to_json(input_file, output_file):
    cages = []  # Crea una lista vacía llamada cages para almacenar los datos
                # de las jaulas extraídas. Esta lista contendrá diccionarios,
                # cada uno representando una jaula del Sudoku Killer.

    with open(input_file, 'r') as f:
        for line in f:
            if line.startswith('//'):  # Omite las líneas de comentarios
                continue
              # Si la línea comienza con //, se considera un comentario y
              # se salta.
            line = line.strip()
            # Elimina cualquier espacio en blanco al inicio o al final de la línea.
            if not line:  # Omite las líneas vacías
                continue
            parts = line.split(':')  # Divide la línea en partes separadas por ':'.
            id = int(parts[0])  # Convierte la primera parte en un entero como ID.
            cells = parts[1].split(',')  # Obtiene las celdas dividiéndolas por ','.
            sum = int(parts[2])  # Convierte la última parte en un entero como suma.
            cages.append({
                "id": id,
                "cells": cells,
                "sum": sum
            })
    with open(output_file, 'w') as f:
        # Escribe el resultado en un archivo JSON con formato legible (indentado).
        json.dump({"cages": cages}, f, indent=2)

# Ejemplo de uso
input_file = 'input.txt'  # Reemplaza con la ruta de tu archivo de entrada.
output_file = 'output.json'  # Reemplaza con la ruta de tu archivo de salida.
convert_to_json(input_file, output_file)
