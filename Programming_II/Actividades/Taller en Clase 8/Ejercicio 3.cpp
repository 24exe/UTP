/*
Programación II
Profesor: Felipe Gutiérrez Isaza
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Strings.

Taller en clase 8.
3. Escriba un programa en C++ para escribir en mayúsculas la primera letra de cada
palabra de una cadena dada. Las palabras deben estar separadas por un solo
espacio.
Ejemplo:
Ejemplo de entrada: cpp cadena ejercicios
Ejemplo de salida: Ejercicios de cadenas cpp
*/



//BIBLIOTECAS
#include <iostream>
#include <string>

using namespace std;

//PROTOTIPOS DE FUNCIÓNES AUX.
void data();

//FUN. PARA PEDIR DATOS
void data(){
	cout<<"---MAYÚSCULAS EN LA PRIMERA LETRA DE CADA FRASE---\n\n";
	string cadena;
	cout<<"Ingrese una frase: ";
	getline(cin, cadena);
	cout<<"Frase ingresada: "<<endl;
	cout<<cadena<<endl;
	int largo = cadena.size();
	for(int i = 0; i < largo; i++){
		if((cadena[0] > 96 and cadena[0] <123)){
			cadena[0] = cadena[0]-32;
		}
		if(cadena[i] == ' '){
			if((cadena[i+1] > 96 and cadena[i+1] <123)){
			cadena[i+1] = cadena[i+1]-32;
			} 
		}
		
	}
	cout<<"Frase con primera letra mayuscula: "<<endl;
	cout<<cadena<<endl;
}


//FUN. PRINCIPAL
int main (){
	setlocale(LC_ALL, "spanish");
	data();
	system("pause");
	return 0;
}
