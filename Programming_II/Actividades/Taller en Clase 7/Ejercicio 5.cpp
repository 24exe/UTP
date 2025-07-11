/*
Programación II
Profesor: Felipe Gutiérrez Isaza
Nombre: Carlos Eduardo Grisales Restrepo
Codigo: 1055750849
Tema: Recursividad.

Taller en clase 7: Ejercicio 5.

*/

//BIBLIOTECAS
#include <iostream>
#include <string.h> //para funciones de cadenas  de caracteres


using namespace std;

//VAR. GLOBALES
char vector[25];
int longitud = 0;
//PROTOTIPOS DE FUNCIÓNES AUX.
void data();
void invertircadena (char vec[25], int i);


//FUN. AUX PARA PEDIR DATOS
void data(){
	cout<<"Ingrese una palabra : ";
	cin>>vector;
	cout<<"La palabra ingresada es: "<<vector<<endl;
	
	longitud = strlen(vector);
	
	//cout<<"la longitud del vector es: "<<longitud<<endl;
}

void invertircadena (char vec[25],int i){	
	if(i < 0){
		cout<<endl;
	}
	else{
	cout<<vec[i];
	invertircadena(vec, i-1);
	}
}


//FUN. PRINCIPAL
int main (){
	setlocale(LC_ALL, "spanish");
	cout<<"---INVERTIR UNA CADENA(RECURSIVIDAD)---\n\n";
	data();
	
	cout<<"Palabra original: "<<vector<<endl;
    cout<<"Palabra al revés: ";
    invertircadena(vector,longitud);
	system ("pause");
	return 0;
}
