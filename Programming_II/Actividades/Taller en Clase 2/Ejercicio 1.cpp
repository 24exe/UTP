/*
Programaci�n II
Grupo: 5
Profesor: Felipe Guti�rrez Isaza
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Switch

Taller en clase 2: Ejercicio 1.
*/

//bibliotecas
#include<iostream>

using namespace std;

//fun. principal 
int main(){
	setlocale(LC_ALL, "spanish");
	//para caracteres especiales en espa�ol, no es necesario a�adir ninguna biblioteca.
	cout<<"---Ejercicio 1: Dia de la Semana---\n\n";
	int dia;
	cout<<"Digite un n�mero: ";
	cin>>dia;
	switch(dia){
		case 1:
			cout<<"Lunes\n";
		break;
		case 2:
			cout<<"Martes\n";
		break;
		case 3:
			cout<<"Miercoles\n";
		break;
		case 4:
			cout<<"Jueves\n";
		break;
		case 5:
			cout<<"Viernes\n";
		break;
		case 6:
			cout<<"S�bado\n";
		break;
		case 7:
			cout<<"Domingo\n";
		break;
		default:
			cout<<"ERROR, N�MERO INVALIDO. ";
			return 1;
	
	}
	
	
	
	system("pause");
	return 0;
}
