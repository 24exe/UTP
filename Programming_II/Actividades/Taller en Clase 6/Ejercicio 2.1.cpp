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
#include <climits>


using namespace std;

//FUN. PRINCIPAL

int main (){
		setlocale(LC_ALL, "spanish");
	//para caracteres especiales en español, no es necesario añadir ninguna biblioteca.

	cout<<"---Ejercicio 2: Encontrar el Mínimo y el Máximo---\n\n";
	
	int n;
	cout<<"Digite la cantidad de números que tendra el arreglo: ";
	cin>>n;
	while(n<0){
		cout<<"ERROR, la cantidad de números que debe tener el arreglo tiene que ser positiva. \n\n";
		cout<<"Digite la cantidad de números que tendra el arreglo nuevamente: ";
		cin>>n;
	}
	int vector[n];
	int max = INT_MIN, min;
	/*
	INT_MIN Define el valor mínimo que puede contener un int, esta constante pertenece a las bibliotecas
	limits.h o climits.
	https://www.geeksforgeeks.org/int_max-int_min-cc-applications/
	.
	*/
	for (int i = 0; i < n; i++){
		cout<<"Ingrese el número "<<i+1<<" del arreglo: ";
		cin>>vector[i];
	}
	for (int i = 0; i < n; i++){
		if(max<vector[i]){
			max = vector[i];
		}
	}

	min = max ;//inicializamos la variable
	for (int i = 0; i < n; i++){
		if(min > vector[i]){
			min = vector[i];
		}
	}
	
	
	
	cout<<"El número máximo es: "<<max<<endl;
	cout<<"El número mínimo es: "<<min<<endl;
	
	
	system ("pause");
	return 0;
}
