/*
Programaci�n II
Grupo: 5
Profesor: Felipe Guti�rrez Isaza
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Ciclos (Do-While)

Taller en clase 3: Ejercicio 1.
*/

//BIBLIOTECAS
#include <iostream>

using namespace std;

//FUN. PRINCIPAL
int main(){
	setlocale(LC_ALL, "spanish");
	//para caracteres especiales en espa�ol, no es necesario a�adir ninguna biblioteca.
	cout<<"---Ejercicio 1: Calculadora Simple(Modificada con Do-While y Switch)---\n\n";
	char i = 'N';
	do{
		float num1, num2;
		char op;
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
		cout<<"�Desea hacer otra operaci�n? (S/N)\n";
		cin>>i;
		cout<<endl;
		}while(i == 'S' or i == 's');
		
		if((i == 'S') or (i == 's') or (i == 'N') or (i == 'n')){
			cout<<"Gracias por usar nuestros servicios.\n";
		}
		else{
			cout<<"La calculadora se cerro debido a que ingreso un caracter erroneo.\n";			
		}
		system("pause");
		return 0;
		
}
	
	
