/*
Programación II
Profesor: Felipe Gutiérrez Isaza
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Strings.

Taller en clase 8.
4. Escribe un programa en C++ para encontrar la palabra más grande en una
cadena dada.
Ejemplo:
Ejemplo Entrada: C++ es un lenguaje de programación de propósito general.
Ejemplo de salida: programación
*/



//BIBLIOTECAS
#include <iostream>
#include <string>

using namespace std;

//PROTOTIPOS DE FUNCIÓNES AUX.
void data();

//FUN. PARA PEDIR DATOS
void data(){
	cout<<"---PALABRA MAS LARGA EN UNA FRASE---\n\n";
	string cadena;
	cout<<"Ingrese una frase: ";
	getline(cin, cadena);
	int largo = cadena.size();
	string palabra;
	string palabraFinal;
	int largoPalabra = palabra.size()
	int largoPalabraFinal =
	}
	int j = 0
	for (int i = 0; i < largo; i++){
		while(cadena[i] != ' '){
			palabra[j] == cadena[i]
			i++;
			j++;
		}
		
	}
	
	
	
	
	
	
	
	
	int longitudPalabra = 0;
	int posicion = 0;
	string cadenaAux1;
	string cadenaFinal;
	int largo = cadena.size();
	
	for(int i = 0; i < largo; i++){
		posicion = i;
		while(cadena[i] != ' '){
			longitudPalabra++;
			i++;
		}
		cadenaAux1 = cadena.substr(posicion, longitudPalabra);
		int largoAux = cadenaAux1.size();
		int largoFinal = cadenaFinal.size();
		if (largoAux > largoFinal){
			cadenaFinal = cadenaAux1;
		}
		
	}
	cout<<"Palabra mas larga de la frase: "<<endl;
	cout<<cadena<<endl;
}


//FUN. PRINCIPAL
int main (){
	setlocale(LC_ALL, "spanish");
	data();
	system("pause");
	return 0;
}
