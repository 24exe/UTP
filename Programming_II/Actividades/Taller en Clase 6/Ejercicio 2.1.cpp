/*
Programaci�n II
Profesor: Felipe Guti�rrez Isaza
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
	//para caracteres especiales en espa�ol, no es necesario a�adir ninguna biblioteca.

	cout<<"---Ejercicio 2: Encontrar el M�nimo y el M�ximo---\n\n";
	
	int n;
	cout<<"Digite la cantidad de n�meros que tendra el arreglo: ";
	cin>>n;
	while(n<0){
		cout<<"ERROR, la cantidad de n�meros que debe tener el arreglo tiene que ser positiva. \n\n";
		cout<<"Digite la cantidad de n�meros que tendra el arreglo nuevamente: ";
		cin>>n;
	}
	int vector[n];
	int max = INT_MIN, min;
	/*
	INT_MIN Define el valor m�nimo que puede contener un int, esta constante pertenece a las bibliotecas
	limits.h o climits.
	https://www.geeksforgeeks.org/int_max-int_min-cc-applications/
	.
	*/
	for (int i = 0; i < n; i++){
		cout<<"Ingrese el n�mero "<<i+1<<" del arreglo: ";
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
	
	
	
	cout<<"El n�mero m�ximo es: "<<max<<endl;
	cout<<"El n�mero m�nimo es: "<<min<<endl;
	
	
	system ("pause");
	return 0;
}
