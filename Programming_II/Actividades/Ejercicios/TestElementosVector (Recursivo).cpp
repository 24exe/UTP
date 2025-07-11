#include<iostream>

using namespace std;

// Función recursiva para calcular la suma de los elementos en la matriz
int sumaMatriz(int matriz[][100], int fila, int columna) {
    // Caso base: Si la fila y la columna son negativas, retornar 0
    if (fila < 0 || columna < 0) {
        return 0;
    }
    // Caso recursivo: Sumar el elemento actual y llamar recursivamente para el subproblema con la fila y columna anteriores
    else {
        int suma = matriz[fila][columna];
        // Llamada recursiva para el elemento anterior en la fila y columna
        suma += sumaMatriz(matriz, fila - 1, columna);
        suma += sumaMatriz(matriz, fila, columna - 1);
        // Restar el elemento anterior en la fila y columna para evitar duplicar la suma
        suma -= sumaMatriz(matriz, fila - 1, columna - 1);
        return suma;
    }
}

int main() {
    int N, M;
    cin >> N >> M;

    int matriz[100][100];

    // Entrada de la matriz
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            cin >> matriz[i][j];
        }
    }

    // Llamada a la función recursiva para obtener la suma de los elementos en la matriz
    int resultado = sumaMatriz(matriz, N - 1, M - 1);

    // Salida del resultado
    cout << resultado << endl;

    return 0;
}
