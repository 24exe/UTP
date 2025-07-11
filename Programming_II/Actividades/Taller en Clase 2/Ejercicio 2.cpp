/*
Programaci�n II
Grupo: 5
Profesor: Felipe Guti�rrez Isaza
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Switch

Taller en clase 2: Ejercicio 2.
*/

//bibliotecas
#include<iostream>

using namespace std;

//fun. principal 
int main(){
	setlocale(LC_ALL, "spanish");
	//para caracteres especiales en espa�ol, no es necesario a�adir ninguna biblioteca.
	cout<<"---Ejercicio 2: Estaciones---\n\n";
	int season;
	cout<<"Digite un n�mero(1-12): \n";
	cin>>season;
	switch(season){
		
		/*
		Or es incompatible con swtich:
		"...No se puede, se tiene que usar un valor constante (definido en tiempo de compilaci�n)."
		fuente: https://es.stackoverflow.com/questions/270800/se-puede-usar-un-or-%C3%B3-and-con-un-switch
		*/
		case 1:
		case 2:
		case 12:
			cout<<"Invierno\n";
		break;
		case 3:
		case 4:
		case 5:
			cout<<"Primavera\n";
		break;
		case 6:
		case 7:
		case 8:
			cout<<"Verano\n";
		break;
		case 9:
		case 10:
		case 11:
			cout<<"Oto�o\n";
		break;
		default:
			cout<<"ERROR, N�MERO INVALIDO. ";
			return 1;
	
	}
	
	system("pause");
	return 0;
}
