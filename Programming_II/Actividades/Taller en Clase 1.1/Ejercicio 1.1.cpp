/*
Programación II
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
	//para caracteres especiales en español, no es necesario añadir ninguna biblioteca.


	float num1, num2;
	char op;
	cout<<"---Ejercicio 1: Calculadora Simple---\n";
	cout<<"Digite el primer número: ";
	cin>>num1;
	cout<<"Digite el segundo número: ";
	cin>>num2;
	cin.ignore(); //para limpiar el buffer de entrada.
	cout<<"Digite uno de los siguietes caracteres para realizar la operación correspondiente (+ - * /): \n";
	cin>>op;
	if (op =='+'){
		cout<<"la suma de los dos números es: "<<num1+num2<<".\n";
	}
	else if(op == '-'){
		cout<<"la resta de los dos números es: "<<num1-num2<<".\n";
	}
	else if(op == '*'){
		cout<<"la multiplicación de los dos números es: "<<num1*num2<<".\n";
	}
	else if(op == '/'){
		if(num2 == 0){
				cout<<"es imposible dividir por cero. \n";
			}
			else{
				cout<<"la división de los dos números es: "<<num1/num2<<".\n";
			}	
	}
	else{
		cout<<"ERROR EN EL USO DE LA CALCULADORA \n ";	
	}
	system("pause");
	return 0;
}

