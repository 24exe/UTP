/*
Programación II
Profesor: Felipe Gutiérrez Isaza
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Funciones Secuenciales.

Taller en clase 6: Ejercicio 3.
*/

//BIBLIOTECAS
#include <iostream>


using namespace std;

//FUN. PRINCIPAL
int main (){
		setlocale(LC_ALL, "spanish");
	//para caracteres especiales en español, no es necesario añadir ninguna biblioteca.

	cout<<"---Ejercicio 3: Duplicados en un Array---\n\n";
	
	int n;
	bool repetidos = false;
	cout<<"Digite la cantidad de números que tendra el arreglo: ";
	cin>>n;
	int vector[n];
	
	//Ciclo para ingresar valores en el array.
	for (int i = 0; i < n; i++){
		cout<<"Ingrese el número "<<i+1<<" del arreglo: ";
		cin>>vector[i];
		}
		
	for(int i = 0; i < n ; i++){
		for(int j = i+1; j < n; j++)
		if (vector[i] == vector[j]){
			repetidos = true;
			break;
		}
	}

	if(repetidos == true){
		cout<<"Hay números repetidos.\n";
	}
	else{
		cout<<"No hay números repetidos.\n";
	}
	
	
	system ("pause");
	return 0;
}
