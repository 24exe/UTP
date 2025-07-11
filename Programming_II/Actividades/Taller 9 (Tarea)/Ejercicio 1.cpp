/*
Programaci�n II
Profesor: Felipe Guti�rrez Isaza
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Vectores

Taller 9 (Tarea).

1. Inicializaci�n Uniforme de Vector
Problema: Escribe un programa en C++ que cree un vector de enteros y lo inicialice con los
N�meros del 1 al 10 utilizando inicializaci�n uniforme. Imprime el vector resultante.
Entrada: No aplicable.
Salida: Imprime los elementos del vector, separados por espacio.
*/

//BIBLIOTECAS
#include <iostream>
#include <vector>

using namespace std;


//PROTOTIPOS DE FUNCI�NES AUX.
void data();


//FUN. DE PROCESO
void data(){
	cout<<"---INICIALIZACI�N UNIFORME DE VECTOR---\n\n";
	//contenedor vector
	vector<int> nums(10);
	//ciclo para rellenar contenedor
	for(int i = 0; i < 10; i++){
		nums[i] = i+1;
	}
	cout<<"Elementos del Vector: \n";
	//ciclo para mostrar contenedor
	for(int i = 0; i < 10;  i++ ){
		cout<<nums[i]<<" ";
	}
	cout<<endl;
}

int main(){
	setlocale(LC_ALL, "spanish");
	data();
	
	system ("pause");
	return 0;
}




