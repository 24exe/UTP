

//BIBLIOTECAS
#include <iostream>

using namespace std;


//VAR. GLOBALES
int f;
int c;
int matriz[100][100];

int sumaElementos = 0;


//PROTOTIPOS DE FUNCIÓNES AUX.
void mat();
void data();
void sumaMatriz(int matriz,int i, int j);




//FUN. PARA PEDIR MATRIZ
void mat(){
	int resultado;
	
	cout<<"Ingrese el número de filas de la matriz: ";
	cin>>f;
	cout<<"Ingrese el número de columnas de la matriz: ";
	cin>>c;
	//Ingreso de valores del vector
	
	system ("cls");			//limpiar la pantalla
}

//FUN. PARA PEDIR VALORES E IMPRIMIR MATRIZ
void data(){	
	cout<<"Ingrese los elementos de la matriz: "<<endl;
	
	for(int i = 0; i < f; i++){
		for(int j = 0; j < c; j++){
			cout<<"["<<i<<"]["<<j<<"] = ";
			cin>>matriz[i][j];
		}
	}
	
	system ("cls");
	cout<<"Matriz: \n\n";
	for(int i = 0; i < f; i++){
		for(int j = 0; j < c; j++){
			cout<<matriz[i][j]<<" ";
		}
		cout<<endl;
	}
	
	
}

// FUN. RECURSIVA PARA CALCULAR LA SUMA DE LOS ELEMENTOS DE LA MATRIZ
int sumaMatriz(int matriz[][100], int fila, int columna) {
    // Caso base
    if (fila < 0 or columna < 0) {
        return 0;
    }
    // Caso recursivo.
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



//FUN. PRINCIPAL
int main(){
	setlocale(LC_ALL, "spanish");
	mat();
	data();
	int resultado = sumaMatriz(matriz, f - 1, c - 1);
	cout <<"Suma de elementos de la matriz: "<<resultado<<endl;
	//cout<<"La suma de los elementos de la matriz es: "<<sumaElementos<<endl;
	system ("pause");
	return 0;
}
