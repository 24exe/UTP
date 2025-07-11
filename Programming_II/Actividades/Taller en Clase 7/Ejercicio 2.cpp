/*
Programación II
Profesor: Felipe Gutiérrez Isaza
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Recursividad.

Taller en clase 7: Ejercicio 2.

*/

//BIBLIOTECAS
#include <iostream>

using namespace std;

//VAR. GLOBALES
int x= 0;
int y= 1; 
int z= 1;
int n;

//PROTOTIPOS DE FUNCIÓNES AUX.
void data();
int fibonacci(int i);


//FUN. PARA PEDIR EL N. A BUSCAR
void data(){
	cout<<"Ingrese el número de la serie de Fibonacci que desea encontrar: ";
	cin>>n;
	while(n>45 or n<0){
		cout<<"Error, ingrese un número que este entre 0 y 45: ";
		cin>>n;
	}
}

//FUN. RECURSIVA PARA ENCONTRAR EL NUM. DE FIBONNACCI.
int fibonacci(int i){
	//Caso Base.
	if(i<2){
		return i;
	}
	//Caso Recursivo.
	else{
		return fibonacci(i-1) + fibonacci(i-2);
	}
}

//FUN. PRINCIPAL
int main(){
	setlocale(LC_ALL, "spanish");
	cout<<"---OBTENCIÓN DEL ENÉSIMO NÚMERO DE FIBONACCI (RECURSIVIDAD)---\n\n";
	data();
	int resultado = fibonacci(n);
	cout<<"El número "<<n<<" de la serie de Fibonacci es: "<<resultado<<endl;
	
	
	
	system("pause");
	return 0;
}
