/*
Programación II
Profesor: Felipe Gutiérrez Isaza
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Funciones Secuenciales.

Taller en clase 6: Ejercicio 1.
*/

//BIBLIOTECAS
#include <iostream>


using namespace std;

//FUN. PRINCIPAL

int main (){
		setlocale(LC_ALL, "spanish");
	//para caracteres especiales en español, no es necesario añadir ninguna biblioteca.

	cout<<"---Ejercicio 1: Suma de Elementos---\n\n";
	
	int n;
	cout<<"Digite la cantidad de números que tendra el arreglo: ";
	cin>>n;
	int vector[n];
	int suma = 0;
	
	
	for (int i = 0; i < n; i++){
		cout<<"Ingrese el número "<<i+1<<" del arreglo: ";
		cin>>vector[i];
		suma = suma + vector[i]; 
	}
	
	cout<<"La suma de los números es: "<<suma<<endl;
	
	system ("pause");
	return 0;
}
