/*
Programaci�n II
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Nombre: David Rivas
Codigo: 1004685578
Nombre:	Maycol Becerra
Codigo: 1221714653
Tema: Funciones Secuenciales.


Taller en clase 1: Ejercicio 1.
*/

//bibliotecas
#include<iostream>

using namespace std;

//fun. principal 
int main (){
	setlocale(LC_ALL, "spanish");
	//para caracteres especiales en espa�ol, no es necesario a�adir ninguna biblioteca.


	float num1, num2;
	char op;
	cout<<"---Ejercicio 1: Calculadora Simple---\n";
	cout<<"Digite el primer n�mero: ";
	cin>>num1;
	cout<<"Digite el segundo n�mero: ";
	cin>>num2;
	cin.ignore(); //para limpiar el buffer de entrada.
	cout<<"Digite uno de los siguietes caracteres para realizar la operaci�n correspondiente (+ - * /): \n";
	cin>>op;
	switch(op){
		case '+':
			cout<<"la suma de los dos n�meros es: "<<num1+num2<<".\n";
		break;
		case '-':
			cout<<"la resta de los dos n�meros es: "<<num1-num2<<".\n";
		break;
		case '*':
			cout<<"la multiplicaci�n de los dos n�meros es: "<<num1*num2<<".\n";
		break;
		case '/':
			if(num2 == 0){
				cout<<"es imposible dividir por cero. ";
			}
			else{
				cout<<"la divisi�n de los dos n�meros es: "<<num1/num2<<".\n";
			}	
		break;
		default:
			cout<<"ERROR EN EL USO DE LA CALCULADORA \n ";
		break;
		}
	system("pause");
	return 0;
}

