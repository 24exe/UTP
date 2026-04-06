# Sudoku Killer Solver

## Descripción
Este proyecto utiliza un enfoque a reducir el dominio del sudoku killer con diferentes restricciones las cuales estan en el archivo sudoku.py detalladas y comentadas.

### Archivo `sudoku.py`
El archivo `sudoku.py` implementa el solucionador principal del Sudoku Killer. Este solucionador utiliza técnicas avanzadas como reducción de dominio, verificación de restricciones, y estrategias de búsqueda para resolver tableros complejos de manera eficiente.

#### Funcionalidades Principales
- **Carga del Tablero:** Lee un archivo JSON con la configuración inicial del tablero, incluyendo celdas iniciales y restricciones de sumas.
- **Reducción de Dominio:** Elimina valores no válidos con base en las reglas del Sudoku clásico y las restricciones adicionales del Sudoku Killer.
- **Estrategias de Resolución:** Utiliza algoritmos como backtracking y forward checking para explorar soluciones posibles.
- **Validación y Resultado:** Comprueba que la solución es válida y muestra el tablero resuelto.
- **Funciones Adicionales:** Incluye utilidades para imprimir el tablero y registrar los pasos del proceso de resolución.

Este solucionador está diseñado para abordar cualquier configuración válida de Sudoku Killer, asegurando que todas las restricciones se cumplan y produciendo una solución óptima.

## Creadores
- Juan alejandro Salgado, Carlos grisales, Angel Mora, Santiago Rodriguez,

## Requisitos
- Python 3.8 o superior instalado.
- Entrada: Archivo `input.txt` con el formato correcto para convertir.
    - El formato podria verse de esta manera:

        0:A1,A2:9
        1:A3,A4:5
        2:B1,B2:16
        3:B3,B4:13
        4:C1,C2:10
        5:C3,C4:7
        6:D1,D2,D3:12
        7:E1,E2,E3:14
        8:F1,G1:13
        9:F2,G2:11
        10:F3,F4:7
        11:H1,H2:5
        12:I1,I2:8
        13:G3,G4:10
        14:H3,H4:15
        15:I3,I4:15
        16:A5,B5,C5:14
        17:B6,C6:7
        18:A6,A7,A8:18
        19:B7,B8:4
        20:D4,D5:15
        21:E4,E5:6
        22:F5,G5:8
        23:D6,D7,C7:18
        24:C8,D8:11
        25:C9,D9:13
        26:A9,B9:6
        27:E6,F6:8
        28:E7,F7:14
        29:E8,F8:5
        30:E9,F9,G9:22
        31:H5,I5:12
        32:G6,G7:9
        33:H6,H7:9
        34:I6,I7:8
        35:G8,H8,I8:22
        36:H9,I9:4

    En donde el primer numero representa la id, posteriormente van las coordenadas de las casillas que conforman el bloque y por ultimo la suma del bloque.
    Si se quiere probar el funcionamiento del sudoku se puede hacer con los tableros de ejemplo en la carpeta 'Tableros'.

    Ademas todos los tableros fueron sacados de la pagina: https://www.sudokumania.com.ar/sudoku/killer/


## Instrucciones de Uso
1. Asegúrate de tener Python instalado.
2. Clona este repositorio en tu máquina local:
   ```bash
   git clone <https://github.com/NumMy0/Sudoku-killer-python>