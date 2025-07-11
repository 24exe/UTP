/*
Programación II
Profesor: Felipe Gutiérrez Isaza
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Funciones Secuenciales.

Taller en clase 6: Ejercicio 2.
*/

//BIBLIOTECAS
#include <iostream>


using namespace std;

//FUN. PRINCIPAL

int main (){
		setlocale(LC_ALL, "spanish");
	//para caracteres especiales en español, no es necesario añadir ninguna biblioteca.

	cout<<"---Ejercicio 2: Encontrar el Mínimo y el Máximo---\n\n";
	
	int n;
	cout<<"Digite la cantidad de números que tendra el arreglo: ";
	cin>>n;
	int vector[n];
	int min = vector[0];
	int max = vector[0];
	for (int i = 0; i < n; i++){
		cout<<"Ingrese el número "<<i+1<<" del arreglo: ";
		cin>>vector[i];
		if(vector[i]>max){
			max = vector[i];
		}
		if(vector[i]<min){
			min = vector[i];
		}
	}
	
	cout<<"El número máximo es: "<<max<<endl;
	cout<<"El número mínimo es: "<<min<<endl;
	
	
	system ("pause");
	return 0;
}
