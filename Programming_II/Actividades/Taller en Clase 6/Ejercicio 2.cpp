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


using namespace std;

//FUN. PRINCIPAL

int main (){
		setlocale(LC_ALL, "spanish");
	//para caracteres especiales en espa�ol, no es necesario a�adir ninguna biblioteca.

	cout<<"---Ejercicio 2: Encontrar el M�nimo y el M�ximo---\n\n";
	
	int n;
	cout<<"Digite la cantidad de n�meros que tendra el arreglo: ";
	cin>>n;
	int vector[n];
	int min = vector[0];
	int max = vector[0];
	for (int i = 0; i < n; i++){
		cout<<"Ingrese el n�mero "<<i+1<<" del arreglo: ";
		cin>>vector[i];
		if(vector[i]>max){
			max = vector[i];
		}
		if(vector[i]<min){
			min = vector[i];
		}
	}
	
	cout<<"El n�mero m�ximo es: "<<max<<endl;
	cout<<"El n�mero m�nimo es: "<<min<<endl;
	
	
	system ("pause");
	return 0;
}
