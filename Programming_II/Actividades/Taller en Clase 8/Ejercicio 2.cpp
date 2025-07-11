/*
Programación II
Profesor: Felipe Gutiérrez Isaza
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Strings.

Taller en clase 8.
2. Escribe un programa en C++ para cambiar cada letra de una cadena dada por la
letra que le sigue en el alfabeto (es decir, a se convierte en b, p se convierte en q, z
se convierte en a).
Ejemplo:
Ejemplo de entrada: w3resource
Ejemplo de salida: x3sftpvsdf
*/



//BIBLIOTECAS
#include <iostream>
#include <string>

using namespace std;

//PROTOTIPOS DE FUNCIÓNES AUX.
void data();

//FUN. PARA PEDIR DATOS
void data(){
	cout<<"---CAMBIAR CADA LETRA DE UNA CADENA---\n\n";
	string cadena;
	cout<<"Ingrese una palabra: ";
	cin>>cadena;
	cout<<"Cadena ingresada: "<<endl;
	cout<<cadena<<endl;
	int largo = cadena.size();
	for(int i = 0; i < largo; i++){
		if((cadena[i] > 64 and cadena[i] <91) or (cadena[i] > 96 and cadena[i] <123)){
			cadena[i] = cadena[i]+1;
		} 
	}
	cout<<"Cadena con letras cambiadas por la siguiente: "<<endl;
	cout<<cadena<<endl;
}


//FUN. PRINCIPAL
int main (){
	setlocale(LC_ALL, "spanish");
	data();
	system("pause");
	return 0;
}
