/*
Programación II
Profesor: Felipe Gutiérrez Isaza
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Recursividad.

Taller en clase 7: Ejercicio 4.

*/

//BIBLIOTECAS
#include <iostream>
#include <climits>

using namespace std;

//VAR. GLOBALES
int filas;
int columnas;
int matriz[100][100];

//PROTOTIPOS DE FUNCIÓNES AUX.
void mat();
void data();
int maximo(int mat, int f, int c, int max);
int minimo(int mat, int f, int c, int min);

//FUN. PARA PEDIR MATRIZ
void mat(){
	int resultado;
	
	cout<<"Ingrese el número de filas de la matriz: ";
	cin>>filas;
	while(filas<0){
		cout<<"Error, ingrese un número mayor a 0: ";
		cin>>filas;
	}
	cout<<"Ingrese el número de columnas de la matriz: ";
	cin>>columnas;
	while(columnas<0){
		cout<<"Error, ingrese un número mayor a 0: ";
		cin>>columnas;
	}
	
	system ("cls");			//limpiar la pantalla
}



//FUN. PARA PEDIR VALORES E IMPRIMIR MATRIZ
void data(){	
	cout<<"Ingrese los elementos de la matriz: "<<endl;
	
	for(int i = 0; i < filas; i++){
		for(int j = 0; j < columnas; j++){
			cout<<"["<<i<<"]["<<j<<"] = ";
			cin>>matriz[i][j];
		}
	}
	
	system ("cls");
	cout<<"Matriz: \n\n";
	for(int i = 0; i < filas; i++){
		for(int j = 0; j < columnas; j++){
			cout<<matriz[i][j]<<" ";
		}
		cout<<endl;
	}
}

//FUN. RECURSIVA PARA ENCONTRAR EL MAXIMO DE UNA MATRIZ
int maximo(int matriz[][100], int f, int c, int max) {
	//Caso Base.
    if (f == filas)
        return max;
    if (c == columnas)
        return maximo(matriz, f+1, 0, max);
    if (matriz[f][c] > max)
        max = matriz[f][c];
    return maximo(matriz, f, c+1, max);
}
// Función recursiva para encontrar el mínimo de la matriz
int minimo(int matriz[][100], int f, int c, int min) {
    if (f == filas)
        return min;
    if (c == columnas)
        return minimo(matriz, f+1, 0, min);
    if (matriz[f][c] < min)
        min = matriz[f][c];
    return minimo(matriz, f, c + 1, min);
}  

//FUN. PRINCIPAL
int main(){
	setlocale(LC_ALL, "spanish");
	cout<<"---ENCONTRAR MAX Y MIN DE UNA MATRIZ (RECURSIVIDAD)---\n\n";
	mat();
	data();
	
	int maxMat = maximo(matriz, 0, 0, INT_MIN);
    int minMat = minimo(matriz, 0, 0, INT_MAX);
    cout << "El máximo de la matriz es: " << maxMat << endl;
    cout << "El mínimo de la matriz es: " << minMat << endl;
	system ("pause");
	return 0;
}


