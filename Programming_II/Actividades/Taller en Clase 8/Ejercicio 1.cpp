/*
Programación II
Profesor: Felipe Gutiérrez Isaza
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Strings.

Taller en clase 8.
1. Escribe un programa en C++ para invertir una cadena dada.
Ejemplo:
Ejemplo de entrada: w3resource
Ejemplo de Salida: ecruoser3w
*/



//BIBLIOTECAS
#include <iostream>
#include <string>

using namespace std;


//PROTOTIPOS DE FUNCIÓNES AUX.
void data();

//FUN. PARA PEDIR DATOS
void data(){
	cout<<"---INVERTIR PALABRA---\n\n";
	string cadena;
	cout<<"Ingrese una palabra: ";
	cin>>cadena;
	int largo = cadena.size();
	char temp;
	int mitad = largo/2;
	cout<<"La cadena ingresada es: "<<cadena<<endl;
	
	for (int i = 0; i < mitad; i++){
		temp = cadena[i];
		cadena[i] = cadena[largo - i - 1];
		cadena[largo - i - 1] = temp;
	}
	cout<<"La cadena invertida es: "<<cadena<<endl;
	//cout<<largo<<endl;
}


//FUN. PRINCIPAL
int main (){
	setlocale(LC_ALL, "spanish");
	data();
	system("pause");
	return 0;
}
