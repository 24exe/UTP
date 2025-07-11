/*
Programaci�n II
Profesor: Felipe Guti�rrez Isaza
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
	//para caracteres especiales en espa�ol, no es necesario a�adir ninguna biblioteca.

	cout<<"---Ejercicio 3: Duplicados en un Array---\n\n";
	
	int n;
	bool repetidos = false;
	cout<<"Digite la cantidad de n�meros que tendra el arreglo: ";
	cin>>n;
	int vector[n];
	
	//Ciclo para ingresar valores en el array.
	for (int i = 0; i < n; i++){
		cout<<"Ingrese el n�mero "<<i+1<<" del arreglo: ";
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
		cout<<"Hay n�meros repetidos.\n";
	}
	else{
		cout<<"No hay n�meros repetidos.\n";
	}
	
	
	system ("pause");
	return 0;
}
