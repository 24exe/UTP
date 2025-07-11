/*
Programaci�n II
Grupo: 5
Profesor: Felipe Guti�rrez Isaza
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Ciclos 

Taller en clase 5: Ejercicio 1.
*/

//BIBLIOTECAS
#include <iostream>
#include <iomanip> //Para la precisi�n de los decimales.

using namespace std;


//FUN. PRINCIPAL
int main (){
	
	float promedio, producto;
	
	setlocale(LC_ALL, "spanish");
	//para caracteres especiales en espa�ol, no es necesario a�adir ninguna biblioteca.
	
	
	cout<<"---Ejercicio 1: C�lculo de Promedio de Precios---\n\n";
	
	for(int i = 0; i < 5; i++){
		cout<<"Digite el precio del producto "<<i+1<<": ";
		cin>>producto;
		while (producto<0){
			cout<<"ERROR, el precio tiene que ser un n�mero entero positivo, digite el precio nuevamente: ";
			cin>>producto;
		}
		promedio = producto + promedio;
	}
	cout<<"El promedio de los precios es: "<<fixed<<setprecision(2)<<promedio<<"."<<endl;
	
	//fixed sirve para que el punto decimal no se mueva.	
	
	system ("pause");
	return 0;
}
