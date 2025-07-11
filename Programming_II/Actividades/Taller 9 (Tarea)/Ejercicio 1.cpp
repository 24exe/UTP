/*
Programación II
Profesor: Felipe Gutiérrez Isaza
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Vectores

Taller 9 (Tarea).

1. Inicialización Uniforme de Vector
Problema: Escribe un programa en C++ que cree un vector de enteros y lo inicialice con los
Números del 1 al 10 utilizando inicialización uniforme. Imprime el vector resultante.
Entrada: No aplicable.
Salida: Imprime los elementos del vector, separados por espacio.
*/

//BIBLIOTECAS
#include <iostream>
#include <vector>

using namespace std;


//PROTOTIPOS DE FUNCIÓNES AUX.
void data();


//FUN. DE PROCESO
void data(){
	cout<<"---INICIALIZACIÓN UNIFORME DE VECTOR---\n\n";
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




