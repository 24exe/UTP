import copy
import json
import itertools
from itertools import product
from itertools import combinations

class KillerSudokuSolver:

    def __init__(self, file_path):
        """
        Inicializa una instancia de la clase `KillerSudokuSolver`.

        Args:
            file_path (str): La ruta al archivo JSON que contiene el tablero de Sudoku Killer a resolver.
        """
        self.file_path = file_path  # Guarda la ruta al archivo en el atributo `file_path`
        self.vars_values = self.define_variables()  # Inicializa el diccionario `vars_values` con todas las celdas y sus posibles valores
        self.read_board()  # Lee el tablero de Sudoku desde el archivo y actualiza `vars_values` con los valores iniciales
        self.restricciones = self.define_constraints()  # Define las restricciones del Sudoku (filas, columnas, bloques)
        self.adjacent_constraints = self.define_adjacent_constraints()

    def define_variables(self):
        """
        Define e inicializa las variables del Sudoku Killer.

        Este método crea un diccionario llamado `vars_values` que almacenará la información de cada celda del Sudoku.
        Cada celda se representa con una clave (ej. "A1") y su valor es una lista con la siguiente estructura:
        [id_jaula, suma_jaula, dominio]

        - id_jaula: El identificador de la jaula a la que pertenece la celda.
        - suma_jaula: La suma objetivo de los valores de las celdas dentro de la jaula.
        - dominio: Un conjunto que contiene los posibles valores que la celda puede tomar (inicialmente 1-9).

        Además, define las etiquetas de las columnas (`columnas`) como "ABCDEFGHI" y las filas (`filas`) como un conjunto de números del 1 al 9.

        Returns:
            dict: El diccionario `vars_values` que mapea cada celda a su información correspondiente.
        """
        self.columnas = "ABCDEFGHI"  # Define las etiquetas de las columnas del Sudoku
        self.filas = {i for i in range(1, 10)}  # Define los números de las filas del Sudoku (1-9) como un conjunto
        vars_values = {}  # Crea un diccionario vacío para almacenar las variables y sus valores

        for col in self.columnas:  # Itera sobre cada columna (A, B, C, ...)
            for fila in self.filas:  # Itera sobre cada fila (1, 2, 3, ...)
                vars_values[f"{col}{fila}"] = []  # A cada celda se le asigna una lista vacía donde se agregarán sus atributos
        return vars_values  # Devuelve el diccionario `vars_values`

    def extract_domains(self, length, value):
        """
        Calcula la unión de todos los conjuntos posibles de dígitos únicos (1-9) de una longitud dada que suman un valor dado.

        Este método se utiliza para determinar el dominio inicial de las celdas dentro de una jaula en un Sudoku Killer.
        Genera todas las combinaciones posibles de dígitos únicos (sin repetición) de la longitud especificada y selecciona
        aquellas combinaciones cuya suma es igual al valor dado. Luego, calcula la unión de todos los dígitos presentes en
        estas combinaciones válidas.

        Args:
            length (int): La cantidad de dígitos en el conjunto (corresponde al número de celdas en una jaula).
            value (int): La suma deseada de los dígitos (corresponde a la suma objetivo de la jaula).

        Returns:
            set: Un conjunto que contiene la unión de todos los dominios válidos para la jaula.
        """

        all_combinations = itertools.combinations(range(1, 10), length)  # Genera todas las combinaciones posibles de dígitos únicos de la longitud dada
        union_domain = set()  # Inicializa un conjunto vacío para almacenar la unión de los dominios

        for combination in all_combinations:  # Itera sobre cada combinación
            if sum(combination) == value:  # Si la suma de la combinación es igual al valor objetivo
                union_domain.update(combination)  # Agrega los dígitos de la combinación al conjunto de unión

        return union_domain  # Devuelve el conjunto de unión, que representa el dominio inicial de las celdas en la jaula

    def read_board(self):
        """
        Lee el tablero de Sudoku Killer desde el archivo JSON y actualiza las variables.

        Este método abre el archivo JSON especificado por `file_path` y extrae la información de las jaulas y las celdas.
        Luego, actualiza el diccionario `vars_values` con los valores iniciales y la información del dominio para cada celda.

        Para cada jaula, se calcula el dominio utilizando la función `extract_domains` y se almacena en el diccionario
        `vars_values` junto con el ID de la jaula y la suma objetivo.

        No retorna ningún valor, pero modifica el estado interno del objeto `KillerSudokuSolver`.
        """

        with open(self.file_path, 'r') as file:  # Abre el archivo JSON en modo lectura
            data = json.load(file)  # Carga los datos del archivo JSON en un diccionario llamado 'data'

        for cage_data in data['cages']:  # Itera sobre cada jaula en los datos JSON
            cage_id = cage_data['id']  # Obtiene el ID de la jaula actual
            cage_sum = cage_data['sum']  # Obtiene la suma objetivo de la jaula actual
            cage_cells = cage_data['cells']  # Obtiene la lista de celdas que pertenecen a la jaula actual

            domain = self.extract_domains(len(cage_cells), cage_sum)  # Calcula el dominio de la jaula utilizando la función 'extract_domains'

            # Actualiza vars_values con la información de la jaula para cada celda
            for cell in cage_cells:
                self.vars_values[cell].insert(0, cage_id)  # Agrega el ID de la jaula al inicio de la lista de la celda
                self.vars_values[cell].insert(1, cage_sum)  # Agrega la suma de la jaula en la segunda posición de la lista de la celda
                self.vars_values[cell].append(set(domain))  # Agrega el dominio de la jaula al final de la lista de la celda

    def print_board(self):
        """
        Imprime el tablero de Sudoku Killer con separadores y dominios en tres líneas.

        Este método muestra el tablero en un formato legible, incluyendo:
        - Separadores horizontales y verticales para delimitar filas, columnas y bloques 3x3.
        - El ID de la jaula y la suma objetivo en la primera línea de cada celda.
        - El dominio actual de cada celda, representado por los números del 1 al 9, en las siguientes tres líneas.
        Si un número está presente en el dominio, se muestra; si no, se muestra un espacio en blanco.

        No retorna ningún valor, pero muestra el tablero en la consola.
        """

        columnas = "ABCDEFGHI"
        filas = range(1, 10)

        def format_cell(cell_data):
            """
            Función auxiliar para formatear la información de una celda para la impresión.

            Args:
                cell_data (list): La lista que contiene la información de la celda [id_jaula, suma_jaula, dominio].

            Returns:
                list: Una lista de cadenas que representan las cuatro líneas de información de la celda.
            """
            if cell_data:
                cage_id, cage_sum, domain = cell_data
                cage_id_str = f"{cage_id:02}"  # Formatea el ID de la jaula con ceros a la izquierda si es necesario
                cage_sum_str = f"{cage_sum:02}"  # Formatea la suma de la jaula con ceros a la izquierda si es necesario

                domain_str = [str(num) if num in domain else " " for num in range(1, 10)]  # Valores del dominio
                domain_lines = [
                    " ".join(domain_str[0:3]),  # Divide el dominio en tres líneas
                    " ".join(domain_str[3:6]),
                    " ".join(domain_str[6:9])
                ]

                return [f"{cage_sum_str}-{cage_id_str}"] + domain_lines  # Suma-ID en la primera línea
            else:
                return ["----", "   ", "   ", "   "]  # Representación de una celda vacía

        # Imprime el borde superior
        print("+-------+-------+-------++-------+-------+-------++-------+-------+-------+")

        for fila in filas:
            for line_num in range(4):  # Itera a través de las líneas (información de la jaula + dominio)
                row_str = "| "  # Inicia la cadena de la fila
                for col_index, columna in enumerate(columnas):  # Itera a través de las columnas
                    cell = f"{columna}{fila}"  # Construye el nombre de la celda
                    cell_lines = format_cell(self.vars_values.get(cell))  # Obtiene los datos formateados de la celda
                    row_str += cell_lines[line_num]  # Agrega los datos de la celda a la fila

                    # Agrega separadores verticales (simples o dobles)
                    if (col_index + 1) % 3 == 0:
                        row_str += " || " if (col_index + 1) % 9 != 0 else " |"  # Doble o simple
                    else:
                        row_str += " | "

                print(row_str)  # Imprime la fila

            # Imprime separadores horizontales (simples o dobles)
            if fila % 3 == 0:
                print("+=======+=======+=======++=======+=======+=======++=======+=======+=======+")
            else:
                print("|-------+-------+-------++-------+-------+-------++-------+-------+-------|")

    def print_board2(self):
        """
        Imprime el tablero de Sudoku en un formato legible.

        Este método muestra el tablero con líneas horizontales y verticales para separar las filas,
        columnas y bloques 3x3. Las celdas resueltas se muestran con su valor,
        y las celdas sin resolver se muestran como espacios en blanco.

        No retorna ningún valor, pero muestra el tablero en la consola.
        """
        print("+-------+-------+-------+")  # Imprime la línea superior del tablero
        for fila in self.filas:  # Itera sobre cada fila (1, 2, 3, ...)
            print("|", end=" ")  # Imprime el separador vertical izquierdo de la fila
            for col in self.columnas:  # Itera sobre cada columna (A, B, C, ...)
                cell_key = self.columnas[list(self.filas).index(fila)] + str(self.columnas.index(col) + 1)  # Crea la clave de la celda (ej. "A1")
                if cell_key in self.vars_values and len(self.vars_values[cell_key][2]) == 1:  # Si la celda está en el diccionario y tiene un solo valor asignado
                    print(f"{list(self.vars_values[cell_key][2])[0]} ", end="")  # Imprime el valor de la celda
                else:
                    print("  ", end="")  # Si la celda no tiene un valor asignado, imprime un espacio en blanco
                if (self.columnas.index(col) + 1) % 3 == 0:  # Si se ha llegado al final de un bloque 3x3 en horizontal
                    print("|", end=" ")  # Imprime el separador vertical derecho del bloque
            print()  # Imprime un salto de línea al final de la fila
            if fila % 3 == 0:  # Si se ha llegado al final de un bloque 3x3 en vertical
                print("+-------+-------+-------+")  # Imprime la línea horizontal que separa los bloques 3x3

    def define_constraints(self):
        """
        Define y retorna las restricciones del Sudoku Killer.

        Este método crea una lista de conjuntos, donde cada conjunto representa una restricción específica del Sudoku.
        Las restricciones incluyen:
        - Restricciones de fila: Cada conjunto contiene las celdas que pertenecen a una misma fila.
        - Restricciones de columna: Cada conjunto contiene las celdas que pertenecen a una misma columna.
        - Restricciones de bloque 3x3: Cada conjunto contiene las celdas que pertenecen a un mismo bloque 3x3.
        - Restricciones de jaula: Cada conjunto contiene las celdas que pertenecen a una misma jaula, obtenidas del archivo JSON.

        Returns:
            list: Una lista de conjuntos que representan las restricciones del Sudoku.
        """
        restricciones = []  # Inicializa una lista vacía para almacenar las restricciones

        # Restricciones de filas:
        for col in self.columnas:  # Itera sobre cada columna
            vars = set()  # Crea un conjunto vacío para almacenar las celdas de la fila actual
            for fila in self.filas:  # Itera sobre cada fila
                vars.add(f"{col}{fila}")  # Agrega la celda actual al conjunto de la fila
            restricciones.append(vars)  # Agrega el conjunto de la fila a la lista de restricciones

        # Restricciones de columnas:
        for fila in self.filas:  # Itera sobre cada fila
            vars = set()  # Crea un conjunto vacío para almacenar las celdas de la columna actual
            for col in self.columnas:  # Itera sobre cada columna
                vars.add(f"{col}{fila}")  # Agrega la celda actual al conjunto de la columna
            restricciones.append(vars)  # Agrega el conjunto de la columna a la lista de restricciones

        # Restricciones de bloques 3x3:
        for i in range(3):  # Itera sobre los bloques en horizontal
            for j in range(3):  # Itera sobre los bloques en vertical
                vars = set()  # Crea un conjunto vacío para almacenar las celdas del bloque actual
                for col in self.columnas[i * 3:(i + 1) * 3]:  # Itera sobre las columnas del bloque
                    for fila in list(self.filas)[j * 3:(j + 1) * 3]:  # Itera sobre las filas del bloque
                        vars.add(f"{col}{fila}")  # Agrega la celda actual al conjunto del bloque
                restricciones.append(vars)  # Agrega el conjunto del bloque a la lista de restricciones

        # Restricciones de jaula:
        with open(self.file_path, 'r') as file:  # Abre el archivo JSON
            data = json.load(file)  # Carga los datos del archivo JSON

        for cage_data in data['cages']:  # Itera sobre cada jaula en los datos JSON
            cage_cells = set(cage_data['cells'])  # Crea un conjunto con las celdas de la jaula
            restricciones.append(cage_cells)  # Agrega el conjunto de la jaula a la lista de restricciones

        return restricciones  # Retorna la lista de restricciones

    def obvious_singles(self):
        """
        Aplica la estrategia de "singles obvios" al Sudoku Killer.

        Esta estrategia busca celdas que solo tienen un posible valor en su dominio.
        Si se encuentra una celda con un solo valor posible, ese valor se asigna a la celda
        y se elimina de los dominios de las demás celdas en la misma fila, columna, bloque 3x3 y jaula.

        No retorna ningún valor, pero modifica el estado interno del objeto `KillerSudokuSolver`
        actualizando los dominios de las celdas.
        """

        for constraint in self.restricciones:  # Itera sobre cada restricción (fila, columna, bloque, jaula)
            for key in constraint:  # Itera sobre cada celda dentro de la restricción actual
                if len(self.vars_values[key][2]) == 1:  # Si la celda tiene solo un valor posible en su dominio
                    for borrar_key in constraint:  # Itera sobre las demás celdas en la misma restricción
                        if borrar_key != key:  # Si la celda actual no es la misma que la celda con el single obvio
                            self.vars_values[borrar_key][2].discard(list(self.vars_values[key][2])[0])  # Elimina el valor del single obvio del dominio de la otra celda
                    self.update_domain(key)  # Actualiza el dominio de la celda después de aplicar la estrategia de singles obvios
            if len(constraint) == 2:
                pair_to_match = list(constraint)
                self.match_sum_pair_domains(pair_to_match[0], pair_to_match[1], self.vars_values[pair_to_match[0]][1])

    def update_domain(self, cell):
        """
        Actualiza el dominio de una celda en función de las restricciones de la jaula a la que pertenece.

        Este método se utiliza para reducir el dominio de una celda en una jaula después de que se ha asignado un valor
        a otra celda en la misma jaula. Recorre todas las restricciones de jaula, y si la celda dada pertenece a una de ellas,
        calcula la suma restante necesaria para cumplir con la restricción de la jaula. Luego, reduce el dominio de la celda
        a aquellos valores que aún podrían permitir que se cumpla la restricción de suma de la jaula.

        Args:
            cell (str): El nombre de la celda cuyo dominio se va a actualizar (ej. "A1").
        """
        for i in range(27, len(self.restricciones)):  # Itera sobre las restricciones de jaula (índices 27 en adelante)
            if cell in self.restricciones[i]:  # Si la celda pertenece a la restricción de jaula actual
                sum = self.vars_values[cell][1]  # Obtiene la suma objetivo de la jaula
                cells_to_update = []  # Lista para almacenar las celdas cuyo dominio se actualizará
                domains_to_update = []  # Lista para almacenar los dominios de las celdas a actualizar

                for cell1 in self.restricciones[i]:  # Itera sobre las celdas en la jaula
                    if len(self.vars_values[cell1][2]) == 1:  # Si la celda ya tiene un valor asignado
                        sum = sum - list(self.vars_values[cell1][2])[0]  # Resta el valor asignado de la suma objetivo
                    else:  # Si la celda aún no tiene un valor asignado
                        cells_to_update.append(cell1)  # Agrega la celda a la lista de celdas a actualizar
                        domains_to_update.append(self.vars_values[cell1][2])  # Agrega el dominio de la celda a la lista de dominios a actualizar

                reduced_domain = self.reduce_sum_domain(domains_to_update, sum)  # Llama a reduce_sum_domain para obtener el dominio reducido

                # Actualiza el dominio de las celdas
                for cell1 in cells_to_update:  # Itera sobre las celdas a actualizar
                    current_domain = self.vars_values[cell1][2]  # Obtiene el dominio actual de la celda
                    self.vars_values[cell1][2] = current_domain & reduced_domain  # Actualiza el dominio con la intersección del dominio actual y el dominio reducido
                    if len(cells_to_update) == 2:  # Si hay dos celdas en la jaula a actualizar
                        self.match_sum_pair_domains(cells_to_update[0], cells_to_update[1], sum)  # Llama a match_sum_pair_domains para jaulas de dos celdas

    def match_sum_pair_domains(self, cell1, cell2, target_sum):
        """
        Ajusta los dominios de dos celdas que deben sumar un número dado.

        Este método se utiliza específicamente para jaulas con dos celdas en un Sudoku Killer.
        Analiza los dominios de las dos celdas (`cell1` y `cell2`) y descarta los valores
        "impostores" (números que no pueden formar la suma objetivo `target_sum` con ningún
        número en el dominio de la otra celda).

        Esto asegura que los dominios de ambas celdas sean consistentes con la restricción
        de suma de la jaula y tengan la misma longitud.

        Args:
            cell1 (str): El nombre de la primera celda (ej. "A1").
            cell2 (str): El nombre de la segunda celda (ej. "B1").
            target_sum (int): La suma objetivo para las dos celdas.
        """

        domain1 = self.vars_values[cell1][2]  # Obtiene el dominio de la primera celda
        domain2 = self.vars_values[cell2][2]  # Obtiene el dominio de la segunda celda

        # Encuentra impostores en domain1
        impostors1 = set()  # Inicializa un conjunto para almacenar los impostores de la primera celda
        for num1 in domain1:  # Itera sobre cada valor en el dominio de la primera celda
            if not any(num1 != num2 and num1 + num2 == target_sum for num2 in domain2):  # Si no hay ningún valor en el dominio de la segunda celda que pueda sumar con num1 para alcanzar la suma objetivo
                impostors1.add(num1)  # Agrega num1 a los impostores de la primera celda

        # Encuentra impostores en domain2
        impostors2 = set()  # Inicializa un conjunto para almacenar los impostores de la segunda celda
        for num2 in domain2:  # Itera sobre cada valor en el dominio de la segunda celda
            if not any(num1 != num2 and num1 + num2 == target_sum for num1 in domain1):  # Si no hay ningún valor en el dominio de la primera celda que pueda sumar con num2 para alcanzar la suma objetivo
                impostors2.add(num2)  # Agrega num2 a los impostores de la segunda celda

        # Descarta impostores de ambos dominios
        domain1.difference_update(impostors1)  # Elimina los impostores del dominio de la primera celda
        domain2.difference_update(impostors2)  # Elimina los impostores del dominio de la segunda celda

        # Actualiza los dominios en self.vars_values
        self.vars_values[cell1][2] = domain1  # Actualiza el dominio de la primera celda en el diccionario vars_values
        self.vars_values[cell2][2] = domain2  # Actualiza el dominio de la segunda celda en el diccionario vars_values

    def reduce_sum_domain(self, sets, target_sum):
        """
        Calcula los números de múltiples conjuntos que suman un valor dado, sin repetir números.

        Este método se utiliza para reducir el dominio de las celdas en una jaula en un Sudoku Killer.
        Toma una lista de conjuntos (`sets`), donde cada conjunto representa el dominio de una celda en la jaula,
        y un valor objetivo (`target_sum`).

        El método genera todas las combinaciones posibles de números de los conjuntos de entrada y selecciona
        aquellas combinaciones que cumplen las siguientes condiciones:
        - La suma de los números en la combinación es igual a `target_sum`.
        - Todos los números en la combinación son únicos (no hay repeticiones).

        Luego, devuelve un conjunto que contiene todos los números que forman parte de al menos una combinación válida.

        Args:
            sets (list): Una lista de conjuntos, donde cada conjunto contiene números.
            target_sum (int): La suma objetivo.

        Returns:
            set: Un conjunto que contiene los números de los conjuntos de entrada que pueden formar la suma objetivo.
        """

        result = set()  # Inicializa un conjunto vacío para almacenar los resultados

        # Genera todas las combinaciones posibles de números de los conjuntos
        for combination in itertools.product(*sets):  # Itera sobre todas las combinaciones posibles de números de los conjuntos de entrada utilizando itertools.product
            # Verifica si la combinación tiene números distintos y suma la suma objetivo
            if len(set(combination)) == len(combination) and sum(combination) == target_sum:  # Si la combinación tiene números distintos (sin repeticiones) y la suma de los números es igual a target_sum
                result.update(combination)  # Agrega los números de la combinación válida al conjunto de resultados

        # Descarta números inutilizables
        discard_sets = [set() for _ in range(len(sets))]  # Crea una lista de conjuntos vacíos para almacenar los números a descartar de cada conjunto de entrada

        for i, current_set in enumerate(sets):  # Itera sobre cada conjunto de entrada y su índice
            for num in current_set:  # Itera sobre cada número en el conjunto actual
                is_usable = False  # Inicializa una bandera para indicar si el número es utilizable
                # Itera a través de combinaciones de otros conjuntos para verificar la usabilidad
                for other_combination in itertools.product(*[s for j, s in enumerate(sets) if j != i]):  # Itera sobre las combinaciones de números de los otros conjuntos (excluyendo el conjunto actual)
                    combined = (num,) + other_combination  # Crea una combinación que incluye el número actual y la combinación de los otros conjuntos
                    # Verifica si los números combinados son distintos y suman la suma objetivo
                    if len(set(combined)) == len(combined) and sum(combined) == target_sum:  # Si la combinación tiene números distintos y la suma de los números es igual a target_sum
                        is_usable = True  # Marca el número como utilizable
                        break  # Sale del bucle interno, ya que se ha encontrado una combinación válida que usa el número actual
                if not is_usable:  # Si el número no es utilizable
                    discard_sets[i].add(num)  # Agrega el número al conjunto de números a descartar del conjunto actual

        # Resultado final: unión de todos los conjuntos menos los números descartados
        final_result = set()  # Inicializa un conjunto vacío para almacenar el resultado final
        for i, current_set in enumerate(sets):  # Itera sobre cada conjunto de entrada y su índice
            final_result.update(current_set.difference(discard_sets[i]))  # Agrega los números del conjunto actual que no están en el conjunto de números a descartar al resultado final

        return final_result  # Devuelve el resultado final

    def extract_domains_outsiders(self, length, value):
        """
        Calcula el conjunto de dígitos posibles (1-9) que pueden formar una
        secuencia de una longitud dada que suma un valor dado, permitiendo la repetición.

        Este método se utiliza en la técnica de "outsiders" para determinar los posibles valores
        de celdas que están fuera de una región específica (como un bloque 3x3) pero que
        están relacionadas por restricciones de jaulas.

        Args:
            length (int): La longitud de la secuencia de dígitos.
            value (int): La suma deseada de la secuencia de dígitos.

        Returns:
            set: Un conjunto que contiene todos los dígitos posibles que pueden
                  formar la secuencia con la longitud y suma especificadas.
        """
        possible_digits = set()

        # Genera todas las combinaciones con reemplazo
        for combination in itertools.combinations_with_replacement(range(1, 10), length):
            if sum(combination) == value:
                possible_digits.update(combination)  # Agrega dígitos únicos al conjunto

        return possible_digits

    def outsiders(self):
        """
        Aplica la técnica de "outsiders" al Sudoku Killer.

        Esta técnica se enfoca en jaulas que se extienden a través de múltiples bloques 3x3.
        Analiza las restricciones de adyacencia definidas en `adjacent_constraints` para
        identificar posibles valores en celdas fuera de la región principal de la jaula
        que podrían influir en la suma total de la jaula.

        Si se encuentra que ciertos valores en estas celdas "outsiders" son necesarios
        para satisfacer la restricción de suma de la jaula, esos valores se mantienen
        en el dominio de la celda, mientras que otros valores se descartan.

        Returns:
            bool: True si se realizaron cambios en el tablero (dominios de celdas),
                  False en caso contrario.
        """
        changes_made = False  # Inicializa una variable para rastrear si se realizaron cambios

        # Itera sobre las restricciones de adyacencia por número de bloques adyacentes
        for num_adjacent, constraints in self.adjacent_constraints.items():
            for constraint in constraints:  # Itera sobre cada restricción en la lista
                ids_in_constraint = []  # Lista para almacenar los IDs de jaula en la restricción
                cells_in_constraint = set()  # Conjunto para almacenar las celdas en la restricción
                cages_sum = 0  # Variable para acumular la suma de las jaulas en la restricción

                # Recopila información sobre las jaulas en la restricción
                for cell in constraint:
                    if self.vars_values[cell][0] not in ids_in_constraint:
                        ids_in_constraint.append(self.vars_values[cell][0])  # Agrega el ID de jaula si no está presente
                        cages_sum = cages_sum + self.vars_values[cell][1]  # Acumula la suma de la jaula

                # Encuentra todas las celdas que pertenecen a las jaulas en la restricción
                for j in range(27, len(self.restricciones)):
                    for id in ids_in_constraint:
                        for cell in self.restricciones[j]:
                            if id == self.vars_values[cell][0]:
                                cells_in_constraint.add(cell)  # Agrega la celda al conjunto

                # Excluye las celdas que ya están en la restricción original
                cells_in_constraint = cells_in_constraint.difference(constraint)
                if len(cells_in_constraint) > 4:
                    continue  # Salta la restricción si involucra más de 4 celdas externas

                # Calcula el dominio de las celdas externas utilizando la función extract_domains_outsiders
                domain = self.extract_domains_outsiders(len(cells_in_constraint), cages_sum - 45 * num_adjacent)

                # Si se encuentra un dominio válido, actualiza los dominios de las celdas externas
                if domain != set():
                    for cell in cells_in_constraint:
                        self.vars_values[cell][2] = self.vars_values[cell][2].intersection(set(domain))
                        changes_made = True  # Marca que se realizaron cambios en el tablero

                ids_in_constraint = []
                cells_in_constraint = set()
                cages_sum = 0

        return changes_made  # Devuelve True si se realizaron cambios, False en caso contrario

    def hidden_singles(self):
        """
        Aplica la estrategia de "Hidden Singles" (Singles Ocultos) al Sudoku Killer.

        Esta estrategia busca celdas dentro de una restricción (fila, columna o bloque 3x3)
        donde un valor candidato solo puede aparecer en una única celda. Si se encuentra
        tal valor, se convierte en el único valor posible para esa celda (un "Hidden Single").

        La estrategia funciona examinando cada restricción y cada valor candidato (1-9).
        Si un valor candidato solo aparece una vez en el dominio de las celdas dentro
        de esa restricción, entonces ese valor debe ser asignado a esa celda.

        Returns:
            bool: True si se realizaron cambios en el tablero (dominios de celdas),
                  False en caso contrario.
        """

        changes_made = False  # Inicializa una variable para rastrear si se realizaron cambios

        # Itera sobre las restricciones (filas, columnas, bloques 3x3)
        for constraint in self.restricciones[:27]:  # Solo considera las primeras 27 restricciones (filas, columnas, bloques)
            # Obtiene los dominios de las celdas en la restricción actual
            constraint_domains = [self.vars_values[cell][2] for cell in constraint if self.vars_values[cell]]

            # Busca Hidden Singles para cada dígito (1-9)
            for digit in range(1, 10):
                count = 0  # Contador para la cantidad de veces que aparece el dígito en la restricción
                cell_with_digit = None  # Variable para almacenar la celda que contiene el dígito

                # Itera sobre las celdas en la restricción
                for cell in constraint:
                    if self.vars_values[cell] and digit in self.vars_values[cell][2]:
                        count += 1  # Incrementa el contador si el dígito está en el dominio de la celda
                        cell_with_digit = cell  # Guarda la celda que contiene el dígito

                # Si el dígito aparece solo una vez en la restricción
                if count == 1 and cell_with_digit:
                    # print(f"Hidden single found: Cell {cell_with_digit} must be {digit}")  # (Opcional) Imprime un mensaje para indicar que se encontró un Hidden Single
                    self.vars_values[cell_with_digit][2] = {digit}  # Actualiza el dominio de la celda para contener solo el dígito
                    changes_made = True  # Marca que se realizaron cambios en el tablero

        return changes_made  # Devuelve True si se realizaron cambios, False en caso contrario

    def pointing_pairs(self):
        # Iterar por cada bloque 3x3
        # range(0, 9, 3), itera de 0 a 8 de 3 en 3
        changesMade = False  # Inicializa una bandera para rastrear si se hicieron cambios

        for block_start_row in range(0, 9, 3):
            for block_start_col in range(0, 9, 3):
                # Crear las celdas para el bloque actual
                # chr(65 + col) crea el id alfabético (A, B, C...) de la columna en conjunto con el id para fila, creando identificador de celda (ej: A1)
                block_cells = [
                    f"{chr(65 + col)}{row + 1}"
                    for row in range(block_start_row, block_start_row + 3)
                    for col in range(block_start_col, block_start_col + 3)
                ]
                # Objeto para posicionar y contar las coincidencias de dominios en una misma fila o columna
                # ej: {1: ["A2", "A3"], 2: []... hasta 9}
                candidates = {num: [] for num in range(1, 10)}

                # Obtener las celdas y dominios del bloque
                for cell in block_cells:
                    if cell in self.vars_values:
                        domain = self.vars_values[cell][2]
                        for num in domain:
                            # Se recorren los dominios de cada celda y se agrega el id de la celda al candidato coincidente con num
                            candidates[num].append(cell)

                # Recorrer candidatos en busca de pointing pairs
                for num, cells in candidates.items():
                    # El bloque debe de tener dos coincidencias para aplicar pointing pairs
                    # Existe la posibilidad de que en esta sección de código se pueda aplicar también triples, añadiendo: len(cells) == 3. (Debe de ser testeado y comparar con la solución de Juan)
                    if len(cells) == 2:
                        # rows mantiene un rastreo de las filas en donde se encuentra el candidato actual (num), únicamente guarda el id de row. (ej: 1)
                        # cell[1] es el id de la fila
                        rows = {cell[1] for cell in cells}
                        # cols mantiene un rastreo de las columnas en donde se encuentra num, guarda el id alfabético asociado a las columnas coincidentes. (ej: B)
                        # cell[0] es el carácter alfabético de la columna
                        cols = {cell[0] for cell in cells}  # Columna de cada celda

                        # Si solo existe un elemento en rows, significa que las coincidencias de num están en la misma fila, repartidos por la columna
                        if len(rows) == 1:
                            row = next(iter(rows))
                            # Elimina los elementos coincidentes de las celdas, en la fila
                            for col in "ABCDEFGHI":
                                # Crea los ids de celdas en la misma fila
                                cell = f"{col}{row}"
                                # Comprueba que el id de la celda generada no pertenezca al bloque perteneciente a la celda que está siendo evaluada antes de eliminar el candidato
                                if cell not in cells and cell in self.vars_values:
                                    self.vars_values[cell][2].discard(num)
                                    changesMade = True
                        # En caso de que exista solo una columna, significa que las coincidencias están en la misma columna, repartidos por la fila
                        elif len(cols) == 1:
                            col = next(iter(cols))
                            for row in range(1, 10):
                                # Recrea los ids de las celdas pertenecientes a la misma columna de la celda del bloque que está siendo evaluada
                                cell = f"{col}{row}"
                                # Comprueba que el id de la celda generado no pertenezca al bloque actual antes de eliminarlo
                                if cell not in cells and cell in self.vars_values:
                                    self.vars_values[cell][2].discard(num)
                                    changesMade = True

        return changesMade  # Devuelve la bandera para indicar si se hicieron cambios


    def obvious_pairs(self):
        """
        Aplica la estrategia de "Obvious Pairs" (Pares Obvios) al Sudoku Killer.

        Esta estrategia busca pares de celdas dentro de una misma restricción (fila, columna
        o bloque 3x3) que tengan exactamente los mismos dos candidatos en sus dominios.

        Si se encuentra un par de este tipo, significa que esos dos candidatos deben estar
        en esas dos celdas (aunque no se sabe en qué orden). Por lo tanto, esos dos
        candidatos pueden ser eliminados de los dominios de todas las demás celdas
        en la misma restricción.

        Returns:
            bool: True si se realizaron cambios en el tablero (dominios de celdas),
                  False en caso contrario.
        """

        changes_made = False  # Inicializa una variable para rastrear si se realizaron cambios

        for constraint in self.restricciones:  # Itera sobre las restricciones (filas, columnas, bloques, jaulas)
            pairs = {}  # Diccionario para almacenar los pares de candidatos y las celdas que los contienen

            for cell in constraint:  # Itera sobre las celdas en la restricción actual
                if self.vars_values[cell] and len(self.vars_values[cell][2]) == 2:  # Si la celda tiene un dominio de tamaño 2
                    pair_values = tuple(sorted(list(self.vars_values[cell][2])))  # Obtiene los dos candidatos de la celda, ordenados
                    if pair_values in pairs:  # Si este par de candidatos ya está en el diccionario
                        pairs[pair_values].append(cell)  # Agrega la celda a la lista de celdas que contienen este par
                    else:
                        pairs[pair_values] = [cell]  # Crea una nueva entrada en el diccionario para este par de candidatos

            for pair_values, cells in pairs.items():  # Itera sobre los pares de candidatos y las celdas que los contienen
                if len(cells) == 2:  # Si hay dos celdas con el mismo par de candidatos
                    #print(f"Obvious pair found: Cells {cells[0]} and {cells[1]} must be {pair_values[0]} and {pair_values[1]}")  # (Opcional) Imprime un mensaje para indicar que se encontró un Obvious Pair
                    for cell in constraint:  # Itera sobre las celdas en la restricción actual
                        if cell not in cells and self.vars_values[cell]:  # Si la celda no es una de las celdas del par y tiene un dominio
                            if pair_values[0] in self.vars_values[cell][2] or pair_values[1] in self.vars_values[cell][2]:  # Si alguno de los candidatos del par está en el dominio de la celda
                                self.vars_values[cell][2].discard(pair_values[0])  # Elimina el primer candidato del dominio de la celda
                                self.vars_values[cell][2].discard(pair_values[1])  # Elimina el segundo candidato del dominio de la celda
                                changes_made = True  # Marca que se realizaron cambios en el tablero

        return changes_made  # Devuelve True si se realizaron cambios, False en caso contrario

    def obvious_triples(self):
        """
        Aplica la estrategia de Triples Obvios al rompecabezas de Sudoku.
        Identifica celdas con solo tres valores posibles en su dominio, y
        si esos tres valores son los mismos en tres celdas en la misma restricción,
        los elimina del dominio de otras celdas en esa restricción.

        Actualizaciones:
            self.vars_values: Actualiza el dominio de las celdas basado en la estrategia de Triples Obvios.

        Retorna:
            bool: True si se hicieron cambios en el tablero, False en caso contrario.
        """

        changes_made = False  # Inicializa una bandera para rastrear si se encontraron triples

        for constraint in self.restricciones:  # Itera a través de cada restricción
            # Encuentra todas las celdas en la restricción con un dominio de tamaño 3
            cells_with_3_domain = [cell for cell in constraint if self.vars_values[cell] and len(self.vars_values[cell][2]) == 3]

            if len(cells_with_3_domain) >= 3:
                # Si hay al menos 3 celdas con un dominio de tamaño 3 en la restricción
                for cell_group in itertools.combinations(cells_with_3_domain, 3):
                    # Considera todas las combinaciones de 3 celdas
                    if self.vars_values[cell_group[0]][2] == self.vars_values[cell_group[1]][2] == self.vars_values[cell_group[2]][2]:
                        # Si los dominios de las 3 celdas son iguales
                        triple_values = self.vars_values[cell_group[0]][2]  # Obtén los valores del triple

                        # Elimina los valores del triple de otras celdas en la restricción
                        for cell in constraint:
                            if cell not in cell_group and self.vars_values[cell]:
                                old_domain = set(self.vars_values[cell][2])  # Copia el dominio antes de cualquier cambio
                                self.vars_values[cell][2] = self.vars_values[cell][2].difference(triple_values)  # Elimina los valores del triple
                                if old_domain != self.vars_values[cell][2]:  # Verifica si el dominio realmente cambió
                                    changes_made = True  # Establece la bandera a True si se hicieron cambios

        return changes_made  # Devuelve la bandera para indicar si se hicieron cambios

    def pointing_triples(self):
        """
        Aplica la estrategia de "Pointing Triples" (Triples Apuntadores) al Sudoku Killer.

        Esta estrategia busca trios de candidatos que aparecen únicamente dentro de un mismo
        bloque 3x3 y en la misma fila o columna. Si se encuentra un trío de este tipo,
        se puede eliminar de las demás celdas de esa fila o columna fuera del bloque.

        La lógica es que si esos tres candidatos solo pueden estar en tres celdas dentro del
        bloque, entonces al menos uno de ellos debe estar en una de esas tres celdas.
        Por lo tanto, no pueden estar en ninguna otra celda de la misma fila o columna
        fuera del bloque.

        Returns:
            bool: True si se realizaron cambios en el tablero (dominios de celdas),
                  False en caso contrario.
        """
        initial_board = copy.deepcopy(self.vars_values)  # Crea una copia del tablero actual para comparar y detectar cambios.
        changes_made = False  # Inicializa una variable para rastrear si se realizaron cambios en el tablero.
        for i in range(18, 27):  # Itera a través de las restricciones de bloque (índices 18 a 26 en la lista de restricciones, que representan los 9 bloques 3x3).
            for j in range(0, 18):  # Itera a través de las restricciones de fila y columna (índices 0 a 17 en la lista de restricciones, que representan las 9 filas y 9 columnas).
                cell_intersection = list(self.restricciones[i] & self.restricciones[j])  # Obtiene la intersección entre el bloque actual y la fila/columna actual, es decir, las celdas que pertenecen a ambos.
                if len(cell_intersection) > 0:  # Si hay celdas en la intersección (es decir, celdas compartidas entre el bloque y la fila/columna).
                    possible_nums = self.vars_values[cell_intersection[0]][2] & self.vars_values[cell_intersection[1]][2] & self.vars_values[cell_intersection[2]][2]  # Obtiene los números posibles (candidatos) que están presentes en el dominio de las tres primeras celdas de la intersección.
                    cell_difference1 = self.restricciones[i] - self.restricciones[j]  # Obtiene las celdas que están en el bloque actual pero no en la fila/columna actual.
                    cell_difference2 = self.restricciones[j] - self.restricciones[i]  # Obtiene las celdas que están en la fila/columna actual pero no en el bloque actual.

                    difference1_domain = set()  # Inicializa un conjunto para almacenar los dominios de las celdas en cell_difference1.
                    difference2_domain = set()  # Inicializa un conjunto para almacenar los dominios de las celdas en cell_difference2.

                    for cell in cell_difference1:  # Itera sobre las celdas en cell_difference1 (celdas en el bloque pero no en la fila/columna).
                        difference1_domain = difference1_domain | self.vars_values[cell][2]  # Agrega el dominio de la celda actual al conjunto difference1_domain.

                    for cell in cell_difference2:  # Itera sobre las celdas en cell_difference2 (celdas en la fila/columna pero no en el bloque).
                        difference2_domain = difference2_domain | self.vars_values[cell][2]  # Agrega el dominio de la celda actual al conjunto difference2_domain.

                    for num in possible_nums:  # Itera sobre cada número posible (candidato) en la intersección.
                        if num not in difference1_domain:  # Si el número posible no está en el dominio de las celdas en cell_difference1 (bloque - fila/columna).
                            for cell in cell_difference2:  # Itera sobre las celdas en cell_difference2 (fila/columna - bloque).
                                self.vars_values[cell][2].discard(num)  # Elimina el número posible (candidato) del dominio de la celda actual en cell_difference2.

                        if num not in difference2_domain:  # Si el número posible no está en el dominio de las celdas en cell_difference2 (fila/columna - bloque).
                            for cell in cell_difference1:  # Itera sobre las celdas en cell_difference1 (bloque - fila/columna).
                                self.vars_values[cell][2].discard(num)  # Elimina el número posible (candidato) del dominio de la celda actual en cell_difference1.

        final_board = copy.deepcopy(self.vars_values)  # Crea una copia del tablero después de aplicar la estrategia Pointing Triples.

        if initial_board == final_board:  # Compara el tablero inicial con el tablero final.
            return False  # Si no hay cambios, retorna False (no se realizaron cambios en el tablero).
        else:
            return True  # Si hay cambios, retorna True (se realizaron cambios en el tablero).

    def apply_rules(self, log=False):  # Agrega el parámetro 'log' con valor predeterminado False
        """
        Aplica las reglas de inferencia (estrategias) al Sudoku Killer.

        Este método llama a las diferentes estrategias de inferencia para
        reducir los dominios de las celdas del Sudoku Killer. Las estrategias
        incluyen: obvious_singles, obvious_triples, obvious_pairs,
        pointing_triples, pointing_pairs, hidden_singles.

        El método aplica las estrategias en un orden específico y verifica
        si se realizaron cambios en el tablero después de cada aplicación.

        Args:
            log (bool, optional): Si es True, imprime mensajes indicando
                                qué estrategia se aplicó. Defaults to False.

        Returns:
            bool: True si se realizaron cambios en el tablero (dominios de celdas),
                  False en caso contrario.
        """
        initial_board = copy.deepcopy(self.vars_values)  # Crea una copia del tablero inicial para comparar cambios.
        self.obvious_singles()  # Aplica la regla de "singles obvios".
        if self.obvious_triples():  # Si se aplicó la regla de "triples obvios"...
            if log: print("Se aplicó la estrategia obvious triples")  # Imprime si log es True
            self.obvious_singles()  # ...vuelve a aplicar la regla de "singles obvios".
        if self.obvious_pairs():  # Si se aplicó la regla de "pares obvios"...
            if log: print("Se aplicó la estrategia obvious pairs")  # Imprime si log es True
            self.obvious_singles()  # ...vuelve a aplicar la regla de "singles obvios".
        if self.pointing_triples():  # Si se aplicó la regla de "pointing triples"...
            if log: print("Se aplicó la estrategia pointing triples")  # Imprime si log es True
            self.obvious_singles()  # ...vuelve a aplicar la regla de "singles obvios".
        if self.pointing_pairs():  # Si se aplicó la regla de "pointing pairs"...
            if log: print("Se aplicó la estrategia pointing pairs")  # Imprime si log es True
            self.obvious_singles()  # ...vuelve a aplicar la regla de "singles obvios".
        if self.hidden_singles():  # Si se aplicó la regla de "hidden singles"...
            if log: print("Se aplicó la estrategia hidden singles")  # Imprime si log es True
            self.obvious_singles()  # ...vuelve a aplicar la regla de "singles obvios".

        if initial_board == self.vars_values:  # Compara el tablero actual con el tablero inicial.
            return False  # Si no hay cambios, retorna False (no se realizaron cambios en el tablero).
        else:
            return True  # Si hay cambios, retorna True (se realizaron cambios en el tablero).

    def solver(self, log=False):
        """
        Resuelve el Sudoku Killer utilizando una combinación de estrategias y backtracking.

        Este método primero aplica las estrategias outsiders y las reglas del Sudoku (obvious singles,
        hidden singles, pointing pairs, obvious pairs) para reducir el dominio de las variables.
        Si el Sudoku no se resuelve con estas estrategias, utiliza un enfoque de backtracking para explorar
        diferentes combinaciones de valores para las celdas seleccionadas.

        Args:
            log (bool, optional): Si es True, imprime información sobre las asignaciones de valores durante
                                  el proceso de backtracking. Defaults to False.

        Returns:
            bool: True si se encuentra una solución, False en caso contrario.
        """

        # Aplica la técnica de 'outsiders' para reducir los dominios de las celdas.
        self.outsiders()
        if log:
            print("Se aplicó la estrategia outsiders")
        # Entra en un bucle que aplica las reglas del Sudoku hasta que no haya más cambios.
        while True:
            # Aplica las reglas del Sudoku (obvious singles, hidden singles, pointing pairs, obvious pairs).
            if not self.apply_rules(log):
                # Si no hay cambios, sale del bucle.
                break

        # Verifica si el Sudoku ya está resuelto después de aplicar las reglas.
        if not self.is_solved(self.vars_values):
            # Si no está resuelto, selecciona celdas para el backtracking.
            cells_to_change = ["A1", "C3", "G7", "I9"]
            # Crea una lista para almacenar los dominios de las celdas seleccionadas.
            values_to_change = []

            # Itera sobre las celdas seleccionadas para obtener sus dominios.
            for i in range(4):
                # Obtiene el dominio de la celda actual.
                values = self.vars_values[cells_to_change[i]][2]
                # Agrega el dominio a la lista de dominios.
                values_to_change.append(list(values))

            # Itera sobre todas las combinaciones posibles de valores para las celdas seleccionadas.
            for values in product(*values_to_change):
                # Verifica si la combinación de valores es consistente con las restricciones del Sudoku.
                if self.is_consistent(cells_to_change, values):
                    # Si es consistente, crea una copia temporal de los valores de las variables.
                    temp_vars_values = copy.deepcopy(self.vars_values)
                    # Asigna los valores de la combinación actual a las celdas seleccionadas.
                    for i in range(4):
                        self.vars_values[cells_to_change[i]][2] = {values[i]}

                    # Imprime información sobre las asignaciones si log=True.
                    if log:
                        # Crea una cadena con las asignaciones de valores.
                        assignment_str = ", ".join([f"{cells_to_change[i]}: {values[i]}" for i in range(4)])
                        # Imprime la cadena de asignaciones.
                        print(f"Valores asignados: {assignment_str}")

                    # Aplica las reglas del Sudoku hasta que no haya más cambios.
                    while True:
                        # Aplica las reglas del Sudoku.
                        if not self.apply_rules(log):
                            # Si no hay cambios, sale del bucle.
                            break

                    # Verifica si el Sudoku está resuelto después de aplicar las reglas.
                    if self.is_solved(self.vars_values):
                        # Si está resuelto, retorna True.
                        return True
                    else:
                        if log:
                            print("No se encontró solución en esta rama")
                        # Si no está resuelto, restaura los valores de las variables a la copia temporal.
                        self.vars_values = copy.deepcopy(temp_vars_values)

        # Si no se encontró una solución, retorna False.
        return False

    def is_consistent(self, cells, values):
        """
        Verifica si la asignación de valores a las celdas es consistente con las restricciones del Sudoku.

        Este método comprueba si la asignación de los valores dados a las celdas especificadas
        viola alguna de las restricciones del Sudoku, como la unicidad de valores en filas,
        columnas, bloques 3x3 y jaulas.

        Args:
            cells (list): Una lista de nombres de celdas (ej. ["A1", "B2", "C3"]) a las que se asignarán valores.
            values (list): Una lista de valores correspondientes a las celdas (ej. [1, 2, 3]).

        Returns:
            bool: True si la asignación es consistente (no hay conflictos), False en caso contrario.
        """

        # Crea una copia temporal de vars_values para evitar modificar el original.
        temp_vars_values = copy.deepcopy(self.vars_values)

        # Asigna los valores a las celdas en la copia temporal.
        for cell, value in zip(cells, values):
            # Si la celda ya tiene un valor fijo y es diferente del nuevo valor, es inconsistente.
            # O si el valor no está en el dominio, es inconsistente.
            # Se utiliza el método get para evitar KeyError.
            # Si la clave no existe o no tiene valor, devuelve None. Esto se verifica más adelante.
            if (temp_vars_values.get(cell) and len(temp_vars_values[cell][2]) == 1 and list(temp_vars_values[cell][2])[0] != value) or \
              (temp_vars_values.get(cell) and value not in temp_vars_values[cell][2]):
                return False  # La asignación es inconsistente

            # Solo si la celda no fue inicializada (en el archivo .json),
            # se inicializa con el nuevo valor y un dominio de solo este valor.
            if not temp_vars_values.get(cell):
                temp_vars_values[cell] = [0, 0, {value}]

        # Verifica si hay conflictos en filas, columnas y bloques 3x3.
        for constraint in self.restricciones[:27]:  # Itera sobre las restricciones de filas, columnas y bloques
            values_in_constraint = []  # Lista para almacenar los valores en la restricción actual
            for cell in constraint:  # Itera sobre las celdas en la restricción actual
                if temp_vars_values.get(cell) and len(temp_vars_values[cell][2]) == 1:  # Si la celda tiene un valor asignado
                    values_in_constraint.append(list(temp_vars_values[cell][2])[0])  # Agrega el valor a la lista
                elif not temp_vars_values.get(cell):  # Si la celda no fue inicializada en el archivo JSON
                    for cell2, value2 in zip(cells, values):  # Busca la celda en la lista de celdas a asignar
                        if cell == cell2:  # Si la celda coincide
                            values_in_constraint.append(value2)  # Agrega el valor a la lista
                            break  # Sale del bucle interno

            # Verifica si hay valores duplicados en la restricción.
            if len(values_in_constraint) != len(set(values_in_constraint)):
                return False  # Inconsistent if duplicates are found

        return True  # Consistent if no conflicts are found

    def is_solved(self, board):
        """
        Verifica si el Sudoku está resuelto, es decir, si todas las celdas tienen un único valor asignado
        y el tablero es consistente con las restricciones.

        Returns:
            bool: True si el Sudoku está resuelto, False en caso contrario.
        """
        if board is None:  # Verifica si board es None
            return False  # Si es None, el Sudoku no está resuelto
        # Verificar si todas las celdas tienen un único valor asignado
        for cell in board:
            if len(board[cell][2]) != 1:
                return False  # Si alguna celda tiene más de un valor posible, el Sudoku no está resuelto
        return True  # Si todas las celdas tienen un único valor y el tablero es consistente, el Sudoku está resuelto

    def define_adjacent_constraints(self):
        """
        Define las restricciones de adyacencia para columnas, filas y bloques 3x3.

        Este método crea un diccionario donde las claves representan el número de restricciones adyacentes (de 1 a 9)
        y los valores son listas de conjuntos que contienen las celdas correspondientes a esas restricciones.
        Las restricciones de adyacencia se utilizan en la técnica de "outsiders" para identificar posibles
        valores en celdas fuera de una región específica que podrían influir en la suma total de una jaula.

        Returns:
            dict: Un diccionario que contiene las restricciones de adyacencia.
                  Las claves son el número de restricciones adyacentes (1 a 9).
                  Los valores son listas de conjuntos de celdas que corresponden a esas restricciones.
        """
        adjacent_constraints = {}  # Inicializa el diccionario de restricciones adyacentes

        # Columnas:
        for num_adjacent in range(1, 10):  # Itera para 1 a 9 columnas adyacentes
            adjacent_constraints[num_adjacent] = []  # Inicializa la lista de restricciones para el número actual de adyacencias
            for start_col_index in range(len(self.columnas) - num_adjacent + 1):  # Itera sobre las posibles columnas de inicio
                cells_set = set()  # Inicializa un conjunto para almacenar las celdas de la restricción actual
                for col_index in range(start_col_index, start_col_index + num_adjacent):  # Itera sobre las columnas adyacentes
                    for fila in self.filas:  # Itera sobre las filas para agregar las celdas al conjunto
                        cells_set.add(f"{self.columnas[col_index]}{fila}")  # Agrega la celda al conjunto
                adjacent_constraints[num_adjacent].append(cells_set)  # Agrega el conjunto de celdas a la lista de restricciones

        # Filas:
        for num_adjacent in range(1, 10):  # Itera para 1 a 9 filas adyacentes
            adjacent_constraints[num_adjacent] = adjacent_constraints.get(num_adjacent, [])  # Obtiene la lista de restricciones o la inicializa si no existe
            for start_row in range(1, 10 - num_adjacent + 1):  # Itera sobre las posibles filas de inicio
                cells_set = set()  # Inicializa un conjunto para almacenar las celdas de la restricción actual
                for row in range(start_row, start_row + num_adjacent):  # Itera sobre las filas adyacentes
                    for col in self.columnas:  # Itera sobre las columnas para agregar las celdas al conjunto
                        cells_set.add(f"{col}{row}")  # Agrega la celda al conjunto
                adjacent_constraints[num_adjacent].append(cells_set)  # Agrega el conjunto de celdas a la lista de restricciones

        # Bloques 3x3:
        blocks = self.restricciones[18:27]  # Obtiene las restricciones de bloques 3x3 de la lista de restricciones

        for i in range(18, 27):  # Agrega cada bloque 3x3 como una restricción adyacente individual
            adjacent_constraints[1].append(self.restricciones[i])

        # Define la adyacencia de bloques usando combinaciones:
        for num_adjacent in range(1, 10):
            # Inicializa una lista vacía para el número actual de bloques adyacentes si no existe
            adjacent_constraints[num_adjacent] = adjacent_constraints.get(num_adjacent, [])
            # Genera todas las combinaciones de bloques con el número actual de bloques adyacentes
            for block_combination in combinations(blocks, num_adjacent):
                # Verifica si todos los bloques en la combinación son adyacentes entre sí (continuos)
                # Obtiene los índices de los bloques en la combinación
                block_indices = [self.restricciones.index(block) - 18 for block in block_combination]
                # Verifica si todos los bloques son adyacentes a al menos otro bloque en la combinación
                is_continuous = all(
                    any(self.are_blocks_adjacent(block_indices[i], block_indices[j]) for j in range(len(block_indices)) if i != j)
                    for i in range(len(block_indices))
                )

                # Si los bloques son continuos, crea un conjunto de celdas y lo agrega a la lista
                if is_continuous:
                    # Une todas las celdas de los bloques en la combinación
                    cells_set = set().union(*block_combination)
                    # Agrega el conjunto de celdas a la lista de restricciones adyacentes
                    adjacent_constraints[num_adjacent].append(cells_set)

        return adjacent_constraints  # Retorna el diccionario de restricciones adyacentes

    def are_blocks_adjacent(self, block1_index, block2_index):
        """
        Verifica si dos bloques 3x3 son adyacentes (horizontal o verticalmente, no diagonalmente).

        Esta función determina si dos bloques 3x3 en el tablero de Sudoku son adyacentes,
        considerando la adyacencia horizontal y vertical, pero no la diagonal.

        Args:
            block1_index (int): Índice del primer bloque (0-8).
            block2_index (int): Índice del segundo bloque (0-8).

        Returns:
            bool: True si los bloques son adyacentes, False en caso contrario.
        """
        # Calcula la diferencia en filas y columnas entre los dos bloques
        row_diff = abs(block1_index // 3 - block2_index // 3)  # Diferencia en filas
        col_diff = abs(block1_index % 3 - block2_index % 3)  # Diferencia en columnas

        # Verifica si los bloques son adyacentes y no son el mismo bloque
        # (row_diff <= 1 and col_diff <= 1) asegura que la diferencia de filas y la de columnas sea menor a 1, esto significa que son adyacentes
        # (row_diff + col_diff != 0) asegura que no sean el mismo bloque, ya que un bloque con el mismo índice consigo mismo tendría una diferencia de filas y columnas de 0
        return (row_diff <= 1 and col_diff <= 1) and (row_diff + col_diff != 0)
